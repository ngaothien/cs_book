# Determinant of a Linear Map


<!-- PAGE 241 -->

*Proof.* $(1)$ Assume that Ax $= b$ has a single solution $x_{0}$, and assume that Ay $= 0$ with $y \neq  0$. Then,
$$A(x_{0} + y) = Ax_{0} + Ay = Ax_{0} + 0 = b,$$
and $x_{0} + y \neq  x_{0}$ is another solution of Ax $= b$, contradicting the hypothesis that Ax $= b$ has a single solution $x_{0}$. Thus, Ax $= 0$ only has the trivial solution. Now assume that Ax $= 0$ only has the trivial solution. This means that the columns $A^{1}, \dots  , A^{n}$ of $A$ are linearly independent, and by Proposition 7.11, we have det(A)̸ $= 0$. Finally, if det(A)̸ $= 0$, by Proposition 7.10, this means that $A$ is invertible, and then for every $b$, Ax $= b$ is equivalent to $x = A^{-1}b$, which shows that Ax $= b$ has a single solution.
$(2)$ Assume that Ax $= b$. If we compute
$$\det(A^{1}, \dots  , x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}, \dots  , A^{n}) = \det(A^{1}, \dots  , b, \dots  , A^{n}),$$
where $b$ occurs in the $j$-th position, by multilinearity, all terms containing two identical columns $A^{k}$ for $k \neq  j$ vanish, and we get
$$x_{j} \det(A^{1}, \dots  , A^{n}) = \det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n}),$$
for every $j, 1 \le j \le n$. Since we assumed that det(A) $= det(A^{1}, \dots  , A^{n}) \neq  0$, we get the desired expression.
$(3)$ Note that Ax $= 0$ has a nonzero solution iff $A^{1}, \dots  , A^{n}$ are linearly dependent (as observed in the proof of Proposition 7.11), which, by Proposition 7.11, is equivalent to det(A) $= 0$. As pleasing as Cramer’s rules are, it is usually impractical to solve systems of linear equations using the above expressions. However, these formula imply an interesting fact, which is that the solution of the system Ax $= b$ are continuous in $A$ and $b$. If we assume that the entries in $A$ are continuous functions $a_{ij}(t)$ and the entries in $b$ are are also continuous functions $b_{j}(t)$ of a real parameter $t$, since determinants are polynomial functions of their entries, the expressions
$$x_{j}(t) = \frac{\det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n})}{\det(A^{1}, \dots  , A^{j-1}, A^{j}, A^{j+1}, \dots  , A^{n})}$$
are ratios of polynomials, and thus are also continuous as long as det(A(t)) is nonzero. Similarly, if the functions $a_{ij}(t)$ and $b_{j}(t)$ are differentiable, so are the $x_{j}(t)$.

## 7.6 Determinant of a Linear Map

Given a vector space $E$ of finite dimension $n$, given a basis $(u_{1}, \dots  , u_{n})$ of $E$, for every linear map $f$ : $E \to E$, if M(f) is the matrix of $f$ w.r.t. the basis $(u_{1}, \dots  , u_{n})$, we can define det(f) $=$ det(M(f)). If $(v_{1}, \dots  , v_{n})$ is any other basis of $E$, and if $P$ is the change of basis
