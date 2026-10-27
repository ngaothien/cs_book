# The Cartan–Dieudonné Theorem, Hermitian Case


<!-- PAGE 997 -->
Chapter $28$ Isometries of Hermitian Spaces

## 28.1 The Cartan–Dieudonn´e Theorem,

$$Hermitian Case$$
The Cartan-Dieudonn´e theorem can be generalized (Theorem 28.2), but this requires allowing new types of hyperplane reflections that we call Hermitian reflections. After doing so, every isometry in U(n) can always be written as a composition of at most $n$ Hermitian reflections (for $n \ge 2)$. Better yet, every rotation in SU(n) can be expressed as the composition of at most 2n - $2$ (standard) hyperplane reflections! This implies that every unitary transformation in U(n) is the composition of at most 2n-1 isometries, with at most one Hermitian reflection, the other isometries being (standard) hyperplane reflections. The crucial Proposition 13.2 is false as is, and needs to be amended. The QR-decomposition of arbitrary complex matrices in terms of Householder matrices can also be generalized, using a trick. In order to generalize the Cartan–Dieudonn´e theorem and the QR-decomposition in terms of Householder transformations, we need to introduce new kinds of hyperplane reflections. This is not really surprising, since in the Hermitian case, there are improper isometries whose determinant can be any unit complex number. Hyperplane reflections are generalized as follows.

> **Definition 28.1.** Let $E$ be a Hermitian space of finite dimension. For any hyperplane $H$, for any nonnull vector $w$ orthogonal to $H$, so that $E = H \oplus G$, where $G =\mathbb{C} w$, a Hermitian reflection about $H$ of angle $\theta$  is a linear map of the form $\rho_{H, \theta}$  : $E \to E$, defined such that
$$\rho_{H, \theta} (u) = p_{H}(u) + e^{i\theta}p_{G}(u),$$
$$̸$$
for any unit complex number $e^{i\theta} = 1$ (i.e. $\theta$ ̸ $= k2\pi$ ). For any nonzero vector $w \in E$, we denote by $\rho_{w,\theta}$  the Hermitian reflection given by $\rho_{H,\theta}$ , where $H$ is the hyperplane orthogonal to $w$.
$$997$$

<!-- PAGE 998 -->
Since $u = p_{H}(u) + p_{G}(u)$, the Hermitian reflection $\rho_{w, \theta}$  is also expressed as
$$\rho_{w, \theta} (u) = u + (e^{i\theta}-1)p_{G}(u),$$
or as
$$1)  \cdot$$
$$\rho_{w, \theta} (u) = u + (e^{i\theta}- \frac{(u w)}{\|w\|^{2}} w.$$
Note that the case of a standard hyperplane reflection is obtained when $e^{i\theta} = -1$, i.e., $\theta  = \pi$ . We leave as an easy exercise to check that $\rho_{w, \theta}$  is indeed an isometry, and that the inverse of $\rho_{w, \theta}$  is $\rho_{w,-\theta}$ . If we pick an orthonormal basis $(e_{1}, \dots  , e_{n})$ such that $(e_{1}, \dots  , e_{n-1})$ is an orthonormal basis of $H$, the matrix of $\rho_{w, \theta}$  is
$$\begin{pmatrix} I_{n-1} & 0 \\ 0 & e^{i\theta} \end{pmatrix}$$
We now come to the main surprise. Given any two distinct vectors $u$ and $v$ such that $\|u\| = \|v\|$, there isn’t always a hyperplane reflection mapping $u$ to $v$, but this can be done using two Hermitian reflections!

> **Proposition 28.1.** Let $E$ be any nontrivial Hermitian space.
$(1)$ For any two vectors $u, v \in E$ such that $u \neq  v$ and $\|u\| = \|v\|$, if $u \cdot  v = e^{i\theta}|u \cdot$  v|, then the (usual) reflection $s$ about the hyperplane orthogonal to the vector $v$ - $e^{-i\theta}u$ is such that s(u) $= e^{i\theta}v$.
$(2)$ For any nonnull vector $v \in E$, for any unit complex number $e^{i\theta} \neq  1$, there is a Hermitian reflection $\rho_{v,\theta}$  such that
$$\rho_{v,\theta} (v) = e^{i\theta}v.$$
As a consequence, for $u$ and $v$ as in $(1)$, we have $\rho_{v,-\theta}  \circ$ s(u) $= v$.

*Proof.* $(1)$ Consider the (usual) reflection about the hyperplane orthogonal to $w = v -e^{-i\theta}u$. We have
$$2  \cdot  -$$
$$s(u) = u - \frac{(u (ve^{-i\theta}u))}{\|v -e^{-i\theta}u\|^{2}} (v -e^{-i\theta}u).$$
We need to compute
$$-2u \cdot  (v -e^{-i\theta}u)and(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u).$$
Since $u \cdot  v = e^{i\theta}|u \cdot$  v|, we have
$$e^{-i\theta}u \cdot  v = |u \cdot  v|ande^{i\theta}v \cdot  u = |u \cdot  v|.$$
Using the above and the fact that $\|u\| = \|v\|$, we get
$$-2u \cdot  (v -e^{-i\theta}u) = 2e^{i\theta}\|u\|^{2}-2u \cdot  v,$$
$$= 2e^{i\theta}(\|u\|^{2}-|u \cdot  v|),$$

<!-- PAGE 999 -->
and
$$(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u) = \|v\|^{2}+ \|u\|^{2}-e^{-i\theta}u \cdot  v -e^{i\theta}v \cdot  u,$$
$$= 2(\|u\|^{2}-|u \cdot  v|),$$
and thus,
$$2  \cdot  -$$
$$- \frac{(u (ve^{-i\theta}u))}{\|(v -e^{-i\theta}u)\|^{2}} (v -e^{-i\theta}u) = e^{i\theta}(v -e^{-i\theta}u).$$
But then,
$$s(u) = u + e^{i\theta}(v -e^{-i\theta}u) = u + e^{i\theta}v -u = e^{i\theta}v,$$
and s(u) $= e^{i\theta}v$, as claimed.
$(2)$ This part is easier. Consider the Hermitian reflection
$$1)  \cdot$$
$$\rho_{v,\theta} (u) = u + (e^{i\theta}- \frac{(u v)}{\|v\|^{2}} v.$$
We have
$$1)  \cdot$$
$$\rho_{v,\theta} (v) = v + (e^{i\theta}- \frac{(v v)}{\|v\|^{2}} v,$$
$$= v + (e^{i\theta}-1)v,$$
$$= e^{i\theta}v.$$
Thus, $\rho_{v,\theta} (v) = e^{i\theta}v$. Since $\rho_{v,\theta}$  is linear, changing the argument $v$ to $e^{i\theta}v$, we get
$$\rho_{v,-\theta} (e^{i\theta}v) = v,$$
and thus, $\rho_{v,-\theta}  \circ$ s(u) $= v$.
Remarks:
$(1)$ If we use the vector $v + e^{-i\theta}u$ instead of $v$ - $e^{-i\theta}u$, we get s(u) $= -e^{i\theta}v$.
$(2)$ Certain authors, such as Kincaid and Cheney $[105]$ and Ciarlet $[41]$, use the vector $u + e^{i\theta}v$ instead of our vector $v + e^{-i\theta}u$. The effect of this choice is that they also get s(u) $= -e^{i\theta}v$.
$(3)$ If $v = \|u\|e_{1}$, where $e_{1}$ is a basis vector, $u \cdot  e_{1} = a_{1}$, where $a_{1}$ is just the coefficient of $u$ over the basis vector $e_{1}$. Then, since $u \cdot  e_{1} = e^{i\theta}|a_{1}|$, the choice of the plus sign in the vector $\|u\|e_{1} + e^{-i\theta}u$ has the effect that the coefficient of this vector over $e_{1}$ is $\|u\| + |a_{1}|$, and no cancellations takes place, which is preferable for numerical stability (we need to divide by the square norm of this vector).

<!-- PAGE 1000 -->
The last part of Proposition 28.1 shows that the Cartan–Dieudonn´e is salvaged, since we can send $u$ to $v$ by a sequence of two Hermitian reflections when $u \neq  v$ and $\|u\| = \|v\|$, and since the inverse of a Hermitian reflection is a Hermitian reflection. Actually, because we are over the complex field, a linear map always have (complex) eigenvalues, and we can get a slightly improved result.

> **Theorem 28.2.** Let $E$ be a Hermitian space of dimension $n \ge 1$. Every isometry $f \in$ U(E) is the composition $f = \rho_{n}  \circ \rho_{n-1}  \circ \cdots  \circ \rho_{1}$  of $n$ isometries $\rho_{j}$ , where each $\rho_{j}$  is either the identity or a Hermitian reflection (possibly a standard hyperplane reflection). When $n \ge 2$, the identity is the composition of any hyperplane reflection with itself.

*Proof.* We prove by induction on $n$ that there is an orthonormal basis of eigenvectors $(u_{1}, \dots  , u_{n})$ of $f$ such that
$$f(u_{j}) = e^{i\theta j}u_{j},$$
where $e^{i\theta j}$ is an eigenvalue associated with $u_{j}$, for all $j, 1 \le j \le n$. When $n = 1$, every isometry $f \in$ U(E) is either the identity or a Hermitian reflection $\rho_{\theta}$ , since for any nonnull vector $u$, we have f(u) $= e^{i\theta}u$ for some $\theta$ . We let $u_{1}$ be any nonnull unit vector. Let us now consider the case where $n \ge 2$. Since $\mathbb{C}$ is algebraically closed, the characteristic polynomial det(f - $\lambda$ id) of $f$ has $n$ complex roots which must be the form $e^{i\theta}$, since they have absolute value $1$. Pick any such eigenvalue $e^{i\theta1}$, and pick any eigenvector $u_{1} \neq  0$ of $f$ for $e^{i\theta1}$ of unit length. If $F =\mathbb{C} u_{1}$ is the subspace spanned by $u_{1}$, we have f(F) $= F$, since $f(u_{1}) = e^{i\theta1}u_{1}$. Since f(F) $= F$ and $f$ is an isometry, it is easy to see that $f(F^{\perp}$ ) $\subseteq F^{\perp}$ , and by Proposition 14.13, we have $E = F \oplus F^{\perp}$ . Furthermore, it is obvious that the restriction of $f$ to $F^{\perp}$ is unitary. Since dim $(F^{\perp}$ ) $= n$ - $1$, we can apply the induction hypothesis to $F^{\perp}$ , and we get an orthonormal basis of eigenvectors $(u_{2}, \dots  , u_{n})$ for $F^{\perp}$ such that
$$f(u_{j}) = e^{i\theta j}u_{j},$$
where $e^{i\theta j}$ is an eigenvalue associated with $u_{j}$, for all $j, 2 \le j \le n$ Since $E = F \oplus F^{\perp}$ and $F = \mathbb{C} u_{1}$, the claim is proved. But then, if $\rho_{j}$  is the Hermitian reflection about the hyperplane $H_{j}$ orthogonal to $u_{j}$ and of angle $\theta_{j}$ , it is obvious that
$$f = \rho_{\theta n}  \circ \cdots  \circ \rho_{\theta1} .$$
When $n \ge 2$, we have id $= s \circ s$ for every reflection $s$.
Remarks:
$(1)$ Any isometry $f \in$ U(n) can be express as $f = \rho_{\theta} \circ g$, where $g \in$ SU(n) is a rotation, and $\rho_{\theta}$  is a Hermitian reflection. Indeed, by the above theorem, with respect to the basis $(u_{1}, \dots  , u_{n})$, det(f) $= e^{i(\theta1+\cdot \cdot \cdot+\theta n)}$, and letting $\theta  = \theta_{1}  +\cdots +\theta_{n}$  and $\rho_{\theta}$  be the Hermitian

<!-- PAGE 1001 -->
reflection about the hyperplane orthogonal to $u_{1}$ and of angle $\theta$ , since $\rho_{\theta}  \circ \rho_{-\theta}  =$ id, we have
$$f = (\rho_{\theta}  \circ \rho_{-\theta} ) \circ f = \rho_{\theta}  \circ (\rho_{-\theta}  \circ f).$$
Letting $g = \rho_{-\theta}  \circ f$, it is obvious that det(g) $= 1$. As a consequence, there is a bijection between $S^{1} \times$  SU(n) and U(n), where $S^{1}$ is the unit circle (which corresponds to the group of complex numbers $e^{i\theta}$ of unit length). In fact, it is a homeomorphism.
$(2)$ We abandoned the style of proof used in theorem 27.1, because in the Hermitian case, eigenvalues and eigenvectors always exist, and the proof is simpler that way (in the real case, an isometry may not have any real eigenvalues!). The sacrifice is that the theorem yields no information on the number of (standard) hyperplane reflections. We shall rectify this situation shortly. We will now reveal the beautiful trick (found in Mneimn´e and Testard $[131])$ that allows us to prove that every rotation in SU(n) is the composition of at most 2n - $2$ (standard) hyperplane reflections. For what follows, it is more convenient to denote a standard reflection about the hyperplane $H$ as $h_{u}$ (it is trivial that these do not depend on the choice of $u$ in $H^{\perp})$. Then, given any two distinct orthogonal vectors $u, v$ such that $\|u\| = \|v\|$, consider the composition $\rho_{v,-\theta}  \circ \rho_{u, \theta}$ . The trick is that this composition can be expressed as two standard hyperplane reflections! This wonderful fact is proved in the next Proposition.

> **Proposition 28.3.** Let $E$ be a nontrivial Hermitian space. For any two distinct orthogonal vectors $u, v$ such that $\|u\| = \|v\|$, we have
$$\rho_{v,-\theta}  \circ \rho_{u, \theta}  = h_{v-u} \circ h_{v-e-i\theta u} = h_{u+v} \circ h_{u+ei\theta v}.$$

*Proof.* Since $u$ and $v$ are orthogonal, each one is in the hyperplane orthogonal to the other, and thus,
$$\rho_{u, \theta} (u) = e^{i\theta}u,$$
$$\rho_{u, \theta} (v) = v,$$
$$\rho_{v,-\theta} (u) = u,$$
$$\rho_{v,-\theta} (v) = e^{-i\theta}v,$$
$$h_{v-u}(u) = v,$$
$$h_{v-u}(v) = u,$$
$$h_{v-e-i\theta u}(u) = e^{i\theta}v,$$
$$h_{v-e-i\theta u}(v) = e^{-i\theta}u.$$
Consequently, using linearity,
$$\rho_{v,-\theta}  \circ \rho_{u, \theta} (u) = e^{i\theta}u,$$
$$\rho_{v,-\theta}  \circ \rho_{u, \theta} (v) = e^{-i\theta}v,$$
$$h_{v-u} \circ h_{v-e-i\theta u}(u) = e^{i\theta}u,$$
$$h_{v-u} \circ h_{v-e-i\theta u}(v) = e^{-i\theta}v,$$

<!-- PAGE 1002 -->
and since both $\rho_{v,-\theta}  \circ \rho_{u, \theta}$  and $h_{v-u}\circ h_{v-e-i\theta u}$ are the identity on the orthogonal complement of ${u, v}$, they are equal. Since we also have
$$h_{u+v}(u) = -v,$$
$$h_{u+v}(v) = -u,$$
$$h_{u+ei\theta v}(u) = -e^{i\theta}v,$$
$$h_{u+ei\theta v}(v) = -e^{-i\theta}u,$$
it is immediately verified that
$$h_{v-u} \circ h_{v-e-i\theta u} = h_{u+v} \circ h_{u+ei\theta v}.$$
We will use Proposition 28.3 as follows.

> **Proposition 28.4.** Let $E$ be a nontrivial Hermitian space, and let $(u_{1}, \dots  , u_{n})$ be some orthonormal basis for $E$. For any $\theta_{1} , \dots  , \theta_{n}$  such that $\theta_{1}  + \cdots  + \theta_{n}  = 0$, if $f \in$ U(n) is the isometry defined such that
$$f(u_{j}) = e^{i\theta j}u_{j},$$
for all $j, 1 \le j \le n$, then $f$ is a rotation $(f \in$ SU(n)), and
$$f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1}$$
$$= \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$$
$$= h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1}$$
$$= h_{un-1+un} \circ h_{un-1+ei(\theta1+\cdot \cdot \cdot+\theta n-1)un} \circ \cdots  \circ h_{u1+u2} \circ h_{u1+ei\theta1u2}.$$

*Proof.* It is obvious from the definitions that
$$f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1} ,$$
and since the determinant of $f$ is
$$D(f) = e^{i\theta1}\cdots  e^{i\theta n}= e^{i(\theta1+\cdot \cdot \cdot+\theta n)}$$
and $\theta_{1}  + \cdots  + \theta_{n}  = 0$, we have D(f) $= e^{0} = 1$, and $f$ is a rotation. Letting $f_{k} = \rho_{uk,-(\theta1+\cdot \cdot \cdot+\theta k-1)}  \circ \rho_{uk-1, \theta1+\cdot \cdot \cdot+\theta k-1}  \circ \cdots  \circ \rho_{u3,-(\theta1+\theta2)}  \circ \rho_{u2, \theta1+\theta2}  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$ , we prove by induction on $k, 2 \le k \le n$, that
$$e^{i\theta j}u_{j}if 1 \le j \le k -1,$$
$$$$
$$$$
$$f_{k}(u_{j}) =e^{-i(\theta1+\cdot \cdot \cdot+\theta k-1)}u_{k}if j = k, and$$
$$u_{j}if k + 1 \le j \le n.$$
$$$$

<!-- PAGE 1003 -->
The base case was treated in Proposition 28.3. Now, the proof of Proposition 28.3 also showed that
$$\rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k} (u_{k}) = e^{i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k},$$
$$\rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k} (u_{k+1}) = e^{-i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k+1},$$
and thus, using the induction hypothesis for $k (2 \le k \le n$ - $1)$, we have $f_{k+1}(u_{j}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{j}) = e^{i\theta j}u_{j}, 1 \le j \le k$ - $1, f_{k+1}(u_{k}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{k}) = e^{i(\theta1+\cdot \cdot \cdot+\theta k)}e^{-i(\theta1+\cdot \cdot \cdot+\theta k-1)}u_{k} = e^{i\theta k}u_{k}, f_{k+1}(u_{k+1}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{k+1}) = e^{-i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k+1}, f_{k+1}(u_{j}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{j}) = u_{j}, k + 1 \le j \le n$, which proves the induction step. As a summary, we proved that
$$($$
$$e^{i\theta j}u_{j}if 1 \le j \le n -1,$$
$$f_{n}(u_{j}) =$$
$$e^{-i(\theta1+\cdot \cdot \cdot+\theta n-1)}u_{n}when j = n,$$
but since $\theta_{1}  +\cdots +\theta_{n}  = 0$, we have $\theta_{n}  = -(\theta_{1}  +\cdots +\theta_{n-1}$ ), and the last expression is in fact
$$f_{n}(u_{n}) = e^{i\theta n}u_{n}.$$
Therefore, we proved that $f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1}  = \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$ , and using Proposition 28.3, we also have
$$f = \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$$
$$= h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1}$$
$$= h_{un-1+un} \circ h_{un-1+ei(\theta1+\cdot \cdot \cdot+\theta n-1)un} \circ \cdots  \circ h_{u1+u2} \circ h_{u1+ei\theta1u2},$$
which completes the proof. We finally get our improved version of the Cartan–Dieudonn´e theorem.

> **Theorem 28.5.** Let $E$ be a Hermitian space of dimension $n \ge 1$. Every rotation $f \in$ SU(E) different from the identity is the composition of at most 2n-2 standard hyperplane reflections. Every isometry $f \in$ U(E) different from the identity is the composition of at most 2n - $1$ isometries, all standard hyperplane reflections, except for possibly one Hermitian reflection. When $n \ge 2$, the identity is the composition of any reflection with itself.

<!-- PAGE 1004 -->

*Proof.* By Theorem 28.2, $f \in$ SU(n) can be written as a composition
$$\rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1} ,$$
where $(u_{1}, \dots  , u_{n})$ is an orthonormal basis of eigenvectors. Since $f$ is a rotation, det(f) $= 1$, and this implies that $\theta_{1}  + \cdots  + \theta_{n}  = 0$. By Proposition 28.4,
$$f = h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1},$$
a composition of 2n - $2$ hyperplane reflections. In general, if $f \in$ U(n), by the remark after Theorem 28.2, $f$ can be written as $f = \rho_{\theta}  \circ g$, where $g \in$ SU(n) is a rotation, and $\rho_{\theta}$  is a Hermitian reflection. We conclude by applying what we just proved to $g$. As a corollary of Theorem 28.5, the following interesting result can be shown (this is not hard, do it!). First, recall that a linear map $f$ : $E \to E$ is self-adjoint (or Hermitian) iff $f = f^{*}$ . Then, the subgroup of U(n) generated by the Hermitian isometries is equal to the group
$$SU(n)^{\pm}= {f \in U(n) | \det(f) = \pm 1}.$$
Equivalently, $SU(n)^{\pm}$ is equal to the subgroup of U(n) generated by the hyperplane reflections. This problem had been left open by Dieudonn´e in $[49]$. Evidently, it was settled since the publication of the third edition of the book $[49]$. Inspection of the proof of Proposition 27.4 reveals that this Proposition also holds for Hermitian spaces. Thus, when $n \ge 3$, the composition of any two hyperplane reflections is equal to the composition of two flips. As a consequence, a version of Theorem 27.5 holds for rotations in a Hermitian space of dimension at least $3$.

> **Theorem 28.6.** Let $E$ be a Hermitan space of dimension $n \ge 3$. Every rotation $f \in$ SU(E) is the composition of an even number of flips $f = f_{2k}\circ \cdots \circ f_{1}$, where $k \le$ n-1. Furthermore, if $u \neq  0$ is invariant under $f$ (i.e. $u \in$ Ker $(f$ - id)), we can pick the last flip $f_{2k}$ such that $u \in F_{2k}^{\perp}$ , where $F_{2k}$ is the subspace of dimension $n$ - $2$ determining $f_{2k}$.

*Proof.* It is identical to that of Theorem 27.5, except that it uses Theorem 28.5 instead of Theorem 27.1. The second part of the Proposition also holds, because if u̸ $= 0$ is an eigenvector of $f$ for $1$, then $u$ is one of the vectors in the orthonormal basis of eigenvectors used in 28.2. The details are left as an exercise. We now show that the QR-decomposition in terms of (complex) Householder matrices holds for complex matrices. We need the version of Proposition 28.1 and a trick at the end of the argument, but the proof is basically unchanged.

<!-- PAGE 1005 -->

> **Proposition 28.7.** Let $E$ be a nontrivial Hermitian space of dimension $n$. Given any orthonormal basis $(e_{1}, \dots  , e_{n})$, for any $n$-tuple of vectors $(v_{1}, \dots  , v_{n})$, there is a sequence of $n$ - $1$ isometries $h_{1}, \dots  , h_{n-1}$, such that $h_{i}$ is a hyperplane reflection or the identity, and if $(r_{1}, \dots  , r_{n})$ are the vectors given by
$$r_{j} = h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})1 \le j \le n,$$
then every $r_{j}$ is a linear combination of the vectors $(e_{1}, \dots  , e_{j}), (1 \le j \le n)$. Equivalently, the matrix $R$ whose columns are the components of the $r_{j}$ over the basis $(e_{1}, \dots  , e_{n})$ is an upper triangular matrix. Furthermore, if we allow one more isometry $h_{n}$ of the form
$$h_{n} = \rho_{en, \phi n}  \circ \cdots  \circ \rho_{e1,\phi1}$$
after $h_{1}, \dots  , h_{n-1}$, we can ensure that the diagonal entries of $R$ are nonnegative.

*Proof.* The proof is very similar to the proof of Proposition 13.3, but it needs to be modified a little bit since Proposition 28.1 is weaker than Proposition 13.2. We explain how to modify the induction step, leaving the base case and the rest of the proof as an exercise. As in the proof of Proposition 13.3, the vectors $(e_{1}, \dots  , e_{k})$ form a basis for the subspace denoted as $U_{k}'$ , the vectors $(e_{k+1}, \dots  , e_{n})$ form a basis for the subspace denoted as $U_{k}''$ , the subspaces $U_{k}'$  and $U_{k}''$ are orthogonal, and $E = U_{k}' \oplus U_{k}''$ . Let
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}).$$
We can write
$$u_{k+1} = u_{k+1}' + u_{k+1}'',$$
where $u_{k+1}' \in U_{k}'$ and $u_{k+1}'' \in U_{k}''$ . Let
$$r_{k+1,k+1} =

$u_{k+1}''$

$,ande^{i\theta k+1}|u_{k+1}'' \cdot  e_{k+1}| = u_{k+1}'' \cdot  e_{k+1}.$$$ If $u_{k+1}'' = e^{i\theta k+1}r_{k+1,k+1} e_{k+1}$, we let $h_{k+1} =$ id. Otherwise, by Proposition 28.1, there is a unique hyperplane reflection $h_{k+1}$ such that
$$h_{k+1}(u_{k+1}'') = e^{i\theta k+1}r_{k+1,k+1} e_{k+1},$$
where $h_{k+1}$ is the reflection about the hyperplane $H_{k+1}$ orthogonal to the vector
$$w_{k+1} = r_{k+1,k+1} e_{k+1} -e^{-i\theta k+1}u_{k+1}''.$$
At the end of the induction, we have a triangular matrix $R$, but the diagonal entries $e^{i\theta j}r_{j, j}$ of $R$ may be complex. Letting
$$h_{n+1} = \rho_{en,-\theta n}  \circ \cdots  \circ \rho_{e1,-\theta1} ,$$
we observe that the diagonal entries of the matrix of vectors
$$r_{j}' = h_{n+1} \circ h_{n} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})$$
is triangular with nonnegative entries.
