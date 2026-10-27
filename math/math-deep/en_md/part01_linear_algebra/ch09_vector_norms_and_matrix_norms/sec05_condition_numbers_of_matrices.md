# Condition Numbers of Matrices


<!-- PAGE 364 -->
Note that equality is generally not possible; consider the matrix
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} ,$$
for which $\rho (A) = 0 < \|A\|$, since $A \neq  0$.

## 9.5 Condition Numbers of Matrices

Unfortunately, there exist linear systems Ax $= b$ whose solutions are not stable under small perturbations of either $b$ or $A$. For example, consider the system
$$\begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 32 \\ 23 \\ 33 \\ 31 \end{pmatrix} .$$
The reader should check that it has the solution $x = (1, 1, 1, 1)$. If we perturb slightly the right-hand side as $b + \Delta b$, where
$$\Delta b = \begin{pmatrix} 0.1 \\ -0.1 \\ 0.1 \\ 0.1 \end{pmatrix} ,$$
$$-$$
we obtain the new system
$$\begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} \begin{pmatrix} x_{1} + \Delta x_{1} \\ x_{2} + \Delta x_{2} \\ x_{3} + \Delta x_{3} \\ x_{4} + \Delta x_{4} \end{pmatrix} = \begin{pmatrix} 32.1 \\ 22.9 \\ 33.1 \\ 30.9 \end{pmatrix} .$$
The new solution turns out to be $x + \Delta x =$ (9.2, -12.6, 4.5, -1.1), where
$$\Delta x = (9.2, -12.6, 4.5, -1.1) -(1, 1, 1, 1) = (8.2, -13.6, 3.5, -2.1).$$
Then a relative error of the data in terms of the one-norm,
$$\|\|_{1}$$
$$\frac{\Delta b}{\|b\|_{1}} = \frac{0.4}{119} = \frac{4}{1190} \approx \frac{1}{300} ,$$
produces a relative error in the input
$$\|\|_{1}$$
$$\frac{\Delta x}{\|x\|_{1}} = \frac{27.4}{4} \approx 7.$$
So a relative error of the order $1/300$ in the data produces a relative error of the order $7/1$ in the solution, which represents an amplification of the relative error of the order $2100$.

<!-- PAGE 365 -->
Now let us perturb the matrix slightly, obtaining the new system
$$\begin{pmatrix} 10 & 7 & 8.1 & 7.2 \\ 7.08 & 5.04 & 6 & 5 \\ 8 & 5.98 & 9.98 & 9 \\ 6.99 & 4.99 & 9 & 9.98 \end{pmatrix} \begin{pmatrix} x_{1} + \Delta x_{1} \\ x_{2} + \Delta x_{2} \\ x_{3} + \Delta x_{3} \\ x_{4} + \Delta x_{4} \end{pmatrix} = \begin{pmatrix} 32 \\ 23 \\ 33 \\ 31 \end{pmatrix} .$$
This time the solution is $x + \Delta x =$ (-81, $137$, -34, $22)$. Again a small change in the data alters the result rather drastically. Yet the original system is symmetric, has determinant $1$, and has integer entries. The problem is that the matrix of the system is badly conditioned, a concept that we will now explain. Given an invertible matrix $A$, first assume that we perturb $b$ to $b+\Delta b$, and let us analyze the change between the two exact solutions $x$ and $x + \Delta x$ of the two systems
$$Ax = b$$
$$A(x + \Delta x) = b + \Delta b.$$
We also assume that we have some norm $\|\|$ and we use the subordinate matrix norm on matrices. From
$$Ax = b$$
$$Ax + A\Delta x = b + \Delta b,$$
we get
$$\Delta x = A^{-1}\Delta b,$$
and we conclude that
$$\|\Delta x\|\le

$A^{-1}$

$\|\Delta b\|$$$
$$\|b\|\le \|A\|\|x\|.$$
Consequently, the relative error in the result $\|\Delta x\|/ \|x\|$ is bounded in terms of the relative error $\|\Delta b\|/ \|b\|$ in the data as follows:
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le \begin{pmatrix} \|A\| & A^{-1} \end{pmatrix} \frac{\Delta b}{\|b\|} .$$
Now let us assume that $A$ is perturbed to $A+\Delta A$, and let us analyze the change between the exact solutions of the two systems
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b.$$
The second equation yields Ax $+ A\Delta x + \Delta$ A(x $+ \Delta x) = b$, and by subtracting the first equation we get
$$\Delta x = -A^{-1}\Delta A(x + \Delta x).$$

<!-- PAGE 366 -->
It follows that
$$\|\Delta x\|\le

$A^{-1}$

$\|\Delta A\|\|x + \Delta x\|,$$$ which can be rewritten as
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x + \Delta x\|} \le \begin{pmatrix} \|A\| & A^{-1} \end{pmatrix} \frac{\Delta A}{\|A\|} .$$
Observe that the above reasoning is valid even if the matrix $A + \Delta A$ is singular, as long as $x + \Delta x$ is a solution of the second system. Furthermore, if $\|\Delta A\|$ is small enough, it is not unreasonable to expect that the ratio $\|\Delta x\|/ \|x + \Delta x\|$ is close to $\|\Delta x\|/ \|x\|$. This will be made more precise later. In summary, for each of the two perturbations, we see that the relative error in the result is bounded by the relative error in the data, multiplied the number $\|A\|\|A^{-1}\|$. In fact, this factor turns out to be optimal and this suggests the following definition:

> **Definition 9.11.** For any subordinate matrix norm $\|\|$, for any invertible matrix $A$, the number
$$cond(A) = \|A\|

$A^{-1}$$$ is called the condition number of $A$ relative to $\|\|$. The condition number cond(A) measures the sensitivity of the linear system Ax $= b$ to variations in the data $b$ and $A$; a feature referred to as the condition of the system. Thus, when we says that a linear system is ill-conditioned, we mean that the condition number of its matrix is large. We can sharpen the preceding analysis as follows:

> **Proposition 9.14.** Let $A$ be an invertible matrix and let $x$ and $x + \Delta x$ be the solutions of the linear systems
$$Ax = b$$
$$A(x + \Delta x) = b + \Delta b.$$
If $b \neq  0$, then the inequality
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta b}{\|b\|}$$
holds and is the best possible. This means that for a given matrix $A$, there exist some vectors $b \neq  0$ and $\Delta b \neq  0$ for which equality holds.

*Proof.* We already proved the inequality. Now, because $\|\|$ is a subordinate matrix norm, there exist some vectors $x \neq  0$ and $\Delta b \neq  0$ for which
$$A^{-1}\Delta b

$=$

$A^{-1}$

$\|\Delta b\|and\|Ax\|= \|A\|\|x\|.$$$

<!-- PAGE 367 -->

> **Proposition 9.15.** Let $A$ be an invertible matrix and let $x$ and $x + \Delta x$ be the solutions of the two systems
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b.$$
If $b \neq  0$, then the inequality
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x + \Delta x\|} \le cond(A) \frac{\Delta A}{\|A\|}$$
holds and is the best possible. This means that given a matrix $A$, there exist a vector $b \neq  0$ and a matrix $\Delta A \neq  0$ for which equality holds. Furthermore, if $\|\Delta A\|$ is small enough (for instance, if $\|\Delta A\| < 1/ \|A^{-1}\|)$, we have
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} (1 + O(\|\Delta A\|));$$
in fact, we have
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} \begin{pmatrix} 1 \\ 1 -\|A^{-1}\|\|\Delta A\| \end{pmatrix} .$$

*Proof.* The first inequality has already been proven. To show that equality can be achieved, let $w$ be any vector such that $w \neq  0$ and
$$A^{-1}w

$=$

$A^{-1}$

$\|w\|,$$$ and let $\beta  \neq  0$ be any real number. Now the vectors
$$\Delta x = -\beta A^{-1}w$$
$$x + \Delta x = w$$
$$b = (A + \beta I)w$$
and the matrix
$$\Delta A = \beta I$$
sastisfy the equations
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b$$
$$\|\Delta x\|= |\beta |

$A^{-1}w$

$= \|\Delta A\|$

$A^{-1}$

$\|x + \Delta x\|.$$$ Finally we can pick $\beta$  so that $-\beta$  is not equal to any of the eigenvalues of $A$, so that $A + \Delta A = A + \beta$ I is invertible and $b$ is is nonzero.

<!-- PAGE 368 -->
If $\|\Delta A\| < 1/ \|A^{-1}\|$, then
$$A^{-1}\Delta A

$\le$

$A^{-1}$

$\|\Delta A\|<$ 1,$$ so by Proposition 9.12, the matrix $I + A^{-1}\Delta A$ is invertible and
$$(I + A^{-1}\Delta A)^{-1}

$\le \frac{1}{1 -\|A^{-1}\Delta A\|} \le \frac{1}{1 -\|A^{-1}\|\|\Delta A\|}$ .$$ Recall that we proved earlier that
$$\Delta x = -A^{-1}\Delta A(x + \Delta x),$$
and by adding $x$ to both sides and moving the right-hand side to the left-hand side yields
$$(I + A^{-1}\Delta A)(x + \Delta x) = x,$$
and thus
$$x + \Delta x = (I + A^{-1}\Delta A)^{-1}x,$$
which yields
$$\Delta x = ((I + A^{-1}\Delta A)^{-1}-I)x = (I + A^{-1}\Delta A)^{-1}(I -(I + A^{-1}\Delta A))x$$
$$= -(I + A^{-1}\Delta A)^{-1}A^{-1}(\Delta A)x.$$
From this and
$$(I + A^{-1}\Delta A)^{-1}

$\le \frac{1}{1 -\|A^{-1}\|\|\Delta A\|}$ ,$$ we get
$$\|\|\|\|$$
$$\|\Delta x\|\le \frac{A^{-1}\Delta A}{1 -\|A^{-1}\|\|\Delta A\|} \|x\|,$$
which can be written as
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} \begin{pmatrix} 1 \\ 1 -\|A^{-1}\|\|\Delta A\| \end{pmatrix} ,$$
which is the kind of inequality that we were seeking.
Remark: If $A$ and $b$ are perturbed simultaneously, so that we get the “perturbed” system
$$(A + \Delta A)(x + \Delta x) = b + \Delta b,$$
it can be shown that if $\|\Delta A\| < 1/ \|A^{-1}\|$ (and $b \neq  0)$, then
$$\|\|$$
$$\frac{\Delta x}{\|x\|} \le \frac{cond(A)}{1 -\|A^{-1}\|\|\Delta A\|} \begin{pmatrix} \|\Delta A\| & \|\Delta b\| \\ + \\ \|A\| & \|b\| \end{pmatrix} ;$$

<!-- PAGE 369 -->
see Demmel $[48]$, Section 2.2 and Horn and Johnson $[98]$, Section 5.8. We now list some properties of condition numbers and figure out what cond(A) is in the case of the spectral norm (the matrix norm induced by $\|\|_{2})$. First, we need to introduce a very important factorization of matrices, the singular value decomposition, for short, SVD. It can be shown (see Section 22.2) that given any $n \times  n$ matrix $A \in M_{n}(\mathbb{C})$, there exist two unitary matrices $U$ and $V$ , and a real diagonal matrix $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$ ), with $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}  \ge 0$, such that
$$A = V \Sigma U^{*} .$$

> **Definition 9.12.** Given a complex $n \times  n$ matrix $A$, a triple $(U, V, \Sigma$ ) such that $A = V \Sigma U^{*}$ , where $U$ and $V$ are $n \times  n$ unitary matrices and $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$ ) is a diagonal matrix of real numbers $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}  \ge 0$, is called a singular decomposition (for short SVD) of $A$. If $A$ is a real matrix, then $U$ and $V$ are orthogonal matrices The nonnegative numbers $\sigma_{1} , \dots  , \sigma_{n}$  are called the singular values of $A$. The factorization $A = V \Sigma U^{*}$ implies that
$$A^{*}A = U\Sigma^{2} U^{*} andAA^{*}= V \Sigma^{2} V^{*} ,$$
which shows that $\sigma_{1}^{2} , \dots  , \sigma_{n}^{2}$  are the eigenvalues of both $A^{*}A$ and $AA^{*}$, that the columns of $U$ are corresponding eigenvectors for $A^{*}A$, and that the columns of $V$ are corresponding eigenvectors for $AA^{*}$. Since $\sigma_{1}^{2}$  is the largest eigenvalue of $A^{*}A$ (and $AA^{*})$, note that $p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\rho}\overline{(}\overline{AA}^{*}\overline{) =} \sigma_{1}$ .

> **Corollary 9.16.** The spectral norm $\|A\|_{2}$ of a matrix $A$ is equal to the largest singular value of $A$. Equivalently, the spectral norm $\|A\|_{2}$ of a matrix $A$ is equal to the $\ell^{\infty}$ -norm of its vector of singular values,
$$\|A\|_{2} = \max \sigma_{i}  = \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{\infty}.$$
$$1\le i\le n$$
Since the Frobenius norm of a matrix $A$ is defined by $\|A\|_{F} = p\overline{tr(}\overline{A}^{*}\overline{A}\overline{)}$ and since
$$\mathrm{tr}(A^{*}A) = \sigma_{1}^{2}  + \cdots  + \sigma_{n}^{2}$$
where $\sigma_{1}^{2} , \dots  , \sigma_{n}^{2}$  are the eigenvalues of $A^{*}A$, we see that
$$\|A\|_{F} = (\sigma_{1}^{2}  + \cdots  + \sigma_{n}^{2} )^{1/2}= \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{2} .$$

> **Corollary 9.17.** The Frobenius norm of a matrix is given by the $\ell^{2}$ -norm of its vector of singular values; $\|A\|_{F} = \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{2}$.

<!-- PAGE 370 -->
In the case of a normal matrix, if $\lambda_{1} , \dots  , \lambda_{n}$  are the (complex) eigenvalues of $A$, we showed in the proof of Proposition 9.11 that the eigenvalues of $A^{*}A = AA^{*}$ are $(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, so the singular values of $A$ are
$$\sigma_{i}  = |\lambda_{i} |,1 \le i \le n.$$

> **Proposition 9.18.** For every invertible matrix $A \in M_{n}(\mathbb{C})$, the following properties hold: $(1)$
$$cond(A) \ge 1,$$
$$cond(A) = cond(A^{-1})$$
$$cond(\alpha A) = cond(A)for all \alpha  \in \mathbb{C} -{0}.$$
$(2)$ If $cond_{2}(A)$ denotes the condition number of $A$ with respect to the spectral norm, then
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{n}} ,$$
where $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$  are the singular values of $A$.
$(3)$ If the matrix $A$ is normal, then
$$||$$
$$cond_{2}(A) = \frac{\lambda_{1}}{|\lambda_{n} |} ,$$
where $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $A$ sorted so that $|\lambda_{1}$ | $\ge \cdots  \ge |\lambda_{n}$ |.
$(4)$ If $A$ is a unitary or an orthogonal matrix, then
$$cond_{2}(A) = 1.$$
$(5)$ The condition number $cond_{2}(A)$ is invariant under unitary transformations, which means that
$$cond_{2}(A) = cond_{2}(UA) = cond_{2}(AV ),$$
for all unitary matrices $U$ and $V$ .

*Proof.* The properties in $(1)$ are immediate consequences of the properties of subordinate matrix norms. In particular, $AA^{-1} =$ I implies
$$1 = \|I\|\le \|A\|

$A^{-1}$

$=$ cond(A).$$
$(2)$ We showed earlier that $\|A\|_{2}^{2} = \rho (A^{*}A)$, which is the square of the modulus of the largest eigenvalue of $A^{*}A$. Since we just saw that the eigenvalues of $A^{*}A$ are $\sigma_{1}^{2}  \ge \cdots  \ge \sigma_{n}^{2}$ , where $\sigma_{1} , \dots  , \sigma_{n}$  are the singular values of $A$, we have
$$\|A\|_{2} = \sigma_{1} .$$

<!-- PAGE 371 -->
Now if $A$ is invertible, then $\sigma_{1}  \ge \cdots  \ge \sigma_{n}  > 0$, and it is easy to show that the eigenvalues of $(A^{*}A)^{-1}$ are $\sigma_{n}^{-2} \ge \cdots  \ge \sigma_{1}^{-2}$  , which shows that
$$A_{2}^{-1}

$= \sigma_{n}^{-1}$  ,$$ and thus
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{n}} .$$
$(3)$ This follows from the fact that for a normal matrix $A$, the singular values are given by $\sigma_{i}  = |\lambda_{i}$ |, $1 \le i \le n$.
$$\frac{(4)If}{\rho (A^{*}A} A is a unitary matrix, then A^{*}A = \frac{AA^{*}=I}{\rho (AA^{*}} , so \rho (A^{*}A) = 1, and \|A\|_{2} =$$
$p$ ) $= 1$. We also have $\|A^{-1}\|_{2} = \|A^{*}\|_{2} = p$ ) $= 1$, and thus cond(A) $= 1$.
$(5)$ This follows immediately from the unitary invariance of the spectral norm. Proposition 9.18 $(4)$ shows that unitary and orthogonal transformations are very wellconditioned, and Part $(5)$ shows that unitary transformations preserve the condition number. In order to compute $cond_{2}(A)$, we need to compute the top and bottom singular values of $A$, which may be hard. The inequality
$$\sqrt$$
$$\|A\|_{2} \le \|A\|_{F} \le \overline{n} \|A\|_{2} ,$$
may be useful in getting an approximation of $cond_{2}(A) = \|A\|_{2} \|A^{-1}\|_{2}$, if $A^{-1}$ can be determined.
Remark: There is an interesting geometric characterization of $cond_{2}(A)$. If $\theta (A)$ denotes the least angle between the vectors Au and Av as $u$ and $v$ range over all pairs of orthonormal vectors, then it can be shown that
$$cond_{2}(A) = cot(\theta (A)/2)).$$
Thus if $A$ is nearly singular, then there will be some orthonormal pair $u, v$ such that Au and Av are nearly parallel; the angle $\theta (A)$ will the be small and $cot(\theta (A)/2))$ will be large. For more details, see Horn and Johnson $[98]$ (Section 5.8 and Section 7.4). It should be noted that in general (if $A$ is not a normal matrix) a matrix could have a very large condition number even if all its eigenvalues are identical! For example, if we consider the $n \times  n$ matrix
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix} ,$$

<!-- PAGE 372 -->
it turns out that $cond_{2}(A) \ge 2^{n-1}$. A classical example of matrix with a very large condition number is the Hilbert matrix $H^{(n)}$, the $n \times  n$ matrix with
$$H_{ij}^{(n)}= \begin{pmatrix} 1 \\ i + j -1 \end{pmatrix} .$$
For example, when $n = 5$,
$$H^{(5)} = \begin{pmatrix} 1_{2}^{1} & 1 & 1 & 1 \\ \overline{3} & \overline{4} & \overline{5} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{2} & \overline{3} & \overline{4} & \overline{5} & \overline{6} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{3} & \overline{4} & \overline{5} & \overline{6} & \overline{7} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{4} & \overline{5} & \overline{6} & \overline{7} & \overline{8} \\ 1 & 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$\overline{5}\overline{6}\overline{7}\overline{8}\overline{9}$$
It can be shown that
$$cond_{2}(H^{(5)}) \approx 4.77 \times  10^{5}.$$
Hilbert introduced these matrices in $1894$ while studying a problem in approximation theory. The Hilbert matrix $H^{(n)}$ is symmetric positive definite. A closed-form formula can be given for its determinant (it is a special form of the so-called Cauchy determinant); see
Problem 9.15. The inverse of $H^{(n)}$ can also be computed explicitly; see Problem 9.15. It can be shown that
$$\sqrt\sqrt$$
$$cond_{2}(H^{(n)}) = O((1 +\overline{2)}^{4n}/\overline{n}).$$
Going back to our matrix
$$A = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} ,$$
which is a symmetric positive definite matrix, it can be shown that its eigenvalues, which in this case are also its singular values because $A$ is SPD, are
$$\lambda_{1}  \approx 30.2887 > \lambda_{2}  \approx 3.858 > \lambda_{3}  \approx 0.8431 > \lambda_{4}  \approx 0.01015,$$
so that
$$cond_{2}(A) = \frac{\lambda_{1}}{\lambda_{4}} \approx 2984.$$
The reader should check that for the perturbation of the right-hand side $b$ used earlier, the relative errors $\|\Delta x\|/\|x\|$ and $\|\Delta x\|/\|x\|$ satisfy the inequality
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta b}{\|b\|}$$
and comes close to equality.
