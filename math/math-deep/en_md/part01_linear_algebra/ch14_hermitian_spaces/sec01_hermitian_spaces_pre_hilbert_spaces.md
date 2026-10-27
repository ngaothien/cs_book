# Hermitian Spaces, Pre-Hilbert Spaces


<!-- PAGE 529 -->
Chapter $14$ Hermitian Spaces

## 14.1 Sesquilinear and Hermitian Forms, Pre-Hilbert

$$Spaces and Hermitian Spaces$$
In this chapter we generalize the basic results of Euclidean geometry presented in Chapter $12$ to vector spaces over the complex numbers. Such a generalization is inevitable and not simply a luxury. For example, linear maps may not have real eigenvalues, but they always have complex eigenvalues. Furthermore, some very important classes of linear maps can be diagonalized if they are extended to the complexification of a real vector space. This is the case for orthogonal matrices and, more generally, normal matrices. Also, complex vector spaces are often the natural framework in physics or engineering, and they are more convenient for dealing with Fourier series. However, some complications arise due to complex conjugation. Recall that for any complex number $z \in \mathbb{C}$, if $z = x +$ iy where $x, y \in \mathbb{R}$, we let $\mathcal{ℜ} z = x$, the real part of $z$, and $\mathcal{ℑ} z = y$, the imaginary part of $z$. We also denote the conjugate of $z = x +$ iy by $\overline{z} = x$ - iy, and the absolute value (or length, or modulus) of $z$ by |z|. Recall that $|z|^{2} =\overline{zz} = x^{2} + y^{2}$. There are many natural situations where a map $\phi$ : $E \times  E \to \mathbb{C}$ is linear in its first argument and only semilinear in its second argument, which means that $\phi (u, \mu v) =\overline{\mu \phi}(u, v)$, as opposed to $\phi (u, \mu v) = \mu \phi (u, v)$. For example, the natural inner product to deal with functions $f$ : $\mathbb{R} \to \mathbb{C}$, especially Fourier series, is
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx,$$
$$\pi$$
which is semilinear (but not linear) in $g$. Thus, when generalizing a result from the real case of a Euclidean space to the complex case, we always have to check very carefully that our proofs do not rely on linearity in the second argument. Otherwise, we need to revise our proofs, and sometimes the result is simply wrong!
$$529$$

<!-- PAGE 530 -->
Before defining the natural generalization of an inner product, it is convenient to define semilinear maps.

> **Definition 14.1.** Given two vector spaces $E$ and $F$ over the complex field $\mathbb{C}$, a function $f$ : $E \to F$ is semilinear if
$$f(u + v) = f(u) + f(v),$$
$$f(\lambda u) =\overline{\lambda f}(u),$$
for all $u, v \in E$ and all $\lambda  \in \mathbb{C}$.
Remark: Instead of defining semilinear maps, we could have defined the vector space $\overline{E}$ as the vector space with the same carrier set $E$ whose addition is the same as that of $E$, but whose multiplication by a complex number is given by
$$(\lambda , u) \mapsto \overline{\lambda u.}$$
Then it is easy to check that a function $f$ : $E \to \mathbb{C}$ is semilinear iff $f$ : $\overline{E} \to \mathbb{C}$ is linear. We can now define sesquilinear forms and Hermitian forms.

> **Definition 14.2.** Given a complex vector space $E$, a function $\phi$ : $E\times E \to \mathbb{C}$ is a sesquilinear form if it is linear in its first argument and semilinear in its second argument, which means that
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v),$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2}),$$
$$\phi (\lambda u, v) = \lambda \phi (u, v),$$
$$\phi (u, \mu v) =\overline{\mu \phi}(u, v),$$
for all $u, v, u_{1}, u_{2}, v_{1}, v_{2} \in E$, and all $\lambda , \mu  \in \mathbb{C}$. A function $\phi$ : $E \times  E \to \mathbb{C}$ is a Hermitian form if it is sesquilinear and if
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)}$$
for all all $u, v \in E$. Obviously, $\phi (0, v) = \phi (u, 0) = 0$. Also note that if $\phi$ : $E \times  E \to \mathbb{C}$ is sesquilinear, we have
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = |\lambda |^{2}\phi (u, u) +\overline{\lambda \mu \phi}(u, v) +\overline{\lambda \mu \phi}(v, u) + |\mu |^{2}\phi (v, v),$$
and if $\phi$ : $E \times  E \to \mathbb{C}$ is Hermitian, we have
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = |\lambda |^{2}\phi (u, u) + 2\mathcal{ℜ}(\overline{\lambda \mu \phi}(u, v)) + |\mu |^{2}\phi (v, v).$$
Note that restricted to real coefficients, a sesquilinear form is bilinear (we sometimes say $\mathbb{R}-bilinear)$.

<!-- PAGE 531 -->

> **Definition 14.3.** Given a sesquilinear form $\phi$ : $E \times  E \to \mathbb{C}$, the function $\Phi$ : $E \to \mathbb{C}$ defined such that $\Phi (u) = \phi (u, u)$ for all $u \in E$ is called the quadratic form associated with $\phi$ .
$$\mathbb{C}^{n}$$
The standard example of a Hermitian form on is the map $\phi$  defined such that
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}\overline{y}_{1} + x_{2}\overline{y}_{2} + \cdots  + x_{n}\overline{y}_{n}.$$
This map is also positive definite, but before dealing with these issues, we show the following useful proposition.

> **Proposition 14.1.** Given a complex vector space $E$, the following properties hold:
$(1) A$ sesquilinear form $\phi$ : $E \times E \to \mathbb{C}$ is a Hermitian form iff $\phi (u, u) \in \mathbb{R}$ for all $u \in E$.
$(2)$ If $\phi$ : $E \times  E \to \mathbb{C}$ is a sesquilinear form, then
$$4\phi (u, v) = \phi (u + v, u + v) -\phi (u -v, u -v)$$
$$+ i\phi (u + iv, u + iv) -i\phi (u -iv, u -iv),$$
and
$$2\phi (u, v) = (1 + i)(\phi (u, u) + \phi (v, v)) -\phi (u -v, u -v) -i\phi (u -iv, u -iv).$$
These are called polarization identities.

*Proof.* $(1)$ If $\phi$  is a Hermitian form, then
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)}$$
implies that
$$\phi (u, u) =\overline{\phi}\overline{(}\overline{u, u}\overline{)},$$
and thus $\phi (u, u) \in \mathbb{R}$. If $\phi$  is sesquilinear and $\phi (u, u) \in \mathbb{R}$ for all $u \in E$, then
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v),$$
which proves that
$$\phi (u, v) + \phi (v, u) = \alpha ,$$
where $\alpha$  is real, and changing $u$ to iu, we have
$$i(\phi (u, v) -\phi (v, u)) = \beta ,$$
where $\beta$  is real, and thus
$$\phi (u, v) = \frac{\alpha i\beta}{2} -and\phi (v, u) = \frac{\alpha  + i\beta}{2} ,$$
proving that $\phi$  is Hermitian.
$(2)$ These identities are verified by expanding the right-hand side, and we leave them as an exercise.

<!-- PAGE 532 -->
Proposition 14.1 shows that a sesquilinear form is completely determined by the quadratic form $\Phi (u) = \phi (u, u)$, even if $\phi$  is not Hermitian. This is false for a real bilinear form, unless
$$\mathbb{R}^{2} \mathbb{R}^{2} \mathbb{R}$$
it is symmetric. For example, the bilinear form $\phi$ : $\times \to$  defined such that
$$\phi ((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}y_{2} -x_{2}y_{1}$$
is not identically zero, and yet it is null on the diagonal. However, a real symmetric bilinear form is indeed determined by its values on the diagonal, as we saw in Chapter $12$. As in the Euclidean case, Hermitian forms for which $\phi (u, u) \ge 0$ play an important role.

> **Definition 14.4.** Given a complex vector space $E$, a Hermitian form $\phi$ : $E \times  E \to \mathbb{C}$ is positive if $\phi (u, u) \ge 0$ for all $u \in E$, and positive definite if $\phi (u, u) > 0$ for all $u \neq  0$. A pair $\langle E, \phi \rangle$ where $E$ is a complex vector space and $\phi$  is a Hermitian form on $E$ is called a pre-Hilbert space if $\phi$  is positive, and a Hermitian (or unitary) space if $\phi$  is positive definite. We warn our readers that some authors, such as Lang $[115]$, define a pre-Hilbert space as what we define as a Hermitian space. We prefer following the terminology used in Schwartz $[156]$ and Bourbaki $[27]$. The quantity $\phi (u, v)$ is usually called the Hermitian product of $u$ and $v$. We will occasionally call it the inner product of $u$ and $v$. Given a pre-Hilbert space $\langle E, \phi \rangle$ , as in the case of a Euclidean space, we also denote $\phi (u, v)$ by
$$u \cdot  vor\langle u, v\rangle or(u|v),$$
and $p\overline{\Phi (}\overline{u}\overline{)}$ by $\|u\|$.
$$\mathbb{C}^{n}$$

> **Example 14.1.** The complex vector space under the Hermitian form
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}\overline{y}_{1} + x_{2}\overline{y}_{2} + \cdots  + x_{n}\overline{y}_{n}$$
is a Hermitian space.

> **Example 14.2.** Let $\ell^{2}$ denote the set of all countably infinite sequences $x = (x_{i})_{i\in N}$ of
$$\infty  n$$
$$complex numbers such that \sum_{i}  |x_{i}|^{2}is defined  (i.e.,  \mathbb{C} the sequence \sum_{i}  =0 |x_{i}|^{2}converges as$$
$n \to \infty$ ). It can be shown $that^{=0}$ the map $\phi$ : $\ell^{2} \times  \ell^{2} \to$  defined such that
$$\phi  ((x_{i})_{i\in N}, (y_{i})_{i\in N}) = \sum_{i=0}^{\infty}  x_{i}\overline{y}_{i}$$
is well defined, and $\ell^{2}$ is a Hermitian space under $\phi$ . Actually, $\ell^{2}$ is even a Hilbert space.

> **Example 14.3.** Let $\mathcal{C}_{piece}[a, b]$ be the set of bounded piecewise continuous functions $f$ : [a, $b] \to \mathbb{C}$ under the Hermitian form
$$\langle f, g\rangle = \int_{a}^{}  bf(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
It is easy to check that this Hermitian form is positive, but it is not definite. Thus, under this Hermitian form, $\mathcal{C}_{piece}[a, b]$ is only a pre-Hilbert space.

<!-- PAGE 533 -->

> **Example 14.4.** Let $\mathcal{C}[a, b]$ be the set of complex-valued continuous functions $f$ : [a, $b] \to \mathbb{C}$ under the Hermitian form
$$\langle f, g\rangle = \int_{a}^{}  bf(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
It is easy to check that this Hermitian form is positive definite. Thus, $\mathcal{C}[a, b]$ is a Hermitian space.

> **Example 14.5.** Let $E = M_{n}(\mathbb{C})$ be the vector space of complex $n \times  n$ matrices. If we view a matrix $A \in M_{n}(\mathbb{C})$ as a “long” column vector obtained by concatenating together its columns, we can define the Hermitian product of two matrices $A, B \in M_{n}(\mathbb{C})$ as
$$\langle A, B\rangle = \sum_{i,j=1}^{n}  a_{ij}\overline{b}_{ij},$$
which can be conveniently written as
$$\langle A, B\rangle = \mathrm{tr}(A^{\top}\overline{B}) = \mathrm{tr}(B^{*}A).$$
Since this can be viewed as the standard Hermitian product $on\mathbb{C}^{n2}$, it is a Hermitian product on $M_{n}(\mathbb{C})$. The corresponding norm
$$\|A\|_{F} =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{)}$$
is the Frobenius norm (see Section 9.2). If $E$ is finite-dimensional and if $\phi$ : $E \times  E \to \mathbb{R}$ is a sequilinear form on $E$, given any
$$basis (e_{1}, \dots  , e_{n}) of E, we can write x = \sum_{ni}  n=1 x_{i}e_{i} and y = \sum  nj=1 y_{j}e_{j}, and we have$$
$$\phi (x, y) = \phi \begin{pmatrix} x_{i}e_{i}, & y_{j}e_{j} \end{pmatrix} \sum_{i=1}^{n}  \sum_{j=1}  = \sum_{i,j=1}^{n}  x_{i}\overline{y}_{j}\phi (e_{i}, e_{j}).$$
If we let $G = (g_{ij})$ be the matrix given by $g_{ij} = \phi (e_{j}, e_{i})$, and if $x$ and $y$ are the column vectors associated with $(x_{1}, \dots  , x_{n})$ and $(y_{1}, \dots  , y_{n})$, then we can write
$$\phi (x, y) = x^{\top}G^{\top}\overline{y} = y^{*}Gx,$$
$where\overline{y}$ corresponds to $(\overline{y}_{1}\overline{, \dots  , y}_{n})$. As in Section 12.1, we are committing the slight abuse of
$$notation of letting x denote both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated$$
with $(x_{1}, \dots  , x_{n})$ (and similarly for $y)$. The “correct” expression for $\phi (x, y)$ is
$$\phi (x, y) = y^{*}Gx = x^{\top}G^{\top}\overline{y}.$$
 Observe that in $\phi (x, y) = y^{*}Gx$, the matrix involved is the transpose of the matrix $(\phi (e_{i}, e_{j}))$. The reason for this is that we want $G$ to be positive definite when $\phi$  is positive definite, not $G^{\top}$.

<!-- PAGE 534 -->
Furthermore, observe that $\phi$  is Hermitian iff $G = G^{*}$, and $\phi$  is positive definite iff the matrix $G$ is positive definite, that is,
$$(Gx)^{\top}\overline{x} = x^{*}Gx > 0for all x \in \mathbb{C}^{n}, x \neq  0.$$

> **Definition 14.5.** The matrix $G$ associated with a Hermitian product is called the Gram matrix of the Hermitian product with respect to the basis $(e_{1}, \dots  , e_{n})$. Conversely, if $A$ is a Hermitian positive definite $n \times  n$ matrix, it is easy to check that the Hermitian form
$$\langle x, y\rangle = y^{*}Ax$$
is positive definite. If we make a change of basis from the basis $(e_{1}, \dots  , e_{n})$ to the basis $(f_{1}, \dots  , f_{n})$, and if the change of basis matrix is $P$ (where the jth column of $P$ consists of the coordinates of $f_{j}$ over the basis $(e_{1}, \dots  , e_{n}))$, then with respect to coordinates x' and y' over the basis $(f_{1}, \dots  , f_{n})$, we have
$$y^{*}Gx = (y')^{*}P^{*} GPx',$$
so the matrix of our inner product over the basis $(f_{1}, \dots  , f_{n})$ is $P^{*}$ GP. We summarize these facts in the following proposition.

> **Proposition 14.2.** Let $E$ be a finite-dimensional vector space, and let $(e_{1}, \dots  , e_{n})$ be a basis of $E. 1$. For any Hermitian inner product $\langle$ -, $-\rangle$ on $E$, if $G = (g_{ij})$ with $g_{ij} = \langle e_{j}, e_{i}\rangle$ is the Gram matrix of the Hermitian product $\langle$ -, $-\rangle$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, then $G$ is Hermitian positive definite. $2$. For any change of basis matrix $P$, the Gram matrix of $\langle$ -, $-\rangle$ with respect to the new basis is $P^{*}$ GP. $3$. If $A$ is any $n \times  n$ Hermitian positive definite matrix, then
$$\langle x, y\rangle = y^{*}Ax$$
is a Hermitian product on $E$. We will see later that a Hermitian matrix is positive definite iff its eigenvalues are all positive. The following result reminiscent of the first polarization identity of Proposition 14.1 can be used to prove that two linear maps are identical.

> **Proposition 14.3.** Given any Hermitian space $E$ with Hermitian product $\langle$ -, $-\rangle$ , for any linear map $f$ : $E \to E$, if $\langle$ f(x), $x\rangle = 0$ for all $x \in E$, then $f = 0$.

<!-- PAGE 535 -->

*Proof.* Compute $\langle$ f(x $+ y), x + y\rangle$ and $\langle$ f(x - $y), x$ - $y\rangle$ :
$$\langle f(x + y), x + y\rangle = \langle f(x), x\rangle + \langle f(x), y\rangle + \langle f(y), x\rangle + \langle y, y\rangle$$
$$\langle f(x -y), x -y\rangle = \langle f(x), x\rangle -\langle f(x), y\rangle -\langle f(y), x\rangle + \langle y, y\rangle ;$$
then subtract the second equation from the first to obtain
$$\langle f(x + y), x + y\rangle -\langle f(x -y), x -y\rangle = 2(\langle f(x), y\rangle + \langle f(y), x\rangle ).$$
If $\langle$ f(u), $u\rangle = 0$ for all $u \in E$, we get
$$\langle f(x), y\rangle + \langle f(y), x\rangle = 0for all x, y \in E.$$
Then the above equation also holds if we replace $x$ by ix, and we obtain
$$i\langle f(x), y\rangle -i\langle f(y), x\rangle = 0,for all x, y \in E,$$
so we have
$$\langle f(x), y\rangle + \langle f(y), x\rangle = 0$$
$$\langle f(x), y\rangle -\langle f(y), x\rangle = 0,$$
which implies that $\langle$ f(x), $y\rangle = 0$ for all $x, y \in E$. Since $\langle$ -, $-\rangle$ is positive definite, we have f(x) $= 0$ for all $x \in E$; that is, $f = 0$. One should be careful not to apply Proposition 14.3 to a linear map on a real Euclidean space because it is false! The reader should find a counterexample. The Cauchy–Schwarz inequality and the Minkowski inequalities extend to pre-Hilbert spaces and to Hermitian spaces.

> **Proposition 14.4.** Let $\langle E, \phi \rangle$ be a pre-Hilbert space with associated quadratic form $\Phi$ . For all $u, v \in E$, we have the Cauchy–Schwarz inequality
$$|\phi (u, v)| \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Furthermore, if $\langle E, \phi \rangle$ is a Hermitian space, the equality holds iff $u$ and $v$ are linearly dependent. We also have the Minkowski inequality
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}.$$
Furthermore, if $\langle E, \phi \rangle$ is a Hermitian space, the equality holds iff $u$ and $v$ are linearly dependent, where in addition, if u̸ $= 0$ and v̸ $= 0$, then $u = \lambda v$ for some real $\lambda$  such that $\lambda  > 0$.

<!-- PAGE 536 -->

*Proof.* For all $u, v \in E$ and all $\mu  \in \mathbb{C}$, we have observed that
$$\phi (u + \mu v, u + \mu v) = \phi (u, u) + 2\mathcal{ℜ}(\overline{\mu \phi}(u, v)) + |\mu |^{2}\phi (v, v).$$
Let $\phi (u, v) = \rho e^{i\theta}$, where $|\phi (u$, v)| $= \rho  (\rho  \ge 0)$. Let $F$ : $\mathbb{R} \to \mathbb{R}$ be the function defined such that
$$F(t) = \Phi (u + te^{i\theta}v),$$
for all $t \in \mathbb{R}$. The above shows that
$$F(t) = \phi (u, u) + 2t|\phi (u, v)| + t^{2}\phi (v, v) = \Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v).$$
Since $\phi$  is assumed to be positive, we have F(t) $\ge 0$ for all $t \in \mathbb{R}$. If $\Phi (v) = 0$, we must have $\phi (u, v) = 0$, since otherwise, F(t) could be made negative by choosing $t$ negative and small enough. If $\Phi (v) > 0$, in order for F(t) to be nonnegative, the equation
$$\Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v) = 0$$
must not have distinct real roots, which is equivalent to
$$|\phi (u, v)|^{2}\le \Phi (u)\Phi (v).$$
Taking the square root on both sides yields the Cauchy–Schwarz inequality. For the second part of the claim, if $\phi$  is positive definite, we argue as follows. If $u$ and $v$ are linearly dependent, it is immediately verified that we get an equality. Conversely, if
$$|\phi (u, v)|^{2}= \Phi (u)\Phi (v),$$
then there are two cases. If $\Phi (v) = 0$, since $\phi$  is positive definite, we must have $v = 0$, so $u$ and $v$ are linearly dependent. Otherwise, the equation
$$\Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v) = 0$$
has a double root $t_{0}$, and thus
$$\Phi (u + t_{0}e^{i\theta}v) = 0.$$
Since $\phi$  is positive definite, we must have
$$u + t_{0}e^{i\theta}v = 0,$$
which shows that $u$ and $v$ are linearly dependent. If we square the Minkowski inequality, we get
$$\Phi (u + v) \le \Phi (u) + \Phi (v) + 2p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
However, we observed earlier that
$$\Phi (u + v) = \Phi (u) + \Phi (v) + 2\mathcal{ℜ}(\phi (u, v)).$$

<!-- PAGE 537 -->
Thus, it is enough to prove that
$$\mathcal{ℜ}(\phi (u, v)) \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
but this follows from the Cauchy–Schwarz inequality
$$|\phi (u, v)| \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}$$
and the fact that $\mathcal{ℜ} z \le$ |z|. If $\phi$  is positive definite and $u$ and $v$ are linearly dependent, it is immediately verified that we get an equality. Conversely, if equality holds in the Minkowski inequality, we must have
$$\mathcal{ℜ}(\phi (u, v)) =p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
which implies that
$$|\phi (u, v)| =p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
since otherwise, by the Cauchy–Schwarz inequality, we would have
$$\mathcal{ℜ}(\phi (u, v)) \le |\phi (u, v)| <p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Thus, equality holds in the Cauchy–Schwarz inequality, and
$$\mathcal{ℜ}(\phi (u, v)) = |\phi (u, v)|.$$
But then we proved in the Cauchy–Schwarz case that $u$ and $v$ are linearly dependent. Since we also just proved that $\phi (u, v)$ is real and nonnegative, the coefficient of proportionality between $u$ and $v$ is indeed nonnegative. As in the Euclidean case, if $\langle$   Hermitian space, the Minkowski inequality
$$p \frac{E, \phi \rangle isa}{\Phi (u + v)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}$$
$$shows that the map u \mapsto p\overline{\Phi (}\overline{u}\overline{)} is a norm on E. \frac{The}{\Phi (u)} norm induced by \phi  is called the$$
Hermitian norm induced by $\phi$ . We usually denote $p$  by $\|u\|$, and the Cauchy–Schwarz inequality is written as
$$|u \cdot  v| \le \|u\|\|v\|.$$
Since a Hermitian space is a normed vector space, it is a topological space under the topology induced by the norm (a basis for this topology is given by the open balls $B_{0}(u, \rho$ ) of center $u$ and radius $\rho  > 0$, where
$$B_{0}(u, \rho ) = {v \in E | \|v -u\|< \rho }.$$
If $E$ has finite dimension, every linear map is continuous; see Chapter $9$ (or Lang $[115, 116]$, Dixmier $[52]$, or Schwartz $[156, 157])$. The Cauchy–Schwarz inequality
$$|u \cdot  v| \le \|u\|\|v\|$$
