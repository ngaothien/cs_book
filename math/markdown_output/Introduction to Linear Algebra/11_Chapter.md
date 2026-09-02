# **Chapter 11**

# **Numerical Linear Algebra**

**1** The goals of numerical linear algebra are **speed** and **accuracy** and **stability** : n > 10<sup>3</sup>or 10<sup>6</sup> . 2 Matrices can be full or sparse or banded or structured: special algorithms for each. **<sup>3</sup>**Accuracy of elimination is controlled by the **condition number** 11 A 11 11 A - **4** Gram-Schmidt is often computed by using **Householder reflections** H = I - 2uu T to find *Q.*  **5** Eigenvalues use *QR* **iterations** Ao = QoRo ---+ RoQo = A1 = Q1R1 ---+ ---+ An. **6 Shifted** *QR* is even better: Shift to Ak - ckI = QkRk, shift back Ak+l = RkQk + ckI. 7 Iteration *Sxk+l* = *b* - *Txk* solves *(S* + *T) x* = *b* if all eigenvalues of s-1T have l>-1 < 1. **8** Iterative methods often use **preconditioners** *P.* Change *Ax= b* to *PAx* = *Pb* with *PA� I.*  **9 Conjugate gradients** and **GMRES** are Krylov methods; see Trefethen-Bau (and other texts).

### **11.1 Gaussian Elimination in Practice**

Numerical linear algebra is a struggle for quick solutions and also accurate solutions. We need efficiency but we have to avoid instability. In Gaussian elimination, the main freedom (always available) is to *exchange equations.* This section explains when to exchange rows for the sake of speed, and when to do it for the sake of accuracy.

The key to accuracy is to avoid unnecessarily large numbers. Often that requires us to avoid small numbers! A small pivot generally means large multipliers (since we divide by the pivot). A good plan is *"partial pivoting",* to choose the largest available pivot in each new column. We will see why this pivoting strategy is built into computer programs.

Other row exchanges are done to save elimination steps. In practice, most large matrices are *sparse-almost* all entries are zeros. Elimination is fastest when the equations are ordered *to produce a narrow band of nonzeros.* Zeros inside the band "fill in" during elimination-those zeros are destroyed and don't save computing time.

Section 11.2 is about instability that can't be avoided. It is built into the problem, and this sensitivity is measured by the *"condition number".* Then Section 11.3 describes how to solve *Ax* = *b* **by** *iterations.* Instead of direct elimination, the computer solves an easier equation many times. Each answer Xk leads to the next guess Xk+i· For good iterations (the **conjugate gradient method** is extremely good), the Xk converge quickly to *<sup>X</sup>*= A- *<sup>1</sup>* b.

## **The Fastest Supercomputer**

A new supercomputing record was announced by IBM and Los Alamos on May 20, 2008. The Roadrunner was the first to achieve a quadrillion (10<sup>15</sup> ) floating-point operations per second: *a petafiop machine.* The benchmark for this world record was a large dense linear system *Ax* = *b:* computer speed is tested by linear algebra.

That machine was shut down in 2013 ! The TOP500 project ranks the 500 most powerful computer systems in the world. As I write this page in October 2015, the first four are from NUDT in China, Cray and IBM in the US, and Fujitsu in Japan. They all use a LINUXbased system. And all vector processors have fallen out of the top 500.

Looking ahead, the Summit is expected to take first place with 150-300 petaflops. President Obama has just ordered the development of an exascale system (1000 petaflops). Up to now we are following Moore's Law of doubling every 14 months.

The LAPACK software does elimination with partial pivoting. The biggest difference from this book is to organize the steps to use large submatrices and never single numbers. And graphics processing units (GPU's) are now almost required for success. The market for video games dwarfs scientific computing and led to astonishing acceleration in the chips.

Before IBM's BlueGene, a key issue was to count the standard quad-core processors that a petaflop machine would need: 32,000. The new architecture uses much less power, but its hybrid design has a price: a code needs three separate compilers and explicit instructions to move all the data. Please see the excellent article in *SIAM News* **(siam.org,** July 2008) and the update on **www.Ianl.gov/roadrunner.** 

Our thinking about matrix calculations is reflected in the highly optimized **BLAS**  *(Basic Linear Algebra Subroutines).* They come at levels 1, 2, and 3:

**Level 1** Linear combinations of vectors *au+ v: O(n)* work

**Level 2** Matrix-vector multiplications *Au+ v:* O(n<sup>2</sup> ) work

**Level 3** Matrix-matrix multiplications *AB+ C: O(n<sup>3</sup> )* work

Level 1 is an elimination step (multiply row *j* by £ij and subtract from row i). Level 2 can eliminate a whole column at once. A high performance solver is rich in Level 3 BLAS *(AB* has 2n<sup>3</sup>flops and 2n<sup>2</sup>data, a good ratio of work to talk).

It is *data passing* and *storage retrieval* that limit the speed of parallel processing. The high-velocity cache between main memory and floating-point computation has to be fully used! Top speed demands a *block matrix approach* to elimination.

The big change, corning now, is parallel processing at the chip level.

## **Roundoff Error and Partial Pivoting**

Up to now, any pivot (nonzero of course) was accepted. In practice a small pivot is dangerous. A catastrophe can occur when numbers of different sizes are added. Computers keep a fixed number of significant digits (say three decimals, for a very weak machine). The sum 10,000 + 1 is rounded off to 10,000. The "l" is completely lost. Watch how that changes the solution to this problem:

| $.0001u + v = 1$ | starts with coefficient matrix | $A = \begin{bmatrix} .0001 & 1 \\ -1 & 1 \end{bmatrix}$ |
|------------------|--------------------------------|---------------------------------------------------------|
| $-u + v = 0$     |                                |                                                         |

If we accept .0001 as the pivot, elimination adds 10,000 times row 1 to row 2. Roundoff leaves

| $10,000v = 10,000$ | instead of | $10,001v = 10,001$ . |
|--------------------|------------|----------------------|
|                    |            |                      |

The computed answer v = l is near the true v = .9999. But then back substitution puts the wrong *v* = l into the equation for u:

| .0001 $u + 1 = 1$ | instead of | .0001 $u + .9999 = 1$ . |
|-------------------|------------|-------------------------|
|-------------------|------------|-------------------------|

The first equation gives u = 0. The correct answer (look at the second equation) is u = 1.000. By losing the "1" in the matrix, we have lost the solution. *The small change from* 10,001 *to* 10,000 *has changed the answer from* u = l *to* u = 0 (100% error!).

If we exchange rows, even this weak computer finds an answer that is correct to 3 places:

| $-u + v = 0$     | $\longrightarrow$ | $-u + v = 0$ | $\longrightarrow$ | $u = 1$   |
|------------------|-------------------|--------------|-------------------|-----------|
| $.0001u + v = 1$ |                   | $v = 1$      |                   | $v = 1$ . |

The original pivots were .0001 and 10,000-badly scaled. After a row exchange the exact pivots are -1 and 1.0001-well scaled. The computed pivots -1 and 1 come close to the exact values. Small pivots bring numerical instability, and the remedy is *partial pivoting.* Here is our strategy when we reach and search column *k* for the best available pivot:

*Choose the largest number in row k or below. Exchange its row with row k.* 

The strategy of *complete pivoting* looks also in later columns for the largest pivot. It exchanges columns as well as rows. This expense is seldom justified, and all major codes use partial pivoting. Multiplying a row or column by a scaling constant can also be very worthwhile. *If the first equation above is u* + *10,000v* = 10,000 *and we don't rescale, then* l *looks like a good pivot and we would miss the essential row exchange.* 

For positive definite matrices, row exchanges are *not* required. It is safe to accept the pivots as they appear. Small pivots can occur, but the matrix is not improved by row exchanges. When its condition number is high, the problem is in the matrix and not in the code. In this case the output is unavoidably sensitive to the input.

The reader now understands how a computer actually solves Ax = *b--by elimination with partial pivoting.* Compared with the theoretical description-find A-<sup>1</sup>*and multiply* A-1 b-the details took time. But in computer time, elimination is much faster. I believe that elimination is also the best approach to the algebra of row spaces and nullspaces.

# **Operation Counts: Full Matrices**

Here is a practical question about cost. *How many separate operations are needed to solve*  Ax = *b by elimination?* This decides how large a problem we can afford.

Look first at *A,* which changes gradually into *U.* When a multiple of row 1 is subtracted from row 2, we do *n* operations. The first is a division by the pivot, to find the multiplier£. For the other n -1 entries along the row, the operation is a "multiply-subtract". For convenience, we count this as a single operation. If you regard multiplying by £ and subtracting from the existing entry as two separate operations, *multiply all our counts by* 2.

The matrix *A* is *n* by *n.* The operation count applies to all *n* -1 rows below the first. Thus it requires *n* times *n* -1 operations, or n <sup>2</sup>-*n,* to produce zeros below the first pivot. *Check: All* n<sup>2</sup>*entries are changed, except then entries in the first row.* 

When elimination is down to k equations, the rows are shorter. We need only k <sup>2</sup>- k operations (instead of n <sup>2</sup>- n) to clear out the column below the pivot. This is true for 1 ::::; k ::::; *n.* The last step requires no operations (1 <sup>2</sup>- 1 = 0); forward elimination is complete. The total count to reach U is the sum of k <sup>2</sup>- k over all values of k from 1 to n:

$$(1^2 + \dots + n^2) - (1 + \dots + n) = \frac{n(n+1)(2n+1)}{6} - \frac{n(n+1)}{2} = \frac{n^3 - n}{3}$$

Those are known formulas for the sum of the first n numbers and their squares. Substituting n = 100 gives a million minus a hundred-then divide by 3. (That translates into one second on a workstation.) We will ignore *n* in comparison with n<sup>3</sup> , to reach our main conclusion:

*The multiply-subtract count is* ½n<sup>3</sup>*for forward elimination (A to U, producing L).*

That means ½n3 multiplications and subtractions. Doubling *n* increases this cost by eight (because *n* is cubed). 100 equations are easy, 1000 are more expensive, 10000 dense equations are close to impossible. We need a faster computer or a lot of zeros or a new idea.

On the right side of the equations, the steps go much faster. We operate on single numbers, not whole rows. *Each right side needs exactly n*<sup>2</sup>*operations.* Down and back up we are solving two triangular systems, *Le* = *b* forward and *U x* = c backward. In back substitution, the last unknown needs only division by the last pivot. The equation above it needs two operations-substituting *Xn* and dividing by *its* pivot. The kth step needs k multiply-subtract operations, and the total for back substitution is

$$1 + 2 + \dots + n = \frac{n(n+1)}{2} \approx \frac{1}{2}n^2$$
 operations.

The forward part is similar. *The n* <sup>2</sup>*total exactly equals the count for multiplying* A-lb! This leaves Gaussian elimination with two big advantages over *A* -lb:

- **1 Elimination requires** ½n<sup>3</sup>**multiply-subtracts, compared to** n<sup>3</sup>**for** A-1
- **2** If A **is** *banded* **so are** L **and** U: **by comparison** A -<sup>1</sup>**is full of nonzeros.**

#### **Band Matrices**

These counts are improved when *A* has *"good zeros".* A good zero is an entry that remains zero in *L* and *U. The best zeros are at the beginning of a row.* They require no elimination steps (the multipliers are zero). So we also find those same good zeros in *L.* That is especially clear for this *tridiagonal matrix A* (and for band matrices in Figure 11.1):

**Tridiagonal Bidiagonal times bidiagonal** 

A=

r-i -� -1 1 r-i -1 2 -1 -1 2

1 -1 1 -1

*=LU* 

Figure 11.1: *A* = *LU* for a band matrix. Good zeros in *A stay zero* in Land *U.* 

These zeros lead to a complete change in the operation count, for "half-bandwidth" w:

*A band matrix has 
$$a_{ij} = 0$$
 when  $|i - j| > w$ .*

Thus *w* = 1 for a diagonal matrix, *w* = 2 for tridiagonal, *w* = *n* for dense. The length of the pivot row is at most *w.* There are no more than *w* - 1 nonzeros below any pivot. Each stage of elimination is complete after *w* ( *w* -1) operations, and *the band structure survives.*  There are *n* columns to clear out. Therefore:

#### *Elimination on a band matrix (A to Land U) needs less than w<sup>2</sup>n operations.*

For a band matrix, the count is proportional to n instead of n 3 . It is also proportional to w<sup>2</sup> . A full matrix has *w* = n and we are back to n *.* For an exact count, remember that the bandwidth drops below win the lower right corner (not enough space):

width drops below 
$$w$$
 in the lower right corner (not enough space):

| Band | $\frac{w(w-1)(3n-2w+1)}{3}$ | Dense | $\frac{n(n-1)(n+1)}{3} = \frac{n^3 - n}{3}$ |
|------|-----------------------------|-------|---------------------------------------------|
| 1    | 1                           | 1     | 1                                           |
| 2    | 2                           | 2     | 2                                           |
| 3    | 3                           | 3     | 3                                           |
| 4    | 4                           | 4     | 4                                           |
| 5    | 5                           | 5     | 5                                           |
| 6    | 6                           | 6     | 6                                           |
| 7    | 7                           | 7     | 7                                           |
| 8    | 8                           | 8     | 8                                           |
| 9    | 9                           | 9     | 9                                           |
| 10   | 10                          | 10    | 10                                          |
| 11   | 11                          | 11    | 11                                          |
| 12   | 12                          | 12    | 12                                          |
| 13   | 13                          | 13    | 13                                          |
| 14   | 14                          | 14    | 14                                          |
| 15   | 15                          | 15    | 15                                          |
| 16   | 16                          | 16    | 16                                          |
| 17   | 17                          | 17    | 17                                          |
| 18   | 18                          | 18    | 18                                          |
| 19   | 19                          | 19    | 19                                          |
| 20   | 20                          | 20    | 20                                          |
| 21   | 21                          | 21    | 21                                          |
| 22   | 22                          | 22    | 22                                          |
| 23   | 23                          | 23    | 23                                          |
| 24   | 24                          | 24    | 24                                          |
| 25   | 25                          | 25    | 25                                          |
| 26   | 26                          | 26    | 26                                          |
| 27   | 27                          | 27    | 27                                          |
| 28   | 28                          | 28    | 28                                          |
| 29   | 29                          | 29    | 29                                          |
| 30   | 30                          | 30    | 30                                          |
| 31   | 31                          | 31    | 31                                          |
| 32   | 32                          | 32    | 32                                          |
| 33   | 33                          | 33    | 33                                          |
| 34   | 34                          | 34    | 34                                          |
| 35   | 35                          | 35    | 35                                          |
| 36   | 36                          | 36    | 36                                          |
| 37   | 37                          | 37    | 37                                          |
| 38   | 38                          | 38    | 38                                          |
| 39   | 39                          | 39    | 39                                          |
| 40   | 40                          | 40    | 40                                          |
| 41   | 41                          | 41    | 41                                          |
| 42   | 42                          | 42    | 42                                          |
| 43   | 43                          | 43    | 43                                          |
| 44   | 44                          | 44    | 44                                          |
| 45   | 45                          | 45    | 45                                          |
| 46   | 46                          | 46    | 46                                          |
| 47   | 47                          | 47    | 47                                          |
| 48   | 48                          | 48    | 48                                          |
| 49   | 49                          | 49    | 49                                          |
| 50   | 50                          | 50    | 50                                          |
| 51   | 51                          | 51    | 51                                          |
| 52   | 52                          | 52    | 52                                          |
| 53   | 53                          | 53    | 53                                          |
| 54   | 54                          | 54    | 54                                          |
| 55   | 55                          | 55    | 55                                          |
| 56   | 56                          | 56    | 56                                          |
| 57   | 57                          | 57    | 57                                          |
| 58   | 58                          | 58    | 58                                          |
| 59   | 59                          | 59    | 59                                          |
| 60   | 60                          | 60    | 60                                          |
| 61   | 61                          | 61    | 61                                          |
| 62   | 62                          | 62    | 62                                          |
| 63   | 63                          | 63    | 63                                          |
| 64   | 64                          | 64    | 64                                          |
| 65   | 65                          | 65    | 65                                          |
| 66   | 66                          | 66    | 66                                          |
| 67   | 67                          | 67    | 67                                          |
| 68   | 68                          | 68    | 68                                          |
| 69   | 69                          | 69    | 69                                          |
| 70   | 70                          | 70    | 70                                          |
| 71   | 71                          | 71    | 71                                          |
| 72   | 72                          | 72    | 72                                          |
| 73   | 73                          | 73    | 73                                          |
| 74   | 74                          | 74    | 74                                          |
| 75   | 75                          | 75    | 75                                          |
| 76   | 76                          | 76    | 76                                          |
| 77   | 77                          | 77    | 77                                          |
| 78   | 78                          | 78    | 78                                          |
| 79   | 79                          | 79    | 79                                          |
| 80   | 80                          | 80    | 80                                          |
| 81   | 81                          | 81    | 81                                          |
| 82   | 82                          | 82    | 82                                          |
| 83   | 83                          | 83    | 83                                          |
| 84   | 84                          | 84    | 84                                          |
| 85   | 85                          | 85    | 85                                          |
| 86   | 86                          | 86    | 86                                          |
| 87   | 87                          | 87    | 87                                          |
| 88   | 88                          | 88    | 88                                          |
| 89   | 89                          | 89    | 89                                          |
| 90   | 90                          | 90    | 90                                          |
| 91   | 91                          | 91    | 91                                          |
| 92   | 92                          | 92    | 92                                          |
| 93   | 93                          | 93    | 93                                          |
| 94   | 94                          | 94    | 94                                          |
| 95   | 95                          | 95    | 95                                          |
| 96   | 96                          | 96    | 96                                          |
| 97   | 97                          | 97    | 97                                          |

On the right side of *Ax* = *b,* to find *x* from *b,* the cost is about *2wn* ( compared to the usual n ). *Main point: For a band matrix the operation counts are proportional to n.*  This is extremely fast. A tridiagonal matrix of order 10,000 is very cheap, provided *we don't compute* A- <sup>1</sup> . That inverse matrix has no zeros at all:

$$A = \begin{bmatrix} 1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix} \quad \text{has} \quad A^{-1} = U^{-1} L^{-1} = \begin{bmatrix} 4 & 3 & 2 & 1 \\ 3 & 3 & 2 & 1 \\ 2 & 2 & 2 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix}.$$

We are actually worse off knowing A-<sup>1</sup>than knowing Land *U.* Multiplication by A- <sup>1</sup> needs the full *n* 2 steps. Solving *Le* = *b* and *U x* = c needs only *2wn.* 

A band structure is very common in practice, when the matrix reflects connections between near neighbors:  $a_{13} = 0$  and  $a_{14} = 0$  because 1 is not a neighbor of 3 and 4.

We close with counts for Gauss-Jordan and Gram-Schmidt-Householder:

$$A^{-1} \text{ costs } n^3 \text{ multiply-subtract steps.} \qquad QR \text{ costs } \frac{2}{3} n^3 \text{ steps.}$$

In  $AA^{-1} = I$ , the  $j$ th column of  $A^{-1}$  solves  $Ax_j = j$ th column of  $I$ . The left side costs  $\frac{1}{3}n^3$  as usual. (This is a one-time cost!  $L$  and  $U$  are not repeated.) The special saving for the  $j$ th column of  $I$  comes from its first  $j - 1$  zeros. No work is required on the right side until elimination reaches row  $j$ . The forward cost is  $\frac{1}{2}(n - j)^2$  instead of  $\frac{1}{2}n^2$ . Summing over  $j$ , the total for forward elimination on the  $n$  right sides is  $\frac{1}{6}n^3$ . The final multiply-subtract count for  $A^{-1}$  is  $n^3$  if we actually want the inverse:

$$\text{For } A^{-1} \quad \frac{n^3}{3} (L \text{ and } U) + \frac{n^3}{6} (\text{forward}) + n \left( \frac{n^2}{2} \right) \text{ (back substitutions)} = n^3. \quad (1)$$

**Orthogonalization ( $A$  to  $Q$ ):** The key difference from elimination is that *each multiplier is decided by a dot product*. That takes  $n$  operations, where elimination just divides by the pivot. Then there are  $n$  “multiply-subtract” operations to remove from column  $k$  its projection along column  $j < k$  (see Section 4.4). The combined cost is  $2n$  where for elimination it is  $n$ . This factor 2 is the price of orthogonality. We are changing a dot product to zero where elimination changes an entry to zero.

**Caution** To judge a numerical algorithm, it is **not enough** to count the operations. Beyond “flop counting” is a study of stability (Householder wins) and the flow of data.

## Reordering Sparse Matrices

For band matrices with constant width  $w$ , the row ordering is optimal. But for most sparse matrices in real computations, the width of the band is *not constant* and there are many zeros inside the band. Those zeros can fill in as elimination proceeds—they are lost. We need to *renumber the equations to reduce fill-in*, and thereby speed up elimination.

Generally speaking, we want to move zeros to early rows and columns. Later rows and columns are shorter anyway. The “approximate minimum degree” algorithm in sparse MATLAB is *greedy*—it chooses the row to eliminate without counting all the consequences. We may reach a nearly full matrix near the end, but the total operation count to reach  $LU$  is still much smaller. To find the absolute minimum of nonzeros in  $L$  and  $U$  is an NP-hard problem, much too expensive, and **amd** is a good compromise.

Fill-in is famous when each point on a square grid is connected to its four nearest neighbors. It is impossible to number all the gridpoints so that neighbors stay together! If we number by rows of the grid, there is a long wait to come around to the gridpoint above.

$$\begin{array}{ccc}
 j & \begin{bmatrix} 1 & 1 & 1 \\ -2 & 1 & 0 \\ -2 & 0 & 2 \end{bmatrix} & \longrightarrow & \begin{bmatrix} 1 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 2 & 4 \end{bmatrix} & j = 1 & \begin{array}{c} i = 2 \\ k = 3 \end{array} & \longrightarrow & 1 & \begin{array}{c} 2 \\ \\ \\ 3 \end{array} \\
 a_{32} = 0 & a_{32} = 2 & a_{32} = 0 & \text{before} & a_{32} \neq 0 & \text{after}
 \end{array}$$

We only need the *positions* of the nonzeros, not their exact values. Think of the graph of nonzeros: *Node i is connected to node j if  $a_{ij} \neq 0$* . Watch to see how elimination can create nonzeros (new edges), which we are trying to avoid.

The command **nnz**(*L*) counts the nonzero multipliers in the lower triangular *L*, **find** (*L*) will list them, and **spy**(*L*) shows them all.

The goal of **colamd** and **symamd** is a better ordering (permutation *P*) that reduces fill-in for *AP* and *P*<sup>T</sup>*AP*—by choosing the *pivot with the fewest nonzeros below it*.

### Fast Orthogonalization

There are three ways to reach the important factorization *A = QR*. Gram-Schmidt works to find the orthonormal vectors in *Q*. Then *R* is upper triangular because of the order of Gram-Schmidt steps. Now we look at better methods (Householder and Givens), which use a product of specially simple *Q*'s that we *know* are orthogonal.

Elimination gives *A = LU*, orthogonalization gives *A = QR*. We don't want a triangular *L*, we want an orthogonal *Q*. *L* is a product of *E*'s from elimination, with 1's on the diagonal and the multiplier  $\ell_{ij}$  below. *Q* will be a product of orthogonal matrices.

There are two simple orthogonal matrices to take the place of the *E*'s. The **reflection matrices** *I - 2uu*<sup>T</sup> are named after Householder. The **plane rotation matrices** are named after Givens. The simple matrix that rotates the *xy* plane by  $\theta$  is *Q*<sub>21</sub>:

$$\begin{array}{ll}
 \text{Givens rotation} & Q_{21} = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix}.
 \end{array}$$

Use *Q*<sub>21</sub> the way you used *E*<sub>21</sub>, to produce a zero in the (2, 1) position. That determines the angle  $\theta$ . Bill Hager gives this example in *Applied Numerical Linear Algebra*:

$$Q_{21}A = \begin{bmatrix} .6 & .8 & 0 \\ -.8 & .6 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 90 & -153 & 114 \\ 120 & -79 & -223 \\ 200 & -40 & 395 \end{bmatrix} = \begin{bmatrix} 150 & -155 & -110 \\ 0 & 75 & -225 \\ 200 & -40 & 395 \end{bmatrix}.$$

The zero came from  $-.8(90) + .6(120)$ . No need to find  $\theta$ , what we needed was  $\cos \theta$ :

$$\cos \theta = \frac{90}{\sqrt{90^2 + 120^2}} \quad \text{and} \quad \sin \theta = \frac{-120}{\sqrt{90^2 + 120^2}}. \quad (2)$$

Now we attack the (3, 1) entry. The rotation will be in rows and columns 3 and l. The numbers cos 0 and sin 0 are determined from 150 and 200, instead of 90 and 120.

$$Q_{31}Q_{21}A = \begin{bmatrix} .6 & 0 & .8 \\ 0 & 1 & 0 \\ -.8 & 0 & .6 \end{bmatrix} \begin{bmatrix} 150 & \cdot & \cdot \\ 0 & \cdot & \cdot \\ 200 & \cdot & \cdot \end{bmatrix} = \begin{bmatrix} 250 & -125 & 250 \\ 0 & 75 & -225 \\ 0 & 100 & 325 \end{bmatrix}$$

One more step to *R.* The (3, 2) entry has to go. The numbers cos *0* and sin *0* now come from 75 and 100. The rotation is now in rows and columns 2 and 3:

$$Q_{32}Q_{31}Q_{21}A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & .6 & .8 \\ 0 & -.8 & .6 \end{bmatrix} \begin{bmatrix} 250 & -125 \\ 0 & 75 \\ 0 & 100 \end{bmatrix} = \begin{bmatrix} 250 & -125 \\ 0 & 125 \\ 0 & 0 \end{bmatrix},$$

*We have reached the upper triangular* R. What is Q? Move the plane rotations Qij to the other side to find A = QR-just as you moved the elimination matrices Eij to the other side to find A= LU:

| $Q_{32}Q_{31}Q_{21}A = R$ | means | $A = (Q_{21}^{-1}Q_{31}^{-1}Q_{32}^{-1})R = QR.$ | (3) |
|---------------------------|-------|--------------------------------------------------|-----|
|---------------------------|-------|--------------------------------------------------|-----|

The inverse of each Qij is Q[j (rotation through *-0).* The inverse of Eij was not an orthogonal matrix! L U and QR are similar but L and Q are not the same.

Householder reflections are faster than rotations because each one clears out a whole column below the diagonal. Watch how the first column ai of *A* becomes column ri of R:

The length was not changed, and ui is in the direction of ai - ri. We have n - 1 entries in the unit vector ui to get n - 1 zeros in ri. (Rotations had one angle 0 to get one zero.) When we reach column *k,* we have n - *<sup>k</sup>*available choices in the unit vector *Uk.*  This leads to n - *<sup>k</sup>*zeros in *<sup>r</sup>k* · *We just store the* u *'s and r's to know the final Q and* R:

**Inverse of 
$$H_i$$
 is  $H_i$**     $(H_{n-1} \dots H_1)A = R$    means    $A = (H_1 \dots H_{n-1})R = QR$ . (5)

This is how LAPACK improves on 19th century Gram-Schmidt. *Q* is *exactly* orthogonal.

Section 11.3 explains how *A* = QR is used in the other big computation of linear algebra-the *eigenvalue problem.* The factors QR are reversed to give Ai = RQ which is Q-i AQ. Since Ai is similar to A, the eigenvalues are unchanged. Then Ai is factored into QiRi, and reversing the factors gives A<sup>2</sup> • Amazingly, the entries below the diagonal get smaller in Ai, A<sup>2</sup> , *A3,* ... and we can identify the eigenvalues. This is the "QR method" for *Ax* = *,,\x,* a big success of numerical linear algebra.

## Problem Set 11.1

1 Find the two pivots with and without row exchange to maximize the pivot:

$$A = \begin{bmatrix} .001 & 0 \\ 1 & 1000 \end{bmatrix}.$$

With row exchanges to maximize pivots, why are no entries of  $L$  larger than 1? Find a 3 by 3 matrix  $A$  with all  $|a_{ij}| \leq 1$  and  $|\ell_{ij}| \leq 1$  but third pivot = 4.

2 Compute the exact inverse of the Hilbert matrix  $A$  by elimination. Then compute  $A^{-1}$  again by rounding all numbers to three figures:

**Ill-conditioned matrix** 
$$A = \text{hilb}(3) = \begin{bmatrix} 1 & \frac{1}{2} & \frac{1}{3} \\ \frac{1}{2} & \frac{1}{3} & \frac{1}{4} \\ \frac{1}{3} & \frac{1}{4} & \frac{1}{5} \end{bmatrix}.$$

3 For the same  $A$  compute  $\mathbf{b} = A\mathbf{x}$  for  $\mathbf{x} = (1, 1, 1)$  and  $\mathbf{x} = (0, 6, -3.6)$ . A small change  $\Delta\mathbf{b}$  produces a large change  $\Delta\mathbf{x}$ .

4 Find the eigenvalues (by computer) of the 8 by 8 Hilbert matrix  $a_{ij} = 1/(i+j-1)$ . In the equation  $A\mathbf{x} = \mathbf{b}$  with  $\|\mathbf{b}\| = 1$ , how large can  $\|\mathbf{x}\|$  be? If  $\mathbf{b}$  has roundoff error less than  $10^{-16}$ , how large an error can this cause in  $\mathbf{x}$ ? See Section 9.2.

5 For back substitution with a band matrix (width  $w$ ), show that the number of multiplications to solve  $U\mathbf{x} = \mathbf{c}$  is approximately  $wn$ .

6 If you know  $L$  and  $U$  and  $Q$  and  $R$ , is it faster to solve  $LU\mathbf{x} = \mathbf{b}$  or  $QR\mathbf{x} = \mathbf{b}$ ?

7 Show that the number of multiplications to invert an upper triangular  $n$  by  $n$  matrix is about  $\frac{1}{6}n^3$ . Use back substitution on the columns of  $I$ , upward from 1's.

8 Choosing the largest available pivot in each column (partial pivoting), factor each  $A$  into  $PA = LU$ :

$$A = \begin{bmatrix} 1 & 0 \\ 2 & 2 \end{bmatrix} \quad \text{and} \quad A = \begin{bmatrix} 1 & 0 & 1 \\ 2 & 2 & 0 \\ 0 & 2 & 0 \end{bmatrix}.$$

9 Put 1's on the three central diagonals of a 4 by 4 tridiagonal matrix. Find the cofactors of the six zero entries. Those entries are nonzero in  $A^{-1}$ .

10 (Suggested by C. Van Loan.) Find the  $LU$  factorization and solve by elimination when  $\varepsilon = 10^{-3}, 10^{-6}, 10^{-9}, 10^{-12}, 10^{-15}$ :

$$\begin{bmatrix} \varepsilon & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 + \varepsilon \\ 2 \end{bmatrix}.$$

The true  $\mathbf{x}$  is  $(1, 1)$ . Make a table to show the error for each  $\varepsilon$ . Exchange the two equations and solve again—the errors should almost disappear.

11 (a) Choose sin 0 and cos 0 to triangularize A, and find R:

| Givens rotation | $Q_{21A} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 3 & 5 \end{bmatrix} = \begin{bmatrix} * & * \\ 0 & * \end{bmatrix} = R.$ |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 |                                                                                                                                                                                                     |

(b) Choose sin *0* and cos *0* to make *Q AQ-<sup>1</sup>*triangular. What are the eigenvalues?

12 When *A* is multiplied by a plane rotation *Qij,* which entries of *A* are changed? When *QiJA* is multiplied on the right by Q-;/, which entries are changed now? 13 How many multiplications and how many additions are used to compute *Q ij A?*  Careful organization of the whole sequence of rotations gives jn*3* multiplications and jn*3* additions-the same as for *QR* by reflectors and twice as many as for *LU.* 

### **Challenge Problems**

14 **(Turning** a :robot **hand)** The robot produces any 3 by 3 rotation *A* from plane rotations around the *x, y, z* axes. Then Q32Q31 Q21A **<sup>=</sup>***R,* where *A* is orthogonal so *R*  is I! The three robot turns are in *A* <sup>=</sup>Q·.;]Q3/Q3z1\_ The three angles are "Euler angles" and det *Q* <sup>=</sup>1 to avoid reflection. Start by choosing cos 0 and sin 0 so that

| $Q_{21}A = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \frac{1}{3} \begin{bmatrix} -1 & 2 & 2 \\ 2 & -1 & 2 \\ 2 & 2 & -1 \end{bmatrix}$ is zero in the $(2, 1)$ position. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

15 Create the 10 by 10 second difference matrix *K* **<sup>=</sup>**toepl.itz([2 - 1 zeros(l, 8)]). Permute rows and columns randomly by *KK* **<sup>=</sup>**K(randperm(lO), randperm(lO)). Factor by [L, U] **=** lu(K) and *[LL, UU]* **=** *lu(K K),* and count nonzeros by rmz(L) and *nnz(LL* ). In this case *Lis* in perfect tridiagonal order, but not *LL.*  16 Another ordering for this matrix *K* colors the meshpoints alternately red and black. This permutation *P* changes the normal 1, ... , 10 to 1, 3, 5, 7, 9, 2, 4, 6, 8, 10:

| Red-black ordering | $PKP^T = \begin{bmatrix} 2I & D \\ D^T & 2I \end{bmatrix} \cdot$ | Find the matrix $D$ . |
|--------------------|------------------------------------------------------------------|-----------------------|
|                    |                                                                  |                       |

So many interesting experiments are possible. If you send good ideas they can go on the linear algebra website math.mit.edu/linearalgebra. I also recommend learning the command *B* <sup>=</sup>sparse(A), after which **find(B)** will list the nonzero entries and *fu(B)* will factor *B* using that sparse format for *L* and *U.* Only the nonzeros are computed, where ordinary (dense) MATLAB computes all the zeros too.

17 Jeff Stuart has created a student activity that brilliantly demonstrates ill-conditioning:

$$\begin{bmatrix} 1 & 1.0001 \\ 1 & 1.0000 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 3.0001 + e \\ 3.0000 + E \end{bmatrix}$$
**With errors**     $x = 2 - 10000(e - E)$   
**e and  $E$**      $y = 1 + 10000(e - E)$ 

When those equations are shown by nearly parallel long sticks, a small shake gives a big jump in the crossing point *(x, y).* Errors *e* and *E* are amplified by 10000.

## 11.2 Norms and Condition Numbers

How do we measure the size of a matrix? For a vector, the length is  $\|\mathbf{x}\|$ . For a matrix, *the norm is*  $\|A\|$ . This word “norm” is sometimes used for vectors, instead of length. It is always used for matrices, and there are many ways to measure  $\|A\|$ . We look at the requirements on all “matrix norms” and then choose one.

Frobenius squared all the  $|a_{ij}|^2$  and added; his norm  $\|A\|_F$  is the square root. This treats  $A$  like a long vector with  $n^2$  components: sometimes useful, but not the choice here.

I prefer to start with a vector norm. The triangle inequality says that  $\|\mathbf{x} + \mathbf{y}\|$  is not greater than  $\|\mathbf{x}\| + \|\mathbf{y}\|$ . The length of  $2\mathbf{x}$  or  $-2\mathbf{x}$  is doubled to  $2\|\mathbf{x}\|$ . The same rules will apply to matrix norms:

$$\|A + B\| \leq \|A\| + \|B\| \quad \text{and} \quad \|cA\| = |c| \|A\|. \quad (1)$$

The second requirements for a matrix norm are new, because matrices multiply. The norm  $\|A\|$  controls the growth from  $\mathbf{x}$  to  $A\mathbf{x}$ , and from  $B$  to  $AB$ :

$$\text{Growth factor } \|A\| \quad \|A\mathbf{x}\| \leq \|A\| \|\mathbf{x}\| \quad \text{and} \quad \|AB\| \leq \|A\| \|B\|. \quad (2)$$

This leads to a natural way to define  $\|A\|$ , the norm of a matrix:

$$\text{The norm of } A \text{ is the largest ratio } \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|}: \quad \|A\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|}. \quad (3)$$

 $\|A\mathbf{x}\|/\|\mathbf{x}\|$  is never larger than  $\|A\|$  (its maximum). This says that  $\|A\mathbf{x}\| \leq \|A\| \|\mathbf{x}\|$ .

**Example 1** If  $A$  is the identity matrix  $I$ , the ratios are  $\|\mathbf{x}\|/\|\mathbf{x}\|$ . Therefore  $\|I\| = 1$ . If  $A$  is an orthogonal matrix  $Q$ , lengths are again preserved:  $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ . The ratios still give  $\|Q\| = 1$ . An orthogonal  $Q$  is good to compute with: errors don't grow.

**Example 2** The norm of a diagonal matrix is its largest entry (using absolute values):

$$A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \quad \text{has norm } \|A\| = 3. \quad \text{The eigenvector } \mathbf{x} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \quad \text{has } A\mathbf{x} = 3\mathbf{x}.$$

The eigenvalue is 3. For this  $A$  (but not all  $A$ ), the largest eigenvalue equals the norm.

*For a positive definite symmetric matrix the norm is*  $\|A\| = \lambda_{\max}(A)$ .

Choose  $\mathbf{x}$  to be the eigenvector with maximum eigenvalue. Then  $\|A\mathbf{x}\|/\|\mathbf{x}\|$  equals  $\lambda_{\max}$ . The point is that no other  $\mathbf{x}$  can make the ratio larger. The matrix is  $A = Q\Lambda Q^T$ , and the orthogonal matrices  $Q$  and  $Q^T$  leave lengths unchanged. So the ratio to maximize is really  $\|\Lambda\mathbf{x}\|/\|\mathbf{x}\|$ . The norm is the largest eigenvalue in the diagonal  $\Lambda$ .

**Symmetric matrices** Suppose  $A$  is symmetric but not positive definite.  $A = Q\Lambda Q^T$  is still true. Then the norm is the largest of  $|\lambda_1|, |\lambda_2|, \dots, |\lambda_n|$ . We take absolute values, because the norm is only concerned with length. For an eigenvector  $\|Ax\| = \|\lambda x\| = |\lambda|$  times  $\|x\|$ . The  $x$  that gives the maximum ratio is the eigenvector for the maximum  $|\lambda|$ .

**Unsymmetric matrices** If  $A$  is not symmetric, its eigenvalues may not measure its true size. *The norm can be larger than any eigenvalue.* A very unsymmetric example has  $\lambda_1 = \lambda_2 = 0$  but its norm is not zero:

$$\|A\| > \lambda_{\max} \quad A = \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} \quad \text{has norm} \quad \|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} = 2.$$

The vector  $x = (0, 1)$  gives  $Ax = (2, 0)$ . The ratio of lengths is  $2/1$ . This is the maximum ratio  $\|A\|$ , even though  $x$  is not an eigenvector.

It is the *symmetric matrix*  $A^T A$ , not the unsymmetric  $A$ , that has eigenvector  $x = (0, 1)$ . The norm is really decided by *the largest eigenvalue of  $A^T A$* :

*The norm of  $A$  (symmetric or not) is the square root of  $\lambda_{\max}(A^T A)$ :*

$$\|A\|^2 = \max_{x \neq 0} \frac{\|Ax\|^2}{\|x\|^2} = \max_{x \neq 0} \frac{x^T A^T A x}{x^T x} = \lambda_{\max}(A^T A). \quad (4)$$

The unsymmetric example with  $\lambda_{\max}(A) = 0$  has  $\lambda_{\max}(A^T A) = 4$ :

$$A = \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} \text{ leads to } A^T A = \begin{bmatrix} 0 & 0 \\ 0 & 4 \end{bmatrix} \text{ with } \lambda_{\max} = 4. \text{ So the norm is } \|A\| = \sqrt{4}.$$

**For any  $A$**  Choose  $x$  to be the eigenvector of  $A^T A$  with largest eigenvalue  $\lambda_{\max}$ . The ratio in equation (4) is  $x^T A^T A x = x^T (\lambda_{\max}) x$  divided by  $x^T x$ . This is  $\lambda_{\max}$ .

No  $x$  can give a larger ratio. The symmetric matrix  $A^T A$  has eigenvalues  $\lambda_1, \dots, \lambda_n$  and orthonormal eigenvectors  $q_1, q_2, \dots, q_n$ . Every  $x$  is a combination of those vectors. Try this combination in the ratio and remember that  $q_i^T q_j = 0$ :

$$\frac{x^T A^T A x}{x^T x} = \frac{(c_1 q_1 + \dots + c_n q_n)^T (c_1 \lambda_1 q_1 + \dots + c_n \lambda_n q_n)}{(c_1 q_1 + \dots + c_n q_n)^T (c_1 q_1 + \dots + c_n q_n)} = \frac{c_1^2 \lambda_1 + \dots + c_n^2 \lambda_n}{c_1^2 + \dots + c_n^2}.$$

The maximum ratio  $\lambda_{\max}$  is when all  $c$ 's are zero, except the one that multiplies  $\lambda_{\max}$ .

**Note 1** The ratio in equation (4) is the *Rayleigh quotient* for the symmetric matrix  $A^T A$ . Its maximum is the largest eigenvalue  $\lambda_{\max}(A^T A)$ . The minimum ratio is  $\lambda_{\min}(A^T A)$ . If you substitute any vector  $x$  into the Rayleigh quotient  $x^T A^T A x / x^T x$ , you are guaranteed to get a number between  $\lambda_{\min}(A^T A)$  and  $\lambda_{\max}(A^T A)$ .

**Note 2** The norm  $\|A\|$  equals the *largest singular value*  $\sigma_{\max}$  of  $A$ . The singular values  $\sigma_1, \dots, \sigma_r$  are the square roots of the positive eigenvalues of  $A^T A$ . So certainly  $\sigma_{\max} = (\lambda_{\max})^{1/2}$ . Since  $U$  and  $V$  are orthogonal in  $A = U\Sigma V^T$ , the norm is  $\|A\| = \sigma_{\max}$ .

### The Condition Number of $A$

Section 9.1 showed that roundoff error can be serious. Some systems are sensitive, others are not so sensitive. The sensitivity to error is measured by the *condition number*. This is the first chapter in the book which intentionally introduces errors. We want to estimate how much they change  $x$ .

The original equation is  $Ax = b$ . Suppose the right side is changed to  $b + \Delta b$  because of roundoff or measurement error. The solution is then changed to  $x + \Delta x$ . Our goal is to estimate the change  $\Delta x$  in the solution from the change  $\Delta b$  in the equation. Subtraction gives the *error equation*  $A(\Delta x) = \Delta b$ :

$$\text{Subtract } Ax = b \text{ from } A(x + \Delta x) = b + \Delta b \text{ to find } A(\Delta x) = \Delta b. \quad (5)$$

The error is  $\Delta x = A^{-1}\Delta b$ . It is large when  $A^{-1}$  is large (then  $A$  is nearly singular). The error  $\Delta x$  is especially large when  $\Delta b$  points in the worst direction—which is amplified most by  $A^{-1}$ . *The worst error has*  $\|\Delta x\| = \|A^{-1}\| \|\Delta b\|$ .

This error bound  $\|A^{-1}\|$  has one serious drawback. If we multiply  $A$  by 1000, then  $A^{-1}$  is divided by 1000. The matrix looks a thousand times better. But a simple rescaling cannot change the reality of the problem. It is true that  $\Delta x$  will be divided by 1000, but so will the exact solution  $x = A^{-1}b$ . The *relative error*  $\|\Delta x\|/\|x\|$  will stay the same. It is this relative change in  $x$  that should be compared to the relative change in  $b$ .

Comparing relative errors will now lead to the “condition number”  $c = \|A\| \|A^{-1}\|$ . Multiplying  $A$  by 1000 does not change this number, because  $A^{-1}$  is divided by 1000 and the condition number  $c$  stays the same. It measures the sensitivity of  $Ax = b$ .

*The solution error is less than  $c = \|A\| \|A^{-1}\|$  times the problem error:*

$$\text{Condition number } c \quad \frac{\|\Delta x\|}{\|x\|} \leq c \frac{\|\Delta b\|}{\|b\|}. \quad (6)$$

*If the problem error is  $\Delta A$  (error in  $A$  instead of  $b$ ), still  $c$  controls  $\Delta x$ :*

$$\text{Error } \Delta A \text{ in } A \quad \frac{\|\Delta x\|}{\|x + \Delta x\|} \leq c \frac{\|\Delta A\|}{\|A\|}. \quad (7)$$

**Proof** The original equation is  $b = Ax$ . The error equation (5) is  $\Delta x = A^{-1}\Delta b$ . Apply the key property  $\|Ax\| \leq \|A\|\|x\|$  of matrix norms:

$$\|b\| \leq \|A\| \|x\| \quad \text{and} \quad \|\Delta x\| \leq \|A^{-1}\| \|\Delta b\|.$$

Multiply the left sides to get  $\|b\| \|\Delta x\|$ , and multiply the right sides to get  $c\|x\| \|\Delta b\|$ . Divide both sides by  $\|b\| \|x\|$ . The left side is now the relative error  $\|\Delta x\|/\|x\|$ . The right side is now the upper bound in equation (6).

The same condition number  $c = \|A\| \|A^{-1}\|$  appears when the error is in the matrix. We have  $\Delta A$  instead of  $\Delta b$  in the error equation:

Subtract  $Ax = b$  from  $(A + \Delta A)(x + \Delta x) = b$  to find  $A(\Delta x) = -(\Delta A)(x + \Delta x)$ .

Multiply the last equation by  $A^{-1}$  and take norms to reach equation (7):

$$\|\Delta x\| \leq \|A^{-1}\| \|\Delta A\| \|x + \Delta x\| \quad \text{or} \quad \frac{\|\Delta x\|}{\|x + \Delta x\|} \leq \|A\| \|A^{-1}\| \frac{\|\Delta A\|}{\|A\|}.$$

**Conclusion** Errors enter in two ways. They begin with an error  $\Delta A$  or  $\Delta b$ —a wrong matrix or a wrong  $b$ . This problem error is amplified (a lot or a little) into the solution error  $\Delta x$ . That error is bounded, relative to  $x$  itself, by the condition number  $c$ .

The error  $\Delta b$  depends on computer roundoff and on the original measurements of  $b$ . The error  $\Delta A$  also depends on the elimination steps. Small pivots tend to produce large errors in  $L$  and  $U$ . Then  $L + \Delta L$  times  $U + \Delta U$  equals  $A + \Delta A$ . When  $\Delta A$  or the condition number is very large, the error  $\Delta x$  can be unacceptable.

**Example 3** When  $A$  is symmetric,  $c = \|A\| \|A^{-1}\|$  comes from the eigenvalues:

$$A = \begin{bmatrix} 6 & 0 \\ 0 & 2 \end{bmatrix} \text{ has norm 6.} \quad A^{-1} = \begin{bmatrix} \frac{1}{6} & 0 \\ 0 & \frac{1}{2} \end{bmatrix} \text{ has norm } \frac{1}{2}.$$

This  $A$  is symmetric positive definite. Its norm is  $\lambda_{\max} = 6$ . The norm of  $A^{-1}$  is  $1/\lambda_{\min} = \frac{1}{2}$ . Multiplying norms gives the condition number  $\|A\| \|A^{-1}\| = \lambda_{\max}/\lambda_{\min}$ :

$$\text{Condition number for positive definite } A \quad c = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{6}{2} = 3.$$

**Example 4** Keep the same  $A$ , with eigenvalues 6 and 2. To make  $x$  small, choose  $b$  along the first eigenvector  $(1, 0)$ . To make  $\Delta x$  large, choose  $\Delta b$  along the second eigenvector  $(0, 1)$ . Then  $x = \frac{1}{6}b$  and  $\Delta x = \frac{1}{2}\Delta b$ . The ratio  $\|\Delta x\|/\|x\|$  is exactly  $c = 3$  times the ratio  $\|\Delta b\|/\|b\|$ .

This shows that the worst error allowed by the condition number  $\|A\| \|A^{-1}\|$  can actually happen. Here is a useful rule of thumb, experimentally verified for Gaussian elimination: *The computer can lose log  $c$  decimal places to roundoff error.*

### **Problem Set 11.2**

**<sup>1</sup>**Find the norms IIAII = Amax and condition numbers c = Amax/ Amin of these positive definite matrices:

| $\begin{bmatrix} .5 & 0 \\ 0 & 2 \end{bmatrix}$ | $\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ | $\begin{bmatrix} 3 & 1 \\ 1 & 1 \end{bmatrix}$ |
|-------------------------------------------------|------------------------------------------------|------------------------------------------------|
|-------------------------------------------------|------------------------------------------------|------------------------------------------------|

**<sup>2</sup>**Find the norms and condition numbers from the square roots of >-max(A <sup>T</sup>*A)* and Amin(A<sup>T</sup>*A).* Without positive definiteness in *A,* we go to *A <sup>T</sup>*A!

| $\begin{bmatrix} -2 & 0 \\ 0 & 2 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$ |
|-------------------------------------------------|------------------------------------------------|-------------------------------------------------|
|-------------------------------------------------|------------------------------------------------|-------------------------------------------------|

**<sup>3</sup>**Explain these two inequalities from the definitions (3) of IIAII and IIBII:

$$\|ABx\| \leq \|A\| \|Bx\| \leq \|A\| \|B\| \|x\|.$$

From the ratio of IIABxll to llxll, deduce that IIABII ::; IIAII IIBII- This is the key to using matrix norms. The norm of An is never larger than IIAll<sup>n</sup> .

- 4 Use IIAA-11 :S: IIAII IIA-11 to prove that the condition number is at least l. **<sup>5</sup>**Why is I the only symmetric positive definite matrix that has Amax = Amin = 1? Then the only other matrices with IIAII = 1 and IIA-<sup>1</sup>II = 1 must have *A<sup>T</sup>A= I.* Those are \_\_ matrices: perfectly conditioned. **<sup>6</sup>**Orthogonal matrices have norm IIQII = 1. If *A= QR* show thc>.t IIAII :S: IIRII and also IIRII :S: IIAII- Then IIAII = IIQII IIRII- Find an example of *A* = *LU* with IIAII < IILII IIUll-7 (a) Which famous inequality gives ll(A + B)xll :S: IIAxll + IIBxll for every *x?*
- (b) Why does the definition (3) of matrix norms lead to IIA + BIi :S: IIAII + IIBII? **<sup>8</sup>**Show that if>- is any eigenvalue of *A,* then l>-1 ::; IIAII- Start from *Ax= .\x.* **<sup>9</sup>**The *"spectral radius" p( A)* = l>-max I is the largest absolute value of the eigenvalues. Show with 2 by 2 examples that *p(A* + *B)* ::; *p(A)* + *p(B)* and *p(AB)* ::; *p(A)p(B)* can both be *false.* The spectral radius is not acceptable as a norm. **<sup>10</sup>**(a) Explain why *A* and A-<sup>1</sup>have the same condition number.
- (b) Explain why *A* and *A <sup>T</sup>*have the same norm, based on *>-(A<sup>T</sup>A)* and *>-(AA<sup>T</sup> ).* **<sup>11</sup>**Estimate the condition number of the ill-conditioned matrix *A* = [ � 1. o1oi]. **<sup>12</sup>**Why is the determinant of *A* no good as a norm? Why is it no good as a condition number?

**<sup>13</sup>**(Suggested by C. Moler and C. Van Loan.) Compute b - *Ay* and b - *Az* when

| $b = \begin{bmatrix} .217 \\ .254 \end{bmatrix}$ | $A = \begin{bmatrix} .780 \\ .913 \end{bmatrix}$ | $y = \begin{bmatrix} .341 \\ -.087 \end{bmatrix}$ | $z = \begin{bmatrix} .999 \\ -1.0 \end{bmatrix}$ |
|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------|--------------------------------------------------|
|                                                  |                                                  |                                                   |                                                  |

Is y closer than *z* to solving *Ax* = *b?* Answer in two ways: Compare the *residual <sup>b</sup>*- *Ay* to *b* - *Az.* Then compare *y* and *z* to the true *x* = (1, -1). Both answers can be right. Sometimes we want a small residual, sometimes a small .6.x.

- **<sup>14</sup>**(a) Compute the determinant of *A* in Problem 13. Compute A-<sup>1</sup>
  - (b) If possible compute IIA II and I IA-111 and show that c > 10<sup>6</sup> .

.

**Problems 15-19 are about vector norms other than the usual** llxll = �.

**15** The “ $\ell^1$  norm” and the “ $\ell^\infty$  norm” of  $x = (x_1, \dots, x_n)$  are

$$\|\mathbf{x}\|_1 = |x_1| + \cdots + |x_n| \quad \text{and} \quad \|\mathbf{x}\|_\infty = \max_{1 \leq i \leq n} |x_i|.$$

Compute the norms  $\|\mathbf{x}\|$  and  $\|\mathbf{x}\|_\infty$  and  $\|\mathbf{x}\|_\infty$  of these two vectors in  $\mathbf{R}^5$ :

| $\mathbf{x} = (1, 1, 1, 1, 1)$ | $\mathbf{x} = (.1, .7, .3, .4, .5).$ |
|--------------------------------|--------------------------------------|
|--------------------------------|--------------------------------------|

**16** Prove that  $\|\mathbf{x}\|_\infty \leq \|\mathbf{x}\| \leq \|\mathbf{x}\|_1$ . Show from the Schwarz inequality that the ratios  $\|\mathbf{x}\|_1/\|\mathbf{x}\|_\infty$  and  $\|\mathbf{x}\|_1/\|\mathbf{x}\|$  are never larger than  $\sqrt{n}$ . Which vector  $(x_1, \dots, x_n)$  gives ratios equal to  $\sqrt{n}$ ?

**<sup>17</sup>**All vector norms must satisfy the *triangle inequality.* Prove that

| $\ \mathbf{x} + \mathbf{y}\ _\infty \leq \ \mathbf{x}\ _\infty + \ \mathbf{y}\ _\infty$ | and | $\ \mathbf{x} + \mathbf{y}\ _1 \leq \ \mathbf{x}\ _1 + \ \mathbf{y}\ _1$ |
|-----------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------|
|                                                                                         |     |                                                                          |

**<sup>18</sup>**Vector norms must also satisfy llcxl l = lei llxll- The norm must be positive except when x = 0. Which of these are norms for vectors ( x 1, x 2) in R <sup>2</sup> ?

$$\|\mathbf{x}\|_A = |x_1| + 2|x_2| \quad \|\mathbf{x}\|_B = \min (|x_1|, |x_2|)$$

| $\ \mathbf{x}\ _C = \ \mathbf{x}\  + \ \mathbf{x}\ _\infty$ | $\ \mathbf{x}\ _D = \ A\mathbf{x}\ $ | (this answer depends on $A$ ). |
|-------------------------------------------------------------|--------------------------------------|--------------------------------|
|                                                             |                                      |                                |

# **Challenge Problems**

- 19 Show that  $\mathbf{x}^T \mathbf{y} \leq \|\mathbf{x}\|_1 \|\mathbf{y}\|_\infty$  by choosing components  $y_i = \pm 1$  to make  $\mathbf{x}^T \mathbf{y}$  as large as possible.
- 20 The eigenvalues of the  $-1, 2, -1$  difference matrix  $K$  are  $\lambda = 2 - 2 \cos(j\pi/n+1)$ . Estimate  $\lambda_{\min}$  and  $\lambda_{\max}$  and  $c = \text{cond}(K) = \lambda_{\max}/\lambda_{\min}$  as  $n$  increases:  $c \approx Cn^2$  with what constant  $C$ ?

Test this estimate with eig(K) and **cond(K)** for n = 10, 100, 1000.

### **11.3 Iterative Methods and Preconditioners**

Up to now, our approach to *Ax* = *b* has been direct. We accepted *A* as it came. We attacked it by elimination with row exchanges. We now look at **iterative methods, which replace** A **by a simpler matrix** *S.* The difference *T* = *S* - *A* is moved over to the right side of the equation. The problem becomes easier to solve, with *S* instead of *A.* But there is a price-the *simpler system has to be solved over and over.* 

An iterative method is easy to invent. Just split *A* (carefully) into *S* - *T.* 

| <b>Rewrite <math display="block">Ax = b</math></b> | $x = Tx + b$ | (1) |
|----------------------------------------------------|--------------|-----|
|----------------------------------------------------|--------------|-----|

The novelty is to solve (1) iteratively. Each guess *Xk* leads to the next *Xk+I:* 

| <b>Pure iteration</b> | $Sx_{k+1} = Tx_k + \mathbf{b}$ | (2) |
|-----------------------|--------------------------------|-----|
|-----------------------|--------------------------------|-----|

Start with any *x0.* Then solve *Sx1* = *Tx0* + *b.* Continue to *Sx2* = *Tx1* + *b.* A hundred iterations are very common-often more. Stop when (and if!) *Xk+I* is sufficiently close to *Xk-or* when the **residual** *Tk* = *b* - *Axk* is near zero. Our hope is to get near the true solution, more quickly than by elimination. When the *Xk* converge, their limit *x00* does solve equation (1): *Sx00* = *Tx00*+ *b* means *Ax00* = *b.* 

The two goals of the splitting *A* = *S* - *T* are *speed per step* and *fast convergence.*  The speed of each step depends on Sand the speed of convergence depends on *s-1r:*

1 Equation (2) should be easy to solve for *Xk+i·* The *"preconditioner" S* could be the diagonal or triangular part of *A.* A fast way uses *S* = *L0U0,* where those factors have many zeros compared to the exact *A= LU.* This is *"incomplete LU".*  2 The difference *x* - *Xk* (this is the error *ek)* should go quickly to zero. Subtracting equation (2) from (1) cancels *b,* and it leaves the *equation for the error ek:* 

| Error equation | $sek_{+1} = Te_k$ | which means | $e_{k+1} = s^{-1}Te_k$ | (3) |
|----------------|-------------------|-------------|------------------------|-----|
|                |                   |             |                        |     |

At every step the error is multiplied by *s-1r.* If *s-1r* is small, its powers go quickly to zero. But what is "small"?

The extreme splitting is *S* = *A* and *T* = 0. Then the first step of the iteration is the original *Ax* = *b.* Convergence is perfect and *s- 1r* is zero. But the cost of that step is what we wanted to avoid. The choice of Sis a battle between speed per step (a simple S) and fast convergence *(S* close to A). Here are some choices of *S:* 

J *S* = diagonal part of *A* (the iteration is called *Jacobi's method)*  **GS** *S* = lower triangular part of *A* including the diagonal ( *Gauss-Seidel method)*  **ILU** *S* = approximate *L* times approximate *U (incomplete LU method).* 

Our first question is pure linear algebra: *When do the* Xk *'s converge to x?* The answer uncovers the number l>-l max that controls convergence. In examples of Jacobi and Gauss-Seidel, we will compute this *"spectral radius"* l>-l max · It is the largest eigenvalue of the *iteration matrix B* = *s-1r.* 

# **The Spectral Radius** *p(B)* **Controls Convergence**

Equation (3) is ek+I = *s-1*Tek. Every iteration step multiplies the error by the same matrix B = *s-1*T. The error after k steps is ek = Bkea. *The error approaches zero if the powers of B* = *s- <sup>1</sup>*T *approach zero.* It is beautiful to see how the eigenvalues of B-the largest eigenvalue in particular-control the matrix powers B<sup>k</sup> .

The powers Bk approach zero if and only if every eigenvalue of B has l>-1 < 1. *The rate of convergence is controlled by the spectral radius of B: p* = max I,\ ( *B)* 1-

*The test for convergence is* l>-l max < 1. Real eigenvalues must lie between -1 and 1. Complex eigenvalues>-= *a+ ib* must have l>-1 <sup>2</sup>= a<sup>2</sup>+ b <sup>2</sup>< 1. The spectral radius *"rho"* is the largest distance from Oto the eigenvalues of B = *s-1*T. This is *p* = l>-l max ·

To see why l>-l max < 1 is necessary, suppose the starting error ea happens to be an eigenvector of B. After one step the error is Beo = >-ea. After k steps the error is Bkeo = *A k* ea. If we start with an eigenvector, we continue with that eigenvector-and the *factor* ,>\_ <sup>k</sup>*only goes to zero when* l>-1 < 1. This condition is required of every eigenvalue.

To see why l>-l max < 1 is sufficient for the error to approach zero, suppose eo is a combination of eigenvectors:

| $e_0 = c_1 x_1 + \dots + c_n x_n$ | leads to | $e_k = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$ |  |
|-----------------------------------|----------|-------------------------------------------------------------|--|
|                                   |          |                                                             |  |

This is the point of eigenvectors! When we multiply by *B,* each eigenvector *Xi* is multiplied by Ai- If all I Ai I < 1 then equation ( 4) ensures that eJc goes to zero.

| Example 1 | $B = \begin{bmatrix} .6 & .5 \\ .6 & .5 \end{bmatrix}$ | has $\lambda_{\max} = 1.1$ | $B' = \begin{bmatrix} .6 & 1.1 \\ 0 & .5 \end{bmatrix}$ | has $\lambda_{\max} = .6$ |
|-----------|--------------------------------------------------------|----------------------------|---------------------------------------------------------|---------------------------|
|-----------|--------------------------------------------------------|----------------------------|---------------------------------------------------------|---------------------------|

B2 is 1.1 times B. Then B*3* is (1.1)2 times B. The powers of B will blow up. Contrast with the powers of *B'.* The matrix *(B') <sup>k</sup>*has (.6)k and (.5)k on its diagonal. The off-diagonal entries also involve p <sup>k</sup>= ( *.6) <sup>k</sup> ,* which sets the speed of convergence.

**Note** When there are too few eigenvectors, equation ( 4) is not correct. We turn to the *Jordan form* when eigenvectors are missing and the matrix *B* can't be diagonalized:

| Jordan form $J$ | $B = MJM^{-1}$ | and | $B^k = MJ^kM^{-1}$ . | (5) |
|-----------------|----------------|-----|----------------------|-----|
|                 |                |     |                      |     |

Section 8.3 shows how J and J <sup>k</sup>are made of "blocks" with one repeated eigenvalue:

| The powers of a 2 by 2 block in $J$ are | $\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}^k = \begin{bmatrix} \lambda^k & \lambda k^{k-1} \\ 0 & \lambda^k \end{bmatrix}$ |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|

If  $|\lambda| < 1$  then these powers approach zero. The extra factor  $k$  from a double eigenvalue is overwhelmed by the decreasing factor  $\lambda^{k-1}$ . This applies to every block:

**Diagonalizable or not: Convergence  $B^k \rightarrow 0$  and its speed depend on  $\rho = |\lambda|_{\max} < 1$ .**

### Jacobi versus Gauss-Seidel

We now solve a specific 2 by 2 problem by splitting  $A$ . Watch for that number  $|\lambda|_{\max}$ .

$$Ax = b \quad \begin{array}{l} 2u - v = 4 \\ -u + 2v = -2 \end{array} \quad \text{has the solution} \quad \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}. \quad (6)$$

The first splitting is **Jacobi's method**. Keep the *diagonal* of  $A$  on the left side (this is  $S$ ). Move the off-diagonal part of  $A$  to the right side (this is  $T$ ). Then iterate:

| <b>Jacobi iteration</b> | $Sx_{k+1} = Tx_k + b$ | $\begin{array}{l} 2u_{k+1} = v_k + 4 \\ 2v_{k+1} = u_k - 2. \end{array}$ |
|-------------------------|-----------------------|--------------------------------------------------------------------------|
|-------------------------|-----------------------|--------------------------------------------------------------------------|

Start from  $u_0 = v_0 = 0$ . The first step finds  $u_1 = 2$  and  $v_1 = -1$ . Keep going:

$$\begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1 \end{bmatrix} \quad \begin{bmatrix} 3/2 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1/4 \end{bmatrix} \quad \begin{bmatrix} 15/8 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1/16 \end{bmatrix} \quad \text{approaches} \quad \begin{bmatrix} 2 \\ 0 \end{bmatrix}.$$

This shows convergence. At steps 1, 3, 5 the second component is  $-1, -1/4, -1/16$ . Those drop by 4 in each two steps. The error equation is  $Se_{k+1} = Te_k$ :

$$\text{Error equation} \quad \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} e_{k+1} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} e_k \quad \text{or} \quad e_{k+1} = \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix} e_k. \quad (7)$$

That last matrix  $S^{-1}T$  has eigenvalues  $\frac{1}{2}$  and  $-\frac{1}{2}$ . So its spectral radius is  $\rho(B) = \frac{1}{2}$ :

$$B = S^{-1}T = \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix} \quad \text{has} \quad |\lambda|_{\max} = \frac{1}{2} \quad \text{and} \quad \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix}^2 = \begin{bmatrix} \frac{1}{4} & 0 \\ 0 & \frac{1}{4} \end{bmatrix}.$$

Two steps multiply the error by  $\frac{1}{4}$  exactly, in this special example. The important message is this: Jacobi's method works well when the main diagonal of  $A$  is large compared to the off-diagonal part. The diagonal part is  $S$ , the rest is  $-T$ . We want the diagonal to dominate.

The eigenvalue  $\lambda = \frac{1}{2}$  is unusually small. Ten iterations reduce the error by  $2^{10} = 1024$ . More typical and more expensive is  $|\lambda|_{\max} = .99$  or .999.

The **Gauss-Seidel method** keeps the whole lower triangular part of  $A$  as  $S$ :

$$\begin{array}{lll} \text{Gauss-Seidel} & 2u_{k+1} & = v_k + 4 \\ & -u_{k+1} + 2v_{k+1} & = -2 \end{array} \quad \text{or} \quad \begin{array}{l} u_{k+1} = \frac{1}{2}v_k + 2 \\ v_{k+1} = \frac{1}{2}u_{k+1} - 1. \end{array} \quad (8)$$

Notice the change. The new  $u_{k+1}$  from the first equation is used *immediately* in the second equation. With Jacobi, we saved the old  $u_k$  until the whole step was complete. With Gauss-Seidel, the new values enter right away and the old  $u_k$  is destroyed. This cuts the storage in half. It also speeds up the iteration (usually). And it costs no more than the Jacobi method.

Test the iteration starting from another start *<sup>u</sup>0* <sup>=</sup>0 and *<sup>v</sup>0* <sup>=</sup>-1:

| $\begin{bmatrix} 0 \\ -1 \end{bmatrix}$ | $\begin{bmatrix} 3/2 \\ -1/4 \end{bmatrix}$ | $\begin{bmatrix} 15/8 \\ -1/16 \end{bmatrix}$ | $\begin{bmatrix} 63/32 \\ -1/64 \end{bmatrix}$ | approaches | $\begin{bmatrix} 2 \\ 0 \end{bmatrix}$ |
|-----------------------------------------|---------------------------------------------|-----------------------------------------------|------------------------------------------------|------------|----------------------------------------|
|-----------------------------------------|---------------------------------------------|-----------------------------------------------|------------------------------------------------|------------|----------------------------------------|

The errors in the first component are 2, 1/2, 1/8, 1/32. The errors in the second component are -1, -1/4, -1/16, -1/32. We divide by 4 in one step not two steps. *Gauss-Seidel is twice as fast as Jacobi.* We have PGs = (PJ) 2 when *A* is positive definite tridiagonal:

| $S = \begin{bmatrix} 2 & 0 \\ -1 & 2 \end{bmatrix} \quad \text{and} \quad T = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \quad \text{and} \quad S^{-1}T = \begin{bmatrix} 0 & \frac{1}{2} \\ 0 & \frac{1}{4} \end{bmatrix}.$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The Gauss-Seidel eigenvalues are O and ¼- Compare with ½ and -½ for Jacobi.

With a small push we can describe the *successive overrelaxation method* **(SOR).** The new idea is to introduce a parameter *w* (omega) into the iteration. Then choose this number *w* to make the spectral radius of *s-<sup>1</sup><sup>r</sup>*as small as possible.

Rewrite *Ax* = *bas wAx* = *wb.* The matrix *Sin* **SOR** has the diagonal of the original *A,* but below the diagonal we use *wA.* On the right side Tis *S* - *wA:*

| SOR | $2u_{k+1} = (2 - 2\omega)u_k + \frac{\omega v_k + 4\omega}{(2 - 2\omega)v_k - 2\omega}$ $-\omega u_{k+1} + 2v_{k+1} =$ | (9) |
|-----|------------------------------------------------------------------------------------------------------------------------|-----|
|-----|------------------------------------------------------------------------------------------------------------------------|-----|

This looks more complicated to us, but the computer goes as fast as ever. SOR is like Gauss-Seidel, with an adjustable number *w.* The best *w* makes it faster.

I will put on record the most valuable test matrix of order *n.* It is our favorite -1, 2, -1 tridiagonal matrix *K.* The diagonal is 2I. Below and above are -1 's. Our example had n = 2, which leads to cos i = ½ as the Jacobi eigenvalue found above. Notice especially that this 1>-lmax is squared for Gauss-Seidel:

The splittings of the -1, 2, -1 matrix *K* of order *n* yield these eigenvalues of B:

**Jacobi** (S = 0, 2, 0 matrix):

**Gauss-Seidel** *(S* = -1, 2, 0 matrix):

$$S^{-1}T \text{ has } |\lambda|_{\max} = \cos \frac{\pi}{n+1}$$

$$S^{-1}T \text{ has } |\lambda|_{\max} = \left( \cos \frac{\pi}{n+1} \right)^2$$

**SOR** (with the best 
$$\omega$$
):  $S^{-1}T$  has  $|\lambda|_{\max} = \left( \cos \frac{\pi}{n+1} \right)^2 / \left( 1 + \sin \frac{\pi}{n+1} \right)^2$ .

Let me be clear: For the -1, 2, -1 matrix you should not use any of these iterations! Elimination on a tridiagonal matrix is very fast (exact *LU).* Iterations are intended for a large sparse matrix that has nonzeros far from the central diagonal. Those create many more nonzeros in the exact Land *U.* This **fill-in** is why elimination becomes expensive.

We mention one more splitting. The idea of *"incomplete* LU" is to set the small nonzeros in L and U *back to zero.* This leaves triangular matrices Lo and U0 which are again sparse. The splitting has *S* = *L0U0* on the left side. Each step is quick:

| Incomplete LU | $L_0U_0x_{k+1} = (L_0U_0 - A)x_k + b.$ |
|---------------|----------------------------------------|
|               |                                        |

On the right side we do sparse matrix-vector multiplications. Don't multiply Lo times *U0,*  those are matrices. Multiply Xk by *U0* and then multiply that vector by *L0.* On the left side we do forward and back substitutions. If *L0U0*is close to *A,* then i>-l max is small. A few iterations will give a close answer.

# **Multigrid and Conjugate Gradients**

I cannot leave the impression that Jacobi and Gauss-Seidel are great methods. Generally the "low-frequency" part of the error decays very slowly, and many iterations are needed. Here are two important ideas that bring tremendous improvement. **Multigrid** can solve problems of size n in 0( n) steps. With a good preconditioner, **conjugate gradients** becomes one of the most popular and powerful algorithms in numerical linear algebra.

*Multigrid* Solve smaller problems with coarser grids. Each iteration will be cheaper and faster. Then interpolate between the coarse grid values to get a quick headstart on the full-size problem. Multigrid might go 4 levels down and back.

*Conjugate gradients* An ordinary iteration like Xk+l = Xk - Axk+ *b* involves multiplication by A at each step. If A is sparse, this is not too expensive: Axk is what we are willing to do. It adds one more basis vector to the growing "Krylov spaces" that contain our approximations. But Xk+l is **not the best combination** of xo, Ax<sup>o</sup> , ... , A <sup>k</sup>xo. The ordinary iterations are simple but far from optimal.

The conjugate gradient method chooses **the best combination** Xk at every step. The extra cost (beyond one multiplication by *A)* is not great. We will give the CG iteration, emphasizing that this method was created for a *symmetric positive definite matrix.* When A is not symmetric, one good choice is GMRES. When A = A <sup>T</sup>is not positive definite, there is MINRES. A world of high-powered iterative methods has been created around the idea of making optimal choices of each successive X<sup>k</sup> .

My textbook *Computational Science and Engineering* describes multigrid and CG in much more detail. Among books on numerical linear algebra, Trefethen-Bau is deservedly popular ( others are terrific too). Golub-Van Loan is a level up.

The Problem Set reproduces the five steps in each conjugate gradient cycle from Xk-l to X<sup>k</sup> . We compute that new approximation Xk, the new residual rk= *b* - Axk, and the new search direction dk to look for the next Xk+l·

I wrote those steps for the original matrix *A.* But a **preconditioner** *S* can make convergence much faster. Our original equation is Ax = *b.* The preconditioned equation is s- <sup>1</sup>Ax = *s-<sup>1</sup> b.* Small changes in the code give the *preconditioned conjugate gradient method-the* leading iterative method to solve positive definite systems.

The biggest competition is direct elimination, with the equations reordered to take maximum advantage of the zeros in  $A$ . It is not easy to outperform Gauss.

## Iterative Methods for Eigenvalues

We move from  $Ax = b$  to  $Ax = \lambda x$ . Iterations are an option for linear equations. They are a necessity for eigenvalue problems. The eigenvalues of an  $n$  by  $n$  matrix are the roots of an  $n$ th degree polynomial. The determinant of  $A - \lambda I$  starts with  $(-\lambda)^n$ . This book must not leave the impression that eigenvalues should be computed that way! Working from  $\det(A - \lambda I) = 0$  is a *very poor approach*—except when  $n$  is small.

For  $n > 4$  there is no formula to solve  $\det(A - \lambda I) = 0$ . Worse than that, the  $\lambda$ 's can be very unstable and sensitive. It is much better to work with  $A$  itself, gradually making it diagonal or triangular. (Then the eigenvalues appear on the diagonal.) Good computer codes are available in the LAPACK library—individual routines are free on [www.netlib.org/lapack](http://www.netlib.org/lapack). This library combines the earlier LINPACK and EISPACK, with many improvements (to use matrix-matrix operations in the Level 3 BLAS). It is a collection of Fortran 77 programs for linear algebra on high-performance computers. For your computer and mine, a high quality matrix package is all we need. For supercomputers with parallel processing, move to ScaLAPACK and block elimination.

We will briefly discuss the power method and the  $QR$  method (chosen by LAPACK) for computing eigenvalues. It makes no sense to give full details of the codes.

**1 Power methods and inverse power methods.** Start with any vector  $u_0$ . Multiply by  $A$  to find  $u_1$ . Multiply by  $A$  again to find  $u_2$ . If  $u_0$  is a combination of the eigenvectors, then  $A$  multiplies each eigenvector  $x_i$  by  $\lambda_i$ . After  $k$  steps we have  $(\lambda_i)^k$ :

$$u_k = A^k u_0 = c_1(\lambda_1)^k x_1 + \cdots + c_n(\lambda_n)^k x_n. \quad (10)$$

As the power method continues, *the largest eigenvalue begins to dominate*. The vectors  $u_k$  point toward that dominant eigenvector  $x_1$ . We saw this for Markov matrices:

$$A = \begin{bmatrix} .9 & .3 \\ .1 & .7 \end{bmatrix} \quad \text{has} \quad \lambda_{\max} = 1 \quad \text{with eigenvector} \quad \begin{bmatrix} .75 \\ .25 \end{bmatrix}.$$

Start with  $u_0$  and multiply at every step by  $A$ :

$$u_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad u_1 = \begin{bmatrix} .9 \\ .1 \end{bmatrix}, \quad u_2 = \begin{bmatrix} .84 \\ .16 \end{bmatrix} \quad \text{is approaching} \quad u_\infty = \begin{bmatrix} .75 \\ .25 \end{bmatrix}.$$

The speed of convergence depends on the *ratio* of the second largest eigenvalue  $\lambda_2$  to the largest  $\lambda_1$ . We don't want  $\lambda_1$  to be small, we want  $\lambda_2/\lambda_1$  to be small. Here  $\lambda_2 = .6$  and  $\lambda_1 = 1$ , giving good speed. For large matrices it often happens that  $|\lambda_2/\lambda_1|$  is very close to 1. Then the power method is too slow.

Is there a way to find the *smallest* eigenvalue—which is often the most important in applications? Yes, by the *inverse* power method: Multiply  $u_0$  by  $A^{-1}$  instead of  $A$ . Since we never want to compute  $A^{-1}$ , we actually solve  $Au_1 = u_0$ . By saving the  $LU$  factors, the next step  $Au_2 = u_1$  is fast. Step  $k$  has  $Au_k = u_{k-1}$ :

**Inverse power method**

$$u_k = A^{-k} u_0 = \frac{c_1 x_1}{(\lambda_1)^k} + \cdots + \frac{c_n x_n}{(\lambda_n)^k}. \quad (11)$$

Now the *smallest* eigenvalue  $\lambda_{\min}$  is in control. When it is very small, the factor  $1/\lambda_{\min}^k$  is large. For high speed, we make  $\lambda_{\min}$  even smaller by shifting the matrix to  $A - \lambda^* I$ .

That shift doesn't change the eigenvectors. ( $\lambda^*$  might come from the diagonal of  $A$ , even better is a Rayleigh quotient  $x^T A x / x^T x$ ). If  $\lambda^*$  is close to  $\lambda_{\min}$  then  $(A - \lambda^* I)^{-1}$  has the very large eigenvalue  $(\lambda_{\min} - \lambda^*)^{-1}$ . Each *shifted inverse power step* multiplies the eigenvector by this big number, and that eigenvector quickly dominates.

**2 The QR Method** This is a major achievement in numerical linear algebra. Sixty years ago, eigenvalue computations were slow and inaccurate. We didn't even realize that solving  $\det(A - \lambda I) = 0$  was a terrible method. Jacobi had suggested earlier that  $A$  should gradually be made triangular—then the eigenvalues appear automatically on the diagonal. He used 2 by 2 rotations to produce off-diagonal zeros. (Unfortunately the previous zeros can become nonzero again. But Jacobi's method made a partial comeback with parallel computers.) The *QR method* is now a leader in eigenvalue computations.

The basic step is to factor  $A$ , whose eigenvalues we want, into  $QR$ . Remember from Gram-Schmidt (Section 4.4) that  $Q$  has orthonormal columns and  $R$  is triangular. For eigenvalues the key idea is: *Reverse Q and R*. The new matrix (same  $\lambda$ 's) is  $A_1 = RQ$ . The eigenvalues are not changed in  $RQ$  because  $A = QR$  is similar to  $A_1 = Q^{-1} AQ$ :

$$A_1 = RQ \text{ has the same } \lambda \quad QRx = \lambda x \quad \text{gives} \quad RQ(Q^{-1}x) = \lambda(Q^{-1}x). \quad (12)$$

This process continues. Factor the new matrix  $A_1$  into  $Q_1 R_1$ . Then reverse the factors to  $R_1 Q_1$ . This is the similar matrix  $A_2$  and again no change in the eigenvalues. Amazingly, those eigenvalues begin to show up on the diagonal. Soon the last entry of  $A_4$  holds an accurate eigenvalue. In that case we remove the last row and column and continue with a smaller matrix to find the next eigenvalue.

Two extra ideas make this method a success. One is to shift the matrix by a multiple of  $I$ , before factoring into  $QR$ . Then  $RQ$  is shifted back to give  $A_{k+1}$ :

Factor  $A_k - c_k I$  into  $Q_k R_k$ . The next matrix is  $A_{k+1} = R_k Q_k + c_k I$ .

 $A_{k+1}$  has the same eigenvalues as  $A_k$ , and the same as the original  $A_0 = A$ . A good shift chooses  $c$  near an (unknown) eigenvalue. That eigenvalue appears more accurately on the diagonal of  $A_{k+1}$ —which tells us a better  $c$  for the next step to  $A_{k+2}$ .

The second idea is to obtain off-diagonal zeros before the  $QR$  method starts. An elimination step  $E$  will do it, or a Givens rotation, but don't forget  $E^{-1}$  (or  $\lambda$  will change):

$$EAE^{-1} = \begin{bmatrix} 1 & & \\ & 1 & \\ & & -1 \\ & & & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 1 & 4 & 5 \\ 1 & 6 & 7 \end{bmatrix} \begin{bmatrix} 1 & & \\ & 1 & \\ & & 1 \\ 1 & & 1 \end{bmatrix} = \begin{bmatrix} 1 & 5 & 3 \\ 1 & 9 & 5 \\ 0 & 4 & 2 \end{bmatrix}. \text{ Same } \lambda \text{'s.}$$

We must leave those nonzeros 1 and 4 along *one subdiagonal*. More  $E$ 's could remove them, but  $E^{-1}$  would fill them in again. This is a “*Hessenberg matrix*” (one nonzero

subdiagonal). The zeros in the lower left corner will stay zero through the *QR* method. The operation count for each *QR* factorization drops from O(n<sup>3</sup> ) to O(n<sup>2</sup> ).

Golub and Van Loan give this example of one shifted *QR* step on a Hessenberg matrix. The shift is 7 *I,* taking 7 from all diagonal entries of *A* (then shifting back for A<sup>1</sup> ):

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 0 & .001 & 7 \end{bmatrix} \quad \text{leads to} \quad A_1 = \begin{bmatrix} -.54 & 1.69 & 0.835 \\ .31 & 6.53 & -6.656 \\ 0 & .00002 & 7.012 \end{bmatrix}.$$

Factoring *A-* 7 *I* into *QR* produced A1 = *RQ* + 7 *I.* Notice the very small number .00002. The diagonal entry 7.012 is almost an exact eigenvalue of A<sup>1</sup> , and therefore of *A.* Another *QR* step on A1 with shift by 7.0121 would give terrific accuracy.

For a few eigenvalues of a large sparse matrix I would look to **ARPACK.** Problems 25-27 describe the Arnoldi iteration that orthogonalizes the basis-each step has only three terms when *A* is symmetric. The matrix becomes *tridiagonal:* a wonderful start for computing eigenvalues.

# **Problem Set 11.3**

**Problems 1-12 are about iterative methods for** *Ax* = *b.* 

1 Change Ax = *b* to x = *(I* -A)x +*b.* What are S and T for this splitting? What matrix s-*1*y controls the convergence of Xk+l = *(I* - A)xk +*b?* 2 If *A* is an eigenvalue of *A,* then \_\_ is an eigenvalue of *B* = *I* - *A.* The real eigenvalues of *B* have absolute value less than 1 if the real eigenvalues of *A* lie between and 3 Show why the iteration Xk+l = *(I* -A)xk + *b* does not converge for A= [ \_i -�]. 4 Why is the norm of Bk never larger than II BIi <sup>k</sup> ? Then IIBII < 1 guarantees that the powers Bk approach zero (convergence). No surprise since l>-lmax is below IIBll-**<sup>5</sup>**If *A* is singular then all splittings A = S - T must fail. From Ax = 0 show that *s-<sup>1</sup>rx* = *X.* So this matrix *B* = *s-<sup>1</sup>r*has>.= 1 and fails. 6 Change the 2's to 3's and find the eigenvalues of s- *<sup>1</sup>*y for Jacobi's method:

$$Sx_{k+1} = Tx_k + b \quad \text{is} \quad \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} x_{k+1} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} x_k + b.$$

7 Find the eigenvalues of s-*1*y for the Gauss-Seidel method applied to Problem 6:

| $\begin{bmatrix} 3 & 0 \\ -1 & 3 \end{bmatrix} x_{k+1} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} x_k + b.$ |
|-----------------------------------------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------------------------------------------|

8 For any 2 by 2 matrix [ � �] show that [>-[max equals [be/ *ad[* for Gauss-Seidel and [be/ *ad[* <sup>1</sup> /<sup>2</sup>for Jacobi. We need *ad* =f. 0 for the matrix *S* to be invertible. 9 Write a computer code (MATLAB or other) for the Gauss-Seidel method. You can define *S* and *T* from *A,* or set up the iteration loop directly from the entries *aij .* Test it on the -1, 2, -1 matrices A of order 10, 20, 50 with b = (1, 0, ... ,0). 10 The Gauss-Seidel iteration at component i uses earlier parts of xnew:

$$\text{Gauss-Seidel} \quad x_i^{\text{new}} = x_i^{\text{old}} + \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{\text{new}} - \sum_{j=1}^n a_{ij} x_j^{\text{old}} \right).$$

If every xr ew =x? 1d how does this show that the solution *X* is correct? How does the formula change for Jacobi's method? For SOR insert w outside the parentheses.

11 Divide equation ( 10) by A� and explain why I >-2 / A1 I controls the convergence of the power method. Construct a matrix *A* for which this method *does not converge.*  12 The Markov matrix *A* = [ :i J] has A = 1 and .6, and the power method *U<sup>k</sup> A<sup>k</sup>u0* converges to [ :��]. Find the eigenvectors of A-<sup>1</sup> . What does the inverse power method *u\_ <sup>k</sup>*= *A- <sup>k</sup>u0* converge to (after you multiply by .6<sup>k</sup> )? 13 The tridiagonal matrix of size n - 1 with diagonals -1, 2, -1 has eigenvalues *<sup>A</sup>j*= 2 - 2cos(j1r/n). Why are the smallest eigenvalues approximately (j1r/n)<sup>2</sup> ? The inverse power method converges at the speed >-i/ >-2 :::::: 1 / 4. 14 For *A* = [ \_i -�] apply the power method *Uk+i* = *Auk* three times starting with u*0* = [ 5]. What eigenvector is the power method converging to? 15 For *A=* -1, 2, -1 matrix, apply the *inverse* power method *Uk+l* = *A-1uk* three times with the same u*0.* What eigenvector are the *Uk* 's approaching? 16 In the *QR* method for eigenvalues when *A* is shifted to make A22 = 0, show that the 2, 1 entry drops from sin *0* in *A= QR* to - sin<sup>3</sup>*0* in *RQ. (Compute Rand RQ.)* This "cubic convergence" makes the method a success:

$$A = \begin{bmatrix} \cos \theta & \sin \theta \\ \sin \theta & 0 \end{bmatrix} = QR = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 & ? \\ 0 & ? \end{bmatrix}$$

17 If *A* is an orthogonal matrix, its *QR* factorization has *Q* = \_\_ and *R* = \_\_ . Therefore *RQ* = \_\_ . These are among the rare examples when the *QR* method goes nowhere. 18 The shifted *QR* method factors *A* - *cl* into *QR.* Show that the next matrix A1 = *RQ* + *cl* equals Q-<sup>1</sup>*AQ.* Therefore A1 has the \_\_ eigenvalues as *A* (but A1 is closer to triangular).

19 When  $A = A^T$ , the “Lanczos method” finds  $a$ ’s and  $b$ ’s and orthonormal  $q$ ’s so that  $Aq_j = b_{j-1}q_{j-1} + a_jq_j + b_jq_{j+1}$  (with  $q_0 = \mathbf{0}$ ). Multiply by  $q_j^T$  to find a formula for  $a_j$ . The equation says that  $AQ = QT$  where  $T$  is a tridiagonal matrix.

20 The equation in Problem 19 develops from this loop with  $b_0 = 1$  and  $r_0 = \text{any } q_1$ :

$$q_{j+1} = r_j/b_j; j = j+1; a_j = q_j^T Aq_j; r_j = Aq_j - b_{j-1}q_{j-1} - a_jq_j; b_j = \|r_j\|.$$
Write a code and test it on the `-1, 2, -1` matrix  $A$ .  $Q^T Q$  should be  $I$ .

21 Suppose  $A$  is *tridiagonal and symmetric in the QR method*. From  $A_1 = Q^{-1}AQ$  show that  $A_1$  is symmetric. Write  $A_1 = RAR^{-1}$  to show that  $A_1$  is also tridiagonal. (If the lower part of  $A_1$  is proved tridiagonal then by symmetry the upper part is too.) Symmetric tridiagonal matrices are the best way to start in the QR method.

**Problems 22–25 present two fundamental iterations. Each step involves  $Aq$  or  $Ad$ .**

**The key point for large matrices is that matrix-vector multiplication is much faster than matrix-matrix multiplication.** A crucial construction starts with a vector  $b$ . Repeated multiplication will produce  $Ab$ ,  $A^2b$ , ... but those vectors are far from orthogonal. The “**Arnoldi iteration**” creates an orthonormal basis  $q_1, q_2, \dots$  for the same space by the Gram-Schmidt idea: *orthogonalize each new  $Aq_n$  against the previous  $q_1, \dots, q_{n-1}$* . The “Krylov space” spanned by  $b$ ,  $Ab$ , ...,  $A^{n-1}b$  then has a much better basis  $q_1, \dots, q_n$ .

Here in pseudocode are two of the most important algorithms in numerical linear algebra: Arnoldi gives a good basis and CG gives a good approximation to  $x = A^{-1}b$ .

| <b>Arnoldi Iteration</b>                                                                                                                                                                                 | <b>Conjugate Gradient Iteration for Positive Definite <math>A</math></b>                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $q_1 = b/\ b\ $<br><b>for</b> $n = 1$ <b>to</b> $N - 1$<br>$v = Aq_n$<br><b>for</b> $j = 1$ <b>to</b> $n$<br>$h_{jn} = q_j^T v$<br>$v = v - h_{jn}q_j$<br>$h_{n+1,n} = \ v\ $<br>$q_{n+1} = v/h_{n+1,n}$ | $x_0 = 0, r_0 = b, d_0 = r_0$<br><b>for</b> $n = 1$ <b>to</b> $N$<br>$\alpha_n = (r_{n-1}^T r_{n-1})/(d_{n-1}^T Ad_{n-1})$ step length $x_{n-1}$ to $x_n$<br>$x_n = x_{n-1} + \alpha_n d_{n-1}$ approximate solution<br>$r_n = r_{n-1} - \alpha_n Ad_{n-1}$ new residual $b - Ax_n$<br>$\beta_n = (r_n^T r_n)/(r_{n-1}^T r_{n-1})$ improvement this step<br>$d_n = r_n + \beta_n d_{n-1}$ next search direction<br>% Notice: only 1 matrix-vector multiplication $Aq$ and $Ad$ |

For conjugate gradients, the residuals  $r_n$  are orthogonal and the search directions are  $A$ -orthogonal: all  $d_j^T Ad_k = 0$ . The iteration solves  $Ax = b$  by minimizing the error  $e^T Ae$  over all vectors in the *Krylov space* = span of  $b$ ,  $Ab$ , ...,  $A^{n-1}b$ . It is a fantastic algorithm.

22 For the diagonal matrix  $A = \text{diag}([1 \ 2 \ 3 \ 4])$  and the vector  $b = (1, 1, 1, 1)$ , go through one Arnoldi step to find the orthonormal vectors  $q_1$  and  $q_2$ .

23 Arnoldi's method is finding *Q* so that *AQ* = *QH* (column by column):

$$AQ = \begin{bmatrix} Aq_1 & \cdots & Aq_N \end{bmatrix} = \begin{bmatrix} q_1 & \cdots & q_N \end{bmatrix} \begin{bmatrix} h_{11} & h_{12} & \cdot & h_{1N} \\ h_{21} & h_{22} & \cdot & h_{2N} \\ 0 & h_{32} & \cdot & \cdot \\ 0 & 0 & \cdot & h_{NN} \end{bmatrix} = QH$$

*H* is a "Hessenberg matrix" with one nonzero subdiagonal. Here is the crucial fact when *A* is symmetric: *The Hessenberg matrix H* = Q-<sup>1</sup>*AQ* = *Q<sup>T</sup>AQ is symmetric and therefore* it *is tridiagonal.* Explain that sentence.

24 This tridiagonal *H* (when *A* is symmetric) gives the **Lanc:ws iteration:** 

**Three terms only**      
$$q_{j+1} = (Aq_j - h_{j,j}q_j - h_{j-1,j}q_{j-1})/h_{j+1,j}$$

From *H* = Q-<sup>1</sup>*AQ,* why are the eigenvalues of *H* the same as the eigenvalues of *A?* For large matrices, the "Lanczos method" computes the leading eigenvalues by stopping at a smaller tridiagonal matrix *H k.* The *QR* method in the text is applied to compute the eigenvalues of H *k.* 

25 Apply the conjugate gradient method to solve Ax = b = **ones(lOO, 1),** where A is the -1, **2,** -1 second difference matrix *A=* **toeplitz([2 -** 1 **zeros(l, 98)]).** Graph x*10* and x*20* from CG, along with the exact solution x. (Its 100 components are *Xi <sup>=</sup>(ih* - i 2h 2 )/2 with *h* = 1/101. "plot(i, x(i))" should produce a parabola.) 26 For unsymmetric matrices, the spectral radius p = max I Ai I is not a norm. But still IIA<sup>n</sup> ll grows or decays like p <sup>n</sup>for large n. Compare those numbers for *A=* [1 1; 0 1.1] using the command **norm.** 

A<sup>n</sup> -+ 0 if and only if p < 1. When *A=* s- <sup>1</sup>r, this is the key to convergence.

