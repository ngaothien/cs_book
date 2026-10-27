# Isometries Associated with Sesquilinear Forms


<!-- PAGE 1030 -->
If $\phi_{1}$  and $\phi_{2}$  are symmetric bilinear forms, then $f^{*l}  = f^{*r}$ . This also holds if $\phi$  is $\epsilon$ -Hermitian. Indeed, since
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),$$
we get
$$\overline{\epsilon \phi}_{2}\overline{(}\overline{f}\overline{(}\overline{x}\overline{)}\overline{, u}\overline{) =}\overline{\epsilon \phi}_{1}\overline{(}\overline{x, f}^{*r} \overline{(}\overline{u}\overline{))},$$
and since $\lambda  \mapsto \overline{\lambda}$ is an involution, we get
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*r} (u)).$$
Since we also have
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),$$
we obtain
$$\phi_{1} (x, f^{*r} (u)) = \phi_{1} (x, f^{*l} (u))for all x \in E_{1}, and all u \in E_{2},$$
and since $\phi_{1}$  is nondegenerate, we conclude that $f^{*l}  = f^{*r}$ . Whenever $f^{*l}  = f^{*r}$ , we use the simpler notation $f^{*}$ . If $f$ : $E_{1} \to E_{2}$ and $g: E_{1} \to E_{2}$ are two linear maps, we have the following properties:
$$(f + g)^{*l}= f^{*l}+ g^{*l}$$
$$id^{*l}= id$$
$$(\lambda f)^{*l}=\overline{\lambda f}^{*l},$$
and similarly for right adjoints. If $E_{3}$ is another space, $\phi_{3}$  is a sesquilinear form on $E_{3}$, and if $l_{\phi2}$ and $r_{\phi2}$ are bijective, then for any linear maps $f$ : $E_{1} \to E_{2}$ and $g: E_{2} \to E_{3}$, we have
$$(g \circ f)^{*l}= f^{*l}\circ g^{*l},$$
and similarly for right adjoints. Furthermore, if $E_{1} = E_{2} = E$ and $\phi$ : $E \times  E \to K$ is $\epsilon$ -Hermitian, for any linear map $f$ : $E \to E$ (recall that in this case $f^{*l}  = f^{*r}  = f^{*}$ ), we have
$$f^{**} =\overline{\epsilon \epsilon f.}$$

## 29.5 Isometries Associated with Sesquilinear Forms

The notion of adjoint is a good tool to investigate the notion of isometry between spaces equipped with sesquilinear forms. First, we define metric maps and isometries.

> **Definition 29.15.** If $(E_{1}, \phi_{1}$ ) and $(E_{2}, \phi_{2}$ ) are two pairs of spaces and sesquilinear maps $\phi_{1}$  : $E_{1} \times  E_{1} \to K$ and $\phi_{2}$  : $E_{2} \times  E_{2} \to K$, a metric map from $(E_{1}, \phi_{1}$ ) to $(E_{2}, \phi_{2}$ ) is a linear map $f$ : $E_{1} \to E_{2}$ such that
$$\phi_{1} (u, v) = \phi_{2} (f(u), f(v))for all u, v \in E_{1}.$$
We say that $\phi_{1}$  and $\phi_{2}$  are equivalent iff there is a metric map $f$ : $E_{1} \to E_{2}$ which is bijective. Such a metric map is called an isometry.

<!-- PAGE 1031 -->
The problem of classifying sesquilinear forms up to equivalence is an important but very difficult problem. Solving this problem depends intimately on properties of the field $K$, and a complete answer is only known in a few cases. The problem is easily solved for $K = \mathbb{R}, K = \mathbb{C}$. It is also solved for finite fields and for $K = \mathbb{Q}$ (the rationals), but the solution is surprisingly involved! It is hard to say anything interesting if $\phi_{1}$  is degenerate and if the linear map $f$ does not have adjoints. The next few propositions make use of natural conditions on $\phi_{1}$  that yield a useful criterion for being a metric map.

> **Proposition 29.16.** With the same assumptions as in Definition 29.14 (which imply that $\phi_{1}$  is nondegenerate), if $f$ : $E_{1} \to E_{2}$ is a bijective linear map, then we have
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))for all x, y \in E_{1} iff$$
$$f^{-1}= f^{*l}= f^{*r}.$$

*Proof.* We have
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))$$
iff
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y)) = \phi_{1} (x, f^{*l} (f(y))$$
iff
$$\phi_{1} (x, (id -f^{*l}\circ f)(y)) = 0for all x \in E_{1} and all y \in E_{2}.$$
Since $\phi_{1}$  is nondegenerate, we must have
$$f^{*l}\circ f = id,$$
which implies that $f^{-1} = f^{*l}$. Similarly,
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))$$
iff
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y)) = \phi_{1} (f^{*r} (f(x)), y)$$
iff
$$\phi_{1} ((id -f^{*r}\circ f)(x), y) = 0for all x \in E_{1} and all y \in E_{2}.$$
Since $\phi_{1}$  is nondegenerate, we must have
$$f^{*r}\circ f = id,$$
which implies that $f^{-1} = f^{*r}$. Therefore, $f^{-1} = f^{*l} = f^{*r}$. For the converse, do the computations in reverse. As a corollary, we get the following important proposition.

<!-- PAGE 1032 -->

> **Proposition 29.17.** If $\phi$ : $E \times  E \to K$ is a sesquilinear map, and if $l_{\phi}$ and $r_{\phi}$ are bijective, for every bijective linear map $f$ : $E \to E$, then we have
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E iff$$
$$f^{-1}= f^{*l}= f^{*r}.$$
We also have the following facts.

> **Proposition 29.18.** $(1)$ If $\phi$ : $E \times  E \to K$ is a sesquilinear map and if $l_{\phi}$ is injective, then for every linear map $f$ : $E \to E$, if
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E,(*)$$
then $f$ is injective.
$(2)$ If $E$ is finite-dimensional and if $\phi$  is nondegenerate, then the linear maps $f$ : $E \to E$ satisfying (*) form a group. The inverse of $f$ is given by $f^{-1} = f^{*}$.

*Proof.* $(1)$ If f(x) $= 0$, then
$$\phi (x, y) = \phi (f(x), f(y)) = \phi (0, f(y)) = 0for all y \in E.$$
Since $l_{\phi}$ is injective, we must have $x = 0$, and thus $f$ is injective.
$(2)$ If $E$ is finite-dimensional, since a linear map satisfying (*) is injective, it is a bijection. By Proposition 29.17, we have $f^{-1} = f^{*}$. We also have $\phi$ (f(x), f(y)) $= \phi ((f^{*} \circ$ f)(x), $y) = \phi (x, y) = \phi ((f \circ f^{*} )(x), y) = \phi (f^{*} (x), f^{*} (y))$, which shows that $f^{*}$ satisfies (*). If $\phi$ (f(x), f(y)) $= \phi (x, y)$ for all $x, y \in E$ and $\phi$ (g(x), g(y)) $= \phi (x, y)$ for all $x, y \in E$, then we have
$$\phi ((g \circ f)(x), (g \circ f)(y)) = \phi (f(x), f(y)) = \phi (x, y)for all x, y \in E.$$
Obviously, the identity map $id_{E}$ satisfies (*). Therefore, the set of linear maps satisfying (*) is a group. The above considerations motivate the following definition.

> **Definition 29.16.** Let $\phi$ : $E \times  E \to K$ be a sesquilinear map, and assume that $E$ is finite-dimensional and that $\phi$  is nondegenerate. A linear map $f$ : $E \to E$ is an isometry of $E$ (with respect to $\phi$ ) iff
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E.$$
The set of all isometries of $E$ is a group denoted by $Isom(\phi$ ).

<!-- PAGE 1033 -->
If $\phi$  is symmetric, then the group $Isom(\phi$ ) is denoted $O(\phi$ ) and called the orthogonal group of $\phi$ . If $\phi$  is alternating, then the group $Isom(\phi$ ) is denoted $Sp(\phi$ ) and called the symplectic group of $\phi$ . If $\phi$  is $\epsilon$ -Hermitian, then the group $Isom(\phi$ ) is denoted $U_{\epsilon}(\phi$ ) and called the $\epsilon$ -unitary group of $\phi$ . When $\epsilon  = 1$, we drop $\epsilon$  and just say unitary group. If $(e_{1}, \dots  , e_{n})$ is a basis of $E, \phi$  is the represented by the $n \times  n$ matrix $M$, and $f$ is represented by the $n \times  n$ matrix $A$, since $A^{-1} = A^{*l} = A^{*r} = M^{-1}A^{*}M$, then we find that $f \in Isom(\phi$ ) iff
$$A^{*}MA = M,$$
and $A^{-1}$ is given by $A^{-1} = M^{-1}A^{*}M$. More specifically, we define the following groups, using the matrices $I_{p,q}, J_{m,m}$ and $A_{m,m}$ defined at the end of Section 29.1.
$(1) K =\mathbb{R}$. We have
$$O(n) = {A \in M_{n}(\mathbb{R}) | A^{\top}A = I_{n}}$$
$$O(p, q) = {A \in M_{p+q}(\mathbb{R}) | A^{\top}I_{p,q}A = I_{p,q}}$$
$$Sp(2n,\mathbb{R}) = {A \in M_{2n}(\mathbb{R}) | A^{\top}J_{n,n}A = J_{n,n}}$$
$$SO(n) = {A \in M_{n}(\mathbb{R}) | A^{\top}A = I_{n}, \det(A) = 1}$$
$$SO(p, q) = {A \in M_{p+q}(\mathbb{R}) | A^{\top}I_{p,q}A = I_{p,q}, \det(A) = 1}.$$
The group O(n) is the orthogonal group, $Sp(2n,\mathbb{R})$ is the real symplectic group, and SO(n) is the special orthogonal group. We can define the group
$${A \in M_{2n}(\mathbb{R}) | A^{\top}A_{n,n}A = A_{n,n}},$$
but it is isomorphic to O(n, $n)$.
$(2) K =\mathbb{C}$. We have
$$U(n) = {A \in M_{n}(\mathbb{C}) | A^{*}A = I_{n}}$$
$$U(p, q) = {A \in M_{p+q}(\mathbb{C}) | A^{*}I_{p,q}A = I_{p,q}}$$
$$Sp(2n,\mathbb{C}) = {A \in M_{2n}(\mathbb{C}) | A^{\top}J_{n,n}A = J_{n,n}}$$
$$SU(n) = {A \in M_{n}(\mathbb{C}) | A^{*}A = I_{n}, \det(A) = 1}$$
$$SU(p, q) = {A \in M_{p+q}(\mathbb{C}) | A^{*}I_{p,q}A = I_{p,q}, \det(A) = 1}.$$
The group U(n) is the unitary group, $Sp(2n,\mathbb{C})$ is the complex symplectic group, and SU(n) is the special unitary group. It can be shown that if $A \in Sp(2n,\mathbb{R})$ or if $A \in Sp(2n,\mathbb{C})$, then det(A) $= 1$.
