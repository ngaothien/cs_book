# Summary


<!-- PAGE 1964 -->
$\bullet$  Let $r$ be the rank of $K$, where
$$b$$
$$Kb = K - \frac{1}{n} 11^{\top}K - \frac{1}{n} K11^{\top}+ \frac{1}{n^{2}} (1^{\top}K1)11^{\top},$$
let $\sigma_{1}^{2}  \ge \cdots  \ge \sigma_{r}^{2}$  be the nonzero eigenvalues of $K$, and let $v_{1}, \dots  , v_{r}$ be corresponding
$$b$$
unit eigenvectors. The notation
$$\alpha_{k}  = \sigma_{k}^{-1}  v_{k}$$
is often used, where the $\alpha_{k}$  are called the dual variables. $\bullet$  The column vector $Y_{k} (1 \le k \le r)$ defined by
$$!n$$
$$Y_{k} = \sum_{i=1}^{n}  (\alpha_{k} )_{i} K_{ij}b$$
$$j=1$$
is called the kth kernel principal component (for short kth kernel PCA) of the data set
$$S = {x_{1}, \dots  , x_{n}} in the direction u_{k} = \sum_{i}  n=1 \sigma_{k}^{-1}  (v_{k})_{i} bX_{i}^{\top} (even though the matrix Xb$$
is not known).

## 53.5 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Feature map, feature embedding, feature space. $\bullet$  Kernel function. $\bullet$  Positive definite kernel, real positive definite kernel. $\bullet$  Gram matrix. $\bullet$  Hadamard product, Schur product. $\bullet$  Gaussian kernel. $\bullet$  Reproducing kernel Hilbert space (RKHS). $\bullet$  Reproducing property. $\bullet$  Intersection kernel, union complement kernel, agreement kernel. $\bullet$  Kernel PCA. $\bullet k$-th kernel PCA.
