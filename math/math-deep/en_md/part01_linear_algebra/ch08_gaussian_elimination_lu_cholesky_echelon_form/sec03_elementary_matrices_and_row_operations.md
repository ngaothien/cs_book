# Elementary Matrices and Row Operations


<!-- PAGE 266 -->
dependent and $A_{k}$ would not be invertible, a contradiction. This situation is illustrated by the following matrix for $n = 5$ and $k = 3$:
$$\begin{pmatrix} a_{1 1}^{(3)} & a_{1 2}^{(3)} & a_{1 3}^{(3)} & a_{1 3}^{(3)} & a_{1 5}^{(3)} \\ 0 & a_{2 2}^{(3)} & a_{2 3}^{(3)} & a_{2 4}^{(3)} & a_{2 5}^{(3)} \\ 0 & 0 & 0 & a_{3 4}^{(3)} & a_{3 5}^{(3)} \\ 0 & 0 & 0 & a_{4 4}^{(3)} & a_{4n}^{(3)} \\ 0 & 0 & 0 & a_{5 4}^{(3)} & a_{5 5}^{(3)} \end{pmatrix} .$$
The first three columns of the above matrix are linearly dependent. So one of the entries $a_{i k}^{(k)}$ with $k \le i \le n$ can be chosen as pivot, and we permute the kth row with the ith row, obtaining the matrix $\alpha^{(k)} = (\alpha_{j l}^{(k)}$  ). The new pivot is $\pi_{k}  = \alpha_{k k}^{(k)}$ , and we zero the entries $i = k + 1, \dots  , n$ in column $k$ by adding $-\alpha_{i k}^{(k)}  /\pi_{k}$  times row $k$ to row $i$. At the end of this step, we have $A_{k+1}$. Observe that the first $k$ - $1$ rows of $A_{k}$ are identical to the first $k$ - $1$ rows of $A_{k+1}$. The process of Gaussian elimination is illustrated in schematic form below:
$$\begin{pmatrix} \times & \times & \times & \times \\ \times & \times & \times & \times \\ \times & \times & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & \times & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & 0 & \times & \times \\ 0 & 0 & \times & \times \end{pmatrix} =\Rightarrow \begin{pmatrix} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & 0 & \times & \times \\ 0 & 0 & 0 & \times \end{pmatrix} .$$
$\times \times \times \times$

## 8.3 Elementary Matrices and Row Operations

It is easy to figure out what kind of matrices perform the elementary row operations used during Gaussian elimination. The key point is that if $A = PB$, where $A, B$ are $m \times  n$ matrices and $P$ is a square matrix of dimension $m$, if (as usual) we denote the rows of $A$ and $B$ by $A_{1}, \dots  , A_{m}$ and $B_{1}, \dots  , B_{m}$, then the formula
$$a_{ij} = \sum_{k=1}^{m}  p_{ik}b_{kj}$$
giving the $(i$, j)th entry in $A$ shows that the ith row of $A$ is a linear combination of the rows of $B$:
$$A_{i} = p_{i1}B_{1} + \cdots  + p_{im}B_{m}.$$
Therefore, multiplication of a matrix on the left by a square matrix performs row operations. Similarly, multiplication of a matrix on the right by a square matrix performs column operations The permutation of the kth row with the ith row is achieved by multiplying $A$ on the left by the transposition matrix P(i, $k)$, which is the matrix obtained from the identity matrix

<!-- PAGE 267 -->
by permuting rows $i$ and $k$, i.e.,
$$P(i, k) = \begin{pmatrix} 1 \\ 1 \\ 0 & 1 \\ 1 \\ \ddots \\ 1 \\ 1 & 0 \\ 1 \\ 1 \end{pmatrix} .$$
For example, if $m = 3$,
$$P(1, 3) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,$$
then
$$P(1, 3)B = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} b_{11} & b_{12} & \cdots & \cdots & \cdots  b_{1n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{31} & b_{32} & b_{3n} \end{pmatrix} = \begin{pmatrix} b_{31} & b_{32} & \cdots & \cdots & \cdots  b_{3n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{11} & b_{12} & b_{1n} \end{pmatrix} .$$
$$\cdots \cdots \cdots \cdots \cdots \cdots$$
Observe that det(P(i, $k)) = -1$. Furthermore, P(i, $k)$ is symmetric (P(i, $k)^{\top} =$ P(i, $k))$, and
$$P(i, k)^{-1}= P(i, k).$$
During the permutation Step $(2)$, if row $k$ and row $i$ need to be permuted, the matrix $A$ is multiplied on the left by the matrix $P_{k}$ such that $P_{k} =$ P(i, $k)$, else we set $P_{k} =$ I. Adding $\beta$  times row $j$ to row $i$ (with $i \neq  j)$ is achieved by multiplying $A$ on the left by the elementary matrix,
$$E_{i,j;\beta} = I + \beta e_{i j},$$
where
$$1if k = i and l = j$$
$$(e_{i j})_{k l} =$$
$$0if k \neq  i or l \neq  j,$$
i.e.,
$$E_{i,j;\beta} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ \ddots \\ 1 \\ \beta & 1 \\ 1 \\ 1 \end{pmatrix} orE_{i,j;\beta} = \begin{pmatrix} 1 \\ 1 \\ 1 & \beta \\ 1 \\ \ddots \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} ,$$

<!-- PAGE 268 -->
on the left, $i > j$, and on the right, $i < j$. The index $i$ is the index of the row that is changed by the multiplication. For example, if $m = 3$ and we want to add twice row $1$ to row $3$, since $\beta  = 2, j = 1$ and $i = 3$, we form
$$E_{3,1;2} = I + 2e_{31} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 2 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix} ,$$
and calculate
$$100 \begin{pmatrix} b_{11} & b_{12} & \cdots & \cdots & \cdots  b_{1n} \\ b_{21} & b_{22} & \cdots & \cdots & \cdots  b_{2n} \\ b_{31} & b_{32} & b_{3n} \end{pmatrix}$$
$$E_{3,1;2}B =010$$
$$$$
$$201\cdots \cdots \cdots$$
$$b_{11}b_{12}\cdots \cdots \cdots  b_{1n}$$
$$=b_{21}b_{22}\cdots \cdots \cdots  b_{2n}.$$
$$$$
$$2b_{11} + b_{31}2b_{12} + b_{32}\cdots \cdots \cdots  2b_{1n} + b_{3n}$$
Observe that the inverse of $E_{i,j;\beta} =$ I $+ \beta e_{i j}$ is $E_{i,j;-\beta} =$ I - $\beta e_{i j}$ and that $det(E_{i,j;\beta}) = 1$. Therefore, during Step $3$ (the elimination step), the matrix $A$ is multiplied on the left by a product $E_{k}$ of matrices of the form $E_{i,k;\beta i,k}$, with $i > k$. Consequently, we see that
$$A_{k+1} = E_{k}P_{k}A_{k},$$
and then
$$A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A.$$
This justifies the claim made earlier that $A_{k} = M_{k}A$ for some invertible matrix $M_{k}$; we can pick
$$M_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1},$$
a product of invertible matrices. The fact that det(P(i, $k)) = -1$ and that $det(E_{i,j;\beta}) = 1$ implies immediately the fact claimed above: We always have
$$\det(A_{k}) = \pm  \det(A).$$
Furthermore, since
$$A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A$$
and since Gaussian elimination stops for $k = n$, the matrix
$$A_{n} = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}A$$
is upper-triangular. Also note that if we let $M = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}$, then det(M) $= \pm 1$, and
$$\det(A) = \pm  \det(A_{n}).$$
The matrices P(i, $k)$ and $E_{i,j;\beta}$ are called elementary matrices. We can summarize the above discussion in the following theorem:
