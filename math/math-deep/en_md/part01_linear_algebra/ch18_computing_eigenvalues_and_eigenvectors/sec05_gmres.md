# GMRES


<!-- PAGE 684 -->
However, if $A$ is a symmetric (or Hermitian) matrix, then $H_{n}$ is a symmetric (resp. Hermitian) tridiagonal matrix and more precise results can be shown; see Demmel $[48]$ (Chapter $7$, especially Section 7.2). We will consider the symmetric (and Hermitan) case in the next section, but first we show how Arnoldi iteration can be used to find approximations for the solution of a linear system Ax $= b$ where $A$ is invertible but of very large dimension $m$.

## 18.5 GMRES

Suppose $A$ is an invertible $m\times m$ matrix and let $b$ be a nonzero vector $in\mathbb{C}^{m}$. Let $x_{0} = A^{-1}b$, the unique solution of Ax $= b$. It is not hard to show that $x_{0} \in K_{n}(A, b)$ for some $n \le m$. In fact, there is a unique monic polynomial p(z) of minimal degree $s \le m$ such that p(A)b $= 0$, so $x_{0} \in K_{s}(A, b)$. Thus it makes sense to search for a solution of Ax $= b$ in Krylov spaces of dimension $m \le s$. The idea is to find an approximation $x_{n} \in K_{n}(A, b)$ of $x_{0}$ such that $r_{n} = b$ - $Ax_{n}$ is minimized, that is, $\|r_{n}\|_{2} = \|b$ - $Ax_{n}\|_{2}$ is minimized over $x_{n} \in K_{n}(A, b)$. This minimization problem can be stated as
$$minimize\|r_{n}\|_{2} = \|Ax_{n} -b\|_{2} ,x_{n} \in K_{n}(A, b).$$
This is a least-squares problem, and we know how to solve it (see Section 23.1). The quantity $r_{n}$ is known as the residual and the method which consists in minimizing $\|r_{n}\|_{2}$ is known as GMRES, for generalized minimal residuals. Now since $(u_{1}, \dots  , u_{n})$ is a basis of $\mathcal{K}_{n}(A, b)$ (since $n \le s$, no breakdown occurs, except for $n = s)$, we may write $x_{n} = U_{n}y$, so our minimization problem is
$$minimize\|AU_{n}y -b\|_{2} ,y \in \mathbb{C}^{n}.$$
Since by $(*_{1})$ of Section 18.4, we have $AU_{n} = U_{n+1}H_{n}$, minimizing $\|AU_{n}y$ - $b\|_{2}$ is equiv-
$$e$$
$$\mathbb{C}^{m}$$
alent to minimizing $\|U_{n+1}H_{n}y$ - $b\|_{2}$ over . Since $U_{n+1}H_{n}y$ and $b$ belong to the column
$$ee$$
space of $U_{n+1}$, minimizing $\|U_{n+1}H_{n}y$ - $b\|_{2}$ is equivalent to minimizing $\|H_{n}y$ - $U_{n+1}^{*} b\|_{2}$.
$$ee$$
However, by construction,
$$U_{n+1}^{*} b = \|b\|_{2}e_{1} \in \mathbb{C}^{n+1},$$
so our minimization problem can be stated as
$$minimize\|H_{n}y -\|b\|_{2}e_{1}\|_{2},y \in \mathbb{C}^{n}.$$
$$e$$
The approximate solution of Ax $= b$ is then
$$x_{n} = U_{n}y.$$
Starting with $u_{1} = b/ \|b\|_{2}$ and with $n = 1$, the GMRES method runs $n \le s$ Arnoldi iterations to find $U_{n}$ and $H_{n}$, and then runs a method to solve the least squares problem
$$e$$
$$minimize\|H_{n}y -\|b\|_{2}e_{1}\|_{2},y \in \mathbb{C}^{n}.$$
$$e$$
