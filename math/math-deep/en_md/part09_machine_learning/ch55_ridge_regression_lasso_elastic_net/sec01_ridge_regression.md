# Ridge Regression


<!-- PAGE 2072 -->
it. One of the best methods relies on ADMM (see Section 52.8) and is discussed in Section 55.4. The lasso method has some limitations, in particular when the number $m$ of data is smaller than the dimension $n$ of the data. This happens in some applications in genetics and medicine. Fortunately there is a way to combine the best features of ridge regression and lasso, which is to use two regularizing terms: $1$. An $\ell^{2}$ -term $(1/2)K \|w\|_{2}^{2}$ as in ridge regression (with $K > 0). 2$. An $\ell^{1}$ -term $\tau  \|w\|_{1}$ as in lasso. This method is known as elastic net regression and is discussed in Section 55.6. It retains most of the desirable features of ridge regression and lasso, and eliminates some of their weaknesses. Furthermore, it is effectively solved by ADMM.

## 55.1 Ridge Regression

The problem of solving an overdetermined or underdetermined linear system Aw $= y$, where $A$ is an $m \times  n$ matrix, arises as a “learning problem” in which we observe a sequence of data $((a_{1}, y_{1}), \dots  , (a_{m}, y_{m}))$, viewed as input-output pairs of some unknown function $f$ that we are trying to infer, where the $a_{i}$ are the rows of the matrix $A$ and $y_{i} \in \mathbb{R}$. The values $y_{i}$ are sometimes called labels or responses. The simplest kind of function is a linear function
$$\mathbb{R}^{n}$$
f(x) $= x^{\top}w$, where $w \in$ is a vector of coefficients usually called a weight vector, or sometimes an estimator. In the statistical literature $w$ is often denoted by $\beta$ . Since the problem is overdetermined and since our observations may be subject to errors, we can’t solve for $w$ exactly as the solution of the system Aw $= y$, so instead we solve the least-square problem of minimizing $\|Aw$ - $y\|_{2}^{2}$. In Section 23.1 we showed that this problem can be solved using the pseudo-inverse. We know that the minimizers $w$ are solutions of the normal equations $A^{\top}Aw = A^{\top}y$, but when $A^{\top}A$ is not invertible, such a solution is not unique so some criterion has to be used to choose among these solutions. One solution is to pick the unique vector $w^{+}$ of smallest Euclidean norm $\|w^{+}\|_{2}$ that minimizes $\|Aw$ - $y\|_{2}^{2}$. The solution $w^{+}$ is given by $w^{+} = A^{+}y$, where $A^{+}$ is the pseudoinverse of $A$. The matrix $A^{+}$ is obtained from an SVD of $A$, say $A = V \Sigma U^{\top}$. Namely, $A^{+} = U\Sigma^{+} V^{\top}$, where $\Sigma^{+}$ is the matrix obtained from $\Sigma$  by replacing every nonzero singular value $\sigma_{i}$  in $\Sigma$  by $\sigma_{i}^{-1}$  , leaving all zeros in place, and then transposing. The difficulty with this approach is that it requires knowing whether a singular value is zero or very small but nonzero. A very small nonzero singular value $\sigma$  in $\Sigma$  yields a very large value $\sigma^{-1}$ in $\Sigma^{+}$ , but $\sigma  = 0$ remains $0$ in $\Sigma^{+}$ . This discontinuity phenomenon is not desirable and another way is to control the size of $w$ by adding a regularization term to $\|Aw$ - $y\|^{2}$, and a natural candidate is $\|w\|^{2}$.

<!-- PAGE 2073 -->
It is customary to rename each column vector $a_{i}^{\top}$ as $x_{i}$ (where $x_{i} \in \mathbb{R}^{n})$ and to rename the input data matrix $A$ as $X$, so that the row vector $x_{i}^{\top}$ are the rows of the $m \times  n$ matrix $X$
$$X = \begin{pmatrix} x_{1}^{\top} \\ \vdots \\ x_{m}^{\top} \end{pmatrix} .$$
Our optimization problem, called ridge regression, is Program (RR1):
$$minimize\|y -Xw\|^{2}+ K \|w\|^{2},$$
which by introducing the new variable $\xi  = y$ - Xw can be rewritten as Program (RR2):
$$minimize\xi^{\top} \xi  + Kw^{\top}w$$
$$subject to$$
$$y -Xw = \xi ,$$
where $K > 0$ is some constant determining the influence of the regularizing term $w^{\top}w$, and we minimize over $\xi$  and $w$. The objective function of the first version of our minimization problem can be expressed as
$$J(w) = \|y -Xw\|^{2}+ K \|w\|^{2}$$
$$= (y -Xw)^{\top}(y -Xw) + Kw^{\top}w$$
$$= y^{\top}y -2w^{\top}X^{\top}y + w^{\top}X^{\top}Xw + Kw^{\top}w$$
$$= w^{\top}(X^{\top}X + KI_{n})w -2w^{\top}X^{\top}y + y^{\top}y.$$
The matrix $X^{\top}X$ is symmetric positive semidefinite and $K > 0$, so the matrix $X^{\top}X+KI_{n}$ is positive definite. It follows that
$$J(w) = w^{\top}(X^{\top}X + KI_{n})w -2w^{\top}X^{\top}y + y^{\top}y$$
is strictly convex, so by Theorem 40.13(2)-(4), it has a unique minimum iff $\nabla J_{w} = 0$. Since
$$\nabla J_{w} = 2(X^{\top}X + KI_{n})w -2X^{\top}y,$$
we deduce that
$$w = (X^{\top}X + KI_{n})^{-1}X^{\top}y.(*_{wp})$$
There is an interesting connection between the matrix $(X^{\top}X+KI_{n})^{-1}X^{\top}$ and the pseudoinverse $X^{+}$ of $X$.

<!-- PAGE 2074 -->

> **Proposition 55.1.** The limit of the matrix $(X^{\top}X + KI_{n})^{-1}X^{\top}$ when $K > 0$ goes to zero is the pseudo-inverse $X^{+}$ of $X$.

*Proof.* To show this let $X = V \Sigma U^{\top}$ be a SVD of $X$. Then
$$(X^{\top}X + KI_{n}) = U\Sigma^{\top} V^{\top} V \Sigma U^{\top} + KI_{n} = U(\Sigma^{\top} \Sigma  + KI_{n})U^{\top} ,$$
so $(X^{\top}X + KI_{n})^{-1}X^{\top} = U(\Sigma^{\top} \Sigma  + KI_{n})^{-1}U^{\top} U\Sigma^{\top} V^{\top} = U(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top} V^{\top}$ . The diagonal entries in the matrix $(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top}$ are
$$\frac{\sigma_{i}}{\sigma_{i}^{2} +} K ,if \sigma_{i}  > 0,$$
and zero if $\sigma_{i}  = 0$. All nondiagonal entries are zero. When $\sigma_{i}  > 0$ and $K > 0$ goes to $0$,
$$Klim\mapsto 0 \frac{\sigma_{i}}{\sigma_{i}^{2} + K} = \sigma_{i}^{-1}  ,$$
so
$$lim(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top} = \Sigma^{+} ,$$
$$K\mapsto 0$$
which implies that
$$lim(X^{\top}X + KI_{n})^{-1}X^{\top}= X^{+}.$$
$$K\mapsto 0$$
The dual function of the first formulation of our problem is a constant function (with value the minimum of $J)$ so it is not useful, but the second formulation of our problem yields an interesting dual problem. The Lagrangian is
$$L(\xi , w, \lambda ) = \xi^{\top} \xi  + Kw^{\top}w + (y -Xw -\xi )^{\top}\lambda$$
$$= \xi^{\top} \xi  + Kw^{\top}w -w^{\top}X^{\top}\lambda  -\xi^{\top} \lambda  + \lambda^{\top} y,$$
with $\lambda , \xi , y \in \mathbb{R}^{m}$. The Lagrangian $L(\xi , w, \lambda$ ), as a function of $\xi$  and $w$ with $\lambda$  held fixed, is obviously convex, in fact strictly convex. To derive the dual function $G(\lambda$ ) we minimize $L(\xi , w, \lambda$ ) with respect to $\xi$  and $w$. Since $L(\xi , w, \lambda$ ) is (strictly) convex as a function of $\xi$  and $w$, by Theorem 40.13(4), it has a minimum iff its gradient $\nabla L_{\xi ,w}$ is zero (in fact, by Theorem 40.13(2), a unique minimum since the function is strictly convex). Since
$$\nabla L_{\xi ,w} = \begin{pmatrix} 2\xi  -\lambda \\ 2Kw -X^{\top}\lambda \end{pmatrix} ,$$
we get
$$\lambda  = 2\xi$$
$$\xi$$
$$w = \frac{1}{2} K X^{\top}\lambda  = X^{\top}K .$$
