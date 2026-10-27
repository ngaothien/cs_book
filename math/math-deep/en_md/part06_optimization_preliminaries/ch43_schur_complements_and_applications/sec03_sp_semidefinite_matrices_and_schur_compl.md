# SP Semidefinite Matrices and Schur Complements


<!-- PAGE 1569 -->
Another version of Proposition 43.3 using the Schur complement of $A$ instead of the Schur complement of $C$ also holds. The proof uses the factorization of $M$ using the Schur complement of $A$ (see Section 43.1).

> **Proposition 43.4.** For any symmetric matrix $M$ of the form
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} ,$$
if $A$ is invertible then the following properties hold:
$(1) M$ ≻ $0$ iff $A$ ≻ $0$ and $C$ - $B^{\top}A^{-1}B$ ≻ $0$.
$(2)$ If $A$ ≻ $0$, then $M$ ⪰ $0$ iff $C$ - $B^{\top}A^{-1}B$ ⪰ $0$. Here is an illustration of Proposition 43.4(2). Consider the nonlinear quadratic constraint
$$(Ax + b)^{\top}(Ax + b) \le c^{\top}x + d,$$
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}$$
were $A \in M_{n}($ ), $x, b, c \in$ and $d \in$ . Since obviously $I = I_{n}$ is invertible and I ≻ $0$, we have
$$\begin{pmatrix} I & Ax + b \\ (Ax + b)^{\top} & c^{\top}x + d \end{pmatrix} ⪰0$$
iff $c^{\top}x + d$ - (Ax $+ b)^{\top}(Ax + b)$ ⪰ $0$ iff(Ax $+ b)^{\top}(Ax + b) \le c^{\top}x + d$, since the matrix (a scalar) $c^{\top}x + d$ - (Ax $+ b)^{\top}(Ax + b)$ is the Schur complement of I in the above matrix. The trick of using Schur complements to convert nonlinear inequality constraints into linear constraints on symmetric matrices involving the semidefinite ordering ⪰ is used extensively to convert nonlinear problems into semidefinite programs; see Boyd and Vandenberghe $[29]$. When $C$ is singular (or $A$ is singular), it is still possible to characterize when a symmetric matrix $M$ as above is positive semidefinite, but this requires using a version of the Schur complement involving the pseudo-inverse of $C$, namely $A$ - $BC^{+}B^{\top}$ (or the Schur complement, $C$ - $B^{\top}A^{+}B$, of $A)$. We use the criterion of Proposition 42.5, which tells us when a quadratic function of the $form_{2}^{1} x^{\top}Px$ - $x^{\top}b$ has a minimum and what this optimum value is (where $P$ is a symmetric matrix).

## 43.3 Symmetric Positive Semidefinite Matrices and

$$Schur Complements$$
We now return to our original problem, characterizing when a symmetric matrix
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix}$$

<!-- PAGE 1570 -->
is positive semidefinite. Thus, we want to know when the function
$$f(x, y) = (x^{\top}y^{\top}) \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = x^{\top}Ax + 2x^{\top}By + y^{\top}Cy$$
has a minimum with respect to both $x$ and $y$. If we hold $y$ constant, Proposition 42.5 implies that f(x, $y)$ has a minimum iff $A$ ⪰ $0$ and (I - $AA^{+})By = 0$, and then the minimum value is
$$f(x^{*}, y) = -y^{\top}B^{\top}A^{+}By + y^{\top}Cy = y^{\top}(C -B^{\top}A^{+}B)y.$$
Since we want f(x, $y)$ to be uniformly bounded from below for all $x, y$, we must have (I - $AA^{+})B = 0$. Now $f(x^{*}, y)$ has a minimum iff $C$ - $B^{\top}A^{+}B$ ⪰ $0$. Therefore, we have established that f(x, $y)$ has a minimum over all $x, y$ iff
$$A ⪰0,(I -AA^{+})B = 0,C -B^{\top}A^{+}B ⪰0.$$
Similar reasoning applies if we first minimize with respect to $y$ and then with respect to $x$, but this time, the Schur complement $A$ - $BC^{+}B^{\top}$ of $C$ is involved. Putting all these facts together, we get our main result:

> **Theorem 43.5.** Given any symmetric matrix
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix}$$
the following conditions are equivalent:
$(1) M$ ⪰ $0 (M$ is positive semidefinite).
$(2) A$ ⪰ $0$, (I - $AA^{+})B = 0, C$ - $B^{\top}A^{+}B$ ⪰ $0$.
$(3) C$ ⪰ $0$, (I - $CC^{+})B^{\top} = 0, A$ - $BC^{+}B^{\top}$ ⪰ $0$. If $M$ ⪰ $0$ as in Theorem 43.5, then it is easy to check that we have the following factorizations (using the fact that $A^{+}AA^{+} = A^{+}$ and $C^{+}CC^{+} = C^{+})$:
$$\begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & BC^{+} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BC^{+}B^{\top} & 0 \\ 0 & C \end{pmatrix} \begin{pmatrix} I & 0 \\ C^{+}B^{\top} & I \end{pmatrix}$$
and
$$\begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & 0 \\ B^{\top}A^{+} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & C -B^{\top}A^{+}B \end{pmatrix} \begin{pmatrix} I & A^{+}B \\ 0 & I \end{pmatrix} .$$
