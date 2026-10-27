# Witt's Theorem


<!-- PAGE 1059 -->

## 29.10 Witt’s Theorem

Witt’s theorem was referred to as a “scandal” by Emil Artin. What he meant by this is that one had to wait until $1936$ (Witt $[196])$ to formulate and prove a theorem at once so simple in its statement and underlying concepts, and so useful in various domains (geometry, arithmetic of quadratic $forms).^{1}$ Besides Witt’s original proof (Witt $[196])$, Chevalley’s proof $[37]$ seems to be the “best” proof that applies to the symmetric as well as the skew-symmetric case. The proof in Bourbaki $[24]$ is based on Chevalley’s proof, and so are a number of other proofs. This is the one we follow (slightly reorganized). In the symmetric case, Serre’s exposition is hard to beat (see Serre $[163]$, Chapter IV). The following observation is one of the key ingredients in the proof of Theorem 29.45.

> **Proposition 29.44.** Given a finite-dimensional space $E$ equipped with an $\epsilon$ -Hermitan form $\phi$ , if $U_{1}$ and $U_{2}$ are two subspaces of $E$ such that $U_{1} \cap U_{2} = (0)$ and if we have metric linear maps $f_{1}$ : $U_{1} \to E$ and $f_{2}$ : $U_{2} \to E$ such that
$$\phi (f_{1}(u_{1}), f_{2}(u_{2})) = \phi (u_{1}, u_{2})for u_{i} \in U_{i} (i = 1, 2),(*)$$
then the linear map $f$ : $U_{1} \oplus U_{2} \to E$ given by $f(u_{1} + u_{2}) = f_{1}(u_{1}) + f_{2}(u_{2})$ extends $f_{1}$ and $f_{2}$ and is metric. Furthermore, if $f_{1}$ and $f_{2}$ are injective, then so if $f$.

*Proof.* Indeed, since $f_{1}$ and $f_{2}$ are metric and using (*), we have $\phi (f_{1}(u_{1}) + f_{2}(u_{2}), f_{1}(v_{1}) + f_{2}(v_{2})) = \phi (f_{1}(u_{1}), f_{1}(v_{1})) + \phi (f_{1}(u_{1}), f_{2}(v_{2}))$
$$+ \phi (f_{2}(u_{2}), f_{1}(v_{1})) + \phi (f_{2}(u_{2}), f_{2}(v_{2}))$$
$$= \phi (u_{1}, v_{1}) + \phi (u_{1}, v_{2}) + \phi (u_{2}, v_{1}) + \phi (u_{2}, v_{2})$$
$$= \phi (u_{1} + u_{2}, v_{2} + v_{2}).$$
Thus $f$ is a metric map extending $f_{1}$ and $f_{2}$.

> **Theorem 29.45.** (Witt, $1936)$ Let $E$ and E' be two finite-dimensional spaces respectively equipped with two nondegenerate $\epsilon$ -Hermitan forms $\phi$  and $\phi'$ satisfying condition $(T)$, and assume that there is an isometry between $(E, \phi$ ) and (E', $\phi'$ ). For any subspace $U$ of $E$, every injective metric linear map $f$ from $U$ into E' extends to an isometry from $E$ to E'.

*Proof.* Since $(E, \phi$ ) and (E', $\phi'$ ) are isometric, we may assume that E' $= E$ and $\phi' = \phi$  (if $h: E \to$ E' is an isometry, then $h^{-1}\circ f$ is an injective metric map from $U$ into $E$. The details are left to the reader). $\overline{1}\overline{Curiously$, some references to Witt’s paper claim its date of publication to be $1936$, but others say $1937.}$ The answer to this mystery is that Volume $176$ of Crelle Journal was published in four issues. The cover page of volume $176$ mentions the year $1937$, but Witt’s paper is dated May $1936$. This is not the only paper of Witt appearing in this volume!

<!-- PAGE 1060 -->
We proceed by induction on the dimension $r$ of $U$. Since the proof is quite intricate, we spell out the general plan of attack. For the induction step, we first show that we can reduce the situation to what we call Case $(H)$, namely that the subspace of $U$ left fixed by $f$ is a hyperplane $H$ in $U$. Then, the set $D = {f(u)$ - $u$ | $u \in U}$ is a line in $U$ and it turns out that $D^{\perp}$ is a hyperplane in $E$. We now introduce Hypothesis $(V)$, which says we can find a nontrivial subspace $V$ of $E$ orthogonal to $D$ and such that $V \cap U = V \cap$ f(U) $= (0)$. We show that if Hypothesis $(V)$ holds, then $f$ can be extended to an isometry of $U \oplus V$ . It is then possible to further extend $f$ to an isometry of $E$. To prove that Hypothesis $(V)$ holds we consider two cases. In Case (a), we obtain some $V$ such that $E = U \oplus V$ and we are done. In Case $(b)$, we obtain some $V$ such that $D^{\perp} = U \oplus V$ . We are then reduced to the situation where $U = D^{\perp}$ is a hyperplane in $E$ and $f$ is an isometry of $U$. To finish the proof we pick any $v \in / U$, so that $E = U \oplus$ Kv, and we find some $v_{1} \in E$ such that
$$\phi (f(u), v_{1}) = \phi (u, v)for all u \in U$$
$$\phi (v_{1}, v_{1}) = \phi (v, v).$$
Then, by Proposition 29.44, we can extend $f$ to a metric map $g$ of $U +$ Kv $= E$ such that g(v) $= v_{1}$. The argument used to find $v_{1}$ makes use of $(\dagger$ ) (see below) and is bit tricky. We also makes use of Property $(T)$ in the form of Lemma 29.28. We now go back to the proof. The case $r = 0$ is trivial. For the induction step, $r \ge 1$ so $U \neq  (0)$, and let $H$ be any hyperplane in $U$. Let $f$ : $U \to E$ be an injective metric linear map. By the induction hypothesis, the restriction $f_{0}$ of $f$ to $H$ extends to an isometry $g_{0}$ of $E$. If $g_{0}$ extends $f$, we are done. Otherwise, $H$ is the subspace of elements of $U$ left fixed by $g_{0}^{-1} \circ f$. If the theorem holds in this situation, namely the subspace of $U$ left fixed by $g_{0}^{-1} \circ f$ is a hyperplane $H$ in $U$, then we have an isometry $g_{1}$ of $E$ extending $g_{0}^{-1} \circ f$, and $g_{0} \circ g_{1}$ is an isometry of $E$ extending $f$. Therefore, we are reduced to the following situation: Case $(H)$. The subspace of $U$ left fixed by $f$ is a hyperplane $H$ in $U$. In this case, the set $D = {f(u)$ - $u$ | $u \in U}$ is a line in $U$ (a one-dimensional subspace). For all $u, v \in U$, we have $\phi$ (f(u), f(v) - $v) = \phi$ (f(u), f(v)) - $\phi$ (f(u), $v) = \phi (u, v)$ - $\phi$ (f(u), $v) = \phi (u$ - f(u), $v)$, that is
$$\phi (f(u), f(v) -v) = \phi (u -f(u), v)for all u, v \in U,(**)$$
and if $u \in H$, which means that f(u) $= u$, we get $u \in D^{\perp}$. Therefore, $H \subseteq D^{\perp}$. Since $\phi$  is nondegenerate, we have dim(D) $+ dim(D^{\perp}) =$ dim(E), and since dim(D) $= 1$, the subspace $D^{\perp}$ is a hyperplane in $E$. Hypothesis $(V)$. We can find a nontrivial subspace $V$ of $E$ orthogonal to $D$ and such that $V \cap U = V \cap$ f(U) $= (0)$. Claim. Hypothesis $(V)$ implies that $f$ can be extended to an isometry of $U \oplus V$ .

<!-- PAGE 1061 -->
Proof of Claim. If Hypothesis $(V)$ holds, then we have
$$\phi (f(u), v) = \phi (u, v)for all u \in U and all v \in V ,$$
since $\phi$ (f(u), $v)$ - $\phi (u, v) = \phi$ (f(u) - $u, v) = 0$, with f(u) - $u \in D$ and $v \in V$ orthogonal to $D$. By Proposition 29.44 with $f_{1} = f$ and $f_{2}$ the inclusion of $V$ into $E$, we can extend $f$ to an injective metric map on $U \oplus V$ leaving all vectors in $V$ fixed. In this case, the set ${f(w)$ - $w$ | $w \in U \oplus V$ } is still the line $D$. We show below that the fact that $f$ can be extended to $U \oplus V$ implies that $f$ can be extended to the whole of $E$. There are two cases. In Case (a), $E = U \oplus V$ and we are done. In case $(b), D^{\perp} = U \oplus V$ where $D^{\perp}$ is a hyperplane in $E$ and $f$ is an isometry of $D^{\perp}$. By a subtle argument, we will show that $f$ can be extended to an isometry of $E$. We are reduced to proving that a subspace $V$ as above exists. We distinguish between two cases. Case (a). U̸ $\subseteq D^{\perp}$. Proof of Case (a). In this case, formula (**) show that f(U) is not contained in $D^{\perp}$ (check this!). Consequently,
$$U \cap D^{\perp}= f(U) \cap D^{\perp}= H.$$
We can pick $V$ to be any supplement of $H$ in $D^{\perp}$, and the above formula shows that $V \cap U = V \cap$ f(U) $= (0)$. Since $U \oplus V$ contains the hyperplane $D^{\perp}$ (since $D^{\perp} = H \oplus V$ and $H \subseteq U)$, and $U \oplus$ V̸ $= D^{\perp}$ (since $U$ is not contained in $D^{\perp}$ and $V \subseteq D^{\perp})$, we must have $E = U \oplus V$ , and as we showed as a consequence of hypothesis $(V), f$ can be extended to an isometry of $U \oplus V = E$. Case $(b). U \subseteq D^{\perp}$. Proof of Case $(b)$. In this case, formula (**) shows that f(U) $\subseteq D^{\perp}$ so $U +f(U) \subseteq D^{\perp}$, and since $D = {f(u)$ - $u$ | $u \in U}$, we have $D \subseteq D^{\perp}$; that is, the line $D$ is isotropic. We show that there exists a subspace $V$ of $D^{\perp}$, such that
$$D^{\perp}= U \oplus V = f(U) \oplus V.$$
Thus, case $(b)$ shows that we are reduced to the situation where $U = D^{\perp}$ and $f$ is an isometry of $U$. If $U =$ f(U) we pick $V$ to be a supplement of $U$ in $D^{\perp}$. Otherwise, let $x \in U$ with $x \in / H$, and let $y \in$ f(U) with $y \in / H$. Since f(H) $= H$ (pointwise), $f$ is injective, and $H$ is a hyperplane in $U$, we have
$$U = H \oplus Kx,f(U) = H \oplus Ky.$$

<!-- PAGE 1062 -->
We claim that $x + y \in / U$. Otherwise, since $y = x + y$ - $x$, with $x + y, x \in U$ and since $y \in$ f(U), we would have $y \in U \cap$ f(U) $= H$, a contradiction. Similarly, $x + y \in /$ f(U). It follows that
$$U + f(U) = U \oplus K(x + y) = f(U) \oplus K(x + y).$$
Now, pick $W$ to be any supplement of $U +$ f(U) in $D^{\perp}$ so that $D^{\perp} = (U +$ f(U)) $\oplus W$, and let
$$V = K(x + y) + W.$$
Then, since $x \in U, y \in$ f(U), $W \subseteq D^{\perp}$, and $U +$ f(U) $\subseteq D^{\perp}$, we have $V \subseteq D^{\perp}$. We also have
$$U \oplus V = U \oplus K(x + y) \oplus W = (U + f(U)) \oplus W = D^{\perp}$$
and
$$f(U) \oplus V = f(U) \oplus K(x + y) \oplus W = (U + f(U)) \oplus W = D^{\perp},$$
so as we showed as a consequence of hypothesis $(V), f$ can be extended to an isometry of the hyperplane $D^{\perp} = U \oplus V$ , and $D$ is still the line ${f(w)$ - $w$ | $w \in U \oplus V$ }. The argument in the proof of Case $(b)$ shows that we are reduced to the situation where $U = D^{\perp}$ is a hyperplane in $E$ and $f$ is an isometry of $U$. If we pick any $v \in / U$, then $E = U \oplus$ Kv, so suppose we can find some $v_{1} \in E$ such that
$$\phi (f(u), v_{1}) = \phi (u, v)for all u \in U$$
$$\phi (v_{1}, v_{1}) = \phi (v, v).$$
The first condition is condition (*) of Proposition 29.44, and the second condition asserts that the map $\lambda v \mapsto \lambda v_{2}$ from the line Kv to the line $Kv_{1}$ is a metric map. Then, by Proposition 29.44, we can extend $f$ to a metric map $g$ of $U +$ Kv $= E$ such that g(v) $= v_{1}$. To find $v_{1}$, let us prove that for every $v \in E$, there is some v' $\in E$ such that
$$\phi (f(u), v') = \phi (u, v)for all u \in U.(\dagger )$$
This is because the linear form $u \mapsto \phi (f^{-1} (u), v) (u \in U)$ is the restriction of a linear form $\psi  \in E^{*}$, and since $\phi$  is nondegenerate, there is some (unique) v' $\in E$, such that
$$\psi (x) = \phi (x, v')for all x \in E,$$
which implies that
$$\phi (u, v') = \phi (f^{-1} (u), v)for all u \in U,$$
and since $f$ is an automorphism of $U$, that $(\dagger$ ) holds. Furthermore, observe that formula $(\dagger$ ) still holds if we add to v' any vector $y$ in $D$, since f(U) $= U = D^{\perp}$. Therefore, for any $v_{1} =$ v' $+ y$ with $y \in D$, if we extend $f$ to a linear map of $E$ by setting g(v) $= v_{1}$, then by $(\dagger$ ) we have
$$\phi (g(u), g(v)) = \phi (u, v)for all u \in U.$$

<!-- PAGE 1063 -->
We still need to pick $y \in D$ so that $v_{1} =$ v' $+ y$ satisfies $\phi (v_{1}, v_{1}) = \phi (v, v)$. However, since $v \in / U = D^{\perp}$, the vector $v$ is not orthogonal $D$, and by Lemma 29.28, there is some $y_{0} \in D$ such that
$$\phi (v'+ y_{0}, v'+ y_{0}) = \phi (v, v).$$
Then, if we let $v_{1} =$ v' $+ y_{0}$, by Proposition 29.44, we can extend $f$ to a metric map $g$ of $U +$ Kv $= E$ by setting g(v) $= v_{1}$. Since $\phi$  is nondegenerate, $g$ is an isometry. The first corollary of Witt’s theorem is sometimes called the Witt’s cancellation theorem.

> **Theorem 29.46.** (Witt Cancellation Theorem) Let $(E_{1}, \phi_{1}$ ) and $(E_{2}, \phi_{2}$ ) be two pairs of finite-dimensional spaces and nondegenerate $\epsilon$ -Hermitian forms satisfying condition $(T)$, and assume that $(E_{1}, \phi_{1}$ ) and $(E_{2}, \phi_{2}$ ) are isometric. For any subspace $U$ of $E_{1}$ and any subspace $V$ of $E_{2}$, if there is an isometry $f$ : $U \to V$ , then there is an isometry $g: U^{\perp} \to V^{\perp}$ .

*Proof.* If $f$ : $U \to V$ is an isometry between $U$ and $V$ , by Witt’s theorem (Theorem 29.46), the linear map $f$ extends to an isometry $g$ between $E_{1}$ and $E_{2}$. We claim that $g$ maps $U^{\perp}$ into $V^{\perp}$ . This is because if $v \in U^{\perp}$ , we have $\phi_{1} (u, v) = 0$ for all $u \in U$, so
$$\phi_{2} (g(u), g(v)) = \phi_{1} (u, v) = 0for all u \in U,$$
and since $g$ is a bijection between $U$ and $V$ , we have g(U) $= V$ , so we see that g(v) is orthogonal to $V$ for every $v \in U^{\perp}$ ; that is, $g(U^{\perp}$ ) $\subseteq V^{\perp}$ . Since $g$ is a metric map and since $\phi_{1}$  is nondegenerate, the restriction of $g$ to $U^{\perp}$ is an isometry from $U^{\perp}$ to $V^{\perp}$ . A pair $(E, \phi$ ) where $E$ is finite-dimensional and $\phi$  is a nondegenerate $\epsilon$ -Hermitian form is often called an $\epsilon$ -Hermitian space. When $\epsilon  = 1$ and $\phi$  is symmetric, we use the term
$$Euclidean space or quadratic space. When \epsilon  = -1 and \phi \frac{is}{\lambda} alternating, we use the term$$
symplectic space. When $\epsilon  = 1$ and the automorphism $\lambda  \mapsto$  is not the identity we use the term Hermitian space, and when $\epsilon  = -1$, we use the term skew-Hermitian space. We also have the following result showing that the group of isometries of an $\epsilon$ -Hermitian space is transitive on totally isotropic subspaces of the same dimension.

> **Theorem 29.47.** Let $E$ be a finite-dimensional vector space and let $\phi$  be a nondegenerate $\epsilon$ -Hermitian form on $E$ satisfying condition $(T)$. Then for any two totally isotropic subspaces $U$ and $V$ of the same dimension, there is an isometry $f \in Isom(\phi$ ) such that f(U) $= V$ . Furthermore, every linear automorphism of $U$ is induced by an isometry of $E$.
Remark: Witt’s cancelation theorem can be used to define an equivalence relation on $\epsilon$ - Hermitian spaces and to define a group structure on these equivalence classes. This way, we obtain the Witt group, but we will not discuss it here. Witt’s Theorem can be sharpened to isometries in $SO(\phi$ ), but some condition on $U$ is needed.

<!-- PAGE 1064 -->

> **Theorem 29.48.** (Witt–Sharpened Version) Let $E$ be a finite-dimensional space equipped with a nondegenerate symmetric bilinear forms $\phi$ . For any subspace $U$ of $E$, every linear injective metric map $f$ from $U$ into $E$ extends to an isometry $g$ of $E$ with a prescribed value $\pm 1$ of det(g) iff
$$\dim(U) + \dim(rad(U)) < \dim(E) = n.$$
If
$$\dim(U) + \dim(rad(U)) = \dim(E) = n,$$
and det(f) $= -1$, then there is no $g \in SO(\phi$ ) extending $f$.

*Proof.* If $g_{1}$ and $g_{2}$ are two extensions of $f$ such that $det(g_{1}) det(g_{2}) = -1$, then $h = g_{1}^{-1} \circ g_{2}$ is an isometry such that det(h) $= -1$, and $h$ leaves every vector of $U$ fixed. Conversely, if $h$ is an isometry such that det(h) $= -1$, and h(u) $= u$ for all $u \in U$, then for any extesnion $g_{1}$ of $f$, the map $g_{2} = h \circ g_{1}$ is another extension of $f$ such that $det(g_{2}) = -det(g_{1})$. Therefore, we need to show that a map $h$ as above exists.
$$If \dim(U)+\dim(rad(U)) < \dim(E), consider the nondegenerate completion\overline{U} of U \frac{given}{U}$$
by Proposition 29.32. We know that $dim(\overline{U}) =$ dim(U) $+$ dim(rad(U)) $< n$, and since  is nondegenerate, we have
$$E =\overline{U}^{\perp}\oplus \overline{U}^{\perp},$$
$$̸$$
$$with \overline{U}^{\perp}= (0). Pick any isometry \frac{\tau}{U} of \overline{U}^{\perp}such that \det(\tau ) = -1, and extend it to an$$
isometry $h$ of $E$ whose restriction to  is the identity. If dim(U) $+$ dim(rad(U)) $=$ dim(E) $= n$, then $U = V^{\perp}\oplus W$ with $V =$ rad(U) and since $dim(\overline{U}) =$ dim(U) $+$ dim(rad(U)) $= n$, we have
$$E =\overline{U} = (V \oplus V' )^{\perp}\oplus W,$$
where $V \oplus$ V' $= Ar_{2r} = W^{\perp}$ is an Artinian space. Any isometry $h$ of $E$ which is the identity on $U$ and with det(h) $= -1$ is the identity on $W$, and thus it must map $W^{\perp} = Ar_{2r} = V \oplus$ V' into itself, and the restriction h' of $h$ to $Ar_{2r}$ has det(h') $= -1$. However, h' is the identity on $V =$ rad(U), a totally isotropic subspace of $Ar_{2r}$ of dimension $r$, and by Proposition 29.42, we have det(h') $= +1$, a contradiction. It can be shown that the center of $O(\phi$ ) is ${id, -id}$. For further properties of orthogonal groups, see Grove $[86]$, Jacobson $[101]$, Taylor $[180]$, and Artin $[6]$.
