# Matrices


<!-- PAGE 95 -->

## 3.6 Matrices

In Section 2.1 we introduced informally the notion of a matrix. In this section we define matrices precisely, and also introduce some operations on matrices. It turns out that matrices form a vector space equipped with a multiplication operation which is associative, but noncommutative. We will explain in Section 4.1 how matrices can be used to represent linear maps, defined in the next section.

> **Definition 3.12.** If $K =\mathbb{R}$ or $K =\mathbb{C}$, an $m\times n$-matrix over $K$ is a family $(a_{i j})_{1\le i\le m,1\le j\le n}$ of scalars in $K$, represented by an array
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix}$$
In the special case where $m = 1$, we have a row vector, represented by
$$(a_{1 1} \cdots  a_{1n})$$
and in the special case where $n = 1$, we have a column vector, represented by
$$\begin{pmatrix} a_{1 1} \\ \vdots \\ a_{m1} \end{pmatrix} .$$
In these last two cases, we usually omit the constant index $1$ (first index in case of a row, second index in case of a column). The set of all $m \times n$-matrices is denoted by $M_{m,n}(K)$ or $M_{m,n}$. An $n \times n$-matrix is called a square matrix of dimension $n$. The set of all square matrices of dimension $n$ is denoted by $M_{n}(K)$, or $M_{n}$.
Remark: As defined, a matrix $A = (a_{i j})_{1\le i\le m,1\le j\le n}$ is a family, that is, a function from ${1, 2, \dots  , m} \times  {1, 2, \dots  , n}$ to $K$. As such, there is no reason to assume an ordering on the indices. Thus, the matrix $A$ can be represented in many different ways as an array, by adopting different orders for the rows or the columns. However, it is customary (and usually convenient) to assume the natural ordering on the sets ${1, 2, \dots  , m}$ and ${1, 2, \dots  , n}$, and to represent $A$ as an array according to this ordering of the rows and columns. We define some operations on matrices as follows.

<!-- PAGE 96 -->

> **Definition 3.13.** Given two $m \times  n$ matrices $A = (a_{i j})$ and $B = (b_{i j})$, we define their sum $A + B$ as the matrix $C = (c_{i j})$ such that $c_{i j} = a_{i j} + b_{i j}$; that is,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} + \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1n} \\ b_{2 1} & b_{2 2} & \dots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2} & \dots & b_{m n} \end{pmatrix}$$
$$= \begin{pmatrix} a_{1 1} + b_{1 1} & a_{1 2} + b_{1 2} & \dots & a_{1n} + b_{1n} \\ a_{2 1} + b_{2 1} & a_{2 2} + b_{2 2} & \dots & a_{2n} + b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} + b_{m1} & a_{m2} + b_{m2} & \dots & a_{m n} + b_{m n} \end{pmatrix} .$$
For any matrix $A = (a_{i j})$, we let $-A$ be the matrix $(-a_{i j})$. Given a scalar $\lambda  \in K$, we define the matrix $\lambda A$ as the matrix $C = (c_{i j})$ such that $c_{i j} = \lambda a_{i j}$; that is
$$\lambda \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} = \begin{pmatrix} \lambda a_{1 1} & \lambda a_{1 2} & \dots & \lambda a_{1n} \\ \lambda a_{2 1} & \lambda a_{2 2} & \dots & \lambda a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \lambda a_{m1} & \lambda a_{m2} & \dots & \lambda a_{m n} \end{pmatrix} .$$
Given an $m \times  n$ matrices $A = (a_{i k})$ and an $n \times  p$ matrices $B = (b_{k j})$, we define their product $AB$ as the $m \times  p$ matrix $C = (c_{i j})$ such that
$$c_{i j} = \sum_{k=1}^{n}  a_{i k}b_{k j},$$
for $1 \le i \le m$, and $1 \le j \le p$. In the product $AB = C$ shown below
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1p} \\ b_{2 1} & b_{2 2} & \dots & b_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{n p} \end{pmatrix} = \begin{pmatrix} c_{1 1} & c_{1 2} & \dots & c_{1p} \\ c_{2 1} & c_{2 2} & \dots & c_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ c_{m1} & c_{m2} & \dots & c_{m p} \end{pmatrix} ,$$
note that the entry of index $i$ and $j$ of the matrix $AB$ obtained by multiplying the matrices $A$ and $B$ can be identified with the product of the row matrix corresponding to the $i$-th row of $A$ with the column matrix corresponding to the j-column of $B$:
$$(a_{i1} \cdots  a_{i n}) \begin{pmatrix} b_{1j} \\ \vdots \\ b_{n j} \end{pmatrix} = \sum_{k=1}^{n}  a_{i k}b_{k j}.$$

<!-- PAGE 97 -->

> **Definition 3.14.** The square matrix $I_{n}$ of dimension $n$ containing $1$ on the diagonal and $0$ everywhere else is called the identity matrix. It is denoted by
$$I_{n} = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix}$$

> **Definition 3.15.** Given an $m \times  n$ matrix $A = (a_{i j})$, its transpose $A^{\top} = (a_{j i}^{\top})$, is the $n \times m$-matrix such that $a_{j i}^{\top} = a_{i j}$, for all $i, 1 \le i \le m$, and all $j, 1 \le j \le n$. The transpose of a matrix $A$ is sometimes denoted by $A^{t}$, or even by $^{t}$ A. Note that the transpose $A^{\top}$ of a matrix $A$ has the property that the $j$-th row of $A^{\top}$ is the $j$-th column of $A$. In other words, transposition exchanges the rows and the columns of a matrix. Here is an example. If $A$ is the $5 \times  6$ matrix
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 7 & 1 & 2 & 3 & 4 & 5 \\ 8 & 7 & 1 & 2 & 3 & 4 \\ 9 & 8 & 7 & 1 & 2 & 3 \\ 10 & 9 & 8 & 7 & 1 & 2 \end{pmatrix} ,$$
then $A^{\top}$ is the $6 \times  5$ matrix
$$A^{\top}= \begin{pmatrix} 1 & 7 & 8 & 9 & 10 \\ 2 & 1 & 7 & 8 & 9 \\ 3 & 2 & 1 & 7 & 8 \\ 4 & 3 & 2 & 1 & 7 \\ 5 & 4 & 3 & 2 & 1 \\ 6 & 5 & 4 & 3 & 2 \end{pmatrix} .$$
The following observation will be useful later on when we discuss the SVD. Given any $m \times  n$ matrix $A$ and any $n \times  p$ matrix $B$, if we denote the columns of $A$ by $A^{1}, \dots  , A^{n}$ and the rows of $B$ by $B_{1}, \dots  , B_{n}$, then we have
$$AB = A^{1}B_{1} + \cdots  + A^{n}B_{n}.$$
For every square matrix $A$ of dimension $n$, it is immediately verified that $AI_{n} = I_{n}A = A$.
Remark: If $C$ is an $n \times  1$ matrix (a column vector) and $R$ is a $1 \times  n$ matrix (a row vector), then the $n \times  n$ matrix $CR$ is sometimes called an outer product.

> **Definition 3.16.** For any square matrix $A$ of dimension $n$, if a matrix $B$ such that $AB = BA = I_{n}$ exists, then it is unique, and it is called the inverse of $A$. The matrix $B$ is also denoted by $A^{-1}$. An invertible matrix is also called a nonsingular matrix, and a matrix that is not invertible is called a singular matrix.

<!-- PAGE 98 -->
The following result is a matrix analog of Proposition 3.23.

> **Proposition 3.15.** If a square matrix $A \in M_{n}(K)$ has a left inverse, that is a matrix $B$ such that $BA = I_{n}$, or a right inverse, that is a matrix $C$ such that $AC = I_{n}$, then $A$ is actually invertible. Furthermore, $B = A^{-1}$ and $C = A^{-1}$.

*Proof.* Proposition 3.15 follows from Proposition 3.23 and the fact that matrices represent linear maps. We can also give a direct proof as follows. Suppose that there is a matrix $B$ such that $BA = I_{n}$. This implies that the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly independent, because if
$$A\lambda  = \lambda_{1} A^{1}+ \cdots  + \lambda_{n} A^{n}= 0,$$
where $\lambda  \in K^{n}$ is the column vector
$$\lambda  = \begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{n} \end{pmatrix} ,$$
for some $\lambda_{1} , \dots  , \lambda_{n}  \in K$, by multiplying both sides of the equation $A\lambda  = 0$ by $B$ we get
$$BA\lambda  = I_{n}\lambda  = \lambda  = B0 = 0,$$
so $\lambda  = 0$. Then since $(A^{1}, \dots  , A^{n})$ are $n$ linearly independent vectors in $K^{n}$, by Proposition 3.13(3), they form a basis of $K^{n}$. Consequently, for every vector $b \in K^{n}$, there is a unique column vector $(x_{1}, \dots  , x_{n}) \in K^{n}$ such that
$$Ax = x_{1}A^{1}+ \cdots  + x_{n}A^{n}= b,$$
where $x$ is the column vector
$$x = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
Thus we can solve the $n$ equations
$$Ax^{j}= e_{j},1 \le j \le n,$$
where $e_{j} = (0, \dots  , 0, 1, 0, \dots  , 0)$ is the jth canonical basis vector in $K^{n}$. These equations yield the matrix equation
$$AX = I_{n},$$
where $X = (x^{1} \cdots  x^{n})$ is the $n \times  n$ matrix whose jth column is $x^{j}$. Consequently, $X$ is a right inverse of $A$. Now $A$ has a left inverse $B$ and a right inverse $X$, so by Proposition 2.2, we have $X = B$, so $A$ is invertible and its inverse is equal to $B$. Let us now assume that there is a matrix $C$ such that $AC = I_{n}$. We can repeat the previous proof with $C$ playing the role of $A$ and $A$ playing the role of $B$ to conclude that $C$ is invertible and that $C^{-1} = A$. But then $C^{-1}$ is invertible with inverse $C$, and since $C = (C^{-1})^{-1} = A^{-1}$, we conclude that $A$ is invertible and that its inverse is equal to $C$.

<!-- PAGE 99 -->
Using Proposition 2.3 (or mimicking the computations in its proof), we note that if $A$ and $B$ are two $n \times  n$ invertible matrices, then AB is also invertible and $(AB)^{-1} = B^{-1}A^{-1}$. An important criterion for a square matrix to be invertible is stated next. Another proof is provided in Proposition 4.4 .

> **Proposition 3.16.** A square matrix $A \in M_{n}(K)$ is invertible iff its columns $(A^{1}, \dots  , A^{n})$ are linearly independent.

*Proof.* If $A$ is invertible, then in particular it has a left inverse $A^{-1}$, so the first part of the proof of Proposition 3.15 with $B = A^{-1}$ proves that the columns $(A^{1}, \dots  , A^{n})$ of $A$ are linearly independent. This fact is also proven as part of the proof of Proposition 4.4. Conversely, assume that the columns $(A^{1}, \dots  , A^{n})$ of $A$ are linearly independent. The second part of the proof of Proposition 3.15 shows that $A$ is invertible. Another useful criterion for a square matrix to be invertible is stated next.

> **Proposition 3.17.** A square matrix $A \in M_{n}(K)$ is invertible iff for any $x \in K^{n}$, the equation Ax $= 0$ implies that $x = 0$.

*Proof.* If $A$ is invertible and if Ax $= 0$, then by multiplying both sides of the equation $x = 0$ by $A^{-1}$, we get
$$A^{-1}Ax = I_{n}x = x = A^{-1}0 = 0.$$
Conversely, for any $x = (x_{1}, \dots  , x_{n}) \in K^{n}$, since
$$Ax = x_{1}A^{1}+ \cdots  + x_{n}A^{n},$$
the condition Ax $= 0$ implies $x = 0$ is equivalent to the linear independence of the columns $(A^{1}, \dots  , A^{n})$ of $A$. By Proposition 3.16, the matrix $A$ is invertible. It is immediately verified that the set $M_{m,n}(K)$ of $m \times  n$ matrices is a vector space under addition of matrices and multiplication of a matrix by a scalar.

> **Definition 3.17.** The $m \times n$-matrices $E_{ij} = (e_{h k})$, are defined such that $e_{i j} = 1$, and $e_{h k} = 0$, if $h \neq  i$ or $k \neq  j$; in other words, the $(i$, j)-entry is equal to $1$ and all other entries are $0$. Here are the $E_{ij}$ matrices for $m = 2$ and $n = 3$:
$$E_{11} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,E_{12} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,E_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
$$E_{21} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,E_{22} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} ,E_{23} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .$$

<!-- PAGE 100 -->
It is clear that every matrix $A = (a_{i j}) \in M_{m,n}(K)$ can be written in a unique way as
$$A = \sum_{i=1j}^{m}  \sum_{=1}^{n}  a_{i j}E_{ij}.$$
Thus, the family $(E_{ij})_{1\le i\le m,1\le j\le n}$ is a basis of the vector space $M_{m,n}(K)$, which has dimension mn.
Remark: Definition 3.12 and Definition 3.13 also make perfect sense when $K$ is a (commutative) ring rather than a field. In this more general setting, the framework of vector spaces is too narrow, but we can consider structures over a commutative ring $A$ satisfying all the axioms of Definition 3.1. Such structures are called modules. The theory of modules is (much) more complicated than that of vector spaces. For example, modules do not always have a basis, and other properties holding for vector spaces usually fail for modules. When a module has a basis, it is called a free module. For example, when $A$ is a commutative ring, the structure $A^{n}$ is a module such that the vectors $e_{i}$, with $(e_{i})_{i} = 1$ and $(e_{i})_{j} = 0$ for $j \neq  i$, form a basis of $A^{n}$. Many properties of vector spaces still hold for $A^{n}$. Thus, $A^{n}$ is a free module. As another example, when $A$ is a commutative ring, $M_{m,n}(A)$ is a free module with basis $(E_{i,j})_{1\le i\le m,1\le j\le n}$. Polynomials over a commutative ring also form a free module of infinite dimension. The properties listed in Proposition 3.18 are easily verified, although some of the computations are a bit tedious. A more conceptual proof is given in Proposition 4.1.

> **Proposition 3.18.** $(1)$ Given any matrices $A \in M_{m,n}(K), B \in M_{n,p}(K)$, and $C \in M_{p,q}(K)$, we have
$$(AB)C = A(BC);$$
that is, matrix multiplication is associative.
$(2)$ Given any matrices $A, B \in M_{m,n}(K)$, and $C, D \in M_{n,p}(K)$, for all $\lambda  \in K$, we have
$$(A + B)C = AC + BC$$
$$A(C + D) = AC + AD$$
$$(\lambda A)C = \lambda (AC)$$
$$A(\lambda C) = \lambda (AC),$$
so that matrix multiplication $\cdot$ : $M_{m,n}(K) \times  M_{n,p}(K) \to M_{m,p}(K)$ is bilinear. The properties of Proposition 3.18 together with the fact that $AI_{n} = I_{n}A = A$ for all square $n\times n$ matrices show that $M_{n}(K)$ is a ring with unit $I_{n}$ (in fact, an associative algebra). This is a noncommutative ring with zero divisors, as shown by the following example.
