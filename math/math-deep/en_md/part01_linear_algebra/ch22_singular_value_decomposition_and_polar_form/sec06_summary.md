# Summary


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
