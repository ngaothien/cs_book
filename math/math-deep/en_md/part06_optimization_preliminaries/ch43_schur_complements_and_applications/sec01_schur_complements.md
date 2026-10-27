# Schur Complements


<!-- PAGE 1565 -->
Chapter $43$ Schur Complements and Applications Schur complements arise naturally in the process of inverting block matrices of the form
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$$
and in characterizing when symmetric versions of these matrices are positive definite or positive semidefinite. These characterizations come up in various quadratic optimization problems; see Boyd and Vandenberghe $[29]$, especially Appendix $B$. In the most general case, pseudo-inverses are also needed. In this chapter we introduce Schur complements and describe several interesting ways in which they are used. Along the way we provide some details and proofs of some results from Appendix A.5 (especially Section A.5.5) of Boyd and Vandenberghe $[29]$.

## 43.1 Schur Complements

Let $M$ be an $n \times  n$ matrix written as a $2 \times  2$ block matrix
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} ,$$
where $A$ is a $p \times  p$ matrix and $D$ is a $q \times  q$ matrix, with $n = p + q$ (so $B$ is a $p \times  q$ matrix and $C$ is a $q \times  p$ matrix). We can try to solve the linear system
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
that is,
$$Ax + By=c,$$
$$Cx + Dy=d,$$
$$1565$$

<!-- PAGE 1566 -->
by mimicking Gaussian elimination. If we assume that $D$ is invertible, then we first solve for $y$, getting
$$y = D^{-1}(d -Cx),$$
and after substituting this expression for $y$ in the first equation, we get
$$Ax + B(D^{-1}(d -Cx)) = c,$$
that is,
$$(A -BD^{-1}C)x = c -BD^{-1}d.$$
If the matrix $A$ - $BD^{-1}C$ is invertible, then we obtain the solution to our system
$$x = (A -BD^{-1}C)^{-1}(c -BD^{-1}d),$$
$$y = D^{-1}(d -C(A -BD^{-1}C)^{-1}(c -BD^{-1}d)).$$
If $A$ is invertible, then by eliminating $x$ first using the first equation, we obtain analogous formulas involving the matrix $D$ - $CA^{-1}B$. The above formulas suggest that the matrices $A$ - $BD^{-1}C$ and $D$ - $CA^{-1}B$ play a special role and suggest the following definition:

> **Definition 43.1.** Given any $n \times  n$ block matrix of the form
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} ,$$
where $A$ is a $p \times  p$ matrix and $D$ is a $q \times  q$ matrix, with $n = p + q$ (so $B$ is a $p \times  q$ matrix and $C$ is a $q \times  p$ matrix), if $D$ is invertible, then the matrix $A$ - $BD^{-1}C$ is called the Schur complement of $D$ in $M$. If $A$ is invertible, then the matrix $D$ - $CA^{-1}B$ is called the Schur complement of $A$ in $M$. The above equations written as
$$x = (A -BD^{-1}C)^{-1}c -(A -BD^{-1}C)^{-1}BD^{-1}d,$$
$$y = -D^{-1}C(A -BD^{-1}C)^{-1}c$$
$$+ (D^{-1}+ D^{-1}C(A -BD^{-1}C)^{-1}BD^{-1})d,$$
yield a formula for the inverse of $M$ in terms of the Schur complement of $D$ in $M$, namely
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & -(A -BD^{-1}C)^{-1}BD^{-1} \\ -D^{-1}C(A -BD^{-1}C)^{-1} & D^{-1}+ D^{-1}C(A -BD^{-1}C)^{-1}BD^{-1} \end{pmatrix} .$$
A moment of reflection reveals that
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & 0 \\ -D^{-1}C(A -BD^{-1}C)^{-1} & D^{-1} \end{pmatrix} \begin{pmatrix} I & -BD^{-1} \\ 0 & I \end{pmatrix} ,$$
and then
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} I & 0 \\ -D^{-1}C & I \end{pmatrix} \begin{pmatrix} (A -BD^{-1}C)^{-1} & 0 \\ 0 & D^{-1} \end{pmatrix} \begin{pmatrix} I & -BD^{-1} \\ 0 & I \end{pmatrix} .$$
By taking inverses, we obtain the following result.

<!-- PAGE 1567 -->

> **Proposition 43.1.** If the matrix $D$ is invertible, then
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & BD^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BD^{-1}C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1}C & I \end{pmatrix} .$$
The above expression can be checked directly and has the advantage of requiring only the invertibility of $D$.
Remark: If $A$ is invertible, then we can use the Schur complement $D$ - $CA^{-1}B$ of $A$ to obtain the following factorization of $M$:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & 0 \\ CA^{-1} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & D -CA^{-1}B \end{pmatrix} \begin{pmatrix} I & A^{-1}B \\ 0 & I \end{pmatrix} .$$
If $D$ - $CA^{-1}B$ is invertible, we can invert all three matrices above, and we get another formula for the inverse of $M$ in terms of $(D$ - $CA^{-1}B)$, namely,
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} A^{-1} + A^{-1}B(D -CA^{-1}B)^{-1}CA^{-1} & -A^{-1}B(D -CA^{-1}B)^{-1} \\ -(D -CA^{-1}B)^{-1}CA^{-1} & (D -CA^{-1}B)^{-1} \end{pmatrix} .$$
If $A, D$ and both Schur complements $A$ - $BD^{-1}C$ and $D$ - $CA^{-1}B$ are all invertible, by comparing the two expressions for $M^{-1}$ , we get the (non-obvious) formula
$$(A -BD^{-1}C)^{-1}= A^{-1}+ A^{-1}B(D -CA^{-1}B)^{-1}CA^{-1}.$$
Using this formula, we obtain another expression for the inverse of $M$ involving the Schur complements of $A$ and $D$ (see Horn and Johnson $[98])$:

> **Proposition 43.2.** If $A, D$ and both Schur complements $A$ - $BD^{-1}C$ and $D$ - $CA^{-1}B$ are all invertible, then
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & -A^{-1}B(D -CA^{-1}B)^{-1} \\ -(D -CA^{-1}B)^{-1}CA^{-1} & (D -CA^{-1}B)^{-1} \end{pmatrix} .$$
If we set $D =$ I and change $B$ to $-B$, we get
$$(A + BC)^{-1}= A^{-1}-A^{-1}B(I -CA^{-1}B)^{-1}CA^{-1},$$
a formula known as the matrix inversion lemma (see Boyd and Vandenberghe $[29]$, Appendix C.4, especially C.4.3).
