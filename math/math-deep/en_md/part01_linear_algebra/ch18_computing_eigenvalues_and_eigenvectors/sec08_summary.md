# Summary


<!-- PAGE 688 -->

> **Proposition 18.7.** Let $A$ be an $m \times  m$ diagonalizable (complex or real) matrix with eigenvalues $\lambda_{1} , \dots  , \lambda_{m}$ , and let $\lambda  = \lambda_{\ell}$ be an arbitrary eigenvalue of $A$ (not necessary simple). For any $\mu$  such that
$$\mu  \neq  \lambda and|\mu  -\lambda | < |\mu  -\lambda_{j} |for all j \neq  \ell ,$$
if $x^{0}$ does not belong to the subspace spanned by the eigenvectors associated with the eigenvalues $\lambda_{j}$  with $j \neq  \ell$ , then
$$klim\mapsto \infty \begin{pmatrix} (\lambda  -\mu )^{k} \\ |\lambda  -\mu |^{k} \end{pmatrix} x^{k}= v,$$
where $v$ is an eigenvector associated with $\lambda$ . Furthermore, if both $\lambda$  and $\mu$  are real, we have
$$limx^{k}= vif \mu  < \lambda ,$$
$$k\mapsto \infty$$
$$lim(-1)^{k}x^{k}= vif \mu  > \lambda .$$
$$k\mapsto \infty$$
Also, if we define the sequence $(\lambda^{(k)}$ ) by
$$\lambda^{(k+1)} = (x^{k+1})^{*}Ax^{k+1},$$
then
$$lim\lambda^{(k+1)} = \lambda .$$
$$k\mapsto \infty$$
The condition of $x^{0}$ may seem quite stringent, but in practice, a vector $x^{0}$ chosen at random usually satisfies it. If $A$ is a Hermitian matrix, then we can say more. In particular, the inverse iteration algorithm can be modified to make use of the newly computed $\lambda^{(k+1)}$ instead of $\mu$ , and an even faster convergence is achieved. Such a method is called the Rayleigh quotient iteration. When it converges (which is for almost all $x^{0})$, this method eventually achieves cubic convergence, which is remarkable. Essentially, this means that the number of correct digits is tripled at every iteration. For more details, see Trefethen and Bau $[182]$ (Lecture $27)$ and Demmel $[48]$ (Section 5.3.2).

## 18.8 Summary

The main concepts and results of this chapter are listed below: $\bullet$  QR iteration, QR algorithm. $\bullet$  Upper Hessenberg matrices. $\bullet$  Householder matrix.
