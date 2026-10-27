# Power Methods


<!-- PAGE 686 -->
of the symmetric (respectively Hermitian) tridiagonal matrix $H_{n}$ applies, but there are more methods for finding the eigenvalues of symmetric (respectively Hermitian) tridiagonal matrices. Also theorems about error estimates exist. The version of Lanczos iteration given above may run into problems in floating point arithmetic. What happens is that the vectors $u_{j}$ may lose the property of being orthogonal, so it may be necessary to reorthogonalize them. For more on all this, see Demmel $[48]$ (Chapter $7$, in particular Section 7.2-7.4). The version of GMRES using Lanczos iteration is called MINRES. We close our brief survey of methods for computing the eigenvalues and the eigenvectors of a matrix with a quick discussion of two methods known as power methods.

## 18.7 Power Methods

Let $A$ be an $m \times  m$ complex or real matrix. There are two power methods, both of which yield one eigenvalue and one eigenvector associated with this vector:
$(1)$ Power iteration.
$(2)$ Inverse (power) iteration. Power iteration only works if the matrix $A$ has an eigenvalue $\lambda$  of largest modulus, which means that if $\lambda_{1} , \dots  , \lambda_{m}$  are the eigenvalues of $A$, then
$$|\lambda_{1} | > |\lambda_{2} | \ge \cdots  \ge |\lambda_{m} | \ge 0.$$
In particular, if $A$ is a real matrix, then $\lambda_{1}$  must be real (since otherwise there are two complex conjugate eigenvalues of the same largest modulus). If the above condition is satisfied, then power iteration yields $\lambda_{1}$  and some eigenvector associated with it. The method is simple enough: Pick some initial unit vector $x^{0}$ and compute the following sequence $(x^{k})$, where
$$x^{k+1}= \frac{Ax^{k}}{\|Ax^{k}\|} ,k \ge 0.$$
We would expect that $(x^{k})$ converges to an eigenvector associated with $\lambda_{1}$ , but this is not quite correct. The following results are proven in Serre $[162]$ (Section 13.5.1). First assume that $\lambda_{1}  \neq  0$. We have
$$lim

$Ax^{k}$

$= |\lambda_{1}$ |.$$
$$k\mapsto \infty$$
If $A$ is a complex matrix which has a unique complex eigenvalue $\lambda_{1}$  of largest modulus, then
$$k$$
$$v = klim\mapsto \infty \begin{pmatrix} \overline{\lambda}_{1} \\ |\lambda_{1} | \end{pmatrix} x^{k}$$

<!-- PAGE 687 -->
is a unit eigenvector of $A$ associated with $\lambda_{1}$ . If $\lambda_{1}$  is real, then
$$v = limx^{k}$$
$$k\mapsto \infty$$
is a unit eigenvector of $A$ associated with $\lambda_{1}$ . Actually some condition on $x^{0}$ is needed: $x^{0}$ must have a nonzero component in the eigenspace $E$ associated with $\lambda_{1}$  (in any direct sum $\mathbb{C}^{m}$ of in which $E$ is a summand). The eigenvalue $\lambda_{1}$  is found as follows. If $\lambda_{1}$  is complex, and if $v_{j}$ ̸ $= 0$ is any nonzero coordinate of $v$, then
$$\lambda_{1}  = klim\mapsto \infty \frac{(Ax^{k})_{j}}{x_{j}^{k}} .$$
If $\lambda_{1}$  is real, then we can define the sequence $(\lambda^{(k)}$ ) by
$$\lambda^{(k+1)} = (x^{k+1})^{*}Ax^{k+1},k \ge 0,$$
and we have
$$\lambda_{1}  = lim\lambda^{(k)} .$$
$$k\mapsto \infty$$
Indeed, in this case, since $v = lim_{k\mapsto \infty} x^{k}$ and $v$ is a unit eigenvector for $\lambda_{1}$ , we have
$$lim\lambda^{(k)} = lim(x^{k+1})^{*}Ax^{k+1}= v^{*}Av = \lambda_{1} v^{*}v = \lambda_{1} .$$
$$k\mapsto \infty k\mapsto \infty$$
Note that since $x^{k+1}$ is a unit vector, $(x^{k+1})^{*}Ax^{k+1}$ is a Rayleigh ratio. If $A$ is a Hermitian matrix, then the eigenvalues are real and we can say more about the rate of convergence, which is not great (only linear). For details, see Trefethen and Bau $[182]$ (Lecture $27)$. If $\lambda_{1}  = 0$, then there is some power $\ell < m$ such that $Ax^{\ell} = 0$. The inverse iteration method is designed to find an eigenvector associated with an eigenvalue $\lambda$  of $A$ for which we know a good approximation $\mu$ . Pick some initial unit vector $x^{0}$ and compute the following sequences $(w^{k})$ and $(x^{k})$, where $w^{k+1}$ is the solution of the system
$$(A -\mu I)w^{k+1}= x^{k}equivalentlyw^{k+1}= (A -\mu I)^{-1}x^{k},k \ge 0,$$
and
$$x^{k+1}= \frac{w^{k+1}}{\|w^{k+1}\|} ,k \ge 0.$$
The following result is proven in Ciarlet $[41]$ (Theorem 6.4.1).
