# RREF, Free Variables, Homogeneous Systems


<!-- PAGE 307 -->

## 8.11 RREF, Free Variables, and Homogenous Linear

$$Systems$$
Given a system of the form Ax $= b$, we can apply the reduction procedure to the augmented matrix $(A, b)$ to obtain a reduced row echelon matrix (A', b') such that the system A'x $=$ b' has the same solutions as the original system Ax $= b$. The advantage of the reduced system A'x $=$ b' is that there is a simple test to check whether this system is solvable, and to find its solutions if it is solvable. Indeed, if any row of the matrix A' is zero and if the corresponding entry in b' is nonzero, then it is a pivot and we have the “equation”
$$0 = 1,$$
which means that the system A'x $=$ b' has no solution. On the other hand, if there is no pivot in b', then for every row $i$ in which $b_{i}'$ ̸ $= 0$, there is some column $j$ in A' where the entry on row $i$ is $1$ (a pivot). Consequently, we can assign arbitrary values to the variable $x_{k}$ if column $k$ does not contain a pivot, and then solve for the pivot variables. For example, if we consider the reduced row echelon matrix
$$(A', b') = \begin{pmatrix} 1 & 6 & 0 & 1 & 0 \\ 0 & 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
there is no solution to A'x $=$ b' because the third equation is $0 = 1$. On the other hand, the reduced system
$$(A', b') = \begin{pmatrix} 1 & 6 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
has solutions. We can pick the variables $x_{2}, x_{4}$ corresponding to nonpivot columns arbitrarily, and then solve for $x_{3}$ (using the second equation) and $x_{1}$ (using the first equation). The above reasoning proves the following theorem:

> **Theorem 8.16.** Given any system Ax $= b$ where $A$ is a $m \times  n$ matrix, if the augmented matrix $(A, b)$ is a reduced row echelon matrix, then the system Ax $= b$ has a solution iff there is no pivot in $b$. In that case, an arbitrary value can be assigned to the variable $x_{j}$ if column $j$ does not contain a pivot.

> **Definition 8.7.** Nonpivot variables are often called free variables. Putting Proposition 8.14 and Theorem 8.16 together we obtain a criterion to decide whether a system Ax $= b$ has a solution: Convert the augmented system $(A, b)$ to a row reduced echelon matrix (A', b') and check whether b' has no pivot.

<!-- PAGE 308 -->
Remark: When writing a program implementing row reduction, we may stop when the last column of the matrix $A$ is reached. In this case, the test whether the system Ax $= b$ is solvable is that the row-reduced matrix A' has no zero row of index $i > r$ such that $b_{i}'$ ̸ $= 0$ (where $r$ is the number of pivots, and b' is the row-reduced right-hand side). If we have a homogeneous system Ax $= 0$, which means that $b = 0$, of course $x = 0$ is always a solution, but Theorem 8.16 implies that if the system Ax $= 0$ has more variables than equations, then it has some nonzero solution (we call it a nontrivial solution).

> **Proposition 8.17.** Given any homogeneous system Ax $= 0$ of $m$ equations in $n$ variables,
$$\mathbb{R}^{n}$$
if $m < n$, then there is a nonzero vector $x \in$ such that Ax $= 0$.

*Proof.* Convert the matrix $A$ to a reduced row echelon matrix A'. We know that Ax $= 0$ iff A'x $= 0$. If $r$ is the number of pivots of A', we must have $r \le m$, so by Theorem 8.16 we may assign arbitrary values to $n$ - $r > 0$ nonpivot variables and we get nontrivial solutions. Theorem 8.16 can also be used to characterize when a square matrix is invertible. First, note the following simple but important fact: If a square $n \times  n$ matrix $A$ is a row reduced echelon matrix, then either $A$ is the identity or the bottom row of $A$ is zero.

> **Proposition 8.18.** Let $A$ be a square matrix of dimension $n$. The following conditions are equivalent:
(a) The matrix $A$ can be reduced to the identity by a sequence of elementary row operations.
$(b)$ The matrix $A$ is a product of elementary matrices.
$(c)$ The matrix $A$ is invertible.
$(d)$ The system of homogeneous equations Ax $= 0$ has only the trivial solution $x = 0$.

*Proof.* First we prove that (a) implies $(b)$. If (a) can be reduced to the identity by a sequence of row operations $E_{1}, \dots  , E_{p}$, this means that $E_{p} \cdots  E_{1}A =$ I. Since each $E_{i}$ is invertible, we get
$$A = E_{1}^{-1}\cdots  E_{p}^{-1} ,$$
where each $E_{i}^{-1}$ is also an elementary row operation, so $(b)$ holds. Now if $(b)$ holds, since elementary row operations are invertible, $A$ is invertible and $(c)$ holds. If $A$ is invertible, we already observed that the homogeneous system Ax $= 0$ has only the trivial solution $x = 0$, because from Ax $= 0$, we get $A^{-1}Ax = A^{-1}0$; that is, $x = 0$. It remains to prove that $(d)$ implies (a) and for this we prove the contrapositive: if (a) does not hold, then $(d)$ does not hold. Using our basic observation about reducing square matrices, if $A$ does not reduce to the identity, then $A$ reduces to a row echelon matrix A' whose bottom row is zero. Say A' $= PA$,

<!-- PAGE 309 -->
where $P$ is a product of elementary row operations. Because the bottom row of A' is zero, the system A'x $= 0$ has at most $n$ - $1$ nontrivial equations, and by Proposition 8.17, this system has a nontrivial solution $x$. But then, Ax $= P^{-1}$ A'x $= 0$ with $x \neq  0$, contradicting the fact that the system Ax $= 0$ is assumed to have only the trivial solution. Therefore, $(d)$ implies (a) and the proof is complete. Proposition 8.18 yields a method for computing the inverse of an invertible matrix $A$: reduce $A$ to the identity using elementary row operations, obtaining
$$E_{p} \cdots  E_{1}A = I.$$
Multiplying both sides by $A^{-1}$ we get
$$A^{-1}= E_{p} \cdots  E_{1}.$$
From a practical point of view, we can build up the product $E_{p} \cdots  E_{1}$ by reducing to row echelon form the augmented $n \times$  2n matrix $(A, I_{n})$ obtained by adding the $n$ columns of the identity matrix to $A$. This is just another way of performing the Gauss–Jordan procedure. Here is an example: let us find the inverse of the matrix
$$A = \begin{pmatrix} 5 & 4 \\ 6 & 5 \end{pmatrix} .$$
We form the $2 \times  4$ block matrix
$$(A, I) = \begin{pmatrix} 5 & 4 & 1 & 0 \\ 6 & 5 & 0 & 1 \end{pmatrix}$$
and apply elementary row operations to reduce $A$ to the identity. For example:
$$(A, I) = \begin{pmatrix} 5 & 4 & 1 & 0 \\ 6 & 5 & 0 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 5 & 4 & 1 & 0 \\ 1 & 1 & -1 & 1 \end{pmatrix}$$
by subtracting row $1$ from row $2$,
$$\begin{pmatrix} 5 & 4 & 1 & 0 \\ 1 & 1 & -1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 5 & -4 \\ 1 & 1 & -1 & 1 \end{pmatrix}$$
by subtracting $4 \times$  row $2$ from row $1$,
$$\begin{pmatrix} 1 & 0 & 5 & -4 \\ 1 & 1 & -1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 5 & -4 \\ 0 & 1 & -6 & 5 \end{pmatrix} = (I, A^{-1}),$$
by subtracting row $1$ from row $2$. Thus
$$A^{-1}= \begin{pmatrix} 5 & -4 \\ -6 & 5 \end{pmatrix} .$$
Proposition 8.18 can also be used to give an elementary proof of the fact that if a square matrix $A$ has a left inverse $B$ (resp. a right inverse $B)$, so that $BA =$ I (resp. $AB =$ I), then $A$ is invertible and $A^{-1} = B$. This is an interesting exercise, try it!
