# Duality and the Riesz Representation Theorem


<!-- PAGE 1694 -->
Therefore, the solutions of the original least-squares problem are precisely the solutions of the the so-called normal equations
$$A^{\top}Ax = A^{\top}b,$$
discovered by Gauss and Legendre around $1800$. We also proved that the normal equations always have a solution. Computationally, it is best not to solve the normal equations directly, and instead, to use methods such as the QR-decomposition (applied to $A)$ or the SVD-decomposition (in the form of the pseudo-inverse). We will come back to this point later on. Here is another important corollary of Proposition 48.7.

> **Corollary 48.8.** For any continuous nonnull linear map $h: E \to \mathbb{C}$, the null space
$$H = \mathrm{Ker} h = {u \in E | h(u) = 0} = h^{-1}(0)$$
is a closed hyperplane $H$, and thus, $H^{\perp}$ is a subspace of dimension one such that $E = H\oplus H^{\perp}$. The above suggests defining the dual space of $E$ as the set of all continuous maps $h: E \to \mathbb{C}$.
Remark: If $h: E \to \mathbb{C}$ is a linear map which is not continuous, then it can be shown that the hyperplane $H =$ Ker $h$ is dense in $E$! Thus, $H^{\perp}$ is reduced to the trivial subspace
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$
${0}$. This goes against our intuition of what a hyperplane in (or ) is, and warns us not to trust our “physical” intuition too much when dealing with infinite dimensions. As a consequence, the map $\flat$ : $E \to E^{*}$ introduced in Section 14.2 (see just after Definition 48.4 below) is not surjective, since the linear forms of the form $u \mapsto \langle u, v\rangle$ (for some fixed vector $v \in E)$ are continuous (the inner product is continuous).

## 48.2 Duality and the Riesz Representation Theorem

We now show that by redefining the dual space of a Hilbert space as the set of continuous linear forms on $E$ we recover Theorem 14.6.

> **Definition 48.4.** Given a Hilbert space $E$, we define the dual space E' of $E$ as the vector
$$\mathbb{C}$$
space of all continuous linear forms $h: E \to$ . Maps in E' are also called bounded linear operators, bounded linear functionals, or simply operators or functionals. As in Section 14.2, for all $u, v \in E$, we define the maps $\phi_{u}^{l}$  : $E \to \mathbb{C}$ and $\phi_{v}^{r}$  : $E \to \mathbb{C}$ such that
$$\phi_{u}^{l} (v) =\overline{\langle}\overline{u, v}\overline{\rangle},$$
and
$$\phi_{v}^{r} (u) = \langle u, v\rangle .$$

<!-- PAGE 1695 -->
In fact, $\phi_{u}^{l}  = \phi_{u}^{r}$ , and because the inner product $\langle$ -, $-\rangle$ is continuous, it is obvious that $\phi_{v}^{r}$ is continuous and linear, so that $\phi_{v}^{r}  \in$ E'. To simplify notation, we write $\phi_{v}$  instead of $\phi_{v}^{r}$ . Theorem 14.6 is generalized to Hilbert spaces as follows.

> **Proposition 48.9.** (Riesz representation theorem) Let $E$ be a Hilbert space. Then the map $\flat$ : $E \to$ E' defined such that
$$\flat (v) = \phi_{v} ,$$
is semilinear, continuous, and bijective. Furthermore, for any continuous linear map $\psi  \in$ E', if $u \in E$ is the unique vector such that
$$\psi (v) = \langle v, u\rangle for all v \in E,$$
then we have $\|\psi \| = \|u\|$, where
$$|$$
$$|



$$
$$\|\psi \|= \sup \frac{\psi (v)}{\|v\|} v \in E, v \neq  0.$$

*Proof.* The proof is basically identical to the proof of Theorem 14.6, except that a different argument is required for the surjectivity of $\flat$ : $E \to$ E', since $E$ may not be finite dimensional. For any nonnull linear operator $h \in$ E', the hyperplane $H =$ Ker $h = h^{-1}(0)$ is a closed subspace of $E$, and by Proposition 48.7, $H^{\perp}$ is a subspace of dimension one such that $E = H \oplus H^{\perp}$. Then picking any nonnull vector $w \in H^{\perp}$, observe that $H$ is also the kernel of the linear operator $\phi_{w}$ , with
$$\phi_{w} (u) = \langle u, w\rangle ,$$
and thus, since any two nonzero linear forms defining the same hyperplane must be proportional, there is some nonzero scalar $\lambda  \in \mathbb{C}$ such that $h = \lambda \phi_{w}$ . But then, $h = \overline{\phi}_{\lambda w}$, proving that $\flat$ : $E \to$ E' is surjective. By the Cauchy–Schwarz inequality we have
$$|\psi (v)| = |\langle v, u\rangle | \le \|v\|\|u\|,$$
so by definition of $\|\psi \|$ we get
$$\|\psi \|\le \|u\|.$$
Obviously $\psi  = 0$ iff $u = 0$ so assume $u \neq  0$. We have
$$\|u\|^{2}= \langle u, u\rangle = \psi (u) \le \|\psi \|\|u\|,$$
which yields $\|u\|\le \|\psi \|$, and therefore $\|\psi \| = \|u\|$, as claimed. Proposition 48.9 is known as the Riesz representation theorem or “Little Riesz Theorem.” It shows that the inner product on a Hilbert space induces a natural semilinear isomorphism between $E$ and its dual E' (equivalently, a linear isomorphism between $\overline{E}$ and E'). This isomorphism is an isometry (it is preserves the norm).

<!-- PAGE 1696 -->
Remark: Many books on quantum mechanics use the so-called Dirac notation to denote objects in the Hilbert space $E$ and operators in its dual space E'. In the Dirac notation, an element of $E$ is denoted as $|x\rangle$ , and an element of E' is denoted as $\langle$ t|. The scalar product is denoted as $\langle$ t| $\cdot  |x\rangle$ . This uses the isomorphism between $E$ and E', except that the inner product is assumed to be semi-linear on the left rather than on the right. Proposition 48.9 allows us to define the adjoint of a linear map, as in the Hermitian case (see Proposition 14.8). Actually, we can prove a slightly more general result which is used in optimization theory. If $\phi$ : $E\times E \to \mathbb{C}$ is a sesquilinear map on a normed vector space $(E, \|\|)$, then Proposition 37.59 is immediately adapted to prove that $\phi$  is continuous iff there is some constant $k \ge 0$ such that
$$|\phi (u, v)| \le k \|u\|\|v\|for all u, v \in E.$$
Thus we define $\|\phi \|$ as in Definition 37.42 by
$$\|\phi \|= \sup {|\phi (x, y)| | \|x\|\le 1, \|y\|\le 1, x, y \in E} .$$

> **Proposition 48.10.** Given a Hilbert space $E$, for every continuous sesquilinear map $\phi$ : $E \times E \to \mathbb{C}$, there is a unique continuous linear map $f_{\phi}$ : $E \to E$, such that
$$\phi (u, v) = \langle u, f_{\phi}(v)\rangle for all u, v \in E.$$
We also have $\|f_{\phi}\| = \|\phi \|$. If $\phi$  is Hermitian, then $f_{\phi}$ is self-adjoint, that is
$$\langle u, f_{\phi}(v)\rangle = \langle f_{\phi}(u), v\rangle for all u, v \in E.$$

*Proof.* The proof is adapted from Rudin $[146]$ (Theorem 12.8). To define the function $f_{\phi}$, we proceed as follows. For any fixed $v \in E$, define the linear map $\phi_{v}$  by
$$\phi_{v} (u) = \phi (u, v)for all u \in E.$$
Since $\phi$  is continuous, $\phi_{v}$  is continuous. So by Proposition 48.9, there is a unique vector in $E$ that we denote $f_{\phi}(v)$ such that
$$\phi_{v} (u) = \langle u, f_{\phi}(v)\rangle for all u \in E,$$
and $\|f_{\phi}(v)\| = \|\phi_{v} \|$. Let us check that the map $v \mapsto f_{\phi}(v)$ is linear. We have
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})\phi  is additive$$
$$= \langle u, f_{\phi}(v_{1})\rangle + \langle u, f_{\phi}(v_{2})\rangle by definition of f_{\phi}$$
$$= \langle u, f_{\phi}(v_{1}) + f_{\phi}(v_{2})\rangle \langle -, -\rangle is additive$$

<!-- PAGE 1697 -->
for all $u \in E$, and since $f_{\phi}(v_{1}+v_{2})$ is the unique vector such that $\phi (u, v_{1}+v_{2}) = \langle u, f_{\phi}(v_{1}+v_{2})\rangle$ for all $u \in E$, we must have
$$f_{\phi}(v_{1} + v_{2}) = f_{\phi}(v_{1}) + f_{\phi}(v_{2}).$$
For any $\lambda  \in \mathbb{C}$ we have
$$\phi (u, \lambda v) =\overline{\lambda \phi}(u, v)\phi  is sesquilinear$$
$$=\overline{\lambda}\langle u, f_{\phi}(v)\rangle by definition of f_{\phi}$$
$$= \langle u, \lambda f_{\phi}(v)\rangle \langle -, -\rangle is sesquilinear$$
for all $u \in E$, and since $f_{\phi}(\lambda v)$ is the unique vector such that $\phi (u, \lambda v) = \langle u, f_{\phi}(\lambda v)\rangle$ for all $u \in E$, we must have
$$f_{\phi}(\lambda v) = \lambda f_{\phi}(v).$$
Therefore $f_{\phi}$ is linear. Then by definition of $\|\phi \|$, we have
$$|\phi_{v} (u)| = |\phi (u, v)| \le \|\phi \|\|u\|\|v\|,$$
which shows that $\|\phi_{v} \|\le \|\phi \|\|v\|$. Since $\|f_{\phi}(v)\| = \|\phi_{v} \|$, we have
$$\|f_{\phi}(v)\|\le \|\phi \|\|v\|,$$
which shows that $f_{\phi}$ is continuous and that $\|f_{\phi}\|\le \|\phi \|$. But by the Cauchy–Schwarz inequality we also have
$$|\phi (u, v)| = |\langle u, f_{\phi}(v)\rangle | \le \|u\|\|f_{\phi}(v)\|\le \|u\|\|f_{\phi}\|\|v\|,$$
so $\|\phi \|\le \|f_{\phi}\|$, and thus
$$\|f_{\phi}\|= \|\phi \|.$$
If $\phi$  is Hermitian, $\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{),}$ so
$$\langle f_{\phi}(u), v\rangle =\overline{\langle}\overline{v, f}_{\phi}\overline{(}\overline{u}\overline{)}\overline{\rangle}=\overline{\phi}\overline{(}\overline{v, u}\overline{) =} \phi (u, v) = \langle u, f_{\phi}(v)\rangle ,$$
which shows that $f_{\phi}$ is self-adjoint.

> **Proposition 48.11.** Given a Hilbert space $E$, for every continuous linear map $f$ : $E \to E$, there is a unique continuous linear map $f^{*}$ : $E \to E$, such that
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle for all u, v \in E,$$
and we have $\|f^{*} \| = \|f\|$. The map $f^{*}$ is called the adjoint of $f$.

<!-- PAGE 1698 -->

*Proof.* The proof is adapted from Rudin $[146]$ (Section 12.9). By the Cauchy–Schwarz inequality, since
$$|\langle x, y\rangle | \le \|x\|\|y\|,$$
we see that the sesquilinear map $(x, y) \mapsto \langle x, y\rangle$ on $E \times  E$ is continuous. Let $\phi$ : $E \times  E \to \mathbb{C}$ be the sesquilinear map given by
$$\phi (u, v) = \langle f(u), v\rangle for all u, v \in E.$$
Since $f$ is continuous and the inner product $\langle$ -, $-\rangle$ is continuous, this is a continuous map. By Proposition 48.10, there is a unique linear map $f^{*}$ : $E \to E$ such that
$$\langle f(u), v\rangle = \phi (u, v) = \langle u, f^{*} (v)\rangle for all u, v \in E,$$
with $\|f^{*} \| = \|\phi \|$. We can also prove that $\|\phi \| = \|f\|$. First, by definition of $\|\phi \|$ we have
$$\|\phi \|= \sup {|\phi (x, y)| | \|x\|\le 1, \|y\|\le 1}$$
$$= \sup {|\langle f(x), y\rangle | | \|x\|\le 1, \|y\|\le 1}$$
$$\le \sup {\|f(x)\|\|y\|| \|x\|\le 1, \|y\|\le 1}$$
$$\le \sup {\|f(x)\|| \|x\|\le 1}$$
$$= \|f\|.$$
In the other direction we have
$$\|f(x)\|^{2}= \langle f(x), f(x)\rangle = \phi (x, f(x)) \le \|\phi \|\|x\|\|f(x)\|,$$
and if f(x) $\neq  0$ we get $\|f(x)\|\le \|\phi \|\|x\|$. This inequality holds trivially if f(x) $= 0$, so we conclude that $\|f\|\le \|\phi \|$. Therefore we have
$$\|\phi \|= \|f\|,$$
as claimed, and consequently $\|f^{*} \| = \|\phi \| = \|f\|$. It is easy to show that the adjoint satisfies the following properties:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*}$$
$$(f \circ g)^{*}= g^{*}\circ f^{*}$$
$$f^{**} = f.$$
One can also show that $\|f^{*} \circ f\| = \|f\|^{2}$ (see Rudin $[146]$, Section 12.9). As in the Hermitian case, given two Hilbert spaces $E$ and $F$, the above results can be adapted to show that for any linear map $f$ : $E \to F$, there is a unique linear map $f^{*}$ : $F \to E$ such that
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1}$$
for all $u \in E$ and all $v \in F$. The linear map $f^{*}$ is also called the adjoint of $f$.
