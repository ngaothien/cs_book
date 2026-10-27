# Gaussian Elimination of Tridiagonal Matrices


<!-- PAGE 290 -->

## 8.8 Gaussian Elimination of Tridiagonal Matrices

Consider the tridiagonal matrix
$$A = \begin{pmatrix} b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \\ \ddots & \ddots & \ddots \\ a_{n-2} & b_{n-2} & c_{n-2} \\ a_{n-1} & b_{n-1} & c_{n-1} \\ a_{n} & b_{n} \end{pmatrix} .$$
Define the sequence
$$\delta_{0}  = 1,\delta_{1}  = b_{1},\delta_{k}  = b_{k}\delta_{k-1}  -a_{k}c_{k-1}\delta_{k-2} ,2 \le k \le n.$$

> **Proposition 8.7.** If $A$ is the tridiagonal matrix above, then $\delta_{k}  =$ det(A(1 : $k, 1$ : $k))$ for $k = 1, \dots  , n$.

*Proof.* By expanding det(A(1 : $k, 1$ : $k))$ with respect to its last row, the proposition follows by induction on $k$.

> **Theorem 8.8.** If $A$ is the tridiagonal matrix above and $\delta_{k}  \neq  0$ for $k = 1, \dots  , n$, then $A$ has the following LU-factorization:
$$A = \begin{pmatrix} 1 \\ \delta_{0} \\ a_{2} & 1 \\ \delta_{1} \\ \delta_{1} \\ a_{3} & 1 \\ \delta_{2} \\ \ddots & \ddots \\ \delta_{n-3} \\ a_{n-1} & 1 \\ \delta_{n-2} \\ \delta_{n-2} \\ a_{n} & 1 \end{pmatrix} \begin{pmatrix} \delta_{1} \\ c_{1} \\ \delta_{0} \\ \delta_{2} \\ c_{2} \\ \delta_{1} \\ \delta_{3} \\ c_{3} \\ \delta_{2} \\ \ddots & \ddots \\ \delta_{n-1} \\ c_{n-1} \\ \delta_{n-2} \\ \delta_{n} \\ \delta_{n-1} \end{pmatrix} .$$
$$\delta_{n-1}$$

*Proof.* Since $\delta_{k}  =$ det(A(1 : $k, 1$ : $k)) \neq  0$ for $k = 1, \dots  , n$, by Theorem 8.5 (and Proposition 8.2), we know that $A$ has a unique LU-factorization. Therefore, it suffices to check that the proposed factorization works. We easily check that
$$(LU)_{k k+1}=c_{k},1 \le k \le n -1$$
$$(LU)_{k k-1}=a_{k},2 \le k \le n$$
$$(LU)_{k l}=0,|k -l| \ge 2$$
$$(LU)_{1 1}= \frac{\delta_{1}}{\delta_{0}} = b_{1}$$
$$(LU)_{k k}= \frac{a_{k}c_{k-1}\delta_{k-2}  + \delta_{k}}{\delta_{k-1}} = b_{k},2 \le k \le n,$$

<!-- PAGE 291 -->
since $\delta_{k}  = b_{k}\delta_{k-1}$  - $a_{k}c_{k-1}\delta_{k-2}$ . It follows that there is a simple method to solve a linear system Ax $= d$ where $A$ is tridiagonal (and $\delta_{k}  \neq  0$ for $k = 1, \dots  , n)$. For this, it is convenient to “squeeze” the diagonal matrix $\Delta$ defined such that $\Delta_{k k}  = \delta_{k} /\delta_{k-1}$  into the factorization so that $A = (L\Delta )(\Delta^{-1} U)$, and if we let
$$z_{1} = \frac{c_{1}}{b_{1}} ,z_{k} = c_{k} \frac{\delta_{k-1}}{\delta_{k}} ,2 \le k \le n -1,z_{n} = \frac{\delta_{n}}{\delta_{n-1}} = b_{n} -a_{n}z_{n-1},$$
$A = (L\Delta )(\Delta^{-1} U)$ is written as
$$A = \begin{pmatrix} c_{1} \\ z_{1} & c_{2} \\ a_{2} \\ z_{2} & c_{3} \\ a_{3} \\ z_{3} \\ \ddots & \ddots \\ c_{n-1} \\ a_{n-1} \\ z_{n-1} \\ a_{n} & z_{n} \end{pmatrix} \begin{pmatrix} 1 & z_{1} \\ 1 & z_{2} \\ 1 & z_{3} \\ \ddots & \ddots \\ 1 & z_{n-2} \\ 1 & z_{n-1} \\ 1 \end{pmatrix} .$$
As a consequence, the system Ax $= d$ can be solved by constructing three sequences: First, the sequence
$$z_{1} = \frac{c_{1}}{b_{1}} ,z_{k} = \frac{c_{k}}{b_{k} -a_{k}z_{k-1}} ,k = 2, \dots  , n -1,z_{n} = b_{n} -a_{n}z_{n-1},$$
corresponding to the recurrence $\delta_{k}  = b_{k}\delta_{k-1}$  - $a_{k}c_{k-1}\delta_{k-2}$  and obtained by dividing both sides of this equation by $\delta_{k-1}$ , next
$$w_{1} = \frac{d_{1}}{b_{1}} ,w_{k} = \frac{d_{k}a_{k}w_{k-1}}{b_{k} -a_{k}z_{k-1}} -,k = 2, \dots  , n,$$
corresponding to solving the system $L\Delta w = d$, and finally
$$x_{n} = w_{n},x_{k} = w_{k} -z_{k}x_{k+1},k = n -1, n -2, \dots  , 1,$$
corresponding to solving the system $\Delta^{-1}$ Ux $= w$.
Remark: It can be verified that this requires 3(n - $1)$ additions, 3(n - $1)$ multiplications, and 2n divisions, a total of 8n-6 operations, which is much less that the $O(2n^{3}/3)$ required by Gaussian elimination in general. We now consider the special case of symmetric positive definite matrices $(SPD$ matrices).
