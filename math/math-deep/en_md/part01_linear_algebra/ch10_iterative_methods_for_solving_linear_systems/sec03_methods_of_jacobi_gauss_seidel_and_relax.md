# Methods of Jacobi, Gauss–Seidel, and Relaxation


<!-- PAGE 394 -->
with $e_{0} = u_{0} -u = v_{0} -u$. Again, by Proposition 10.2, for every $\epsilon  > 0$, there is some natural
$$ee$$
number $N(\epsilon$ ) such that if $k \ge N(\epsilon$ ), then
$$\sup\|B_{1}^{k}e_{0}\|^{1/k}\le \rho (B_{1}) + \epsilon .$$
$$\|e0\|=1$$
Furthermore, for all $k \ge N(\epsilon$ ), there exists a vector $e_{0} = e_{0}(k)$ (for some suitable choice of $u_{0})$ such that
$$\|e_{0}\|= 1and\|B_{2}^{k}e_{0}\|^{1/k}= \|B_{2}^{k}\|^{1/k}\ge \rho (B_{2}),$$
which implies Statement $(2)$. In light of the above, we see that when we investigate new iterative methods, we have to deal with the following two problems: $1$. Given an iterative method with matrix $B$, determine whether the method is convergent. This involves determining whether $\rho (B) < 1$, or equivalently whether there is a subordinate matrix norm such that $\|B\| < 1$. By Proposition 9.12, this implies that I - $B$ is invertible (since $\|- B\| = \|B\|$, Proposition 9.12 applies). $2$. Given two convergent iterative methods, compare them. The iterative method which is faster is that whose matrix has the smaller spectral radius. We now discuss three iterative methods for solving linear systems: $1$. Jacobi’s method $2$. Gauss–Seidel’s method $3$. The relaxation method.

## 10.3 Description of the Methods of Jacobi,

$$Gauss–Seidel, and Relaxation$$
The methods described in this section are instances of the following scheme: Given a linear system Ax $= b$, with $A$ invertible, suppose we can write $A$ in the form
$$A = M -N,$$
with $M$ invertible, and “easy to invert,” which means that $M$ is close to being a diagonal or a triangular matrix (perhaps by blocks). Then Au $= b$ is equivalent to
$$Mu = Nu + b,$$
that is,
$$u = M^{-1} Nu + M^{-1} b.$$

<!-- PAGE 395 -->
Therefore, we are in the situation described in the previous sections with $B = M^{-1} N$ and $c = M^{-1} b$. In fact, since $A = M$ - $N$, we have
$$B = M^{-1} N = M^{-1} (M -A) = I -M^{-1} A,(*)$$
which shows that I - $B = M^{-1} A$ is invertible. The iterative method associated with the matrix $B = M^{-1} N$ is given by
$$u_{k+1} = M^{-1} Nu_{k} + M^{-1} b,k \ge 0,(\dagger )$$
starting from any arbitrary vector $u_{0}$. From a practical point of view, we do not invert $M$, and instead we solve iteratively the systems
$$Mu_{k+1} = Nu_{k} + b,k \ge 0.$$
Various methods correspond to various ways of choosing $M$ and $N$ from $A$. The first two methods choose $M$ and $N$ as disjoint submatrices of $A$, but the relaxation method allows some overlapping of $M$ and $N$. To describe the various choices of $M$ and $N$, it is convenient to write $A$ in terms of three submatrices $D, E, F$, as
$$A = D -E -F,$$
where the only nonzero entries in $D$ are the diagonal entries in $A$, the only nonzero entries in $E$ are the negatives of nonzero entries in $A$ below the the diagonal, and the only nonzero entries in $F$ are the negatives of nonzero entries in $A$ above the diagonal. More explicitly, if
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & \cdots & a_{1n-1} & a_{1n} \\ a_{21} & a_{22} & a_{23} & \cdots & a_{2n-1} & a_{2n} \\ a_{31} & a_{32} & a_{33} & \cdots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n-1 1} & a_{n-1 2} & a_{n-1 3} & \cdots & a_{n-1n-1} & a_{n-1n} \\ a_{n1} & a_{n2} & a_{n3} & a_{n n-1} & a_{n n} \end{pmatrix} ,$$
$$\cdots$$
then
$$D = \begin{pmatrix} a_{11} & 0 & 0 & \cdots & 0 & 0 \\ 0 & a_{22} & 0 & \cdots & 0 & 0 \\ 0 & 0 & a_{33} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & a_{n-1n-1} & 0 \\ 0 & 0 & 0 & 0 & a_{n n} \end{pmatrix} ,$$
$$\cdots$$

<!-- PAGE 396 -->
$$-E = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & 0 \\ a_{21} & 0 & 0 & \cdots & 0 & 0 \\ a_{31} & a_{32} & 0 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ a_{n-1 1} & a_{n-1 2} & a_{n-1 3} & \ddots & 0 & 0 \\ a_{n1} & a_{n2} & a_{n3} & a_{n n-1} & 0 \end{pmatrix} , -F = \begin{pmatrix} 0 & a_{12} & a_{13} & \cdots & a_{1n-1} & a_{1n} \\ 0 & 0 & a_{23} & \cdots & a_{2n-1} & a_{2n} \\ 0 & 0 & 0 & \ddots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & a_{n-1n} \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} .$$
$$\cdots \cdots$$
In Jacobi’s method, we assume that all diagonal entries in $A$ are nonzero, and we pick
$$M = D$$
$$N = E + F,$$
so that by (*),
$$B = M^{-1} N = D^{-1}(E + F) = I -D^{-1}A.$$
As a matter of notation, we let
$$J = I -D^{-1}A = D^{-1}(E + F),$$
which is called Jacobi’s matrix. The corresponding method, Jacobi’s iterative method, computes the sequence $(u_{k})$ using the recurrence
$$u_{k+1} = D^{-1}(E + F)u_{k} + D^{-1}b,k \ge 0.$$
In practice, we iteratively solve the systems
$$Du_{k+1} = (E + F)u_{k} + b,k \ge 0.$$
If we write $u_{k} = (u_{1}^{k}, \dots  , u_{n}^{k})$, we solve iteratively the following system: $a_{11}u_{1}^{k+1} = -a_{12}u_{2}^{k} -a_{13}u_{3}^{k} \cdots -a_{1n}u_{n}^{k} + b_{1} a_{22}u_{2}^{k+1} = -a_{21}u_{1}^{k} -a_{23}u_{3}^{k} \cdots -a_{2n}u_{n}^{k} + b_{2}$
$$\vdots \vdots \vdots$$
$$.$$
$a_{n-1n-1}u_{n}^{k+1} = -a_{n-1 1}u_{1}^{k} \cdots -a_{n-1n-2}u_{n-2}^{k} -a_{n-1n}u_{n}^{k} + b_{n-1} a_{n n}u_{n}^{k+1-1} = -a_{n1}u_{1}^{k} -a_{n2}u_{2}^{k} \cdots -a_{n n-1}u_{n-1}^{k} + b_{n}$ In Matlab one step of Jacobi iteration is achieved by the following function: function $v =$ Jacobi2(A,b,u) $n =$ size(A,1); $v =$ zeros(n,1); for $i =$ 1:n
$$v(i,1)= u(i,1) + (-A(i,:)*u + b(i))/A(i,i);$$
end end

<!-- PAGE 397 -->
In order to run $m$ iteration steps, run the following function: function $u =$ jacobi(A,b,u0,m) $u =$ u0; for $j =$ 1:m $u =$ Jacobi2(A,b,u); end end

> **Example 10.1.** Consider the linear system
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 25 \\ -24 \\ 21 \\ 15 \end{pmatrix} .$$
$$--$$
We check immediately that the solution is
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
It is easy to see that the Jacobi matrix is
$$J = \frac{1}{2} \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
After $10$ Jacobi iterations, we find the approximate solution
$$x_{1} = 10.2588, x_{2} = -2.5244, x_{3} = 5.8008, x_{4} = -3.7061.$$
After $20$ iterations, we find the approximate solution
$$x_{1} = 10.9110, x_{2} = -2.9429, x_{3} = 6.8560, x_{4} = -3.9647.$$
After $50$ iterations, we find the approximate solution
$$x_{1} = 10.9998, x_{2} = -2.9999, x_{3} = 6.9998, x_{4} = -3.9999,$$
and After $60$ iterations, we find the approximate solution
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
correct up to at least four decimals. It can be shown (see Problem 10.6) that the eigenvalues of $J$ are
$$\cos \begin{pmatrix} \pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 2\pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 3\pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 4\pi \\ 5 \end{pmatrix} ,$$

<!-- PAGE 398 -->
so the spectral radius of $J = B$ is
$$\rho (J) = \cos \begin{pmatrix} \pi \\ 5 \end{pmatrix} = 0.8090 < 1.$$
By Theorem 10.3, Jacobi’s method converges for the matrix of this example. Observe that we can try to “speed up” the method by using the new value $u_{1}^{k+1}$ instead of $u_{1}^{k}$ in solving for $u_{2}^{k+2}$ using the second equations, and more generally, use $u_{1}^{k+1}, \dots  , u_{i-1}^{k+1}$ instead of $u_{1}^{k}, \dots  , u_{i-1}^{k}$ in solving for $u_{i}^{k+1}$ in the ith equation. This observation leads to the system $a_{11}u^{k+1} = -a_{12}u_{2}^{k} -a_{13}u_{3}^{k} \cdots -a_{1n}u_{n}^{k} + b_{1} a_{22}u_{2}^{k1+1} = -a_{21}u_{1}^{k+1} -a_{23}u_{3}^{k} \cdots -a_{2n}u_{n}^{k} + b_{2} \vdots \vdots \vdots a_{n-1n-1}u_{n}^{k+1} = -a_{n-1 1}u_{1}^{k+1} \cdots -a_{n-1n-2}u_{n-2}^{k+1} -a_{n-1n}u_{n}^{k} + b_{n-1} a_{n n}u_{n}^{k+1-1} = -a_{n1}u_{1}^{k+1} -a_{n2}u_{2}^{k+1} \cdots -a_{n n-1}u_{n-1}^{k+1} + b_{n}$, which, in matrix form, is written
$$Du_{k+1} = Eu_{k+1} + Fu_{k} + b.$$
Because $D$ is invertible and $E$ is lower triangular, the matrix $D$ - $E$ is invertible, so the above equation is equivalent to
$$u_{k+1} = (D -E)^{-1}Fu_{k} + (D -E)^{-1}b,k \ge 0.$$
The above corresponds to choosing $M$ and $N$ to be
$$M = D -E$$
$$N = F,$$
and the matrix $B$ is given by
$$B = M^{-1} N = (D -E)^{-1}F.$$
Since $M = D$ - $E$ is invertible, we know that I - $B = M^{-1} A$ is also invertible. The method that we just described is the iterative method of Gauss–Seidel, and the matrix $B$ is called the matrix of Gauss–Seidel and denoted by $\mathcal{L}_{1}$, with
$$\mathcal{L}_{1} = (D -E)^{-1}F.$$
One of the advantages of the method of Gauss–Seidel is that is requires only half of the memory used by Jacobi’s method, since we only need
$$u_{1}^{k+1}, \dots  , u_{i-1}^{k+1} , u_{i+1}^{k}, \dots  , u_{n}^{k}$$
to compute $u_{i}^{k+1}$. We also show that in certain important cases (for example, if $A$ is a tridiagonal matrix), the method of Gauss–Seidel converges faster than Jacobi’s method (in this case, they both converge or diverge simultaneously). In Matlab one step of Gauss–Seidel iteration is achieved by the following function:

<!-- PAGE 399 -->
function $u =$ GaussSeidel3(A,b,u) $n =$ size(A,1); for $i =$ 1:n u(i,1) $=$ u(i,1) $+$ (-A(i,:)*u $+ b(i))/A(i,i)$; end end It is remarkable that the only difference with Jacobi2 is that the same variable $u$ is used on both sides of the assignment. In order to run $m$ iteration steps, run the following function: function $u =$ GaussSeidel1(A,b,u0,m) $u =$ u0; for $j =$ 1:m $u =$ GaussSeidel3(A,b,u); end end

> **Example 10.2.** Consider the same linear system
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 25 \\ -24 \\ 21 \\ 15 \end{pmatrix}$$
$$--$$
as in Example 10.1, whose solution is
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
After $10$ Gauss–Seidel iterations, we find the approximate solution
$$x_{1} = 10.9966, x_{2} = -3.0044, x_{3} = 6.9964, x_{4} = -4.0018.$$
After $20$ iterations, we find the approximate solution
$$x_{1} = 11.0000, x_{2} = -3.0001, x_{3} = 6.9999, x_{4} = -4.0000.$$
After $25$ iterations, we find the approximate solution
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
correct up to at least four decimals. We observe that for this example, Gauss–Seidel’s method converges about twice as fast as Jacobi’s method. It will be shown in Proposition 10.8 that for a tridiagonal matrix, the spectral radius of the Gauss–Seidel matrix $\mathcal{L}_{1}$ is given by
$$\rho (\mathcal{L}_{1}) = (\rho (J))^{2},$$
so our observation is consistent with the theory.

<!-- PAGE 400 -->
The new ingredient in the relaxation method is to incorporate part of the matrix $D$ into $N$: we define $M$ and $N$ by
$$M = \frac{D}{\omega} -E$$
$$-$$
$$N = \frac{1\omega}{\omega} D + F,$$
where $\omega  \neq  0$ is a real parameter to be suitably chosen. Actually, we show in Section 10.4 that for the relaxation method to converge, we must have $\omega  \in (0, 2)$. Note that the case $\omega  = 1$ corresponds to the method of Gauss–Seidel. If we assume that all diagonal entries of $D$ are nonzero, the matrix $M$ is invertible. The matrix $B$ is denoted by $\mathcal{L}_{\omega}$ and called the matrix of relaxation, with
$$-1$$
$$\mathcal{L}_{\omega} = \begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \end{pmatrix} = (D -\omega E)^{-1}((1 -\omega )D + \omega F).$$
The number $\omega$  is called the parameter of relaxation. When $\omega  > 1$, the relaxation method is known as successive overrelaxation, abbreviated as SOR. At first glance the relaxation matrix $\mathcal{L}_{\omega}$ seems a lot more complicated than the Gauss– Seidel matrix $\mathcal{L}_{1}$, but the iterative system associated with the relaxation method is very similar to the method of Gauss–Seidel, and is quite simple. Indeed, the system associated with the relaxation method is given by
$$\begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} u_{k+1} = \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \end{pmatrix} u_{k} + b,$$
which is equivalent to
$$(D -\omega E)u_{k+1} = ((1 -\omega )D + \omega F)u_{k} + \omega b,$$
and can be written
$$Du_{k+1} = Du_{k} -\omega (Du_{k} -Eu_{k+1} -Fu_{k} -b).$$
Explicitly, this is the system $a_{11}u_{1}^{k+1} = a_{11}u_{1}^{k}$ - $\omega (a_{11}u_{1}^{k} + a_{12}u_{2}^{k} + a_{13}u_{3}^{k} + \cdots  + a_{1n-2}u_{n-2}^{k} + a_{1n-1}u_{n-1}^{k} + a_{1n}u_{n}^{k}$ - $b_{1}) a_{22}u_{2}^{k+1} = a_{22}u_{2}^{k}$ - $\omega (a_{21}u_{1}^{k+1} + a_{22}u_{2}^{k} + a_{23}u_{3}^{k} + \cdots  + a_{2n-2}u_{n-2}^{k} + a_{2n-1}u_{n-1}^{k} + a_{2n}u_{n}^{k}$ - $b_{2})$
$$\vdots$$
$a_{n n}u_{n}^{k+1} = a_{n n}u_{n}^{k}$ - $\omega (a_{n1}u_{1}^{k+1} + a_{n2}u_{2}^{k+1} + \cdots  + a_{n n-2}u_{n-2}^{k+1} + a_{n n-1}u_{n-1}^{k+1} + a_{n n}u_{n}^{k}$ - $b_{n})$. In Matlab one step of relaxation iteration is achieved by the following function:

<!-- PAGE 401 -->
function $u =$ relax3(A,b,u,omega) $n =$ size(A,1); for $i =$ 1:n u(i,1) $=$ u(i,1) $+$ omega*(-A(i,:)*u $+ b(i))/A(i,i)$; end end Observe that function relax3 is obtained from the function GaussSeidel3 by simply inserting $\omega$  in front of the expression (-A(i, $:)*u+b(i))/A(i, i)$. In order to run $m$ iteration steps, run the following function: function $u =$ relax(A,b,u0,omega,m) $u =$ u0; for $j =$ 1:m $u =$ relax3(A,b,u,omega); end end

> **Example 10.3.** Consider the same linear system as in Examples 10.1 and 10.2, whose solution is
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
After $10$ relaxation iterations with $\omega  =$ 1.1, we find the approximate solution
$$x_{1} = 11.0026, x_{2} = -2.9968, x_{3} = 7.0024, x_{4} = -3.9989.$$
After $10$ iterations with $\omega  =$ 1.2, we find the approximate solution
$$x_{1} = 11.0014, x_{2} = -2.9985, x_{3} = 7.0010, x_{4} = -3.9996.$$
After $10$ iterations with $\omega  =$ 1.3, we find the approximate solution
$$x_{1} = 10.9996, x_{2} = -3.0001, x_{3} = 6.9999, x_{4} = -4.0000.$$
After $10$ iterations with $\omega  =$ 1.27, we find the approximate solution
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
correct up to at least four decimals. We observe that for this example the method of relaxation with $\omega  =$ 1.27 converges faster than the method of Gauss–Seidel. This observation will be confirmed by Proposition 10.10. What remains to be done is to find conditions that ensure the convergence of the relaxation method (and the Gauss–Seidel method), that is: $1$. Find conditions on $\omega$ , namely some interval $I \subseteq \mathbb{R}$ so that $\omega  \in$ I implies $\rho (\mathcal{L}_{\omega}) < 1$; we will prove that $\omega  \in (0, 2)$ is a necessary condition.
