# Lasso Regression; Learning an Affine Function


<!-- PAGE 2092 -->

## 55.5 Lasso Regression; Learning an Affine Function

In the preceding section we made the simplifying assumption that we were trying to learn a linear function f(x) $= x^{\top}w$. To learn an affine function f(x) $= x^{\top}w + b$, we solve the following optimization problem Program (lasso3):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon$$
$$subject to$$
$$y -Xw -b1_{m} = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon .$$
Observe that as in the case of ridge regression, minimization is performed over $\xi , w, \epsilon$  and $b$, but $b$ is not penalized in the objective function. The Lagrangian associated with this optimization problem is
$$L(\xi , w, \epsilon , b, \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y -b1_{m}^{\top}\lambda$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$
so by setting the gradient $\nabla L_{\xi ,w,\epsilon ,b}$ to zero we obtain the equations
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$1_{m}^{\top}\lambda  = 0.$$
Using these equations, we find that the dual function is also given by
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix} ,$$
and the dual lasso program is given by
$$maximize- \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau$$
$$1_{m}^{\top}\lambda  = 0,$$
which is equivalent to

<!-- PAGE 2093 -->
Program (Dlasso3):
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau$$
$$1_{m}^{\top}\lambda  = 0,$$
minimizing over $\lambda  \in \mathbb{R}^{m}$. Once $\lambda  = \xi$  and $w$ are determined, we obtain $b$ using the equation
$$b1_{m} = y -Xw -\xi ,$$
and since $1_{m}^{\top}1_{m} = m$ and $1_{m}^{\top}\xi  = 1_{m}^{\top}\lambda  = 0$, the above yields
$$b = \frac{1}{m} 1_{m}^{\top}y - \frac{1}{m} 1_{m}^{\top}Xw - \frac{1}{m} 1_{m}^{\top}\xi  =\overline{y} - \sum_{j=1}^{n}  \overline{X}^{j}w_{j},$$
where $\overline{y}$ is the mean of $y$ and $\overline{X}^{j}$ is the mean of the jth column of $X$. The equation
$$b = bb +\overline{y} - \sum_{j=1}^{n}  \overline{X}^{j}w_{j} = bb +\overline{y} -(\overline{X}^{1} \cdots  \overline{X}^{n})w,$$
can be used as in ridge regression, (see Section 55.2), to show that the Program (lasso3) is equivalent to applying lasso regression (lasso2) without an intercept term to the centered data, by replacing $y$ by $y = y$ - $\overline{y} 1$ and $X$ by $X = X$ - $\overline{X}$. Then $b$ is given by
$$b b$$
$$- \cdots$$
$$b =\overline{y}(\overline{X}^{1} \overline{X}^{n})w,$$
$$b$$
where $w$ is the solution given by (lasso2). This is the method described by Hastie, Tibshirani, $b$ and Wainwright $[92]$ (Section 2.2).

> **Example 55.3.** We can create a data set $(X, y)$ where $X$ a $100\times 5$ matrix and $y$ is a $100\times 1$ vector using the following Matlab program in which the command randn creates an array of normally distributed numbers. $X =$ randn(100,5); ww $= [0; 2; 0; -3; 0]; y =$ X*ww $+$ randn(100,1)*0.1; The purpose of the third line is to add some small noise to the “output” $X$ * ww. The first five rows of $X$ are
$$\begin{pmatrix} -1.1658 & -0.0679 & -1.6118 & 0.3199 & 0.4400 \\ -1.1480 & -0.1952 & -0.0245 & -0.5583 & -0.6169 \\ 0.1049 & -0.2176 & -1.9488 & -0.3114 & 0.2748 \\ 0.7223 & -0.3031 & 1.0205 & -0.5700 & 0.6011 \\ 2.5855 & 0.0230 & 0.8617 & 1.0257 & 0.0923 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 2094 -->
and the first five rows of $y$ are
$$y = \begin{pmatrix} -1.0965 \\ 1.2155 \\ 0.4324 \\ 1.1902 \\ 3.1346 \end{pmatrix} .$$
We ran the program for lasso using ADMM (see Problem 52.7) with various values of $\rho$  and $\tau$ , including $\rho  = 1$ and $\rho  = 10$. We observed that the program converges a lot faster for $\rho  = 10$ than for $\rho  = 1$. We plotted the values of the five components of $w(\tau$ ) for values of $\tau$  from $\tau  = 0$ to $\tau  =$ 0.5 by increment of 0.02, and observed that the first, third, and fifth coordinate drop basically linearly to zero (a value less that $10^{-4})$ around $\tau  =$ 0.2. See Figures 55.7, 55.8, and 55.9. This behavior is also observed in Hastie, Tibshirani, and Wainwright $[92]$ (Section 2.2).
$$5 \overline{#}\overline{10}\overline{-3}$$
$$2.02$$
$$2$$
$$01.98$$
$$1.96$$
$$-51.94$$
$$1.92$$
$$-101.9$$
$$1.88$$
$$-151.86$$
$$1.84$$
$$-20$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5} 1.82$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.7: First and second component of w.$$
$$0.045-2.6$$
$$0.04$$
$$-2.65$$
$$0.035$$
$$-2.7$$
$$0.03$$
$$0.025-2.75$$
$$0.02-2.8$$
$$0.015-2.85$$
$$0.01$$
$$-2.9$$
$$0.005$$
$$-2.95$$
$$0$$
$$-0.005-3$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5} 0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.8: Third and fourth component of w.$$

<!-- PAGE 2095 -->
For $\tau  =$ 0.02, we have
$$w = \begin{pmatrix} 0.00003 \\ 2.01056 \\ -0.00004 \\ -2.99821 \\ 0.00000 \end{pmatrix} ,b = 0.00135.$$
$$\overline{#}\overline{10}\overline{-3}$$
$$2$$
$$0$$
$$-2$$
$$-4$$
$$-6$$
$$-8$$
$$-10$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.9: Fifth component of w.$$
This weight vector $w$ is very close to the original vector ww $= [0; 2; 0; -3; 0]$ that we used to create $y$. For large values of $\tau$ , the weight vector is essentially the zero vector. This happens for $\tau  = 235$, where every component of $w$ is less than $10^{-5}$. Another way to find $b$ is to add the term $(C/2)b^{2}$ to the objective function, for some positive constant $C$, obtaining the program Program(lasso4):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon  + \frac{1}{2} Cb^{2}$$
$$subject to$$
$$y -Xw -b1_{m} = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon ,$$
minimizing over $\xi , w, \epsilon$  and $b$. This time the Lagrangian is
$$-$$
$$L(\xi , w, \epsilon , b, \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y + \frac{C}{2} b^{2}b1_{m}^{\top}\lambda$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$

<!-- PAGE 2096 -->
so by setting the gradient $\nabla L_{\xi ,w,\epsilon ,b}$ to zero we obtain the equations
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$Cb = 1_{m}^{\top}\lambda .$$
Thus $b$ is also determined, and the dual lasso program is identical to the first lasso dual (Dlasso2), namely
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
minimizing over $\lambda$ . Since the equations $\xi  = \lambda$  and
$$y -Xw -b1_{m} = \xi$$
hold, from Cb $= 1_{m}^{\top}\lambda$  we get
$$1$$
$$\frac{1}{m} 1_{m}^{\top}y - \frac{1}{m} 1_{m}^{\top}Xw -b\overline{m} 1_{m}^{\top}1 = \frac{1}{m} 1_{m}^{\top}\lambda ,$$
that is
$$- \cdots  -$$
$$\overline{y}(\overline{X}^{1} \overline{X}^{n})wb = \frac{C}{m} b,$$
which yields
$$- \cdots$$
$$b = \frac{m}{m + C} (\overline{y}(\overline{X}^{1} \overline{X}^{n})w).$$
As in the case of ridge regression, a defect of the approach where $b$ is also penalized is that the solution for $b$ is not invariant under adding a constant $c$ to each value $y_{i}$ It is interesting to compare the behavior of the methods: $1$. Ridge regression (RR6') (which is equivalent to (RR3)). $2$. Ridge regression (RR3b), with $b$ penalized (by adding the term $Kb^{2}$ to the objective function). $3$. Least squares applied to $[X 1]. 4$. (lasso3).
