# SPD Matrices and Schur Complements


<!-- PAGE 1568 -->

## 43.2 Symmetric Positive Definite Matrices and

$$Schur Complements$$
If we assume that our block matrix $M$ is symmetric, so that $A, D$ are symmetric and $C = B^{\top}$, then we see by Proposition 43.1 that $M$ is expressed as
$$M = \begin{pmatrix} A & B \\ B^{\top} & D \end{pmatrix} = \begin{pmatrix} I & BD^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BD^{-1}B^{\top} & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & BD^{-1\top} \\ 0 & I \end{pmatrix} ,$$
which shows that $M$ is similar to a block diagonal matrix (obviously, the Schur complement, $A$ - $BD^{-1}B^{\top}$, is symmetric). As a consequence, we have the following version of “Schur’s trick” to check whether $M$ ≻ $0$ for a symmetric matrix.

> **Proposition 43.3.** For any symmetric matrix $M$ of the form
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} ,$$
if $C$ is invertible, then the following properties hold:
$(1) M$ ≻ $0$ iff $C$ ≻ $0$ and $A$ - $BC^{-1}B^{\top}$ ≻ $0$.
$(2)$ If $C$ ≻ $0$, then $M$ ⪰ $0$ iff $A$ - $BC^{-1}B^{\top}$ ⪰ $0$.

*Proof.* $(1)$ Since $C$ is invertible, we have
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & BC^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BC^{-1}B^{\top} & 0 \\ 0 & C \end{pmatrix} \begin{pmatrix} I & BC^{-1\top} \\ 0 & I \end{pmatrix} .(*)$$
Observe that
$$\begin{pmatrix} I & BC^{-1-1} \\ 0 & I \end{pmatrix} = \begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} ,$$
so (*) yields
$$\begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} \begin{pmatrix} I & -BC^{-1\top} \\ 0 & I \end{pmatrix} = \begin{pmatrix} A -BC^{-1}B^{\top} & 0 \\ 0 & C \end{pmatrix} ,$$
and we know that for any symmetric matrix $T$, here $T = M$, and any invertible matrix $N$, here
$$N = \begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} ,$$
the matrix $T$ is positive definite $(T$ ≻ $0)$ iff $NTN^{\top}$ (which is obviously symmetric) is positive definite $(NTN^{\top}$ ≻ $0)$. But a block diagonal matrix is positive definite iff each diagonal block is positive definite, which concludes the proof.
$(2)$ This is because for any symmetric matrix $T$ and any invertible matrix $N$, we have $T$ ⪰ $0$ iff $NTN^{\top}$ ⪰ $0$.
