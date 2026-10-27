# Time-Dependent Boundary Problems


<!-- PAGE 705 -->
$1$. “Good” triangulations must be found. This in itself is a vast research topic. Delaunay triangulations are good candidates. $2$. “Good” spaces of functions must be found; typically piecewise polynomials and splines. $3$. “Good” bases consisting of functions will small support must be found, so that integrals can be easily computed and sparse banded matrices arise. We now consider boundary problems where the solution varies with time.

## 19.3 Time-Dependent Boundary Problems: The Wave

$$Equation$$
Consider a homogeneous string (or rope) of constant cross-section, of length $L$, and stretched (in a vertical plane) between its two ends which are assumed to be fixed and located along the x-axis at $x = 0$ and at $x = L$.
$$Figure 19.6: A vibrating string$$
The string is subjected to a transverse force $\tau$ f(x)dx per element of length dx (where $\tau$  is the tension of the string). We would like to investigate the small displacements of the string in the vertical plane, that is, how it vibrates. Thus, we seek a function u(x, $t)$ defined for $t \ge 0$ and $x \in [0, L]$, such that u(x, $t)$ represents the vertical deformation of the string at the abscissa $x$ and at time $t$. It can be shown that $u$ must satisfy the following PDE
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = f(x, t),0 < x < L, t > 0,$$
with $c = p\overline{\tau /\rho}$, where $\rho$  is the linear density of the string, known as the one-dimensional wave equation. Furthermore, the initial shape of the string is known at $t = 0$, as well as the distribution of the initial velocities along the string; in other words, there are two functions $u_{i,0}$ and $u_{i,1}$

<!-- PAGE 706 -->
such that
$$u(x, 0) = u_{i,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L.$$
For example, if the string is simply released from its given starting position, we have $u_{i,1} = 0$. Lastly, because the ends of the string are fixed, we must have
$$u(0, t) = u(L, t) = 0,t \ge 0.$$
Consequently, we look for a function $u: \mathbb{R}_{+} \times  [0, L] \to \mathbb{R}$ satisfying the following conditions:
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = f(x, t),0 < x < L, t > 0,$$
$$u(0, t) = u(L, t) = 0,t \ge 0(boundary condition),$$
$$u(x, 0) = u_{i,0}(x),0 \le x \le L(intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L(intitial condition).$$
This is an example of a time-dependent boundary-value problem, with two initial conditions. To simplify the problem, assume that $f = 0$, which amounts to neglecting the effect of gravity. In this case, our PDE becomes
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) - \frac{\partial^{2} u}{\partial x^{2}} (x, t) = 0,0 < x < L, t > 0,$$
Let us try our trick of multiplying by a test function $v$ depending only on $x, C^{1}$ on $[0, L]$, and such that v(0) $=$ v(L) $= 0$, and integrate by parts. We get the equation
$$\int_{0}^{}  L \frac{\partial^{2} u}{\partial t^{2}} (x, t)v(x)dx -c^{2} \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = 0.$$
For the first term, we get
$$\int_{0}^{}  L \frac{\partial^{2} u}{\partial t^{2}} (x, t)v(x)dx = \int_{0}^{}  L \frac{\partial^{2}}{\partial t^{2}} [u(x, t)v(x)]dx$$
$$= \frac{d^{2}}{dt^{2}} \int_{0}^{}  Lu(x, t)v(x)dx$$
$$= \frac{d^{2}}{dt^{2}} \langle u, v\rangle ,$$

<!-- PAGE 707 -->
where $\langle u, v\rangle$ is the inner product in $L^{2}([0, L])$. The fact that it is legitimate to move $\partial^{2} /\partial t^{2}$ outside of the integral needs to be justified rigorously, but we won’t do it here. For the second term, we get
$$- \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = - \frac{\partial u}{\partial x} (x, t)v(x)x=L+ \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx,$$
$$x=0$$
and because $v \in V$ , we have v(0) $=$ v(L) $= 0$, so we obtain
$$- \int_{0}^{}  L \frac{\partial^{2} u}{\partial x^{2}} (x, t)v(x)dx = \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx.$$
Our integrated equation becomes
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + c^{2} \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{dv}{dx} (x)dx = 0,for all v \in Vand all t \ge 0.$$
It is natural to introduce the bilinear form a: $V \times  V \to \mathbb{R}$ given by
$$a(u, v) = \int_{0}^{}  L \frac{\partial u}{\partial x} (x, t) \frac{\partial v}{\partial x} (x, t)dx,$$
where, for every $t \in \mathbb{R}_{+}$, the functions u(x, $t)$ and $(v, t)$ belong to $V$ . Actually, we have to replace $V$ by the subspace of the Sobolev space $H_{0}^{1}(0, L)$ consisting of the functions such that v(0) $=$ v(L) $= 0$. Then, the weak formulation (variational formulation) of our problem is this: Find a function $u \in V$ such that
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + a(u, v) = 0,for all v \in Vand all t \ge 0$$
$$u(x, 0) = u_{i,0}(x),0 \le x \le L(intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),0 \le x \le L(intitial condition).$$
It can be shown that there is a positive constant $\alpha  > 0$ such that
$$a(u, u) \ge \alpha  \|u\|_{H1}^{2}for all v \in V$$
$$0$$
(Poincar´e’s inequality), which shows that a is positive definite on $V$ . The above method is known as the method of Rayleigh-Ritz. A study of the above equation requires some sophisticated tools of analysis which go far beyond the scope of these notes. Let us just say that there is a countable sequence of solutions with separated variables of the form
$$u_{k}^{(1)}= \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \cos \begin{pmatrix} k\pi ct \\ L \end{pmatrix} ,u_{k}^{(2)}= \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \sin \begin{pmatrix} k\pi ct \\ L \end{pmatrix} ,k \in \mathbb{N}_{+},$$

<!-- PAGE 708 -->
called modes (or normal modes). Complete solutions of the problem are series obtained by combining the normal modes, and they are of the form
$$u(x, t) = \sum_{k=1}^{\infty}  \sin \begin{pmatrix} k\pi x \\ L \end{pmatrix} \begin{pmatrix} k\pi ct \\ A_{k} \cos \\ L \end{pmatrix} \begin{pmatrix} k\pi ct \\ + B_{k} \sin \\ L \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
where the coefficients $A_{k}, B_{k}$ are determined from the Fourier series of $u_{i,0}$ and $u_{i,1}$. We now consider discrete approximations of our problem. As before, consider a finite dimensional subspace $V_{a}$ of $V$ and assume that we have approximations $u_{a,0}$ and $u_{a,1}$ of $u_{i,0}$ and $u_{i,1}$. If we pick a basis $(w_{1}, \dots  , w_{n})$ of $V_{a}$, then we can write our unknown function u(x, $t)$ as
$$u(x, t) = u_{1}(t)w_{1} + \cdots  + u_{n}(t)w_{n},$$
where $u_{1}, \dots  , u_{n}$ are functions of $t$. Then, if we write $u = (u_{1}, \dots  , u_{n})$, the discrete version of our problem is
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0,$$
$$u(x, 0) = u_{a,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),0 \le x \le L,$$
where $A = (\langle w_{i}, w_{j}\rangle$ ) and $K = (a(w_{i}, w_{j}))$ are two symmetric matrices, called the mass matrix and the stiffness matrix, respectively. In fact, because a and the inner product $\langle$ -, $-\rangle$ are positive definite, these matrices are also positive definite. We have made some progress since we now have a system of ODE’s, and we can solve it by analogy with the scalar case. So, we look for solutions of the form $U$ cos $\omega t$ (or $U$ sin $\omega t)$, where $U$ is an $n$-dimensional vector. We find that we should have
$$(K -\omega^{2} A)U \cos \omega t = 0,$$
which implies that $\omega$  must be a solution of the equation
$$KU = \omega^{2} AU.$$
Thus, we have to find some $\lambda$  such that
$$KU = \lambda AU,$$
a problem known as a generalized eigenvalue problem, since the ordinary eigenvalue problem for $K$ is
$$KU = \lambda U.$$

<!-- PAGE 709 -->
Fortunately, because $A$ is SPD, we can reduce this generalized eigenvalue problem to a standard eigenvalue problem. A good way to do so is to use a Cholesky decomposition of $A$ as
$$A = LL^{\top},$$
where $L$ is a lower triangular matrix (see Theorem 8.10). Because $A$ is SPD, it is invertible, so $L$ is also invertible, and
$$KU = \lambda AU = \lambda LL^{\top}U$$
yields
$$L^{-1}KU = \lambda L^{\top}U,$$
which can also be written as
$$L^{-1}K(L^{\top})^{-1}L^{\top}U = \lambda L^{\top}U.$$
Then, if we make the change of variable
$$Y = L^{\top}U,$$
using the fact $(L^{\top})^{-1} = (L^{-1})^{\top}$, the above equation is equivalent to
$$L^{-1}K(L^{-1})^{\top}Y = \lambda Y,$$
a standard eigenvalue problem for the matrix $K = L^{-1}K(L^{-1})^{\top}$. Furthermore, we know
$$b$$
from Section 8.8 that since $K$ is SPD and $L^{-1}$ is invertible, the matrix $K = L^{-1}K(L^{-1})^{\top}$ is
$$b$$
also SPD. Consequently, $K$ has positive real eigenvalues $(\omega_{1}^{2} , \dots  , \omega_{n}^{2}$ ) (not necessarily distinct) and
$$b$$
it can be diagonalized with respect to an orthonormal basis of eigenvectors, say $Y^{1}, \dots  , Y^{n}$. Then, since $Y = L^{\top}U$, the vectors
$$U^{i}= (L^{\top})^{-1}Y^{i},i = 1, \dots  , n,$$
are linearly independent and are solutions of the generalized eigenvalue problem; that is,
$$KU^{i}= \omega_{i}^{2}  AU^{i},i = 1, \dots  , n.$$
More is true. Because the vectors $Y^{1}, \dots  , Y^{n}$ are orthonormal, and because $Y^{i} = L^{\top}U^{i}$, from
$$(Y^{i})^{\top}Y^{j}= \delta_{ij} ,$$
we get
$$(U^{i})^{\top}LL^{\top}U^{j}= \delta_{ij} ,1 \le i, j \le n,$$
and since $A = LL^{\top}$, this yields
$$(U^{i})^{\top}AU^{j}= \delta_{ij} ,1 \le i, j \le n.$$

<!-- PAGE 710 -->
This suggests defining the functions $U^{i} \in V_{a}$ by
$$U^{i}  = \sum_{k=1}^{n}  U_{k}^{i}w_{k}.$$
Then, it immediate to check that
$$a(U^{i}, U^{j}) = (U^{i})^{\top}AU^{j}= \delta_{ij} ,$$
which means that the functions $(U^{1} , \dots  , U^{n}$ ) form an orthonormal basis of $V_{a}$ for the inner product a. The functions $U^{i} \in V_{a}$ are called modes (or modal vectors). As a final step, let us look again for a solution of our discrete weak formulation of the problem, this time expressing the unknown solution u(x, $t)$ over the modal basis $(U^{1} , \dots  , U^{n}$ ), say
$$u = \sum_{j=1}^{n}  u_{j}e(t)U^{j} ,$$
where each $u_{j}$ is a function of $t$. Because
$$e$$
$$! !$$
$$u = \sum_{j=1}^{n}  u_{j}(t)U^{j}  = \sum_{j=1}^{n}  u_{j}(t) \sum_{k=1}^{n}  U_{k}^{j}w_{k}= \sum_{k=1}^{n}  \sum_{j=1}^{n}  u_{j}(t)U_{k}^{j}w_{k},$$
$$eee$$
$$if we write u = (u_{1}, \dots  , u_{n}) with u_{k} = \sum_{j}  n=1u_{j}e(t)U_{k}^{j} for k = 1, \dots  , n, we see that$$
$$u = \sum_{j=1}^{n}  u_{j}eU^{j},$$
so using the fact that
$$KU^{j}= \omega_{j}^{2} AU^{j},j = 1, \dots  , n,$$
the equation
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0$$
yields
$$\sum_{j=1}^{n}  [(u_{j})'' + \omega_{j}^{2} u_{j}]AU^{j} = 0.$$
$$e e$$
Since $A$ is invertible and since $(U^{1}, \dots  , U^{n})$ are linearly independent, the vectors $(AU^{1}, \dots  , AU^{n})$ are linearly independent, and consequently we get the system of $n$ ODEs’
$$(u_{j})''+ \omega_{j}^{2} u_{j} = 0,1 \le j \le n.$$
$$e e$$
Each of these equation has a well-known solution of the form
$$u_{j} = A_{j} \cos \omega_{j} t + B_{j} \sin \omega_{j} t.$$
$$e$$

<!-- PAGE 711 -->
Therefore, the solution of our approximation problem is given by
$$u = \sum_{j=1}^{n}  (A_{j} \cos \omega_{j} t + B_{j} \sin \omega_{j} t)U^{j} ,$$
and the constants $A_{j}, B_{j}$ are obtained from the intial conditions
$$u(x, 0) = u_{a,0}(x),0 \le x \le L,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),0 \le x \le L,$$
by expressing $u_{a,0}$ and $u_{a,1}$ on the modal basis $(U^{1} , \dots  , U^{n}$ ). Furthermore, the modal functions $(U^{1} , \dots  , U^{n}$ ) form an orthonormal basis of $V_{a}$ for the inner product a. If we use the vector space $V_{N}^{0}$  of piecewise affine functions, we find that the matrices $A$ and $K$ are familar! Indeed,
$$A = \frac{1}{h} \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & -1 & 2 \end{pmatrix}$$
and
$$K = \frac{h}{6} \begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 1 & 4 \end{pmatrix} .$$
To conclude this section, let us discuss briefly the wave equation for an elastic membrane, as described in Section 19.2. This time, we look for a function $u: \mathbb{R}_{+} \times  \Omega \to \mathbb{R}$ satisfying the following conditions:
$$\frac{1}{c^{2}} \frac{\partial^{2} u}{\partial t^{2}} (x, t) -\Delta u(x, t) = f(x, t),x \in \Omega , t > 0,$$
$$u(x, t) = 0,x \in \Gamma ,t \ge 0(boundary condition),$$
$$u(x, 0) = u_{i,0}(x),x \in \Omega (intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),x \in \Omega (intitial condition).$$
Assuming that $f = 0$, we look for solutions in the subspace $V$ of the Sobolev space $H_{0}^{1}\overline{(\Omega$ )} consisting of functions $v$ such that $v = 0$ on $\Gamma$ . Multiplying by a test function $v \in V$ and using Green’s first identity, we get the weak formulation of our problem:

<!-- PAGE 712 -->
Find a function $u \in V$ such that
$$\frac{d^{2}}{dt^{2}} \langle u, v\rangle + a(u, v) = 0,for all v \in Vand all t \ge 0$$
$$u(x, 0) = u_{i,0}(x),x \in \Omega (intitial condition),$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{i,1}(x),x \in \Omega (intitial condition),$$
where a: $V \times  V \to \mathbb{R}$ is the bilinear form given by
$$a(u, v) = \int_{\Omega}  \begin{pmatrix} \partial u \\ \partial v & \partial u\partial v \\ + \\ \partial x_{1}\partial x_{1} & \partial x_{2}\partial x_{2} \end{pmatrix} dx,$$
$$and \int_{\Omega}$$
$$\langle u, v\rangle =uvdx.$$
As usual, we find approximations of our problem by using finite dimensional subspaces $V_{a}$ of $V$ . Picking some basis $(w_{1}, \dots  , w_{n})$ of $V_{a}$, and triangulating $\Omega$ , as before, we obtain the equation
$$A \frac{d^{2}u}{dt^{2}} + Ku = 0,$$
$$u(x, 0) = u_{a,0}(x),x \in \Gamma ,$$
$$\frac{\partial u}{\partial t} (x, 0) = u_{a,1}(x),x \in \Gamma ,$$
where $A = (\langle w_{i}, w_{j}\rangle$ ) and $K = (a(w_{i}, w_{j}))$ are two symmetric positive definite matrices. In principle, the problem is solved, but, it may be difficult to find good spaces $V_{a}$, good triangulations of $\Omega$ , and good bases of $V_{a}$, to be able to compute the matrices $A$ and $K$, and to ensure that they are sparse.
