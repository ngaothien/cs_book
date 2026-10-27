# Properties of f*f


<!-- PAGE 747 -->
Chapter $22$ Singular Value Decomposition and Polar Form

## 22.1 Properties of f * \circ f

In this section we assume that we are dealing with real Euclidean spaces. Let $f$ : $E \to E$ be any linear map. In general, it may not be possible to diagonalize $f$. We show that every linear map can be diagonalized if we are willing to use two orthonormal bases. This is the celebrated singular value decomposition (SVD). A close cousin of the SVD is the polar form of a linear map, which shows how a linear map can be decomposed into its purely rotational component (perhaps with a flip) and its purely stretching part. The key observation is that $f^{*} \circ f$ is self-adjoint since
$$\langle (f^{*} \circ f)(u), v\rangle = \langle f(u), f(v)\rangle = \langle u, (f^{*} \circ f)(v)\rangle .$$
Similarly, $f \circ f^{*}$ is self-adjoint. The fact that $f^{*} \circ f$ and $f \circ f^{*}$ are self-adjoint is very important, because by Theorem 17.8, it implies that $f^{*} \circ f$ and $f \circ f^{*}$ can be diagonalized and that they have real eigenvalues. In fact, these eigenvalues are all nonnegative as shown in the following proposition.

> **Proposition 22.1.** The eigenvalues of $f^{*} \circ f$ and $f \circ f^{*}$ are nonnegative.

*Proof.* If $u$ is an eigenvector of $f^{*} \circ f$ for the eigenvalue $\lambda$ , then
$$\langle (f^{*} \circ f)(u), u\rangle = \langle f(u), f(u)\rangle$$
and
$$\langle (f^{*} \circ f)(u), u\rangle = \lambda \langle u, u\rangle ,$$
and thus
$$\lambda \langle u, u\rangle = \langle f(u), f(u)\rangle ,$$
which implies that $\lambda  \ge 0$, since $\langle$ -, $-\rangle$ is positive definite. A similar proof applies to $f \circ f^{*}$ .
$$747$$

<!-- PAGE 748 -->
Thus, the eigenvalues of $f^{*} \circ f$ are of the form $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$  or $0$, where $\sigma_{i}  > 0$, and similarly for $f \circ f^{*}$ . The above considerations also apply to any linear map $f$ : $E \to F$ between two Euclidean spaces $(E, \langle$ -, $-\rangle_{1}$ ) and $(F, \langle$ -, $-\rangle_{2}$ ). Recall that the adjoint $f^{*}$ : $F \to E$ of $f$ is the unique linear map $f^{*}$ such that
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1} ,for all u \in E and all v \in F.$$
Then $f^{*} \circ f$ and $f \circ f^{*}$ are self-adjoint (the proof is the same as in the previous case), and the eigenvalues of $f^{*} \circ f$ and $f \circ f^{*}$ are nonnegative.

*Proof.* If $\lambda$  is an eigenvalue of $f^{*} \circ f$ and $u (\neq  0)$ is a corresponding eigenvector, we have
$$\langle (f^{*} \circ f)(u), u\rangle_{1}  = \langle f(u), f(u)\rangle_{2} ,$$
and also
$$\langle (f^{*} \circ f)(u), u\rangle_{1}  = \lambda \langle u, u\rangle_{1} ,$$
so
$$\lambda \langle u, u\rangle_{1} , = \langle f(u), f(u)\rangle_{2} ,$$
which implies that $\lambda  \ge 0$. A similar proof applies to $f \circ f^{*}$ . The situation is even better, since we will show shortly that $f^{*} \circ f$ and $f \circ f^{*}$ have the same nonzero eigenvalues.
Remark: Given any two linear maps $f$ : $E \to F$ and $g: F \to E$, where dim(E) $= n$ and dim(F) $= m$, it can be shown that
$$\lambda^{m} \det(\lambda  I_{n} -g \circ f) = \lambda^{n} \det(\lambda  I_{m} -f \circ g),$$
and thus $g \circ f$ and $f \circ g$ always have the same nonzero eigenvalues; see Problem 15.14.

> **Definition 22.1.** Given any linear map $f$ : $E \to F$, the square roots $\sigma_{i}  > 0$ of the positive eigenvalues of $f^{*} \circ f$ (and $f \circ f^{*}$ ) are called the singular values of $f$.

> **Definition 22.2.** A self-adjoint linear map $f$ : $E \to E$ whose eigenvalues are nonnegative is called positive semidefinite (or positive), and if $f$ is also invertible, $f$ is said to be positive definite. In the latter case, every eigenvalue of $f$ is strictly positive. The following proposition shows that the conditions on the eigenvalues of a self-adjoint linear map used to define the notion of a positive definite linear map is equivalent to the condition used in Definition 8.4. A similar but weaker condition is equivalent to the notion of self-adjoint positive semidefinite linear map.

> **Proposition 22.2.** Let $f$ : $E \to E$ be a self-adjoint linear map, where $E$ is a Euclidean space of finite dimension with inner product $\langle -.-\rangle$ .

<!-- PAGE 749 -->
$(1)$ The eigenvalues of $f$ are strictly positive iff
$$\langle f(u), u\rangle > 0for all u \neq  0.$$
$(2)$ The eigenvalues of $f$ are nonnegative iff
$$\langle f(u), u\rangle \ge 0for all u \neq  0.$$

*Proof.* Since $f$ is self-adjoint, by the spectral theorem (Theorem 17.8), $f$ has real eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$ , and there is some orthonormal basis $(e_{1}, \dots  , e_{n})$, where $e_{i}$ is an eigenvector for $\lambda_{i}$ . With respect to this basis, every vector $u \in E$ can be written in a unique way as
$$u = \sum_{i}  n=1 x_{i}u_{i} for some x_{i} \in \mathbb{R}. Since each e_{i} is eigenvector associated with \lambda_{i}  \in \mathbb{R}, we have$$
$$f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{n}  x_{i}f(e_{i}) = \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i},$$
and using the bilinearity of the inner product, we have
$$*+$$
$$\langle f(u), u\rangle =f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  , \sum_{j=1}^{n}  x_{j}e_{j}$$
$$=* \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i}, \sum_{j=1}^{n}  x_{j}e_{j}+$$
$$= \sum_{i=1j}^{n}  \sum_{=1}^{n}  \lambda_{i} x_{i}x_{j}\langle e_{i}, e_{j}\rangle ,$$
and since $(e_{1}, \dots  , e_{n})$, is an orthonormal basis, we obtain
$$\langle f(u), u\rangle = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} .(\dagger )$$
$(1)$ If $\lambda_{i}  > 0$ for $i = 1, \dots  , n$, for any $u \neq  0$, we have $x_{i} \neq  0$ for some $i$, so $\langle$ f(u), $u\rangle =$
$$\sum_{i}  n=1 \lambda_{i} x_{i}^{2} > 0.$$
Conversely, if $\langle$ f(u), $u\rangle > 0$ for all $u \neq  0$, by picking $u = e_{i}$, we get
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} \langle e_{i}, e_{i}\rangle = \lambda_{i} ,$$
so $\lambda_{i}  > 0$ for $i = 1, \dots  , n$.
$$(2) If \lambda_{i}  \ge 0 for i = 1, \dots  , n, for any u \neq  0, then \langle f(u), u\rangle = \sum_{i}  n=1 \lambda_{i} x_{i}^{2} \ge 0.$$
Conversely, if $\langle$ f(u), $u\rangle \ge 0$ for all $u \neq  0$, by picking $u = e_{i}$, we get
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} \langle e_{i}, e_{i}\rangle = \lambda_{i} ,$$
so $\lambda_{i}  \ge 0$ for $i = 1, \dots  , n$.

<!-- PAGE 750 -->
Proposition 22.2 also holds for self-adjoint linear maps on a complex vector space with a Hermitian inner product. The proof is essentially the same and is left as an exercise to the reader. The version of Proposition 22.2 for matrices follows immediately.

> **Proposition 22.3.** Let $A$ be a real $n \times  n$ symmetric matrix.
$(1)$ The eigenvalues of $A$ are strictly positive iff
$$u^{\top}Au > 0for all u \neq  0.$$
$(2)$ The eigenvalues of $A$ are nonnegative iff
$$u^{\top}Au \ge 0for all u \neq  0.$$
It is important to note that Proposition 22.3 is false for nonsymmetric matrices.

> **Example 22.1.** The matrix
$$A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$
has the positive eigenvalues $(1, 1)$, but
$$\begin{pmatrix} 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \end{pmatrix} \begin{pmatrix} -3 \\ -1 \end{pmatrix} = -2.$$

> **Example 22.2.** The matrix
$$A = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}$$
has the complex eigenvalues $1 +$ 2i, $1$ - 2i, and yet
$$\begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} x -2y \\ 2x + y \end{pmatrix} = x^{2}+ y^{2},$$
so $u^{\top}Au > 0$ for all $u \neq  0$. Since $u^{\top}Au$ is a scalar, if $A$ is a skew symmetric matrix $(A^{\top} = -A)$, then we see that
$$u^{\top}Au = 0for all u \in \mathbb{R}.$$
Therefore, if $A$ is a real $n \times  n$ matrix then
$$u^{\top}Au = u^{\top}H(A)ufor all u \in \mathbb{R},$$
where H(A) $= (1/2)(A + A^{\top})$ is the symmetric part of $A$. This explains why the notion of a positive definite matrix is only interesting for symmetric matrices. But but one should also be aware that even if a nonsymmetric matrix $A$ has “well-behaved” eigenvalues, its symmetric part H(A) may not be positive definite.

<!-- PAGE 751 -->

> **Example 22.3.** The matrix
$$A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$
of Example 22.1 has positive eigenvalues $(1, 1)$, but its symmetric part
$$H(A) = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$$
is not positive definite, since its eigenvalues are $-1, 3$. Beware that if $A$ is a complex skew-Hermitian matrix, which means that $A^{*} = -A$, then
$$(u^{*}Au)^{*}= -u^{*}Au,$$
but this only implies that the real part of $u^{*}Au$ is zero. So for any arbitrary complex square matrix $A$, in general,
$$u^{*}Au \neq  u^{*}H(A)u,$$
where H(A) $= (1/2)(A + A^{*})$. If $f$ : $E \to F$ is any linear map, we just showed that $f^{*} \circ f$ and $f \circ f^{*}$ are positive semidefinite self-adjoint linear maps. This fact has the remarkable consequence that every linear map has two important decompositions: $1$. The polar form. $2$. The singular value decomposition (SVD). The wonderful thing about the singular value decomposition is that there exist two orthonormal bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$ such that, with respect to these bases, $f$ is a diagonal matrix consisting of the singular values of $f$ or $0$. Thus, in some sense, $f$ can always be diagonalized with respect to two orthonormal bases. The SVD is also a useful tool for solving overdetermined linear systems in the least squares sense and for data analysis, as we show later on. First we show some useful relationships between the kernels and the images of $f, f^{*} , f^{*} \circ f$, and $f \circ f^{*}$ . Recall that if $f$ : $E \to F$ is a linear map, the image Im $f$ of $f$ is the subspace f(E) of $F$, and the rank of $f$ is the dimension dim(Im $f)$ of its image. Also recall that (Theorem 6.16)
$$\dim (\mathrm{Ker} f) + \dim (\mathrm{Im} f) = \dim (E),$$
and that (Propositions 12.11 and 14.13) for every subspace $W$ of $E$,
$$\dim (W) + \dim (W^{\perp} ) = \dim (E).$$

<!-- PAGE 752 -->

> **Proposition 22.4.** Given any two Euclidean spaces $E$ and $F$, where $E$ has dimension $n$ and $F$ has dimension $m$, for any linear map $f$ : $E \to F$, we have
$$\mathrm{Ker} f = \mathrm{Ker} (f^{*} \circ f),$$
$$\mathrm{Ker} f^{*} = \mathrm{Ker} (f \circ f^{*} ),$$
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp},$$
$$\mathrm{Ker} f^{*} = (\mathrm{Im} f)^{\perp},$$
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} f^{*} ),$$
and $f, f^{*} , f^{*} \circ f$, and $f \circ f^{*}$ have the same rank.

*Proof.* To simplify the notation, we will denote the inner products on $E$ and $F$ by the same symbol $\langle$ -, $-\rangle$ (to avoid subscripts). If f(u) $= 0$, then $(f^{*} \circ$ f)(u) $= f^{*}$ (f(u)) $= f^{*} (0) = 0$, and so Ker $f \subseteq$ Ker $(f^{*} \circ f)$. By definition of $f^{*}$ , we have
$$\langle f(u), f(u)\rangle = \langle (f^{*} \circ f)(u), u\rangle$$
for all $u \in E$. If $(f^{*} \circ$ f)(u) $= 0$, since $\langle$ -, $-\rangle$ is positive definite, we must have f(u) $= 0$, and so Ker $(f^{*} \circ f) \subseteq$ Ker $f$. Therefore,
$$\mathrm{Ker} f = \mathrm{Ker} (f^{*} \circ f).$$
The proof that Ker $f^{*} =$ Ker $(f \circ f^{*}$ ) is similar. By definition of $f^{*}$ , we have
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle for all u \in E and all v \in F.(*)$$
This immediately implies that
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp}andKer f^{*} = (\mathrm{Im} f)^{\perp}.$$
Let us explain why Ker $f =$ (Im $f^{*} )^{\perp}$, the proof of the other equation being similar. Because the inner product is positive definite, for every $u \in E$, we have $\bullet  u \in$ Ker $f \bullet$  iff f(u) $= 0 \bullet$  iff $\langle$ f(u), $v\rangle = 0$ for all $v, \bullet$  by (*) iff $\langle u, f^{*} (v)\rangle = 0$ for all $v, \bullet$  iff $u \in$ (Im $f^{*} )^{\perp}$.
