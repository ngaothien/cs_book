# Least Squares Problems and the Pseudo-Inverse


<!-- PAGE 769 -->
Chapter $23$ Applications of SVD and Pseudo-Inverses De tous les principes qu’on peut proposer pour cet objet, je pense qu’il n’en est pas de plus g´en´eral, de plus exact, ni d’une application plus facile, que celui dont nous avons fait usage dans les recherches pr´ec´edentes, et qui consiste `a rendre minimum la somme des carr´es des erreurs. Par ce moyen il s’´etablit entre les erreurs une sorte d’´equilibre qui, empˆechant les extrˆemes de pr´evaloir, est tr`es propre `as faire connaitre l’´etat du syst`eme le plus proche de la v´erit´e. —Legendre, $1805$, Nouvelles M´ethodes pour la d´etermination des Orbites des Com`etes

## 23.1 Least Squares Problems and the Pseudo-Inverse

This chapter presents several applications of SVD. The first one is the pseudo-inverse, which plays a crucial role in solving linear systems by the method of least squares. The second application is data compression. The third application is principal component analysis (PCA), whose purpose is to identify patterns in data and understand the variance–covariance structure of the data. The fourth application is the best affine approximation of a set of data, a problem closely related to PCA. The method of least squares is a way of “solving” an overdetermined system of linear equations
$$Ax = b,$$
i.e., a system in which $A$ is a rectangular $m \times  n$ matrix with more equations than unknowns (when $m > n)$. Historically, the method of least squares was used by Gauss and Legendre to solve problems in astronomy and geodesy. The method was first published by Legendre in $1805$ in a paper on methods for determining the orbits of comets. However, Gauss had already used the method of least squares as early as $1801$ to determine the orbit of the asteroid
$$769$$

<!-- PAGE 770 -->
Ceres, and he published a paper about it in $1810$ after the discovery of the asteroid Pallas. Incidentally, it is in that same paper that Gaussian elimination using pivots is introduced. The reason why more equations than unknowns arise in such problems is that repeated measurements are taken to minimize errors. This produces an overdetermined and often inconsistent system of linear equations. For example, Gauss solved a system of eleven equations in six unknowns to determine the orbit of the asteroid Pallas.

> **Example 23.1.** As a concrete illustration, suppose that we observe the motion of a small object, assimilated to a point, in the plane. From our observations, we suspect that this point moves along a straight line, say of equation $y =$ cx $+ d$. Suppose that we observed the moving point at three different locations $(x_{1}, y_{1}), (x_{2}, y_{2})$, and $(x_{3}, y_{3})$. Then we should have
$$d + cx_{1} = y_{1},$$
$$d + cx_{2} = y_{2},$$
$$d + cx_{3} = y_{3}.$$
If there were no errors in our measurements, these equations would be compatible, and $c$ and $d$ would be determined by only two of the equations. However, in the presence of errors, the system may be inconsistent. Yet we would like to find $c$ and $d$! The idea of the method of least squares is to determine $(c, d)$ such that it minimizes the sum of the squares of the errors, namely,
$$(d + cx_{1} -y_{1})^{2}+ (d + cx_{2} -y_{2})^{2}+ (d + cx_{3} -y_{3})^{2}.$$
See Figure 23.1.
$$+ d$$
$$cx$$
$$=$$
$$y$$
$$(x , y )(x , y )$$
$$3333$$
$$(x , cx +d )$$
$$(x , cx +d )33$$
$$22$$
$$(x , y )(x , y )$$
$$2222$$
$$(x , y )(x , y )$$
$$1111$$
$$\overline{(x , cx +d )}$$
$$11$$

![Figure 23.1](../../assets/ch23/fig_23_1.png)

**Figure 23.1:** Given three points $(x_{1}, y_{1}), (x_{2}, y_{2}), (x_{3}, y_{3})$, we want to determine the line $y =$ cx $+ d$ which minimizes the lengths of the dashed vertical lines.

<!-- PAGE 771 -->
In general, for an overdetermined $m \times  n$ system Ax $= b$, what Gauss and Legendre discovered is that there are solutions $x$ minimizing
$$\|Ax -b\|_{2}^{2}$$
(where $\|u\|_{2}^{2} = u_{1}^{2}+\cdots +u_{n}^{2}$, the square of the Euclidean norm of the vector $u = (u_{1}, \dots  , u_{n}))$, and that these solutions are given by the square $n \times  n$ system
$$A^{\top}Ax = A^{\top}b,$$
called the normal equations. Furthermore, when the columns of $A$ are linearly independent, it turns out that $A^{\top}A$ is invertible, and so $x$ is unique and given by
$$x = (A^{\top}A)^{-1}A^{\top}b.$$
Note that $A^{\top}A$ is a symmetric matrix, one of the nice features of the normal equations of a least squares problem. For instance, since the above problem in matrix form is represented as
$$\begin{pmatrix} 1 & x_{1} \\ 1 & x_{2} \\ 1 & x_{3} \end{pmatrix} \begin{pmatrix} d \\ c \end{pmatrix} = \begin{pmatrix} y_{1} \\ y_{2} \\ y_{3} \end{pmatrix} ,$$
the normal equations are
$$\begin{pmatrix} 3 & x_{1} + x_{2} + x_{3} \\ x_{1} + x_{2} + x_{3} & x_{1}^{2}+ x_{2}^{2}+ x_{3}^{2} \end{pmatrix} \begin{pmatrix} d \\ c \end{pmatrix} = \begin{pmatrix} y_{1} + y_{2} + y_{3} \\ x_{1}y_{1} + x_{2}y_{2} + x_{3}y_{3} \end{pmatrix} .$$
In fact, given any real $m \times  n$ matrix $A$, there is always a unique $x^{+}$ of minimum norm that minimizes $\|Ax$ - $b\|_{2}^{2}$, even when the columns of $A$ are linearly dependent. How do we prove this, and how do we find $x^{+}$?

> **Theorem 23.1.** Every linear system Ax $= b$, where $A$ is an $m \times  n$ matrix, has a unique least squares solution $x^{+}$ of smallest norm.

*Proof.* Geometry offers a nice proof of the existence and uniqueness of $x^{+}$. Indeed, we can interpret $b$ as a point in the Euclidean (affine) space $\mathbb{R}^{m}$, and the image subspace of $A$ (also
$$\mathbb{R}^{m}$$
called the column space of $A)$ as a subspace $U$ of (passing through the origin). Then it is clear that
$$\inf \|Ax -b\|_{2}^{2} = \inf \|y -b\|_{2}^{2},$$
$$x\in \mathbb{R} ny\in U$$
with $U =$ Im $A$, and we claim that $x$ minimizes $\|Ax-b\|_{2}^{2}$ iff Ax $= p$, where $p$ the orthogonal projection of $b$ onto the subspace $U$. Recall from Section 13.1 that the orthogonal projection $p_{U}$ : $U \oplus U^{\perp} \to U$ is the linear map given by
$$p_{U}(u + v) = u,$$

<!-- PAGE 772 -->
with $u \in U$ and $v \in U^{\perp}$ . If we let $p = p_{U}(b) \in U$, then for any point $y \in U$, the vectors $\longrightarrow  \longrightarrow$ py $= y$ - $p \in U$ and bp $= p$ - $b \in U^{\perp}$ are orthogonal, which implies that
$$\longrightarrow  \|\longrightarrow  \|\longrightarrow$$
$$\|by\|_{2}^{2} =bp\|_{2}^{2} +py\|_{2}^{2},$$
$\longrightarrow$ where by $= y -b$. Thus, $p$ is indeed the unique point in $U$ that minimizes the distance from $b$ to any point in $U$. See Figure 23.2.
$$bb$$
$$p$$
$$p$$
$$y$$
$$\mathrm{Im} A = UIm A = U$$
$$\mathbb{R}^{3}$$

![Figure 23.2](../../assets/ch23/fig_23_2.png)

**Figure 23.2:** Given a $3 \times  2$ matrix $A, U =$ Im $A$ is the peach plane in and $p$ is the orthogonal projection of $b$ onto $U$. Furthermore, given $y \in U$, the points $b, y$, and $p$ are the vertices of a right triangle. Thus the problem has been reduced to proving that there is a unique $x^{+}$ of minimum norm such that $Ax^{+} = p$, with $p = p_{U}(b) \in U$, the orthogonal projection of $b$ onto $U$. We use the fact that
$$\mathbb{R}^{n}$$
$$= \mathrm{Ker} A \oplus (\mathrm{Ker} A)^{\perp}.$$
$$\mathbb{R}^{n}$$
Consequently, every $x \in$ can be written uniquely as $x = u + v$, where $u \in$ Ker $A$ and $v \in$ (Ker $A)^{\perp}$, and since $u$ and $v$ are orthogonal,
$$\|x\|_{2}^{2} = \|u\|_{2}^{2} + \|v\|_{2}^{2}.$$
Furthermore, since $u \in$ Ker $A$, we have Au $= 0$, and thus Ax $= p$ iff Av $= p$, which shows that the solutions of Ax $= p$ for which $x$ has minimum norm must belong to (Ker $A)^{\perp}$. However, the restriction of $A$ to (Ker $A)^{\perp}$ is injective. This is because if $Av_{1} = Av_{2}$, where $v_{1}, v_{2} \in$ (Ker $A)^{\perp}$, then $A(v_{2}$ - $v_{1}) = 0$, which implies $v_{2}$ - $v_{1} \in$ Ker $A$, and since $v_{1}, v_{2} \in$ (Ker $A)^{\perp}$, we also have $v_{2}$ - $v_{1} \in$ (Ker $A)^{\perp}$, and consequently, $v_{2}$ - $v_{1} = 0$. This shows that there is a unique $x^{+}$ of minimum norm such that $Ax^{+} = p$, and that $x^{+}$ must belong to (Ker $A)^{\perp}$. By our previous reasoning, $x^{+}$ is the unique vector of minimum norm minimizing $\|Ax$ - $b\|_{2}^{2}$.

<!-- PAGE 773 -->
$$\longrightarrow$$
The proof also shows that $x$ minimizes $\|Ax$ - $b\|_{2}^{2}$ iff pb $= b$ - Ax is orthogonal to $U$, which can be expressed by saying that $b$ -Ax is orthogonal to every column of $A$. However, this is equivalent to
$$A^{\top}(b -Ax) = 0,i.e.,A^{\top}Ax = A^{\top}b.$$
Finally, it turns out that the minimum norm least squares solution $x^{+}$ can be found in terms of the pseudo-inverse $A^{+}$ of $A$, which is itself obtained from any SVD of $A$.

> **Definition 23.1.** Given any nonzero $m \times  n$ matrix $A$ of rank $r$, if $A = V DU^{\top}$ is an SVD of $A$ such that
$$D = \begin{pmatrix} \Lambda & 0_{r,n-r} \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} ,$$
with
$$\Lambda  = \mathrm{diag}(\lambda_{1} , \dots  , \lambda_{r} )$$
an $r \times  r$ diagonal matrix consisting of the nonzero singular values of $A$, then if we let $D^{+}$ be the $n \times  m$ matrix
$$D^{+}= \begin{pmatrix} \Lambda^{-1} & 0_{r,m-r} \\ 0_{n-r,r} & 0_{n-r,m-r} \end{pmatrix} ,$$
with
$$\Lambda^{-1} = \mathrm{diag}(1/\lambda_{1} , \dots  , 1/\lambda_{r} ),$$
the pseudo-inverse of $A$ is defined by
$$A^{+}= UD^{+}V^{\top}.$$
If $A = 0_{m,n}$ is the zero matrix, we set $A^{+} = 0_{n,m}$. Observe that $D^{+}$ is obtained from $D$ by inverting the nonzero diagonal entries of $D$, leaving all zeros in place, and then transposing the matrix. For example, given the matrix
$$D = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 & 0 \\ 0 & 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} ,$$
its pseudo-inverse is
$$D^{+} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0_{2}^{1} & 0 & 0 \\ 0 & 0_{3}^{1} & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} .$$
The pseudo-inverse of a matrix is also known as the Moore–Penrose pseudo-inverse. Actually, it seems that $A^{+}$ depends on the specific choice of $U$ and $V$ in an SVD $(U, D, V$ ) for $A$, but the next theorem shows that this is not so.

<!-- PAGE 774 -->

> **Theorem 23.2.** The least squares solution of smallest norm of the linear system Ax $= b$, where $A$ is an $m \times  n$ matrix, is given by
$$x^{+}= A^{+}b = UD^{+}V^{\top}b.$$

*Proof.* First assume that $A$ is a (rectangular) diagonal matrix $D$, as above. Then since $x$ minimizes $\|Dx-b\|_{2}^{2}$ iff Dx is the projection of $b$ onto the image subspace $F$ of $D$, it is fairly obvious that $x^{+} = D^{+}b$. Otherwise, we can write
$$A = V DU^{\top} ,$$
where $U$ and $V$ are orthogonal. However, since $V$ is an isometry,
$$\|Ax -b\|_{2} = \|V DU^{\top} x -b\|_{2} = \|DU^{\top} x -V^{\top} b\|_{2}.$$
Letting $y = U^{\top} x$, we have $\|x\|_{2} = \|y\|_{2}$, since $U$ is an isometry, and since $U$ is surjective, $\|Ax$ - $b\|_{2}$ is minimized iff $\|Dy$ - $V^{\top} b\|_{2}$ is minimized, and we have shown that the least solution is
$$y^{+}= D^{+}V^{\top}b.$$
Since $y = U^{\top} x$, with $\|x\|_{2} = \|y\|_{2}$, we get
$$x^{+}= UD^{+}V^{\top}b = A^{+}b.$$
Thus, the pseudo-inverse provides the optimal solution to the least squares problem. By Theorem 23.2 and Theorem 23.1, $A^{+}b$ is uniquely defined by every $b$, and thus $A^{+}$ depends only on $A$. The Matlab command for computing the pseudo-inverse $B$ of the matrix $A$ is $B =$ pinv(A).

> **Example 23.2.** If $A$ is the rank $2$ matrix
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \\ 4 & 5 & 6 & 7 \end{pmatrix}$$
whose eigenvalues are -1.1652, $0, 0$, 17.1652, using Matlab we obtain the SVD $A = V DU^{\top}$ with $U =$ ,
$$\begin{pmatrix} -0.3147 & 0.7752 & 0.2630 & -0.4805 \\ -0.4275 & 0.3424 & 0.0075 & 0.8366 \\ -0.5402 & -0.0903 & -0.8039 & -0.2319 \\ -0.6530 & -0.5231 & 0.5334 & -0.1243 \\ -0.3147 & -0.7752 & 0.5452 & 0.0520 \\ -0.4275 & -0.3424 & -0.7658 & 0.3371 \\ -0.5402 & 0.0903 & -0.1042 & -0.8301 \\ 0.6530 & 0.5231 & 0.3247 & 0.4411 \end{pmatrix}$$
$$V =,D = \begin{pmatrix} 17.1652 & 0 & 0 & 0 \\ 0 & 1.1652 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$

<!-- PAGE 775 -->
Then
$$D^{+} = \begin{pmatrix} 0.0583 & 0 & 0 & 0 \\ 0 & 0.8583 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
and
$$A^{+} = UD^{+}V^{\top} = \begin{pmatrix} -0.5100 & -0.2200 & 0.0700 & 0.3600 \\ -0.2200 & -0.0900 & 0.0400 & 0.1700 \\ 0.0700 & 0.0400 & 0.0100 & -0.0200 \\ 0.3600 & 0.1700 & 0.0200 & 0.2100 \end{pmatrix} ,$$
$$--$$
which is also the result obtained by calling pinv(A). If $A$ is an $m \times  n$ matrix of rank $n$ (and so $m \ge n)$, it is immediately shown that the QR-decomposition in terms of Householder transformations applies as follows: There are $n m \times  m$ matrices $H_{1}, \dots  , H_{n}$, Householder matrices or the identity, and an upper triangular $m \times  n$ matrix $R$ of rank $n$ such that
$$A = H_{1} \cdots  H_{n}R.$$
Then because each $H_{i}$ is an isometry,
$$\|Ax -b\|_{2} = \|Rx -H_{n} \cdots  H_{1}b\|_{2},$$
and the least squares problem Ax $= b$ is equivalent to the system
$$Rx = H_{n} \cdots  H_{1}b.$$
Now the system
$$Rx = H_{n} \cdots  H_{1}b$$
is of the form
$$\begin{pmatrix} R_{1} \\ 0_{m-n} \end{pmatrix} x = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
where $R_{1}$ is an invertible $n \times  n$ matrix (since $A$ has rank $n), c \in \mathbb{R}^{n}$, and $d \in \mathbb{R}^{m-n}$, and the least squares solution of smallest norm is
$$x^{+}= R_{1}^{-1} c.$$
Since $R_{1}$ is a triangular matrix, it is very easy to invert $R_{1}$. The method of least squares is one of the most effective tools of the mathematical sciences. There are entire books devoted to it. Readers are advised to consult Strang $[176]$, Golub and Van Loan $[83]$, Demmel $[48]$, and Trefethen and Bau $[182]$, where extensions and applications of least squares (such as weighted least squares and recursive least squares) are described. Golub and Van Loan $[83]$ also contains a very extensive bibliography, including a list of books on least squares.
