# Witt Decomposition


<!-- PAGE 1040 -->

> **Proposition 29.27.** If $\Phi$  is any nondegenerate quadratic form (over a field of characteristic $= 2)$ such that there is some nonzero vector $x \in E$ with $\Phi (x) = 0$, then for every $\alpha  \in K$, there is some $y \in E$ such that $\Phi (y) = \alpha$ .

*Proof.* Since by hypothesis there is some nonzero vector $u \in E$ with $\Phi (u) = 0$, by Proposition 29.26 there is another isotropic vector $v$ such that $u$ and $v$ are linearly independent and such that (after rescaling) $\phi (u, v) = 1$. Then for any $\alpha  \in K$, check that
$$\Phi \begin{pmatrix} \alpha \\ u + & v \\ 2 \end{pmatrix} = \alpha ,$$
as desired.
Remark: Some authors refer to the above plane as a hyperbolic plane. Berger (and others) point out that this terminology is undesirable because the notion of hyperbolic plane already exists in differential geometry and refers to a very different object. We leave it as an exercice to figure out that the group of isometries of the Artinian plane, the set of all $2 \times  2$ matrices $A$ such that
$$A^{\top} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,$$
consists of all matrices of the form
$$\begin{pmatrix} \lambda & 0 \\ 0 & \lambda^{-1} \end{pmatrix} or \begin{pmatrix} 0 & \lambda \\ \lambda^{-1} & 0 \end{pmatrix} ,\lambda  \in K -{0}.$$
In particular, if $K =\mathbb{R}$, then this group denoted O(1, $1)$ has four connected components. We now turn to the Witt decomposition.

## 29.7 Witt Decomposition

From now on, $\phi$ : $E \times  E \to K$ is an $\epsilon$ -Hermitian form. The following assumption will be needed: Property $(T)$. For every $u \in E$, there is some $\alpha  \in K$ such that $\phi (u, u) = \alpha  +\overline{\epsilon \alpha}$. Property $(T)$ is always satisfied if $\phi$  is alternating, or if $K$ is of characteristic $\neq  2$ and $\epsilon  = \pm 1$, with $\alpha  =_{2}^{1} \phi (u, u)$. The following (bizarre) technical lemma will be needed.

> **Lemma 29.28.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$ and assume that $\phi$  satisfies property $(T)$. For any totally isotropic subspace $U \neq  (0)$ of $E$, for every $x \in E$ not orthogonal to $U$, and for every $\alpha  \in K$, there is some $y \in U$ so that
$$\phi (x + y, x + y) = \alpha  +\overline{\epsilon \alpha .}$$

<!-- PAGE 1041 -->
$$Proof. By property (T), \frac{wehave}{\epsilon \phi (x, y),} \phi (x, x) = \beta  +\overline{\epsilon \beta} for some \beta  \in K. For any y \in U, since \phi$$
is $\epsilon$ -Hermitian, $\phi (y, x) =$  and since $U$ is totally isotropic $\phi (y, y) = 0$, so we have
$$\phi (x + y, x + y) = \phi (x, x) + \phi (x, y) + \phi (y, x) + \phi (y, y)$$
$$= \beta  +\overline{\epsilon \beta} + \phi (x, y) +\overline{\epsilon \phi}\overline{(}\overline{x, y}\overline{)}$$
$$= \beta  + \phi (x, y) + \epsilon \overline{(}\overline{\beta}\overline{+}\overline{\phi}\overline{(}\overline{x, y}\overline{)}.$$
Since $x$ is not orthogonal to $U$, the function $y \mapsto \phi (x, y) + \beta$  is not the constant function. Consequently, this function takes the value $\alpha$  for some $y \in U$, which proves the lemma.

> **Definition 29.18.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$. A weak Witt decomposition of $E$ is a triple $(U$, U' , $W)$, such that
$(i) E = U \oplus$ U' $\oplus W$ (a direct sum).
(ii) $U$ and U' are totally isotropic.
(iii) $W$ is nondegenerate and orthogonal to $U \oplus$ U' . We say that a weak Witt decomposition $(U$, U', $W)$ is nontrivial if U̸ $= (0)$ and U' $\neq  (0)$. Furthermore, if $E$ is finite-dimensional, then dim(U) $=$ dim(U' ) and in a suitable basis, the matrix representing $\phi$  is of the form
$$\begin{pmatrix} 0 & A & 0 \\ \epsilon A & 0 & 0 \\ 0 & 0 & B \end{pmatrix}$$
We say that $\phi$  is a neutral form if it is nondegenerate, $E$ is finite-dimensional, and if $W = (0)$. In this case, the matrix $B$ is missing. A Witt decomposition for which $W$ has no nonzero isotropic vectors $(W$ is anisotropic) is called a Witt decomposition. Observe that if $\Phi$  is nondegenerate, then we have the trivial weak Witt decomposition obtained by letting $U =$ U' $= (0)$ and $W = E$. Thus a weak Witt decomposition is informative only if $E$ is not anisotropic (there is some nonzero isotropic vector, i.e. some u̸ $= 0$ such that $\Phi (u) = 0)$, in which case the most informative nontrivial weak Witt decompositions are those for which $W$ is anisotropic and $U$ and U' are as big as possible. Sometimes, we use the notation $U_{1}^{\perp}\oplus U_{2}$ to indicate that in a direct sum $U_{1} \oplus U_{2}$, the subspaces $U_{1}$ and $U_{2}$ are orthogonal. Then, in Definition 29.18, we can write that $E = (U \oplus$ U' $)^{\perp}\oplus W$. The first step in showing the existence of a Witt decomposition is this.

<!-- PAGE 1042 -->

> **Proposition 29.29.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$, assume that $\phi$  is nondegenerate and satisfies property $(T)$, and let $U$ be any totally isotropic subspace of $E$ of finite dimension dim(U) $= r \ge 1$.
$(1)$ If U' is any totally isotropic subspace of dimension $r$ and if $U'\cap U^{\perp} = (0)$, then $U \oplus$ U' is nondegenerate, and for any basis $(u_{1}, \dots  , u_{r})$ of $U$, there is a basis $(u_{1}', \dots  , u_{r}')$ of U' such that $\phi (u_{i}, u_{j}') = \delta_{ij}$ , for all $i, j = 1, \dots  , r$.
$(2)$ If $W$ is any totally isotropic subspace of dimension at most $r$ and if $W \cap U^{\perp} = (0)$, then there exists a totally isotropic subspace U' with dim(U') $= r$ such that $W \subseteq$ U' and U' $\cap U^{\perp} = (0)$.

*Proof.* $(1)$ Let $\phi'$ be the restriction of $\phi$  to $U \times$  U'. Since U' $\cap U^{\perp} = (0)$, for any $v \in$ U', if $\phi (u, v) = 0$ for all $u \in U$, then $v = 0$. Thus, $\phi'$ is nondegenerate (we only have to check on the left since $\phi$  is $\epsilon$ -Hermitian). Then, the assertion about bases follows from the version of Proposition 29.3 for sesquilinear forms. Since $U$ is totally isotropic, $U \subseteq U^{\perp}$ , and since U' $\cap U^{\perp} = (0)$, we must have U' $\cap U = (0)$, which show that we have a direct sum $U \oplus$ U'. It remains to prove that $U +$ U' is nondegenerate. Observe that
$$H = (U + U' ) \cap (U + U' )^{\perp}= (U + U' ) \cap U^{\perp} \cap U^{'\perp} .$$
Since $U$ is totally isotropic, $U \subseteq U^{\perp}$, and since U' $\cap U^{\perp} = (0)$, we have
$$(U + U') \cap U^{\perp}= (U \cap U^{\perp}) + (U'\cap U^{\perp}) = U + (0) = U,$$
thus $H = U \cap U^{'\perp}$. Since $\phi'$ is nondegenerate, $U \cap U^{'\perp} = (0)$, so $H = (0)$ and $U +$ U' is nondegenerate.
$(2)$ We proceed by descending induction on $s =$ dim(W). The base case $s = r$ is trivial. For the induction step, it suffices to prove that if $s < r$, then there is a totally isotropic subspace W' containing $W$ such that dim(W') $= s + 1$ and W' $\cap U^{\perp} = (0)$. Since $s =$ dim(W) $<$ dim(U), the restriction of $\phi$  to $U \times  W$ is degenerate. Since $W \cap U^{\perp} = (0)$, we must have $U \cap W^{\perp} \neq  (0)$. We claim that
$$̸$$
$$W^{\perp}\subseteq W + U^{\perp}.$$
If we had
$$W^{\perp} \subseteq W + U^{\perp} ,$$
then because $U$ and $W$ are finite-dimensional and $\phi$  is nondegenerate, by Proposition 29.13, $U^{\perp \perp} = U$ and $W^{\perp \perp} = W$, so by taking orthogonals, $W^{\perp} \subseteq W + U^{\perp}$ would yield
$$(W + U^{\perp} )^{\perp}\subseteq W^{\perp \perp} ,$$
that is,
$$W^{\perp} \cap U \subseteq W,$$

<!-- PAGE 1043 -->
thus $W^{\perp} \cap U \subseteq W \cap U$, and since $U$ is totally isotropic, $U \subseteq U^{\perp}$ , which yields
$$W^{\perp} \cap U \subseteq W \cap U \subseteq W \cap U^{\perp} = (0),$$
contradicting the fact that $U \cap W^{\perp} \neq  (0)$. Therefore, there is some $u \in W^{\perp}$ such that $u \in / W +U^{\perp}$ . Since $U \subseteq U^{\perp}$ , we can add to $u$ any vector $z \in W^{\perp} \cap U \subseteq U^{\perp}$ so that $u + z \in W^{\perp}$ and $u + z \in / W + U^{\perp}$ (if $u + z \in W + U^{\perp}$ , since $z \in U^{\perp}$ , then $u \in W + U^{\perp}$ , a contradiction). Since $W^{\perp} \cap$ U̸ $= (0)$ is totally isotropic and $u \in / W + U^{\perp} = (W^{\perp} \cap U)^{\perp}$, we can invoke Lemma 29.28 to find a $z \in W^{\perp} \cap U$ such that $\phi (u + z, u + z) = 0$. See Figure 29.1. If we write $x = u + z$, then $x \in / W + U^{\perp}$ , so W' $= W +$ Kx is a totally isotropic subspace of dimension $s + 1$. Furthermore, we claim that W' $\cap U^{\perp} = 0$.
$$U$$
$$0zUt$$
$$W$$
$$u$$
$$W$$
$$E$$
$$Figure 29.1: A schematic illustration of W and x = u + z$$
Otherwise, we would have $y = w + \lambda x \in U^{\perp}$ , for some $w \in W$ and some $\lambda  \in K$, and then we would have $\lambda x = -w + y \in W + U^{\perp}$ . If $\lambda  \neq  0$, then $x \in W + U^{\perp}$ , a contradiction. Therefore, $\lambda  = 0, y = w$, and since $y \in U^{\perp}$ and $w \in W$, we have $y \in W \cap U^{\perp} = (0)$, which means that $y = 0$. Therefore, W' is the required subspace and this completes the proof. Here are some consequences of Proposition 29.29. If we set $W = (0)$ in Proposition 29.29(2), then we get the following theorem showing that if $E$ is not anisotropic (there is some nonzero isotropic vector) then weak nontrivial Witt decompositions exist.

> **Theorem 29.30.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$ which is nondegenerate and satisfies property $(T)$. For any totally isotropic subspace $U$ of $E$ of finite dimension $r \ge 1$, there exists a totally isotropic subspace U' of dimension $r$ such that $U \cap$ U' $= (0)$ and $U \oplus$ U' is nondegenerate. As a consequence, if $E$ is not anisotropic, then $(U$, U' , $(U \oplus$ U' $)^{\perp})$ is a weak nontrivial Witt decomposition for $E$. Furthermore, by Proposition 29.29(1), the block $A$ in the matrix of $\phi$  is the identity matrix.

<!-- PAGE 1044 -->

> **Proposition 29.31.** Any two $\epsilon$ -Hermitian neutral forms satisfying property $(T)$ defined on spaces of the same dimension are equivalent. The following proposition shows that every subspace $U$ of $E$ can be embedded into a nondegenerate subspace. It is needed to prove a version of the Witt extension theorem (Theorem 29.48).

> **Proposition 29.32.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$ which is nondegenerate and satisfies property $(T)$. For any subspace $U$ of $E$ of finite dimension, if we write
$$U = V^{\perp}\oplus W,$$
for some orthogonal complement $W$ of $V =$ rad(U), and if we let $r =$ dim(rad(U)), then there exists a totally isotropic subspace V' of dimension $r$ such that $V \cap$ V' $= (0)$, and $(V \oplus V')^{\perp}\oplus W =$ V' $\oplus U$ is nondegenerate. Furthermore, any isometry $f$ from $U$ into another space (E', $\phi'$ ) where $\phi'$ is an $\epsilon$ -Hermitian form satisfying the same assumptions as $\phi$  can be extended to an isometry on $(V \oplus$ V' $)^{\perp}\oplus W$.

*Proof.* Since $W$ is nondegenerate, $W^{\perp}$ is also nondegenerate, and $V \subseteq W^{\perp}$ . Therefore, we can apply Theorem 29.30 to the restriction of $\phi$  to $W^{\perp}$ and to $V$ to obtain the required V' . We know that $V \oplus$ V' is nondegenerate and orthogonal to $W$, which is also nondegenerate,
$$\oplus$$
so $(V \oplus V')^{\perp}\oplus W =$ V' $U$ is nondegenerate. We leave the second statement about extending $f$ as an exercise (use the fact that f(U) $=$ f(V $)^{\perp}\oplus$ f(W), where $V_{1} =$ f(V ) is totally isotropic of dimension $r$, to find another totally isotropic susbpace $V_{1}'$  of dimension $r$ such that $V_{1} \cap V_{1}'  = (0)$ and $V_{1} \oplus V_{1}'$  is orthogonal to f(W)).
$$\oplus$$
The subspace $(V \oplus V')^{\perp}\oplus W =$ V' $U$ is often called a nondegenerate completion of $U$. The subspace $V \oplus$ V' is called an Artinian space. Proposition 29.29 show that $V \oplus$ V' has a basis $(u_{1}, v_{1}, \dots  , u_{r}, v_{r})$ consisting of vectors $u_{i} \in V$ and $v_{j} \in$ V' such that $\phi (u_{i}, u_{j}) = \delta_{ij}$ . The subspace spanned by $(u_{i}, v_{i})$ is an Artinian plane, so $V \oplus$ V' is the orthogonal direct sum of $r$ Artinian planes. Such a space is often denoted by $Ar_{2r}$. In order to obtain the stronger version of the Witt decomposition when $\phi$  has some nonzero isotropic vector and $W$ is anisotropic we now sharpen Proposition 29.29

> **Theorem 29.33.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$ which is nondegenerate and satisfies property $(T)$. Let $U_{1}$ and $U_{2}$ be two totally isotropic maximal subspaces of $E$, with $U_{1}$ or $U_{2}$ of finite dimension $\ge 1$. Write $U = U_{1} \cap U_{2}$, let $S_{1}$ be a supplement of $U$ in $U_{1}$ and $S_{2}$ be a supplement of $U$ in $U_{2}$ (so that $U_{1} = U \oplus S_{1}, U_{2} = U \oplus S_{2})$, and let $S = S_{1} + S_{2}$. Then, there exist two subspaces $W$ and $D$ of $E$ such that:
(a) The subspaces $S, U + W$, and $D$ are nondegenerate and pairwise orthogonal.

<!-- PAGE 1045 -->
$(b)$ We have a direct sum $E = S^{\perp}\oplus (U \oplus W)^{\perp}\oplus D$.
$(c)$ The subspace $D$ contains no nonzero isotropic vector $(D$ is anisotropic).
$(d)$ The subspace $W$ is totally isotropic. Furthermore, $U_{1}$ and $U_{2}$ are both finite dimensional, and we have $dim(U_{1}) = dim(U_{2})$, dim(W) $=$ dim(U), $dim(S_{1}) = dim(S_{2})$, and codim(D) $= 2 dim(F_{1})$.

*Proof.* First observe that if $X$ is a totally isotropic maximal subspace of $E$, then any isotropic vector $x \in E$ orthogonal to $X$ must belong to $X$, since otherwise, $X +$ Kx would be a totally isotropic subspace strictly containing $X$, contradicting the maximality of $X$. As a consequence, if $x_{i}$ is any isotropic vector such that $x_{i} \in U_{i}^{\perp}$  (for $i = 1, 2)$, then $x_{i} \in U_{i}$. We claim that
$$S_{1} \cap S_{2}^{\perp} = (0)andS_{2} \cap S_{1}^{\perp} = (0).$$
Assume that $y \in S_{1}$ is orthogonal to $S_{2}$. Since $U_{1} = U \oplus S_{1}$ and $U_{1}$ is totally isotropic, $y$ is orthogonal to $U_{1}$, and thus orthogonal to $U$, so that $y$ is orthogonal to $U_{2} = U \oplus S_{2}$. Since $S_{1} \subseteq U_{1}$ and $U_{1}$ is totally isotropic, $y$ is an isotropic vector orthogonal to $U_{2}$, which by a previous remark implies that $y \in U_{2}$. Then, since $S_{1} \subseteq U_{1}$ and $U \oplus S_{1}$ is a direct sum, we have
$$y \in S_{1} \cap U_{2} = S_{1} \cap U_{1} \cap U_{2} = S_{1} \cap U = (0).$$
Therefore $S_{1} \cap S_{2}^{\perp} = (0)$. A similar proof show that $S_{2} \cap S_{1}^{\perp} = (0)$. If $U_{1}$ is finite-dimensional (the case where $U_{2}$ is finite-dimensional is similar), then $S_{1}$ is finite-dimensional, so by Proposition 29.13, $S_{1}^{\perp}$ has finite codimension. Since $S_{2}\cap S_{1}^{\perp} = (0)$, and since any supplement of $S_{1}^{\perp}$ has finite dimension, we must have
$$\dim(S_{2}) \le codim(S_{1}^{\perp} ) = \dim(S_{1}).$$
By a similar argument, $dim(S_{1}) \le dim(S_{2})$, so we have
$$\dim(S_{1}) = \dim(S_{2}).$$
By Proposition 29.29(1), we conclude that $S = S_{1} + S_{2}$ is nondegenerate. By Proposition 29.21, the subspace $N = S^{\perp} = (S_{1} + S_{2})^{\perp}$ is nondegenerate. Since $U_{1} = U \oplus S_{1}, U_{2} = U \oplus S_{2}$, and $U_{1}, U_{2}$ are totally isotropic, $U$ is orthogonal to $S_{1}$ and to $S_{2}$, so $U \subseteq N$. Since $U$ is totally isotropic, by Proposition 29.30 applied to $N$, there is a totally isotropic subspace $W$ of $N$ such that dim(W) $=$ dim(U), $U \cap W = (0)$, and $U + W$ is nondegenerate. Consequently, $(d)$ is satisfied by $W$. To satisfy (a) and $(b)$, we pick $D$ to be the orthogonal of $U \oplus W$ in $N$. Then, $N = (U \oplus W)^{\perp}\oplus D$ and $E = S^{\perp}\oplus N$, so $E = S^{\perp}\oplus (U \oplus W)^{\perp}\oplus D$. As to $(c)$, since $D$ is orthogonal $U \oplus W, D$ is orthogonal to $U$, and since $D \subseteq N$ and $N$ is orthogonal to $S_{1} + S_{2}, D$ is orthogonal to $S_{1}$, so $D$ is orthogonal to $U_{1} = U \oplus S_{1}$. If $y \in D$

<!-- PAGE 1046 -->
is any isotropic vector, since $y \in U_{1}^{\perp}$  , by a previous remark, $y \in U_{1}$, so $y \in D \cap U_{1}$. But, $D \subseteq N$ with $N \cap (S_{1} + S_{2}) = (0)$, and $D \cap (U + W) = (0)$, so $D \cap (U + S_{1}) = D \cap U_{1} = (0)$, which yields $y = 0$. The statements about dimensions are easily obtained. Finally, Theorem 29.33 yields the strong form of the Witt decomposition in which $W$ is anistropic. Given any matrix $A \in M_{n}(K)$, we say that $A$ is definite if $x^{\top}Ax \neq  0$ for all $x \in K^{n}$.

> **Theorem 29.34.** Let $\phi$  be an $\epsilon$ -Hermitian form on $E$ which is nondegenerate and satisfies property $(T)$.
$(1)$ Any two totally isotropic maximal spaces of finite dimension have the same dimension.
$(2)$ For any totally isotropic maximal subspace $U$ of finite dimension $r \ge 1$, there is another totally isotropic maximal subspace U' of dimension $r$ such that $U \cap$ U' $= (0)$, and $U \oplus$ U' is nondegenerate. Furthermore, if $D = (U \oplus U')^{\perp}$, then $(U$, U', $D)$ is a Witt decomposition of $E$; that is, there are no nonzero isotropic vectors in $D (D$ is anisotropic).
$(3)$ If $E$ has finite dimension $n \ge 1$ and there is some nonzero isotropic vector for $\phi  (E$ is not anisotropic), then $E$ has a nontrivial Witt decomposition $(U$, U' , $D)$ as in $(2)$. There is a basis of $E$ such that
$$(a) if \phi  is alternating (\epsilon  = -1 and \lambda  = \overline{\lambda} for all \lambda  \in K), then n = 2m and \phi  is$$
$$represented by a matrix of the form$$
$$\begin{pmatrix} 0 & I_{m} \\ -I_{m} & 0 \end{pmatrix}$$
$$(b) if \phi  is symmetric (\epsilon  = +1 and \lambda  = \overline{\lambda} for all \lambda  \in K), then \phi  is represented by a$$
$$matrix of the form$$
$$\begin{pmatrix} 0 & I_{r} & 0 \\ I_{r} & 0 & 0 \\ 0 & 0 & P \end{pmatrix} ,$$
$$where either n = 2r and P does not occur, or n > 2r and P is a definite symmetric$$
$$matrix.$$
$$(c) if \phi  is \epsilon -Hermitian (the involutive automorphism \lambda  \mapsto \overline{\lambda} is not the identity), then$$
$$\phi  is represented by a matrix of the form$$
$$\begin{pmatrix} 0 & I_{r} & 0 \\ \epsilon I_{r} & 0 & 0 \\ 0 & 0 & P \end{pmatrix} ,$$
$$where either n = 2r and P does not occur, or n > 2r and P is a definite matrix$$
$$such that P^{*} = \epsilon P.$$

<!-- PAGE 1047 -->

*Proof.* Part $(1)$ follows from Theorem 29.33. By Proposition 29.30, we obtain a totally isotropic subspace U' of dimension $r$ such that $U \cap$ U' $= (0)$. By applying Theorem 29.33 to $U_{1} = U$ and $U_{2} =$ U' , we get $U = W = (0)$, which proves $(2)$. Part $(3)$ is an immediate consequence of $(2)$. As a consequence of Theorem 29.34, we make the following definition.

> **Definition 29.19.** Let $E$ be a vector space of finite dimension $n$, and let $\phi$  be an $\epsilon$ -Hermitian form on $E$ which is nondegenerate and satisfies property $(T)$. The index (or Witt index) $\nu$ of $\phi$ , is the common dimension of all totally isotropic maximal subspaces of $E$. We have $2\nu  \le n$. Neutral forms only exist if $n$ is even, in which case, $\nu  = n/2$. Forms of index $\nu  = 0$ have no nonzero isotropic vectors. When $K = \mathbb{R}$, this is satisfied by positive definite or negative definite symmetric forms. When $K = \mathbb{C}$, this is satisfied by positive definite or negative definite Hermitian forms. The vector space of a neutral Hermitian form $(\epsilon  = +1)$ is an Artinian space, and the vector space of a neutral alternating form is a hyperbolic space. If the field $K$ is algebraically closed, we can describe all nondegenerate quadratic forms.

> **Proposition 29.35.** If $K$ is algebraically closed and $E$ has dimension $n$, then for every nondegenerate quadratic form $\Phi$ , there is a basis $(e_{1}, \dots  , e_{n})$ such that $\Phi$  is given by
$$\Phi \sum_{i-1}^{n}  =( \sum_{imi}  m=1 x_{i}x_{m+i}if n = 2m$$
$$\begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum  =1 x_{i}x_{m+i} + x_{2m+1}^{2}if n = 2m + 1.$$

*Proof.* We work with the polar form $\phi$  of $\Phi$ . Let $U_{1}$ and $U_{2}$ be some totally isotropic subspaces such that $U_{1} \cap U_{2} = (0)$ given by Theorem 29.34, and let $q$ be their common dimension. Then, $W = U = (0)$. Since we can pick bases $(e_{1}, \dots  e_{q})$ in $U_{1}$ and $(e_{q+1}, \dots  , e_{2q})$ in $U_{2}$ such that $\phi (e_{i}, e_{i+q}) = 0$, for $i, j = 1, \dots  , q$, it suffices to proves that dim(D) $\le 1$. If $x, y \in D$ with $x \neq  0$, from the identity
$$\Phi (y -\lambda x) = \Phi (y) -\lambda \phi (x, y) + \lambda^{2} \Phi (x)$$
and the fact that $\Phi (x) \neq  0$ since $x \in D$ and $x \neq  0$, we see that the equation $\Phi (y$ - $\lambda y) = 0$ has at least one solution. Since $\Phi (z) \neq  0$ for every nonzero $z \in D$, we get $y = \lambda x$, and thus dim(D) $\le 1$, as claimed. Proposition 29.35 shows that for every nondegenerate quadratic form $\Phi$  over an algebraically closed field, if dim(E) $=$ 2m or dim(E) $=$ 2m $+ 1$ with $m \ge 1$, then $\Phi$  has some nonzero isotropic vector.
