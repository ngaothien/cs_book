# Dealing with Roundoff Errors; Pivoting Strategies


<!-- PAGE 288 -->
Since $E_{k}^{k} = E_{k}$, we obtain
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}(E_{k}^{k})^{-1}= (I + P_{k}\Lambda_{k-1} )E_{k}^{-1} .$$
However, by definition
$$I + \Lambda_{k}  = (I + P_{k}\Lambda_{k-1} )E_{k}^{-1} ,$$
which proves that
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}(E_{k}^{k})^{-1},(\dagger )$$
and finishes the induction step for the proof of this formula. If we apply Equation (*) again with $k + 1$ in place of $k$, we have
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k}^{k})^{-1}= I +\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
and together with $(\dagger$ ), we obtain,
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
also finishing the induction step for the proof of this formula. For $k =$ n-1 in $(\dagger$ ), we obtain the desired equation: $L =$ I $+ \Lambda_{n-1}$ .

## 8.7 Dealing with RoundoffErrors; Pivoting Strategies

Let us now briefly comment on the choice of a pivot. Although theoretically, any pivot can be chosen, the possibility of roundofferrors implies that it is not a good idea to pick very small pivots. The following example illustrates this point. Consider the linear system
$$10^{-4}x+y=1$$
$$x+y=2.$$
Since $10^{-4}$ is nonzero, it can be taken as pivot, and we get
$$10^{-4}x+y=1$$
$$(1 -10^{4})y=2 -10^{4}.$$
Thus, the exact solution is
$$-$$
$$x = \frac{10^{4}}{10^{4}-1} ,y = \frac{10^{4}2}{10^{4}-1} .$$
However, if roundofftakes place on the fourth digit, then $10^{4} -1 = 9999$ and $10^{4} -2 = 9998$ will be rounded offboth to $9990$, and then the solution is $x = 0$ and $y = 1$, very far from the exact solution where $x \approx 1$ and $y \approx 1$. The problem is that we picked a very small pivot. If instead we permute the equations, the pivot is $1$, and after elimination we get the system
$$x+y=2$$
$$(1 -10^{-4})y=1 -2 \times  10^{-4}.$$

<!-- PAGE 289 -->
This time, $1$ - $10^{-4} =$ 0.9999 and $1$ - $2 \times  10^{-4} =$ 0.9998 are rounded offto 0.999 and the solution is $x = 1, y = 1$, much closer to the exact solution. To remedy this problem, one may use the strategy of partial pivoting. This consists of choosing during Step $k (1 \le k \le n$ - $1)$ one of the entries $a_{i k}^{(k)}$ such that
$$|a_{i k}^{(k)} | = \max |a_{p k}^{(k)}|.$$
$$k\le p\le n$$
By maximizing the value of the pivot, we avoid dividing by undesirably small pivots.
Remark: $A$ matrix, $A$, is called strictly column diagonally dominant iff
$$|a_{j j}| > \sum_{=1, i\neq j}^{n}  |a_{i j}|,for j = 1, \dots  , n$$
$$i$$
(resp. strictly row diagonally dominant iff
$$|a_{i i}| > \sum_{=1, j\neq}^{n}  |a_{i j}|,for i = 1, \dots  , n.)$$
$$ji$$
For example, the matrix
$$\begin{pmatrix} 7 & 1 \\ 1\overline{2} & 4 & 1 & 0 \\ \ddots & \ddots & \ddots \\ 0 & 1 & 4 & 1 \\ 1 & 7 \end{pmatrix}$$
$$\overline{2}$$
of the curve interpolation problem discussed in Section 8.1 is strictly column (and row) diagonally dominant. It has been known for a long time (before $1900$, say by Hadamard) that if a matrix $A$ is strictly column diagonally dominant (resp. strictly row diagonally dominant), then it is invertible. It can also be shown that if $A$ is strictly column diagonally dominant, then Gaussian elimination with partial pivoting does not actually require pivoting (see Problem 8.12). Another strategy, called complete pivoting, consists in choosing some entry $a_{i j}^{(k)}$ , where $k \le i, j \le n$, such that
$$|a_{i j}^{(k)} | = \max |a_{p q}^{(k)} |.$$
$$k\le p,q\le n$$
However, in this method, if the chosen pivot is not in column $k$, it is also necessary to permute columns. This is achieved by multiplying on the right by a permutation matrix. However, complete pivoting tends to be too expensive in practice, and partial pivoting is the method of choice. A special case where the LU-factorization is particularly efficient is the case of tridiagonal matrices, which we now consider.
