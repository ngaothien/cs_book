# The Hermitian Case; Lanczos Iteration


<!-- PAGE 685 -->
When $\|r_{n}\|_{2} = \|H_{n}y -\|b\|_{2}e_{1}\|_{2}$ is considered small enough, we stop and the approximate
$$e$$
solution of Ax $= b$ is then
$$x_{n} = U_{n}y.$$
There are ways of improving efficiency of the “naive” version of GMRES that we just presented; see Trefethen and Bau $[182]$ (Lecture $35)$. We now consider the case where $A$ is a Hermitian (or symmetric) matrix.

## 18.6 The Hermitian Case; Lanczos Iteration

If $A$ is an $m\times m$ symmetric or Hermitian matrix, then Arnoldi’s method is simpler and much more efficient. Indeed, in this case, it is easy to see that the upper Hessenberg matrices $H_{n}$ are also symmetric (Hermitian respectively), and thus tridiagonal. Also, the eigenvalues of $A$ and $H_{n}$ are real. It is convenient to write
$$H_{n} = \begin{pmatrix} \alpha_{1} & \beta_{1} \\ \beta_{1} & \alpha_{2} & \beta_{2} \\ \beta_{2} & \alpha_{3} & \ddots \\ \ddots & \ddots & \beta_{n-1} \\ \beta_{n-1} & \alpha_{n} \end{pmatrix} .$$
The recurrence $(*_{2})$ of Section 18.4 becomes the three-term recurrence
$$Au_{n} = \beta_{n-1} u_{n-1} + \alpha_{n} u_{n} + \beta_{n} u_{n+1}.(*_{6})$$
We also have $\alpha_{n}  = u_{n}^{*}Au_{n}$, so Arnoldi’s algorithm becomes the following algorithm known as Lanczos’ algorithm (or Lanczos iteration). The inner loop on $j$ from $1$ to $n$ has been eliminated and replaced by a single assignment. Given an arbitrary nonzero vector $b \in \mathbb{C}^{m}$, let $u_{1} = b/ \|b\|$; for $n = 1, 2, 3, \dots$  do $z := Au_{n}; \alpha_{n}  := u_{n}^{*}z; z := z$ - $\beta_{n-1} u_{n-1}$ - $\alpha_{n} u_{n} \beta_{n}  := \|z\|$; if $\beta_{n}  = 0$ quit $u_{n+1} = z/\beta_{n}$ When $\beta_{n}  = 0$, we say that we have a breakdown of the Lanczos iteration. Versions of Proposition 18.5 and Theorem 18.6 apply to Lanczos iteration. Besides being much more efficient than Arnoldi iteration, Lanczos iteration has the advantage that the Rayleigh–Ritz method for finding some of the eigenvalues of $A$ as the eigenvalues
