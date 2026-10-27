# Applications of ADMM to 1-Norm Problems


<!-- PAGE 1934 -->
so we obtain
$$b = w^{\top}(u_{i0} + v_{j0})/2.$$
For improved numerical stability, we can average over the sets of indices defined as $I_{\lambda >0} = {i \in {1, \dots  , p}$ | $\lambda_{i}  > 0}$ and $I_{\mu >0} = {j \in {1, \dots  , q}$ | $\mu_{j}  > 0}$. We obtain
$$b = w^{\top} \begin{pmatrix}  \\ u_{i} \end{pmatrix} \begin{pmatrix}  \\ /|I_{\lambda >0}| + & v_{j} \end{pmatrix} \sum_{i\in I\lambda >0}  \begin{pmatrix} /|I_{\mu >0}| \end{pmatrix} \sum_{j\in I\mu >0}  /2.$$
The Matlab programs implementing the above method are given in Appendix $B$, Section B.1. This should convince the reader that there is very little gap between theory and practice, although it is quite consuming to tune the tolerance parameters needed to deal with floatingpoint arithmetric. Figure 52.5 shows the result of running the Matlab program implementing the above method using ADMM on two sets of points of $50$ points each generated at random using the following Matlab code. u14 $= 10.1*randn(2,50)+18$; v14 $=$ -10.1*randn(2,50)-18; The function SVMhard2 is called with $\rho  = 10$ as follows [lamb,mu,w] $=$ SVMhard2(10,u14,v14) and produces the output shown in Figure 52.5. Observe that there is one blue support vector and two red support vectors.

## 52.8 Applications of ADMM to \ell 1-Norm Problems

Another important application of ADMM is to $\ell^{1}$ -norm minimization problems, especially lasso minimization, discussed below and in Section 55.4. This involves the special case of ADMM where f(x) $= \tau  \|x\|_{1}$ and $A =$ I. In particular, in the one-dimensional case, we need to solve the minimization problem: find
$$x^{*}= arg minx \begin{pmatrix} \tau |x| + (\rho /2)(x -v)^{2} \end{pmatrix} ,$$
with $x, v \in \mathbb{R}$, and $\rho , \tau  > 0$. Let $c = \tau /\rho$  and write
$$f(x) = \frac{\tau}{2c} \begin{pmatrix} 2c|x| + (x -v)^{2} \end{pmatrix} .$$
Minimizing $f$ over $x$ is equivalent to minimizing
$$g(x) = 2c|x| + (x -v)^{2}= 2c|x| + x^{2}-2xv + v^{2},$$

<!-- PAGE 1935 -->
$$Figure 52.5: An example of hard margin SVM.$$
which is equivalent to minimizing
$$h(x) = x^{2}+ 2(c|x| -xv)$$
over $x$. If $x \ge 0$, then
$$h(x) = x^{2}+ 2(cx -xv) = x^{2}+ 2(c -v)x = (x -(v -c))^{2}-(v -c)^{2}.$$
If $v$ - $c > 0$, that is, $v > c$, since $x \ge 0$, the function $x \mapsto (x$ - $(v$ - $c))^{2}$ has a minimum for $x = v$ - $c > 0$, else if $v$ - $c \le 0$, then the function $x \mapsto (x$ - $(v$ - $c))^{2}$ has a minimum for $x = 0$. If $x \le 0$, then
$$h(x) = x^{2}+ 2(-cx -xv) = x^{2}-2(c + v)x = (x -(v + c))^{2}-(v + c)^{2}.$$
if $v + c < 0$, that is, $v < -c$, since $x \le 0$, the function $x \mapsto (x$ -(v $+ c))^{2}$ has a minimum for $x = v + c$, else if $v + c \ge 0$, then the function $x \mapsto (x$ - $(v + c))^{2}$ has a minimum for $x = 0$. In summary, $inf_{x}$ h(x) is the function of $v$ given by
$$v -cif v > c$$
$$$$
$$$$
$$S_{c}(v) =0if |v| \le c$$
$$v + cif v < -c.$$
$$$$
The function $S_{c}$ is known as a soft thresholding operator. The graph of $S_{c}$ shown in Figure 52.6.

<!-- PAGE 1936 -->
$$Figure 52.6: The graph of S_{c} (when c = 2).$$
One can check that
$$S_{c}(v) = (v -c)_{+} -(-v -c)_{+},$$
and also
$$S_{c}(v) = (1 -c/|v|)_{+}v,v \neq  0,$$
which shows that $S_{c}$ is a shrinkage operator (it moves a point toward zero).
$$\mathbb{R}^{n}$$
The operator $S_{c}$ is extended to vectors in component wise, that is, if $x = (x_{1}, \dots  , x_{n})$, then
$$S_{c}(x) = (S_{c}(x_{1}), \dots  , S_{c}(x_{n})).$$
We now consider several $\ell^{1}$ -norm problems.
$(1)$ Least absolute deviation. This is the problem of minimizing $\|Ax$ - $b\|_{1}$, rather than $\|Ax$ - $b\|_{2}$. Least absolute deviation is more robust than least squares fit because it deals better with outliers. The problem can be formulated in ADMM form as follows:
$$minimize\|z\|_{1}$$
$$subject to Ax -z = b,$$
with $f = 0$ and $g = \|\|_{1}$. As usual, we assume that $A$ is an $m \times  n$ matrix of rank $n$, so that $A^{\top}A$ is invertible. ADMM (in scaled form) can be expressed as
$$x^{k+1}= (A^{\top}A)^{-1}A^{\top}(b + z^{k}-u^{k})$$
$$z^{k+1}= S_{1/\rho}(Ax^{k+1}-b + u^{k})$$
$$u^{k+1}= u^{k}+ Ax^{k+1}-z^{k+1}-b.$$

<!-- PAGE 1937 -->
$(2)$ Basis pursuit. This is the following minimization problem:
$$minimize\|x\|_{1}$$
$$subject to Ax = b,$$
where $A$ is an $m \times  n$ matrix of rank $m < n$, and $b \in \mathbb{R}^{m}, x \in \mathbb{R}^{n}$. The problem is to find a sparse solution to an underdetermined linear system, which means a solution $x$ with many zero coordinates. This problem plays a central role in compressed sensing and statistical signal processing. Basis pursuit can be expressed in ADMM form as the problem
$$minimizeI_{C}(x) + \|z\|_{1}$$
$$subject to x -z = 0,$$
$$\mathbb{R}^{n}$$
with $C = {x \in$ | Ax $= b}$. It is easy to see that the ADMM procedure (in scaled form) is
$$x^{k+1}= \Pi_{C} (z^{k}-u^{k})$$
$$z^{k+1}= S_{1/\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1},$$
where $\Pi_{C}$  is the orthogonal projection onto the subspace $C$. In fact, it is not hard to show that
$$x^{k+1}= (I -A^{\top}(AA^{\top})^{-1}A)(z^{k}-u^{k}) + A^{\top}(AA^{\top})^{-1}b.$$
In some sense, an $\ell^{1}$ -minimization problem is reduced to a sequence of $\ell^{2}$ -norm problems. There are ways of improving the efficiency of the method; see Boyd et al. $[28]$ (Section 6.2)
$(3)$ General $\ell^{1}$ -regularized loss minimization. This is the following minimization problem:
$$minimizel(x) + \tau  \|x\|_{1} ,$$
where $l$ is any proper closed and convex loss function, and $\tau  > 0$. We convert the problem to the ADMM problem:
$$minimizel(x) + \tau  \|z\|_{1}$$
$$subject to x -z = 0.$$

<!-- PAGE 1938 -->
The ADMM procedure (in scaled form) is
$$x^{k+1}= arg minx \begin{pmatrix} l(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= S_{\tau /\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
The x-update is a proximal operator evaluation. In general, one needs to apply a numerical procedure to compute $x^{k+1}$, for example, a version of Newton’s method. The special case where l(x) $= (1/2) \|Ax$ - $b\|_{2}^{2}$ is particularly important.
$(4)$ Lasso regularization. This is the following minimization problem:
$$minimize(1/2) \|Ax -b\|_{2}^{2} + \tau  \|x\|_{1} .$$
This is a linear regression with the regularizing term $\tau  \|x\|_{1}$ instead of $\tau  \|x\|_{2}$, to encourage a sparse solution. This method was first proposed by Tibshirani around $1996$, under the name lasso, which stands for “least absolute selection and shrinkage operator.” This method is also known as $\ell^{1}$ -regularized regression, but this is not as cute as “lasso,” which is used predominantly. This method is discussed extensively in Hastie, Tibshirani, and Wainwright $[92]$. The lasso minimization is converted to the following problem in ADMM form:
$$minimize \frac{1}{2} \|Ax -b\|_{2}^{2} + \tau  \|z\|_{1}$$
$$subject to x -z = 0.$$
Then the ADMM procedure (in scaled form) is
$$x^{k+1}= (A^{\top}A + \rho I)^{-1}(A^{\top}b + \rho (z^{k}-u^{k}))$$
$$z^{k+1}= S_{\tau /\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
Since $\rho  > 0$, the matrix $A^{\top}A+\rho$ I is symmetric positive definite. Note that the x-update looks like a ridge regression step (see Section 55.1). There are various generalizations of lasso.
$(5)$ Generalized Lasso regularization. This is the following minimization problem:
$$minimize(1/2) \|Ax -b\|_{2}^{2} + \tau  \|Fx\|_{1} ,$$
