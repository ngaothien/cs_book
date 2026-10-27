# Problems


<!-- PAGE 326 -->
$\bullet$  Avoiding small pivots: partial pivoting; complete pivoting. $\bullet$  Gaussian elimination of tridiagonal matrices. $\bullet$  LU-factorization of tridiagonal matrices. $\bullet$  Symmetric positive definite matrices $(SPD$ matrices). $\bullet$  Cholesky factorization (Theorem 8.10). $\bullet$  Criteria for a symmetric matrix to be positive definite; Sylvester’s criterion. $\bullet$  Reduced row echelon form. $\bullet$  Reduction of a rectangular matrix to its row echelon form. $\bullet$  Using the reduction to row echelon form to decide whether a system Ax $= b$ is solvable, and to find its solutions, using a special solution and a basis of the homogeneous system Ax $= 0. \bullet$  Magic squares. $\bullet$  Transvections and dilatations.

## 8.17 Problems

Problem 8.1. Solve the following linear systems by Gaussian elimination:
$$\begin{pmatrix} 2 & 3 & 1 \\ 1 & 2 & -1 \\ 3 & 5 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 6 \\ 2 \\ 7 \end{pmatrix} , \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 6 \\ 9 \\ 14 \end{pmatrix} .$$
$$---$$
Problem 8.2. Solve the following linear system by Gaussian elimination:
$$\begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 4 & 0 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 7 \\ 14 \\ -1 \\ 2 \end{pmatrix} .$$
$$--$$
Problem 8.3. Consider the matrix
$$A = \begin{pmatrix} 1 & c & 0 \\ 2 & 4 & 1 \\ 3 & 5 & 1 \end{pmatrix} .$$
When applying Gaussian elimination, which value of $c$ yields zero in the second pivot position? Which value of $c$ yields zero in the third pivot position? In this case, what can you say about the matrix $A$?

<!-- PAGE 327 -->
Problem 8.4. Solve the system
$$\begin{pmatrix} 2 & 1 & 1 & 0 \\ 4 & 3 & 3 & 1 \\ 8 & 7 & 9 & 5 \\ 6 & 7 & 9 & 8 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ -1 \\ 1 \end{pmatrix}$$
using the LU-factorization of Example 8.1.
Problem 8.5. Apply rref to the matrix
$$A_{2} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 3 & 0 \end{pmatrix} .$$
$$--$$
Problem 8.6. Apply rref to the matrix
$$\begin{pmatrix} 1 & 4 & 9 & 16 \\ 4 & 9 & 16 & 25 \\ 9 & 16 & 25 & 36 \\ 16 & 25 & 36 & 49 \end{pmatrix} .$$
Problem 8.7. $(1)$ Prove that the dimension of the subspace of $2 \times  2$ matrices $A$, such that the sum of the entries of every row is the same (say $c_{1})$ and the sum of entries of every column is the same (say $c_{2})$ is $2$.
$(2)$ Prove that the dimension of the subspace of $2 \times  2$ matrices $A$, such that the sum of the entries of every row is the same (say $c_{1})$, the sum of entries of every column is the same (say $c_{2})$, and $c_{1} = c_{2}$ is also $2$. Prove that every such matrix is of the form
$$\begin{pmatrix} a & b \\ b & a \end{pmatrix} ,$$
and give a basis for this subspace.
$(3)$ Prove that the dimension of the subspace of $3 \times  3$ matrices $A$, such that the sum of the entries of every row is the same (say $c_{1})$, the sum of entries of every column is the same (say $c_{2})$, and $c_{1} = c_{2}$ is $5$. Begin by showing that the above constraints are given by the set of equations
$$\begin{pmatrix} 1 & 1 & 1 & -1 & -1 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 & 1 & -1 & -1 & -1 \\ 1 & -1 & 0 & 1 & -1 & 0 & 1 & -1 & 0 \\ 0 & 1 & -1 & 0 & 1 & -1 & 0 & 1 & -1 \\ 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} \\ a_{12} \\ a_{13} \\ a_{21} \\ a_{22} \\ a_{23} \\ a_{31} \\ a_{32} \\ a_{33} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} .$$
$$--$$

<!-- PAGE 328 -->
Prove that every matrix satisfying the above constraints is of the form
$$\begin{pmatrix} a + b -c & -a + c + e & -b + c + d \\ -a -b + c + d + e & a & b \\ c & d & e \end{pmatrix} ,$$
with a, $b, c, d, e \in \mathbb{R}$. Find a basis for this subspace. (Use the method to find a basis for the kernel of a matrix).
Problem 8.8. If $A$ is an $n \times  n$ matrix and $B$ is any $n \times  n$ invertible matrix, prove that $A$ is symmetric positive definite iff $B^{\top}AB$ is symmetric positive definite.
Problem 8.9. $(1)$ Consider the matrix
$$A_{4} = \begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
$$-$$
Find three matrices of the form $E_{2,1;\beta1}, E_{3,2;\beta2}, E_{4,3;\beta3}$, such that
$$E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}A_{4} = U_{4}$$
where $U_{4}$ is an upper triangular matrix. Compute
$$M = E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}$$
and check that
$$MA_{4} = U_{4} = \begin{pmatrix} 2 & -1 & 0 & 0 \\ 0 & 3/2 & -1 & 0 \\ 0 & 0 & 4/3 & -1 \\ 0 & 0 & 0 & 5/4 \end{pmatrix} .$$
$(2)$ Now consider the matrix
$$A_{5} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 \\ 0 & -1 & 2 & -1 & 0 \\ 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & 1 & 2 \end{pmatrix} .$$
$$-$$
Find four matrices of the form $E_{2,1;\beta1}, E_{3,2;\beta2}, E_{4,3;\beta3}, E_{5,4;\beta4}$, such that
$$E_{5,4;\beta4}E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}A_{5} = U_{5}$$
where $U_{5}$ is an upper triangular matrix. Compute
$$M = E_{5,4;\beta4}E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}$$

<!-- PAGE 329 -->
and check that
$$MA_{5} = U_{5} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 \\ 0 & 0 & 0 & 5/4 & -1 \\ 0 & 0 & 0 & 0 & 6/5 \end{pmatrix} .$$
$(3)$ Write a Matlab program defining the function Ematrix(n, $i, j, b)$ which is the $n \times  n$ matrix that adds $b$ times row $j$ to row $i$. Also write some Matlab code that produces an $n \times  n$ matrix $A_{n}$ generalizing the matrices $A_{4}$ and $A_{5}$. Use your program to figure out which five matrices $E_{i,j;\beta}$ reduce $A_{6}$ to the upper triangular matrix
$$U_{6} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & -1 \\ 0 & 0 & 0 & 0 & 0 & 7/6 \end{pmatrix} .$$
Also use your program to figure out which six matrices $E_{i,j;\beta}$ reduce $A_{7}$ to the upper triangular matrix
$$U_{7} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & -1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 7/6 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 8/7 \end{pmatrix} .$$
$(4)$ Find the lower triangular matrices $L_{6}$ and $L_{7}$ such that
$$L_{6}U_{6} = A_{6}$$
and
$$L_{7}U_{7} = A_{7}.$$
$(5)$ It is natural to conjecture that there are $n -1$ matrices of the form $E_{i,j;\beta}$ that reduce $A_{n}$ to the upper triangular matrix
$$U_{n} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & \ddots & \vdots \\ \vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\ 0 & 0 & 0 & 0 & 0 & (n + 1)/n \end{pmatrix} ,$$
$$\cdots$$

<!-- PAGE 330 -->
namely,
$$E_{2,1;1/2}, E_{3,2;2/3}, E_{4,3;3/4}, \cdots  , E_{n,n-1;(n-1)/n}.$$
It is also natural to conjecture that the lower triangular matrix $L_{n}$ such that
$$L_{n}U_{n} = A_{n}$$
is given by
$$L_{n} = E_{2,1;-1/2}E_{3,2;-2/3}E_{4,3;-3/4} \cdots  E_{n,n-1;-(n-1)/n},$$
that is,
$$L_{n} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ -1/2 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & -2/3 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & -3/4 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -4/5 & 1 & \ddots & \vdots \\ \vdots & \vdots & \vdots & \vdots & \ddots & \ddots & 0 \\ 0 & 0 & 0 & 0 & (n & 1)/n & 1 \end{pmatrix} .$$
$$\cdots - -$$
Prove the above conjectures.
$(6)$ Prove that the last column of $A_{n}^{-1}$ is
$$\begin{pmatrix} 1/(n + 1) \\ 2/(n + 1) \\ \vdots \\ n/(n + 1) \end{pmatrix} .$$
Problem 8.10. $(1)$ Let $A$ be any invertible $2 \times  2$ matrix
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} .$$
Prove that there is an invertible matrix $S$ such that
$$SA = \begin{pmatrix} 1 & 0 \\ 0 & ad -bc \end{pmatrix} ,$$
where $S$ is the product of at most four elementary matrices of the form $E_{i,j;\beta}$. Conclude that every matrix $A$ in SL(2) (the group of invertible $2 \times  2$ matrices $A$ with det(A) $= +1)$ is the product of at most four elementary matrices of the form $E_{i,j;\beta}$. For any $a \neq  0, 1$, give an explicit factorization as above for
$$A = \begin{pmatrix} a & 0 \\ 0 & a^{-1} \end{pmatrix} .$$

<!-- PAGE 331 -->
What is this decomposition for $a = -1$?
$(2)$ Recall that a rotation matrix $R$ (a member of the group SO(2)) is a matrix of the form
$$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
Prove that if $\theta  \neq  k\pi$  (with $k \in \mathbb{Z})$, any rotation matrix can be written as a product
$$R = ULU,$$
where $U$ is upper triangular and $L$ is lower triangular of the form
$$U = \begin{pmatrix} 1 & u \\ 0 & 1 \end{pmatrix} ,L = \begin{pmatrix} 1 & 0 \\ v & 1 \end{pmatrix} .$$
Therefore, every plane rotation (except a flip about the origin when $\theta  = \pi$ ) can be written as the composition of three shear transformations!
Problem 8.11. $(1)$ Recall that $E_{i,d}$ is the diagonal matrix
$$E_{i,d} = \mathrm{diag}(1, \dots  , 1, d, 1, \dots  , 1),$$
whose diagonal entries are all $+1$, except the $(i$, i)th entry which is equal to $d$. Given any $n \times  n$ matrix $A$, for any pair $(i, j)$ of distinct row indices $(1 \le i, j \le n)$, prove that there exist two elementary matrices $E_{1}(i, j)$ and $E_{2}(i, j)$ of the form $E_{k,\ell;\beta}$, such that
$$E_{j,-1}E_{1}(i, j)E_{2}(i, j)E_{1}(i, j)A = P(i, j)A,$$
the matrix obtained from the matrix $A$ by permuting row $i$ and row $j$. Equivalently, we have
$$E_{1}(i, j)E_{2}(i, j)E_{1}(i, j)A = E_{j,-1}P(i, j)A,$$
the matrix obtained from $A$ by permuting row $i$ and row $j$ and multiplying row $j$ by $-1$. Prove that for every $i = 2, \dots  , n$, there exist four elementary matrices $E_{3}(i, d), E_{4}(i, d), E_{5}(i, d), E_{6}(i, d)$ of the form $E_{k,\ell;\beta}$, such that
$$E_{6}(i, d)E_{5}(i, d)E_{4}(i, d)E_{3}(i, d)E_{n,d} = E_{i,d}.$$
What happens when $d = -1$, that is, what kind of simplifications occur? Prove that all permutation matrices can be written as products of elementary operations of the form $E_{k,\ell;\beta}$ and the operation $E_{n,-1}$.
$(2)$ Prove that for every invertible $n \times  n$ matrix $A$, there is a matrix $S$ such that
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & d \end{pmatrix} = E_{n,d},$$

<!-- PAGE 332 -->
with $d =$ det(A), and where $S$ is a product of elementary matrices of the form $E_{k,\ell;\beta}$. In particular, every matrix in SL(n) (the group of invertible $n \times  n$ matrices $A$ with det(A) $= +1)$ can be written as a product of elementary matrices of the form $E_{k,\ell;\beta}$. Prove that at most n(n $+ 1)$ - $2$ such transformations are needed.
$(3)$ Prove that every matrix in SL(n) can be written as a product of at most $(n$ - $1)(max{n, 3} + 1)$ elementary matrices of the form $E_{k,\ell;\beta}$.
Problem 8.12. A matrix $A$ is called strictly column diagonally dominant iff
$$|a_{j j}| > \sum_{=1, i\neq j}^{n}  |a_{i j}|,for j = 1, \dots  , n.$$
$$i$$
Prove that if $A$ is strictly column diagonally dominant, then Gaussian elimination with partial pivoting does not require pivoting, and $A$ is invertible.
Problem 8.13. $(1)$ Find a lower triangular matrix $E$ such that
$$E \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 2 & 1 \end{pmatrix} .$$
$(2)$ What is the effect of the product (on the left) with
$$E_{4,3;-1}E_{3,2;-1}E_{4,3;-1}E_{2,1;-1}E_{3,2;-1}E_{4,3;-1}$$
on the matrix
$$Pa_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} .$$
$(3)$ Find the inverse of the matrix $Pa_{3}$.
$(4)$ Consider the $(n + 1) \times  (n + 1)$ Pascal matrix $Pa_{n}$ whose ith row is given by the binomial coefficients
$$\begin{pmatrix} i -1 \\ j -1 \end{pmatrix} ,$$
with $1 \le i \le n + 1, 1 \le j \le n + 1$, and with the usual convention that
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} = 1, \begin{pmatrix} i \\ j \end{pmatrix} = 0ifj > i.$$

<!-- PAGE 333 -->
The matrix $Pa_{3}$ is shown in Part $(3)$ and $Pa_{4}$ is shown below:
$$Pa_{4} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 & 0 \\ 1 & 2 & 1 & 0 & 0 \\ 1 & 3 & 3 & 1 & 0 \\ 1 & 4 & 6 & 4 & 1 \end{pmatrix} .$$
Find $n$ elementary matrices $E_{ik,jk;\beta k}$ such that
$$E_{in,jn;\beta n} \cdots  E_{i1,j1;\beta1}Pa_{n} = \begin{pmatrix} 1 & 0 \\ 0 & Pa_{n-1} \end{pmatrix} .$$
Use the above to prove that the inverse of $Pa_{n}$ is the lower triangular matrix whose ith row is given by the signed binomial coefficients
$$(-1)^{i+j-2} \begin{pmatrix} i -1 \\ j -1 \end{pmatrix} = (-1)^{i+j} \begin{pmatrix} i -1 \\ j -1 \end{pmatrix} ,$$
with $1 \le i \le n + 1, 1 \le j \le n + 1$. For example,
$$Pa_{4}^{-1}= \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 & 0 \\ 1 & -2 & 1 & 0 & 0 \\ -1 & 3 & -3 & 1 & 0 \\ 1 & 4 & 6 & 4 & 1 \end{pmatrix} .$$
$$--$$
Hint. Given any $n \times  n$ matrix $A$, multiplying $A$ by the elementary matrix $E_{i,j;\beta}$ on the right yields the matrix $AE_{i,j;\beta}$ in which $\beta$  times the ith column is added to the jth column.
Problem 8.14. $(1)$ Implement the method for converting a rectangular matrix to reduced row echelon form in Matlab.
$(2)$ Use the above method to find the inverse of an invertible $n \times  n$ matrix $A$ by applying it to the the $n \times$  2n matrix $[A$ I] obtained by adding the $n$ columns of the identity matrix to $A$.
$(3)$ Consider the matrix
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & \cdots & n \\ 2 & 3 & 4 & 5 & \cdots & n + 1 \\ 3 & 4 & 5 & 6 & \cdots & n + 2 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ n & n + 1 & n + 2 & n + 3 & \cdots & 2n -1 \end{pmatrix} .$$
Using your program, find the row reduced echelon form of $A$ for $n = 4, \dots  , 20$.

<!-- PAGE 334 -->
Also run the Matlab rref function and compare results. Your program probably disagrees with rref even for small values of $n$. The problem is that some pivots are very small and the normalization step (to make the pivot $1)$ causes roundofferrors. Use a tolerance parameter to fix this problem. What can you conjecture about the rank of $A$?
$(4)$ Prove that the matrix $A$ has the following row reduced form:
$$R = \begin{pmatrix} 1 & 0 & -1 & -2 & \cdots & -(n -2) \\ 0 & 1 & 2 & 3 & \cdots & n -1 \\ 0 & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & 0 \end{pmatrix} .$$
Deduce from the above that $A$ has rank $2$. Hint. Some well chosen sequence of row operations.
$(5)$ Use your program to show that if you add any number greater than or equal to $(2/25)n^{2}$ to every diagonal entry of $A$ you get an invertible matrix! In fact, running the Matlab function chol should tell you that these matrices are SPD (symmetric, positive definite).
Problem 8.15. Let $A$ be an $n \times  n$ complex Hermitian positive definite matrix. Prove that the lower-triangular matrix $B$ with positive diagonal entries such that $A = BB^{*}$ is given by the following formulae: For $j = 1, \dots  , n$,
$$1/2$$
$$!$$
$$b_{j j} =a_{j j} - \sum_{k=1}^{j-1}  |b_{j k}|^{2},$$
and for $i = j + 1, \dots  , n$ (and $j = 1, \dots  , n$ - $1)$
$$!$$
$$\overline{b}_{i j} =a_{i j} - \sum_{k=1}^{j-1}  b_{i k}\overline{b}_{j k}/b_{j j}.$$
Problem 8.16. (Permutations and permutation matrices) $A$ permutation can be viewed as an operation permuting the rows of a matrix. For example, the permutation
$$\begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 4 & 2 & 1 \end{pmatrix}$$
corresponds to the matrix
$$P_{\pi} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} .$$

<!-- PAGE 335 -->
Observe that the matrix $P_{\pi}$ has a single $1$ on every row and every column, all other entries being zero, and that if we multiply any $4 \times  4$ matrix $A$ by $P_{\pi}$ on the left, then the rows of $A$ are permuted according to the permutation $\pi$ ; that is, the $\pi$ (i)th row of $P_{\pi}A$ is the ith row of $A$. For example,
$$P_{\pi}A = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} = \begin{pmatrix} a_{41} & a_{42} & a_{43} & a_{44} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \end{pmatrix} .$$
Equivalently, the ith row of $P_{\pi}A$ is the $\pi^{-1}$ (i)th row of $A$. In order for the matrix $P_{\pi}$ to move the ith row of $A$ to the $\pi$ (i)th row, the $\pi$ (i)th row of $P_{\pi}$ must have a $1$ in column $i$ and zeros everywhere else; this means that the ith column of $P_{\pi}$ contains the basis vector $e_{\pi(i)}$, the vector that has a $1$ in position $\pi (i)$ and zeros everywhere else. This is the general situation and it leads to the following definition.

> **Definition 8.10.** Given any permutation $\pi$ : $[n] \to [n]$, the permutation matrix $P_{\pi} = (p_{ij})$ representing $\pi$  is the matrix given by
$$($$
$$1if i = \pi (j)$$
$$p_{ij} =$$
$$0if i \neq  \pi (j);$$
equivalently, the jth column of $P_{\pi}$ is the basis vector $e_{\pi(j)}$. A permutation matrix $P$ is any matrix of the form $P_{\pi}$ (where $P$ is an $n \times  n$ matrix, and $\pi$ : $[n] \to [n]$ is a permutation, for some $n \ge 1)$.
Remark: There is a confusing point about the notation for permutation matrices. A permutation matrix $P$ acts on a matrix $A$ by multiplication on the left by permuting the rows of $A$. As we said before, this means that the $\pi$ (i)th row of $P_{\pi}A$ is the ith row of $A$, or equivalently that the ith row of $P_{\pi}A$ is the $\pi^{-1}$ (i)th row of $A$. But then observe that the row index of the entries of the ith row of $PA$ is $\pi^{-1} (i)$, and not $\pi (i)$! See the following example:
$$\begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} = \begin{pmatrix} a_{41} & a_{42} & a_{43} & a_{44} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \end{pmatrix} ,$$
where
$$\pi^{-1} (1) = 4$$
$$\pi^{-1} (2) = 3$$
$$\pi^{-1} (3) = 1$$
$$\pi^{-1} (4) = 2.$$
Prove the following results

<!-- PAGE 336 -->
$(1)$ Given any two permutations $\pi_{1} , \pi_{2}$  : $[n] \to [n]$, the permutation matrix $P_{\pi2\circ\pi1}$ representing the composition of $\pi_{1}$  and $\pi_{2}$  is equal to the product $P_{\pi2}P_{\pi1}$ of the permutation matrices $P_{\pi1}$ and $P_{\pi2}$ representing $\pi_{1}$  and $\pi_{2}$ ; that is,
$$P_{\pi2\circ\pi1} = P_{\pi2}P_{\pi1}.$$
$(2)$ The matrix $P_{\pi-1}$ representing the inverse of the permutation $\pi_{1}$  is the inverse $P_{\pi1}^{-1}$  of the matrix $P_{\pi1}^{1}$ representing the permutation $\pi_{1}$ ; that is,
$$P_{\pi-1}= P_{\pi1}^{-1}  .$$
$$1$$
Furthermore,
$$P_{\pi1}^{-1}  = (P_{\pi1})^{\top}.$$
$(3)$ Prove that if $P$ is the matrix associated with a transposition, then det(P) $= -1$.
$(4)$ Prove that if $P$ is a permutation matrix, then det(P) $= \pm 1$.
$(5)$ Use permutation matrices to give another proof of the fact that the parity of the number of transpositions used to express a permutation $\pi$  depends only on $\pi$ .
