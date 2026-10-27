# Totally Isotropic Subspaces


<!-- PAGE 1034 -->

## 29.6 Totally Isotropic Subspaces

In this section, we deal with $\epsilon$ -Hermitian forms, $\phi$ : $E \times  E \to K$. In general, $E$ may have subspaces $U$ such that $U \cap U^{\perp} \neq  (0)$, or worse, such that $U \subseteq U^{\perp}$ (that is, $\phi$  is zero on $U)$. We will see that such subspaces play a crucial in the decomposition of $E$ into orthogonal subspaces.

> **Definition 29.17.** Given an $\epsilon$ -Hermitian forms $\phi$ : $E \times  E \to K$, a nonzero vector $u \in E$ is said to be isotropic if $\phi (u, u) = 0$. It is convenient to consider $0$ to be isotropic. Given any subspace $U$ of $E$, the subspace rad(U) $= U \cap U^{\perp}$ is called the radical of $U$. We say that
$(i) U$ is degenerate if rad(U) $\neq  (0)$ (equivalently if there is some nonzero vector $u \in U$ such that $x \in U^{\perp}$ ). Otherwise, we say that $U$ is nondegenerate.
(ii) $U$ is totally isotropic if $U \subseteq U^{\perp}$ (equivalently if the restriction of $\phi$  to $U$ is zero). By definition, the trivial subspace $U = (0) (= {0})$ is nondegenerate. Observe that a subspace $U$ is nondegenerate iff the restriction of $\phi$  to $U$ is nondegenerate. A degenerate subspace is sometimes called an isotropic subspace. Other authors say that a subspace $U$ is isotropic if it contains some (nonzero) isotropic vector. A subspace which has no nonzero isotropic vector is often called anisotropic. The space of all isotropic vectors is a cone often called the light cone (a terminology coming from the theory of relativity). This is not to be confused with the cone of silence (from Get Smart)! It should also be noted that some authors (such as Serre) use the term isotropic instead of totally isotropic. The apparent lack of standard terminology is almost as bad as in graph theory! It is clear that any direct sum of pairwise orthogonal totally isotropic subspaces is totally isotropic. Thus, every totally isotropic subspace is contained in some maximal totally isotropic subspace. Here is another fact that we will use all the time: if $V$ is a totally isotropic subspace and if $U$ is a subspace of $V$ , then $U$ is totally isotropic. This is because by definition $V$ is isotropic if $V \subseteq V^{\perp}$ , and since $U \subseteq V$ we get $V^{\perp} \subseteq U^{\perp}$ , so $U \subseteq V \subseteq V^{\perp} \subseteq U^{\perp}$ , which shows that $U$ is totally isotropic. First, let us show that in order to sudy an $\epsilon$ -Hermitian form on a space $E$, it suffices to restrict our attention to nondegenerate forms.

> **Proposition 29.19.** Given an $\epsilon$ -Hermitian form $\phi$ : $E \times  E \to K$ on $E$, we have:
(a) If $U$ and $V$ are any two orthogonal subspaces of $E$, then
$$rad(U + V ) = rad(U) + rad(V ).$$
$(b)$ rad(rad(E)) $=$ rad(E).

<!-- PAGE 1035 -->
$(c)$ If $U$ is any subspace supplementary to rad(E), so that
$$E = rad(E) \oplus U,$$
then $U$ is nondegenerate, and rad(E) and $U$ are orthogonal.

*Proof.* (a) If $U$ and $V$ are orthogonal, then $U \subseteq V^{\perp}$ and $V \subseteq U^{\perp}$ . We get
$$rad(U + V ) = (U + V ) \cap (U + V )^{\perp}$$
$$= (U + V ) \cap U^{\perp} \cap V^{\perp}$$
$$= U \cap U^{\perp} \cap V^{\perp} + V \cap U^{\perp} \cap V^{\perp}$$
$$= U \cap U^{\perp} + V \cap V^{\perp}$$
$$= rad(U) + rad(V ).$$
$(b)$ By definition, rad(E) $= E^{\perp}$, and obviously $E = E^{\perp \perp}$, so we get
$$rad(rad(E)) = E^{\perp}\cap E^{\perp \perp}= E^{\perp}\cap E = E^{\perp}= rad(E).$$
$(c)$ If $E =$ rad(E) $\oplus U$, by definition of rad(E), the subspaces rad(E) and $U$ are orthogonal. From (a) and $(b)$, we get
$$rad(E) = rad(E) + rad(U).$$
Since rad(U) $= U \cap U^{\perp} \subseteq U$ and since rad(E) $\oplus U$ is a direct sum, we have a direct sum
$$rad(E) = rad(E) \oplus rad(U),$$
which implies that rad(U) $= (0)$; that is, $U$ is nondegenerate. Proposition 29.19(c) shows that the restriction of $\phi$  to any supplement $U$ of rad(E) is nondegenerate and $\phi$  is zero on rad(U), so we may restrict our attention to nondegenerate forms. The following is also a key result.

> **Proposition 29.20.** Given an $\epsilon$ -Hermitian form $\phi$ : $E \times  E \to K$ on $E$, if $U$ is a finite-dimensional nondegenerate subspace of $E$, then $E = U \oplus U^{\perp}$ .

*Proof.* By hypothesis, the restriction $\phi_{U}$  of $\phi$  to $U$ is nondegenerate, so the semilinear map $r_{\phi U}$ : $U \to U^{*}$ is injective. Since $U$ is finite-dimensional, $r_{\phi U}$ is actually bijective, so for every $v \in E$, if we consider the linear form in $U^{*}$ given by $u \mapsto \phi (u, v) (u \in U)$, there is a unique $v_{0} \in U$ such that
$$\phi (u, v_{0}) = \phi (u, v)for all u \in U;$$
that is, $\phi (u, v$ - $v_{0}) = 0$ for all $u \in U$, so $v$ - $v_{0} \in U^{\perp}$ . It follows that $v = v_{0} + v$ - $v_{0}$, with $v_{0} \in U$ and $v_{0}$ - $v \in U^{\perp}$ , and since $U$ is nondegenerate $U \cap U^{\perp} = (0)$, and $E = U \oplus U^{\perp}$ . As a corollary of Proposition 29.20, we get the following result.

<!-- PAGE 1036 -->

> **Proposition 29.21.** Given an $\epsilon$ -Hermitian form $\phi$ : $E\times E \to K$ on $E$, if $\phi$  is nondegenerate and if $U$ is a finite-dimensional subspace of $E$, then rad(U) $= rad(U^{\perp}$ ), and the following conditions are equivalent:
$(i) U$ is nondegenerate.
(ii) $U^{\perp}$ is nondegenerate.
(iii) $E = U \oplus U^{\perp}$ .

*Proof.* By definition, $rad(U^{\perp}$ ) $= U^{\perp} \cap U^{\perp \perp}$ , and since $\phi$  is nondegenerate and $U$ is finite-dimensional, $U^{\perp \perp} = U$, so $rad(U^{\perp}$ ) $= U^{\perp} \cap U^{\perp \perp} = U \cap U^{\perp} =$ rad(U). By Proposition 29.20, $(i)$ implies (iii). If $E = U \oplus U^{\perp}$ , then rad(U) $= U \cap U^{\perp} = (0)$, so $U$ is nondegenerate and (iii) implies $(i)$. Since $rad(U^{\perp}$ ) $=$ rad(U), (iii) also implies (ii). Now, if $U^{\perp}$ is nondegenerate, we have $U^{\perp} \cap U^{\perp \perp} = (0)$, and since $U \subseteq U^{\perp \perp}$ , we get
$$U \cap U^{\perp} \subseteq U^{\perp \perp} \cap U^{\perp} = (0),$$
which shows that $U$ is nondegenerate, proving the implication (ii) $=\Rightarrow (i)$. If $E$ is finite-dimensional, we have the following results.

> **Proposition 29.22.** Given an $\epsilon$ -Hermitian form $\phi$ : $E \times  E \to K$ on a finite-dimensional space $E$, if $\phi$  is nondegenerate, then for every subspace $U$ of $E$ we have
$(i)$ dim(U) $+ dim(U^{\perp}$ ) $=$ dim(E).
(ii) $U^{\perp \perp} = U$.

*Proof.* $(i)$ Since $\phi$  is nondegenerate and $E$ is finite-dimensional, the semilinear map $l_{\phi}$ : $E \to E^{*}$ is bijective. By transposition, the inclusion $i: U \to E$ yields a surjection $r: E^{*} \to U^{*}$ (with r(f) $= f \circ i$ for every $f \in E^{*}$; the map $f \circ i$ is the restriction of the linear form $f$ to $U)$. It follows that the semilinear map $r \circ l_{\phi}$ : $E \to U^{*}$ given by
$$(r \circ l_{\phi})(x)(u) =\overline{\phi}\overline{(}\overline{x, u}\overline{)} x \in E, u \in U$$
is surjective, and its kernel is $U^{\perp}$ . Thus, we have
$$\dim(U^{*} ) + \dim(U^{\perp} ) = \dim(E),$$
and since dim(U) $= dim(U^{*}$ ) because $U$ is finite-dimensional, we get
$$\dim(U) + \dim(U^{\perp} ) = \dim(U^{*} ) + \dim(U^{\perp} ) = \dim(E).$$
(ii) Applying the above formula to $U^{\perp}$ , we deduce that dim(U) $= dim(U^{\perp \perp}$ ). Since $U \subseteq U^{\perp \perp}$ , we must have $U^{\perp \perp} = U$.

<!-- PAGE 1037 -->
Remark: We already proved in Proposition 29.13 that if $U$ is finite-dimensional, then $codim(U^{\perp}$ ) $=$ dim(U) and $U^{\perp \perp} = U$, but it doesn’t hurt to give another proof. Observe that
$(i)$ implies that
$$\dim(U) + \dim(rad(U)) \le \dim(E).$$
We can now proceed with the Witt decomposition, but before that, we quickly take care of the structure theorem for alternating bilinear forms (the case where $\phi (u, u) = 0$ for all $u \in E)$. For an alternating bilinear form, the space $E$ is totally isotropic. For example in dimension $2$, the matrix
$$B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$
defines the alternating form given by
$$\phi ((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}y_{2} -x_{2}y_{1}.$$
This case is surprisingly general.

> **Proposition 29.23.** Let $\phi$ : $E \times  E \to K$ be an alternating bilinear form on $E$. If $u, v \in E$ are two (nonzero) vectors such that $\phi (u, v) = \lambda  \neq  0$, then $u$ and $v$ are linearly independent. If we let $u_{1} = \lambda^{-1} u$ and $v_{1} = v$, then $\phi (u_{1}, v_{1}) = 1$, and the restriction of $\phi$  to the plane spanned by $u_{1}$ and $v_{1}$ is represented by the matrix
$$\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} .$$

*Proof.* If $u$ and $v$ were linearly dependent, as $u, v \neq  0$, we could write $v = \mu u$ for some $\mu  \neq  0$, but then, since $\phi$  is alternating, we would have
$$\lambda  = \phi (u, v) = \phi (u, \mu u) = \mu \phi (u, u) = 0,$$
contradicting the fact that $\lambda  \neq  0$. The rest is obvious. Proposition 29.23 yields a plane spanned by two vectors $u_{1}, v_{1}$ such that $\phi (u_{1}, u_{1}) = \phi (v_{1}, v_{1}) = 0$ and $\phi (u_{1}, v_{1}) = 1$. Such a plane is called a hyperbolic plane. If $E$ is finite-dimensional, we obtain the following theorem.

> **Theorem 29.24.** Let $\phi$ : $E \times  E \to K$ be an alternating bilinear form on a space $E$ of finite dimension $n$. Then, there is a direct sum decomposition of $E$ into pairwise orthogonal subspaces
$$E = W_{1} \oplus \cdots  \oplus W_{r} \oplus rad(E),$$
where each $W_{i}$ is a hyperbolic plane and rad(E) $= E^{\perp}$. Therefore, there is a basis of $E$ of the form
$$(u_{1}, v_{1}, \dots  , u_{r}, v_{r}, w_{1}, \dots  , w_{n-2r}),$$

<!-- PAGE 1038 -->
with respect to which the matrix representing $\phi$  is a block diagonal matrix $M$ of the form
$$M = \begin{pmatrix} J & 0 \\ J \\ \ddots \\ J \\ 0 & 0_{n-2r} \end{pmatrix} ,$$
with
$$J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} .$$

*Proof.* If $\phi  = 0$, then $E = E^{\perp}$ and we are done. Otherwise, there are two nonzero vectors $u, v \in E$ such that $\phi (u, v) \neq  0$, so by Proposition 29.23, we obtain a hyperbolic plane $W_{2}$ spanned by two vectors $u_{1}, v_{1}$ such that $\phi (u_{1}, v_{1}) = 1$. The subspace $W_{1}$ is nondegenerate (for example, det(J) $= -1)$, so by Proposition 29.21, we get a direct sum
$$E = W_{1} \oplus W_{1}^{\perp}  .$$
By Proposition 29.14, we also have
$$E^{\perp}= (W_{1} \oplus W_{1}^{\perp}  ) = W_{1}^{\perp} \cap W_{1}^{\perp \perp}= rad(W_{1}^{\perp}  ).$$
By the induction hypothesis applied to $W_{1}^{\perp}$  , we obtain our theorem. The following corollary follows immediately.

> **Proposition 29.25.** Let $\phi$ : $E \times  E \to K$ be an alternating bilinear form on a space $E$ of finite dimension $n$.
$(1)$ The rank of $\phi$  is even.
$(2)$ If $\phi$  is nondegenerate, then dim(E) $= n$ is even.
$(3)$ Two alternating bilinear forms $\phi_{1}$  : $E_{1} \times E_{1} \to K$ and $\phi_{2}$  : $E_{2} \times E_{2} \to K$ are equivalent iff $dim(E_{1}) = dim(E_{2})$ and $\phi_{1}$  and $\phi_{2}$  have the same rank. The only part that requires a proof is part $(3)$, which is left as an easy exercise. If $\phi$  is nondegenerate, then $n =$ 2r, and a basis of $E$ as in Theorem 29.24 is called a symplectic basis. The space $E$ is called a hyperbolic space (or symplectic space). Observe that if we reorder the vectors in the basis
$$(u_{1}, v_{1}, \dots  , u_{r}, v_{r}, w_{1}, \dots  , w_{n-2r})$$
to obtain the basis
$$(u_{1}, \dots  , u_{r}, v_{1}, \dots  v_{r}, w_{1}, \dots  , w_{n-2r}),$$

<!-- PAGE 1039 -->
then the matrix representing $\phi$  becomes
$$\begin{pmatrix} 0 & I_{r} & 0 \\ -I_{r} & 0 & 0 \\ 0 & 0 & 0_{n-2r} \end{pmatrix} .$$
This particularly simple matrix is often preferable, especially when dealing with the matrices (symplectic matrices) representing the isometries of $\phi$  (in which case $n =$ 2r). As a warm up for Proposition 29.29 of the next section, we prove an analog of Proposition 29.23 in the case of a symmetric bilinear form.

> **Proposition 29.26.** Let $\phi$ : $E\times E \to K$ be a nondegenerate symmetric bilinear form with $K$ a field of characteristic different from $2$. For any nonzero isotropic vector $u$, there is another nonzero isotropic vector $v$ such that $\phi (u, v) = 2$, and $u$ and $v$ are linearly independent. In the basis $(u, v/2)$, the restriction of $\phi$  to the plane spanned by $u$ and $v/2$ is of the form
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .$$

*Proof.* Since $\phi$  is nondegenerate, there is some nonzero vector $z$ such that (rescaling $z$ if necessary) $\phi (u, z) = 1$. If
$$v = 2z -\phi (z, z)u,$$
then since $\phi (u, u) = 0$ and $\phi (u, z) = 1$, note that
$$\phi (u, v) = \phi (u, 2z -\phi (z, z)u) = 2\phi (u, z) -\phi (z, z)\phi (u, u) = 2,$$
and
$$\phi (v, v) = \phi (2z -\phi (z, z)u, 2z -\phi (z, z)u)$$
$$= 4\phi (z, z) -4\phi (z, z)\phi (u, z) + \phi (z, z)^{2}\phi (u, u)$$
$$= 4\phi (z, z) -4\phi (z, z) = 0.$$
If $u$ and $z$ were linearly dependent, as $u, z \neq  0$, we could write $z = \mu u$ for some $\mu  \neq  0$, but then, we would have
$$\phi (u, z) = \phi (u, \mu u) = \mu \phi (u, u) = 0,$$
contradicting the fact that $\phi (u$, z)̸ $= 0$. Then $u$ and $v =$ 2z - $\phi (z$, z)u are also linearly independent, since otherwise $z$ could be expressed as a multiple of $u$. The rest is obvious. Proposition 29.26 yields a plane spanned by two vectors $u_{1}, v_{1}$ such that $\phi (u_{1}, u_{1}) = \phi (v_{1}, v_{1}) = 0$ and $\phi (u_{1}, v_{1}) = 1$. Such a plane is called an Artinian plane. Proposition 29.26 also shows that nonzero isotropic vectors come in pair. Proposition 29.26 has the following corollary which has applications in number theory; see Serre $[163]$, Chapter IV.
