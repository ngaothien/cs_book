# Best Affine Approximation


<!-- PAGE 794 -->
In general, since an SVD of $X$ is not unique, the principal directions $u_{1}, \dots  , u_{d}$ are not unique. This can happen when a data set has some rotational symmetries, and in such a case, PCA is not a very good method for analyzing the data set.

## 23.5 Best Affine Approximation

A problem very close to PCA (and based on least squares) is to best approximate a data set of $n$ points $X_{1}, \dots  , X_{n}$, with $X_{i} \in \mathbb{R}^{d}$, by a $p$-dimensional affine subspace $A$ of $\mathbb{R}^{d}$, with $1 \le p \le d$ - $1$ (the terminology rank $d$ - $p$ is also used). First consider $p = d -1$. Then $A = A_{1}$ is an affine hyperplane (in $\mathbb{R}^{d})$, and it is given by an equation of the form
$$a_{1}x_{1} + \cdots  + a_{d}x_{d} + c = 0.$$
By best approximation, we mean that $(a_{1}, \dots  , a_{d}, c)$ solves the homogeneous linear system
$$\begin{pmatrix} x_{1 1} & \cdots & x_{1d} & 1 \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix} \begin{pmatrix} a_{1} \\ \vdots \\ a_{d} \\ c \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 0 \end{pmatrix}$$
in the least squares sense, subject to the condition that $a = (a_{1}, \dots  , a_{d})$ is a unit vector, that is, $a^{\top}a = 1$, where $X_{i} = (x_{i1}, \cdots  , x_{i d})$. If we form the symmetric matrix
$$1^{\top}$$
$$\begin{pmatrix} x_{1 1} & \cdots & x_{1d} \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix} \begin{pmatrix} x_{1 1} & \cdots & x_{1d} & 1 \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix}$$
involved in the normal equations, we see that the bottom row (and last column) of that matrix is
$$n\mu_{1} \cdots n\mu_{d} n,$$
$$where n\mu_{j}  = \sum_{i}  n=1 x_{i j} is n times the mean of the column C_{j} of X.$$
Therefore, if $(a_{1}, \dots  , a_{d}, c)$ is a least squares solution, that is, a solution of the normal equations, we must have
$$n\mu_{1} a_{1} + \cdots  + n\mu_{d} a_{d} + nc = 0,$$
that is,
$$a_{1}\mu_{1}  + \cdots  + a_{d}\mu_{d}  + c = 0,$$
which means that the hyperplane $A_{1}$ must pass through the centroid $\mu$  of the data points $X_{1}, \dots  , X_{n}$. Then we can rewrite the original system with respect to the centered data $X_{i}$ - $\mu$ , find that the variable $c$ drops out, get the system
$$(X -\mu )a = 0,$$

<!-- PAGE 795 -->
where $a = (a_{1}, \dots  , a_{d})$. Thus, we are looking for a unit vector a solving $(X$ - $\mu )a = 0$ in the least squares sense, that is, some a such that $a^{\top}a = 1$ minimizing
$$a^{\top}(X -\mu )^{\top}(X -\mu )a.$$
Compute some SVD $V DU^{\top}$ of $X -\mu$ , where the main diagonal of $D$ consists of the singular values $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$  of $X$ - $\mu$  arranged in descending order. Then
$$a^{\top}(X -\mu )^{\top}(X -\mu )a = a^{\top}UD^{2}U^{\top} a,$$
where $D^{2} = diag(\sigma_{1}^{2} , \dots  , \sigma_{d}^{2}$ ) is a diagonal matrix, so pick a to be the last column in $U$ (corresponding to the smallest eigenvalue $\sigma_{d}^{2}$  of $(X$ - $\mu )^{\top}(X$ - $\mu$ )). This is a solution to our best fit problem. Therefore, if $U_{d-1}$ is the linear hyperplane defined by a, that is,
$$\mathbb{R}^{d}$$
$$U_{d-1} = {u \in | \langle u, a\rangle = 0},$$
where a is the last column in $U$ for some SVD $V DU^{\top}$ of $X$ - $\mu$ , we have shown that the affine hyperplane $A_{1} = \mu  + U_{d-1}$ is a best approximation of the data set $X_{1}, \dots  , X_{n}$ in the least squares sense. It is easy to show that this hyperplane $A_{1} = \mu  + U_{d-1}$ minimizes the sum of the square distances of each $X_{i}$ to its orthogonal projection onto $A_{1}$. Also, since $U_{d-1}$ is the orthogonal complement of a, the last column of $U$, we see that $U_{d-1}$ is spanned by the first d-1 columns of $U$, that is, the first $d$ - $1$ principal directions of $X$ - $\mu$ . All this can be generalized to a best (d-k)-dimensional affine subspace $A_{k}$ approximating $X_{1}, \dots  , X_{n}$ in the least squares sense $(1 \le k \le d -1)$. Such an affine subspace $A_{k}$ is cut out by $k$ independent hyperplanes $H_{i}$ (with $1 \le i \le k)$, each given by some equation
$$a_{i1}x_{1} + \cdots  + a_{i d}x_{d} + c_{i} = 0.$$
If we write $a_{i} = (a_{i1}, \cdots  , a_{i d})$, to say that the $H_{i}$ are independent means that $a_{1}, \dots  , a_{k}$ are linearly independent. In fact, we may assume that $a_{1}, \dots  , a_{k}$ form an orthonormal system. Then finding a best $(d$ - k)-dimensional affine subspace $A_{k}$ amounts to solving the homogeneous linear system
$$\begin{pmatrix} X & 1 & 0 & \cdots & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & X & 1 \end{pmatrix} \begin{pmatrix} a_{1} \\ c_{1} \\ \vdots \\ a_{k} \\ c_{k} \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} ,$$

<!-- PAGE 796 -->
in the least squares sense, subject to the conditions $a_{i}^{\top} a_{j} = \delta_{i j}$ , for all $i, j$ with $1 \le i, j \le k$, where the matrix of the system is a block diagonal matrix consisting of $k$ diagonal blocks $(X, 1)$, where $1$ denotes the column vector $(1, \dots  , 1) \in \mathbb{R}^{n}$. Again it is easy to see that each hyperplane $H_{i}$ must pass through the centroid $\mu$  of $X_{1}, \dots  , X_{n}$, and by switching to the centered data $X_{i}$ - $\mu$  we get the system
$$\begin{pmatrix} X-\mu & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & X-\mu \end{pmatrix} \begin{pmatrix} a_{1} \\ \vdots \\ a_{k} \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} ,$$
with $a_{i}^{\top} a_{j} = \delta_{i j}$  for all $i, j$ with $1 \le i, j \le k$. If $V DU^{\top} = X -\mu$  is an SVD decomposition, it is easy to see that a least squares solution of this system is given by the last $k$ columns of $U$, assuming that the main diagonal of $D$ consists of the singular values $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$  of $X -\mu$  arranged in descending order. But now the $(d$ -k)-dimensional subspace $U_{d-k}$ cut out by the hyperplanes defined by $a_{1}, \dots  , a_{k}$ is simply the orthogonal complement of $(a_{1}, \dots  , a_{k})$, which is the subspace spanned by the first $d$ - $k$ columns of $U$. So the best (d-k)-dimensional affine subpsace $A_{k}$ approximating $X_{1}, \dots  , X_{n}$ in the least squares sense is
$$A_{k} = \mu  + U_{d-k},$$
where $U_{d-k}$ is the linear subspace spanned by the first d-k principal directions of $X-\mu$ , that is, the first d-k columns of $U$. Consequently, we get the following interesting interpretation of PCA (actually, principal directions):

> **Theorem 23.12.** Let $X$ be an $n \times  d$ matrix of data points $X_{1}, \dots  , X_{n}$, and let $\mu$  be the centroid of the $X_{i}’s$. If $X$ - $\mu  = V DU^{\top}$ is an SVD decomposition of $X$ - $\mu$  and if the main diagonal of $D$ consists of the singular values $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$ , then a best $(d$ - k)- dimensional affine approximation $A_{k}$ of $X_{1}, \dots  , X_{n}$ in the least squares sense is given by
$$A_{k} = \mu  + U_{d-k},$$
where $U_{d-k}$ is the linear subspace spanned by the first $d$ - $k$ columns of $U$, the first $d$ - $k$ principal directions of $X$ - $\mu  (1 \le k \le d$ - $1)$.

> **Example 23.11.** Going back to Example 23.10, a best 1-dimensional affine approximation $A_{1}$ is the affine line passing through $(\mu_{1} , \mu_{2}$ ) $=$ (1824.4, 5.6) of direction $u_{1} =$ (0.9995, 0.0325).

> **Example 23.12.** Suppose in the data set of Example 23.5 that we add the month of birth of every mathematician as a feature. We obtain the following data set.

<!-- PAGE 797 -->
$$Namemonthyearlength$$
$$Carl Friedrich Gauss417770$$
$$Camille Jordan1183812$$
$$Adrien-Marie Legendre917520$$
$$Bernhard Riemann9182615$$
$$David Hilbert118622$$
$$Henri Poincar´e418545$$
$$Emmy Noether318820$$
$$Karl Weierstrass1018150$$
$$Eugenio Beltrami1018352$$
$$Hermann Schwarz1184320$$
The mean of the first column is 5.2, and the centered data set is given below.
$$Namemonthyearlength$$
$$Carl Friedrich Gauss-1.2-51.4-5.6$$
$$Camille Jordan-4.29.66.4$$
$$Adrien-Marie Legendre3.8-76.4-5.6$$
$$Bernhard Riemann3.8-2.49.4$$
$$David Hilbert-4.233.6-3.6$$
$$Henri Poincar´e-1.225.6-0.6$$
$$Emmy Noether-2.253.6-5.6$$
$$Karl Weierstrass4.813.4-5.6$$
$$Eugenio Beltrami4.86.6-3.6$$
$$Hermann Schwarz-4.214.614.4$$
Running SVD on this data set we get
$$U = \begin{pmatrix} 0.0394 & 0.1717 & 0.9844 \\ -0.9987 & 0.0390 & 0.0332 \\ 0.0327 & 0.9844 & 0.1730 \end{pmatrix} ,D = \begin{pmatrix} 117.0706 & 0 & 0 \\ 0 & 22.0390 & 0 \\ 0 & 0 & 10.1571 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,$$
$$--$$
