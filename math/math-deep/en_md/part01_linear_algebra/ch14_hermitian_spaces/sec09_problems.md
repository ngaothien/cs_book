# Problems


<!-- PAGE 564 -->

## 14.9 Problems

Problem 14.1. Let $(E, \langle$ -, $-\rangle$ ) be a Hermitian space of finite dimension. Prove that if $f$ : $E \to E$ is a self-adjoint linear map (that is, $f^{*} = f)$, then $\langle$ f(x), $x\rangle \in \mathbb{R}$ for all $x \in E$.
Problem 14.2. Prove the polarization identities of Proposition 14.1.
Problem 14.3. Let $E$ be a real Euclidean space. Give an example of a nonzero linear map $f$ : $E \to E$ such that $\langle$ f(u), $u\rangle = 0$ for all $u \in E$.
Problem 14.4. Prove Proposition 14.9.
Problem 14.5. $(1)$ Prove that every matrix in SU(2) is of the form
$$\mathbb{R}$$
$$A = \begin{pmatrix} a + ib & c + id \\ -c + id & a -ib \end{pmatrix} ,a^{2}+ b^{2}+ c^{2}+ d^{2}= 1, a, b, c, d \in ,$$
$(2)$ Prove that the matrices
$$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} , \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} , \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} , \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$$
all belong to SU(2) and are linearly independent over $\mathbb{C}$.
$(3)$ Prove that the linear span of SU(2) over $\mathbb{C}$ is the complex vector space $M_{2}(\mathbb{C})$ of all complex $2 \times  2$ matrices.
Problem 14.6. The purpose of this problem is to prove that the linear span of SU(n) over $\mathbb{C}$ is $M_{n}(\mathbb{C})$ for all $n \ge 3$. One way to prove this result is to adapt the method of Problem 12.12, so please review this problem. Every complex matrix $A \in M_{n}(\mathbb{C})$ can be written as
$$-$$
$$A = \frac{A + A^{*}}{2} + \frac{AA^{*}}{2}$$
where the first matrix is Hermitian and the second matrix is skew-Hermitian. Observe that if $A = (z_{ij})$ is a Hermitian matrix, that is $A^{*} = A$, then $z_{ji} = \overline{z}_{ij}$, so if $z_{ij} = a_{ij} + ib_{ij}$ with $a_{ij}, b_{ij} \in \mathbb{R}$, then $a_{ij} = a_{ji}$ and $b_{ij} = -b_{ji}$. On the other hand, if $A = (z_{ij})$ is a skew-Hermitian matrix, that is $A^{*} = -A$, then $z_{ji} = -\overline{z}_{ij}$, so $a_{ij} = -a_{ji}$ and $b_{ij} = b_{ji}$. The Hermitian and the skew-Hermitian matrices do not form complex vector spaces because they are not closed under multiplication by a complex number, but we can get around this problem by treating the real part and the complex part of these matrices separately and using multiplication by reals.

<!-- PAGE 565 -->
$(1)$ Consider the matrices of the form
$$R_{c}^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & i \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ i & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Prove that $(R_{c}^{i,j} )^{*}R_{c}^{i,j} =$ I and $det(R_{c}^{i,j}$ ) $= +1$. Use the matrices $R^{i,j}, R_{c}^{i,j} \in$ SU(n) and the matrices $(R^{i,j}-(R^{i,j})^{*})/2$ (from Problem 12.12) to form the real part of a skew-Hermitian matrix and the matrices $(R_{c}^{i,j}$ - $(R_{c}^{i,j} )^{*})/2$ to form the imaginary part of a skew-Hermitian matrix. Deduce that the matrices in SU(n) span all skew-Hermitian matrices.
$(2)$ Consider matrices of the form Type $1$
$$S_{c}^{1,2}= \begin{pmatrix} 0 & -i & 0 & 0 & \dots & 0 \\ i & 0 & 0 & 0 & \dots & 0 \\ 0 & 0 & -1 & 0 & \dots & 0 \\ 0 & 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \dots & 1 \end{pmatrix} .$$
Type $2$
$$S_{c}^{i,i+1}= \begin{pmatrix} -1 \\ 1 \\ \ddots \\ 1 \\ 0 & -i \\ i & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$

<!-- PAGE 566 -->
Type $3$
$$S_{c}^{i,j}= \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & -i \\ 0 & -1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ i & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Prove that $S^{i,j}, S_{c}^{i,j} \in$ SU(n), and using diagonal matrices as in Problem 12.12, prove that the matrices $S^{i,j}$ can be used to form the real part of a Hermitian matrix and the matrices $S_{c}^{i,j}$ can be used to form the imaginary part of a Hermitian matrix.
$(3)$ Use $(1)$ and $(2)$ to prove that the matrices in SU(n) span all Hermitian matrices. It follows that SU(n) spans $M_{n}(\mathbb{C})$ for $n \ge 3$.
Problem 14.7. Consider the complex matrix
$$A = \begin{pmatrix} i & 1 \\ 1 & -i \end{pmatrix} .$$
Check that this matrix is symmetric but not Hermitian. Prove that
$$\det(\lambda I -A) = \lambda^{2} ,$$
and so the eigenvalues of $A$ are $0, 0$.
Problem 14.8. Let $(E, \langle$ -, $-\rangle$ ) be a Hermitian space of finite dimension and let $f$ : $E \to E$ be a linear map. Prove that the following conditions are equivalent.
$(1) f \circ f^{*} = f^{*} \circ f (f$ is normal).
$(2) \langle$ f(x), $f(y)\rangle = \langle f^{*} (x), f^{*} (y)\rangle$ for all $x, y \in E$.
$(3) \|f(x)\| = \|f^{*} (x)\|$ for all $x \in E$.
$(4)$ The map $f$ can be diagonalized with respect to an orthonormal basis of eigenvectors.
$(5)$ There exist some linear maps $g, h: E \to E$ such that, $g = g^{*}, \langle x, g(x)\rangle \ge 0$ for all $x \in E, h^{-1} = h^{*}$, and $f = g \circ h = h \circ g$.
$(6)$ There exist some linear map $h: E \to E$ such that $h^{-1} = h^{*}$ and $f^{*} = h \circ f$.

<!-- PAGE 567 -->
$(7)$ There is a polynomial $P$ (with complex coefficients) such that $f^{*} =$ P(f).
Problem 14.9. Recall from Problem 13.7 that a complex $n\times n$ matrix $H$ is upper Hessenberg if $h_{jk} = 0$ for all $(j, k)$ such that $j$ - $k \ge 0$. Adapt the proof of Problem 13.7 to prove that given any complex $n \times n$-matrix $A$, there are $n$ - $2 \ge 1$ complex matrices $H_{1}, \dots  , H_{n-2}$, Householder matrices or the identity, such that
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
is upper Hessenberg.
Problem 14.10. Prove that all $y \in \mathbb{C}^{n}$,
$$\|y\|_{1}^{D} = \|y\|_{\infty}$$
$$\|y\|_{\infty}^{D}= \|y\|_{1}$$
$$\|y\|_{2}^{D} = \|y\|_{2} .$$
Problem 14.11. The purpose of this problem is to complete each of the matrices $A_{0}, B_{0}, C_{0}$ of Section 14.7 to a matrix $A$ in such way that the nuclear norm $\|A\|_{N}$ is minimized.
$(1)$ Prove that the squares $\sigma_{1}^{2}$  and $\sigma_{2}^{2}$  of the singular values of
$$A = \begin{pmatrix} 1 & 2 \\ c & d \end{pmatrix}$$
are the zeros of the equation
$$\lambda^{2} -(5 + c^{2}+ d^{2})\lambda  + (2c -d)^{2}= 0.$$
$(2)$ Using the fact that
$$q$$
$$\|A\|_{N} = \sigma_{1}  + \sigma_{2}  =\sigma_{1}^{2}  + \sigma_{2}^{2}  + 2\sigma_{1} \sigma_{2} ,$$
prove that
$$+ + 2$$
$$\|A\|_{N}^{2} = 5 + c^{2} d^{2}|2c -d|.$$
Consider the cases where 2c - $d \ge 0$ and 2c - $d \le 0$, and show that in both cases we must have $c =$ -2d, and that the minimum of f(c, $d) = 5 + c^{2} + d^{2} +$ 2|2c - d| is achieved by $c = d = 0$. Conclude that the matrix $A$ completing $A_{0}$ that minimizes $\|A\|_{N}$ is
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} .$$
$(3)$ Prove that the squares $\sigma_{1}^{2}$  and $\sigma_{2}^{2}$  of the singular values of
$$A = \begin{pmatrix} 1 & b \\ c & 4 \end{pmatrix}$$

<!-- PAGE 568 -->
are the zeros of the equation
$$\lambda^{2} -(17 + b^{2}+ c^{2})\lambda  + (4 -bc)^{2}= 0.$$
$(4)$ Prove that
$$+ + 2$$
$$\|A\|_{N}^{2} = 17 + b^{2} c^{2}|4 -bc|.$$
Consider the cases where $4$ - bc $\ge 0$ and $4$ - bc $\le 0$, and show that in both cases we must have $b^{2} = c^{2}$. Then show that the minimum of f(c, $d) = 17+b^{2}+c^{2}+2|4-bc|$ is achieved by $b = c$ with $-2 \le b \le 2$. Conclude that the matrices $A$ completing $B_{0}$ that minimize $\|A\|_{N}$ are given by
$$A = \begin{pmatrix} 1 & b \\ b & 4 \end{pmatrix} ,-2 \le b \le 2.$$
$(5)$ Prove that the squares $\sigma_{1}^{2}$  and $\sigma_{2}^{2}$  of the singular values of
$$A = \begin{pmatrix} 1 & 2 \\ 3 & d \end{pmatrix}$$
are the zeros of the equation
$$\lambda^{2} -(14 + d^{2})\lambda  + (6 -d)^{2}= 0$$
$(6)$ Prove that
$$+ 2$$
$$\|A\|_{N}^{2} = 14 + d^{2}|6 -d|.$$
Consider the cases where $6$ - $d \ge 0$ and $6$ - $d \le 0$, and show that the minimum of f(c, $d) = 14 + d^{2} +$ 2|6 - d| is achieved by $d = 1$. Conclude that the the matrix $A$ completing $C_{0}$ that minimizes $\|A\|_{N}$ is given by
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} .$$
Problem 14.12. Prove Theorem 14.32 when $E$ is a finite-dimensional Hermitian space.
