# Convergence Methods for Tridiagonal Matrices


<!-- PAGE 405 -->

> **Proposition 10.7.** Given any matrix $A = D$ - $E$ - $F$, with $A$ and $D$ invertible, for any $\omega  \neq  0$, we have
$$\rho (\mathcal{L}_{\omega}) \ge |\omega  -1|,$$
$$-1$$
$$where \mathcal{L}_{\omega} = \begin{pmatrix} D-E \\ \overline{\omega} \end{pmatrix} \begin{pmatrix} 1-\omega D + F \\ \overline{\omega} \\ \omega & (0, 2). \end{pmatrix} . Therefore, the relaxation method (possibly by blocks)$$
does not converge unless  $\in$  If we allow $\omega$  to be complex, then we must have
$$|\omega  -1| < 1$$
for the relaxation method to converge.

*Proof.* Observe that the product $\lambda_{1}  \cdots  \lambda_{n}$  of the eigenvalues $of\mathcal{L}_{\omega}$, which is equal to $det(\mathcal{L}_{\omega})$, is given by
$$\lambda_{1}  \cdots  \lambda_{n}  = \det(\mathcal{L}_{\omega}) = \frac{\det}{\det} \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \\ D &  \end{pmatrix} = (1 -\omega )^{n}.$$
$$\begin{pmatrix} -E \\ \omega \end{pmatrix}$$
It follows that
$$\rho (\mathcal{L}_{\omega}) \ge |\lambda_{1}  \cdots  \lambda_{n} |^{1/n}= |\omega  -1|.$$
The proof is the same if $\omega  \in \mathbb{C}$.

## 10.5 Convergence of the Methods of Jacobi,

$$Gauss–Seidel, and Relaxation for$$
$$Tridiagonal Matrices$$
We now consider the case where $A$ is a tridiagonal matrix, possibly by blocks. In this case, we obtain precise results about the spectral radius of $J$ and $\mathcal{L}_{\omega}$, and as a consequence, about the convergence of these methods. We also obtain some information about the rate of convergence of these methods. We begin with the case $\omega  = 1$, which is technically easier to deal with. The following proposition gives us the precise relationship between the spectral radii $\rho (J)$ and $\rho (\mathcal{L}_{1})$ of the Jacobi matrix and the Gauss–Seidel matrix.

> **Proposition 10.8.** Let $A$ be a tridiagonal matrix (possibly by blocks). If $\rho (J)$ is the spectral radius of the Jacobi matrix and $\rho (\mathcal{L}_{1})$ is the spectral radius of the Gauss–Seidel matrix, then we have
$$\rho (\mathcal{L}_{1}) = (\rho (J))^{2}.$$
Consequently, the method of Jacobi and the method of Gauss–Seidel both converge or both diverge simultaneously (even when $A$ is tridiagonal by blocks); when they converge, the method of Gauss–Seidel converges faster than Jacobi’s method.

<!-- PAGE 406 -->

*Proof.* We begin with a preliminary result. Let $A(\mu$ ) be a tridiagonal matrix by block of the form
$$A(\mu ) = \begin{pmatrix} A_{1} & \mu^{-1} C_{1} & 0 & 0 & \cdots & 0 \\ \mu B_{1} & A_{2} & \mu^{-1} C_{2} & 0 & \cdots & 0 \\ 0 & \ddots & \ddots & \ddots & \cdots & \vdots \\ \vdots & \cdots & \ddots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & \mu B_{p-2} & A_{p-1} & \mu^{-1} C_{p-1} \\ 0 & 0 & \mu B_{p-1} & A_{p} \end{pmatrix} ,$$
$$\cdots \cdots$$
then
$$\det(A(\mu )) = \det(A(1)),\mu  \neq  0.$$
To prove this fact, form the block diagonal matrix
$$P(\mu ) = \mathrm{diag}(\mu I_{1}, \mu^{2} I_{2}, \dots  , \mu^{p} I_{p}),$$
where $I_{j}$ is the identity matrix of the same dimension as the block $A_{j}$. Then it is easy to see that
$$A(\mu ) = P(\mu )A(1)P(\mu )^{-1},$$
and thus,
$$\det(A(\mu )) = \det(P(\mu )A(1)P(\mu )^{-1}) = \det(A(1)).$$
Since the Jacobi matrix is $J = D^{-1}(E + F)$, the eigenvalues of $J$ are the zeros of the characteristic polynomial
$$p_{J}(\lambda ) = \det(\lambda I -D^{-1}(E + F)),$$
and thus, they are also the zeros of the polynomial
$$q_{J}(\lambda ) = \det(\lambda D -E -F) = \det(D)p_{J}(\lambda ).$$
Similarly, since the Gauss–Seidel matrix is $\mathcal{L}_{1} = (D -E)^{-1}F$, the zeros of the characteristic polynomial
$$p_{L1}(\lambda ) = \det(\lambda I -(D -E)^{-1}F)$$
are also the zeros of the polynomial
$$q_{L1}(\lambda ) = \det(\lambda D -\lambda E -F) = \det(D -E)p_{L1}(\lambda ).$$
Since $A = D$ - $E$ - $F$ is tridiagonal (or tridiagonal by blocks), $\lambda^{2} D$ - $\lambda^{2} E$ - $F$ is also tridiagonal (or tridiagonal by blocks), and by using our preliminary result with $\mu  = \lambda  \neq  0$ starting with the matrix $\lambda^{2} D$ - $\lambda E$ - $\lambda F$, we get
$$\lambda^{n} q_{J}(\lambda ) = \det(\lambda^{2} D -\lambda E -\lambda F) = \det(\lambda^{2} D -\lambda^{2} E -F) = q_{L1}(\lambda^{2} ).$$
By continuity, the above equation also holds for $\lambda  = 0$. But then we deduce that:

<!-- PAGE 407 -->
$1$. For any $\beta  \neq  0$, if $\beta$  is an eigenvalue of $\mathcal{L}_{1}$, then $\beta^{1/2}$ and $-\beta^{1/2}$ are both eigenvalues of $J$, where $\beta^{1/2}$ is one of the complex square roots of $\beta$ . $2$. For any $\alpha  \neq  0, \alpha$  is an eigenvalues of $J$ iff $-\alpha$  is an eigenvalues of $J$, and if $\alpha$  is an eigenvalues of $J$, then $\alpha^{2}$ is an eigenvalue of $\mathcal{L}_{1}$. The above immediately implies that $\rho (\mathcal{L}_{1}) = (\rho (J))^{2}$. We now consider the more general situation where $\omega$  is any real in $(0, 2)$.

> **Proposition 10.9.** Let $A$ be a tridiagonal matrix (possibly by blocks), and assume that the eigenvalues of the Jacobi matrix are all real. If $\omega  \in (0, 2)$, then the method of Jacobi and the method of relaxation both converge or both diverge simultaneously (even when $A$ is tridiagonal by blocks). When they converge, the function $\omega  \mapsto \rho (\mathcal{L}_{\omega})$ (for $\omega  \in (0, 2))$ has a unique minimum equal to $\omega_{0}$  - $1$ for
$$\omega_{0}  = \frac{2}{1 +p1 -(\rho (J))^{2}} ,$$
where $1 < \omega_{0}  < 2$ if $\rho (J) > 0$.

*Proof.* The proof is very technical and can be found in Serre $[162]$ and Ciarlet $[41]$. As in the proof of the previous proposition, we begin by showing that the eigenvalues of the matrix $\mathcal{L}_{\omega}$ are the zeros of the polynomial
$$q_{L\omega}(\lambda ) = \det \begin{pmatrix} \lambda  + \omega  -1 \\ D -\lambda E -F \\ \omega \end{pmatrix} = \det \begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} p_{L\omega}(\lambda ),$$
where $p_{L\omega}(\lambda$ ) is the characteristic polynomial of $\mathcal{L}_{\omega}$. Then using the preliminary fact from Proposition 10.8, it is easy to show that
$$q_{L\omega}(\lambda^{2} ) = \lambda^{n} q_{J} \begin{pmatrix} \lambda^{2}  + \omega  -1 \\ \lambda \omega \end{pmatrix} ,$$
for all $\lambda  \in \mathbb{C}$, with $\lambda  \neq  0$. This time we cannot extend the above equation to $\lambda  = 0$. This leads us to consider the equation
$$\frac{\lambda^{2} + \omega 1}{\lambda \omega} -= \alpha ,$$
which is equivalent to
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0,$$
for all $\lambda  \neq  0$. Since $\lambda  \neq  0$, the above equivalence does not hold for $\omega  = 1$, but this is not a problem since the case $\omega  = 1$ has already been considered in the previous proposition. Then we can show the following:

<!-- PAGE 408 -->
$1$. For any $\beta  \neq  0$, if $\beta$  is an eigenvalue of $\mathcal{L}_{\omega}$, then
$$- -$$
$$\frac{\beta  + \omega 1}{\beta^{1/2} \omega} ,- \frac{\beta  + \omega 1}{\beta^{1/2} \omega}$$
are eigenvalues of $J. 2$. For every $\alpha  \neq  0$, if $\alpha$  and $-\alpha$  are eigenvalues of $J$, then $\mu_{+} (\alpha , \omega$ ) and $\mu_{-} (\alpha , \omega$ ) are eigenvalues of $\mathcal{L}_{\omega}$, where $\mu_{+} (\alpha , \omega$ ) and $\mu_{-} (\alpha , \omega$ ) are the squares of the roots of the equation
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0.$$
It follows that
$$\rho (\mathcal{L}_{\omega}) =\max{\max(|\mu_{+} (\alpha , \omega )|, |\mu_{-} (\alpha , \omega )|)},$$
$$\alpha  | pJ(\alpha )=0$$
and since we are assuming that $J$ has real roots, we are led to study the function
$$M(\alpha , \omega ) = \max{|\mu_{+} (\alpha , \omega )|, |\mu_{-} (\alpha , \omega )|},$$
where $\alpha  \in \mathbb{R}$ and $\omega  \in (0, 2)$. Actually, because $M(-\alpha , \omega$ ) $= M(\alpha , \omega$ ), it is only necessary to consider the case where $\alpha  \ge 0$. Note that for $\alpha  \neq  0$, the roots of the equation
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0.$$
are
$$\frac{\alpha \omega \sqrt{\alpha}^{2}\overline{\omega}^{2}\overline{4}\overline{\omega}\overline{+ 4}}{2} \pm  \overline{-}.$$
In turn, this leads to consider the roots of the equation
$$\omega^{2} \alpha^{2} -4\omega  + 4 = 0,$$
which are
$$\frac{2(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} \pm \overline{-},$$
for $\alpha  \neq  0$. Since we have
$$\overline{-} \overline{-} -\overline{-}$$
$$\frac{2(1 +\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} = \frac{2(1 +\sqrt{1}\overline{\alpha}^{2})(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2} (1 -1 -\alpha^{2} )} \sqrt= \frac{2}{1 -1 -\alpha^{2}} \sqrt$$
and
$$-\overline{-} \overline{-} -\overline{-}$$
$$\frac{2(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} = \frac{2(1 +\sqrt{1}\overline{\alpha}^{2})(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2} (1 +1 -\alpha^{2} )} \sqrt= \frac{2}{1 +1 -\alpha^{2}} \sqrt,$$
these roots are
$$\omega_{0} (\alpha ) = \frac{2}{1 +1 -\alpha^{2}} \sqrt,\omega_{1} (\alpha ) = \frac{2}{1 -1 -\alpha^{2}} \sqrt.$$

<!-- PAGE 409 -->
Observe that the expression for $\omega_{0} (\alpha$ ) is exactly the expression in the statement of our proposition! The rest of the proof consists in analyzing the variations of the function $M(\alpha , \omega$ ) by considering various cases for $\alpha$ . In the end, we find that the minimum of $\rho (\mathcal{L}_{\omega})$ is obtained for $\omega_{0} (\rho (J))$. The details are tedious and we omit them. The reader will find complete proofs in Serre $[162]$ and Ciarlet $[41]$. Combining the results of Theorem 10.6 and Proposition 10.9, we obtain the following result which gives precise information about the spectral radii of the matrices $J, \mathcal{L}_{1}$, and $\mathcal{L}_{\omega}$.

> **Proposition 10.10.** Let $A$ be a tridiagonal matrix (possibly by blocks) which is Hermitian positive definite. Then the methods of Jacobi, Gauss–Seidel, and relaxation, all converge for $\omega  \in (0, 2)$. There is a unique optimal relaxation parameter
$$\omega_{0}  = \frac{2}{1 +p1 -(\rho (J))^{2}} ,$$
such that
$$\rho (\mathcal{L}_{\omega0}) =\inf \rho (\mathcal{L}_{\omega}) = \omega_{0}  -1.$$
$$0<\omega <2$$
Furthermore, if $\rho (J) > 0$, then
$$\rho (\mathcal{L}_{\omega0}) < \rho (\mathcal{L}_{1}) = (\rho (J))^{2}< \rho (J),$$
and if $\rho (J) = 0$, then $\omega_{0}  = 1$ and $\rho (\mathcal{L}_{1}) = \rho (J) = 0$.

*Proof.* In order to apply Proposition 10.9, we have to check that $J = D^{-1}(E + F)$ has real eigenvalues. However, if $\alpha$  is any eigenvalue of $J$ and if $u$ is any corresponding eigenvector, then
$$D^{-1}(E + F)u = \alpha u$$
implies that
$$(E + F)u = \alpha Du,$$
and since $A = D$ - $E$ - $F$, the above shows that $(D$ - A)u $= \alpha$ Du, that is,
$$Au = (1 -\alpha )Du.$$
Consequently,
$$u^{*}Au = (1 -\alpha )u^{*}Du,$$
and since $A$ and $D$ are Hermitian positive definite, we have $u^{*}Au > 0$ and $u^{*}Du > 0$ since u̸ $= 0$, which proves that $\alpha  \in \mathbb{R}$. The rest follows from Theorem 10.6 and Proposition 10.9.
Remark: It is preferable to overestimate rather than underestimate the relaxation parameter when the optimum relaxation parameter is not known exactly.
