# Normal Linear Maps: Eigenvalues and Eigenvectors


<!-- PAGE 625 -->
Chapter $17$ Spectral Theorems in Euclidean and Hermitian Spaces

## 17.1 Introduction

The goal of this chapter is to show that there are nice normal forms for symmetric matrices, skew-symmetric matrices, orthogonal matrices, and normal matrices. The spectral theorem for symmetric matrices states that symmetric matrices have real eigenvalues and that they can be diagonalized over an orthonormal basis. The spectral theorem for Hermitian matrices states that Hermitian matrices also have real eigenvalues and that they can be diagonalized over a complex orthonormal basis. Normal real matrices can be block diagonalized over an orthonormal basis with blocks having size at most two and there are refinements of this normal form for skew-symmetric and orthogonal matrices. The spectral result for real symmetric matrices can be used to prove two characterizations of the eigenvalues of a symmetric matrix in terms of the Rayleigh ratio. The first characterization is the Rayleigh–Ritz theorem and the second one is the Courant–Fischer theorem. Both results are used in optimization theory and to obtain results about perturbing the eigenvalues of a symmetric matrix. In this chapter all vector spaces are finite-dimensional real or complex vector spaces.

## 17.2 Normal Linear Maps: Eigenvalues and Eigenvec-

$$tors$$
We begin by studying normal maps, to understand the structure of their eigenvalues and eigenvectors. This section and the next three were inspired by Lang $[113]$, Artin $[7]$, Mac Lane and Birkhoff[122], Berger $[11]$, and Bertin $[15]$.
$$625$$

<!-- PAGE 626 -->

> **Definition 17.1.** Given a Euclidean or Hermitian space $E$, a linear map $f$ : $E \to E$ is normal if
$$f \circ f^{*} = f^{*} \circ f.$$
A linear map $f$ : $E \to E$ is self-adjoint if $f = f^{*}$ , skew-self-adjoint if $f = -f^{*}$ , and orthogonal if $f \circ f^{*} = f^{*} \circ f =$ id. Obviously, a self-adjoint, skew-self-adjoint, or orthogonal linear map is a normal linear map. Our first goal is to show that for every normal linear map $f$ : $E \to E$, there is an orthonormal basis (w.r.t. $\langle$ -, $-\rangle$ ) such that the matrix of $f$ over this basis has an especially nice form: it is a block diagonal matrix in which the blocks are either one-dimensional matrices (i.e., single entries) or two-dimensional matrices of the form
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix} .$$
This normal form can be further refined if $f$ is self-adjoint, skew-self-adjoint, or orthogonal. As a first step we show that $f$ and $f^{*}$ have the same kernel when $f$ is normal.

> **Proposition 17.1.** Given a Euclidean space $E$, if $f$ : $E \to E$ is a normal linear map, then Ker $f =$ Ker $f^{*}$ .

*Proof.* First let us prove that
$$\langle f(u), f(v)\rangle = \langle f^{*} (u), f^{*} (v)\rangle$$
for all $u, v \in E$. Since $f^{*}$ is the adjoint of $f$ and $f \circ f^{*} = f^{*} \circ f$, we have
$$\langle f(u), f(u)\rangle = \langle u, (f^{*} \circ f)(u)\rangle ,$$
$$= \langle u, (f \circ f^{*} )(u)\rangle ,$$
$$= \langle f^{*} (u), f^{*} (u)\rangle .$$
Since $\langle$ -, $-\rangle$ is positive definite,
$$\langle f(u), f(u)\rangle = 0ifff(u) = 0,$$
$$\langle f^{*} (u), f^{*} (u)\rangle = 0ifff^{*} (u) = 0,$$
and since
$$\langle f(u), f(u)\rangle = \langle f^{*} (u), f^{*} (u)\rangle ,$$
we have
$$f(u) = 0ifff^{*} (u) = 0.$$
Consequently, Ker $f =$ Ker $f^{*}$ .

<!-- PAGE 627 -->
Assuming again that $E$ is a Hermitian space, observe that Proposition 17.1 also holds. We deduce the following corollary.

> **Proposition 17.2.** Given a Hermitian space $E$, for any normal linear map $f$ : $E \to E$, we have Ker $(f) \cap$ Im(f) $= (0)$.

*Proof.* Assume $v \in$ Ker $(f) \cap$ Im(f), which means that $v =$ f(u) for some $u \in E$, and f(v) $= 0$. By Proposition 17.1, Ker $(f) =$ Ker $(f^{*}$ ), so f(v) $= 0$ implies that $f^{*} (v) = 0$. Consequently,
$$0 = \langle f^{*} (v), u\rangle$$
$$= \langle v, f(u)\rangle$$
$$= \langle v, v\rangle ,$$
and thus, $v = 0$. We also have the following crucial proposition relating the eigenvalues of $f$ and $f^{*}$ .

> **Proposition 17.3.** Given a Hermitian space $E$, for any normal linear map $f$ : $E \to E$, a vector $u$ is an eigenvector of $f$ for the eigenvalue $\lambda$  (in $\mathbb{C})$ iff $u$ is an eigenvector of $f^{*}$ for the eigenvalue $\overline{\lambda}$.

*Proof.* First it is immediately verified that the adjoint of $f$ - $\lambda$  id is $f^{*}$ - $\overline{\lambda}$ id. Furthermore, $f$ - $\lambda$  id is normal. Indeed,
$$(f -\lambda  id) \circ (f -\lambda  id)^{*}= (f -\lambda  id) \circ (f^{*} -\overline{\lambda} id),$$
$$= f \circ f^{*} -\overline{\lambda f} -\lambda f^{*} +\overline{\lambda \lambda} id,$$
$$= f^{*} \circ f -\lambda f^{*} -\overline{\lambda f} +\overline{\lambda \lambda} id,$$
$$= (f^{*} -\overline{\lambda} id) \circ (f -\lambda  id),$$
$$= (f -\lambda  id)^{*}\circ (f -\lambda  id).$$
Applying Proposition 17.1 to $f$ - $\lambda$  id, for every nonnull vector $u$, we see that
$$(f -\lambda  id)(u) = 0iff(f^{*} -\overline{\lambda} id)(u) = 0,$$
which is exactly the statement of the proposition. The next proposition shows a very important property of normal linear maps: eigenvectors corresponding to distinct eigenvalues are orthogonal.

> **Proposition 17.4.** Given a Hermitian space $E$, for any normal linear map $f$ : $E \to E$, if $u$ and $v$ are eigenvectors of $f$ associated with the eigenvalues $\lambda$  and $\mu$  (in $\mathbb{C})$ where $\lambda  \neq  \mu$ , then $\langle u, v\rangle = 0$.

<!-- PAGE 628 -->

*Proof.* Let us compute $\langle$ f(u), $v\rangle$ in two different ways. Since $v$ is an eigenvector of $f$ for $\mu$ , by Proposition 17.3, $v$ is also an eigenvector of $f^{*}$ for $\overline{\mu}$, and we have
$$\langle f(u), v\rangle = \langle \lambda u, v\rangle = \lambda \langle u, v\rangle ,$$
and
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle = \langle \overline{u, \mu v}\rangle = \mu \langle u, v\rangle ,$$
where the last identity holds because of the semilinearity in the second argument. Thus
$$\lambda \langle u, v\rangle = \mu \langle u, v\rangle ,$$
that is,
$$(\lambda  -\mu )\langle u, v\rangle = 0,$$
which implies that $\langle u, v\rangle = 0$, since $\lambda  \neq  \mu$ . We can show easily that the eigenvalues of a self-adjoint linear map are real.

> **Proposition 17.5.** Given a Hermitian space $E$, all the eigenvalues of any self-adjoint linear map $f$ : $E \to E$ are real.

*Proof.* Let $z$ (in $\mathbb{C})$ be an eigenvalue of $f$ and let $u$ be an eigenvector for $z$. We compute $\langle$ f(u), $u\rangle$ in two different ways. We have
$$\langle f(u), u\rangle = \langle zu, u\rangle = z\langle u, u\rangle ,$$
and since $f = f^{*}$ , we also have
$$\langle f(u), u\rangle = \langle u, f^{*} (u)\rangle = \langle u, f(u)\rangle = \langle u, zu\rangle =\overline{z}\langle u, u\rangle .$$
Thus,
$$z\langle u, u\rangle =\overline{z}\langle u, u\rangle ,$$
which implies that $z =\overline{z}$, since $u \neq  0$, and $z$ is indeed real. There is also a version of Proposition 17.5 for a (real) Euclidean space $E$ and a self-adjoint map $f$ : $E \to E$ since every real vector space $E$ can be embedded into a complex vector space $E_{C}$, and every linear map $f$ : $E \to E$ can be extended to a linear map $f_{C}$ : $E_{C} \to E_{C}$.

> **Definition 17.2.** Given a real vector space $E$, let $E_{C}$ be the structure $E \times  E$ under the addition operation
$$(u_{1}, u_{2}) + (v_{1}, v_{2}) = (u_{1} + v_{1}, u_{2} + v_{2}),$$
and let multiplication by a complex scalar $z = x +$ iy be defined such that
$$(x + iy) \cdot  (u, v) = (xu -yv, yu + xv).$$
The space $E_{C}$ is called the complexification of $E$.

<!-- PAGE 629 -->
It is easily shown that the structure $E_{C}$ is a complex vector space. It is also immediate that
$$(0, v) = i(v, 0),$$
and thus, identifying $E$ with the subspace of $E_{C}$ consisting of all vectors of the form $(u, 0)$, we can write
$$(u, v) = u + iv.$$
Observe that if $(e_{1}, \dots  , e_{n})$ is a basis of $E$ (a real vector space), then $(e_{1}, \dots  , e_{n})$ is also a basis of $E_{C}$ (recall that $e_{i}$ is an abbreviation for $(e_{i}, 0))$. A linear map $f$ : $E \to E$ is extended to the linear map $f_{C}$ : $E_{C} \to E_{C}$ defined such that
$$f_{C}(u + iv) = f(u) + if(v).$$
For any basis $(e_{1}, \dots  , e_{n})$ of $E$, the matrix M(f) representing $f$ over $(e_{1}, \dots  , e_{n})$ is identical to the matrix $M(f_{C})$ representing $f_{C}$ over $(e_{1}, \dots  , e_{n})$, where we view $(e_{1}, \dots  , e_{n})$ as a basis of $E_{C}$. As a consequence, det(zI - M(f)) $=$ det(zI - $M(f_{C}))$, which means that $f$ and $f_{C}$ have the same characteristic polynomial (which has real coefficients). We know that every polynomial of degree $n$ with real (or complex) coefficients always has $n$ complex roots (counted with their multiplicity), and the roots of det(zI $-M(f_{C}))$ that are real (if any) are the eigenvalues of $f$. Next we need to extend the inner product on $E$ to an inner product on $E_{C}$. The inner product $\langle$ -, $-\rangle$ on a Euclidean space $E$ is extended to the Hermitian positive definite form $\langle$ -, $-\rangle_{C}$  on $E_{C}$ as follows:
$$\langle u_{1} + iv_{1}, u_{2} + iv_{2}\rangle_{C}  = \langle u_{1}, u_{2}\rangle + \langle v_{1}, v_{2}\rangle + i(\langle v_{1}, u_{2}\rangle -\langle u_{1}, v_{2}\rangle ).$$
It is easily verified that $\langle$ -, $-\rangle_{C}$  is indeed a Hermitian form that is positive definite, and it is clear that $\langle$ -, $-\rangle_{C}$  agrees with $\langle$ -, $-\rangle$ on real vectors. Then given any linear map $f$ : $E \to E$, it is easily verified that the map $f_{C}^{*}$  defined such that
$$f_{C}^{*} (u + iv) = f^{*}(u) + if^{*}(v)$$
for all $u, v \in E$ is the adjoint of $f_{C}$ w.r.t. $\langle$ -, $-\rangle_{C}$ .

> **Proposition 17.6.** Given a Euclidean space $E$, if $f$ : $E \to E$ is any self-adjoint linear map, then every eigenvalue $\lambda$  of $f_{C}$ is real and is actually an eigenvalue of $f$ (which means that there is some real eigenvector $u \in E$ such that f(u) $= \lambda u)$. Therefore, all the eigenvalues of $f$ are real.

<!-- PAGE 630 -->

*Proof.* Let $E_{C}$ be the complexification of $E, \langle$ -, $-\rangle_{C}$  the complexification of the inner product $\langle$ -, $-\rangle$ on $E$, and $f_{C}$ : $E_{C} \to E_{C}$ the complexification of $f$ : $E \to E$. By definition of $f_{C}$ and $\langle$ -, $-\rangle_{C}$ , if $f$ is self-adjoint, we have $\langle f_{C}(u_{1} + iv_{1}), u_{2} + iv_{2}\rangle_{C}  = \langle f(u_{1}) + if(v_{1}), u_{2} + iv_{2}\rangle_{C}$
$$= \langle f(u_{1}), u_{2}\rangle + \langle f(v_{1}), v_{2}\rangle + i(\langle u_{2}, f(v_{1})\rangle -\langle f(u_{1}), v_{2}\rangle )$$
$$= \langle u_{1}, f(u_{2})\rangle + \langle v_{1}, f(v_{2})\rangle + i(\langle f(u_{2}), v_{1}\rangle -\langle u_{1}, f(v_{2})\rangle )$$
$$= \langle u_{1} + iv_{1}, f(u_{2}) + if(v_{2})\rangle_{C}$$
$$= \langle u_{1} + iv_{1}, f_{C}(u_{2} + iv_{2})\rangle_{C} ,$$
which shows that $f_{C}$ is also self-adjoint with respect to $\langle$ -, $-\rangle_{C}$ . As we pointed out earlier, $f$ and $f_{C}$ have the same characteristic polynomial $det(zI-f_{C}) =$ det(zI - $f)$, which is a polynomial with real coefficients. Proposition 17.5 shows that the zeros of det(zI - $f_{C}) =$ det(zI - $f)$ are all real, and for each real zero $\lambda$  of det(zI - $f)$, the linear map $\lambda$ id - $f$ is singular, which means that there is some nonzero $u \in E$ such that f(u) $= \lambda u$. Therefore, all the eigenvalues of $f$ are real.

> **Proposition 17.7.** Given a Hermitian space $E$, for any linear map $f$ : $E \to E$, if $f$ is skewself-adjoint, then $f$ has eigenvalues that are pure imaginary or zero, and if $f$ is unitary, then $f$ has eigenvalues of absolute value $1$.

*Proof.* If $f$ is skew-self-adjoint, $f^{*} = -f$, and then by the definition of the adjoint map, for any eigenvalue $\lambda$  and any eigenvector $u$ associated with $\lambda$ , we have
$$\lambda \langle u, u\rangle = \langle \lambda u, u\rangle = \langle f(u), u\rangle = \langle u, f^{*} (u)\rangle = \langle u, -f(u)\rangle = -\langle u, \lambda u\rangle = -\overline{\lambda}\langle u, u\rangle ,$$
and since $u \neq  0$ and $\langle$ -, $-\rangle$ is positive definite, $\langle u, u\rangle$ ̸ $= 0$, so
$$\lambda  = -\overline{\lambda ,}$$
which shows that $\lambda  =$ ir for some $r \in \mathbb{R}$. If $f$ is unitary, then $f$ is an isometry, so for any eigenvalue $\lambda$  and any eigenvector $u$ associated with $\lambda$ , we have
$$|\lambda |^{2}\langle u, u\rangle =\overline{\lambda \lambda}\langle u, u\rangle = \langle \lambda u, \lambda u\rangle = \langle f(u), f(u)\rangle = \langle u, u\rangle ,$$
and since $u \neq  0$, we obtain $|\lambda |^{2} = 1$, which implies
$$|\lambda | = 1.$$
