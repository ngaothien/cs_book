# Orthogonality


<!-- PAGE 1023 -->
Proposition 29.5 also holds for sesquilinear forms and their matrix representations. Observe that if $\phi$  is a Hermitian form $(E = F)$ and if $K$ does not have characteristic $2$, then by Theorem 29.10, there is a basis of $E$ with respect to which the matrix $M$ representing $\phi$  is a diagonal matrix. If $K = \mathbb{C}$, then these entries are real, and this allows us to classify completely the Hermitian forms.

> **Proposition 29.11.** Given any Hermitian form $\phi$ : $E \times  E \to \mathbb{C}$ with dim(E) $= n$, there is a basis $(e_{1}, \dots  , e_{n})$ of $E$ such that
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
with $0 \le p, q$ and $p + q \le n$. The proof of Proposition 29.11 is the same as the real case of Proposition 29.6. Sylvester’s inertia law (Proposition 29.7) also holds for Hermitian forms: $p$ and $q$ only depend on $\phi$ .

## 29.3 Orthogonality

In this section we assume that we are dealing with a sesquilinear form $\phi$ : $E \times  F \to K$. We allow the automorphism $\lambda  \mapsto \overline{\lambda}$ to be the identity, in which case $\phi$  is a bilinear form. This way, we can deal with properties shared by bilinear forms and sesquilinear forms in a uniform fashion. Orthogonality is such a property.

> **Definition 29.12.** Given a sesquilinear form $\phi$ : $E \times F \to K$, we say that two vectors $u \in E$ and $v \in F$ are orthogonal (or conjugate) if $\phi (u, v) = 0$. Two subsets E' $\subseteq E$ and F' $\subseteq F$ are orthogonal if $\phi (u, v) = 0$ for all $u \in$ E' and all $v \in$ F'. Given a subspace $U$ of $E$, the right orthogonal space of $U$, denoted $U^{\perp}$ , is the subspace of $F$ given by
$$U^{\perp} = {v \in F | \phi (u, v) = 0for all u \in U},$$
and given a subspace $V$ of $F$, the left orthogonal space of $V$ , denoted $V^{\perp}$ , is the subspace of $E$ given by
$$V^{\perp} = {u \in E | \phi (u, v) = 0for all v \in V }.$$
When $E$ and $F$ are distinct, there is little chance of confusing the right orthogonal subspace $U^{\perp}$ of a subspace $U$ of $E$ and the left orthogonal subspace $V^{\perp}$ of a subspace $V$ of $F$. However, if $E = F$, then $\phi (u, v) = 0$ does not necessarily imply that $\phi (v, u) = 0$, that is, orthogonality is not necessarily symmetric. Thus, if both $U$ and $V$ are subsets of $E$, there is a notational ambiguity if $U = V$ . In this case, we may write $U^{\perp r}$  for the right orthogonal and $U^{\perp l}$  for the left orthogonal. The above discussion brings up the following point: When is orthogonality symmetric?

<!-- PAGE 1024 -->
If $\phi$  is bilinear, it is shown in $E$. Artin $[6]$ (and in Jacobson $[101])$ that orthogonality is symmetric iff either $\phi$  is symmetric or $\phi$  is alternating $(\phi (u, u) = 0$ for all $u \in E)$. If $\phi$  is sesquilinear, the answer is more complicated. In addition to the previous two cases, there is a third possibility:
$$\phi (u, v) =\overline{\epsilon \phi}\overline{(}\overline{v, u}\overline{)} for all u, v \in E,$$
where $\epsilon$  is some nonzero element in $K$. We say that $\phi$  is $\epsilon$ -Hermitian. Observe that
$$\phi (u, u) =\overline{\epsilon \epsilon \phi}(u, u),$$
so if $\phi$  is not alternating, then $\phi (u, u) \neq  0$ for some $u$, and we must have $\overline{\epsilon \epsilon} = 1$. The most common cases are $1. \epsilon  = 1$, in which case $\phi$  is Hermitian, and $2. \epsilon  = -1$, in which case $\phi$  is skew-Hermitian. If $\phi$  is alternating and $K$ is not of characteristic $2$, then equation (*) from Section 29.2 implies that the automorphism $\lambda  \mapsto \overline{\lambda}$ must be the identity if $\phi$  is nonzero. If so, $\phi$  is skew-symmetric, so $\epsilon  = -1$. In summary, if $\phi$  is either symmetric, alternating, or $\epsilon$ -Hermitian, then orthogonality is symmetric, and it makes sense to talk about the orthogonal subspace $U^{\perp}$ of $U$. Observe that if $\phi$  is $\epsilon$ -Hermitian, then
$$r_{\phi} = \epsilon l_{\phi}.$$
This is because
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)}$$
$$r_{\phi}(u)(y) = \phi (y, u)$$
$$=\overline{\epsilon \phi}\overline{(}\overline{u, y}\overline{)},$$
so $r_{\phi} = \epsilon l_{\phi}$. If $E$ and $F$ are finite-dimensional with bases $(e_{1}, \dots  , e_{m})$ and $(f_{1}, \dots  , f_{n})$, and if $\phi$  is represented by the $n \times  m$ matrix $M$, then $\phi$  is $\epsilon$ -Hermitian iff
$$M = \epsilon M^{*} ,$$
where $M^{*} = (\overline{M})^{\top}$ (as usual). This captures the following kinds of familiar matrices: $1$. Symmetric matrices $(\epsilon  = 1) 2$. Skew-symmetric matrices $(\epsilon  = -1)$

<!-- PAGE 1025 -->
$3$. Hermitian matrices $(\epsilon  = 1) 4$. Skew-Hermitian matrices $(\epsilon  = -1)$. Going back to a sesquilinear form $\phi$ : $E \times  F \to K$, for any subspace $U$ of $E$, it is easy to check that
$$U \subseteq (U^{\perp} )^{\perp},$$
and that for any subspace $V$ of $F$, we have
$$V \subseteq (V^{\perp} )^{\perp}.$$
For simplicity of notation, we write $U^{\perp \perp}$ instead of $(U^{\perp} )^{\perp}$ (and $V^{\perp \perp}$ instead of $(V^{\perp} )^{\perp})$. Given any two subspaces $U_{1}$ and $U_{2}$ of $E$, if $U_{1} \subseteq U_{2}$, then $U_{2}^{\perp}  \subseteq U_{1}^{\perp}$ . Indeed, if $v \in U_{2}^{\perp}$ then $\phi (u_{2}, v) = 0$ for all $u_{2} \in U_{2}$, and since $U_{1} \subseteq U_{2}$ this implies that $\phi (u_{1}, v) = 0$ for all $u_{1} \in U_{1}$, which shows that $v \in U_{1}^{\perp}$  . Similarly for any two subspaces $V_{1}, V_{2}$ of $F$, if $V_{1} \subseteq V_{2}$, then $V_{2}^{\perp}  \subseteq V_{1}^{\perp}$  . As a consequence,
$$U^{\perp} = U^{\perp \perp \perp} ,V^{\perp} = V^{\perp \perp \perp} .$$
First, we have $U^{\perp} \subseteq U^{\perp \perp \perp}$ . Second, from $U \subseteq U^{\perp \perp}$ , we get $U^{\perp \perp \perp} \subseteq U^{\perp}$ , so $U^{\perp} = U^{\perp \perp \perp}$ . The other equation is proved is a similar way. Observe that $\phi$  is nondegenerate iff $E^{\perp} = {0}$ and $F^{\perp} = {0}$. Furthermore, since
$$\phi (u + x, v) = \phi (u, v)$$
$$\phi (u, v + y) = \phi (u, v)$$
for any $x \in F^{\perp}$ and any $y \in E^{\perp}$, we see that we obtain by passing to the quotient a sesquilinear form
$$[\phi ]: (E/F^{\perp} ) \times  (F/E^{\perp}) \to K$$
which is nondegenerate.

> **Proposition 29.12.** For any sesquilinear form $\phi$ : $E \times  F \to K$, the space $E/F^{\perp}$ is finite-dimensional iff the space $F/E^{\perp}$ is finite-dimensional; if so, $dim(E/F^{\perp}$ ) $= dim(F/E^{\perp})$.
$$Proof. \frac{Since}{(E/F^{\perp})} the sesquilinear form [\phi \frac{]:(E/F^{\perp}}{(F/E^{\perp})} ) \times  (F/E^{\perp}) \to K is nondegenerate, the maps$$
$l_{[\phi]}$ :   $\to (F/E^{\perp})^{*}$ and $r_{[\phi]}$ :  $\to (E/F^{\perp} )^{*}$ are injective. If $dim(E/F^{\perp}$ ) $=$
$$m, \frac{thendim(}{F/E^{\perp}))} E/F^{\perp} ) = \dim((E/F^{\perp} )^{*}), so by injectivity of r_{[\phi]}, we have \dim(F/E^{\perp}) =$$
$$\dim(( \le m. \frac{A similar reasoning using the injectivity of}{E/F^{\perp}))} l_{[\phi]} applies if \dim(F/E^{\perp}) = n,$$
and we get $dim(E/F^{\perp}$ ) $=$ dim((   $\le n$. Therefore, $dim(E/F^{\perp}$ ) $= m$ is finite iff $dim(F/E^{\perp}) = n$ is finite, in which case $m = n$ by Proposition 29.1(d).

<!-- PAGE 1026 -->
If $U$ is a subspace of a space $E$, recall that the codimension of $U$ is the dimension of $E/U$, which is also equal to the dimension of any subspace $V$ such that $E$ is a direct sum of $U$ and $V (E = U \oplus V$ ). Proposition 29.12 implies the following useful fact.

> **Proposition 29.13.** Let $\phi$ : $E\times F \to K$ be any nondegenerate sesquilinear form. A subspace $U$ of $E$ has finite dimension iff $U^{\perp}$ has finite codimension in $F$. If dim(U) is finite, then $codim(U^{\perp}$ ) $=$ dim(U), and $U^{\perp \perp} = U$.

*Proof.* Since $\phi$  is nondegenerate $E^{\perp} = {0}$ and $F^{\perp} = {0}$, so Proposition 29.12 applied to the restriction of $\phi$  to $U \times  F$ implies that a subspace $U$ of $E$ has finite dimension iff $U^{\perp}$ has finite codimension in $F$, and that if dim(U) is finite, then $codim(U^{\perp}$ ) $=$ dim(U). Since $U^{\perp}$ and $U^{\perp \perp}$ are orthogonal, and since $codim(U^{\perp}$ ) is finite, $dim(U^{\perp \perp}$ ) is finite and we have $dim(U^{\perp \perp}$ ) $= codim(U^{\perp \perp \perp}$ ) $= codim(U^{\perp}$ ) $=$ dim(U). Since $U \subseteq U^{\perp \perp}$ , we must have $U = U^{\perp \perp}$ .

> **Proposition 29.14.** Let $\phi$ : $E \times F \to K$ be any sesquilinear form. Given any two subspaces $U$ and $V$ of $E$, we have
$$(U + V )^{\perp}= U^{\perp} \cap V^{\perp} .$$
Furthermore, if $\phi$  is nondegenerate and if $U$ and $V$ are finite-dimensional, then
$$(U \cap V )^{\perp}= U^{\perp} + V^{\perp} .$$

*Proof.* If $w \in (U + V )^{\perp}$, then $\phi (u + v, w) = 0$ for all $u \in U$ and all $v \in V$ . In particular, with $v = 0$, we have $\phi (u, w) = 0$ for all $u \in U$, and with $u = 0$, we have $\phi (v, w) = 0$ for all $v \in V$ , so $w \in U^{\perp} \cap V^{\perp}$ . Conversely, if $w \in U^{\perp} \cap V^{\perp}$ , then $\phi (u, w) = 0$ for all $u \in U$ and $\phi (v, w) = 0$ for all $v \in V$ . By bilinearity, $\phi (u + v, w) = \phi (u, w) + \phi (v, w) = 0$, which shows that $w \in (U + V )^{\perp}$. Therefore, the first identity holds. Now, assume that $\phi$  is nondegenerate and that $U$ and $V$ are finite-dimensional, and let $W = U^{\perp} + V^{\perp}$ . Using the equation that we just established and the fact that $U$ and $V$ are finite-dimensional, by Proposition 29.13, we get
$$W^{\perp} = U^{\perp \perp} \cap V^{\perp \perp} = U \cap V.$$
We can apply Proposition 29.12 to the restriction of $\phi$  to $U \times  W$ (since $U^{\perp} \subseteq W$ and $W^{\perp} \subseteq U)$, and we get
$$\dim(U/W^{\perp} ) = \dim(U/(U \cap V )) = \dim(W/U^{\perp} ).$$
If $T$ is a supplement of $U^{\perp}$ in $W$ so that $W = U^{\perp} \oplus T$ and if $S$ is a supplement of $W$ in $E$ so that $E = W \oplus S$, then codim(W) $=$ dim(S), dim(T) $= dim(W/U^{\perp}$ ), and we have the direct sum
$$E = U^{\perp} \oplus T \oplus S$$

<!-- PAGE 1027 -->
which implies that
$$\dim(T) = codim(U^{\perp} ) -\dim(S) = codim(U^{\perp} ) -codim(W)$$
so
$$\dim(U/(U \cap V )) = \dim(W/U^{\perp} ) = codim(U^{\perp} ) -codim(W),$$
and since $codim(U^{\perp}$ ) $=$ dim(U), we deduce that
$$\dim(U \cap V ) = codim(W).$$
However, by Proposition 29.13, we have dim(U $\cap V$ ) $=$ codim((U $\cap V )^{\perp})$, so codim(W) $=$ codim((U $\cap V )^{\perp})$, and since $W \subseteq W^{\perp \perp} = (U \cap V )^{\perp}$, we must have $W = (U \cap V )^{\perp}$, as claimed. In view of Proposition 29.12, we can make the following definition.

> **Definition 29.13.** Let $\phi$ : $E \times  F \to K$ be any sesquilinear form. If $E/F^{\perp}$ and $F/E^{\perp}$ are finite-dimensional, then their common dimension is called the rank of the form $\phi$ . If $E/F^{\perp}$ and $F/E^{\perp}$ have infinite dimension, we say that $\phi$  has infinite rank. Not surprisingly, the rank of $\phi$  is related to the ranks of $l_{\phi}$ and $r_{\phi}$.

> **Proposition 29.15.** Let $\phi$ : $E \times  F \to K$ be any sesquilinear form. If $\phi$  has finite rank $r$, then $l_{\phi}$ and $r_{\phi}$ have the same rank, which is equal to $r$.

*Proof.* Because for every $u \in E$,
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)} for all y \in F,$$
and for every $v \in F$,
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E,$$
it is clear that the kernel of $l_{\phi}$ : $\overline{E} \to F^{*}$ is equal to $F^{\perp}$ and that, the kernel of $r_{\phi}$ : $\overline{F} \to E^{*}$ is equal to $E^{\perp}$. Therefore, $rank(l_{\phi}) =$ dim(Im $l_{\phi}) = dim(E/F^{\perp}$ ) $= r$, and similarly $rank(r_{\phi}) = dim(F/E^{\perp}) = r$.
Remark: If the sesquilinear form $\phi$  is represented by the matrix $n \times  m$ matrix $M$ with respect to the bases $(e_{1}, \dots  , e_{m})$ in $E$ and $(f_{1}, \dots  , f_{n})$ in $F$, it can be shown that the matrix representing $l_{\phi}$ with respect to the bases $(e_{1}, \dots  , e_{m})$ and $(f_{1}^{*} , \dots  , f_{n}^{*})$ is $\overline{M}$, and that the matrix representing $r_{\phi}$ with respect to the bases $(f_{1}, \dots  , f_{n})$ and $(e_{1}^{*}, \dots  , e_{m}^{*})$ is $M^{\top}$. It follows that the rank of $\phi$  is equal to the rank of $M$.
