# Polynomial Interpolation (Lagrange, Newton, Hermite)


<!-- PAGE 1095 -->
Remark: Letting U(g) $=$ A-V $(g)$, the identity $V (g_{1})\cup \cdots \cup V (g_{m}) = V (g_{1} \cdots  g_{m})$ translates to $U(g_{1}) \cap \cdots  \cap U(g_{m}) = U(g_{1} \cdots  g_{m})$. This suggests to define a topology on $A$ whose basis of open sets consists of the sets U(g). In this topology (called the Zariski topology), the sets of the form $V (g)$ are closed sets. Also, when $g_{1}, \dots  , g_{m} \in A[X_{1}, \dots  , X_{n}]$ and $n \ge 2$, understanding the structure of the closed sets of the form $V (g_{1})\cap \cdots \cap V (g_{m})$ is quite difficult, and it is the object of algebraic geometry (at least, its classical part).  When $f \in A[X_{1}, \dots  , X_{n}]$ and $n \ge 2$, one should not apply Proposition 30.27 abusively. For example, let
$$f(X, Y ) = X^{2}+ Y^{2}-1,$$
considered as a polynomial in $\mathbb{R}[X, Y$ ]. Since $\mathbb{R}$ is an infinite field and since
$$-$$
$$f \begin{pmatrix} 1 -t^{2} & 2t \\ , \\ 1 + t^{2} & 1 + t^{2} \end{pmatrix} = \frac{(1t^{2})^{2}}{(1 + t^{2})^{2}} + \frac{(2t)^{2}}{(1 + t^{2})^{2}} -1 = 0,$$
for every $t \in \mathbb{R}$, it would be tempting to say that $f = 0$. But what’s wrong with the above reasoning is that there are no two infinite subsets $R_{1}, R_{2}$ of $\mathbb{R}$ such that $f(\alpha_{1} , \alpha_{2}$ ) $= 0$ for all $(\alpha_{1} , \alpha_{2}$ ) $\in \mathbb{R}^{2}$. For every $\alpha_{1}  \in \mathbb{R}$, there are at most two $\alpha_{2}  \in \mathbb{R}$ such that $f(\alpha_{1} , \alpha_{2}$ ) $= 0$. What the example shows though, is that a nonnull polynomial $f \in A[X_{1}, \dots  , X_{n}]$ where $n \ge 2$ can have an infinite number of zeros. This is in contrast with nonnull polynomials in one variables over an infinite field (which have a number of roots bounded by their degree). We now look at polynomial interpolation.

## 30.7 Polynomial Interpolation (Lagrange, Newton,

$$Hermite)$$
Let $K$ be a field. First, we consider the following interpolation problem: Given a sequence $(\alpha_{1} , \dots  , \alpha_{m+1}$ ) of pairwise distinct scalars in $K$ and any sequence $(\beta_{1} , \dots  , \beta_{m+1}$ ) of scalars in $K$, where the $\beta_{j}$  are not necessarily distinct, find a polynomial P(X) of degree $\le m$ such that
$$P(\alpha_{1} ) = \beta_{1} , \dots  , P(\alpha_{m+1} ) = \beta_{m+1} .$$
First, observe that if such a polynomial exists, then it is unique. Indeed, this is a consequence of Proposition 30.24. Thus, we just have to find any polynomial of degree $\le m$. Consider the following so-called Lagrange polynomials:
$$(X -\alpha_{1} ) \cdots  (X -\alpha_{i-1} )(X -\alpha_{i+1} ) \cdots  (X -\alpha_{m+1} )$$
$$L_{i}(X) =.$$
$$(\alpha_{i}  -\alpha_{1} ) \cdots  (\alpha_{i}  -\alpha_{i-1} )(\alpha_{i}  -\alpha_{i+1} ) \cdots  (\alpha_{i}  -\alpha_{m+1} )$$
Note that $L(\alpha_{i}$ ) $= 1$ and that $L(\alpha_{j}$ ) $= 0$, for all $j \neq  i$. But then,
$$P(X) = \beta_{1} L_{1} + \cdots  + \beta_{m+1} L_{m+1}$$

<!-- PAGE 1096 -->
is the unique desired polynomial, since clearly, $P(\alpha_{i}$ ) $= \beta_{i}$ . Such a polynomial is called a Lagrange interpolant. Also note that the polynomials $(L_{1}, \dots  , L_{m+1})$ form a basis of the vector space of all polynomials of degree $\le m$. Indeed, if we had
$$\lambda_{1} L_{1}(X) + \cdots  + \lambda_{m+1} L_{m+1}(X) = 0,$$
setting $X$ to $\alpha_{i}$ , we would get $\lambda_{i}  = 0$. Thus, the $L_{i}$ are linearly independent, and by the previous argument, they are a set of generators. We we call $(L_{1}, \dots  , L_{m+1})$ the Lagrange basis (of order $m + 1)$. It is known from numerical analysis that from a computational point of view, the Lagrange basis is not very good. Newton proposed another solution, the method of divided differences. Consider the polynomial P(X) of degree $\le m$, called the Newton interpolant, P(X) $= \lambda_{0}  + \lambda_{1} (X$ - $\alpha_{1}$ ) $+ \lambda_{2} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$ ) $+ \cdots  + \lambda_{m} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$ ) $\cdots  (X$ - $\alpha_{m}$ ). Then, the $\lambda_{i}$  can be determined by successively setting $X$ to, $\alpha_{1} , \alpha_{2} , \dots  , \alpha_{m+1}$ . More precisely, we define inductively the polynomials Q(X) and $Q(\alpha_{1} , \dots  , \alpha_{i} , X)$, for $1 \le i \le m$, as follows:
$$Q(X) = P(X)$$
$$Q_{1}(\alpha_{1} , X) = \frac{Q(X)Q(\alpha_{1} )}{X-\alpha_{1}} -$$
$$-$$
$$Q(\alpha_{1} , \alpha_{2} , X) = \frac{Q(\alpha_{1} , X)Q(\alpha_{1} , \alpha_{2} )}{X-\alpha_{2}}$$
$$\dots$$
$$Q(\alpha_{1} , \dots  , \alpha_{i} , X) = \frac{Q(\alpha_{1} , \dots  , \alpha_{i-1} , X)Q(\alpha_{1} , \dots  , \alpha_{i-1} , \alpha_{i} )}{X-\alpha_{i}} -,$$
$$\dots$$
$$-$$
$$Q(\alpha_{1} , \dots  , \alpha_{m} , X) = \frac{Q(\alpha_{1} , \dots  , \alpha_{m-1} , X)Q(\alpha_{1} , \dots  , \alpha_{m-1} , \alpha_{m} )}{X-\alpha_{m}} .$$
By induction on $i, 1 \le i \le m$ - $1$, it is easily verified that
$$Q(X) = P(X),$$
$$Q(\alpha_{1} , \dots  , \alpha_{i} , X) = \lambda_{i}  + \lambda_{i+1} (X -\alpha_{i+1} ) + \cdots  + \lambda_{m} (X -\alpha_{i+1} ) \cdots  (X -\alpha_{m} ),$$
$$Q(\alpha_{1} , \dots  , \alpha_{m} , X) = \lambda_{m} .$$
From the above expressions, it is clear that
$$\lambda_{0}  = Q(\alpha_{1} ),$$
$$\lambda_{i}  = Q(\alpha_{1} , \dots  , \alpha_{i} , \alpha_{i+1} ),$$
$$\lambda_{m}  = Q(\alpha_{1} , \dots  , \alpha_{m} , \alpha_{m+1} ).$$

<!-- PAGE 1097 -->
The expression $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$ ) is called the $i$-th difference quotient. Then, we can compute the $\lambda_{i}$  in terms of $\beta_{1}  = P(\alpha_{1}$ ), $\dots  , \beta_{m+1}  = P(\alpha_{m+1}$ ), using the inductive formulae for the $Q(\alpha_{1} , \dots  , \alpha_{i} , X)$ given above, initializing the $Q(\alpha_{i}$ ) such that $Q(\alpha_{i}$ ) $= \beta_{i}$ . The above method is called the method of divided differences and it is due to Newton. An astute observation may be used to optimize the computation. Observe that if $P_{i}(X)$ is the polynomial of degree $\le i$ taking the values $\beta_{1} , \dots  , \beta_{i+1}$  at the points $\alpha_{1} , \dots  , \alpha_{i+1}$ , then the coefficient of $X^{i}$ in $P_{i}(X)$ is $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$ ), which is the value of $\lambda_{i}$  in the Newton interpolant $P_{i}(X) = \lambda_{0}  + \lambda_{1} (X$ - $\alpha_{1}$ ) $+ \lambda_{2} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$ ) $+ \cdots  + \lambda_{i} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$ ) $\cdots  (X$ - $\alpha_{i}$ ). As a consequence, $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$ ) does not depend on the specific ordering of the $\alpha_{j}$ and there are better ways of computing it. For example, $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$ ) can be computed using
$$-$$
$$Q(\alpha_{1} , \dots  , \alpha_{i+1} ) = \frac{Q(\alpha_{2} , \dots  , \alpha_{i+1} )Q(\alpha_{1} , \dots  , \alpha_{i} )}{\alpha_{i+1}  -\alpha_{1}} .$$
Then, the computation can be arranged into a triangular array reminiscent of Pascal’s triangle, as follows: Initially, $Q(\alpha_{j}$ ) $= \beta_{j} , 1 \le j \le m + 1$, and
$$Q(\alpha_{1} )$$
$$Q(\alpha_{1} , \alpha_{2} )$$
$$Q(\alpha_{2} )Q(\alpha_{1} , \alpha_{2} , \alpha_{3} )$$
$$Q(\alpha_{2} , \alpha_{3} )\dots$$
$$Q(\alpha_{3} )Q(\alpha_{2} , \alpha_{3} , \alpha_{4} )$$
$$Q(\alpha_{3} , \alpha_{4} )\dots$$
$$Q(\alpha_{4} )\dots$$
$$\dots$$
In this computation, each successive column is obtained by forming the difference quotients of the preceeding column according to the formula
$$Q(\alpha_{k} , \dots  , \alpha_{i+k} ) = \frac{Q(\alpha_{k+1} , \dots  , \alpha_{i+k} )Q(\alpha_{k} , \dots  , \alpha_{i+k-1} )}{\alpha_{i+k}  -\alpha_{k}} -.$$
The $\lambda_{i}$  are the elements of the descending diagonal. Observe that if we performed the above computation starting with a polynomial Q(X) of degree $m$, we could extend it by considering new given points $\alpha_{m+2} , \alpha_{m+3}$ , etc. Then, from what we saw above, the $(m +$ 1)th column consists of $\lambda_{m}$  in the expression of Q(X) as a Newton interpolant and the $(m +$ 2)th column consists of zeros. Such divided differences are used in numerical analysis.

<!-- PAGE 1098 -->
Newton’s method can be used to compute the value $P(\alpha$ ) at some $\alpha$  of the interpolant P(X) taking the values $\beta_{1} , \dots  , \beta_{m+1}$  for the (distinct) arguments $\alpha_{1} , \dots  , \alpha_{m+1}$ . We also mention that inductive methods for computing $P(\alpha$ ) without first computing the coefficients of the Newton interpolant exist, for example, Aitken’s method. For this method, the reader is referred to Farin $[59]$. It has been observed that Lagrange interpolants oscillate quite badly as their degree increases, and thus, this makes them undesirable as a stable method for interpolation. A standard example due to Runge, is the function
$$f(x) = \frac{1}{1 + x^{2}} ,$$
in the interval $[-5, +5]$. Assuming a uniform distribution of points on the curve in the interval $[-5, +5]$, as the degree of the Lagrange interpolant increases, the interpolant shows wilder and wilder oscillations around the points $x = -5$ and $x = +5$. This phenomenon becomes quite noticeable beginning for degree $14$, and gets worse and worse. For degree $22$, things are quite bad! Equivalently, one may consider the function
$$f(x) = \frac{1}{1 + 25x^{2}} ,$$
in the interval $[-1, +1]$. We now consider a more general interpolation problem which will lead to the Hermite polynomials. We consider the following interpolation problem: Given a sequence $(\alpha_{1} , \dots  , \alpha_{m+1}$ ) of pairwise distinct scalars in $K$, integers $n_{1}, \dots  , n_{m+1}$ where $n_{j} \ge 0$, and $m + 1$ sequences $(\beta_{j}^{0}  , \dots  , \beta_{j}^{nj}$  ) of scalars in $K$, letting
$$n = n_{1} + \cdots  + n_{m+1} + m,$$
find a polynomial $P$ of degree $\le n$, such that
$$P(\alpha_{1} ) = \beta_{1}^{0} ,\dots P(\alpha_{m+1} ) = \beta_{m+1}^{0} ,$$
$$D^{1}P(\alpha_{1} ) = \beta_{1}^{1} ,\dots D^{1}P(\alpha_{m+1} ) = \beta_{m+1}^{1} ,$$
$$\dots$$
$$D^{i}P(\alpha_{1} ) = \beta_{1}^{i} ,\dots D^{i}P(\alpha_{m+1} ) = \beta_{m+1}^{i} ,$$
$$\dots$$
$$D^{n1}P(\alpha_{1} ) = \beta_{1}^{n1}  ,\dots D^{nm+1}P(\alpha_{m+1} ) = \beta_{m+1}^{nm+1}  .$$
Note that the above equations constitute $n + 1$ constraints, and thus, we can expect that there is a unique polynomial of degree $\le n$ satisfying the above problem. This is indeed the case and such a polynomial is called a Hermite polynomial. We call the above problem the Hermite interpolation problem.

<!-- PAGE 1099 -->

> **Proposition 30.29.** The Hermite interpolation problem has a unique solution of degree $\le n$, where $n = n_{1} + \cdots  + n_{m+1} + m$.

*Proof.* First, we prove that the Hermite interpolation problem has at most one solution. Assume that $P$ and $Q$ are two distinct solutions of degree $\le n$. Then, by Proposition 30.26 and the criterion following it, $P -Q$ has among its roots $\alpha_{1}$  of multiplicity at least $n_{1}+1, \dots , \alpha_{m+1}$  of multiplicity at least $n_{m+1} + 1$. However, by Theorem 30.23, we should have
$$n_{1} + 1 + \cdots  + n_{m+1} + 1 = n_{1} + \cdots  + n_{m+1} + m + 1 \le n,$$
which is a contradiction, since $n = n_{1} + \cdots  + n_{m+1} + m$. Thus, $P = Q$. We are left with proving the existence of a Hermite interpolant. A quick way to do so is to use Proposition 7.12, which tells us that given a square matrix $A$ over a field $K$, the following properties hold: For every column vector $B$, there is a unique column vector $X$ such that $AX = B$ iff the only solution to $AX = 0$ is the trivial vector $X = 0$ iff D(A) $\neq  0$. If we let $P = y_{0} + y_{1}X + \cdots  + y_{n}X^{n}$, the Hermite interpolation problem yields a linear system of equations in the unknowns $(y_{0}, \dots  , y_{n})$ with some associated $(n+1)\times (n+1)$ matrix $A$. Now, the system $AY = 0$ has a solution iff $P$ has among its roots $\alpha_{1}$  of multiplicity at least $n_{1} + 1, \dots , \alpha_{m+1}$  of multiplicity at least $n_{m+1} + 1$. By the previous argument, since $P$ has degree $\le n$, we must have $P = 0$, that is, $Y = 0$. This concludes the proof. Proposition 30.29 shows the existence of unique polynomials $H_{j}^{i}(X)$ of degree $\le n$ such that $D^{i}H_{j}^{i}(\alpha_{j}$ ) $= 1$ and $D^{k}H_{j}^{i}(\alpha_{l}$ ) $= 0$, for $k \neq  i$ or $l \neq  j, 1 \le j, l \le m + 1, 0 \le i, k \le n_{j}$. The polynomials $H_{j}^{i}$ are called Hermite basis polynomials. One problem with Proposition 30.29 is that it does not give an explicit way of computing the Hermite basis polynomials. We first show that this can be done explicitly in the special cases $n_{1} = \dots  = n_{m+1} = 1$, and $n_{1} = \dots  = n_{m+1} = 2$, and then suggest a method using a generalized Newton interpolant. Assume that $n_{1} = \dots  = n_{m+1} = 1$. We try $H_{j}^{0} =$ (a(X - $\alpha_{j}$ ) $+ b)L_{j}^{2}$, and $H_{j}^{1} =$ (c(X - $\alpha_{j}$ ) $+ d)L_{j}^{2}$, where $L_{j}$ is the Lagrange interpolant determined earlier. Since
$$DH_{j}^{0} = aL_{j}^{2} + 2(a(X -\alpha_{j} ) + b)L_{j}DL_{j},$$
requiring that $H_{j}^{0} (\alpha_{j}$ ) $= 1, H_{j}^{0} (\alpha_{k}$ ) $= 0, DH_{j}^{0} (\alpha_{j}$ ) $= 0$, and $DH_{j}^{0} (\alpha_{k}$ ) $= 0$, for $k \neq  j$, implies $b = 1$ and $a = -2DL_{j}(\alpha_{j}$ ). Similarly, from the requirements $H_{j}^{1} (\alpha_{j}$ ) $= 0, H_{j}^{1} (\alpha_{k}$ ) $= 0, DH_{j}^{1} (\alpha_{j}$ ) $= 1$, and $DH_{j}^{1} (\alpha_{k}$ ) $= 0, k \neq  j$, we get $c = 1$ and $d = 0$. Thus, we have the Hermite polynomials
$$H_{j}^{0} = (1 -2DL_{j}(\alpha_{j} )(X -\alpha_{j} ))L_{j}^{2},H_{j}^{1} = (X -\alpha_{j} )L_{j}^{2}.$$

<!-- PAGE 1100 -->
In the special case where $m = 1, \alpha_{1}  = 0$, and $\alpha_{2}  = 1$, we leave as an exercise to show that the Hermite polynomials are
$$- + 1$$
$$H_{0}^{0} = 2X^{3}3X^{2},$$
$$+ 3$$
$$H_{1}^{0} = -2X^{3}X^{2},$$
$$- +$$
$$H_{0}^{1} = X^{3}2X^{2} X,$$
$$-$$
$$H_{1}^{1} = X^{3}X^{2}.$$
As a consequence, the polynomial $P$ of degree $3$ such that P(0) $= x_{0}$, P(1) $= x_{1}$, P' $(0) = m_{0}$, and P' $(1) = m_{1}$, can be written as P(X) $= x_{0}(2X^{3}$ - $3X^{2} + 1) + m_{0}(X^{3}$ - $2X^{2} + X) + m_{1}(X^{3}$ - $X^{2}) + x_{1}(-2X^{3} + 3X^{2})$. If we want the polynomial $P$ of degree $3$ such that P(a) $= x_{0}$, P(b) $= x_{1}$, P' $(a) = m_{0}$, and P' $(b) = m_{1}$, where $b \neq$  a, then we have P(X) $= x_{0}(2t^{3}$ - $3t^{2} + 1) + (b$ - $a)m_{0}(t^{3}$ - $2t^{2} + t) + (b$ - $a)m_{1}(t^{3}$ - $t^{2}) + x_{1}(-2t^{3} + 3t^{2})$, where
$$t = \frac{Xa}{b -a} - .$$
Observe the presence of the extra factor $(b$ - $a)$ in front of $m_{0}$ and $m_{1}$, the formula would be false otherwise! We now consider the case where $n_{1} = \dots  = n_{m+1} = 2$. Let us try
$$+$$
$$H_{j}^{i}(X) = (a^{i}(X -\alpha_{j} )^{2} b^{i}(X -\alpha_{j} ) + c^{i})L_{j}^{3},$$
where $0 \le i \le 2$. Sparing the readers some (tedious) computations, we find:
$$H_{j}^{0} (X) = \begin{pmatrix}   & 3 \\ 6(DL_{j}(\alpha_{j} ))^{2}- & D^{2}L_{j}(\alpha_{j} ) \\ 2 \\ 9(DL_{j}(\alpha_{j} ))^{2}(X & \alpha_{j} )^{2} & 3D \end{pmatrix} \begin{pmatrix} (X-\alpha_{j} )^{2}-3DL_{j}(\alpha_{j} )(X-\alpha_{j} ) + 1 \end{pmatrix} L_{j}^{3}(X),$$
$$H_{j}^{1} (X) = \begin{pmatrix} - & - & L_{j}(\alpha_{j} )(X-\alpha_{j} ) \end{pmatrix} L_{j}^{3}(X),$$
$$H_{j}^{2} (X) = \frac{1}{2} (X -\alpha_{j} )^{2}L_{j}^{3}(X).$$
Going back to the general problem, it seems to us that a kind of Newton interpolant will be more manageable. Let $P_{0}^{0}  (X) = 1, \cdots P_{j}^{0} (X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{j} )^{nj+1}, 1 \le j \le m \cdots P_{0}^{i}(X) = (X$ - $\alpha_{1} )^{i}(X$ - $\alpha_{2} )^{n2+1}  (X$ - $\alpha_{m+1} )^{nm+1+1}, 1 \le i \le n_{1}, \cdots  \cdots P_{j}^{i}(X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{j} )^{nj+1}(X$ - $\alpha_{j+1} )^{i}(X$ - $\alpha_{j+2} )^{nj+2+1}  (X$ - $\alpha_{m+1} )^{nm+1+1}$,
$$1 \le j \le m -1, 1 \le i \le n_{j+1},$$
$\cdots P_{m}^{i}(X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{m} )^{nm+1}(X$ - $\alpha_{m+1} )^{i}, 1 \le i \le n_{m+1}$,

<!-- PAGE 1101 -->
and let
$$j=j+1$$
$$P(X) = \sum_{=0,i=0}^{m,i=n}  \lambda_{j}^{i} P_{j}^{i}(X).$$
$$j$$
We can think of P(X) as a generalized Newton interpolant. We can compute the derivatives $D^{k}P_{j}^{i}$ , for $1 \le k \le n_{j+1}$, and if we look for the Hermite basis polynomials $H_{j}^{i}(X)$ such that $D^{i}H_{j}^{i}(\alpha_{j}$ ) $= 1$ and $D^{k}H_{j}^{i}(\alpha_{l}$ ) $= 0$, for $k \neq  i$ or $l \neq  j, 1 \le j, l \le m + 1, 0 \le i, k \le n_{j}$, we find that we have to solve triangular systems of linear equations. Thus, as in the simple case $n_{1} = \dots  = n_{m+1} = 0$, we can solve successively for the $\lambda_{j}^{i}$ . Obviously, the computations are quite formidable and we leave such considerations for further study.

<!-- PAGE 1102 -->
