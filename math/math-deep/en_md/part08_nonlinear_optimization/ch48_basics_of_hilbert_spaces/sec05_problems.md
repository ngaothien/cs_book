# Problems


<!-- PAGE 1701 -->
$\bullet$  Distance of a point to a subset, diameter. $\bullet$  Projection onto a closed and convex subset. $\bullet$  Orthogonal complement of a closed subspace. $\bullet$  Dual of a Hilbert space. $\bullet$  Bounded linear operator (or functional). $\bullet$  Riesz representation theorem. $\bullet$  Adjoint of a continuous linear map. $\bullet$  Farkas–Minkowski lemma.

## 48.5 Problems

Problem 48.1. Let $V$ be a Hilbert space. Prove that a subspace $W$ of $V$ is dense in $V$ if and only if there is no nonzero vector orthogonal to $W$.
Problem 48.2. Prove that the adjoint satisfies the following properties:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*}$$
$$(f \circ g)^{*}= g^{*}\circ f^{*}$$
$$f^{**} = f.$$
Problem 48.3. Prove that $\|f^{*} \circ f\| = \|f\|^{2}$.
Problem 48.4. Let $V$ be a (real) Hilbert space and let $C$ be a nonempty closed convex subset of $V$ . Define the map $h: V \to \mathbb{R} \cup {+\infty$ } by
$$h(u) = \sup\langle u, v\rangle .$$
$$v\in C$$
Prove that
$$C = \bigcap_{u\in V}  {v \in V | \langle u, v\rangle \le h(u)} = \bigcap_{u\in\Lambda C}  {v \in V | \langle u, v\rangle \le h(u)},$$
where $\Lambda_{C}  = {u \in V$ | h(u) $\neq  +\infty$ }. Describe $\Lambda_{C}$  when $C$ is also a subspace of $V$ .
Problem 48.5. Let $A$ be a real $m\times n$ matrix, and let $(u_{k})$ be a sequence of vectors $u_{k} \in \mathbb{R}^{n}$ such that $u_{k} \ge 0$. Prove that if the sequence $(Au_{k})$ converges, then there is some $u \in \mathbb{R}^{n}$ such that
$$Au = limAu_{k}andu \ge 0.$$
$$k\mapsto \infty$$

<!-- PAGE 1702 -->
Problem 48.6. Let $V$ be a real Hilbert space, $(a_{1}, \dots  , a_{m})$ a sequence of $m$ vectors in $V , b$ some vector in $V , (\alpha_{1} , \dots  , \alpha_{m}$ ) a sequence of $m$ real numbers, and $\beta$  some real number. Prove that the inclusion
$${w \in V | \langle a_{i}, w\rangle \ge \alpha_{i} , 1 \le i \le m} \subseteq {w \in V | \langle b, w\rangle \ge \beta }$$
holds if and only if there exist $\lambda_{1} , \dots  , \lambda_{m}  \in \mathbb{R}$ such that $\lambda_{i}  \ge 0$ for $i = 1, \dots  , m$ and
$$b = \sum_{i=1}^{m}  \lambda_{i} a_{i}$$
$$\beta  \le \sum_{i=1}^{m}  \lambda_{i} \alpha_{i} .$$
