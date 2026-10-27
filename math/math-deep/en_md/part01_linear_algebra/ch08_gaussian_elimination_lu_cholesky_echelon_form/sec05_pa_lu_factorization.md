# PA = LU Factorization


<!-- PAGE 275 -->

## 8.5 PA = LU Factorization

The following easy proposition shows that, in principle, $A$ can be premultiplied by some permutation matrix $P$, so that $PA$ can be converted to upper-triangular form without using any pivoting. Permutations are discussed in some detail in Section 30.3, but for now we just need this definition. For the precise connection between the notion of permutation (as discussed in Section 30.3) and permutation matrices, see Problem 8.16.

> **Definition 8.3.** A permutation matrix is a square matrix that has a single $1$ in every row and every column and zeros everywhere else. It is shown in Section 30.3 that every permutation matrix is a product of transposition matrices (the P(i, k)s), and that $P$ is invertible with inverse $P^{\top}$ .

> **Proposition 8.4.** Let $A$ be an invertible $n \times n$-matrix. There is some permutation matrix $P$ so that (PA)(1 : $k, 1$ : $k)$ is invertible for $k = 1, \dots  , n$.

*Proof.* The case $n = 1$ is trivial, and so is the case $n = 2$ (we swap the rows if necessary). If $n \ge 3$, we proceed by induction. Since $A$ is invertible, its columns are linearly independent; in particular, its first $n -1$ columns are also linearly independent. Delete the last column of $A$. Since the remaining $n -1$ columns are linearly independent, there are also $n -1$ linearly independent rows in the corresponding $n \times  (n$ - $1)$ matrix. Thus, there is a permutation of these $n$ rows so that the $(n$ - $1) \times  (n$ - $1)$ matrix consisting of the first $n$ - $1$ rows is invertible. But then there is a corresponding permutation matrix $P_{1}$, so that the first $n$ - $1$ rows and columns of $P_{1}A$ form an invertible matrix A'. Applying the induction hypothesis to the $(n$ - $1) \times  (n$ - $1)$ matrix A', we see that there some permutation matrix $P_{2}$ (leaving the nth row fixed), so that $(P_{2}P_{1}A)(1$ : $k, 1$ : $k)$ is invertible, for $k = 1, \dots  , n$ - $1$. Since $A$ is invertible in the first place and $P_{1}$ and $P_{2}$ are invertible, $P_{1}P_{2}A$ is also invertible, and we are done.
Remark: One can also prove Proposition 8.4 using a clever reordering of the Gaussian elimination steps suggested by Trefethen and Bau $[182]$ (Lecture $21)$. Indeed, we know that if $A$ is invertible, then there are permutation matrices $P_{i}$ and products of elementary matrices $E_{i}$, so that
$$A_{n} = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}A,$$
where $U = A_{n}$ is upper-triangular. For example, when $n = 4$, we have $E_{3}P_{3}E_{2}P_{2}E_{1}P_{1}A = U$. We can define new matrices $E_{1}', E_{2}', E_{3}'$ which are still products of elementary matrices so that we have
$$E_{3}'E_{2}'E_{1}'P_{3}P_{2}P_{1}A = U.$$
Indeed, if we let $E_{3}' = E_{3}, E_{2}' = P_{3}E_{2}P_{3}^{-1}$ , and $E_{1}' = P_{3}P_{2}E_{1}P_{2}^{-1} P_{3}^{-1}$ , we easily verify that each $E_{k}'$ is a product of elementary matrices and that
$$E_{3}'E_{2}'E_{1}'P_{3}P_{2}P_{1} = E_{3}(P_{3}E_{2}P_{3}^{-1} )(P_{3}P_{2}E_{1}P_{2}^{-1} P_{3}^{-1} )P_{3}P_{2}P_{1} = E_{3}P_{3}E_{2}P_{2}E_{1}P_{1}.$$

<!-- PAGE 276 -->
It can also be proven that $E_{1}', E_{2}', E_{3}'$ are lower triangular (see Theorem 8.5). In general, we let
$$E_{k}' = P_{n-1} \cdots  P_{k+1}E_{k}P_{k+1}^{-1} \cdots  P_{n-1}^{-1},$$
and we have
$$E_{n-1}' \cdots  E_{1}'P_{n-1} \cdots  P_{1}A = U,$$
where each $E_{j}'$ is a lower triangular matrix (see Theorem 8.5). It is remarkable that if pivoting steps are necessary during Gaussian elimination, a very simple modification of the algorithm for finding an LU-factorization yields the matrices $L, U$, and $P$, such that $PA = LU$. To describe this new method, since the diagonal entries of $L$ are 1s, it is convenient to write
$$L = I + \Lambda .$$
Then in assembling the matrix $\Lambda$  while performing Gaussian elimination with pivoting, we make the same transposition on the rows of $\Lambda$  (really $\Lambda_{k-1}$ ) that we make on the rows of $A$ (really $A_{k})$ during a pivoting step involving row $k$ and row $i$. We also assemble $P$ by starting with the identity matrix and applying to $P$ the same row transpositions that we apply to $A$ and $\Lambda$ . Here is an example illustrating this method.

> **Example 8.3.** Given
$$A = A_{1} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
we have the following sequence of steps: We initialize $\Lambda_{0}  = 0$ and $P_{0} = I_{4}$. The first pivot is $\pi_{1}  = 1$ in row $1$, and we subtract row $1$ from rows $2, 3$, and $4$. We get
$$A_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 0 & -2 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 2 & 1 & 1 \end{pmatrix} \Lambda_{1}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} P_{1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
The next pivot is $\pi_{2}  = -2$ in row $3$, so we permute row $2$ and $3$; we also apply this permutation to $\Lambda$  and $P$:
$$A_{3}' = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 2 & 1 & 1 \end{pmatrix} \Lambda_{2}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Next we subtract row $2$ from row $4$ (and add $0$ times row $2$ to row $3)$. We get
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} \Lambda_{2}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$

<!-- PAGE 277 -->
The next pivot is $\pi_{3}  = -2$ in row $3$, and since the fourth entry in column $3$ is already a zero, we add $0$ times row $3$ to row $4$. We get
$$A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} \Lambda_{3}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
The procedure is finished, and we have
$$L = \Lambda_{3}  + I = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} U = A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} P = P_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
It is easy to check that indeed
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$---$$
and
$$PA = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$----$$
Using the idea in the remark before the above example, we can prove the theorem below which shows the correctness of the algorithm for computing $P, L$ and $U$ using a simple adaptation of Gaussian elimination. We are not aware of a detailed proof of Theorem 8.5 in the standard texts. Although Golub and Van Loan $[83]$ state a version of this theorem as their Theorem 3.1.4, they say that “The proof is a messy subscripting argument.” Meyer $[129]$ also provides a sketch of proof (see the end of Section 3.10). In view of this situation, we offer a complete proof. It does involve a lot of subscripts and superscripts, but in our opinion, it contains some techniques that go far beyond symbol manipulation.

> **Theorem 8.5.** For every invertible $n \times n$-matrix $A$, the following hold:
$(1)$ There is some permutation matrix $P$, some upper-triangular matrix $U$, and some unit lower-triangular matrix $L$, so that $PA = LU$ (recall, $L_{i i} = 1$ for $i = 1, \dots  , n)$. Furthermore, if $P =$ I, then $L$ and $U$ are unique and they are produced as a result of Gaussian elimination without pivoting.

<!-- PAGE 278 -->
$(2)$ If $E_{n-1} \dots  E_{1}A = U$ is the result of Gaussian elimination without pivoting, write as usual $A_{k} = E_{k-1} \dots  E_{1}A$ (with $A_{k} = (a_{ij}^{(k)}$ )), and let $\ell_{ik}  = a_{ik}^{(k)} /a_{kk}^{(k)}$ , with $1 \le k \le n -1$ and $k + 1 \le i \le n$. Then
$$L = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ \ell_{21} & 1 & 0 & \cdots & 0 \\ \ell_{31} & \ell_{32} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots \\ 0 \\ \ell_{n1} & \ell_{n2} & \ell_{n3} & \cdots & 1 \end{pmatrix} ,$$
where the kth column of $L$ is the kth column of $E_{k}^{-1}$ , for $k = 1, \dots  , n$ - $1$.
$(3)$ If $E_{n-1}P_{n-1} \cdots  E_{1}P_{1}A = U$ is the result of Gaussian elimination with some pivoting, write $A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A$, and define $E_{j}^{k}$ , with $1 \le j \le n -1$ and $j \le k \le n -1$, such that, for $j = 1, \dots  , n$ - $2$,
$$E_{j}^{j} = E_{j}$$
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},for k = j + 1, \dots  , n -1,$$
and
$$E_{n-1}^{n-1} = E_{n-1}.$$
Then,
$$E_{j}^{k} = P_{k}P_{k-1} \cdots  P_{j+1}E_{j}P_{j+1} \cdots  P_{k-1}P_{k}$$
$$U = E_{n-1}^{n-1} \cdots  E_{1}^{n-1}P_{n-1} \cdots  P_{1}A,$$
and if we set
$$P = P_{n-1} \cdots  P_{1}$$
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1},$$
then
$$PA = LU.(\dagger_{1} )$$
Furthermore,
$$(E_{j}^{k} )^{-1}= I +\mathcal{E}_{j}^{k} ,1 \le j \le n -1, j \le k \le n -1,$$
where $\mathcal{E}_{j}^{k}$ is a lower triangular matrix of the form
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$

<!-- PAGE 279 -->
we have
$$E_{j}^{k} = I -E_{j}^{k} ,$$
and
$$\mathcal{E}_{j}^{k} = P_{k}\mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
where $P_{k} =$ I or else $P_{k} =$ P(k, $i)$ for some $i$ such that $k + 1 \le i \le n$; if $P_{k} \neq$  I, this means that $(E_{j}^{k} )^{-1}$ is obtained from $(E_{j}^{k-1})^{-1}$ by permuting the entries on rows $i$ and $k$ in column $j$. Because the matrices $(E_{j}^{k} )^{-1}$ are all lower triangular, the matrix $L$ is also lower triangular. In order to find $L$, define lower triangular $n \times  n$ matrices $\Lambda_{k}$  of the form
$$\Lambda_{k}  = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 & \cdots & \cdots & 0 \\ \vdots & \vdots \\ \lambda_{21}^{(k)} & 0 & 0 & 0 & 0 & 0 \\ \ddots & \vdots & \vdots \\ \lambda_{31}^{(k)} & \lambda_{32}^{(k)} & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 \\ \lambda_{k+11}^{(k)} & \lambda_{k+12}^{(k)} & \cdots & \lambda_{k+1k}^{(k)} & 0 & \cdots & \cdots & 0 \\ \lambda_{k+21}^{(k)} & \lambda_{k+22}^{(k)} & \cdots & \lambda_{k+2k}^{(k)} & 0 & \ddots & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \lambda_{n1}^{(k)} & \lambda_{n2}^{(k)} & \lambda_{nk}^{(k)} & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots \cdots$$
to assemble the columns of $L$ iteratively as follows: let
$$(-\ell_{k+1k}^{(k)} , \dots  , -\ell_{nk}^{(k)}  )$$
be the last n-k elements of the kth column of $E_{k}$, and define $\Lambda_{k}$  inductively by setting
$$\Lambda_{1}  = \begin{pmatrix} 0 & 0 & \cdots & 0 \\ \ell_{21}^{(1)} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots$$
then for $k = 2, \dots  , n$ - $1$, define
$$\Lambda_{k}'  = P_{k}\Lambda_{k-1} ,(\dagger_{2} )$$

<!-- PAGE 280 -->
and
$$\Lambda_{k}  = (I + \Lambda_{k}' )E_{k}^{-1}-I = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 & \cdots & \cdots & 0 \\ \vdots & \vdots \\ \lambda_{21}^{'(k-1)} & 0 & 0 & 0 & 0 & 0 \\ \ddots & \vdots & \vdots \\ \lambda_{31}^{'(k-1)} & \lambda_{32}^{'(k-1)} & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 \\ \lambda_{k1}^{'(k-1)} & \lambda_{k2}^{'(k-1)} & \cdots & \lambda_{k(k-1)}^{'(k-1)} & 0 & \cdots & \cdots & 0 \\ \lambda_{k+11}^{'(k-1)} & \lambda_{k+12}^{'(k-1)} & \cdots & \lambda_{k+1 (-1)}^{'(k-1)} & \ell_{k+1k}^{(k)} & \ddots & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \lambda_{n1}^{'(k-1)} & \lambda_{n2}^{'(k-1)} & \lambda_{n k-1}^{'(k-1)} & \ell_{nk}^{(k)} & 0 \end{pmatrix} ,$$
$$\cdots \cdots \cdots$$
with $P_{k} =$ I or $P_{k} =$ P(k, $i)$ for some $i > k$. This means that in assembling $L$, row $k$ and row $i$ of $\Lambda_{k-1}$  need to be permuted when a pivoting step permuting row $k$ and row $i$ of $A_{k}$ is required. Then
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k}^{k})^{-1}$$
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
for $k = 1, \dots  , n$ - $1$, and therefore
$$L = I + \Lambda_{n-1} .$$
The proof of Theorem 8.5, which is very technical, is given in Section 8.6. We emphasize again that Part $(3)$ of Theorem 8.5 shows the remarkable fact that in assembling the matrix $L$ while performing Gaussian elimination with pivoting, the only change to the algorithm is to make the same transposition on the rows of $\Lambda_{k-1}$  that we make on the rows of $A$ (really $A_{k})$ during a pivoting step involving row $k$ and row $i$. We can also assemble $P$ by starting with the identity matrix and applying to $P$ the same row transpositions that we apply to $A$ and $\Lambda$ . Here is an example illustrating this method.

> **Example 8.4.** Consider the matrix
$$A = \begin{pmatrix} 1 & 2 & -3 & 4 \\ 4 & 8 & 12 & -8 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} .$$
$$---$$
We set $P_{0} = I_{4}$, and we can also set $\Lambda_{0}  = 0$. The first step is to permute row $1$ and row $2$, using the pivot $4$. We also apply this permutation to $P_{0}$:
$$A_{1}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} P_{1} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$

<!-- PAGE 281 -->
Next we subtract $1/4$ times row $1$ from row $2, 1/2$ times row $1$ from row $3$, and add $3/4$ times row $1$ to row $4$, and start assembling $\Lambda$ :
$$A_{2} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 0 & -6 & 6 \\ 0 & -1 & -4 & 5 \\ 0 & 5 & 10 & 10 \end{pmatrix} \Lambda_{1}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 0 & 0 & 0 \\ 3/4 & 0 & 0 & 0 \end{pmatrix} P_{1} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$--$$
Next we permute row $2$ and row $4$, using the pivot $5$. We also apply this permutation to $\Lambda$ and $P$:
$$A_{3}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & -1 & -4 & 5 \\ 0 & 0 & 6 & 6 \end{pmatrix} \Lambda_{2}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/2 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
Next we add $1/5$ times row $2$ to row $3$, and update $\Lambda_{2}'$ :
$$A_{3} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -2 & 3 \\ 0 & 0 & 6 & 6 \end{pmatrix} \Lambda_{2}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/2 & -1/5 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
Next we permute row $3$ and row $4$, using the pivot $-6$. We also apply this permutation to $\Lambda$  and $P$:
$$A_{4}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 2 & 3 \end{pmatrix} \Lambda_{3}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 1/5 & 0 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$--$$
Finally we subtract $1/3$ times row $3$ from row $4$, and update $\Lambda_{3}'$ :
$$A_{4} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} \Lambda_{3}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 1/5 & 1/3 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$-$$
Consequently, adding the identity to $\Lambda_{3}$ , we obtain
$$L = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3/4 & 1 & 0 & 0 \\ 1/4 & 0 & 1 & 0 \\ 1/2 & 1/5 & 1/3 & 1 \end{pmatrix} ,U = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,P = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$-$$

<!-- PAGE 282 -->
We check that
$$PA = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 & -3 & 4 \\ 4 & 8 & 12 & -8 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ -3 & -1 & 1 & -4 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \end{pmatrix} ,$$
$$---$$
and that
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3/4 & 1 & 0 & 0 \\ 1/4 & 0 & 1 & 0 \\ 1/2 & 1/5 & 1/3 & 1 \end{pmatrix} \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ -3 & -1 & 1 & -4 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \end{pmatrix} = PA.$$
$$-$$
Note that if one willing to overwrite the lower triangular part of the evolving matrix $A$, one can store the evolving $\Lambda$  there, since these entries will eventually be zero anyway! There is also no need to save explicitly the permutation matrix $P$. One could instead record the permutation steps in an extra column (record the vector $(\pi (1), \dots  , \pi (n))$ corresponding to the permutation $\pi$  applied to the rows). We let the reader write such a bold and spaceefficient version of LU-decomposition!
Remark: In Matlab the function lu returns the matrices $P, L, U$ involved in the $PA = LU$ factorization using the call $[L, U, P] =$ lu(A). As a corollary of Theorem 8.5(1), we can show the following result.

> **Proposition 8.6.** If an invertible real symmetric matrix $A$ has an LU-decomposition, then $A$ has a factorization of the form
$$A = LDL^{\top},$$
where $L$ is a lower-triangular matrix whose diagonal entries are equal to $1$, and where $D$ consists of the pivots. Furthermore, such a decomposition is unique.

*Proof.* If $A$ has an LU-factorization, then it has an LDU factorization
$$A = LDU,$$
where $L$ is lower-triangular, $U$ is upper-triangular, and the diagonal entries of both $L$ and $U$ are equal to $1$. Since $A$ is symmetric, we have
$$LDU = A = A^{\top}= U^{\top} DL^{\top},$$
with $U^{\top}$ lower-triangular and $DL^{\top}$ upper-triangular. By the uniqueness of LU-factorization (Part $(1)$ of Theorem 8.5), we must have $L = U^{\top}$ (and $DU = DL^{\top})$, thus $U = L^{\top}$, as claimed.
Remark: It can be shown that Gaussian elimination plus back-substitution requires $n^{3}/3+ O(n^{2})$ additions, $n^{3}/3 + O(n^{2})$ multiplications and $n^{2}/2 +$ O(n) divisions.
