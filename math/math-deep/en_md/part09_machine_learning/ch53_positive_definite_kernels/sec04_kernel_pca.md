# Kernel PCA


<!-- PAGE 1961 -->
Also, if $\kappa$ : $X \times  X \to \mathbb{R}$ is a real symmetric positive definite kernel, then we see immediately that Theorem 53.8 holds with $H_{0}$ a real Euclidean space and $H$ a real Hilbert space. ⊛ Remark: If $X = G$, where $G$ is a locally compact group, then a function $p: G \to \mathbb{C}$ (not necessarily continuous) is positive semidefinite if for all $s_{1}, \dots  , s_{n} \in G$ and all $\xi_{1} , \dots  , \xi_{n}  \in \mathbb{C}$, we have
$$\sum_{j,k=1}^{n}  p(s_{j}^{-1} s_{k})\xi_{k} \overline{\xi}_{j} \ge 0.$$
So if we define $\kappa$ : $G \times  G \to \mathbb{C}$ by
$$\kappa (s, t) = p(t^{-1}s),$$
then $\kappa$  is a positive definite kernel on $G$. If $p$ is continuous, then it is known that $p$ arises from a unitary representation $U$ : $G \to$ U(H) of the group $G$ in a Hilbert space $H$ with inner product $\langle$ -, $-\rangle$ (a homomorphism with a certain continuity property), in the sense that there is some vector $x_{0} \in H$ such that
$$p(s) = \langle U(s)(x_{0}), x_{0}\rangle ,for all s \in G.$$
Since the U(s) are unitary operators on $H$,
$$p(t^{-1}s) = \langle U(t^{-1}s)(x_{0}), x_{0}\rangle = \langle U(t^{-1})(U(s)(x_{0})), x_{0}\rangle$$
$$= \langle U(t)^{*}(U(s)(x_{0})), x_{0}\rangle = \langle U(s)(x_{0}), U(t)(x_{0})\rangle ,$$
which shows that
$$\kappa (s, t) = \langle U(s)(x_{0}), U(t)(x_{0})\rangle ,$$
so the map $\phi$ : $G \to H$ given by
$$\phi (s) = U(s)(x_{0})$$
is a feature map into the feature space $H$. This theorem is due to Gelfand and Raikov $(1943)$. The proof of Theorem 53.8 is essentially identical to part of Godement’s proof of the above result about the correspondence between functions of positive type and unitary representations; see Helgason $[93]$, Chapter IV, Theorem 1.5. Theorem 53.8 is a little more general since it does not assume that $X$ is a group, but when $G$ is a group, the feature map arises from a unitary representation.

## 53.4 Kernel PCA

As an application of kernel functions, we discuss a generalization of the method of principal component analysis (PCA). Suppose we have a set of data $S = {x_{1}, \dots  , x_{n}}$ in some input space $\mathcal{X}$, and pretend that we have an embedding $\phi$ : $\mathcal{X} \to F$ of $\mathcal{X}$ in a (real) feature space $(F, \langle$ -, $-\rangle$ ), but that we only have access to the kernel function $\kappa (x, y) = \langle \phi (x), \phi (y)\rangle$ . We would like to do PCA analysis on the set $\phi (S) = {\phi (x_{1}), \dots  , \phi (x_{n})}$. There are two obstacles:

<!-- PAGE 1962 -->
$(1)$ We need to center the data and compute the inner products of pairs of centered data. More precisely, if the centroid of $\phi (S)$ is
$$\mu  = \frac{1}{n} (\phi (x_{1}) + \cdots  + \phi (x_{n})),$$
then we need to compute the inner products $\langle \phi (x)$ - $\mu , \phi (y)$ - $\mu \rangle$ .
$$\mathbb{R}^{d}$$
$(2)$ Let us assume that $F =$ with the standard Euclidean inner product and that the data points $\phi (x_{i})$ are expressed as row vectors $X_{i}$ of an $n \times  d$ matrix $X$ (as it is customary). Then the inner products $\kappa (x_{i}, x_{j}) = \langle \phi (x_{i}), \phi (x_{j})\rangle$ are given by the kernel matrix $K = XX^{\top}$. Be aware that with this representation, in the expression $\langle \phi (x_{i}), \phi (x_{j})\rangle , \phi (x_{i})$ is a $d$-dimensional column vector, while $\phi (x_{i}) = X_{i}^{\top}$ . However, the jth component $(Y_{k})_{j}$ of the principal component $Y_{k}$ (viewed as a $n$-dimensional column vector) is given by the projection of $X_{j} = X_{j} -\mu$  onto the direction $u_{k}$ (viewing $\mu$  as a
$$b$$
$d$-dimensional row vector), which is a unit eigenvector of the matrix $(X$ - $\mu )^{\top}(X$ - $\mu$ ) (where $X = X$ - $\mu$  is the matrix whose jth row is $X_{j} = X_{j}$ - $\mu$ ), is given by the inner
$$b b$$
product
$$\langle X_{j} -\mu , u_{k}\rangle = (Y_{k})_{j};$$
see Definition 23.2 and Theorem 23.11. The problem is that we know what the matrix $(X$ - $\mu )(X$ - $\mu )^{\top}$ is from $(1)$, because it can be expressed in terms of $K$, but we don’t know what $(X$ - $\mu )^{\top}(X$ - $\mu$ ) is because we don’t have access to $X = X$ - $\mu$ .
$$b$$
Both difficulties are easily overcome. For $(1)$ we have
$$*+$$
$$\langle \phi (x) -\mu , \phi (y) -\mu \rangle =\phi (x) - \frac{1}{n} \sum_{k=1}^{n}  \phi (x_{k}), \phi (y) - \frac{1}{n} \sum_{k=1}^{n}  \phi (x_{k})$$
$$= \kappa (x, y) - \frac{1}{n} \sum_{i=1}^{n}  \kappa (x, x_{i}) - \frac{1}{n} \sum_{j=1}^{n}  \kappa (x_{j}, y) + \frac{1}{n^{2}} \sum_{i,j=1}^{n}  \kappa (x_{i}, x_{j}).$$
For $(2)$, if $K$ is the kernel matrix $K = (\kappa (x_{i}, x_{j}))$, then the kernel matrix $K$ corresponding
$$b$$
to the kernel function $\kappa$  given by
$$b$$
$$\kappa (x, y) = \langle \phi (x) -\mu , \phi (y) -\mu \rangle$$
$$b$$
can be expressed in terms of $K$. Let $1$ be the column vector (of dimension $n)$ whose entries are all $1$. Then $11^{\top}$ is the $n \times  n$ matrix whose entries are all $1$. If $A$ is an $n \times  n$ matrix, then $1^{\top}A$ is the row vector consisting of the sums of the columns of $A$, A1 is the column vector consisting of the sums of the rows of $A$, and $1^{\top}A1$ is the sum of all the entries in $A$. Then it is easy to see that the kernel matrix corresponding to the kernel function $\kappa$  is given by
$$b$$
$$Kb = K - \frac{1}{n} 11^{\top}K - \frac{1}{n} K11^{\top}+ \frac{1}{n^{2}} (1^{\top}K1)11^{\top}.$$

<!-- PAGE 1963 -->
Suppose $X = X$ - $\mu$  has rank $r$. To overcome the second problem, note that if
$$b$$
$$X = V DU^{\top}$$
$$b$$
is an SVD for $X$, then
$$b$$
$$X^{\top}= UD^{\top}V^{\top}$$
$$b$$
is an SVD for $X^{\top}$, and the $r\times r$ submatrix of $D^{\top}$ consisting of the first $r$ rows and $r$ columns
$$b$$
of $D^{\top}$ (and $D)$, is the diagonal $\Sigma_{r}$  matrix consisting of the singular values $\sigma_{1}  \ge \cdots  \ge \sigma_{r}$  of $X$, so we can express the matrix $U_{r}$ consisting of the first $r$ columns $u_{k}$ of $U$ in terms of the $b$ matrix $V_{r}$ consisting of the first $r$ columns $v_{k}$ of $V (1 \le k \le r)$ as
$$U_{r} =X^{\top}V_{r}\Sigma_{r}^{-1}  .$$
$$b$$
Furthermore, $\sigma_{1}^{2}  \ge \cdots  \ge \sigma_{r}^{2}$  are the nonzero eigenvalues of $K = XX^{\top}$, and the columns of
$$b b b$$
$V_{r}$ are corresponding unit eigenvectors of $K$. From
$$b$$
$$U_{r} =X^{\top}V_{r}\Sigma_{r}^{-1}$$
$$b$$
the kth column $u_{k}$ of $U_{r}$ (which is a unit eigenvector of $X^{\top}X$ associated with the eigenvalue
$$bb$$
$\sigma_{k}^{2}$ ) is given by
$$[$$
$$u_{k} = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i} bX_{i}^{\top} = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\phi (x_{i}),1 \le k \le r,$$
$$[$$
so the projection of $\phi (x)$ onto $u_{k}$ is given by
$$*+$$
$$[[ [$$
$$\langle \phi (x), u_{k}\rangle =\phi (x), \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\phi (x_{i})$$
$$= \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k}) \bigoplus_{i}  \phi [(x), \phi [(x_{i})E= \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\kappa (x, x_{i}).$$
$$b$$
Therefore, the jth component of the principal component $Y_{k}$ in the principal direction $u_{k}$ is given by
$$(Y_{k})_{j} = \langle X_{j} -\mu , u_{k}\rangle = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\kappa b(x_{j}, x_{i}) = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i} bK_{ij}.$$
The generalization of kernel PCA to a general embedding $\phi$ : $\mathcal{X} \to F$ of $\mathcal{X}$ in a (real) feature space $(F, \langle$ -, $-\rangle$ ) (where $F$ is not restricted to be equal $to\mathbb{R}^{d})$ with the kernel matrix $K$ given by
$$K_{ij} = \langle \phi (x_{i}), \phi (x_{j})\rangle ,$$
goes as follows.
