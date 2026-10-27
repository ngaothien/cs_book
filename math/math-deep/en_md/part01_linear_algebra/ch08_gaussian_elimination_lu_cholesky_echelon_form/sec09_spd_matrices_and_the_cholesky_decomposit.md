# SPD Matrices and the Cholesky Decomposition


<!-- PAGE 292 -->

## 8.9 SPD Matrices and the Cholesky Decomposition


> **Definition 8.4.** A real $n \times  n$ matrix $A$ is symmetric positive definite, for short SPD, iff it is symmetric and if
$$\mathbb{R}^{n}$$
$$x^{\top}Ax > 0for all x \in with x \neq  0.$$
The following facts about a symmetric positive definite matrix $A$ are easily established (some left as an exercise):
$(1)$ The matrix $A$ is invertible. (Indeed, if Ax $= 0$, then $x^{\top}Ax = 0$, which implies $x = 0.)$
$(2)$ We have $a_{i i} > 0$ for $i = 1, \dots  , n$. (Just observe that for $x = e_{i}$, the ith canonical basis vector of $\mathbb{R}^{n}$, we have $e_{i}^{\top} Ae_{i} = a_{i i} > 0.)$
$(3)$ For every $n \times  n$ real invertible matrix $Z$, the matrix $Z^{\top}AZ$ is real symmetric positive definite iff $A$ is real symmetric positive definite.
$(4)$ The set of $n \times  n$ real symmetric positive definite matrices is convex. This means that if $A$ and $B$ are two $n\times n$ symmetric positive definite matrices, then for any $\lambda  \in \mathbb{R}$ such that $0 \le \lambda  \le 1$, the matrix $(1$ - $\lambda )A + \lambda B$ is also symmetric positive definite. Clearly since $A$ and $B$ are symmetric, $(1$ - $\lambda )A + \lambda B$ is also symmetric. For any nonzero $x \in \mathbb{R}^{n}$, we have $x^{\top}Ax > 0$ and $x^{\top}Bx > 0$, so
$$x^{\top}((1 -\lambda )A + \lambda B)x = (1 -\lambda )x^{\top}Ax + \lambda x^{\top}Bx > 0,$$
because $0 \le \lambda  \le 1$, so $1-\lambda  \ge 0$ and $\lambda  \ge 0$, and $1-\lambda$  and $\lambda$  can’t be zero simultaneously.
$(5)$ The set of $n\times n$ real symmetric positive definite matrices is a cone. This means that if $A$ is symmetric positive definite and if $\lambda  > 0$ is any real, then $\lambda A$ is symmetric positive definite. Clearly $\lambda A$ is symmetric, and for nonzero $x \in \mathbb{R}^{n}$, we have $x^{\top}Ax > 0$, and since $\lambda  > 0$, we have $x^{\top}\lambda$ Ax $= \lambda x^{\top}Ax > 0$.
$$Remark: Given a complex m \times  n matrix A, we define \frac{the}{A} matrix \frac{\overline{A}}{A^{\top}).} as the m \times  n matrix$$
$\overline{A} = (\overline{a}_{ij})$. Then we define $A^{*}$ as the $n \times  m$ matrix $A^{*} =$ ( $)^{\top} =$ (  The $n \times  n$ complex matrix $A$ is Hermitian if $A^{*} = A$. This is the complex analog of the notion of a real symmetric matrix.

> **Definition 8.5.** A complex $n \times  n$ matrix $A$ is Hermitian positive definite, for short HPD, if it is Hermitian and if
$$\mathbb{C}^{n}$$
$$z^{*}Az > 0for all z \in with z \neq  0.$$
It is easily verified that Properties (1)-(5) hold for Hermitian positive definite matrices; replace $\top$ by *.

<!-- PAGE 293 -->
It is instructive to characterize when a $2\times 2$ real matrix $A$ is symmetric positive definite. Write
$$A = \begin{pmatrix} a & c \\ c & b \end{pmatrix} .$$
Then we have
$$\begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} a & c \\ c & b \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = ax^{2}+ 2cxy + by^{2}.$$
$$If the above expression is strictly positive for all nonzero vectors^{x} \begin{pmatrix}\end{pmatrix} , then for x = 1, y = 0$$
we get a $> 0$ and for $x = 0, y = 1$ we get $b > 0$. Then we can $write^{y}$
$$2c^{2}$$
$$ax^{2}+ 2cxy + by^{2}= \begin{pmatrix} \sqrt & c \\ \overline{ax} +\sqrt ay \end{pmatrix} + by^{2}-a y^{2}$$
$$2$$
$$= \begin{pmatrix} \sqrt & c \\ \overline{ax} +\sqrt ay \end{pmatrix} + \frac{1}{a} \begin{pmatrix} ab -c^{2} \end{pmatrix} y^{2}.(\dagger )$$
Since a $> 0$, if ab - $c^{2} \le 0$, then we can choose $y > 0$ so that the second term is negative or zero, and we can set $x = -(c/a)y$ to make the first term zero, in which case $ax^{2}+2cxy+by^{2} \le 0$, so we must have ab - $c^{2} > 0$. Conversely, if a $> 0, b > 0$ and ab $> c^{2}$, then for any $(x, y) \neq  (0, 0)$, if $y = 0$, then $x \neq  0$ and the first term of $(\dagger$ ) is positive, and if $y \neq  0$, then the second term of $(\dagger$ ) is positive. Therefore, the matrix $A$ is symmetric positive definite iff
$$a > 0, b > 0, ab > c^{2}.(*)$$
Note that ab - $c^{2} =$ det(A), so the third condition says that det(A) $> 0$. Observe that the condition $b > 0$ is redundant, since if a $> 0$ and ab $> c^{2}$, then we must have $b > 0$ (and similarly $b > 0$ and ab $> c^{2}$ implies that a $> 0)$. We can try to visualize the space of $2 \times  2$ real symmetric positive definite matrices in $\mathbb{R}^{3}$, by viewing (a, $b, c)$ as the coordinates along the $x, y, z$ axes. Then the locus determined by the strict inequalities in (*) corresponds to the region on the side of the cone of equation xy $= z^{2}$ that does not contain the origin and for which $x > 0$ and $y > 0$. For $z = \delta$  fixed, the equation xy $= \delta^{2}$ define a hyperbola in the plane $z = \delta$ . The cone of equation xy $= z^{2}$ consists of the lines through the origin that touch the hyperbola xy $= 1$ in the plane $z = 1$. We only consider the branch of this hyperbola for which $x > 0$ and $y > 0$. See Figure 8.6. It is not hard to show that the inverse of a real symmetric positive definite matrix is also real symmetric positive definite, but the product of two real symmetric positive definite matrices may not be symmetric positive definite, as the following example shows:
$$\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & -1\sqrt{2} \\ -1/ & 2 & 3/ & 2 \end{pmatrix} = \begin{pmatrix} \sqrt \\ 0\sqrt & 2/\sqrt{2} \\ -1/ & \overline{2} & 5/ & 2 \end{pmatrix} .$$

<!-- PAGE 294 -->
$$xy = 1$$
$$\mathbb{R}^{3}$$

![Figure 8.6](../../assets/ch08/fig_8_6.png)

**Figure 8.6:** Two views of the surface xy $= z^{2}$ in . The intersection of the surface with a constant $z$ plane results in a hyperbola. The region associated with the $2 \times  2$ symmetric positive definite matrices lies in ”front” of the green side. According to the above criterion, the two matrices on the left-hand side are real symmetric positive definite, but the matrix on the right-hand side is not even symmetric, and
$$\sqrt$$
$$\begin{pmatrix} -6 & 1 \end{pmatrix} \begin{pmatrix} \sqrt \\ 0\sqrt & 2/\sqrt{2} \\ -1/ & \overline{2} & 5/ & 2 \end{pmatrix} \begin{pmatrix} -6 \\ 1 \end{pmatrix} = \begin{pmatrix} -6 & 1 \end{pmatrix} \begin{pmatrix} \sqrt \\ 2/\sqrt{2} \\ 11/ & 2 \end{pmatrix} = -1/\overline{2},$$
even though its eigenvalues are both real and positive. Next we show that a real symmetric positive definite matrix has a special LU-factorization of the form $A = BB^{\top}$, where $B$ is a lower-triangular matrix whose diagonal elements are strictly positive. This is the Cholesky factorization. First we note that a symmetric positive definite matrix satisfies the condition of Proposition 8.2.

> **Proposition 8.9.** If $A$ is a real symmetric positive definite matrix, then A(1 : $k, 1$ : $k)$ is symmetric positive definite and thus invertible for $k = 1, \dots  , n$.

<!-- PAGE 295 -->

*Proof.* Since $A$ is symmetric, each A(1 : $k, 1$ : $k)$ is also symmetric. If $w \in \mathbb{R}^{k}$, with
$$\mathbb{R}^{n}$$
$1 \le k \le n$, we let $x \in$ be the vector with $x_{i} = w_{i}$ for $i = 1, \dots  , k$ and $x_{i} = 0$ for $i = k + 1, \dots  , n$. Now since $A$ is symmetric positive definite, we have $x^{\top}Ax > 0$ for all $\mathbb{R}^{n} x \in$ with $x \neq  0$. This holds in particular for all vectors $x$ obtained from nonzero vectors $\mathbb{R}^{k} w \in$ as defined earlier, and clearly
$$x^{\top}Ax = w^{\top}A(1 : k, 1 : k) w,$$
which implies that A(1 : $k, 1$ : $k)$ is symmetric positive definite. Thus, by Fact $1$ above, A(1 : $k, 1$ : $k)$ is also invertible. Proposition 8.9 also holds for a complex Hermitian positive definite matrix. Proposition 8.9 can be strengthened as follows: $A$ real (resp. complex) matrix $A$ is symmetric (resp. Hermitian) positive definite iff det(A(1 : $k, 1$ : $k)) > 0$ for $k = 1, \dots  , n$. The above fact is known as Sylvester’s criterion. We will prove it after establishing the Cholesky factorization. Let $A$ be an $n \times  n$ real symmetric positive definite matrix and write
$$A = \begin{pmatrix} a_{1 1} & W^{\top} \\ W & C \end{pmatrix} ,$$
where $C$ is an $(n$ - $1) \times  (n$ - $1)$ symmetric matrix and $W$ is an $(n$ - $1) \times  1$ matrix. Since $A$
$$\sqrt$$
is symmetric positive definite, $a_{1 1} > 0$, and we can compute $\alpha  = \overline{a}_{1 1}$. The trick is that we can factor $A$ uniquely as
$$A = \begin{pmatrix} a_{1 1} & W^{\top} \\ W & C \end{pmatrix} = \begin{pmatrix} \alpha & 0 \\ W/\alpha & I \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & C -WW^{\top}/a_{1 1} \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & I \end{pmatrix} ,$$
i.e., as $A = B_{1}A_{1}B_{1}^{\top}$ , where $B_{1}$ is lower-triangular with positive diagonal entries. Thus, $B_{1}$ is invertible, and by Fact $(3)$ above, $A_{1}$ is also symmetric positive definite.
Remark: The matrix $C -WW^{\top} /a_{1 1}$ is known as the Schur complement of the $1\times 1$ matrix $(a_{11})$ in $A$.

> **Theorem 8.10.** (Cholesky factorization) Let $A$ be a real symmetric positive definite matrix. Then there is some real lower-triangular matrix $B$ so that $A = BB^{\top}$. Furthermore, $B$ can be chosen so that its diagonal elements are strictly positive, in which case $B$ is unique.

*Proof.* We proceed by induction on the dimension $n$ of $A$. For $n = 1$, we must have $a_{1 1} > 0$,
$$\sqrt$$
and if we let $\alpha  = \overline{a}_{1 1}$ and $B = (\alpha$ ), the theorem holds trivially. If $n \ge 2$, as we explained above, again we must have $a_{1 1} > 0$, and we can write
$$A = \begin{pmatrix} a_{1 1} & W^{\top} \\ W & C \end{pmatrix} = \begin{pmatrix} \alpha & 0 \\ W/\alpha & I \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & C -WW^{\top}/a_{1 1} \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & I \end{pmatrix} = B_{1}A_{1}B_{1}^{\top} ,$$

<!-- PAGE 296 -->
$$\sqrt$$
where $\alpha  = \overline{a}_{1 1}$, the matrix $B_{1}$ is invertible and
$$A_{1} = \begin{pmatrix} 1 & 0 \\ 0 & C -WW^{\top}/a_{1 1} \end{pmatrix}$$
is symmetric positive definite. However, this implies that $C$ - $WW^{\top} /a_{1 1}$ is also symmetric
$$\mathbb{R}^{n}$$
positive definite (consider $x^{\top}A_{1}x$ for every $x \in$ with $x \neq  0$ and $x_{1} = 0)$. Thus, we can apply the induction hypothesis to $C$ - $WW^{\top} /a_{1 1}$ (which is an $(n$ - $1) \times  (n$ - $1)$ matrix), and we find a unique lower-triangular matrix $L$ with positive diagonal entries so that
$$C -WW^{\top} /a_{1 1} = LL^{\top}.$$
But then we get
$$A= \begin{pmatrix} \alpha & 0 \\ W/\alpha & I \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & C -WW^{\top}/a_{1 1} \\  \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & I \end{pmatrix}$$
$$= \begin{pmatrix} \alpha & 0 \\ W/\alpha & I \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & LL^{\top} \\  \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & I \\  \end{pmatrix}$$
$$= \begin{pmatrix} \alpha & 0 \\ W/\alpha & I \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & L \\  \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & L^{\top} \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & I \end{pmatrix}$$
$$= \begin{pmatrix} \alpha & 0 \\ W/\alpha & L \end{pmatrix} \begin{pmatrix} \alpha & W^{\top}/\alpha \\ 0 & L^{\top} \end{pmatrix} .$$
Therefore, if we let
$$B = \begin{pmatrix} \alpha & 0 \\ W/\alpha & L \end{pmatrix} ,$$
we have a unique lower-triangular matrix with positive diagonal entries and $A = BB^{\top}$.
Remark: The uniqueness of the Cholesky decomposition can also be established using the uniqueness of an LU-decomposition. Indeed, if $A = B_{1}B_{1}^{\top} = B_{2}B_{2}^{\top}$ where $B_{1}$ and $B_{2}$ are lower triangular with positive diagonal entries, if we let $\Delta_{1}$  (resp. $\Delta_{2}$ ) be the diagonal matrix consisting of the diagonal entries of $B_{1}$ (resp. $B_{2})$ so that $(\Delta_{k} )_{ii} = (B_{k})_{ii}$ for $k = 1, 2$, then we have two LU-decompositions
$$A = (B_{1}\Delta_{1}^{-1}  )(\Delta_{1} B_{1}^{\top} ) = (B_{2}\Delta_{2}^{-1}  )(\Delta_{2} B_{2}^{\top} )$$
with $B_{1}\Delta_{1}^{-1}  , B_{2}\Delta_{2}^{-1}$ unit lower triangular, and $\Delta_{1} B_{1}^{\top} , \Delta_{2} B_{2}^{\top}$ upper triangular. By uniquenes of LU-factorization (Theorem 8.5(1)), we have
$$B_{1}\Delta_{1}^{-1} = B_{2}\Delta_{2}^{-1}  ,\Delta_{1} B_{1}^{\top} = \Delta_{2} B_{2}^{\top} ,$$
and the second equation yields
$$B_{1}\Delta_{1}  = B_{2}\Delta_{2} .(*)$$

<!-- PAGE 297 -->
The diagonal entries of $B_{1}\Delta_{1}$  are $(B_{1})_{ii}^{2}$ and similarly the diagonal entries of $B_{2}\Delta_{2}$  are $(B_{2})_{ii}^{2}$, so the above equation implies that
$$(B_{1})_{ii}^{2} = (B_{2})_{ii}^{2},i = 1, \dots  , n.$$
Since the diagonal entries of both $B_{1}$ and $B_{2}$ are assumed to be positive, we must have
$$(B_{1})_{ii} = (B_{2})_{ii},i = 1, \dots  , n;$$
that is, $\Delta_{1}  = \Delta_{2}$ , and since both are invertible, we conclude from (*) that $B_{1} = B_{2}$. Theorem 8.10 also holds for complex Hermitian positive definite matrices. In this case, we have $A = BB^{*}$ for some unique lower triangular matrix $B$ with positive diagonal entries. The proof of Theorem 8.10 immediately yields an algorithm to compute $B$ from $A$ by solving for a lower triangular matrix $B$ such that $A = BB^{\top}$ (where both $A$ and $B$ are real matrices). For $j = 1, \dots  , n$,
$$1/2$$
$$!$$
$$b_{j j} =a_{j j} - \sum_{k=1}^{j-1}  b_{j k}^{2},$$
and for $i = j + 1, \dots  , n$ (and $j = 1, \dots  , n$ - $1)$
$$!$$
$$b_{i j} =a_{i j} - \sum_{k=1}^{j-1}  b_{i k}b_{j k}/b_{j j}.$$
The above formulae are used to compute the jth column of $B$ from top-down, using the first $j -1$ columns of $B$ previously computed, and the matrix $A$. In the case of $n = 3, A = BB^{\top}$ yields
$$\begin{pmatrix} a_{11} & a_{12} & a_{31} \\ a_{21} & a_{22} & a_{32} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} b_{11}00 \begin{pmatrix} b_{11} & b_{21} & b_{31} \\ 0 & b_{22} & b_{32} \\ 0 & 0 & b_{33} \end{pmatrix}$$
$$=b_{21}b_{22}0$$
$$$$
$$b_{31}b_{32}b_{33}$$
$$b_{11}^{2}b_{11}b_{21}b_{11}b_{31}$$
$$=b_{11}b_{21}b_{21}^{2} + b_{22}^{2}b_{21}b_{31} + b_{22}b_{32}.$$
$$$$
$$b_{11}b_{31}b_{21}b_{31} + b_{22}b_{32}b_{31}^{2} + b_{32}^{2} + b_{33}^{2}$$
We work down the first column of $A$, compare entries, and discover that
$$\sqrt$$
$$a_{11} = b_{11}^{2}b_{11} =\overline{a}_{11}$$
$$a_{21} = b_{11}b_{21}b_{21} = \frac{a_{21}}{b_{11}}$$
$$a_{31} = b_{11}b_{31}b_{31} = \frac{a_{31}}{b_{11}} .$$

<!-- PAGE 298 -->
Next we work down the second column of $A$ using previously calculated expressions for $b_{21}$ and $b_{31}$ to find that
$$a_{22} = b_{21}^{2} + b_{22}^{2}b_{22} = \begin{pmatrix} a_{22} -\overline{b}_{21}^{212} \\ a_{32} -b_{21} \end{pmatrix}$$
$$a_{32} = b_{21}b_{31} + b_{22}b_{32}b_{32} = \frac{b_{31}}{b_{22}} .$$
Finally, we use the third column of $A$ and the previously calculated expressions for $b_{31}$ and $b_{32}$ to determine $b_{33}$ as
$$a_{33} = b_{31}^{2} + b_{32}^{2} + b_{33}^{2}b_{33} = \begin{pmatrix} a_{33} -b_{31}^{2}-\overline{b}_{32}^{212} \end{pmatrix} .$$
For another example, if
$$A = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 2 & 2 & 2 & 2 & 2 \\ 1 & 2 & 3 & 3 & 3 & 3 \\ 1 & 2 & 3 & 4 & 4 & 4 \\ 1 & 2 & 3 & 4 & 5 & 5 \\ 1 & 2 & 3 & 4 & 5 & 6 \end{pmatrix} ,$$
we find that
$$B = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 1 & 1 \end{pmatrix} .$$
We leave it as an exercise to find similar formulae (involving conjugation) to factor a complex Hermitian positive definite matrix $A$ as $A = BB^{*}$. The following Matlab program implements the Cholesky factorization. function $B =$ Cholesky(A) $n =$ size(A,1); $B =$ zeros(n,n); for $j =$ 1:n-1; if $j == 1$
$$B(1,1) = sqrt(A(1,1));$$
$$for i = 2:n$$
$$B(i,1) = A(i,1)/B(1,1);$$
$$end$$
else
$$B(j,j) = sqrt(A(j,j) - B(j,1:j-1)*B(j,1:j-1)’);$$
$$for i = j+1:n$$

<!-- PAGE 299 -->
$$B(i,j) = (A(i,j) - B(i,1:j-1)*B(j,1:j-1)’)/B(j,j);$$
$$end$$
end end B(n,n) $=$ sqrt(A(n,n) - B(n,1:n-1)*B(n,1:n-1)’); end If we run the above algorithm on the following matrix
$$A = \begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 \\ 0 & 1 & 4 & 1 & 0 \\ 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 1 & 4 \end{pmatrix} ,$$
we obtain
$$B = \begin{pmatrix} 2.0000 & 0 & 0 & 0 & 0 \\ 0.5000 & 1.9365 & 0 & 0 & 0 \\ 0 & 0.5164 & 1.9322 & 0 & 0 \\ 0 & 0 & 0.5175 & 1.9319 & 0 \\ 0 & 0 & 0 & 0.5176 & 1.9319 \end{pmatrix} .$$
The Cholesky factorization can be used to solve linear systems Ax $= b$ where $A$ is symmetric positive definite: Solve the two systems Bw $= b$ and $B^{\top}x = w$.
Remark: It can be shown that this method requires $n^{3}/6 + O(n^{2})$ additions, $n^{3}/6 + O(n^{2})$ multiplications, $n^{2}/2+O(n)$ divisions, and O(n) square root extractions. Thus, the Cholesky method requires half of the number of operations required by Gaussian elimination (since Gaussian elimination requires $n^{3}/3 + O(n^{2})$ additions, $n^{3}/3 + O(n^{2})$ multiplications, and $n^{2}/2 +$ O(n) divisions). It also requires half of the space (only $B$ is needed, as opposed to both $L$ and $U)$. Furthermore, it can be shown that Cholesky’s method is numerically stable (see Trefethen and Bau $[182]$, Lecture $23)$. In Matlab the function chol returns the lower-triangular matrix $B$ such that $A = BB^{\top}$ using the call $B =$ chol(A, ‘lower’).
Remark: If $A = BB^{\top}$, where $B$ is any invertible matrix, then $A$ is symmetric positive definite.

*Proof.* Obviously, $BB^{\top}$ is symmetric, and since $B$ is invertible, $B^{\top}$ is invertible, and from
$$x^{\top}Ax = x^{\top}BB^{\top}x = (B^{\top}x)^{\top}B^{\top}x,$$
it is clear that $x^{\top}Ax > 0$ if $x \neq  0$. We now give three more criteria for a symmetric matrix to be positive definite.

<!-- PAGE 300 -->

> **Proposition 8.11.** Let $A$ be any $n\times n$ real symmetric matrix. The following conditions are equivalent:
(a) $A$ is positive definite.
$(b)$ All principal minors of $A$ are positive; that is: det(A(1 : $k, 1$ : $k)) > 0$ for $k = 1, \dots  , n$ (Sylvester’s criterion).
$(c) A$ has an LU-factorization and all pivots are positive.
$(d) A$ has an $LDL^{\top}-factorization$ and all pivots in $D$ are positive.

*Proof.* By Proposition 8.9, if $A$ is symmetric positive definite, then each matrix A(1 : $k, 1$ : $k)$ is symmetric positive definite for $k = 1, \dots  , n$. By the Cholesky decomposition, A(1 : $k, 1$ : $k) = Q^{\top}Q$ for some invertible matrix $Q$, so det(A(1 : $k, 1$ : $k)) = det(Q)^{2} > 0$. This shows that (a) implies $(b)$. If det(A(1 : $k, 1$ : $k)) > 0$ for $k = 1, \dots  , n$, then each A(1 : $k, 1$ : $k)$ is invertible. By Proposition 8.2, the matrix $A$ has an LU-factorization, and since the pivots $\pi_{k}$  are given by
$$a_{11} = \det(A(1 : 1, 1 : 1))if k = 1$$
$$$$
$$\pi_{k}  = \frac{\det(A(1 : k, 1 : k))}{\det(A(1 : k -1, 1 : k -1))} if k = 2, \dots  , n,$$
$$$$
we see that $\pi_{k}  > 0$ for $k = 1, \dots  , n$. Thus $(b)$ implies $(c)$. Assume $A$ has an LU-factorization and that the pivots are all positive. Since $A$ is symmetric, this implies that $A$ has a factorization of the form
$$A = LDL^{\top},$$
with $L$ lower-triangular with 1s on its diagonal, and where $D$ is a diagonal matrix with positive entries on the diagonal (the pivots). This shows that $(c)$ implies $(d)$. Given a factorization $A = LDL^{\top}$ with all pivots in $D$ positive, if we form the diagonal matrix
$$\sqrt\sqrt \sqrt$$
$$\overline{D} = \mathrm{diag}(\overline{\pi}_{1}, \dots  ,\overline{\pi}_{n})$$
$$\sqrt$$
and if we let $B = L \overline{D}$, then we have
$$A = BB^{\top},$$
with $B$ lower-triangular and invertible. By the remark before Proposition 8.11, $A$ is positive definite. Hence, $(d)$ implies (a). Criterion $(c)$ yields a simple computational test to check whether a symmetric matrix is positive definite. There is one more criterion for a symmetric matrix to be positive definite:
