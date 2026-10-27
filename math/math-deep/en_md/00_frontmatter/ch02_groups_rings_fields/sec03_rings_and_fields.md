# 2.3 Rings and Fields

> **Source Pages:** 47–54

The groups $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}/n\mathbb{Z}$, and $\mathrm{M}_n(\mathbb{R})$ are more than abelian groups, they are also commutative rings (except $\mathrm{M}_n(\mathbb{R})$ for $n \ge 2$). Furthermore, $\mathbb{Q}, \mathbb{R}$, and $\mathbb{C}$ are fields. We now introduce rings and fields.

> **Definition 2.16.** A *ring* is a set $A$ equipped with two operations $+ : A \times A \to A$ (called *addition*) and $* : A \times A \to A$ (called *multiplication*) having the following properties:
> - **(R1)** $A$ is an abelian group w.r.t. $+$;
> - **(R2)** $*$ is associative and has an identity element $1 \in A$;
> <!-- PAGE 48 -->
> - **(R3)** $*$ is distributive w.r.t. $+$.
>
> The identity element for addition is denoted $0$, and the additive inverse of $a \in A$ is denoted by $-a$. More explicitly, the axioms of a ring are the following equations which hold for all $a, b, c \in A$:
> $$\begin{aligned}
> a + (b + c) &= (a + b) + c && \text{(associativity of $+$)} \tag{2.1} \\
> a + b &= b + a && \text{(commutativity of $+$)} \tag{2.2} \\
> a + 0 &= 0 + a = a && \text{(zero)} \tag{2.3} \\
> a + (-a) &= (-a) + a = 0 && \text{(additive inverse)} \tag{2.4} \\
> a * (b * c) &= (a * b) * c && \text{(associativity of $*$)} \tag{2.5} \\
> a * 1 &= 1 * a = a && \text{(identity for $*$)} \tag{2.6} \\
> (a + b) * c &= (a * c) + (b * c) && \text{(distributivity)} \tag{2.7} \\
> a * (b + c) &= (a * b) + (a * c) && \text{(distributivity)} \tag{2.8}
> \end{aligned}$$
>
> The ring $A$ is *commutative* if
> $$a * b = b * a \quad \text{for all } a, b \in A.$$

From (2.7) and (2.8), we easily obtain
$$\begin{aligned}
a * 0 &= 0 * a = 0 \tag{2.9} \\
a * (-b) &= (-a) * b = -(a * b). \tag{2.10}
\end{aligned}$$
Note that (2.9) implies that if $1 = 0$, then $a = 0$ for all $a \in A$, and thus, $A = \{0\}$. The ring $A = \{0\}$ is called the *trivial ring*. A ring for which $1 \neq 0$ is called *nontrivial*. The multiplication $a * b$ of two elements $a, b \in A$ is often denoted by $ab$.

> **Example 2.11.**
> 1. The additive groups $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$, are commutative rings.
> 2. For any positive integer $n \in \mathbb{N}$, the group $\mathbb{Z}/n\mathbb{Z}$ is a group under addition. We can also define a multiplication operation by
>    $$\overline{a} \cdot \overline{b} = \overline{ab} = \overline{ab \bmod n},$$
>    for all $a, b \in \mathbb{Z}$. The reader will easily check that the ring axioms are satisfied, with $\overline{0}$ as zero and $\overline{1}$ as multiplicative unit. The resulting ring is denoted by $\mathbb{Z}/n\mathbb{Z}$.[^2]
> 3. The group $\mathbb{R}[X]$ of polynomials in one variable with real coefficients is a ring under multiplication of polynomials. It is a commutative ring.
> <!-- PAGE 49 -->
> 4. Let $d$ be any positive integer. If $d$ is not divisible by any integer of the form $m^2$, with $m \in \mathbb{N}$ and $m \ge 2$, then we say that $d$ is *square-free*. For example, $d = 1, 2, 3, 5, 6, 7, 10$ are square-free, but $4, 8, 9, 12$ are not square-free. If $d$ is any square-free integer and if $d \ge 2$, then the set of real numbers
>    $$\mathbb{Z}[\sqrt{d}] = \{a + b\sqrt{d} \in \mathbb{R} \mid a, b \in \mathbb{Z}\}$$
>    is a commutative ring. If $z = a + b\sqrt{d} \in \mathbb{Z}[\sqrt{d}]$, we write $\overline{z} = a - b\sqrt{d}$. Note that $z\overline{z} = a^2 - db^2$.
> 5. Similarly, if $d \ge 1$ is a positive square-free integer, then the set of complex numbers
>    $$\mathbb{Z}[\sqrt{-d}] = \{a + ib\sqrt{d} \in \mathbb{C} \mid a, b \in \mathbb{Z}\}$$
>    is a commutative ring. If $z = a + ib\sqrt{d} \in \mathbb{Z}[\sqrt{-d}]$, we write $\overline{z} = a - ib\sqrt{d}$. Note that $z\overline{z} = a^2 + db^2$. The case where $d = 1$ is a famous example that was investigated by Gauss, and $\mathbb{Z}[\sqrt{-1}]$, also denoted $\mathbb{Z}[i]$, is called the ring of *Gaussian integers*.
> 6. The group of $n \times n$ matrices $\mathrm{M}_n(\mathbb{R})$ is a ring under matrix multiplication. However, it is not a commutative ring.
> 7. The group $\mathcal{C}(a, b)$ of continuous functions $f : (a, b) \to \mathbb{R}$ is a ring under the operation $f \cdot g$ defined such that
>    $$(f \cdot g)(x) = f(x)g(x)$$
>    for all $x \in (a, b)$.

> **Definition 2.17.** Given a ring $A$, for any element $a \in A$, if there is some element $b \in A$ such that $b \neq 0$ and $ab = 0$, then we say that $a$ is a *zero divisor*. A ring $A$ is an *integral domain* (or an *entire ring*) if $0 \neq 1$, $A$ is commutative, and $ab = 0$ implies that $a = 0$ or $b = 0$, for all $a, b \in A$. In other words, an integral domain is a nontrivial commutative ring with no zero divisors besides $0$.

> **Example 2.12.**
> 1. The rings $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$, are integral domains.
> 2. The ring $\mathbb{R}[X]$ of polynomials in one variable with real coefficients is an integral domain.
> 3. For any positive integer, $n \in \mathbb{N}$, we have the ring $\mathbb{Z}/n\mathbb{Z}$. Observe that if $n$ is composite, then this ring has zero-divisors. For example, if $n = 4$, then we have
>    $$2 \cdot 2 \equiv 0 \pmod{4}.$$
>    The reader should prove that $\mathbb{Z}/n\mathbb{Z}$ is an integral domain iff $n$ is prime (use Proposition 2.17).
> <!-- PAGE 50 -->
> 4. If $d$ is a square-free positive integer and if $d \ge 2$, the ring $\mathbb{Z}[\sqrt{d}]$ is an integral domain. Similarly, if $d \ge 1$ is a square-free positive integer, the ring $\mathbb{Z}[\sqrt{-d}]$ is an integral domain. Finding the invertible elements of these rings is a very interesting problem.
> 5. The ring of $n \times n$ matrices $\mathrm{M}_n(\mathbb{R})$ has zero divisors.

A homomorphism between rings is a mapping preserving addition and multiplication (and $0$ and $1$).

> **Definition 2.18.** Given two rings $A$ and $B$, a *homomorphism* between $A$ and $B$ is a function $h : A \to B$ satisfying the following conditions for all $x, y \in A$:
> $$\begin{aligned}
> h(x + y) &= h(x) + h(y) \\
> h(xy) &= h(x)h(y) \\
> h(0) &= 0 \\
> h(1) &= 1.
> \end{aligned}$$

Actually, because $B$ is a group under addition, $h(0) = 0$ follows from
$$h(x + y) = h(x) + h(y).$$

> **Example 2.13.**
> 1. If $A$ is a ring, for any integer $n \in \mathbb{Z}$, for any $a \in A$, we define $n \cdot a$ by
>    $$n \cdot a = \underbrace{a + \dots + a}_{n}$$
>    if $n \ge 0$ (with $0 \cdot a = 0$) and
>    $$n \cdot a = -(-n) \cdot a$$
>    if $n < 0$. Then, the map $h : \mathbb{Z} \to A$ given by
>    $$h(n) = n \cdot 1_A$$
>    is a ring homomorphism (where $1_A$ is the multiplicative identity of $A$).
> 2. Given any real $\lambda \in \mathbb{R}$, the evaluation map $\eta_\lambda : \mathbb{R}[X] \to \mathbb{R}$ defined by
>    $$\eta_\lambda(f(X)) = f(\lambda)$$
>    for every polynomial $f(X) \in \mathbb{R}[X]$ is a ring homomorphism.

> **Definition 2.19.** A ring homomorphism $h : A \to B$ is an *isomorphism* iff there is a ring homomorphism $g : B \to A$ such that $g \circ h = \mathrm{id}_A$ and $h \circ g = \mathrm{id}_B$. An isomorphism from a ring to itself is called an *automorphism*.

<!-- PAGE 51 -->

As in the case of a group isomorphism, the homomorphism $g$ is unique and denoted by $h^{-1}$, and it is easy to show that a bijective ring homomorphism $h : A \to B$ is an isomorphism.

> **Definition 2.20.** Given a ring $A$, a subset $A'$ of $A$ is a *subring* of $A$ if $A'$ is a subgroup of $A$ (under addition), is closed under multiplication, and contains $1$.

For example, we have the following sequence in which every ring on the left of an inclusion sign is a subring of the ring on the right of the inclusion sign:
$$\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}.$$
The ring $\mathbb{Z}$ is a subring of both $\mathbb{Z}[\sqrt{d}]$ and $\mathbb{Z}[\sqrt{-d}]$, the ring $\mathbb{Z}[\sqrt{d}]$ is a subring of $\mathbb{R}$ and the ring $\mathbb{Z}[\sqrt{-d}]$ is a subring of $\mathbb{C}$.

If $h : A \to B$ is a homomorphism of rings, then it is easy to show for any subring $A'$, the image $h(A')$ is a subring of $B$, and for any subring $B'$ of $B$, the inverse image $h^{-1}(B')$ is a subring of $A$.

As for groups, the kernel of a ring homomorphism $h : A \to B$ is defined by
$$\operatorname{Ker} h = \{a \in A \mid h(a) = 0\}.$$
Just as in the case of groups, we have the following criterion for the injectivity of a ring homomorphism. The proof is identical to the proof for groups.

> **Proposition 2.18.** If $h : A \to B$ is a homomorphism of rings, then $h : A \to B$ is injective iff $\operatorname{Ker} h = \{0\}$. (We also write $\operatorname{Ker} h = (0)$.)

The kernel of a ring homomorphism is an abelian subgroup of the additive group $A$, but in general it is not a subring of $A$, because it may not contain the multiplicative identity element $1$. However, it satisfies the following closure property under multiplication:
$$ab \in \operatorname{Ker} h \quad \text{and} \quad ba \in \operatorname{Ker} h \quad \text{for all } a \in \operatorname{Ker} h \text{ and all } b \in A.$$
This is because if $h(a) = 0$, then for all $b \in A$ we have
$$h(ab) = h(a)h(b) = 0h(b) = 0 \quad \text{and} \quad h(ba) = h(b)h(a) = h(b)0 = 0.$$

> **Definition 2.21.** Given a ring $A$, an additive subgroup $I$ of $A$ satisfying the property below
> $$ab \in I \quad \text{and} \quad ba \in I \quad \text{for all } a \in I \text{ and all } b \in A \tag{$*_{\text{ideal}}$}$$
> is called a *two-sided ideal*. If $A$ is a commutative ring, we simply say an *ideal*.

It turns out that for any ring $A$ and any two-sided ideal $I$, the set $A/I$ of additive cosets $a + I$ (with $a \in A$) is a ring called a *quotient ring*. Then we have the following analog of Proposition 2.12, also called the *first isomorphism theorem*.

<!-- PAGE 52 -->

> **Proposition 2.19.** Given a homomorphism of rings $h : A \to B$, the rings $A/\operatorname{Ker} h$ and $\operatorname{Im} h = h(A)$ are isomorphic.

A field is a commutative ring $K$ for which $K - \{0\}$ is a group under multiplication.

> **Definition 2.22.** A set $K$ is a *field* if it is a ring and the following properties hold:
> - **(F1)** $0 \neq 1$;
> - **(F2)** For every $a \in K$, if $a \neq 0$, then $a$ has an inverse w.r.t. $*$;
> - **(F3)** $*$ is commutative.

Let $K^* = K - \{0\}$. Observe that (F1) and (F2) are equivalent to the fact that $K^*$ is a group w.r.t. $*$ with identity element $1$. If $*$ is not commutative but (F1) and (F2) hold, we say that we have a *skew field* (or *noncommutative field*).

Note that we are assuming that the operation $*$ of a field is commutative. This convention is not universally adopted, but since $*$ will be commutative for most fields we will encounter, we may as well include this condition in the definition.

> **Example 2.14.**
> 1. The rings $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$ are fields.
> 2. The set of (formal) fractions $f(X)/g(X)$ of polynomials $f(X), g(X) \in \mathbb{R}[X]$, where $g(X)$ is not the null polynomial, is a field.
> 3. The ring $\mathcal{C}(a, b)$ of continuous functions $f : (a, b) \to \mathbb{R}$ such that $f(x) \neq 0$ for all $x \in (a, b)$ is a field (when equipped with pointwise operations on nonvanishing rational expressions, or note that nonvanishing functions have multiplicative inverses in $\mathcal{C}(a,b)$).
> 4. Using Proposition 2.17, it is easy to see that the ring $\mathbb{Z}/p\mathbb{Z}$ is a field iff $p$ is prime.
> 5. If $d$ is a square-free positive integer and if $d \ge 2$, the set
>    $$\mathbb{Q}(\sqrt{d}) = \{a + b\sqrt{d} \in \mathbb{R} \mid a, b \in \mathbb{Q}\}$$
>    is a field. If $z = a + b\sqrt{d} \in \mathbb{Q}(\sqrt{d})$ and $\overline{z} = a - b\sqrt{d}$, then it is easy to check that if $z \neq 0$, then $z^{-1} = \overline{z}/(z\overline{z})$.
> 6. Similarly, if $d \ge 1$ is a square-free positive integer, the set of complex numbers
>    $$\mathbb{Q}(\sqrt{-d}) = \{a + ib\sqrt{d} \in \mathbb{C} \mid a, b \in \mathbb{Q}\}$$
>    is a field. If $z = a + ib\sqrt{d} \in \mathbb{Q}(\sqrt{-d})$ and $\overline{z} = a - ib\sqrt{d}$, then it is easy to check that if $z \neq 0$, then $z^{-1} = \overline{z}/(z\overline{z})$.

<!-- PAGE 53 -->

> **Definition 2.23.** A *homomorphism* $h : K_1 \to K_2$ between two fields $K_1$ and $K_2$ is just a homomorphism between the rings $K_1$ and $K_2$.

However, because $K_1^*$ and $K_2^*$ are groups under multiplication, a homomorphism of fields must be injective.

*Proof.* First, observe that for any $x \neq 0$,
$$1 = h(1) = h(x x^{-1}) = h(x)h(x^{-1})$$
and
$$1 = h(1) = h(x^{-1} x) = h(x^{-1})h(x),$$
so $h(x) \neq 0$ and
$$h(x^{-1}) = h(x)^{-1}.$$
But then, if $h(x) = 0$, we must have $x = 0$. Consequently, $h$ is injective. $\square$

> **Definition 2.24.** A field homomorphism $h : K_1 \to K_2$ is an *isomorphism* iff there is a homomorphism $g : K_2 \to K_1$ such that $g \circ h = \mathrm{id}_{K_1}$ and $h \circ g = \mathrm{id}_{K_2}$. An isomorphism from a field to itself is called an *automorphism*.

Then, just as in the case of rings, $g$ is unique and denoted by $h^{-1}$, and a bijective field homomorphism $h : K_1 \to K_2$ is an isomorphism.

> **Definition 2.25.** Since every homomorphism $h : K_1 \to K_2$ between two fields is injective, the image $h(K_1)$ of $K_1$ is a *subfield* of $K_2$. We say that $K_2$ is an *extension* of $K_1$.

For example, $\mathbb{R}$ is an extension of $\mathbb{Q}$ and $\mathbb{C}$ is an extension of $\mathbb{R}$. The fields $\mathbb{Q}(\sqrt{d})$ and $\mathbb{Q}(\sqrt{-d})$ are extensions of $\mathbb{Q}$, the field $\mathbb{R}$ is an extension of $\mathbb{Q}(\sqrt{d})$ and the field $\mathbb{C}$ is an extension of $\mathbb{Q}(\sqrt{-d})$.

> **Definition 2.26.** A field $K$ is said to be *algebraically closed* if every nonconstant polynomial $p(X)$ with coefficients in $K$ has some root in $K$; that is, there is some $a \in K$ such that $p(a) = 0$.

It can be shown that every field $K$ has some minimal extension $\Omega$ which is algebraically closed, called an *algebraic closure* of $K$. For example, $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$. The algebraic closure of $\mathbb{Q}$ is called the *field of algebraic numbers*. This field consists of all complex numbers that are zeros of a polynomial with coefficients in $\mathbb{Q}$.

> **Definition 2.27.** Given a field $K$ and an automorphism $h : K \to K$ of $K$, it is easy to check that the set
> $$\operatorname{Fix}(h) = \{a \in K \mid h(a) = a\}$$
> of elements of $K$ fixed by $h$ is a subfield of $K$ called the *field fixed by $h$*.

<!-- PAGE 54 -->

For example, if $d \ge 2$ is square-free, then the map $c : \mathbb{Q}(\sqrt{d}) \to \mathbb{Q}(\sqrt{d})$ given by
$$c(a + b\sqrt{d}) = a - b\sqrt{d}$$
is an automorphism of $\mathbb{Q}(\sqrt{d})$, and $\operatorname{Fix}(c) = \mathbb{Q}$.

If $K$ is a field, we have the ring homomorphism $h : \mathbb{Z} \to K$ given by $h(n) = n \cdot 1$. If $h$ is injective, then $K$ contains a copy of $\mathbb{Z}$, and since it is a field, it contains a copy of $\mathbb{Q}$. In this case, we say that $K$ has *characteristic $0$*. If $h$ is not injective, then $h(\mathbb{Z})$ is a subring of $K$, and thus an integral domain; the kernel of $h$ is a subgroup of $\mathbb{Z}$, which by Proposition 2.15 must be of the form $p\mathbb{Z}$ for some $p \ge 1$. By the first isomorphism theorem, $h(\mathbb{Z})$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$ for some $p \ge 1$. But then, $p$ must be prime since $\mathbb{Z}/p\mathbb{Z}$ is an integral domain iff it is a field iff $p$ is prime. The prime $p$ is called the *characteristic* of $K$, and we also say that $K$ is of *finite characteristic*.

> **Definition 2.28.** If $K$ is a field, then either
> 1. $n \cdot 1 \neq 0$ for all integers $n \ge 1$, in which case we say that $K$ has *characteristic $0$*, or
> 2. There is some smallest prime number $p$ such that $p \cdot 1 = 0$ called the *characteristic* of $K$, and we say $K$ is of *finite characteristic*.

A field $K$ of characteristic $0$ contains a copy of $\mathbb{Q}$, thus is infinite. As we will see in Section 8.10, a finite field has nonzero characteristic $p$. However, there are infinite fields of nonzero characteristic.

[^2]: The notation $\mathbb{Z}_n$ is sometimes used instead of $\mathbb{Z}/n\mathbb{Z}$ but it clashes with the notation for the $n$-adic integers so we prefer not to use it.
