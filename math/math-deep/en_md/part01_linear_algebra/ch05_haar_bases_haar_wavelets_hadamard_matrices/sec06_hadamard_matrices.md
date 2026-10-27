# Hadamard Matrices


<!-- PAGE 171 -->
If the columns of $W^{-1}$ are $w_{1}', \dots  , w_{2n}'$, then
$$h_{ij} = w_{i}'(w_{j}')^{\top}.$$
We leave it as exercise to compute the bases $(w_{ij})$ and $(h_{ij})$ for $n = 2$, and to display the corresponding images using the command imagesc.

## 5.6 Hadamard Matrices

There is another famous family of matrices somewhat similar to Haar matrices, but these matrices have entries $+1$ and $-1$ (no zero entries).

> **Definition 5.6.** A real $n \times  n$ matrix $H$ is a Hadamard matrix if $h_{ij} = \pm 1$ for all $i, j$ such that $1 \le i, j \le n$ and if
$$H^{\top}H = nI_{n}.$$
Thus the columns of a Hadamard matrix are pairwise orthogonal. Because $H$ is a square matrix, the equation $H^{\top}H = nI_{n}$ shows that $H$ is invertible, so we also have $HH^{\top} = nI_{n}$. The following matrices are example of Hadamard matrices:
$$H_{2} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} ,H_{4} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix} ,$$
$$--$$
and
$$H_{8} = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 & 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 & 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 \\ 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\ 1 & -1 & 1 & -1 & -1 & 1 & -1 & 1 \\ 1 & 1 & -1 & -1 & -1 & -1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$----$$
A natural question is to determine the positive integers $n$ for which a Hadamard matrix of dimension $n$ exists, but surprisingly this is an open problem. The Hadamard conjecture is that for every positive integer of the form $n =$ 4k, there is a Hadamard matrix of dimension $n$. What is known is a necessary condition and various sufficient conditions.

> **Theorem 5.1.** If $H$ is an $n \times  n$ Hadamard matrix, then either $n = 1, 2$, or $n =$ 4k for some positive integer $k$.

<!-- PAGE 172 -->
Sylvester introduced a family of Hadamard matrices and proved that there are Hadamard matrices of dimension $n = 2^{m}$ for all $m \ge 1$ using the following construction.

> **Proposition 5.2.** (Sylvester, $1867)$ If $H$ is a Hadamard matrix of dimension $n$, then the block matrix of dimension 2n,
$$\begin{pmatrix} H & H \\ H & -H \end{pmatrix} ,$$
is a Hadamard matrix. If we start with
$$H_{2} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} ,$$
we obtain an infinite family of symmetric Hadamard matrices usually called Sylvester– Hadamard matrices and denoted by $H_{2m}$. The Sylvester–Hadamard matrices $H_{2}, H_{4}$ and $H_{8}$ are shown on the previous page. In $1893$, Hadamard gave examples of Hadamard matrices for $n = 12$ and $n = 20$. At the present, Hadamard matrices are known for all $n =$ 4k $\le 1000$, except for $n = 668, 716$, and $892$. Hadamard matrices have various applications to error correcting codes, signal processing, and numerical linear algebra; see Seberry, Wysocki and Wysocki $[160]$ and Tropp $[183]$. For example, there is a code based on $H_{32}$ that can correct $7$ errors in any 32-bit encoded block, and can detect an eighth. This code was used on a Mariner spacecraft in $1969$ to transmit pictures back to the earth. For every $m \ge 0$, the piecewise affine functions $plf((H_{2m})_{i})$ associated with the $2^{m}$ rows of the Sylvester–Hadamard matrix $H_{2m}$ are functions on $[0, 1]$ known as the Walsh functions. It is customary to index these $2^{m}$ functions by the integers $0, 1, \dots  , 2^{m}-1$ in such a way that the Walsh function Wal(k, $t)$ is equal to the function $plf((H_{2m})_{i})$ associated with the Row $i$ of $H_{2m}$ that contains $k$ changes of signs between consecutive groups of $+1$ and consecutive groups of $-1$. For example, the fifth row of $H_{8}$, namely
$$\begin{pmatrix} 1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 \end{pmatrix} ,$$
has five consecutive blocks of $+1s$ and -1s, four sign changes between these blocks, and thus is associated with Wal(4, $t)$. In particular, Walsh functions corresponding to the rows of $H_{8}$ (from top down) are: Wal(0, $t)$, Wal(7, $t)$, Wal(3, $t)$, Wal(4, $t)$, Wal(1, $t)$, Wal(6, $t)$, Wal(2, $t)$, Wal(5, $t)$. Because of the connection between Sylvester–Hadamard matrices and Walsh functions, Sylvester–Hadamard matrices are called Walsh–Hadamard matrices by some authors. For every $m$, the $2^{m}$ Walsh functions are pairwise orthogonal. The countable set of Walsh functions Wal(k, $t)$ for all $m \ge 0$ and all $k$ such that $0 \le k \le 2^{m}$ - $1$ can be ordered in
