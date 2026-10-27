# Problems


<!-- PAGE 689 -->
$\bullet$  Unreduced and reduced Hessenberg matrices. $\bullet$  Deflation. $\bullet$  Shift. $\bullet$  Wilkinson shift. $\bullet$  Double shift. $\bullet$  Francis shift. $\bullet$  Implicit shifting. $\bullet$  Implicit Q-theorem. $\bullet$  Arnoldi iteration. $\bullet$  Breakdown of Arnoldi iteration. $\bullet$  Krylov subspace. $\bullet$  Rayleigh–Ritz method. $\bullet$  Ritz values, Arnoldi estimates. $\bullet$  Residual. $\bullet$  GMRES $\bullet$  Lanczos iteration. $\bullet$  Power iteration. $\bullet$  Inverse power iteration. $\bullet$  Rayleigh ratio.

## 18.9 Problems

Problem 18.1. Prove Theorem 18.2; see Problem 13.7.
Problem 18.2. Prove that if a matrix $A$ is Hermitian (or real symmetric), then any Hessenberg matrix $H$ similar to $A$ is Hermitian tridiagonal (real symmetric tridiagonal).
Problem 18.3. For any matrix (real or complex) $A$, if $A = QR$ is a QR-decomposition of $A$ using Householder reflections, prove that if $A$ is upper Hessenberg then so is $Q$.

<!-- PAGE 690 -->
Problem 18.4. Prove that if $A$ is upper Hessenberg, then the matrices $A_{k}$ obtained by applying the QR-algorithm are also upper Hessenberg.
Problem 18.5. Prove the implicit $Q$ theorem. This theorem says that if $A$ is reduced to upper Hessenberg form as $A = UHU^{*}$ and if $H$ is unreduced $(h_{i+1i} \neq  0$ for $i = 1, \dots  , n -1)$, then the columns of index $2, \dots  , n$ of $U$ are determined by the first column of $U$ up to sign;
Problem 18.6. Read Section 7.5 of Golub and Van Loan $[83]$ and implement their version of the QR-algorithm with shifts.
Problem 18.7. If an Arnoldi iteration has a breakdown at stage $n$, that is, $h_{n+1} = 0$, then we found the first unreduced block of the Hessenberg matrix $H$. Prove that the eigenvalues of $H_{n}$ are eigenvalues of $A$.
Problem 18.8. Prove Theorem 18.6.
Problem 18.9. Implement GRMES and test it on some linear systems.
Problem 18.10. State and prove versions of Proposition 18.5 and Theorem 18.6 for the Lanczos iteration.
Problem 18.11. Prove the results about the power iteration method stated in Section 18.7.
Problem 18.12. Prove the results about the inverse power iteration method stated in Section 18.7.
Problem 18.13. Implement and test the power iteration method and the inverse power iteration method.
Problem 18.14. Read Lecture $27$ in Trefethen and Bau $[182]$ and implement and test the Rayleigh quotient iteration method.
