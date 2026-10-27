# Torsion Modules over a PID; Primary Decomposition


<!-- PAGE 1291 -->
and
$$\phi (\psi (u)) = \phi \overline{(1} \otimes u)$$
$$= 1u$$
$$= u,$$
which shows that $\phi$  and $\psi$  are mutual inverses. We now develop the theory necessary to understand the structure of finitely generated modules over a PID.

## 35.4 Torsion Modules over a PID; The Primary

$$Decomposition$$
We begin by considering modules over a product ring obtained from a direct decomposition, as in Definition 32.6. In this section and the next, we closely follow Bourbaki $[26]$ (Chapter VII). Let $A$ be a commutative ring and let $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ be ideals in $A$ such that there is an isomorphism $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$. From Theorem 32.17 part $(b)$, there exist some elements $e_{1}, \dots  , e_{n}$ of $A$ such that
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A},$$
and $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$, for $i, j = 1, \dots  , n$. Given an A-module $M$ with $A \approx A/\mathfrak{b}_{1}\times \cdots \times A/\mathfrak{b}_{n}$, let $M_{i}$ be the subset of $M$ annihilated by $\mathfrak{b}_{i}$; that is,
$$M_{i} = {x \in M | bx = 0, for all b \in \mathfrak{b}_{i}}.$$
Because $\mathfrak{b}_{i}$ is an ideal, each $M_{i}$ is a submodule of $M$. Observe that if $\lambda , \mu  \in A, b \in \mathfrak{b}_{i}$, and if $\lambda$  - $\mu  = b$, then for any $x \in M_{i}$, since bx $= 0$,
$$\lambda x = (\mu  + b)x = \mu x + bx = \mu x,$$
so $M_{i}$ can be viewed as a $A/\mathfrak{b}_{i}-$ module.

> **Proposition 35.15.** Given a ring $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$ as above, the A-module $M$ is the direct sum
$$M = M_{1} \oplus \cdots  \oplus M_{n},$$
where $M_{i}$ is the submodule of $M$ annihilated by $\mathfrak{b}_{i}$.

<!-- PAGE 1292 -->

*Proof.* For $i = 1, \dots  , n$, let $p_{i}$ : $M \to M$ be the map given by
$$p_{i}(x) = e_{i}x,x \in M.$$
The map $p_{i}$ is clearly linear, and because of the properties satisfied by the $e_{i}s$, we have
$$p_{i}^{2} = p_{i}$$
$$p_{i}p_{j} = 0,i \neq  j$$
$$p_{1} + \cdots  + p_{n} = id.$$
This shows that the $p_{i}$ are projections, and by Proposition 6.8 (which also holds for modules), we have a direct sum
$$M = p_{1}(M) \oplus \cdots  \oplus p_{n}(M) = e_{1}M \oplus \cdots  \oplus e_{n}M.$$
It remains to show that $M_{i} = e_{i}M$. Since $(1$ - $e_{i})e_{i} = e_{i}$ - $e_{i}^{2} = e_{i}$ - $e_{i} = 0$, we see that $e_{i}M$ is annihilated by $\mathfrak{b}_{i} = (1$ - $e_{i})A$. Furthermore, for i̸ $= j$, for any $x \in M$, we have $(1$ - $e_{i})e_{j}x = (e_{j}$ - $e_{i}e_{j})x = e_{j}x$, so no nonzero element of $e_{j}M$ is annihilated by $1$ - $e_{i}$, and thus not annihilated by $\mathfrak{b}_{i}$. It follows that $e_{i}M = M_{i}$, as claimed.

> **Definition 35.8.** Given an A-module $M$, for any nonzero $\alpha  \in A$, let
$$M(\alpha ) = {x \in M | \alpha x = 0},$$
the submodule of $M$ annihilated by $\alpha$ . If $\alpha$  divides $\beta$ , then $M(\alpha$ ) $\subseteq M(\beta$ ), so we can define
$$M_{\alpha} = \bigcup_{n\ge1}  M(\alpha^{n} ) = {x \in M | (\exists n \ge 1)(\alpha^{n} x = 0)},$$
the submodule of $M$ consisting of all elements of $M$ annihilated by some power of $\alpha$ . If $N$ is any submodule of $M$, it is clear that
$$N_{\alpha} = M \cap M_{\alpha}.$$
Recall that in a PID, an irreducible element is also called a prime element.

> **Definition 35.9.** If $A$ is a PID and $p$ is a prime element in $A$, we say that a module $M$ is p-primary if $M = M_{p}$.

> **Proposition 35.16.** Let $M$ be module over a PID $A$. For every nonzero $\alpha  \in A$, if
$$\alpha  = up_{1}^{n1} \cdots  p_{r}^{nr}$$
is a factorization of $\alpha$  into prime factors (where $u$ is a unit), then the module $M(\alpha$ ) annihilated by $\alpha$  is the direct sum
$$M(\alpha ) = M(p_{1}^{n1} ) \oplus \cdots  \oplus M(p_{r}^{nr} ).$$
Furthermore, the projection from $M(\alpha$ ) onto $M(p_{i}^{ni}$ ) is of the form $x \mapsto \gamma_{i} x$, for some $\gamma_{i}  \in A$, and
$$M(p_{i}^{ni} ) = M(\alpha ) \cap M_{pi}.$$

<!-- PAGE 1293 -->

*Proof.* First observe that since $M(\alpha$ ) is annihilated by $\alpha$ , we can view $M(\alpha$ ) as a $A/(\alpha$ )- module. By the Chinese remainder theorem (Theorem 32.16) applied to the ideals $(up_{1}^{n1}$ ) $= (p_{1}^{n1}$ ), $(p_{2}^{n2}$ ), $\dots  , (p_{r}^{nr}$ ), we have an isomorphism
$$A/(\alpha ) \approx A/(p_{1}^{n1} ) \times  \cdots  \times  A/(p_{r}^{nr} ).$$
Since we also have isomorphisms
$$A/(p_{i}^{ni} ) \approx (A/(\alpha ))/((p_{i}^{ni} )/(\alpha )),$$
we can apply Proposition 35.15, and we get a direct sum
$$M(\alpha ) = N_{1} \oplus \cdots  \oplus N_{r},$$
where $N_{i}$ is the $A/(\alpha$ )-submodule of $M(\alpha$ ) annihilated by $(p_{i}^{ni} )/(\alpha$ ), and the projections onto the $N_{i}$ are of the form stated in the proposition. However, $N_{i}$ is just the A-module $M(p_{i}^{ni}$ ) annihilated by $p_{i}^{ni}$ , because every nonzero element of $(p_{i}^{ni} )/(\alpha$ ) is an equivalence class modulo $(\alpha$ ) of the form $\overline{ap}_{i}^{ni}$ for some nonzero $a \in A$, and by definition, $x \in N_{i}$ iff
$$0 =\overline{ap}_{i}^{ni} x = ap_{i}^{ni} x,for all a \in A -{0},$$
in particular for $a = 1$, which implies that $x \in M(p_{i}^{ni}$ ). The inclusion $M(p_{i}^{ni}$ ) $\subseteq M(\alpha$ ) $\cap M_{pi}$ is clear. Conversely, pick $x \in M(\alpha$ ) $\cap M_{pi}$, which means that $\alpha x = 0$ and $p_{i}^{s}x = 0$ for some $s \ge 1$. If $s < n_{i}$, we are done, so assume $s \ge n_{i}$. Since $p_{i}^{ni}$ is a gcd of $\alpha$  and $p_{i}^{s}$, by Bezout, we can write
$$p_{i}^{ni} = \lambda p_{i}^{s} + \mu \alpha$$
for some $\lambda , \mu  \in A$, and then $p_{i}^{ni} x = \lambda p_{i}^{s}x + \mu \alpha x = 0$, which shows that $x \in M(p_{i}^{ni}$ ), as desired. Here is an example of Proposition 35.16. Let $M = \mathbb{Z}/60\mathbb{Z}$, where $M$ is considered as $a \mathbb{Z}-module$. A element in $M$ is denoted by $\overline{x}$, where $x$ is an integer with $0 \le x \le 59$ . Let $\alpha  = 6$ and define
$$M(6) = {\overline{x} \in M | 6\overline{x}\overline{= 0}} = {\overline{0},\overline{10},\overline{20},\overline{30},\overline{40},\overline{50}}.$$
Since $6 = 2 \cdot  3$, Proposition 35.16 implies that M(6) $=$ M(2) $\oplus$ M(3), where
$$M(2) = {\overline{x} \in M | 2\overline{x}\overline{= 0}} = {\overline{0},\overline{30}}$$
$$M(3) = {\overline{x} \in M | 3\overline{x}\overline{= 0}} = {\overline{0},\overline{20},\overline{40}}.$$
Recall that if $M$ is a torsion module over a ring $A$ which is an integral domain, then every finite set of elements $x_{1}, \dots  , x_{n}$ in $M$ is annihilated by $a = a_{1} \cdots  a_{n}$, where each $a_{i}$ annihilates $x_{i}$. Since $A$ is a PID, we can pick a set $P$ of irreducible elements of $A$ such that every nonzero nonunit of $A$ has a unique factorization up to a unit. Then, we have the following structure theorem for torsion modules which holds even for modules that are not finitely generated.

<!-- PAGE 1294 -->

> **Theorem 35.17.** (Primary Decomposition Theorem) Let $M$ be a torsion-module over a PID. For every irreducible element $p \in P$, let $M_{p}$ be the submodule of $M$ annihilated by some power of $p$. Then, $M$ is the (possibly infinite) direct sum
$$M =MM_{p}.$$
$$p\in P$$

*Proof.* Since $M$ is a torsion-module, for every $x \in M$, there is some $\alpha  \in A$ such that $x \in M(\alpha$ ). By Proposition 35.16, if $\alpha  = up_{1}^{n1} \cdots  p_{r}^{nr}$ is a factorization of $\alpha$  into prime factors (where $u$ is a unit), then the module $M(\alpha$ ) is the direct sum
$$M(\alpha ) = M(p_{1}^{n1} ) \oplus \cdots  \oplus M(p_{r}^{nr} ).$$
This means that $x$ can be written as
$$x = \sum_{p\in P}  x_{p},x_{p} \in M_{p},$$
with only finitely many $x_{p}$ nonzero. If
$$\sum_{p\in P}  x_{p} = \sum_{p\in P}  y_{p}$$
for all $p \in P$, with only finitely many $x_{p}$ and $y_{p}$ nonzero, then $x_{p}$ and $y_{p}$ are annihilated by some common nonzero element $a \in A$, so $x_{p}, y_{p} \in$ M(a). By Proposition 35.16, we must have $x_{p} = y_{p}$ for all $p$, which proves that we have a direct sum. It is clear that if $p$ and p' are two irreducible elements such that $p =$ up' for some unit $u$, then $M_{p} = M_{p'}$. Therefore, $M_{p}$ only depends on the ideal $(p)$.

> **Definition 35.10.** Given a torsion-module $M$ over a PID, the modules $M_{p}$ associated with irreducible elements in $P$ are called the p-primary components of $M$. The p-primary components of a torsion module uniquely determine the module, as shown by the next proposition.

> **Proposition 35.18.** Two torsion modules $M$ and $N$ over a PID are isomorphic iff for every every irreducible element $p \in P$, the p-primary components $M_{p}$ and $N_{p}$ of $M$ and $N$ are isomorphic.

*Proof.* Let $f$ : $M \to N$ be an isomorphism. For any $p \in P$, we have $x \in M_{p}$ iff $p^{k}x = 0$ for some $k \ge 1$, so
$$0 = f(p^{k}x) = p^{k}f(x),$$
which shows that f(x) $\in N_{p}$. Therefore, $f$ restricts to a linear map $f$ | $M_{p}$ from $M_{p}$ to $N_{p}$. Since $f$ is an isomorphism, we also have a linear map $f^{-1}: M \to N$, and our previous

<!-- PAGE 1295 -->
reasoning shows that $f^{-1}$ restricts to a linear map $f^{-1}$ | $N_{p}$ from $N_{p}$ to $M_{p}$. But, $f$ | $M_{p}$ and $f^{-1}$ | $N_{p}$ are mutual inverses, so $M_{p}$ and $N_{p}$ are isomorphic. Conversely, if $M_{p} \approx N$  for all $p \in P$, by Theorem 35.17, we get an isomorphism between
$$M = \bigoplus_{p}  \in P M_{p} and N = \bigoplus^{p}  p\in P N_{p}.$$
In view of Proposition 35.18, the direct sum of Theorem 35.17 in terms of its p-primary components is called the canonical primary decomposition of $M$. If $M$ is a finitely generated torsion-module, then Theorem 35.17 takes the following form.

> **Theorem 35.19.** (Primary Decomposition Theorem for finitely generated torsion modules) Let $M$ be a finitely generated torsion-module over a PID $A$. If Ann(M) $= (a)$ and if $a = up_{1}^{n1} \cdots  p_{r}^{nr}$ is a factorization of a into prime factors, then $M$ is the finite direct sum
$$r$$
$$M =MM(p_{i}^{ni} ).$$
$$i=1$$
Furthermore, the projection of $M$ over $M(p_{i}^{ni}$ ) is of the form $x \mapsto \gamma_{i} x$, for some $\gamma_{i}  \in A$.

*Proof.* This is an immediate consequence of Proposition 35.16. Theorem 35.19 applies when $A =\mathbb{Z}$. In this case, $M$ is a finitely generated torsion abelian group, and the theorem says that such a group is the direct sum of a finite number of groups whose elements have order some power of a prime number $p$. In particular, consider the $\mathbb{Z}-module \mathbb{Z}/10\mathbb{Z}$ where
$$\mathbb{Z}/10\mathbb{Z} = {\overline{0},\overline{1},\overline{2},\overline{3},\overline{4},\overline{5},\overline{6},\overline{7},\overline{8},\overline{9}}.$$
Clearly $\mathbb{Z}/10\mathbb{Z}$ is generated by $\overline{1}$ and Ann $(\mathbb{Z}/10\mathbb{Z}) = 10$. Theorem 35.19 implies that
$$\mathbb{Z}/10\mathbb{Z} = M(2) \oplus M(5),$$
where
$$M(2) = {\overline{x} \in M | 2\overline{x}\overline{= 0}} = {\overline{0},\overline{5}}$$
$$M(5) = {\overline{x} \in M | 5\overline{x}\overline{= 0}} = {\overline{0},\overline{2},\overline{4},\overline{6},\overline{8}}.$$
Theorem 35.17 has several useful corollaries.

> **Proposition 35.20.** If $M$ is a torsion module over a PID, for every submodule $N$ of $M$, we have a direct sum
$$N =MN \cap M_{p}.$$
$$p\in P$$

*Proof.* It is easily verified that $N \cap M_{p}$ is the p-primary component of $N$.

<!-- PAGE 1296 -->

> **Proposition 35.21.** If $M$ is a torsion module over a PID, a submodule $N$ of $M$ is a direct factor of $M$ iff $N_{p}$ is a direct factor of $M_{p}$ for every irreducible element $p \in A$.

*Proof.* This is because if $N$ and N' are two submodules of $M$, we have $M = N \oplus$ N' iff, by Proposition 35.20, $M_{p} = N_{p} \oplus N_{p}'$  for every irreducible elements $p \in A$.

> **Definition 35.11.** An A-module $M$ is said to be semi-simple iff for every submodule $N$ of $M$, there is some submodule N' of $M$ such that $M = N \oplus$ N'.

> **Proposition 35.22.** Let $A$ be a PID which is not a field, and let $M$ be any A-module. Then $M$ is semi-simple iff it is a torsion module and if $M_{p} =$ M(p) for every irreducible element $p \in A$ (in other words, if $x \in M$ is annihilated by a power of $p$, then it is already annihilated by $p)$.

*Proof.* Assume that $M$ is semi-simple. Let $x \in M$ and pick any irreducible element $p \in A$. Then, the submodule pAx has a supplement $N$ such that
$$M = pAx \oplus N,$$
so we can write $x =$ pax $+ y$, for some $y \in N$ and some $a \in A$. But then,
$$y = (1 -pa)x,$$
and since $p$ is irreducible, $p$ is not a unit, so $1$ - pa $\neq  0$. Observe that
$$p(1 -ap)x = py \in pAx \cap N = (0).$$
Since p(1 - ap) $\neq  0, x$ is a torsion element, and thus $M$ is a torsion module. The above argument shows that
$$p(1 -ap)x = 0,$$
which implies that px $= ap^{2}x$, and by induction,
$$px = a^{n}p^{n+1}x,for all n \ge 1.$$
If we pick $x$ in $M_{p}$, then there is some $m \ge 1$ such that $p^{m}x = 0$, and we conclude that
$$px = 0.$$
Therefore, $M_{p} =$ M(p), as claimed. Conversely, assume that $M$ is a torsion-module and that $M_{p} =$ M(p) for every irreducible element $p \in A$. By Proposition 35.21, it is sufficient to prove that a module annihilated by a an irreducible element is semi-simple. This is because such a module is a vector space over the field $A/(p)$ (recall that in a PID, an ideal $(p)$ is maximal iff $p$ is irreducible), and in a vector space, every subspace has a supplement. Theorem 35.19 shows that a finitely generated torsion module is a direct sum of p-primary modules $M_{p}$. We can do better. In the next section we show that each primary module $M_{p}$ is the direct sum of cyclic modules of the form $A/(p^{n})$.
