# Polar Form for Square Matrices


<!-- PAGE 757 -->

## 22.3 Polar Form for Square Matrices

A notion closely related to the SVD is the polar form of a matrix.

> **Definition 22.4.** A pair $(R, S)$ such that $A = RS$ with $R$ orthogonal and $S$ symmetric positive semidefinite is called a polar decomposition of $A$. Theorem 22.5 implies that for every real $n\times n$ matrix $A$, there is some orthogonal matrix $R$ and some positive semidefinite symmetric matrix $S$ such that
$$A = RS.$$
This is easy to show and we will prove it below. Furthermore, $R, S$ are unique if $A$ is invertible, but this is harder to prove; see Problem 22.9. For example, the matrix
$$A = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix}$$
$$--$$
is both orthogonal and symmetric, and $A = RS$ with $R = A$ and $S =$ I, which implies that some of the eigenvalues of $A$ are negative.
Remark: In the complex case, the polar decomposition states that for every complex $n \times  n$ matrix $A$, there is some unitary matrix $U$ and some positive semidefinite Hermitian matrix $H$ such that
$$A = UH.$$
It is easy to go from the polar form to the SVD, and conversely. Given an SVD $A = V D U^{\top}$ , let $R = V U^{\top}$ and $S = UD U^{\top}$ . It is clear that $R$ is orthogonal and that $S$ is positive semidefinite symmetric, and
$$RS = V U^{\top} UD U^{\top} = V D U^{\top} = A.$$

> **Example 22.5.** Recall from Example 22.4 that $A = V DU^{\top}$ where $V = I_{2}$ and
$$11!$$
$$\overline{\sqrt}\overline{\sqrt}$$
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} ,U =\overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21},D = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} .$$
$$\overline{2}$$
Set $R = V U^{\top} = U$ and
$$11!$$
$$\overline{\sqrt}\overline{\sqrt}$$
$$S = UDU^{\top} =\overline{2}\overline{2}.$$
$$\overline{\sqrt} 1\overline{\sqrt} 1$$
$$\overline{2}\overline{2}$$
$$\sqrt$$
Since $S =_{2}^{\sqrt1}A^{\top}A, S$ has eigenvalues $\overline{2}$ and $0$. We leave it to the reader to check that $A = RS$.

<!-- PAGE 758 -->
Going the other way, given a polar decomposition $A = R_{1}S$, where $R_{1}$ is orthogonal and $S$ is positive semidefinite symmetric, there is an orthogonal matrix $R_{2}$ and a positive semidefinite diagonal matrix $D$ such that $S = R_{2}D R_{2}^{\top}$ , and thus
$$A = R_{1}R_{2}D R_{2}^{\top} = V D U^{\top},$$
where $V = R_{1}R_{2}$ and $U = R_{2}$ are orthogonal.
$$Example 22.6. Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} and A = R_{1}S, where R_{1} = \begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} and S =$$
$$\begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & 1/ & 2 \end{pmatrix} . This is the polar decomposition of Example 22.5. Observe that$$
$$11! 11!$$
$$\overline{\sqrt}\overline{\sqrt}\overline{\sqrt}\overline{\sqrt}$$
$$S =\overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21} \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} \overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21}= R_{2}DR_{2}^{\top} .$$
$$\overline{2}\overline{2}$$
$$Set U = R_{2} and V = R_{1}R_{2} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} to obtain the SVD decomposition of Example 22.4.$$
The eigenvalues and the singular values of a matrix are typically not related in any obvious way. For example, the $n \times  n$ matrix
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix}$$
has the eigenvalue $1$ with multiplicity $n$, but its singular values, $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$ , which are the positive square roots of the eigenvalues of the matrix $B = A^{\top}A$ with
$$B = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 2 & 5 & 2 & 0 & \dots & 0 & 0 \\ 0 & 2 & 5 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 5 & 2 & 0 \\ 0 & 0 & \dots & 0 & 2 & 5 & 2 \\ 0 & 0 & \dots & 0 & 0 & 2 & 5 \end{pmatrix}$$
have a wide spread, since
$$\frac{\sigma_{1}}{\sigma_{n}} = cond_{2}(A) \ge 2^{n-1}.$$
