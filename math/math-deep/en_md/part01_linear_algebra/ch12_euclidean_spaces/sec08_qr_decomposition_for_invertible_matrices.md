# QR-Decomposition for Invertible Matrices


<!-- PAGE 487 -->

## 12.8 QR-Decomposition for Invertible Matrices

Now that we have the definition of an orthogonal matrix, we can explain how the Gram– Schmidt orthonormalization procedure immediately yields the QR-decomposition for matrices.

> **Definition 12.8.** Given any real $n \times  n$ matrix $A$, a QR-decomposition of $A$ is any pair of $n\times n$ matrices $(Q, R)$, where $Q$ is an orthogonal matrix and $R$ is an upper triangular matrix such that $A = QR$. Note that if $A$ is not invertible, then some diagonal entry in $R$ must be zero.

> **Proposition 12.16.** Given any real $n \times  n$ matrix $A$, if $A$ is invertible, then there is an orthogonal matrix $Q$ and an upper triangular matrix $R$ with positive diagonal entries such that $A = QR$.
$$\mathbb{E}^{n}$$

*Proof.* We can view the columns of $A$ as vectors $A^{1}, \dots  , A^{n}$ in . If $A$ is invertible, then they are linearly independent, and we can apply Proposition 12.10 to produce an orthonormal basis using the Gram–Schmidt orthonormalization procedure. Recall that we construct vectors $Q^{k}$ and $Q^{'k}$ as follows:
$$Q^{'1}= A^{1},Q^{1}= \frac{Q^{'1}}{\|Q^{'1}\|} ,$$
and for the inductive step
$$-$$
$$Q^{'k+1}= A^{k+1} \sum_{i=1}^{k}  (A^{k+1}\cdot  Q^{i}) Q^{i},Q^{k+1}= \frac{Q^{'k+1}}{\|Q^{'k+1}\|} ,$$
where $1 \le k \le n$ - $1$. If we express the vectors $A^{k}$ in terms of the $Q^{i}$ and $Q^{'i}$, we get the triangular system
$$A^{1}=\|Q^{'1}\|Q^{1},$$
$$\vdots$$
$$A^{j}=(A^{j}\cdot  Q^{1}) Q^{1}+ \cdots  + (A^{j}\cdot  Q^{i}) Q^{i}+ \cdots  + (A^{j}\cdot  Q^{j-1}) Q^{j-1}+ \|Q^{'j}\|Q^{j},$$
$$\vdots$$
$$A^{n}=(A^{n}\cdot  Q^{1}) Q^{1}+ \cdots  + (A^{n}\cdot  Q^{n-1}) Q^{n-1}+ \|Q^{'n}\|Q^{n}.$$
Letting $r_{k k} = \|Q^{'k}\|$, and $r_{i j} = A^{j} \cdot  Q^{i}$ (the reversal of $i$ and $j$ on the right-hand side is intentional!), where $1 \le k \le n, 2 \le j \le n$, and $1 \le i \le j$ - $1$, and letting $q_{i j}$ be the ith component of $Q^{j}$, we note that $a_{i j}$, the ith component of $A^{j}$, is given by
$$a_{i j} = r_{1j}q_{i1} + \cdots  + r_{i j}q_{i i} + \cdots  + r_{j j}q_{i j} = q_{i1}r_{1j} + \cdots  + q_{i i}r_{i j} + \cdots  + q_{i j}r_{j j}.$$
If we let $Q = (q_{i j})$, the matrix whose columns are the components of the $Q^{j}$, and $R = (r_{i j})$, the above equations show that $A = QR$, where $R$ is upper triangular. The diagonal entries
$$\cdot$$
$r_{k k} = \|Q^{'k}\| = A^{k}  Q^{k}$ are indeed positive.

<!-- PAGE 488 -->
The reader should try the above procedure on some concrete examples for $2\times 2$ and $3\times 3$ matrices.
Remarks:
$(1)$ Because the diagonal entries of $R$ are positive, it can be shown that $Q$ and $R$ are unique. More generally, if $A$ is invertible and if $A = Q_{1}R_{1} = Q_{2}R_{2}$ are two QR-decompositions for $A$, then
$$R_{1}R_{2}^{-1}= Q_{1}^{\top} Q_{2}.$$
The matrix $Q_{1}^{\top} Q_{2}$ is orthogonal and it is easy to see that $R_{1}R_{2}^{-1}$ is upper triangular. But an upper triangular matrix which is orthogonal must be a diagonal matrix $D$ with diagonal entries $\pm 1$, so $Q_{2} = Q_{1}D$ and $R_{1} = DR_{2}$.
$(2)$ The QR-decomposition holds even when $A$ is not invertible. In this case, $R$ has some zero on the diagonal. However, a different proof is needed. We will give a nice proof using Householder matrices (see Proposition 13.4, and also Strang $[175, 176]$, Golub and Van Loan $[83]$, Trefethen and Bau $[182]$, Demmel $[48]$, Kincaid and Cheney $[105]$, or Ciarlet $[41])$. For better numerical stability, it is preferable to use the modified Gram–Schmidt method to implement the QR-factorization method. Here is a Matlab program implementing QRfactorization using modified Gram–Schmidt. function [Q,R] $=$ qrv4(A) $n =$ size(A,1); for $i =$ 1:n Q(:,i) $=$ A(:,i); for $j =$ 1:i-1
$$R(j,i) = Q(:,j)’*Q(:,i);$$
$$Q(:,i) = Q(:,i) - R(j,i)*Q(:,j);$$
end R(i,i) $=$ sqrt(Q(:,i)’*Q(:,i)); Q(:,i) $= Q(:,i)/R(i,i)$; end end

> **Example 12.13.** Consider the matrix
$$A = \begin{pmatrix} 0 & 0 & 5 \\ 0 & 4 & 1 \\ 1 & 1 & 1 \end{pmatrix} .$$
To determine the QR-decomposition of $A$, we first use the Gram-Schmidt orthonormalization

<!-- PAGE 489 -->
procedure to calculate $Q = (Q^{1}Q^{2}Q^{3})$. By definition
$$A^{1} = Q^{'1} = Q^{1} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} ,$$
$$and since A^{2} = \begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} , we discover that$$
$$Q^{'2} = A^{2} -(A^{2} \cdot  Q^{1})Q^{1} = \begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix} .$$
$$Hence, Q^{2} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} . Finally,$$
$$Q^{'3} = A_{3} -(A^{3} \cdot  Q^{1})Q^{1} -(A^{3} \cdot  Q^{2})Q^{2} = \begin{pmatrix} 5 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix} ,$$
$$which implies that Q^{3} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} . According to Proposition 12.16, in order to determine R we$$
need to calculate
$$= 1$$
$$r_{11} =Q^{'1}r_{12} = A^{2}\cdot  Q^{1}= 1r_{13} = A^{3}\cdot  Q^{1}= 1$$
$$= 4$$
$$r_{22} =Q^{'2}r_{23} = A_{3} \cdot  Q^{2}= 1$$
$$r_{33} =

$Q^{'3}$

$=$ 5.$$
$$In summary, we have found that the QR-decomposition of A = \begin{pmatrix} 0 & 0 & 5 \\ 0 & 4 & 1 \\ 1 & 1 & 1 \end{pmatrix} is$$
$$Q = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} andR = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 4 & 1 \\ 0 & 0 & 5 \end{pmatrix} .$$

> **Example 12.14.** Another example of QR-decomposition is
$$A = \begin{pmatrix} 1 & 1 & 2 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} = \begin{pmatrix} \sqrt & \sqrt \\ 1/ & \overline{2} & 1/ & \overline{2} & 0 \\ 0\sqrt & 0\sqrt & 1 \\ 1/ & \overline{2} & 1/ & \overline{2} & 0 \end{pmatrix} \begin{pmatrix} \sqrt & \sqrt & \sqrt \\ \overline{2} & 1/\sqrt{2} & \sqrt{2} \\ 0 & 1/ & 2 & 2 \\ 0 & 0 & 1 \end{pmatrix} .$$
$$-$$

<!-- PAGE 490 -->

> **Example 12.15.** If we apply the above Matlab function to the matrix
$$A = \begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 \\ 0 & 1 & 4 & 1 & 0 \\ 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 1 & 4 \end{pmatrix} ,$$
we obtain
$$Q = \begin{pmatrix} 0.9701 & -0.2339 & 0.0619 & -0.0166 & 0.0046 \\ 0.2425 & 0.9354 & -0.2477 & 0.0663 & -0.0184 \\ 0 & 0.2650 & 0.9291 & -0.2486 & 0.0691 \\ 0 & 0 & 0.2677 & 0.9283 & -0.2581 \\ 0 & 0 & 0 & 0.2679 & 0.9634 \end{pmatrix}$$
and
$$R = \begin{pmatrix} 4.1231 & 1.9403 & 0.2425 & 0 & 0 \\ 0 & 3.7730 & 1.9956 & 0.2650 & 0 \\ 0 & 0 & 3.7361 & 1.9997 & 0.2677 \\ 0 & 0 & 073.7324 & 2.0000 \\ 0 & 0 & 0 & 0 & 3.5956 \end{pmatrix} .$$
Remark: The Matlab function qr, called by $[Q, R] =$ qr(A), does not necessarily return an upper-triangular matrix whose diagonal entries are positive. The QR-decomposition yields a rather efficient and numerically stable method for solving systems of linear equations. Indeed, given a system Ax $= b$, where $A$ is an $n \times  n$ invertible matrix, writing $A = QR$, since $Q$ is orthogonal, we get
$$Rx = Q^{\top}b,$$
and since $R$ is upper triangular, we can solve it by Gaussian elimination, by solving for the last variable $x_{n}$ first, substituting its value into the system, then solving for $x_{n-1}$, etc. The QR-decomposition is also very useful in solving least squares problems (we will come back to this in Chapter $23)$, and for finding eigenvalues; see Chapter $18$. It can be easily adapted to the case where $A$ is a rectangular $m\times n$ matrix with independent columns (thus, $n \le m)$. In this case, $Q$ is not quite orthogonal. It is an $m \times  n$ matrix whose columns are orthogonal, and $R$ is an invertible $n\times n$ upper triangular matrix with positive diagonal entries. For more on QR, see Strang $[175, 176]$, Golub and Van Loan $[83]$, Demmel $[48]$, Trefethen and Bau $[182]$, or Serre $[162]$. A somewhat surprising consequence of the QR-decomposition is a famous determinantal inequality due to Hadamard.

<!-- PAGE 491 -->

> **Proposition 12.17.** (Hadamard) For any real $n \times  n$ matrix $A = (a_{ij})$, we have
$$1/21/2$$
$$| \det(A)| \le \prod_{i=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{j=1}^{n}  and| \det(A)| \le \prod_{j=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
Moreover, equality holds iff either $A$ has orthogonal rows in the left inequality or orthogonal columns in the right inequality.

*Proof.* If det(A) $= 0$, then the inequality is trivial. In addition, if the righthand side is also $0$, then either some column or some row is zero. If det(A) $\neq  0$, then we can factor $A$ as $A = QR$, with $Q$ is orthogonal and $R = (r_{ij})$ upper triangular with positive diagonal entries. Then since $Q$ is orthogonal det(Q) $= \pm 1$, so
$$| \det(A)| = | \det(Q)| | \det(R)| = \prod_{j=1}  r_{jj}.$$
Now as $Q$ is orthogonal, it preserves the Euclidean norm, so
$$\sum_{i=1}^{n}  a_{ij}^{2} =

$A_{2}^{j2}$

$=$

$QR_{2}^{j2}$

$=$

$R_{2}^{j2}$

$= \sum_{i=1}^{n}  r_{ij}^{2} \ge r_{jj}^{2},$$$ which implies that
$$1/2$$
$$| \det(A)| = \prod_{j=1}^{n}  r_{jj} \le \prod_{j=1}^{n}  R_{2}^{j}

$= \prod_{j=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}$  .$$ The other inequality is obtained by replacing $A$ by $A^{\top}$. Finally, if det(A) $\neq  0$ and equality holds, then we must have
$$r_{jj} =

$A_{2}^{j}$

$,1 \le j \le$ n,$$ which can only occur if $A$ has orthogonal columns. Another version of Hadamard’s inequality applies to symmetric positive semidefinite matrices.

> **Proposition 12.18.** (Hadamard) For any real $n \times  n$ matrix $A = (a_{ij})$, if $A$ is symmetric positive semidefinite, then we have
$$\det(A) \le \prod_{i=1}^{n}  a_{ii}.$$
Moreover, if $A$ is positive definite, then equality holds iff $A$ is a diagonal matrix.
