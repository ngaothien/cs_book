# Kronecker Product Construction of Haar Matrices


<!-- PAGE 160 -->
sequence $u^{0} = (10, 15, 5, -2, 1, 3, 1, 1) u^{1} = (10 + 15, 10$ - $15, 5, -2, 1, 3, 1, 1) = (25, -5, 5, -2, 1, 3, 1, 1) u^{2} = (25 + 5, 25$ - $5, -5 + (-2), -5$ - $(-2), 1, 3, 1, 1) = (30, 20, -7, -3, 1, 3, 1, 1) u^{3} = (30 + 1, 30$ - $1, 20 + 3, 20$ - $3, -7 + 1, -7$ - $1, -3 + 1, -3$ - $1)$
$$= (31, 29, 23, 17, -6, -8, -2, -4),$$
which gives back $u = (31, 29, 23, 17, -6, -8, -2, -4)$.

## 5.3 Kronecker Product Construction of Haar Matrices

There is another recursive method for constructing the Haar matrix $W_{n}$ of dimension $2^{n}$ that makes it clearer why the columns of $W_{n}$ are pairwise orthogonal, and why the above algorithms are indeed correct (which nobody seems to prove!). If we split $W_{n}$ into two $2^{n} \times  2^{n-1}$ matrices, then the second matrix containing the last $2^{n-1}$ columns of $W_{n}$ has a very simple structure: it consists of the vector
$$(1, -1, 0, \dots  , 0)$$
$$|{z}$$
$$2n$$
and $2^{n-1}$ - $1$ shifted copies of it, as illustrated below for $n = 3$:
$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
Observe that this matrix can be obtained from the identity matrix $I_{2n-1}$, in our example
$$I_{4} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,$$
by forming the $2^{n} \times  2^{n-1}$ matrix obtained by replacing each $1$ by the column vector
$$\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

<!-- PAGE 161 -->
and each zero by the column vector
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
Now the first half of $W_{n}$, that is the matrix consisting of the first $2^{n-1}$ columns of $W_{n}$, can be obtained from $W_{n-1}$ by forming the $2^{n} \times 2^{n-1}$ matrix obtained by replacing each $1$ by the column vector
$$\begin{pmatrix} 1 \\ 1 \end{pmatrix} ,$$
each $-1$ by the column vector
$$\begin{pmatrix} -1 \\ -1 \end{pmatrix} ,$$
and each zero by the column vector
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
For $n = 3$, the first half of $W_{3}$ is the matrix
$$\begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & -1 & 0 & 1 \\ 1 & -1 & 0 & -1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
which is indeed obtained from
$$W_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
using the process that we just described. These matrix manipulations can be described conveniently using a product operation on matrices known as the Kronecker product.

> **Definition 5.4.** Given a $m\times n$ matrix $A = (a_{ij})$ and a $p\times q$ matrix $B = (b_{ij})$, the Kronecker product (or tensor product) $A \otimes B$ of $A$ and $B$ is the mp $\times$  nq matrix
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$
