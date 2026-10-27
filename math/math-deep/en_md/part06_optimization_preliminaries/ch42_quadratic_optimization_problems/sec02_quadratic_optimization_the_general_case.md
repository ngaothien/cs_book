# Quadratic Optimization: The General Case


<!-- PAGE 1553 -->
The use of Lagrange multipliers in optimization and variational problems is discussed extensively in Chapter $50$. Least squares methods and Lagrange multipliers are used to tackle many problems in computer graphics and computer vision; see Trucco and Verri $[184]$, Metaxas $[128]$, Jain, Katsuri, and Schunck $[103]$, Faugeras $[60]$, and Foley, van Dam, Feiner, and Hughes $[64]$.

## 42.2 Quadratic Optimization: The General Case

In this section we complete the study initiated in Section 42.1 and give necessary and sufficient conditions for the quadratic $function_{2}^{1} x^{\top}Ax$ - $x^{\top}b$ to have a global minimum. We begin with the following simple fact:

> **Proposition 42.4.** If $A$ is an invertible symmetric matrix, then the function
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
has a minimum value iff $A$ ⪰ $0$, in which case this optimal value is obtained for a unique value of $x$, namely $x^{*} = A^{-1}b$, and with
$$f(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$

*Proof.* Observe that
$$\frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) = \frac{1}{2} x^{\top}Ax -x^{\top}b + \frac{1}{2} b^{\top}A^{-1}b.$$
Thus,
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b = \frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) - \frac{1}{2} b^{\top}A^{-1}b.$$
If $A$ has some negative eigenvalue, say $-\lambda$  (with $\lambda  > 0)$, if we pick any eigenvector $u$ of $A$ associated with $\lambda$ , then for any $\alpha  \in \mathbb{R}$ with $\alpha  \neq  0$, if we let $x = \alpha u + A^{-1}b$, then since Au $= -\lambda u$, we get
$$f(x) = \frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) - \frac{1}{2} b^{\top}A^{-1}b$$
$$= \frac{1}{2} \alpha u^{\top}A\alpha u - \frac{1}{2} b^{\top}A^{-1}b$$
$$= - \frac{1}{2} \alpha^{2} \lambda  \|u\|_{2}^{2} - \frac{1}{2} b^{\top}A^{-1}b,$$
and since $\alpha$  can be made as large as we want and $\lambda  > 0$, we see that $f$ has no minimum. Consequently, in order for $f$ to have a minimum, we must have $A$ ⪰ $0$. If $A$ ⪰ $0$, since $A$ is invertible, it is positive definite, so $(x$ - $A^{-1}b)^{\top}A(x$ - $A^{-1}b) > 0$ iff $x$ - $A^{-1}b \neq  0$, and it is clear that the minimum value of $f$ is achieved when $x$ - $A^{-1}b = 0$, that is, $x = A^{-1}b$.

<!-- PAGE 1554 -->
Let us now consider the case of an arbitrary symmetric matrix $A$.

> **Proposition 42.5.** If $A$ is an $n \times  n$ symmetric matrix, then the function
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
has a minimum value iff $A$ ⪰ $0$ and (I - $AA^{+})b = 0$, in which case this minimum value is
$$p^{*}= - \frac{1}{2} b^{\top}A^{+}b.$$
Furthermore, if $A$ is diagonalized as $A = U^{\top} \Sigma U$ (with $U$ orthogonal), then the optimal value
$$\mathbb{R}^{n}$$
is achieved by all $x \in$ of the form
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} ,$$
for any $z \in \mathbb{R}^{n-r}$, where $r$ is the rank of $A$.

*Proof.* The case that $A$ is invertible is taken care of by Proposition 42.4, so we may assume that $A$ is singular. If $A$ has rank $r < n$, then we can diagonalize $A$ as
$$A = U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} U,$$
where $U$ is an orthogonal matrix and where $\Sigma_{r}$  is an $r \times  r$ diagonal invertible matrix. Then we have
$$f(x) = \frac{1}{2} x^{\top}U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} Ux -x^{\top}U^{\top} Ub$$
$$= \frac{1}{2} (Ux)^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} Ux -(Ux)^{\top}Ub.$$
If we write
$$Ux = \begin{pmatrix} y \\ z \end{pmatrix} andUb = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
with $y, c \in$ and $z, d \in$ , we get
$$f(x) = \frac{1}{2} (Ux)^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \\  \end{pmatrix} Ux -(Ux)^{\top}Ub$$
$$= \frac{1}{2} (y^{\top}z^{\top}) \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} -(y^{\top}z^{\top}) \begin{pmatrix} c \\ d \end{pmatrix}$$
$$= \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c -z^{\top}d.$$

<!-- PAGE 1555 -->
For $y = 0$, we get
$$f(x) = -z^{\top}d,$$
so if $d \neq  0$, the function $f$ has no minimum. Therefore, if $f$ has a minimum, then $d = 0$. However, $d = 0$ means that
$$Ub = \begin{pmatrix} c \\ 0 \end{pmatrix} ,$$
and we know from Proposition 23.5 that $b$ is in the range of $A$ (here, $U$ is $V^{\top}$ ), which is equivalent to (I - $AA^{+})b = 0$. If $d = 0$, then
$$f(x) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c.$$
$$\mathbb{R}^{r} \mathbb{R}$$
Consider the function $g: \to$  given by
$$g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,y \in \mathbb{R}^{r}.$$
Since
$$\begin{pmatrix} y \\ z \end{pmatrix} = U^{\top} x$$
and $U^{\top}$ is invertible (with inverse $U)$, when $x$ ranges over $\mathbb{R}^{n}, y$ ranges over the whole of $\mathbb{R}^{r}$, and since f(x) $=$ g(y), the function $f$ has a minimum iff $g$ has a minimum. Since $\Sigma_{r}$  is invertible, by Proposition 42.4, the function $g$ has a minimum $iff\Sigma_{r}$  ⪰ $0$, which is equivalent to $A$ ⪰ $0$. Therefore, we have proven that if $f$ has a minimum, then (I - $AA^{+})b = 0$ and $A$ ⪰ $0$. Conversely, if (I - $AA^{+})b = 0$, then
$$\begin{pmatrix} I_{r} & 0 \\ 0 & I_{n-r} \end{pmatrix} \begin{pmatrix} \Sigma_{r} & 0 \\ -U^{\top} & 0 & 0 \end{pmatrix} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ UU^{\top} & 0 & 0 \end{pmatrix} \begin{pmatrix} U \end{pmatrix} b = \begin{pmatrix} I_{r} & 0 \\ 0 & I_{n-r} \\  \end{pmatrix} \begin{pmatrix} I_{r} & 0 \\ -U^{\top} & 0 & 0 \\  \end{pmatrix} \begin{pmatrix} U \end{pmatrix} b$$
$$= U^{\top} \begin{pmatrix} 0 & 0 \\ 0 & I_{n-r} \end{pmatrix} Ub = 0,$$
which implies that if
$$Ub = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
then $d = 0$, so as above
$$f(x) = g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,$$
and because $A$ ⪰ $0$, we also have $\Sigma_{r}$  ⪰ $0$, so $g$ and $f$ have a minimum. When the above conditions hold, since
$$A = U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} U$$

<!-- PAGE 1556 -->
is positive semidefinite, the pseudo-inverse $A^{+}$ of $A$ is given by
$$A^{+}= U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} U,$$
and since
$$f(x) = g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,$$
by Proposition 42.4 the minimum of $g$ is achieved iff $y^{*} = \Sigma_{r}^{-1}  c$. Since f(x) is independent of $z$, we can choose $z = 0$, and since $d = 0$, for $x^{*}$ given by
$$Ux^{*}= \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} andUb = \begin{pmatrix} c \\ 0 \end{pmatrix} ,$$
we deduce that
$$x^{*}= U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} c \\ 0 \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} Ub = A^{+}b,(*)$$
and the minimum value of $f$ is
$$f(x^{*}) = \frac{1}{2} (A^{+}b)^{\top}AA^{+}b -b^{\top}A^{+}b = \frac{1}{2} b^{\top}A^{+}AA^{+}b -b^{\top}A^{+}b = - \frac{1}{2} b^{\top}A^{+}b,$$
$$\mathbb{R}^{n}$$
since $A^{+}$ is symmetric and $A^{+}AA^{+} = A^{+}$. For any $x \in$ of the form
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} ,z \in \mathbb{R}^{n-r},$$
since
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ z \end{pmatrix} ,$$
and since f(x) is independent of $z$ (because f(x) $=$ g(y)), we have
$$f(x) = f(x^{*}) = - \frac{1}{2} b^{\top}A^{+}b.$$
The problem of minimizing the function
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
in the case where we add either linear constraints of the form $C^{\top}x = 0$ or affine constraints
$$\mathbb{R}^{m}$$
of the form $C^{\top}x = t$ (where $t \in$ and $t \neq  0)$ where $C$ is an $n \times  m$ matrix can be reduced to the unconstrained case using a QR-decomposition of $C$. Let us show how to do this for linear constraints of the form $C^{\top}x = 0$.

<!-- PAGE 1557 -->
If we use a QR decomposition of $C$, by permuting the columns of $C$ to make sure that the first $r$ columns of $C$ are linearly independent (where $r =$ rank(C)), we may assume that
$$C = Q^{\top} \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix} \Pi ,$$
where $Q$ is an $n \times  n$ orthogonal matrix, $R$ is an $r \times  r$ invertible upper triangular matrix, $S$ is an $r \times  (m$ - $r)$ matrix, and $\Pi$  is a permutation matrix $(C$ has rank $r)$. Then if we let
$$x = Q^{\top} \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
where $y \in$ and $z \in$ , then $C^{\top}x = 0$ becomes
$$C^{\top}x = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} Qx = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} = 0,$$
which implies $y = 0$, and every solution of $C^{\top}x = 0$ is of the form
$$x = Q^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} .$$
Our original problem becomes
$$minimize \frac{1}{2} (y^{\top}z^{\top})QAQ^{\top} \begin{pmatrix} y \\ z \end{pmatrix} + (y^{\top}z^{\top})Qb$$
$$subject toy = 0, y \in \mathbb{R}^{r}, z \in \mathbb{R}^{n-r}.$$
Thus, the constraint $C^{\top}x = 0$ has been simplified to $y = 0$, and if we write
$$QAQ^{\top}= \begin{pmatrix} G_{11} & G_{12} \\ G_{21} & G_{22} \end{pmatrix} ,$$
where $G_{11}$ is an $r \times  r$ matrix and $G_{22}$ is an $(n$ - $r) \times  (n$ - $r)$ matrix and
$$Qb = \begin{pmatrix} b_{1} \\ b_{2} \end{pmatrix} ,b_{1} \in \mathbb{R}^{r}, b_{2} \in \mathbb{R}^{n-r},$$
our problem becomes
$$minimize \frac{1}{2} z^{\top}G_{22}z + z^{\top}b_{2},z \in \mathbb{R}^{n-r},$$
the problem solved in Proposition 42.5. Constraints of the form $C^{\top}x = t$ (where $t \neq  0)$ can be handled in a similar fashion. In this case, we may assume that $C$ is an $n \times  m$ matrix with full rank (so that $m \le n)$ and $t \in \mathbb{R}^{m}$. Then we use a QR-decomposition of the form
$$C = P \begin{pmatrix} R \\ 0 \end{pmatrix} ,$$
