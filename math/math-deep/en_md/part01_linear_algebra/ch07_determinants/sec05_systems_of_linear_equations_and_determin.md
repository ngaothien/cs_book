# Systems of Linear Equations and Determinants


<!-- PAGE 239 -->
and we have
$$\begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} = 24 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
$$--$$
with det(A) $= 24$. When $K$ is a field, an element $a \in K$ is invertible iff $a \neq  0$. In this case, the second part of the proposition can be stated as $A$ is invertible iff det(A) $\neq  0$. Note in passing that this method of computing the inverse of a matrix is usually not practical.

## 7.5 Systems of Linear Equations and Determinants

We now consider some applications of determinants to linear independence and to solving systems of linear equations. Although these results hold for matrices over certain rings, their proofs require more sophisticated methods. Therefore, we assume again that $K$ is a field (usually, $K =\mathbb{R}$ or $K =\mathbb{C})$. Let $A$ be an $n \times n$-matrix, $x$ a column vectors of variables, and $b$ another column vector, and let $A^{1}, \dots  , A^{n}$ denote the columns of $A$. Observe that the system of equations Ax $= b$,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{n} \end{pmatrix}$$
is equivalent to
$$x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}= b,$$
since the equation corresponding to the $i$-th row is in both cases
$$a_{i1}x_{1} + \cdots  + a_{i j}x_{j} + \cdots  + a_{i n}x_{n} = b_{i}.$$
First we characterize linear independence of the column vectors of a matrix $A$ in terms of its determinant.

> **Proposition 7.11.** Given an $n \times n$-matrix $A$ over a field $K$, the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly dependent iff det(A) $= det(A^{1}, \dots  , A^{n}) = 0$. Equivalently, $A$ has rank $n$ iff det(A) $\neq  0$.

*Proof.* First assume that the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly dependent. Then there are $x_{1}, \dots  , x_{n} \in K$, such that
$$x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}= 0,$$

<!-- PAGE 240 -->
where $x_{j} \neq  0$ for some $j$. If we compute $det(A^{1}, \dots  , x_{1}A^{1} + \cdots  + x_{j}A^{j} + \cdots  + x_{n}A^{n}, \dots  , A^{n}) = det(A^{1}, \dots  , 0, \dots  , A^{n}) = 0$, where $0$ occurs in the $j$-th position. By multilinearity, all terms containing two identical columns $A^{k}$ for $k \neq  j$ vanish, and we get
$$\det(A^{1}, \dots  , x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}, \dots  , A^{n}) = x_{j} \det(A^{1}, \dots  , A^{n}) = 0.$$
Since $x_{j} \neq  0$ and $K$ is a field, we must have $det(A^{1}, \dots  , A^{n}) = 0$. Conversely, we show that if the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly independent, then $det(A^{1}, \dots  , A^{n})̸ = 0$. If the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly independent, then they form a basis of $K^{n}$, and we can express the standard basis $(e_{1}, \dots  , e_{n})$ of $K^{n}$ in terms of $A^{1}, \dots  , A^{n}$. Thus, we have
$$\begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1n} \\ b_{2 1} & b_{2 2} & \dots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{n n} \end{pmatrix} \begin{pmatrix} A^{1} \\ A^{2} \\ \vdots \\ A^{n} \end{pmatrix} ,$$
for some matrix $B = (b_{i j})$, and by Proposition 7.8, we get
$$\det(e_{1}, \dots  , e_{n}) = \det(B) \det(A^{1}, \dots  , A^{n}),$$
and since $det(e_{1}, \dots  , e_{n}) = 1$, this implies that $det(A^{1}, \dots  , A^{n}) \neq  0$ (and det(B) $\neq  0)$. For the second assertion, recall that the rank of a matrix is equal to the maximum number of linearly independent columns, and the conclusion is clear. We now characterize when a system of linear equations of the form Ax $= b$ has a unique solution.

> **Proposition 7.12.** Given an $n \times n$-matrix $A$ over a field $K$, the following properties hold:
$(1)$ For every column vector $b$, there is a unique column vector $x$ such that Ax $= b$ iff the only solution to Ax $= 0$ is the trivial vector $x = 0$, iff det(A) $\neq  0$.
$(2)$ If det(A) $\neq  0$, the unique solution of Ax $= b$ is given by the expressions
$$x_{j} = \frac{\det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n})}{\det(A^{1}, \dots  , A^{j-1}, A^{j}, A^{j+1}, \dots  , A^{n})} ,$$
known as Cramer’s rules.
$(3)$ The system of linear equations Ax $= 0$ has a nonzero solution iff det(A) $= 0$.
