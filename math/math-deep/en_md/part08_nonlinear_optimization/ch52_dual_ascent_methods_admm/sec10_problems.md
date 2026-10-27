# Problems


<!-- PAGE 1940 -->
$\bullet$  x-update, z-update, $\lambda$ -update. $\bullet$  Scaled form of ADMM. $\bullet$  Residual, dual residual. $\bullet$  Stopping criteria. $\bullet$  Proximity operator, proximal minimization. $\bullet$  Quadratic programming. $\bullet$  KKT equations. $\bullet$  Soft thresholding operator. $\bullet$  Shrinkage operator. $\bullet$  Least absolute deviation. $\bullet$  Basis pursuit. $\bullet$  General $\ell^{1}$ -regularized loss minimization. $\bullet$  Lasso regularization. $\bullet$  Generalized lasso regularization. $\bullet$  Group lasso.

## 52.10 Problems

Problem 52.1. In the method of multipliers described in Section 52.2, prove that choosing $\alpha^{k} = \rho$  guarantees that $(u^{k+1}, \lambda^{k+1}$ ) satisfies the equation
$$\nabla J_{uk+1} + A^{\top}\lambda^{k+1} = 0.$$
Problem 52.2. Prove that the Inequality (A1) follows from the Inequalities (A2) and (A3) (see the proof of Theorem 52.1). For help consult Appendix $A$ of Boyd et al. $[28]$.
Problem 52.3. Consider Example 52.8. Prove that if $f = I_{C}$, the indicator function of a nonempty closed convex set $C$, then
$$x^{+}= arg minx \begin{pmatrix} I_{C}(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = \Pi_{C} (v),$$
the orthogonal projection of $v$ onto $C$. In the special case where $C =\mathbb{R}_{+}^{n}$ (the first orthant), then
$$x^{+}= (v)_{+},$$
the vector obtained by setting the negative components of $v$ to zero.

<!-- PAGE 1941 -->
Problem 52.4. Prove that the soft thresholding operator $S_{c}$ from Section 52.8 satisfies the equations
$$S_{c}(v) = (v -c)_{+} -(-v -c)_{+},$$
and
$$S_{c}(v) = (1 -c/|v|)_{+}v,v \neq  0.$$
Problem 52.5. Rederive the formula
$$v -cif v > c$$
$$$$
$$$$
$$S_{c}(v) =0if |v| \le c$$
$$v + cif v < -c$$
$$$$
using subgradients.
Problem 52.6. In basis pursuit (see Section 52.8 $(2))$ prove that
$$x^{k+1}= (I -A^{\top}(AA^{\top})^{-1}A)(z^{k}-u^{k}) + A^{\top}(AA^{\top})^{-1}b.$$
Problem 52.7. Implement (in Matlab) ADMM applied to lasso regularization as described in Section 52.6 $(4)$. The stopping criterion should be based on feasibility tolerances $\epsilon^{pri}$ and $\epsilon^{dual}$ , say $10^{-4}$, and on a maximum number of iteration steps, say $10000$. There is a build in Matlab function wthresh implementing soft thresholding. You may use the Matlab command randn to create a random data set $X$ and a random response vector $y$ (see the help menu in Matlab under lasso). Try various values of $\rho$  and $\tau$ . You will observe that the choice of $\rho$  greatly affects the rate of convergence of the procedure.

<!-- PAGE 1942 -->
