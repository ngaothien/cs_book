# Lasso Regression (1-Regularized Regression)


<!-- PAGE 2088 -->

## 55.4 Lasso Regression (\ell 1-Regularized Regression)

The main weakness of ridge regression is that the estimated weight vector $w$ usually has many nonzero coefficients. As a consequence, ridge regression does not scale up well. In practice we need methods capable of handling millions of parameters, or more. A way to encourage sparsity of the vector $w$, which means that many coordinates of $w$ are zero, is to replace the quadratic penalty function $\tau w^{\top}w = \tau  \|w\|_{2}^{2}$ by the penalty function $\tau  \|w\|_{1}$, with the $\ell^{2}$ -norm replaced by the $\ell^{1}$ -norm. This method was first proposed by Tibshirani around $1996$, under the name lasso, which stands for “least absolute selection and shrinkage operator.” This method is also known as $\ell^{1}$ -regularized regression, but this is not as cute as “lasso,” which is used predominantly.
$$\mathbb{R}^{n} \mathbb{R}$$
Given a set of training data ${(x_{1}, y_{1}), \dots  , (x_{m}, y_{m})}$, with $x_{i} \in$ and $y_{i} \in$ , if $X$ is the $m \times  n$ matrix
$$X = \begin{pmatrix} x_{1}^{\top} \\ \vdots \\ x_{m}^{\top} \end{pmatrix} ,$$
in which the row vectors $x_{i}^{\top}$ are the rows of $X$, then lasso regression is the following optimization problem Program (lasso1):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau  \|w\|_{1}$$
$$subject to$$
$$y -Xw = \xi ,$$
minimizing over $\xi$  and $w$, where $\tau  > 0$ is some constant determining the influence of the regularizing term $\|w\|_{1}$. The objective function expressed in terms of $w$ is
$$J(w) = \frac{1}{2} (Xw -y)^{\top}(Xw -y) + \tau  \|w\|_{1}$$
$$= \frac{1}{2} w^{\top}X^{\top}Xw -w^{\top}X^{\top}y + \frac{1}{2} y^{\top}y + \tau  \|w\|_{1} .$$
This function is convex, but not necessarily strictly convex. Since it is nonnegative, it has a minimum, but in general it is not achieved by a unique $w$. The difficulty with the regularizing term $\|w\|_{1} = |w_{1}| + \cdots  + |w_{n}|$ is that the map $w \mapsto \|w\|_{1}$ is not differentiable for all $w$. This difficulty can be overcome by using subgradients, but the dual of the above program can also be obtained in an elementary fashion by using a trick that we already used, which is that if $x \in \mathbb{R}$, then
$$|x| = \max{x, -x}.$$

<!-- PAGE 2089 -->
$$\mathbb{R}^{n}$$
Using this trick, by introducing a vector $\epsilon  \in$ of nonnegative variables, we can rewrite lasso minimization as follows: Program lasso regularization (lasso2):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon$$
$$subject to$$
$$y -Xw = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon .$$
minimizing over $\xi , w$ and $\epsilon$ , with $y, \xi  \in \mathbb{R}^{m}$, and $w, \epsilon , 1_{n} \in \mathbb{R}^{n}$. The constraints $w \le \epsilon$  and $-w \le \epsilon$  are equivalent to $|w_{i}| \le \epsilon_{i}$  for $i = 1, \dots  , n$, so for an optimal solution we must have $\epsilon  \ge 0$ and $|w_{i}| = \epsilon_{i}$ , that is, $\|w\|_{1} = \epsilon_{1}  + \cdots  + \epsilon_{n}$ . The Lagrangian $L(\xi , w, \epsilon , \lambda , \alpha_{+} , \alpha_{-}$ ) is given by
$$L(\xi , w, \epsilon , \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon  + \lambda^{\top} (y -Xw -\xi )$$
$$+ \alpha_{+}^{\top} (w -\epsilon ) + \alpha_{-}^{\top} (-w -\epsilon )$$
$$= \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$
$$\mathbb{R}^{m} \mathbb{R}_{+}^{n}$$
with $\lambda  \in$ and $\alpha_{+} , \alpha_{-} \in$ . Since the objective function is convex and the constraints are affine (and thus qualified), the Lagrangian $L$ has a minimum with respect to the primal variables, $\xi , w, \epsilon$  iff $\nabla L_{\xi ,w,\epsilon} = 0$. Since the gradient $\nabla L_{\xi ,w,\epsilon}$ is given by
$$\nabla L_{\xi ,w,\epsilon} = \begin{pmatrix} \xi  -\lambda \\ \alpha_{+}  -\alpha_{-} -X^{\top}\lambda \\ \tau 1_{n} & \alpha_{+} & \alpha_{-} \end{pmatrix} ,$$
$$- -$$
we obtain the equations
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}.$$
Using these equations, the dual function $G(\lambda , \alpha_{+} , \alpha_{-}$ ) $= min_{\xi ,w,\epsilon} L$ is given by
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y = \frac{1}{2} \lambda^{\top} \lambda  -\lambda^{\top} \lambda  + \lambda^{\top} y$$
$$= - \frac{1}{2} \lambda^{\top} \lambda  + \lambda^{\top} y = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix} ,$$

<!-- PAGE 2090 -->
so
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \\ minimumof( \end{pmatrix} .$$
Since $\alpha_{+} , \alpha_{-} \ge 0$, for any $i \in {1, \dots  , n}$ the   $\alpha_{+} )_{i}$ - $(\alpha_{-} )_{i}$ is $-\tau$  , and the maximum is $\tau$ . If we recall that for any $z \in \mathbb{R}^{n}$,
$$\|z\|_{\infty}= \max |z_{i}|,$$
$$1\le i\le n$$
it follows that the constraints
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$X^{\top}\lambda  = \alpha_{+}  -\alpha_{-}$$
are equivalent to
$$X^{\top}\lambda_{\infty} \le \tau .$$
The above is equivalent to the 2n constraints
$$-\tau  \le (X^{\top}\lambda )_{i} \le \tau ,1 \le i \le n.$$
Therefore, the dual lasso program is given by
$$maximize- \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
which (since $\|y\|_{2}^{2}$ is a constant term) is equivalent to Program (Dlasso2):
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
minimizing over $\lambda  \in \mathbb{R}^{m}$. One way to solve lasso regression is to use the dual program to find $\lambda  = \xi$ , and then to use linear programming to find $w$ by solving the linear program arising from the lasso primal by holding $\xi$  constant. The best way is to use ADMM as explained in Section 52.8(4). There are also a number of variations of gradient descent; see Hastie, Tibshirani, and Wainwright $[92]$. In theory, if we know the support of $w$ and the signs of its components, then $w$ is determined as we now explain.

<!-- PAGE 2091 -->
In view of the constraint $y$ - Xw $= \xi$  and the fact that for an optimal solution we must have $\xi  = \lambda$ , the following condition must hold:
$$X^{\top}(Xw -y)_{\infty}\le \tau .(*)$$
Also observe that for an optimal solution, we have
$$-$$
$$\frac{1}{2} \|y -Xw\|_{2}^{2} + w^{\top}X^{\top}(y -Xw) = \frac{1}{2} \|y\|^{2}w^{\top}X^{\top}y + \frac{1}{2} w^{\top}X^{\top}Xw + w^{\top}X^{\top}y -w^{\top}X^{\top}Xw$$
$$= \frac{1}{2} \begin{pmatrix} \|y\|_{2}^{2}-\|Xw\|_{2}^{2} \end{pmatrix}$$
$$= \frac{1}{2} \begin{pmatrix} \|y\|_{2}^{2}-\|y -\lambda \|_{2}^{2} \end{pmatrix} = G(\lambda ).$$
Since the objective function is convex and the constaints are qualified, by Theorem 50.19(2) the duality gap is zero, so for optimal solutions of the primal and the dual, $G(\lambda$ ) $= L(\xi , w, \epsilon$ ), that is
$$\frac{1}{2} \|y -Xw\|_{2}^{2} + w^{\top}X^{\top}(y -Xw) = \frac{1}{2} \|\xi \|_{2}^{2} + \tau  \|w\|_{1} = \frac{1}{2} \|y -Xw\|_{2}^{2} + \tau  \|w\|_{1} ,$$
which yields the equation
$$w^{\top}X^{\top}(y -Xw) = \tau  \|w\|_{1} .(**_{1})$$
The above is the inner product of $w$ and $X^{\top}(y$ - Xw), so whenever $w_{i}$ ̸ $= 0$, since $\|w\|_{1} = |w_{1}| + \cdots  + |w_{n}|$, in view of (*), we must have $(X^{\top}(y$ - $Xw))_{i} = \tau sgn(w_{i})$. If
$$S = {i \in {1, \dots  , n} | w_{i} \neq  0},(\dagger )$$
if $X_{S}$ denotes the matrix consisting of the columns of $X$ indexed by $S$, and if $w_{S}$ denotes the vector consisting of the nonzero components of $w$, then we have
$$X_{S}^{\top} (y -X_{S}w_{S}) = \tau sgn(w_{S}).(**_{2})$$
We also have
$$X_{S}^{\top} (y -X_{S}w_{S})_{\infty}\le \tau ,(**_{3})$$
where $\overline{S}$ is the complement of $S$. Equation $(**_{2})$ yields
$$X_{S}^{\top} X_{S}w_{S} = X_{S}^{\top} y -\tau sgn(w_{S}),$$
so if $X_{S}^{\top} X_{S}$ is invertible (which will be the case if the columns of $X$ are linearly independent), we get
$$w_{S} = (X_{S}^{\top} X_{S})^{-1}(X_{S}^{\top} y -\tau sgn(w_{S})).(**_{4})$$
In theory, if we know the support of $w$ and the signs of its components, then $w_{S}$ is determined, but in practice this is useless since the problem is to find the support and the sign of the solution.
