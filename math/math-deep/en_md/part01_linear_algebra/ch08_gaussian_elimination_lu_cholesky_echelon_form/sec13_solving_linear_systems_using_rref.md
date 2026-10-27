# Solving Linear Systems Using RREF


<!-- PAGE 312 -->

## 8.13 Solving Linear Systems Using RREF

First we have the following simple result.
$$\mathbb{R}^{m}$$

> **Proposition 8.20.** Let $A$ be any $m \times  n$ matrix and let $b \in$ be any vector. If the system Ax $= b$ has a solution, then the set $Z$ of all solutions of this system is the set
$$Z = x_{0} + \mathrm{Ker} (A) = {x_{0} + x | Ax = 0},$$
$$\mathbb{R}^{n}$$
where $x_{0} \in$ is any solution of the system Ax $= b$, which means that $Ax_{0} = b (x_{0}$ is called
$$\mathbb{R}^{n}$$
a special solution or a particular solution), and where Ker $(A) = {x \in$ | Ax $= 0}$, the set of solutions of the homogeneous system associated with Ax $= b$.

*Proof.* Assume that the system Ax $= b$ is solvable and let $x_{0}$ and $x_{1}$ be any two solutions so that $Ax_{0} = b$ and $Ax_{1} = b$. Subtracting the first equation from the second, we get
$$A(x_{1} -x_{0}) = 0,$$
which means that $x_{1}$ - $x_{0} \in$ Ker $(A)$. Therefore, $Z \subseteq x_{0} +$ Ker $(A)$, where $x_{0}$ is a special solution of Ax $= b$. Conversely, if $Ax_{0} = b$, then for any $z \in$ Ker $(A)$, we have Az $= 0$, and so
$$A(x_{0} + z) = Ax_{0} + Az = b + 0 = b,$$
which shows that $x_{0} +$ Ker $(A) \subseteq Z$. Therefore, $Z = x_{0} +$ Ker $(A)$. Given a linear system Ax $= b$, reduce the augmented matrix $(A, b)$ to its row echelon form (A', b'). As we showed before, the system Ax $= b$ has a solution iff b' contains no pivot. Assume that this is the case. Then, if (A', b') has $r$ pivots, which means that A' has $r$ pivots since b' has no pivot, we know that the first $r$ columns of $I_{m}$ appear in A'. We can permute the columns of A' and renumber the variables in $x$ correspondingly so that the first $r$ columns of $I_{m}$ match the first $r$ columns of A', and then our reduced echelon matrix is of the form $(R$, b') with
$$R = \begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix}$$
and
$$b'= \begin{pmatrix} d \\ 0_{m-r} \end{pmatrix} ,$$
where $F$ is a $r \times  (n$ - $r)$ matrix and $d \in \mathbb{R}^{r}$. Note that $R$ has $m$ - $r$ zero rows. Then because
$$\begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix} = \begin{pmatrix} d \\ 0_{m-r} \end{pmatrix} = b',$$

<!-- PAGE 313 -->
we see that
$$x_{0} = \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix}$$
is a special solution of Rx $=$ b', and thus to Ax $= b$. In other words, we get a special solution by assigning the first $r$ components of b' to the pivot variables and setting the nonpivot variables (the free variables) to zero. Here is an example of the preceding construction taken from Kumpel and Thorpe $[110]$. The linear system
$$x_{1} -x_{2} + x_{3} + x_{4} -2x_{5} = -1$$
$$-2x_{1} + 2x_{2} -x_{3} + x_{5} = 2$$
$$x_{1} -x_{2} + 2x_{3} + 3x_{4} -5x_{5} = -1,$$
is represented by the augmented matrix
$$(A, b) = \begin{pmatrix} 1 & -1 & 1 & 1 & -2 & -1 \\ -2 & 2 & -1 & 0 & 1 & 2 \\ 1 & 1 & 2 & 3 & 5 & 1 \end{pmatrix} ,$$
$$---$$
where $A$ is a $3 \times  5$ matrix. The reader should find that the row echelon form of this system is
$$(A', b') = \begin{pmatrix} 1 & -1 & 0 & -1 & 1 & -1 \\ 0 & 0 & 1 & 2 & -3 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} .$$
The $3 \times  5$ matrix A' has rank $2$. We permute the second and third columns (which is equivalent to interchanging variables $x_{2}$ and $x_{3})$ to form
$$R = \begin{pmatrix} I_{2} & F \\ 0_{1,2} & 0_{1,3} \end{pmatrix} ,F = \begin{pmatrix} -1 & -1 & 1 \\ 0 & 2 & -3 \end{pmatrix} .$$
Then a special solution to this linear system is given by
$$x_{0} = \begin{pmatrix} d \\ 0_{3} \end{pmatrix} = \begin{pmatrix} -1 \\ 0 \\ 0_{3} \end{pmatrix} .$$
We can also find a basis of the kernel (nullspace) of $A$ using $F$. If $x = (u, v)$ is in the
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
kernel of $A$, with $u \in$ and $v \in$ , then $x$ is also in the kernel of $R$, which means that Rx $= 0$; that is,
$$\begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} u + Fv \\ 0_{m-r} \end{pmatrix} = \begin{pmatrix} 0_{r} \\ 0_{m-r} \end{pmatrix} .$$
Therefore, $u =$ -Fv, and Ker $(A)$ consists of all vectors of the form
$$\begin{pmatrix} -Fv \\ v \end{pmatrix} = \begin{pmatrix} -F \\ I_{n-r} \end{pmatrix} v,$$

<!-- PAGE 314 -->
for any arbitrary $v \in \mathbb{R}^{n-r}$. It follows that the $n$ - $r$ columns of the matrix
$$N = \begin{pmatrix} -F \\ I_{n-r} \end{pmatrix}$$
form a basis of the kernel of $A$. This is because $N$ contains the identity matrix $I_{n-r}$ as a submatrix, so the columns of $N$ are linearly independent. In summary, if $N^{1}, \dots  , N^{n-r}$ are the columns of $N$, then the general solution of the equation Ax $= b$ is given by
$$x = \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix} + x_{r+1}N^{1}+ \cdots  + x_{n}N^{n-r},$$
where $x_{r+1}, \dots  , x_{n}$ are the free variables; that is, the nonpivot variables. Going back to our example from Kumpel and Thorpe $[110]$, we see that
$$N = \begin{pmatrix} -F \\ I_{3} \end{pmatrix} = \begin{pmatrix} 1 & 1 & -1 \\ 0 & -2 & 3 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} .$$
Since earlier we permuted the second and the third column, row $2$ and row $3$ need to be swapped so the general solution in terms of the original variables is given by
$$x = \begin{pmatrix} -1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} + x_{3} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + x_{4} \begin{pmatrix} 1 \\ 0 \\ -2 \\ 1 \\ 0 \end{pmatrix} + x_{5} \begin{pmatrix} -1 \\ 0 \\ 3 \\ 0 \\ 1 \end{pmatrix} .$$
In the general case where the columns corresponding to pivots are mixed with the columns corresponding to free variables, we find the special solution as follows. Let $i_{1} < \cdots  < i_{r}$ be the indices of the columns corresponding to pivots. Assign $b_{k}'$ to the pivot variable $x_{ik}$ for $k = 1, \dots  , r$, and set all other variables to $0$. To find a basis of the kernel, we form the $n$ - $r$ vectors $N^{k}$ obtained as follows. Let $j_{1} < \cdots  < j_{n-r}$ be the indices of the columns corresponding to free variables. For every column $j_{k}$ corresponding to a free variable $(1 \le k \le n -r)$, form the vector $N^{k}$ defined so that the entries $N_{i}^{k}, \dots  , N_{i}^{k}$ are equal to the negatives of the first $r$ entries in column $j_{k}$ (flip the sign of $these^{1} entries);^{r}$ let $N_{jk}^{k}  = 1$, and set all other entries to zero. Schematically, if the column of index $j_{k}$ (corresponding to the free variable $x_{jk})$ is
$$\begin{pmatrix} \alpha_{1} \\ \vdots \\ \alpha_{r} \\ 0 \\ \vdots \\ 0 \end{pmatrix} ,$$

<!-- PAGE 315 -->
then the vector $N^{k}$ is given by
$$1$$
$$\vdots$$
$$i_{1} -1$$
$$i_{1}$$
$$i_{1} + 1$$
$$\vdots$$
$$i_{r} -1 \begin{pmatrix} 0 \\ \vdots \\ 0 \\ -\alpha_{1} \\ 0 \\ \vdots \\ 0 \\ -\alpha_{r} \\ 0 \\ \vdots \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$
$$i_{r}.$$
$$i_{r} + 1$$
$$\vdots$$
$$j_{k} -1$$
$$j_{k}$$
$$j_{k} + 1$$
$$\vdots$$
$$n$$
The presence of the $1$ in position $j_{k}$ guarantees that $N^{1}, \dots  , N^{n-r}$ are linearly independent. As an illustration of the above method, consider the problem of finding a basis of the subspace $V$ of $n \times  n$ matrices $A \in M_{n}(\mathbb{R})$ satisfying the following properties: $1$. The sum of the entries in every row has the same value (say $c_{1}); 2$. The sum of the entries in every column has the same value (say $c_{2})$. It turns out that $c_{1} = c_{2}$ and that the 2n-2 equations corresponding to the above conditions are linearly independent. We leave the proof of these facts as an interesting exercise. It can be shown using the duality theorem (Theorem 11.4) that the dimension of the space $V$ of matrices satisying the above equations is $n^{2}$ - (2n - $2)$. Let us consider the case $n = 4$. There are $6$ equations, and the space $V$ has dimension $10$. The equations are
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0,$$

<!-- PAGE 316 -->
and the corresponding matrix is
$$A = \begin{pmatrix} 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\ 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$----$$
The result of performing the reduction to row echelon form yields the following matrix in rref:
$$U = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & -1 & -1 & -1 & 0 & -1 & -1 & -1 & 2 & 1 & 1 & 1 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & -1 & 0 & -1 & -1 \\ 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & -1 & -1 & 0 & -1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & -1 & -1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & -1 & -1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{pmatrix}$$
$$----$$
The list pivlist of indices of the pivot variables and the list freelist of indices of the free variables is given by
$$pivlist = (1, 2, 3, 4, 5, 9),$$
$$freelist = (6, 7, 8, 10, 11, 12, 13, 14, 15, 16).$$
After applying the algorithm to find a basis of the kernel of $U$, we find the following $16 \times  10$ matrix
$$BK = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & -2 & -1 & -1 & -1 \\ -1 & 0 & 0 & -1 & 0 & 0 & 1 & 0 & 1 & 1 \\ 0 & -1 & 0 & 0 & -1 & 0 & 1 & 1 & 0 & 1 \\ 0 & 0 & -1 & 0 & 0 & -1 & 1 & 1 & 1 & 0 \\ -1 & -1 & -1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 & -1 & -1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
The reader should check that that in each column $j$ of $BK$, the lowest bold $1$ belongs to the row whose index is the jth element in freelist, and that in each column $j$ of $BK$, the

<!-- PAGE 317 -->
signs of the entries whose indices belong to pivlist are the flipped signs of the $6$ entries in the column $U$ corresponding to the jth index in freelist. We can now read offfrom BK the $4 \times  4$ matrices that form a basis of $V$ : every column of $BK$ corresponds to a matrix whose rows have been concatenated. We get the following $10$ matrices:
$$M_{1} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{2} = \begin{pmatrix} 1 & 0 & -1 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{3} = \begin{pmatrix} 1 & 0 & 0 & -1 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
$$M_{4} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{5} = \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{6} = \begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
$$M_{7} =,M_{8} = \begin{pmatrix} -1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} ,M_{9} = \begin{pmatrix} -1 & 1 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} ,$$
$$\begin{pmatrix} -2 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ -1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$
$M_{10} =$ . Recall that a magic square is a square matrix that satisfies the two conditions about the sum of the entries in each row and in each column to be the same number, and also the additional two constraints that the main descending and the main ascending diagonals add up to this common number. Furthermore, the entries are also required to be positive integers. For $n = 4$, the additional two equations are
$$a_{22} + a_{33} + a_{44} -a_{12} -a_{13} -a_{14} = 0$$
$$a_{41} + a_{32} + a_{23} -a_{11} -a_{12} -a_{13} = 0,$$
and the $8$ equations stating that a matrix is a magic square are linearly independent. Again, by running row elimination, we get a basis of the “generalized magic squares” whose entries are not restricted to be positive integers. We find a basis of $8$ matrices. For $n = 3$, we find a basis of $3$ matrices. A magic square is said to be normal if its entries are precisely the integers $1, 2 \dots  , n^{2}$. Then since the sum of these entries is
$$1 + 2 + 3 + \cdots  + n^{2}= \frac{n^{2}(n^{2} + 1)}{2} ,$$
