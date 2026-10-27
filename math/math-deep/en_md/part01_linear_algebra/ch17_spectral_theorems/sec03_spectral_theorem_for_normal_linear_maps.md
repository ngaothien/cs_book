# Spectral Theorem for Normal Linear Maps


<!-- PAGE 631 -->

## 17.3 Spectral Theorem for Normal Linear Maps

Given a Euclidean space $E$, our next step is to show that for every linear map $f$ : $E \to E$ there is some subspace $W$ of dimension $1$ or $2$ such that f(W) $\subseteq W$. When dim(W) $= 1$, the subspace $W$ is actually an eigenspace for some real eigenvalue of $f$. Furthermore, when $f$ is normal, there is a subspace $W$ of dimension $1$ or $2$ such that f(W) $\subseteq W$ and $f^{*} (W) \subseteq W$. The difficulty is that the eigenvalues of $f$ are not necessarily real. One way to get around this problem is to complexify both the vector space $E$ and the inner product $\langle$ -, $-\rangle$ as we did in Section 17.2. Given any subspace $W$ of a Euclidean space $E$, recall that the orthogonal complement $W^{\perp}$ of $W$ is the subspace defined such that
$$W^{\perp} = {u \in E | \langle u, w\rangle = 0, for all w \in W}.$$
Recall from Proposition 12.11 that $E = W \oplus W^{\perp}$ (this can be easily shown, for example, by constructing an orthonormal basis of $E$ using the Gram–Schmidt orthonormalization procedure). The same result also holds for Hermitian spaces; see Proposition 14.13. As a warm up for the proof of Theorem 17.12, let us prove that every self-adjoint map on a Euclidean space can be diagonalized with respect to an orthonormal basis of eigenvectors.

> **Theorem 17.8.** (Spectral theorem for self-adjoint linear maps on a Euclidean space) Given a Euclidean space $E$ of dimension $n$, for every self-adjoint linear map $f$ : $E \to E$, there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ of eigenvectors of $f$ such that the matrix of $f$ w.r.t. this basis is a diagonal matrix
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
with $\lambda_{i}  \in \mathbb{R}$.

*Proof.* We proceed by induction on the dimension $n$ of $E$ as follows. If $n = 1$, the result is trivial. Assume now that $n \ge 2$. From Proposition 17.6, all the eigenvalues of $f$ are real, so pick some eigenvalue $\lambda  \in \mathbb{R}$, and let $w$ be some eigenvector for $\lambda$ . By dividing $w$ by its norm, we may assume that $w$ is a unit vector. Let $W$ be the subspace of dimension $1$ spanned by $w$. Clearly, f(W) $\subseteq W$. We claim that $f(W^{\perp}$ ) $\subseteq W^{\perp}$ , where $W^{\perp}$ is the orthogonal complement of $W$. Indeed, for any $v \in W^{\perp}$ , that is, if $\langle v, w\rangle = 0$, because $f$ is self-adjoint and f(w) $= \lambda w$, we have
$$\langle f(v), w\rangle = \langle v, f(w)\rangle$$
$$= \langle v, \lambda w\rangle$$
$$= \lambda \langle v, w\rangle = 0$$

<!-- PAGE 632 -->
since $\langle v, w\rangle = 0$. Therefore,
$$f(W^{\perp} ) \subseteq W^{\perp} .$$
Clearly, the restriction of $f$ to $W^{\perp}$ is self-adjoint, and we conclude by applying the induction hypothesis to $W^{\perp}$ (whose dimension is $n$ - $1)$. We now come back to normal linear maps. One of the key points in the proof of Theorem 17.8 is that we found a subspace $W$ with the property that f(W) $\subseteq W$ implies that $f(W^{\perp}$ ) $\subseteq W^{\perp}$ . In general, this does not happen, but normal maps satisfy a stronger property which ensures that such a subspace exists. The following proposition provides a condition that will allow us to show that a normal linear map can be diagonalized. It actually holds for any linear map. We found the inspiration for this proposition in Berger $[11]$.

> **Proposition 17.9.** Given a Hermitian space $E$, for any linear map $f$ : $E \to E$ and any
$$subspace W of E, if f(W) \subseteq W, then f^{*} \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} . Consequently, if f(W) \subseteq W and$$
$$f^{*} (W) \subseteq W, then f \begin{pmatrix} W^{\perp} \\ then \end{pmatrix} \subseteq W^{\perp} and f^{*} \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} .$$

*Proof.* If $u \in W^{\perp}$ ,
$$\langle w, u\rangle = 0for all w \in W.$$
However,
$$\langle f(w), u\rangle = \langle w, f^{*} (u)\rangle ,$$
and f(W) $\subseteq W$ implies that f(w) $\in W$. Since $u \in W^{\perp}$ , we get
$$0 = \langle f(w), u\rangle = \langle w, f^{*} (u)\rangle ,$$
which shows that $\langle w, f^{*} (u)\rangle = 0$ for all $w \in W$, that is, $f^{*} (u) \in W^{\perp}$ . Therefore, we have $f^{*} (W^{\perp}$ ) $\subseteq W^{\perp}$ .
$$We just proved that if f(W) \subseteq W, then f^{*} \begin{pmatrix} W^{\perp} \\ f^{**}( \end{pmatrix} \subseteq W^{\perp} . If we also have f^{*} (W) \subseteq W,$$
then by applying the above fact to $f^{*}$ , we get  $W^{\perp}$ ) $\subseteq W^{\perp}$ , and since $f^{**} = f$, this is just $f(W^{\perp}$ ) $\subseteq W^{\perp}$ , which proves the second statement of the proposition. It is clear that the above proposition also holds for Euclidean spaces. Although we are ready to prove that for every normal linear map $f$ (over a Hermitian space) there is an orthonormal basis of eigenvectors (see Theorem 17.13 below), we now return to real Euclidean spaces.

> **Proposition 17.10.** If $f$ : $E \to E$ is a linear map and $w = u +$ iv is an eigenvector of $f_{C}$ : $E_{C} \to E_{C}$ for the eigenvalue $z = \lambda  + i\mu$ , where $u, v \in E$ and $\lambda , \mu  \in \mathbb{R}$, then
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.(*)$$
As a consequence,
$$f_{C}(u -iv) = f(u) -if(v) = (\lambda  -i\mu )(u -iv),$$
which shows that $\overline{w} = u$ - iv is an eigenvector of $f_{C}$ for $\overline{z} = \lambda$  - $i\mu$ .

<!-- PAGE 633 -->

*Proof.* Since
$$f_{C}(u + iv) = f(u) + if(v)$$
and
$$f_{C}(u + iv) = (\lambda  + i\mu )(u + iv) = \lambda u -\mu v + i(\mu u + \lambda v),$$
we have
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.$$
Using this fact, we can prove the following proposition.

> **Proposition 17.11.** Given a Euclidean space $E$, for any normal linear map $f$ : $E \to E$, if $w = u +$ iv is an eigenvector of $f_{C}$ associated with the eigenvalue $z = \lambda  + i\mu$  (where $u, v \in E$ and $\lambda , \mu  \in \mathbb{R})$, if $\mu  \neq  0$ (i.e., $z$ is not real) then $\langle u, v\rangle = 0$ and $\langle u, u\rangle = \langle v, v\rangle$ , which implies that $u$ and $v$ are linearly independent, and if $W$ is the subspace spanned by $u$ and $v$, then f(W) $= W$ and $f^{*} (W) = W$. Furthermore, with respect to the (orthogonal) basis $(u, v)$, the restriction of $f$ to $W$ has the matrix
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix} .$$
If $\mu  = 0$, then $\lambda$  is a real eigenvalue of $f$, and either $u$ or $v$ is an eigenvector of $f$ for $\lambda$ . If $W$ is the subspace spanned by $u$ if $u \neq  0$, or spanned by $v \neq  0$ if $u = 0$, then f(W) $\subseteq W$ and $f^{*} (W) \subseteq W$.

*Proof.* Since $w = u +$ iv is an eigenvector of $f_{C}$, by definition it is nonnull, and either $u \neq  0$ or $v \neq  0$. Proposition 17.10 implies that $u$ - iv is an eigenvector of $f_{C}$ for $\lambda$  - $i\mu$ . It is easy to check that $f_{C}$ is normal. However, if $\mu  \neq  0$, then $\lambda  + i\mu  \neq  \lambda$  - $i\mu$ , and from Proposition 17.4, the vectors $u +$ iv and $u$ - iv are orthogonal w.r.t. $\langle$ -, $-\rangle_{C}$ , that is,
$$\langle u + iv, u -iv\rangle_{C}  = \langle u, u\rangle -\langle v, v\rangle + 2i\langle u, v\rangle = 0.$$
Thus we get $\langle u, v\rangle = 0$ and $\langle u, u\rangle = \langle v, v\rangle$ , and since $u \neq  0$ or $v \neq  0, u$ and $v$ are linearly independent. Since
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v$$
and since by Proposition 17.3 $u +$ iv is an eigenvector of $f_{C}^{*}$  for $\lambda$  - $i\mu$ , we have
$$f^{*} (u) = \lambda u + \mu vandf^{*} (v) = -\mu u + \lambda v,$$
and thus f(W) $= W$ and $f^{*} (W) = W$, where $W$ is the subspace spanned by $u$ and $v$. When $\mu  = 0$, we have
$$f(u) = \lambda uandf(v) = \lambda v,$$
and since $u \neq  0$ or $v \neq  0$, either $u$ or $v$ is an eigenvector of $f$ for $\lambda$ . If $W$ is the subspace spanned by $u$ if u̸ $= 0$, or spanned by $v$ if $u = 0$, it is obvious that f(W) $\subseteq W$ and $f^{*} (W) \subseteq W$. Note that $\lambda  = 0$ is possible, and this is why $\subseteq$ cannot be replaced by $=$.

<!-- PAGE 634 -->
The beginning of the proof of Proposition 17.11 actually shows that for every linear map $f$ : $E \to E$ there is some subspace $W$ such that f(W) $\subseteq W$, where $W$ has dimension $1$ or $2$. In general, it doesn’t seem possible to prove that $W^{\perp}$ is invariant under $f$. However, this happens when $f$ is normal. We can finally prove our first main theorem.

> **Theorem 17.12.** (Main spectral theorem) Given a Euclidean space $E$ of dimension $n$, for every normal linear map $f$ : $E \to E$, there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ such that the matrix of $f$ w.r.t. this basis is a block diagonal matrix of the form
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
such that each block $A_{j}$ is either a one-dimensional matrix (i.e., a real scalar) or a twodimensional matrix of the form
$$A_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix} ,$$
where $\lambda_{j} , \mu_{j}  \in \mathbb{R}$, with $\mu_{j}  > 0$.

*Proof.* We proceed by induction on the dimension $n$ of $E$ as follows. If $n = 1$, the result is trivial. Assume now that $n \ge 2$. First, since $\mathbb{C}$ is algebraically closed (i.e., every polynomial has a root in $\mathbb{C})$, the linear map $f_{C}$ : $E_{C} \to E_{C}$ has some eigenvalue $z = \lambda  + i\mu$  (where $\lambda , \mu  \in \mathbb{R})$. Let $w = u +$ iv be some eigenvector of $f_{C}$ for $\lambda  + i\mu$  (where $u, v \in E)$. We can now apply Proposition 17.11. If $\mu  = 0$, then either $u$ or $v$ is an eigenvector of $f$ for $\lambda  \in \mathbb{R}$. Let $W$ be the subspace of dimension $1$ spanned by $e_{1} = u/\|u\|$ if $u \neq  0$, or by $e_{1} = v/\|v\|$ otherwise. It is obvious that f(W) $\subseteq W$ and $f^{*} (W) W$. The orthogonal $W^{\perp}$ of $W$ has dimension $n$ - $1$, and by
$$Proposition 17.9, we have f \begin{pmatrix} \subseteq \\ W^{\perp} \\ the \end{pmatrix} \subseteq W^{\perp} . But the restriction of f to W^{\perp} is also normal,$$
and we conclude by applying  induction hypothesis to $W^{\perp}$ . If $\mu  \neq  0$, then $\langle u, v\rangle = 0$ and $\langle u, u\rangle = \langle v, v\rangle$ , and if $W$ is the subspace spanned by $u/\|u\|$ and $v/\|v\|$, then f(W) $= W$ and $f^{*} (W) = W$. We also know that the restriction of $f$ to $W$ has the matrix
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix}$$
with respect to the basis $(u/\|u\|, v/\|v\|)$. If $\mu  < 0$, we let $\lambda_{1}  = \lambda , \mu_{1}  = -\mu , e_{1} = u/\|u\|$, and $e_{2} = v/\|v\|$. If $\mu  > 0$, we let $\lambda_{1}  = \lambda , \mu_{1}  = \mu , e_{1} = v/\|v\|$, and $e_{2} = u/\|u\|$. In all cases, it is easily verified that the matrix of the restriction of $f$ to $W$ w.r.t. the orthonormal basis $(e_{1}, e_{2})$ is
$$A_{1} = \begin{pmatrix} \lambda_{1} & -\mu_{1} \\ \mu_{1} & \lambda_{1} \end{pmatrix} ,$$

<!-- PAGE 635 -->
where $\lambda_{1} , \mu_{1}  \in \mathbb{R}$, with $\mu_{1}  > 0$. However, $W^{\perp}$ has dimension $n -2$, and by Proposition 17.9,
$$f \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} . Since the restriction of f to W^{\perp} is also normal, we conclude by applying$$
the induction hypothesis to $W^{\perp}$ . After this relatively hard work, we can easily obtain some nice normal forms for the matrices of self-adjoint, skew-self-adjoint, and orthogonal linear maps. However, for the sake of completeness (and since we have all the tools to so do), we go back to the case of a Hermitian space and show that normal linear maps can be diagonalized with respect to an orthonormal basis. The proof is a slight generalization of the proof of Theorem 17.6.

> **Theorem 17.13.** (Spectral theorem for normal linear maps on a Hermitian space) Given a Hermitian space $E$ of dimension $n$, for every normal linear map $f$ : $E \to E$ there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ of eigenvectors of $f$ such that the matrix of $f$ w.r.t. this basis is a diagonal matrix
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
where $\lambda_{j}  \in \mathbb{C}$.

*Proof.* We proceed by induction on the dimension $n$ of $E$ as follows. If $n = 1$, the result is trivial. Assume now that $n \ge 2$. Since $\mathbb{C}$ is algebraically closed (i.e., every polynomial has a root in $\mathbb{C})$, the linear map $f$ : $E \to E$ has some eigenvalue $\lambda  \in \mathbb{C}$, and let $w$ be some unit eigenvector for $\lambda$ . Let $W$ be the subspace of dimension $1$ spanned by $w$. Clearly, f(W) $\subseteq W$. By Proposition 17.3, $w$ is an eigenvector of $f^{*}$ for $\overline{\lambda}$, and thus $f^{*} (W) \subseteq W$. By Proposition 17.9, we also have $f(W^{\perp}$ ) $\subseteq W^{\perp}$ . The restriction of $f$ to $W^{\perp}$ is still normal, and we conclude by applying the induction hypothesis to $W^{\perp}$ (whose dimension is $n$ - $1)$. Theorem 17.13 implies that (complex) self-adjoint, skew-self-adjoint, and orthogonal linear maps can be diagonalized with respect to an orthonormal basis of eigenvectors. In this latter case, though, an orthogonal map is called a unitary map. Proposition 17.5 also shows that the eigenvalues of a self-adjoint linear map are real, and Proposition 17.7 shows that the eigenvalues of a skew self-adjoint map are pure imaginary or zero, and that the eigenvalues of a unitary map have absolute value $1$.
Remark: There is a converse to Theorem 17.13, namely, if there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ of eigenvectors of $f$, then $f$ is normal. We leave the easy proof as an exercise. In the next section we specialize Theorem 17.12 to self-adjoint, skew-self-adjoint, and orthogonal linear maps. Due to the additional structure, we obtain more precise normal forms.
