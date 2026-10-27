# Maximizing a Quadratic Function on the Unit Sphere


<!-- PAGE 1558 -->
where $P$ is an orthogonal $n\times n$ matrix and $R$ is an $m\times m$ invertible upper triangular matrix. If we write
$$x = P \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{m} \mathbb{R}^{n-m}$$
where $y \in$ and $z \in$ , the equation $C^{\top}x = t$ becomes
$$(R^{\top}0)P^{\top} x = t,$$
that is,
$$(R^{\top}0) \begin{pmatrix} y \\ z \end{pmatrix} = t,$$
which yields
$$R^{\top}y = t.$$
Since $R$ is invertible, we get $y = (R^{\top})^{-1}t$, and then it is easy to see that our original problem reduces to an unconstrained problem in terms of the matrix $P^{\top}$ AP; the details are left as an exercise.

## 42.3 Maximizing a Quadratic Function on the

$$Unit Sphere$$
In this section we discuss various quadratic optimization problems mostly arising from computer vision (image segmentation and contour grouping). These problems can be reduced to the following basic optimization problem: given an $n \times  n$ real symmetric matrix $A$
$$maximizex^{\top}Ax$$
$$subject tox^{\top}x = 1, x \in \mathbb{R}^{n}.$$
In view of Proposition 23.10, the maximum value of $x^{\top}Ax$ on the unit sphere is equal to the largest eigenvalue $\lambda_{1}$  of the matrix $A$, and it is achieved for any unit eigenvector $u_{1}$ associated with $\lambda_{1}$ . Similarly, the minimum value of $x^{\top}Ax$ on the unit sphere is equal to the smallest eigenvalue $\lambda_{n}$  of the matrix $A$, and it is achieved for any unit eigenvector $u_{n}$ associated with $\lambda_{n}$ . A variant of the above problem often encountered in computer vision consists in minimizing $x^{\top}Ax$ on the ellipsoid given by an equation of the form
$$x^{\top}Bx = 1,$$
where $B$ is a symmetric positive definite matrix. Since $B$ is positive definite, it can be diagonalized as
$$B = QDQ^{\top},$$

<!-- PAGE 1559 -->
where $Q$ is an orthogonal matrix and $D$ is a diagonal matrix,
$$D = \mathrm{diag}(d_{1}, \dots  , d_{n}),$$
with $d_{i} > 0$, for $i = 1, \dots  , n$. If we define the matrices $B^{1/2}$ and $B^{-1/2}$ by
$$B^{1/2}= Q \mathrm{diag} \begin{pmatrix} p\overline{d}_{1}, \dots  ,p\overline{d}_{n} \end{pmatrix} Q^{\top}$$
and
$$B^{-1/2}= Q \mathrm{diag} \begin{pmatrix} 1/p\overline{d}_{1}, \dots  , 1/p\overline{d}_{n} \end{pmatrix} Q^{\top},$$
it is clear that these matrices are symmetric, that $B^{-1/2}BB^{-1/2} =$ I, and that $B^{1/2}$ and $B^{-1/2}$ are mutual inverses. Then if we make the change of variable
$$x = B^{-1/2}y,$$
the equation $x^{\top}Bx = 1$ becomes $y^{\top}y = 1$, and the optimization problem
$$minimizex^{\top}Ax$$
$$subject tox^{\top}Bx = 1, x \in \mathbb{R}^{n},$$
is equivalent to the problem
$$minimizey^{\top}B^{-1/2}AB^{-1/2}y$$
$$subject toy^{\top}y = 1, y \in \mathbb{R}^{n},$$
where $y = B^{1/2}x$ and $B^{-1/2}AB^{-1/2}$ are symmetric. The complex version of our basic optimization problem in which $A$ is a Hermitian matrix also arises in computer vision. Namely, given an $n \times  n$ complex Hermitian matrix $A$,
$$maximizex^{*}Ax$$
$$subject tox^{*}x = 1, x \in \mathbb{C}^{n}.$$
Again by Proposition 23.10, the maximum value of $x^{*}Ax$ on the unit sphere is equal to the largest eigenvalue $\lambda_{1}$  of the matrix $A$, and it is achieved for any unit eigenvector $u_{1}$ associated with $\lambda_{1}$ .
Remark: It is worth pointing out that if $A$ is a skew-Hermitian matrix, that is, if $A^{*} = -A$, then $x^{*}Ax$ is pure imaginary or zero. Indeed, since $z = x^{*}Ax$ is a scalar, we have $z^{*} =\overline{z}$ (the conjugate of $z)$, so we have
$$\overline{x}^{*}\overline{Ax} = (x^{*}Ax)^{*}= x^{*}A^{*}x = -x^{*}Ax,$$
so $\overline{x}^{*}\overline{Ax} + x^{*}Ax = 2Re(x^{*}Ax) = 0$, which means that $x^{*}Ax$ is pure imaginary or zero.

<!-- PAGE 1560 -->
In particular, if $A$ is a real matrix and if $A$ is skew-symmetric, then
$$x^{\top}Ax = 0.$$
Thus, for any real matrix (symmetric or not),
$$x^{\top}Ax = x^{\top}H(A)x,$$
where H(A) $= (A + A^{\top})/2$, the symmetric part of $A$. There are situations in which it is necessary to add linear constraints to the problem of maximizing a quadratic function on the sphere. This problem was completely solved by Golub $[81] (1973)$. The problem is the following: given an $n \times  n$ real symmetric matrix $A$ and an $n \times  p$ matrix $C$,
$$minimizex^{\top}Ax$$
$$subject tox^{\top}x = 1, C^{\top}x = 0, x \in \mathbb{R}^{n}.$$
As in Section 42.2, Golub shows that the linear constraint $C^{\top}x = 0$ can be eliminated as follows: if we use a QR decomposition of $C$, by permuting the columns, we may assume that
$$C = Q^{\top} \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix} \Pi ,$$
where $Q$ is an orthogonal $n\times n$ matrix, $R$ is an $r \times r$ invertible upper triangular matrix, and $S$ is an $r \times  (p$ - $r)$ matrix (assuming $C$ has rank $r)$. If we let
$$x = Q^{\top} \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
where $y \in$ and $z \in$ , then $C^{\top}x = 0$ becomes
$$\Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} Qx = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} = 0,$$
which implies $y = 0$, and every solution of $C^{\top}x = 0$ is of the form
$$x = Q^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} .$$
Our original problem becomes
$$minimize(y^{\top}z^{\top})QAQ^{\top} \begin{pmatrix} y \\ z \end{pmatrix}$$
$$subject toz^{\top}z = 1, z \in \mathbb{R}^{n-r},$$
$$y = 0, y \in \mathbb{R}^{r}.$$

<!-- PAGE 1561 -->
Thus the constraint $C^{\top}x = 0$ has been simplified to $y = 0$, and if we write
$$QAQ^{\top}= \begin{pmatrix} G_{11} & G_{12} \\ G_{12}^{\top} & G_{22} \end{pmatrix} ,$$
our problem becomes
$$minimizez^{\top}G_{22}z$$
$$subject toz^{\top}z = 1, z \in \mathbb{R}^{n-r},$$
a standard eigenvalue problem.
Remark: There is a way of finding the eigenvalues of $G_{22}$ which does not require the QRfactorization of $C$. Observe that if we let
$$J = \begin{pmatrix} 0 & 0 \\ 0 & I_{n-r} \end{pmatrix} ,$$
then
$$JQAQ^{\top}J = \begin{pmatrix} 0 & 0 \\ 0 & G_{22} \end{pmatrix} ,$$
and if we set
$$P = Q^{\top}JQ,$$
then
$$PAP = Q^{\top}JQAQ^{\top}JQ.$$
Now, $Q^{\top}JQAQ^{\top}JQ$ and $JQAQ^{\top}J$ have the same eigenvalues, so PAP and $JQAQ^{\top}J$ also have the same eigenvalues. It follows that the solutions of our optimization problem are among the eigenvalues of $K = PAP$, and at least $r$ of those are $0$. Using the fact that $CC^{+}$ is the projection onto the range of $C$, where $C^{+}$ is the pseudo-inverse of $C$, it can also be shown that
$$P = I -CC^{+},$$
the projection onto the kernel of $C^{\top}$. So $P$ can be computed directly in terms of $C$. In particular, when $n \ge p$ and $C$ has full rank (the columns of $C$ are linearly independent), then we know that $C^{+} = (C^{\top}C)^{-1}C^{\top}$ and
$$P = I -C(C^{\top}C)^{-1}C^{\top}.$$
This fact is used by Cour and Shi $[42]$ and implicitly by Yu and Shi $[198]$. The problem of adding affine constraints of the form $N^{\top} x = t$, where $t \neq  0$, also comes up in practice. At first glance, this problem may not seem harder than the linear problem in which $t = 0$, but it is. This problem was extensively studied in a paper by Gander, Golub, and von Matt $[78] (1989)$.

<!-- PAGE 1562 -->
Gander, Golub, and von Matt consider the following problem: Given an $(n+m)\times (n+m)$ real symmetric matrix $A$ (with $n > 0)$, an $(n+m)\times m$ matrix $N$ with full rank, and a nonzero
$$\mathbb{R}^{m}



$<$$$ vector $t \in$ with $(N^{\top})^{+}t  1$ (where $(N^{\top})^{+}$ denotes the pseudo-inverse of $N^{\top})$,
$$minimizex^{\top}Ax$$
$$subject tox^{\top}x = 1, N^{\top} x = t, x \in \mathbb{R}^{n+m}.$$
The condition

$(N^{\top})^{+}t$

$< 1$ ensures that the problem has a solution and is not trivial. The authors begin by proving that the affine constraint $N^{\top} x = t$ can be eliminated. One way to do so is to use a QR decomposition of $N$. If
$$N = P \begin{pmatrix} R \\ 0 \end{pmatrix} ,$$
where $P$ is an orthogonal $(n + m) \times  (n + m)$ matrix and $R$ is an $m \times  m$ invertible upper triangular matrix, then if we observe that
$$x^{\top}Ax = x^{\top}PP^{\top} APP^{\top} x,$$
$$N^{\top} x = (R^{\top}0)P^{\top} x = t,$$
$$x^{\top}x = x^{\top}PP^{\top} x = 1,$$
and if we write
$$P^{\top} AP = \begin{pmatrix} B & \Gamma^{\top} \\ \Gamma & C \end{pmatrix} ,$$
where $B$ is an $m \times  m$ symmetric matrix, $C$ is an $n \times  n$ symmetric matrix, $\Gamma$  is an $m \times  n$ matrix, and
$$P^{\top} x = \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
with $y \in$ and $z \in$ , we then get
$$x^{\top}Ax = y^{\top}By + 2z^{\top}\Gamma y + z^{\top}Cz,$$
$$R^{\top}y = t,$$
$$y^{\top}y + z^{\top}z = 1.$$
Thus
$$y = (R^{\top})^{-1}t,$$
and if we write
$$s^{2}= 1 -y^{\top}y > 0$$
and
$$b = \Gamma y,$$
