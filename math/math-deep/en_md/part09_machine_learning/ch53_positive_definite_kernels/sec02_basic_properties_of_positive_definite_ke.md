# Basic Properties of Positive Definite Kernels


<!-- PAGE 1952 -->

## 53.2 Basic Properties of Positive Definite Kernels

Proposition 53.1 suggests a second approach to kernel functions which does not assume that a feature space and a feature map are provided. We will see in Section 53.3 that the two approaches are equivalent. The second approach is useful in practice because it is often difficult to define a feature space and a feature map in a simple manner.

> **Definition 53.2.** Let $X$ be a nonempty set. A function $\kappa$ : $X \times X \to \mathbb{C}$ is a positive definite kernel if for every finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, if $K_{S}$ is the $p \times  p$ matrix
$$K_{S} = (\kappa (x_{j}, x_{i}))_{1\le i,j\le p}$$
called a Gram matrix, then we have
$$u^{*}K_{S} u = \sum_{i,j=1}^{p}  \kappa (x_{i}, x_{j})u_{i}\overline{u}_{j} \ge 0,for all u \in \mathbb{C}^{p}.$$
Observe that Definition 53.2 does not require that $u^{*}K_{S} u > 0$ if $u \neq  0$, so the terminology positive definite is a bit abusive, and it would be more appropriate to use the terminology positive semidefinite. However, it seems customary to use the term positive definite kernel, or even positive kernel.

> **Proposition 53.2.** Let $\kappa$ : $X \times  X \to \mathbb{C}$ be a positive definite kernel. Then $\kappa (x, x) \ge 0$ for all $x \in X$, and for any finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, the $p \times  p$ matrix $K_{S}$ given by
$$K_{S} = (\kappa (x_{j}, x_{i}))_{1\le i,j\le p}$$
is Hermitian, that is, $K_{S}^{*} = K_{S}$.

*Proof.* The first property is obvious by choosing $S = {x}$. To prove that $K_{S}$ is Hermitian, observe that we have
$$(u + v)^{*}K_{S}(u + v) = u^{*}K_{S}u + u^{*}K_{S}v + v^{*}K_{S}u + v^{*}K_{S}v,$$
and since $(u + v)^{*}K_{S}(u + v), u^{*}K_{S}u, v^{*}K_{S}v \ge 0$, we deduce that
$$2A = u^{*}K_{S}v + v^{*}K_{S}u(1)$$
must be real. By replacing $u$ by iu, we see that
$$2B = -iu^{*}K_{S}v + iv^{*}K_{S}u(2)$$
must also be real. By multiplying Equation $(2)$ by $i$ and adding it to Equation $(1)$ we get
$$u^{*}K_{S}v = A + iB.(3)$$

<!-- PAGE 1953 -->
By subtracting Equation $(3)$ from Equation $(1)$ we get
$$v^{*}K_{S}u = A -iB.$$
Then
$$u^{*}K_{S}^{*}v =\overline{v}^{*}\overline{K}_{S}\overline{u} =\overline{A}\overline{-}\overline{iB} = A + iB = u^{*}K_{S}v,$$
for all $u, v \in \mathbb{C}^{*}$, which implies $K_{S}^{*} = K_{S}$. If the map $\kappa$ : $X \times  X \to \mathbb{R}$ is real-valued, then we have the following criterion for $\kappa$  to be a positive definite kernel that only involves real vectors.

> **Proposition 53.3.** If $\kappa$ : $X \times  X \to \mathbb{R}$, then $\kappa$  is a positive definite kernel iff for any finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, the $p \times  p$ real matrix $K_{S}$ given by
$$K_{S} = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p}$$
is symmetric, that is, $K_{S}^{\top} = K_{S}$, and
$$u^{\top}K_{S} u = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})u_{j}u_{k} \ge 0,for all u \in \mathbb{R}^{p}.$$

*Proof.* If $\kappa$  is a real-valued positive definite kernel, then the proposition is a trivial consequence of Proposition 53.2. For the converse assume that $\kappa$  is symmetric and that it satisfies the second condition of the proposition. We need to show that $\kappa$  is a positive definite kernel with respect to complex vectors. If we write $u_{k} = a_{k} + ib_{k}$, then
$$u^{*}K_{S} u = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})(a_{j} + ib_{j})(a_{k} -ib_{k})$$
$$= \sum_{j,k=1}^{p}  (a_{j}a_{k} + b_{j}b_{k})\kappa (x_{j}, x_{k}) + i \sum_{j,k=1}^{p}  (b_{j}a_{k} -a_{j}b_{k})\kappa (x_{j}, x_{k})$$
$$= \sum_{j,k=1}^{p}  (a_{j}a_{k} + b_{j}b_{k})\kappa (x_{j}, x_{k}) + i \sum_{\le j<k\le}  b_{j}a_{k}(\kappa (x_{j}, x_{k}) -\kappa (x_{k}, x_{j})).$$
$$1p$$
Thus $u^{*}K_{S}u$ is real iff $K_{S}$ is symmetric. Consequently we make the following definition.

> **Definition 53.3.** Let $X$ be a nonempty set. A function $\kappa$ : $X \times  X \to \mathbb{R}$ is a (real) positive definite kernel if $\kappa (x, y) = \kappa (y, x)$ for all $x, y \in X$, and for every finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, if $K_{S}$ is the $p \times  p$ real symmetric matrix
$$K_{S} = (\kappa (x_{i}, x_{j}))_{1\le i,j\le p},$$

<!-- PAGE 1954 -->
then we have
$$u^{\top}K_{S} u = \sum_{i,j=1}^{p}  \kappa (x_{i}, x_{j})u_{i}u_{j} \ge 0,for all u \in \mathbb{R}^{p}.$$
Among other things, the next proposition shows that a positive definite kernel satisfies the Cauchy–Schwarz inequality.

> **Proposition 53.4.** A Hermitian $2 \times  2$ matrix
$$A = \begin{pmatrix} a & \overline{b} \\ b & d \end{pmatrix}$$
is positive semidefinite if and only if $a \ge 0, d \ge 0$, and ad $-|b|^{2} \ge 0$. Let $\kappa$ : $X \times  X \to \mathbb{C}$ be a positive definite kernel. For all $x, y \in X$, we have
$$|\kappa (x, y)|^{2}\le \kappa (x, x)\kappa (y, y).$$

*Proof.* For all $x, y \in \mathbb{C}$, we have
$$\begin{pmatrix} \overline{x} & \overline{y} \end{pmatrix} \begin{pmatrix} a & \overline{b} \\ b & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \overline{x} & \overline{y} \end{pmatrix} \begin{pmatrix} ax +\overline{by} \\ bx + dy \end{pmatrix}$$
$$= a|x|^{2}+\overline{bxy} +\overline{bxy} + d|y|^{2}.$$
$$If A is positive semidefinite, then we already know \frac{that}{\overline{bxy},} a \ge 0 and d \ge 0. If a = 0, then$$
we must have $b = 0$, since otherwise we can make $\overline{bxy} +$  which is twice the real part of $\overline{bxy}$, as negative as we want. In this case, ad $-|b|^{2} = 0$. If a $> 0$, then
$$\overline{b}^{2} ||^{2}$$
$$a|x|^{2}+\overline{bxy} +\overline{bxy} + d|y|^{2}= ax +\overline{a} y+ \frac{y}{a} (ad -|b|^{2}).$$
If $ad-|b|^{2} < 0$, we can pick $y \neq  0$ and $x = -(\overline{by})/a$, so that the above expression is negative. Therefore, ad $-|b|^{2} \ge 0$. The converse is trivial. If $x = y$, the inequality $|\kappa (x, y)|^{2} \le \kappa (x, x)\kappa (y, y)$ is trivial. If x̸ $= y$, the inequality follows by applying the criterion for being positive semidefinite to the matrix
$$\begin{pmatrix} \kappa (x, x) & \overline{\kappa}\overline{(}\overline{x, y}\overline{)} \\ \kappa (x, y) & \kappa (y, y) \end{pmatrix} ,$$
as claimed. The following property due to I. Schur $(1911)$ shows that the pointwise product of two positive definite kernels is also a positive definite kernel.

<!-- PAGE 1955 -->

> **Proposition 53.5.** (I. Schur) If $\kappa_{1}$  : $X \times  X \to \mathbb{C}$ and $\kappa_{2}$  : $X \times  X \to \mathbb{C}$ are two positive definite kernels, then the function $\kappa$ : $X \times  X \to \mathbb{C}$ given by $\kappa (x, y) = \kappa_{1} (x, y)\kappa_{2} (x, y)$ for all $x, y \in X$ is also a positive definite kernel.

*Proof.* It suffices to prove that if $A = (a_{jk})$ and $B = (b_{jk})$ are two Hermitian positive semidefinite $p \times  p$ matrices, then so is their pointwise product $C = A \circ B = (a_{jk}b_{jk})$ (also known as Hadamard or Schur product). Recall that a Hermitian positive semidefinite matrix $A$ can be diagonalized as $A = U\Lambda U^{*}$ , where $\Lambda$  is a diagonal matrix with nonnegative entries and $U$ is a unitary matrix. Let $\Lambda^{1/2}$ be the diagonal matrix consisting of the positive square roots of the diagonal entries in $\Lambda$ . Then we have
$$A = U\Lambda U^{*} = U\Lambda^{1/2} \Lambda^{1/2} U^{*} = U\Lambda^{1/2} (U\Lambda^{1/2} )^{*}.$$
Thus if we set $R = U\Lambda^{1/2}$ , we have
$$A = RR^{*},$$
which means that
$$a_{jk} = \sum_{h=1}^{p}  r_{jh}\overline{r}_{kh}.$$
Then for any $u \in \mathbb{C}^{p}$, we have
$$u^{*}(A \circ B)u = \sum_{j,k=1}^{p}  a_{jk}b_{jk}u_{j}\overline{u}_{k}$$
$$= \sum_{j,k=1}^{p}  \sum_{h=1}^{p}  r_{jh}\overline{r}_{kh}b_{jk}u_{j}\overline{u}_{k}$$
$$= \sum_{h=1}^{p}  \sum_{j,k=1}^{p}  b_{jk}u_{j}r_{jh}\overline{u}_{k}\overline{r}_{kh}.$$
Since $B$ is positive semidefinite, for each fixed $h$, we have
$$\sum_{j,k=1}^{p}  b_{jk}u_{j}r_{jh}\overline{u}_{k}\overline{r}_{kh} = \sum_{j,k=1}^{p}  b_{jk}z_{j}\overline{z}_{k} \ge 0,$$
as we see by letting $z = (u_{1}r_{1h}, \dots  , u_{p}r_{ph})$, In contrast, the ordinary product $AB$ of two symmetric positive semidefinite matrices $A$ and $B$ may not be symmetric positive semidefinite; see Section 8.9 for an example. Here are other ways of obtaining new positive definite kernels from old ones.

> **Proposition 53.6.** Let $\kappa_{1}$  : $X \times X \to \mathbb{C}$ and $\kappa_{2}$  : $X \times X \to \mathbb{C}$ be two positive definite kernels,
$$\mathbb{C}\mathbb{R}^{N}  \mathbb{R}^{N} \mathbb{R}^{N} \mathbb{C}$$
$f$ : $X \to$  be a function, $\psi$ : $X \to$ be a function, $\kappa_{3}$  : $\times \to$  be a positive definite kernel, and $a \in \mathbb{R}$ be any positive real number. Then the following functions are positive definite kernels:

<!-- PAGE 1956 -->
$(1) \kappa (x, y) = \kappa_{1} (x, y) + \kappa_{2} (x, y)$.
$(2) \kappa (x, y) = a\kappa_{1} (x, y)$.
$(3) \kappa (x, y) = f(x)\overline{f}\overline{(}\overline{y}\overline{)}$.
$(4) \kappa (x, y) = \kappa_{3} (\psi (x), \psi (y))$.
$(5)$ If $B$ is a symmetric positive semidefinite $n \times  n$ matrix, then the map
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
$\kappa$ : $\times \to$  given by
$$\kappa (x, y) = x^{\top}By$$
is a positive definite kernel.

*Proof.* $(1)$ For every finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, if $K_{1}$ is the $p \times  p$ matrix
$$K_{1} = (\kappa_{1} (x_{k}, x_{j}))_{1\le j,k\le p}$$
and if if $K_{2}$ is the $p \times  p$ matrix
$$K_{2} = (\kappa_{2} (x_{k}, x_{j}))_{1\le j,k\le p},$$
then for any $u \in \mathbb{C}^{p}$, we have
$$u^{*}(K_{1} + K_{2})u = u^{*}K_{1}u + u^{*}K_{2}u \ge 0,$$
since $u^{*}K_{1}u \ge 0$ and $u^{*}K_{2}u \ge 0$ because $\kappa_{2}$  and $\kappa_{2}$  are positive definite kernels, which means that $K_{1}$ and $K_{2}$ are positive semidefinite.
$(2)$ We have
$$u^{*}(aK_{1})u = au^{*}K_{1}u \ge 0,$$
since a $> 0$ and $u^{*}K_{1}u \ge 0$.
$(3)$ For every finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, if $K$ is the $p \times  p$ matrix
$$K = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p} = (\overline{f}\overline{(}\overline{x}_{k}\overline{)} f(x_{j}))_{1\le j,k\le p}$$
then we have
$$2$$
$$u^{*}Ku = u^{\top}K^{\top}\overline{u} = \sum_{j,k=1}^{p}  \kappa (x_{j}, x_{k})u_{j}\overline{u}_{k} = \sum_{j,k=1}^{p}  u_{j}f(x_{j})\overline{u}_{k}\overline{f}\overline{(}\overline{x}_{k}\overline{) =} \sum_{j=1}^{p}  u_{j}f(x_{j})\ge 0.$$
$(4)$ For every finite subset $S = {x_{1}, \dots  , x_{p}}$ of $X$, the $p \times  p$ matrix $K$ given by
$$K = (\kappa (x_{k}, x_{j}))_{1\le j,k\le p} = (\kappa_{3} (\psi (x_{k}), \psi (x_{j})))_{1\le j,k\le p}$$
is symmetric positive semidefinite since $\kappa_{3}$  is a positive definite kernel.

<!-- PAGE 1957 -->
$(5)$ As in the proof of Proposition 53.5 (adapted to the real case) there is a matrix $R$ such that
$$B = RR^{\top},$$
so
$$\kappa (x, y) = x^{\top}By = x^{\top}RR^{\top}y = (R^{\top}x)^{\top}R^{\top}y = \langle R^{\top}x, R^{\top}y\rangle ,$$
$$\mathbb{R}^{n}$$
so $\kappa$  is the kernel function given by the feature map $\phi (x) = R^{\top}x$ from to itself, and by Proposition 53.1, it is a symmetric positive definite kernel.

> **Proposition 53.7.** Let $\kappa_{1}$  : $X \times  X \to \mathbb{C}$ be a positive definite kernel, and let p(z) be a polynomial with nonnegative coefficients. Then the following functions $\kappa$  defined below are also positive definite kernels.
$(1) \kappa (x, y) = p(\kappa_{1} (x, y))$.
$(2) \kappa (x, y) = e^{\kappa1(x,y)}$.
$(3)$ If $X$ is real Hilbert space with inner product $\langle$ -, $-\rangle_{X}$  and corresponding norm $\|\|_{X}$,
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
for any $\sigma  > 0$.

*Proof.* $(1)$ If p(z) $= a_{m}z^{m} + \cdots  + a_{1}z + a_{0}$, then
$$p(\kappa_{1} (x, y)) = a_{m}\kappa_{1} (x, y)^{m}+ \cdots  + a_{1}\kappa_{1} (x, y) + a_{0}.$$
Since $a_{k} \ge 0$ for $k = 0, \dots  , m$, by Proposition 53.5 and Proposition 53.6(2), each function $a_{k}\kappa_{i} (x, y)^{k}$ with $1 \le k \le m$ is a positive definite kernel, by Proposition 53.6(3) with
$$\sqrt$$
f(x) $= \overline{a}_{0}$, the constant function $a_{0}$ is a positive definite kernel, and by Proposition 53.6(1), $p(\kappa_{1} (x, y))$ is a positive definite kernel.
$(2)$ We have
$$e^{\kappa1(x,y)} = \sum_{k=0}^{\infty}  \frac{\kappa_{1} (x, y)^{k}}{k!} .$$
By $(1)$, the partial sums
$$\sum_{k=0}^{m}  \frac{\kappa_{1} (x, y)^{k}}{k!}$$
are positive definite kernels, and since $e^{\kappa1(x,y)}$ is the (uniform) pointwise limit of positive definite kernels, it is also a positive definite kernel.
$(3)$ By Proposition 53.6(2), since the map $(x, y) \mapsto \langle x, y\rangle_{X}$  is obviously a positive definite kernel (the feature map is the identity) and since $\sigma  \neq  0$, the function $(x, y) \mapsto \langle x, y\rangle_{X} /\sigma^{2}$ is a positive definite kernel (by Proposition 53.6(2)), so by $(2)$,
$$\kappa_{1} (x, y) =\overline{e}_{\sigma}^{\langle x,y2\rangle X}$$
