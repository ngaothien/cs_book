# Hilbert Space Representation of a Positive Kernel


<!-- PAGE 1958 -->
is a positive definite kernel. Let $f$ : $X \to \mathbb{R}$ be the function given by
$$f(x) =\overline{e}_{2\sigma}^{-\|x\|22} .$$
Then by Proposition 53.6(3),
$$\kappa_{2} (x, y) = f(x)f(y) =\overline{e}_{2\sigma}^{-\|x\|22}\overline{e}_{2\sigma}^{-\|y\|22}=\overline{e}_{2\sigma}^{-\|x\|2X+2\|y\|2X}$$
is a positive definite kernel. By Proposition 53.5, the function $\kappa_{1} \kappa_{2}$  is a positive definite kernel, that is
$$\kappa_{1} (x, y)\kappa_{2} (x, y) =\overline{e}_{\sigma}^{\langle x,y2\rangle X}\overline{e}_{2\sigma}^{-\|x\|2X+2\|y\|2X}=\overline{e}_{\sigma2\sigma}^{\langle x,y2\rangle X-\|x\|2X+2\|y\|2X}=\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
is a positive definite kernel.

> **Definition 53.4.** The positive definite kernel
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
is called a Gaussian kernel. This kernel requires a feature map in an infinite-dimensional space because it is an infinite sum of distinct kernels.
Remark: If $\kappa_{1}$  is a positive definite kernel, the proof of Proposition 53.7(3) is immediately adapted to show that
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\kappa1(x,x)+\kappa1(y,y2)-2\kappa1(x,y)}$$
is a positive definite kernel. Next we prove that every positive definite kernel arises from a feature map in a Hilbert space which is a function space.

## 53.3 Hilbert Space Representation of a Positive

$$Definite Kernel$$
The following result shows how to construct a so-called reproducing kernel Hilbert space, for short RKHS, from a positive definite kernel.

> **Theorem 53.8.** Let $\kappa$ : $X \times  X \to \mathbb{C}$ be a positive definite kernel on a nonempty set $X$. For every $x \in X$, let $\kappa_{x}$  : $X \to \mathbb{C}$ be the function given by
$$\kappa_{x} (y) = \kappa (x, y),y \in X.$$

<!-- PAGE 1959 -->
$$\mathbb{C}^{X}  \mathbb{C}$$
Let $H_{0}$ be the subspace of the vector space of functions from $X$ to  spanned by the family of functions $(\kappa_{x} )_{\in X}$, and let $\phi$ : $X \to H_{0}$ be the map given by $\phi (x) = \kappa_{x}$ . There is a Hermitian inner product $\langle$ -, $-\rangle$ on $H_{0}$ such that
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
$$\mathbb{C}^{X}$$
The completion $H$ of $H_{0}$ is a Hilbert space, and the map $\eta$ : $H \to$ given by
$$\eta (f)(x) = \langle f, \kappa_{x} \rangle ,x \in X,$$
is linear and injective, so $H$ can be identified with a subspace of $\mathbb{C}^{X}$. We also have
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
For all $f \in H_{0}$ and all $x \in X$,
$$\langle f, \kappa_{x} \rangle = f(x),(*)$$
a property known as the reproducing property.

*Proof.* Step $1$. Define a candidate inner product.
$$For any two linear combinations f = \sum_{j}  p=1 \alpha_{j} \kappa_{xj}  and g = \sum_{k}  q=1 \beta_{k} \kappa_{yk}  in H_{0}, with$$
$x_{j}, y_{k} \in X$ and $\alpha_{j} , \beta_{k}  \in \mathbb{C}$, define $\langle f, g\rangle$ by
$$\langle f, g\rangle = \sum_{j=1}^{p}  \sum_{k=1}^{q}  \alpha_{j} \overline{\beta}_{k}\kappa (x_{j}, y_{k}).(\dagger )$$
$$\frac{At first glance, the above expression appears to depend on the expression of}{\kappa (y_{k}, x_{j}),} f and g as linear$$
combinations, but since $\kappa (x_{j}, y_{k}) =$  observe that
$$\sum_{k=1}^{q}  \overline{\beta}_{k}f(y_{k}) = \sum_{j=1}^{p}  \sum_{k=1}^{q}  \alpha_{j} \overline{\beta}_{k}\kappa (x_{j}, y_{k}) = \sum_{j=1}^{p}  \alpha_{j} \overline{g}\overline{(}\overline{x}_{j}\overline{)},(*)$$
and since the first and the third term are equal for all linear combinations representing $f$ and $g$, we conclude that $(\dagger$ ) depends only on $f$ and $g$ and not on their representation as a linear combination. Step $2$. Prove that the inner product defined by $(\dagger$ ) is Hermitian semidefinite. Obviously $(\dagger$ ) defines a Hermitian sequilinear form. For every $f \in H_{0}$, we have
$$\langle f, f\rangle = \sum_{j,k=1}^{p}  \alpha_{j} \overline{\alpha}_{k}\kappa (x_{j}, x_{k}) \ge 0,$$
since $\kappa$  is a positive definite kernel.

<!-- PAGE 1960 -->
Step $3$. Prove that the inner product defined by $(\dagger$ ) is positive definite. For any finite subset ${f_{1}, \dots  , f_{n}}$ of $H_{0}$ and any $z \in \mathbb{C}^{n}$, we have
$$*+$$
$$\sum_{j,k=1}^{n}  \langle f_{j}, f_{k}\rangle z_{j}\overline{z}_{k} = \sum_{j=1}^{n}  z_{j}f_{j}, \sum_{j=1}^{n}  z_{j}f_{j}\ge 0,$$
which shows that the map $(f, g) \mapsto \langle f, g\rangle$ from $H_{0} \times  H_{0}$ to $\mathbb{C}$ is a positive definite kernel. Observe that for all $f \in H_{0}$ and all $x \in X, (\dagger$ ) implies that
$$\langle f, \kappa_{x} \rangle = \sum_{j=1}^{k}  \alpha_{j} \kappa (x_{j}, x) = f(x),$$
a property known as the reproducing property. The above implies that
$$\langle \kappa_{x} , \kappa_{y} \rangle = \kappa (x, y).(**)$$
By Proposition 53.4 applied to the positive definite kernel $(f, g) \mapsto \langle f, g\rangle$ , we have
$$|\langle f, \kappa_{x} \rangle |^{2}\le \langle f, f\rangle \langle \kappa_{x} , \kappa_{x} \rangle ,$$
that is,
$$|f(x)|^{2}\le \langle f, f\rangle \kappa (x, x),$$
so $\langle f, f\rangle = 0$ implies that f(x) $= 0$ for all $x \in X$, which means that $\langle$ -, $-\rangle$ as defined by $(\dagger$ ) is positive definite. Therefore, $\langle$ -, $-\rangle$ is a Hermitian inner product on $H_{0}$, and by (**) and since $\phi (x) = \kappa_{x}$ , we have
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
Step $4$. Define the embedding $\eta$ . Let $H$ be the Hilbert space which is the completion of $H_{0}$, so that $H_{0}$ is dense in $H$. The
$$\mathbb{C}^{X}$$
map $\eta$ : $H \to$ given by
$$\eta (f)(x) = \langle f, \kappa_{x} \rangle$$
is obviously linear, and it is injective because the family $(\kappa_{x} )_{x\in X}$ spans $H_{0}$ which is dense in $H$, thus it is also dense in $H$, so if $\langle f, \kappa_{x} \rangle = 0$ for all $x \in X$, then $f = 0$.

> **Corollary 53.9.** If we identify a function $f \in H$ with the function $\eta (f)$, then we have the reproducing property
$$\langle f, \kappa_{x} \rangle = f(x),for all f \in H and all x \in X.$$
$$\mathbb{C}^{X}$$
If $X$ is finite, then is finite-dimensional. If $X$ is a separable topological space and if $\kappa$  is continuous, then it can be shown that $H$ is a separable Hilbert space.
