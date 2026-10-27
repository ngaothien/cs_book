# Problems


<!-- PAGE 411 -->

## 10.7 Problems

Problem 10.1. Consider the matrix
$$A = \begin{pmatrix} 1 & 2 & -2 \\ 1 & 1 & 1 \\ 2 & 2 & 1 \end{pmatrix} .$$
Prove that $\rho (J) = 0$ and $\rho (\mathcal{L}_{1}) = 2$, so
$$\rho (J) < 1 < \rho (\mathcal{L}_{1}),$$
where $J$ is Jacobi’s matrix and $\mathcal{L}_{1}$ is the matrix of Gauss–Seidel.
Problem 10.2. Consider the matrix
$$A = \begin{pmatrix} 2 & -1 & 1 \\ 2 & 2 & 2 \\ 1 & 1 & 2 \end{pmatrix} .$$
$$--$$
$$\sqrt$$
Prove that $\rho (J) = \overline{5}/2$ and $\rho (\mathcal{L}_{1}) = 1/2$, so
$$\rho (\mathcal{L}_{1}) < \rho (J),$$
where where $J$ is Jacobi’s matrix and $\mathcal{L}_{1}$ is the matrix of Gauss–Seidel.
Problem 10.3. Consider the following linear system:
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 19 \\ 19 \\ -3 \\ 12 \end{pmatrix} .$$
$$--$$
$(1)$ Solve the above system by Gaussian elimination.
$(2)$ Compute the sequences of vectors $u_{k} = (u_{1}^{k}, u_{2}^{k}, u_{3}^{k}, u_{4}^{k})$ for $k = 1, \dots  , 10$, using the methods of Jacobi, Gauss–Seidel, and relaxation for the following values of $\omega$ : $\omega  =$ 1.1, 1.2, $\dots$  , 1.9. In all cases, the initial vector is $u_{0} = (0, 0, 0, 0)$.
Problem 10.4. Recall that a complex or real $n \times  n$ matrix $A$ is strictly row diagonally
$$dominant if |a_{ii}| > \sum_{j}  n=1,j\neq i |a_{ij}| for i = 1, \dots  , n.$$
$(1)$ Prove that if $A$ is strictly row diagonally dominant, then Jacobi’s method converges.
$(2)$ Prove that if $A$ is strictly row diagonally dominant, then Gauss–Seidel’s method converges.

<!-- PAGE 412 -->
Problem 10.5. Prove that the converse of Proposition 10.5 holds. That is, if $A$ is an invertible Hermitian matrix with the splitting $A = M$ - $N$ where $M$ is invertible, if the Hermitian matrix $M^{*} + N$ is positive definite and if $\rho (M^{-1} N) < 1$, then $A$ is positive definite.
Problem 10.6. Consider the following tridiagonal $n \times  n$ matrix:
$$A = \frac{1}{(n + 1)^{2}} \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ \ddots & \ddots & \ddots \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} .$$
$(1)$ Prove that the eigenvalues of the Jacobi matrix $J$ are given by
$$\lambda_{k}  = \cos \begin{pmatrix} k\pi \\ n + 1 \end{pmatrix} ,k = 1, \dots  , n.$$
Hint. First show that the Jacobi matrix is
$$J = \frac{1}{2} \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ \ddots & \ddots & \ddots \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} .$$
Then the eigenvalues and the eigenvectors of $J$ are solutions of the system of equations
$$y_{0} = 0$$
$$y_{k+1} + y_{k-1} = 2\lambda y_{k},k = 1, \dots  , n$$
$$y_{n+1} = 0,$$
where the variables $y_{0}$ and $y_{n+1}$ are introduced so that the same equation applies for $k = 1, \dots  , n$. It is well known that the general solution to the above recurrence is given by
$$y_{k} = \alpha z_{1}^{k} + \beta z_{2}^{k},k = 0, \dots  , n + 1,$$
(with $\alpha , \beta  \neq  0)$ where $z_{1}$ and $z_{2}$ are the zeros of the equation
$$z^{2}-2\lambda z + 1 = 0.$$
It follows that $z_{2} = z_{1}^{-1}$ and $z_{1} + z_{2} = 2\lambda$ . The boundary condition $y_{0} = 0$ yields $\alpha  + \beta  = 0$, so $y_{k} = \alpha (z_{1}^{k}$ - $z_{1}^{-k}$ ), and the boundary condition $y_{n+1} = 0$ yields
$$z_{1}^{2(n+1)}= 1.$$

<!-- PAGE 413 -->
Deduce that we may assume that the $n$ possible values $(z_{1})_{k}$ for $z_{1}$ are given by
$$(z_{1})_{k} =\overline{e}_{n+1}^{k\pi i},k = 1, \dots  , n,$$
and find
$$2\lambda_{k}  = (z_{1})_{k} + (z_{1})_{k}^{-1} .$$
Show that an eigenvector $(y_{1}^{(k)} , \dots  , y_{n}^{(k)}$ ) associated with the eigenvalue $\lambda_{k}$  is given by
$$y_{j}^{(k)}= \sin \begin{pmatrix} kj\pi \\ n + 1 \end{pmatrix} ,j = 1, \dots  , n.$$
$(2)$ Find the spectral radius $\rho (J), \rho (\mathcal{L}_{1})$, and $\rho (\mathcal{L}_{\omega0})$, as functions of $h = 1/(n + 1)$.

<!-- PAGE 414 -->
