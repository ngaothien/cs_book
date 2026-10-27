# Orthogonal Projections and Involutions


<!-- PAGE 553 -->

## 14.6 Orthogonal Projections and Involutions

In this section we begin by assuming that the field $K$ is not a field of characteristic $2$. Recall that a linear map $f$ : $E \to E$ is an involution iff $f^{2} =$ id, and is idempotent iff $f^{2} = f$. We know from Proposition 6.9 that if $f$ is idempotent, then
$$E = \mathrm{Im}(f) \oplus \mathrm{Ker} (f),$$
and that the restriction of $f$ to its image is the identity. For this reason, a linear idempotent map is called a projection. The connection between involutions and projections is given by the following simple proposition.

> **Proposition 14.22.** For any linear map $f$ : $E \to E$, we have $f^{2} =$ id $iff_{2}^{1}(id$ - $f)$ is a projection $iff_{2}^{1}(id + f)$ is a projection; in this case, $f$ is equal to the difference of the two $projections_{2}^{1}$ (id $+ f) and_{2}^{1}$ (id - $f)$.

*Proof.* We have
$$2$$
$$\begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \frac{1}{4} (id -2f + f^{2})$$
so
$$2$$
$$\begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \frac{1}{2} (id -f)iff f^{2}= id.$$
We also have
$$2$$
$$\begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} = \frac{1}{4} (id + 2f + f^{2}),$$
so
$$2$$
$$\begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} = \frac{1}{2} (id + f)iff f^{2}= id.$$
Obviously, $f =_{2}^{1}$ (id $+ f) -_{2}^{1}(id$ - $f)$.

> **Proposition 14.23.** For any linear map $f$ : $E \to E$, let $U^{+} =$ Ker $(_{2}^{1}(id$ - $f))$ and let $U^{-} = Im(_{2}^{1}(id$ - $f))$. If $f^{2} =$ id, then
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} ,$$
and so, f(u) $= u$ on $U^{+}$ and f(u) $= -u$ on $U^{-}$.

*Proof.* If $f^{2} =$ id, then
$$(id -f) \circ (id + f) = id -f^{2}= id -id = 0,$$
which implies that
$$\mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} \subseteq \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} .$$

<!-- PAGE 554 -->
$$Conversely, if u \in Ker_{2}^{1} \begin{pmatrix} (id -f) \end{pmatrix} , then f(u) = u, so$$
$$\frac{1}{2} (id + f)(u) = \frac{1}{2} (u + u) = u,$$
and thus
$$\mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} \subseteq \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} .$$
Therefore,
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} ,$$
and so, f(u) $= u$ on $U^{+}$ and f(u) $= -u$ on $U^{-}$. We now assume that $K =\mathbb{C}$. The involutions of $E$ that are unitary transformations are characterized as follows.

> **Proposition 14.24.** Let $f \in$ GL(E) be an involution. The following properties are equivalent:
(a) The map $f$ is unitary; that is, $f \in$ U(E).
$(b)$ The subspaces $U^{-} = Im(_{2}^{1}(id$ - $f))$ and $U^{+} = Im(_{2}^{1}(id + f))$ are orthogonal. Furthermore, if $E$ is finite-dimensional, then (a) and $(b)$ are equivalent to $(c)$ below:
$(c)$ The map is self-adjoint; that is, $f = f^{*}$ .

*Proof.* If $f$ is unitary, then from $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ for all $u, v \in E$, we see that if $u \in U^{+}$ and $v \in U^{-}$ , we get
$$\langle u, v\rangle = \langle f(u), f(v)\rangle = \langle u, -v\rangle = -\langle u, v\rangle ,$$
so $2\langle u, v\rangle = 0$, which implies $\langle u, v\rangle = 0$, that is, $U^{+}$ and $U^{-}$ are orthogonal. Thus, (a) implies $(b)$. Conversely, if $(b)$ holds, since f(u) $= u$ on $U^{+}$ and f(u) $= -u$ on $U^{-}$, we see that $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ if $u, v \in U^{+}$ or if $u, v \in U^{-}$. Since $E = U^{+} \oplus U^{-}$ and since $U^{+}$ and $U^{-}$ are orthogonal, we also have $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ for all $u, v \in E$, and $(b)$ implies (a). If $E$ is finite-dimensional, the adjoint $f^{*}$ of $f$ exists, and we know that $f^{-1} = f^{*}$. Since $f$ is an involution, $f^{2} =$ id, which implies that $f^{*} = f^{-1} = f$. A unitary involution is the identity on $U^{+} = Im(_{2}^{1}(id + f))$, and f(v) $= -v$ for all $\oplus v \in U^{-} = Im(_{2}^{1}(id-f))$. Furthermore, $E$ is an orthogonal direct sum $E = U^{+} U^{-}$. We say that $f$ is an orthogonal reflection about $U^{+}$. In the special case where $U^{+}$ is a hyperplane, we say that $f$ is a hyperplane reflection. We already studied hyperplane reflections in the Euclidean case; see Chapter $13$.

<!-- PAGE 555 -->
If $f$ : $E \to E$ is a projection $(f^{2} = f)$, then
$$(id -2f)^{2}= id -4f + 4f^{2}= id -4f + 4f = id,$$
so id - 2f is an involution. As a consequence, we get the following result.

> **Proposition 14.25.** If $f$ : $E \to E$ is a projection $(f^{2} = f)$, then Ker $(f)$ and Im(f) are orthogonal iff $f^{*} = f$.

*Proof.* Apply Proposition 14.24 to $g =$ id - 2f. Since id - $g =$ 2f we have
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -g) \\ 2 \end{pmatrix} = \mathrm{Ker} (f)$$
and
$$U^{-} = \mathrm{Im} \begin{pmatrix} 1 \\ (id -g) \\ 2 \end{pmatrix} = \mathrm{Im}(f),$$
which proves the proposition. A projection such that $f = f^{*}$ is called an orthogonal projection. If $(a_{1} \dots  , a_{k})$ are $k$ linearly independent vectors in $\mathbb{R}^{n}$, let us determine the matrix $P$ of
$$\mathbb{R}^{n}$$
the orthogonal projection onto the subspace of spanned by $(a_{1}, \dots  , a_{k})$. Let $A$ be the $n\times k$ matrix whose jth column consists of the coordinates of the vector $a_{j}$ over the canonical basis $(e_{1}, \dots  , e_{n})$. Any vector in the subspace $(a_{1}, \dots  , a_{k})$ is a linear combination of the form Ax, for some $x \in \mathbb{R}^{k}$. Given any $y \in \mathbb{R}^{n}$, the orthogonal projection Py $=$ Ax of $y$ onto the subspace spanned by $(a_{1}, \dots  , a_{k})$ is the vector Ax such that $y$ - Ax is orthogonal to the subspace spanned by $(a_{1}, \dots  , a_{k})$ (prove it). This means that $y$ - Ax is orthogonal to every $a_{j}$, which is expressed by
$$A^{\top}(y -Ax) = 0;$$
that is,
$$A^{\top}Ax = A^{\top}y.$$
The matrix $A^{\top}A$ is invertible because $A$ has full rank $k$, thus we get
$$x = (A^{\top}A)^{-1}A^{\top}y,$$
and so
$$Py = Ax = A(A^{\top}A)^{-1}A^{\top}y.$$
Therefore, the matrix $P$ of the projection onto the subspace spanned by $(a_{1} \dots  , a_{k})$ is given by
$$P = A(A^{\top}A)^{-1}A^{\top}.$$
The reader should check that $P^{2} = P$ and $P^{\top} = P$.
