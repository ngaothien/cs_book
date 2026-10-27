# Ideals, PID's, and Greatest Common Divisors


<!-- PAGE 1076 -->

## 30.4 Ideals, PID’s, and Greatest Common Divisors

First, we introduce the fundamental concept of an ideal.

> **Definition 30.4.** Given a ring $A$, an ideal of $A$ is any nonempty subset $\mathfrak{I}$ of $A$ satisfying the following two properties:
(ID1) If a, $b \in \mathfrak{I}$, then $b$ - $a \in \mathfrak{I}$.
(ID2) If $a \in \mathfrak{I}$, then ax $\in \mathfrak{I}$ for every $x \in A$. An ideal $\mathfrak{I}$ is a principal ideal if there is some $a \in \mathfrak{I}$, called a generator, such that
$$\mathfrak{I} = {ax | x \in A}.$$
The equality $\mathfrak{I} = {ax$ | $x \in A}$ is also written as $\mathfrak{I} =$ aA or as $\mathfrak{I} = (a)$. The ideal $\mathfrak{I} = (0) = {0}$ is called the null ideal (or zero ideal). An ideal $\mathfrak{I}$ is a maximal ideal if $\mathfrak{I} \neq  A$ and for every ideal $\mathfrak{J} \neq  A$, if $\mathfrak{I} \subseteq \mathfrak{J}$, then $\mathfrak{J} = \mathfrak{I}$. An ideal $\mathfrak{I}$ is a prime ideal if $\mathfrak{I} \neq  A$ and if ab $\in \mathfrak{I}$, then $a \in \mathfrak{I}$ or $b \in \mathfrak{I}$, for all a, $b \in A. Equivalently,\mathfrak{I}$ is a prime ideal $if\mathfrak{I} \neq  A$ and if a, $b \in A -\mathfrak{I}$, then ab $\in A -\mathfrak{I}$, for all a, $b \in A$. In other words, $A$ - $\mathfrak{I}$ is closed under multiplication and $1 \in A$ - $\mathfrak{I}$. Note that $if\mathfrak{I}$ is an ideal, $then\mathfrak{I} = A$ iff1 $\in \mathfrak{I}$. Since by definition, an $ideal\mathfrak{I}$ is nonempty, there is some $a \in \mathfrak{I}$, and by (ID1) we get $0 = a$ - $a \in \mathfrak{I}$. Then, for every $a \in \mathfrak{I}$, since $0 \in \mathfrak{I}$, by (ID1) we get $-a \in \mathfrak{I}$. Thus, an ideal is an additive subgroup of $A$. Because of (ID2), an ideal is also a subring. Observe that if $A$ is a field, then $A$ only has two ideals, namely, the trivial ideal $(0)$ and $A$ itself. Indeed, if $\mathfrak{I} \neq  (0)$, because every nonnull element has an inverse, then $1 \in \mathfrak{I}$, and thus, $\mathfrak{I} = A$.

> **Definition 30.5.** Given a ring $A$, for any two elements a, $b \in A$ we say that $b$ is a multiple of a and that a divides $b$ if $b =$ ac for some $c \in A$; this is usually denoted by a | $b$. Note that the principal ideal (a) is the set of all multiples of a, and that a divides $b$ iff $b$ is a multiple of a iff $b \in$ (a) iff(b) $\subseteq$ (a). Note that every $a \in A$ divides $0$. However, it is customary to say that a is a zero divisor iff ac $= 0$ for some $c \neq  0$. With this convention, $0$ is a zero divisor unless $A = {0}$ (the trivial ring), and $A$ is an integral domain iff0 is the only zero divisor in $A$. Given a, $b \in A$ with a, $b \neq  0$, if $(a) = (b)$ then there exist $c, d \in A$ such that $a =$ bc and $b =$ ad. From this, we get $a =$ adc and $b =$ bcd, that is, a(1 -dc) $= 0$ and b(1 -cd) $= 0$. If $A$ is an integral domain, we get dc $= 1$ and cd $= 1$, that is, $c$ is invertible with inverse $d$. Thus, when $A$ is an integral domain, we have $b =$ ad, with $d$ invertible. The converse is obvious, if $b =$ ad with $d$ invertible, then $(a) = (b)$. It is worth recording this fact as the following proposition.

<!-- PAGE 1077 -->

> **Proposition 30.5.** If $A$ is an integral domain, for any a, $b \in A$ with a, b̸ $= 0$, we have
$(a) = (b)$ iff there exists some invertible $d \in A$ such that $b =$ ad. An invertible element $u \in A$ is also called a unit. Given two ideals $\mathfrak{I}$ and $\mathfrak{J}$, their sum
$$\mathfrak{I} +\mathfrak{J} = {a + b | a \in \mathfrak{I}, b \in \mathfrak{J}}$$
is clearly an ideal. Given any nonempty subset $J$ of $A$, the set
$${a_{1}x_{1} + \cdots  + a_{n}x_{n} | x_{1}, \dots  , x_{n} \in A, a_{1}, \dots  , a_{n} \in J, n \ge 1}$$
is easily seen to be an ideal, and in fact, it is the smallest ideal containing $J$. It is usually denoted by $(J)$. Ideals play a very important role in the study of rings. They tend to show up everywhere. For example, they arise naturally from homomorphisms.

> **Proposition 30.6.** Given any ring homomorphism $h: A \to B$, the kernel Ker $h = {a \in A$ | h(a) $= 0}$ of $h$ is an ideal.

*Proof.* Given a, $b \in A$, we have a, $b \in$ Ker $h$ iff h(a) $=$ h(b) $= 0$, and since $h$ is a homomorphism, we get
$$h(b -a) = h(b) -h(a) = 0,$$
and
$$h(ax) = h(a)h(x) = 0$$
for all $x \in A$, which shows that Ker $h$ is an ideal. There is a sort of converse property. Given a ring $A$ and an ideal $\mathfrak{I} \subseteq A$, we can define the quotient ring $A/\mathfrak{I}$, and there is a surjective homomorphism $\pi$ : $A \to A/\mathfrak{I}$ whose kernel is precisely $\mathfrak{I}$.

> **Proposition 30.7.** Given any ring $A$ and any ideal $\mathfrak{I} \subseteq A$, the equivalence relation $\equiv_{I}$ defined by $a \equiv_{I}  b$ iff $b$ - $a \in \mathfrak{I}$ is a congruence, which means that if $a_{1} \equiv_{I}  b_{1}$ and $a_{2} \equiv_{I}  b_{2}$, then $1. a_{1} + a_{2} \equiv_{I}  b_{1} + b_{2}$, and $2. a_{1}a_{2} \equiv_{I}  b_{1}b_{2}$. Then, the set $A/\mathfrak{I}$ of equivalence classes modulo $\mathfrak{I}$ is a ring under the operations
$$[a] + [b]=[a + b]$$
$$[a][b]=[ab].$$
The map $\pi$ : $A \to A/\mathfrak{I}$ such that $\pi (a) = [a]$ is a surjective homomorphism whose kernel is precisely $\mathfrak{I}$.

<!-- PAGE 1078 -->

*Proof.* Everything is straightforward. For example, if $a_{1} \equiv_{I}  b_{1}$ and $a_{2} \equiv_{I}  b_{2}$, then $b_{1} -a_{1} \in \mathfrak{I}$ and $b_{2}$ - $a_{2} \in \mathfrak{I}$. Since $\mathfrak{I}$ is an ideal, we get
$$(b_{1} -a_{1})b_{2} = b_{1}b_{2} -a_{1}b_{2} \in \mathfrak{I}$$
and
$$(b_{2} -a_{2})a_{1} = a_{1}b_{2} -a_{1}a_{2} \in \mathfrak{I}.$$
Since $\mathfrak{I}$ is an ideal, and thus, an additive group, we get
$$b_{1}b_{2} -a_{1}a_{2} \in \mathfrak{I},$$
i.e., $a_{1}a_{2} \equiv_{I}  b_{1}b_{2}$. The equality Ker $\pi  =\mathfrak{I}$ holds because $\mathfrak{I}$ is an ideal.

> **Example 30.1.** $1$. In the ring $\mathbb{Z}$, for every $p \in \mathbb{Z}$, the subroup $p\mathbb{Z}$ is an ideal, and $\mathbb{Z}/p\mathbb{Z}$ is a ring, the ring of residues modulo $p$. This ring is a field iff $p$ is a prime number. $2$. The quotient of the polynomial ring $\mathbb{R}[X]$ by a prime ideal $\mathfrak{I}$ is an integral domain. $3$. The quotient of the polynomial $ring\mathbb{R}[X]$ by a maximal $ideal\mathfrak{I}$ is a field. For example, if $\mathfrak{I} = (X^{2} + 1)$, the principal ideal generated by $X^{2} + 1$ (which is indeed a maximal
$$\mathbb{R}  \sim \mathbb{C}$$
ideal since $X^{2} + 1$ has no real roots), then $[X]/(X^{2} + 1) =$ . The following proposition yields a characterization of prime ideals and maximal ideals in terms of quotients.

> **Proposition 30.8.** Given a ring $A$, for any ideal $\mathfrak{I} \subseteq A$, the following properties hold.
$(1)$ The ideal $\mathfrak{I}$ is a prime ideal iff $A/\mathfrak{I}$ is an integral domain.
$(2)$ The ideal $\mathfrak{I}$ is a maximal ideal iff $A/\mathfrak{I}$ is a field.

*Proof.* $(1)$ Assume $that\mathfrak{I}$ is a prime ideal. $Since\mathfrak{I}$ is $prime,\mathfrak{I} \neq  A$, and thus, $A/\mathfrak{I}$ is not the trivial ring $(0)$. If [a][b] $= 0$, since [a][b] $=$ [ab], we have ab $\in \mathfrak{I}$, and since $\mathfrak{I}$ is prime, then either $a \in \mathfrak{I}$ or $b \in \mathfrak{I}$, so that either $[a] = 0$ or $[b] = 0$. Thus, $A/\mathfrak{I}$ is an integral domain. Conversely, assume that $A/\mathfrak{I}$ is an integral domain. Since $A/\mathfrak{I}$ is not the trivial ring, $\mathfrak{I} \neq  A$. Assume that ab $\in \mathfrak{I}$. Then, we have
$$\pi (ab) = \pi (a)\pi (b) = 0,$$
which implies that either $\pi (a) = 0$ or $\pi (b) = 0$, since $A/\mathfrak{I}$ is an integral domain (where $\pi$ : $A \to A/\mathfrak{I}$ is the quotient map). Thus, either $a \in \mathfrak{I}$ or $b \in \mathfrak{I}$, and $\mathfrak{I}$ is a prime ideal.

<!-- PAGE 1079 -->
$(2)$ Assume that $\mathfrak{I}$ is a maximal ideal. As in $(1), A/\mathfrak{I}$ is not the trivial ring $(0)$. Let $[a] \neq  0$ in $A/\mathfrak{I}$. We need to prove that [a] has a multiplicative inverse. Since $[a] \neq  0$, we have $a \in / \mathfrak{I}$. Let $\mathfrak{I}_{a}$ be the ideal generated by $\mathfrak{I}$ and a. We have
$$\mathfrak{I} \subseteq \mathfrak{I}_{a}and\mathfrak{I} \neq \mathfrak{I}_{a},$$
since $a \in / \mathfrak{I}$, and since $\mathfrak{I}$ is maximal, this implies that
$$\mathfrak{I}_{a} = A.$$
However, we know that
$$\mathfrak{I}_{a} = {ax + h | x \in A, h \in \mathfrak{I}},$$
and thus, there is some $x \in A$ so that
$$ax + h = 1,$$
which proves that [a][x] $= [1]$, as desired. Conversely, assume that $A/\mathfrak{I}$ is a field. Again, since $A/\mathfrak{I}$ is not the trivial ring, $\mathfrak{I} \neq  A$. Let $\mathfrak{J}$ be any proper ideal such that $\mathfrak{I} \subseteq \mathfrak{J}$, and assume that $\mathfrak{I} \neq  \mathfrak{J}$. Thus, there is some $j \in \mathfrak{J}$ - $\mathfrak{I}$, and since Ker $\pi  = \mathfrak{I}$, we have $\pi (j) \neq  0$. Since $A/\mathfrak{I}$ is a field and $\pi$  is surjective, there is some $k \in A$ so that $\pi (j)\pi (k) = 1$, which implies that
$$jk -1 = i$$
for some $i \in \mathfrak{I}$, and since $\mathfrak{I} \subset \mathfrak{J}$ and $\mathfrak{J}$ is an ideal, it follows that $1 =$ jk - $i \in \mathfrak{J}$, showing that $\mathfrak{J} = A$, a contradiction. Therefore, $\mathfrak{I} =\mathfrak{J}$, and $\mathfrak{I}$ is a maximal ideal. As a corollary, we obtain the following useful result. It emphasizes the importance of maximal ideals.

> **Corollary 30.9.** Given any ring $A$, every maximal ideal $\mathfrak{I}$ in $A$ is a prime ideal.

*Proof.* If $\mathfrak{I}$ is a maximal ideal, then, by Proposition 30.8, the quotient ring $A/\mathfrak{I}$ is a field. However, a field is an integral domain, and by Proposition 30.8 $(again),\mathfrak{I}$ is a prime ideal. Observe that a ring $A$ is an integral domain iff(0) is a prime ideal. This is an example of a prime ideal which is not a maximal ideal, as immediately seen in $A =\mathbb{Z}$, where $(p)$ is a maximal ideal for every prime number $p$.  $A$ less obvious example of a prime ideal which is not a maximal ideal is the ideal $(X)$ in the ring of polynomials $\mathbb{Z}[X]$. Indeed, $(X, 2)$ is also a prime ideal, but $(X)$ is properly contained in $(X, 2)$. The ideal $(X)$ is the set of all polynomials of the form XQ(X) for any Q(X) $\in \mathbb{Z}[X]$, in other words the set of all polynomials $in\mathbb{Z}[X]$ with constant term equal to $0$, and the ideal $(X, 2)$ is the set of all polynomials of the form
$$XQ_{1}(X) + 2Q_{2}(X),Q_{1}(X), Q_{2}(X) \in \mathbb{Z}[X],$$

<!-- PAGE 1080 -->
which is just the set of all polynomials in $\mathbb{Z}[X]$ whose constant term is of the form 2c for some $c \in \mathbb{Z}$. The ideal $(X)$ is indeed properly contained in the ideal $(X, 2)$. If P(X)Q(X) $\in (X, 2)$, let a be the constant term in P(X) and let $b$ be the constant term in Q(X). Since P(X)Q(X) $\in (X, 2)$, we must have ab $=$ 2c for some $c \in \mathbb{Z}$, and since $2$ is prime, either a is divisible by $2$ or $b$ is divisible by $2$. It follows that either P(X) $\in (X, 2)$ or Q(X) $\in (X, 2)$, which shows that $(X, 2)$ is a prime ideal.

> **Definition 30.6.** An integral domain in which every ideal is a principal ideal is called a principal ring or principal ideal domain, for short, a PID. The ring $\mathbb{Z}$ is a PID. This is a consequence of the existence of a (Euclidean) division algorithm. As we shall see next, when $K$ is a field, the ring K[X] is also a principal ring.  However, when $n \ge 2$, the ring $K[X_{1}, \dots  , X_{n}]$ is not principal. For example, in the ring K[X, $Y$ ], the ideal $(X, Y$ ) generated by $X$ and $Y$ is not principal. First, since $(X, Y$ ) is the set of all polynomials of the form $Xq_{1} + Y q_{2}$, where $q_{1}, q_{2} \in$ K[X, $Y$ ], except when $Xq_{1} + Y q_{2} = 0$, we have $deg(Xq_{1} + Y q_{2}) \ge 1$. Thus, $1 \in / (X, Y$ ). Now if there was some $p \in$ K[X, $Y$ ] such that $(X, Y$ ) $= (p)$, since $1 \in / (X, Y$ ), we must have deg(p) $\ge 1$. But we would also have $X = pq_{1}$ and $Y = pq_{2}$, for some $q_{1}, q_{2} \in$ K[X, $Y$ ]. Since deg(X) $=$ deg(Y ) $= 1$, this is impossible. Even though K[X, $Y$ ] is not a principal ring, a suitable version of unique factorization in terms of irreducible factors holds. The ring K[X, $Y$ ] (and more generally $K[X_{1}, \dots  , X_{n}])$ is what is called a unique factorization domain, for short, UFD, or a factorial ring. From this point until Definition 30.11, we consider polynomials in one variable over a field $K$.
Remark: Although we already proved part $(1)$ of Proposition 30.10 in a more general situation above, we reprove it in the special case of polynomials. This may offend the purists, but most readers will probably not mind.

> **Proposition 30.10.** Let $K$ be a field. The following properties hold:
$(1)$ For any two nonzero polynomials $f, g \in$ K[X], $(f) = (g)$ iff there is some $\lambda  \neq  0$ in $K$ such that $g = \lambda f$.
$(2)$ For every nonnull ideal $\mathfrak{I}$ in K[X], there is a unique monic polynomial $f \in$ K[X] such that $\mathfrak{I} = (f)$.

*Proof.* $(1)$ If $(f) = (g)$, there are some nonzero polynomials $q_{1}, q_{2} \in$ K[X] such that $g = fq_{1}$ and $f = gq_{2}$. Thus, we have $f = fq_{1}q_{2}$, which implies f(1 - $q_{1}q_{2}) = 0$. Since $K$ is a field, by Proposition 30.1, K[X] has no zero divisor, and since we assumed $f \neq  0$, we must have $q_{1}q_{2} = 1$. However, if either $q_{1}$ or $q_{2}$ is not a constant, by Proposition 30.1 again, $deg(q_{1}q_{2}) = deg(q_{1}) + deg(q_{2}) \ge 1$, contradicting $q_{1}q_{2} = 1$, since deg(1) $= 0$. Thus, both $q_{1}, q_{2} \in K -{0}$, and $(1)$ holds with $\lambda  = q_{1}$. In the other direction, it is obvious that $g = \lambda f$ implies that $(f) = (g)$.

<!-- PAGE 1081 -->
$(2)$ Since we are assuming $that\mathfrak{I}$ is not the null ideal, there is some polynomial of smallest degree in $\mathfrak{I}$, and since $K$ is a field, by suitable multiplication by a scalar, we can make sure that this polynomial is monic. Thus, let $f$ be a monic polynomial of smallest degree in $\mathfrak{I}$. By (ID2), it is clear that $(f) \subseteq \mathfrak{I}$. Now, let $g \in \mathfrak{I}$. Using the Euclidean algorithm, there exist unique $q, r \in$ K[X] such that
$$g = qf + randdeg(r) < deg(f).$$
If r̸ $= 0$, there is some $\lambda$ ̸ $= 0$ in $K$ such that $\lambda r$ is a monic polynomial, and since $\lambda r = \lambda g$ - $\lambda$ qf, with $f, g \in \mathfrak{I}$, by (ID1) and (ID2), we have $\lambda r \in \mathfrak{I}$, where $deg(\lambda r) <$ deg(f) and $\lambda r$ is a monic polynomial, contradicting the minimality of the degree of $f$. Thus, $r = 0$, and $g \in (f)$. The uniqueness of the monic polynomial $f$ follows from $(1)$. Proposition 30.10 shows that K[X] is a principal ring when $K$ is a field. We now investigate the existence of a greatest common divisor (gcd) for two nonzero polynomials. Given any two nonzero polynomials $f, g \in$ K[X], recall that $f$ divides $g$ if $g =$ fq for some $q \in$ K[X].

> **Definition 30.7.** Given any two nonzero polynomials $f, g \in$ K[X], a polynomial $d \in$ K[X] is a greatest common divisor of $f$ and $g$ (for short, a gcd of $f$ and $g)$ if $d$ divides $f$ and $g$ and whenever $h \in$ K[X] divides $f$ and $g$, then $h$ divides $d$. We say that $f$ and $g$ are relatively prime if $1$ is a gcd of $f$ and $g$. Note that $f$ and $g$ are relatively prime iff all of their gcd’s are constants (scalars in $K)$, or equivalently, if $f, g$ have no divisor $q$ of degree deg(q) $\ge 1$.  In particular, note that $f$ and $g$ are relatively prime when $f$ is a nonzero constant polynomial (a scalar $\lambda  \neq  0$ in $K)$ and $g$ is any nonzero polynomial. We can characterize gcd’s of polynomials as follows.

> **Proposition 30.11.** Let $K$ be a field and let $f, g \in$ K[X] be any two nonzero polynomials. For every polynomial $d \in$ K[X], the following properties are equivalent:
$(1)$ The polynomial $d$ is a gcd of $f$ and $g$.
$(2)$ The polynomial $d$ divides $f$ and $g$ and there exist $u, v \in$ K[X] such that
$$d = uf + vg.$$
$(3)$ The ideals $(f), (g)$, and $(d)$ satisfy the equation
$$(d) = (f) + (g).$$
In addition, $d \neq  0$, and $d$ is unique up to multiplication by a nonzero scalar in $K$.

<!-- PAGE 1082 -->

*Proof.* Given any two nonzero polynomials $u, v \in$ K[X], observe that $u$ divides $v$ iff(v) $\subseteq (u)$. Now, $(2)$ can be restated as $(f) \subseteq (d), (g) \subseteq (d)$, and $d \in (f) + (g)$, which is equivalent to
$(d) = (f) + (g)$, namely $(3)$. If $(2)$ holds, since $d =$ uf $+$ vg, whenever $h \in$ K[X] divides $f$ and $g$, then $h$ divides $d$, and $d$ is a gcd of $f$ and $g$. Assume that $d$ is a gcd of $f$ and $g$. Then, since $d$ divides $f$ and $d$ divides $g$, we have
$(f) \subseteq (d)$ and $(g) \subseteq (d)$, and thus $(f) + (g) \subseteq (d)$, and $(f) + (g)$ is nonempty since $f$ and $g$ are nonzero. By Proposition 30.10, there exists a monic polynomial $d_{1} \in$ K[X] such that $(d_{1}) = (f) + (g)$. Then, $d_{1}$ divides both $f$ and $g$, and since $d$ is a gcd of $f$ and $g$, then $d_{1}$ divides $d$, which shows that $(d) \subseteq (d_{1}) = (f) + (g)$. Consequently, $(f) + (g) = (d)$, and $(3)$ holds. Since $(d) = (f) + (g)$ and $f$ and $g$ are nonzero, the last part of the proposition is obvious. As a consequence of Proposition 30.11, two nonzero polynomials $f, g \in$ K[X] are relatively prime iff there exist $u, v \in$ K[X] such that
$$uf + vg = 1.$$
The identity
$$d = uf + vg$$
of part $(2)$ of Proposition 30.11 is often called the Bezout identity. We derive more useful consequences of Proposition 30.11.

> **Proposition 30.12.** Let $K$ be a field and let $f, g \in$ K[X] be any two nonzero polynomials. For every gcd $d \in$ K[X] of $f$ and $g$, the following properties hold:
$(1)$ For every nonzero polynomial $q \in$ K[X], the polynomial dq is a gcd of fq and gq.
$(2)$ For every nonzero polynomial $q \in$ K[X], if $q$ divides $f$ and $g$, then $d/q$ is a gcd of $f/q$ and $g/q$.

*Proof.* $(1)$ By Proposition 30.11 $(2), d$ divides $f$ and $g$, and there exist $u, v \in$ K[X], such that
$$d = uf + vg.$$
Then, dq divides fq and gq, and
$$dq = ufq + vgq.$$
By Proposition 30.11 $(2)$, dq is a gcd of fq and gq. The proof of $(2)$ is similar. The following proposition is used often.

<!-- PAGE 1083 -->

> **Proposition 30.13.** (Euclid’s proposition) Let $K$ be a field and let $f, g, h \in$ K[X] be any nonzero polynomials. If $f$ divides gh and $f$ is relatively prime to $g$, then $f$ divides $h$.

*Proof.* From Proposition 30.11, $f$ and $g$ are relatively prime iff there exist some polynomials $u, v \in$ K[X] such that
$$uf + vg = 1.$$
Then, we have
$$ufh + vgh = h,$$
and since $f$ divides gh, it divides both ufh and vgh, and so, $f$ divides $h$.

> **Proposition 30.14.** Let $K$ be a field and let $f, g_{1}, \dots  , g_{m} \in$ K[X] be some nonzero polynomials. If $f$ and $g_{i}$ are relatively prime for all $i, 1 \le i \le m$, then $f$ and $g_{1} \cdots  g_{m}$ are relatively prime.

*Proof.* We proceed by induction on $m$. The case $m = 1$ is trivial. Let $h = g_{2} \cdots  g_{m}$. By the induction hypothesis, $f$ and $h$ are relatively prime. Let $d$ be a gcd of $f$ and $g_{1}h$. We claim that $d$ is relatively prime to $g_{1}$. Otherwise, $d$ and $g_{1}$ would have some nonconstant gcd $d_{1}$ which would divide both $f$ and $g_{1}$, contradicting the fact that $f$ and $g_{1}$ are relatively prime. Now, by Proposition 30.13, since $d$ divides $g_{1}h$ and $d$ and $g_{1}$ are relatively prime, $d$ divides $h = g_{2} \cdots  g_{m}$. But then, $d$ is a divisor of $f$ and $h$, and since $f$ and $h$ are relatively prime, $d$ must be a constant, and $f$ and $g_{1} \cdots  g_{m}$ are relatively prime. Definition 30.7 is generalized to any finite number of polynomials as follows.

> **Definition 30.8.** Given any nonzero polynomials $f_{1}, \dots  , f_{n} \in$ K[X], where $n \ge 2$, a polynomial $d \in$ K[X] is a greatest common divisor of $f_{1}, \dots  , f_{n}$ (for short, a gcd of $f_{1}, \dots  , f_{n})$ if $d$ divides each $f_{i}$ and whenever $h \in$ K[X] divides each $f_{i}$, then $h$ divides $d$. We say that $f_{1}, \dots  , f_{n}$ are relatively prime if $1$ is a gcd of $f_{1}, \dots  , f_{n}$. It is easily shown that Proposition 30.11 can be generalized to any finite number of polynomials, and similarly for its relevant corollaries. The details are left as an exercise.

> **Proposition 30.15.** Let $K$ be a field and let $f_{1}, \dots  , f_{n} \in$ K[X] be any $n \ge 2$ nonzero polynomials. For every polynomial $d \in$ K[X], the following properties are equivalent:
$(1)$ The polynomial $d$ is a gcd of $f_{1}, \dots  , f_{n}$.
$(2)$ The polynomial $d$ divides each $f_{i}$ and there exist $u_{1}, \dots  , u_{n} \in$ K[X] such that
$$d = u_{1}f_{1} + \cdots  + u_{n}f_{n}.$$
$(3)$ The ideals $(f_{i})$, and $(d)$ satisfy the equation
$$(d) = (f_{1}) + \cdots  + (f_{n}).$$
