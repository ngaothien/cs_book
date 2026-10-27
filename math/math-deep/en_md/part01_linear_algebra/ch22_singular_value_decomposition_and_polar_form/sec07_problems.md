# Problems


<!-- PAGE 764 -->

## 22.6 Summary

The main concepts and results of this chapter are listed below: $\bullet$  For any linear map $f$ : $E \to E$ on a Euclidean space $E$, the maps $f^{*} \circ f$ and $f \circ f^{*}$ are self-adjoint and positive semidefinite. $\bullet$  The singular values of a linear map. $\bullet$  Positive semidefinite and positive definite self-adjoint maps. $\bullet$  Relationships between Im $f$, Ker $f$, Im $f^{*}$ , and Ker $f^{*}$ . $\bullet$  The singular value decomposition theorem for square matrices (Theorem 22.5). $\bullet$  The SVD of matrix. $\bullet$  The polar decomposition of a matrix. $\bullet$  The Weyl inequalities. $\bullet$  The singular value decomposition theorem for $m \times  n$ matrices (Theorem 22.7). $\bullet$  Ky Fan k-norms, Ky Fan p-k-norms, Schatten p-norms.

## 22.7 Problems

Problem 22.1. $(1)$ Let $A$ be a real $n\times n$ matrix and consider the $(2n)\times$ (2n) real symmetric matrix
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix} .$$
Suppose that $A$ has rank $r$. If $A = V \Sigma U^{\top}$ is an SVD for $A$, with $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$ ) and $\sigma_{1}  \ge \cdots  \ge \sigma_{r}  > 0$, denoting the columns of $U$ by $u_{k}$ and the columns of $V$ by $v_{k}$, prove that
$$\sigma_{k}  is an eigenvalue of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ u_{k} \end{pmatrix} for k = 1, \dots  , n, and that -\sigma_{k}$$
$$is an eigenvalue of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ -u_{k} \end{pmatrix} for k = 1, \dots  , n.$$
Hint. We have $Au_{k} = \sigma_{k} v_{k}$ for $k = 1, \dots  , n$. Show that $A^{\top}v_{k} = \sigma_{k} u_{k}$ for $k = 1, \dots  , n$.
$(2)$ Prove that the 2n eigenvectors of $S$ in $(1)$ are pairwise orthogonal. Check that if $A$ has rank $r$, then $S$ has rank 2r.
$(3)$ Now assume that $A$ is a real $m \times  n$ matrix and consider the $(m + n) \times  (m + n)$ real symmetric matrix
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix} .$$

<!-- PAGE 765 -->
Suppose that $A$ has rank $r$. If $A = V \Sigma U^{\top}$ is an SVD for $A$, prove that $\sigma_{k}$  is an eigenvalue
$$of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ u_{k} \end{pmatrix} for k = 1, \dots  , r, and that -\sigma_{k}  is an eigenvalue of$$
$$S with corresponding eigenvector \begin{pmatrix} v_{k} \\ -u_{k} \end{pmatrix} for k = 1, \dots  , r.$$
Find the remaining $m + n$ - 2r eigenvectors of $S$ associated with the eigenvalue $0$.
$(4)$ Prove that these $m + n$ eigenvectors of $S$ are pairwise orthogonal.
Problem 22.2. Let $A$ be a real $m \times  n$ matrix of rank $r$.
$(1)$ Consider the $(m + n) \times  (m + n)$ real symmetric matrix
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix}$$
and prove that
$$\begin{pmatrix} I_{m} & z^{-1}A \\ 0 & I_{n} \end{pmatrix} \begin{pmatrix} zI \\ -A \\ -^{m}A^{\top} & zI_{n} \end{pmatrix} = \begin{pmatrix} zI_{m} -z^{-1}AA^{\top} & 0 \\ -A^{\top} & zI_{n} \end{pmatrix} .(*)$$
Use the Equation (*) to prove that if if $n \ge m$, then
$$\det(zI_{m+n} -S) = z^{n-m}\det(z^{2}I_{m} -AA^{\top}).$$
Permute the two matrices on the lefthand side of Equation (*) to obtain another equation and use this equation to prove that if $m \ge n$, then
$$\det(zI_{m+n} -S) = z^{m-n}\det(z^{2}I_{n} -A^{\top}A).$$
$(2)$ Prove that the eigenvalues of $S$ are $\pm \sigma_{1} , \dots  , \pm \sigma_{r}$ , with $m + n$ - 2r additional zeros.
Problem 22.3. Let $B$ be a real bidiagonal matrix of the form
$$B = \begin{pmatrix} a_{1} & b_{1} & 0 & \cdots & 0 \\ 0 & a_{2} & b_{2} & \ddots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & a_{n-1} & b_{n-1} \\ 0 & 0 & 0 & a_{n} \end{pmatrix} .$$
$$\cdots$$
Let $A$ be the (2n) $\times$  (2n) symmetric matrix
$$A = \begin{pmatrix} 0 \\ B^{\top} \\ B & 0 \end{pmatrix} ,$$
and let $P$ be the permutation matrix given by $P = [e_{1}, e_{n+1}, e_{2}, e_{n+2}, \cdots  , e_{n}, e_{2n}]$.

<!-- PAGE 766 -->
$(1)$ Prove that $T = P^{\top}$ AP is a symmetric tridiagonal (2n) $\times$  (2n) matrix with zero main diagonal of the form
$$T = \begin{pmatrix} 0 & a_{1} & 0 & 0 & 0 & 0 & \cdots & 0 \\ a_{1} & 0 & b_{1} & 0 & 0 & 0 & \cdots & 0 \\ 0 & b_{1} & 0 & a_{2} & 0 & 0 & \cdots & 0 \\ 0 & 0 & a_{2} & 0 & b_{2} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & a_{n-1} & 0 & b_{n-1} & 0 \\ 0 & 0 & 0 & \cdots & 0 & b_{n-1} & 0 & a_{n} \\ 0 & 0 & 0 & \cdots & 0 & 0 & a_{n} & 0 \end{pmatrix} .$$
$(2)$ Prove that if $x_{i}$ is a unit eigenvector for an eigenvalue $\lambda_{i}$  of $T$, then $\lambda_{i}  = \pm \sigma_{i}$  where $\sigma_{i}$  is a singular value of $B$, and that
$$Px_{i} =\sqrt \frac{1}{\overline{2}} \begin{pmatrix} u_{i} \\ \pm v_{i} \end{pmatrix} ,$$
where the $u_{i}$ are unit eigenvectors of $B^{\top}B$ and the $v_{i}$ are unit eigenvectors of $BB^{\top}$.
Problem 22.4. Find the SVD of the matrix
$$A = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix} .$$
$$\mathbb{R}^{n}$$
Problem 22.5. Let $u, v \in$ be two nonzero vectors, and let $A = uv^{\top}$ be the corresponding rank $1$ matrix. Prove that the nonzero singular value of $A$ is $\|u\|_{2} \|v\|_{2}$.
Problem 22.6. Let $A$ be a $n\times n$ real matrix. Prove that if $\sigma_{1} , \dots  , \sigma_{n}$  are the singular values of $A$, then $\sigma_{1}^{3} , \dots  , \sigma_{n}^{3}$  are the singular values of $AA^{\top}A$.
Problem 22.7. Let $A$ be a real $n \times  n$ matrix.
$(1)$ Prove that the largest singular value $\sigma_{1}$  of $A$ is given by
$$\|\|_{2}$$
$$\sigma_{1}  = supx\neq 0 \frac{Ax}{\|x\|_{2}} ,$$
and that this supremum is achieved at $x = u_{1}$, the first column in $U$ in an SVD $A = V \Sigma U^{\top}$ .
$(2)$ Extend the above result to real $m \times  n$ matrices.
Problem 22.8. Let $A$ be a real $m \times  n$ matrix. Prove that if $B$ is any submatrix of $A$ (by keeping $M \le m$ rows and $N \le n$ columns of $A)$, then $(\sigma_{1} )_{B} \le (\sigma_{1} )_{A}$ (where $(\sigma_{1} )_{A}$ is the largest singular value of $A$ and similarly for $(\sigma_{1} )_{B})$.

<!-- PAGE 767 -->
Problem 22.9. Let $A$ be a real $n \times  n$ matrix.
$(1)$ Assume $A$ is invertible. Prove that if $A = Q_{1}S_{1} = Q_{2}S_{2}$ are two polar decompositions of $A$, then $Q_{1} = Q_{2}$ and $S_{1} = S_{2}$. Hint. $A^{\top}A = S_{1}^{2} = S_{2}^{2}$, with $S_{1}$ and $S_{2}$ symmetric positive definite. Then use Problem 17.7.
$(2)$ Now assume that $A$ is singular. Prove that if $A = Q_{1}S_{1} = Q_{2}S_{2}$ are two polar decompositions of $A$, then $S_{1} = S_{2}$, but $Q_{1}$ may not be equal to $Q_{2}$.
Problem 22.10. $(1)$ Let $A$ be any invertible (real) $n \times  n$ matrix. Prove that for every SVD, $A = V DU^{\top}$ of $A$, the product $V U^{\top}$ is the same (i.e., if $V_{1}DU_{1}^{\top} = V_{2}DU_{2}^{\top}$  , then $V_{1}U_{1}^{\top}  = V_{2}U_{2}^{\top}$ ). What does $V U^{\top}$ have to do with the polar form of $A$?
$(2)$ Given any invertible (real) $n \times  n$ matrix, $A$, prove that there is a unique orthogonal matrix, $Q \in$ O(n), such that $\|A$ - $Q\|_{F}$ is minimal (under the Frobenius norm). In fact, prove that $Q = V U^{\top}$ , where $A = V DU^{\top}$ is an SVD of $A$. Moreover, if det(A) $> 0$, show that $Q \in$ SO(n). What can you say if $A$ is singular (i.e., non-invertible)?
Problem 22.11. $(1)$ Prove that for any $n \times  n$ matrix $A$ and any orthogonal matrix $Q$, we have
$$\max{\mathrm{tr}(QA) | Q \in O(n)} = \sigma_{1}  + \cdots  + \sigma_{n} ,$$
where $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$  are the singular values of $A$. Furthermore, this maximum is achieved by $Q = UV^{\top}$ , where $A = V \Sigma U^{\top}$ is any SVD for $A$.
$(2)$ By applying the above result with $A = X^{\top}Z$ and $Q = R$, deduce the following result: for any two fixed $n \times  k$ matrices $X$ and $Z$, the minimum of the set
$${\|X -ZR\|_{F} | R \in O(k)}$$
is achieved by $R = UV^{\top}$ for any SVD decomposition $V \Sigma U^{\top} = X^{\top}Z$ of $X^{\top}Z$.
Remark: The problem of finding an orthogonal matrix $R$ such that $ZR$ comes as close as possible to $X$ is called the orthogonal Procrustes problem; see Strang $[177]$ (Section IV.9) for the history of this problem.

<!-- PAGE 768 -->
