# 2.2 Cyclic Groups

> **Source Pages:** 44–47

Given a group $G$ with unit element $1$, for any element $g \in G$ and for any natural number $n \in \mathbb{N}$, we define $g^n$ as follows:
$$\begin{aligned}
g^0 &= 1 \\
g^{n+1} &= g \cdot g^n.
\end{aligned}$$
<!-- PAGE 45 -->
For any integer $n \in \mathbb{Z}$, we define $g^n$ by
$$g^n = \begin{cases} g^n & \text{if } n \ge 0 \\ (g^{-1})^{(-n)} & \text{if } n < 0. \end{cases}$$
The following properties are easily verified:
$$\begin{aligned}
g^i \cdot g^j &= g^{i+j} \\
(g^i)^{-1} &= g^{-i} \\
g^i \cdot g^j &= g^j \cdot g^i,
\end{aligned}$$
for all $i, j \in \mathbb{Z}$.

Define the subset $\langle g \rangle$ of $G$ by
$$\langle g \rangle = \{g^n \mid n \in \mathbb{Z}\}.$$
The following proposition is left as an exercise.

> **Proposition 2.14.** Given a group $G$, for any element $g \in G$, the set $\langle g \rangle$ is the smallest abelian subgroup of $G$ containing $g$.

> **Definition 2.13.** A group $G$ is *cyclic* iff there is some element $g \in G$ such that $G = \langle g \rangle$. An element $g \in G$ with this property is called a *generator* of $G$.

The Klein four-group $V$ of Example 2.7 is abelian, but not cyclic. This is because $V$ has four elements, but all the elements different from the identity have order $2$.

Cyclic groups are quotients of $\mathbb{Z}$. For this, we use a basic property of $\mathbb{Z}$. Recall that for any $n \in \mathbb{Z}$, we let $n\mathbb{Z}$ denote the set of multiples of $n$,
$$n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}.$$

> **Proposition 2.15.** Every subgroup $H$ of $\mathbb{Z}$ is of the form $H = n\mathbb{Z}$ for some $n \in \mathbb{N}$.

*Proof.* If $H$ is the trivial group $\{0\}$, then let $n = 0$. If $H$ is nontrivial, for any nonzero element $m \in H$, we also have $-m \in H$ and either $m$ or $-m$ is positive, so let $n$ be the smallest positive integer in $H$. By Proposition 2.14, $n\mathbb{Z}$ is the smallest subgroup of $H$ containing $n$. For any $m \in H$ with $m \neq 0$, we can write
$$m = nq + r, \quad \text{with } 0 \le r < n.$$
Now, since $n\mathbb{Z} \subseteq H$, we have $nq \in H$, and since $m \in H$, we get $r = m - nq \in H$. However, $0 \le r < n$, contradicting the minimality of $n$, so $r = 0$, and $H = n\mathbb{Z}$. $\square$

<!-- PAGE 46 -->

Given any cyclic group $G$, for any generator $g$ of $G$, we can define a mapping $\phi : \mathbb{Z} \to G$ by $\phi(m) = g^m$. Since $g$ generates $G$, this mapping is surjective. The mapping $\phi$ is clearly a group homomorphism, so let $H = \operatorname{Ker} \phi$ be its kernel. By a previous observation, $H = n\mathbb{Z}$ for some $n \in \mathbb{Z}$, so by the first homomorphism theorem, we obtain an isomorphism
$$\overline{\phi} : \mathbb{Z}/n\mathbb{Z} \longrightarrow G$$
from the quotient group $\mathbb{Z}/n\mathbb{Z}$ onto $G$. Obviously, if $G$ has finite order, then $|G| = n$. In summary, we have the following result.

> **Proposition 2.16.** Every cyclic group $G$ is either isomorphic to $\mathbb{Z}$, or to $\mathbb{Z}/n\mathbb{Z}$, for some natural number $n > 0$. In the first case, we say that $G$ is an *infinite cyclic group*, and in the second case, we say that $G$ is a *cyclic group of order $n$*.

The quotient group $\mathbb{Z}/n\mathbb{Z}$ consists of the cosets $m + n\mathbb{Z} = \{m + nk \mid k \in \mathbb{Z}\}$, with $m \in \mathbb{Z}$, that is, of the equivalence classes of $\mathbb{Z}$ under the equivalence relation $\equiv$ defined such that
$$x \equiv y \quad \text{iff} \quad x - y \in n\mathbb{Z} \quad \text{iff} \quad x \equiv y \pmod{n}.$$
We also denote the equivalence class $x + n\mathbb{Z}$ of $x$ by $\overline{x}$, or if we want to be more precise by $[x]_n$. The group operation is given by
$$\overline{x} + \overline{y} = \overline{x + y}.$$
For every $x \in \mathbb{Z}$, there is a unique representative, $x \bmod n$ (the nonnegative remainder of the division of $x$ by $n$) in the class $\overline{x}$ of $x$, such that $0 \le x \bmod n \le n - 1$. For this reason, we often identify $\mathbb{Z}/n\mathbb{Z}$ with the set $\{0, \dots, n - 1\}$. To be more rigorous, we can give $\{0, \dots, n - 1\}$ a group structure by defining $+_n$ such that
$$x +_n y = (x + y) \bmod n.$$
Then, it is easy to see that $\{0, \dots, n - 1\}$ with the operation $+_n$ is a group with identity element $0$ isomorphic to $\mathbb{Z}/n\mathbb{Z}$.

We can also define a multiplication operation $\cdot$ on $\mathbb{Z}/n\mathbb{Z}$ as follows:
$$\overline{a} \cdot \overline{b} = \overline{ab} = \overline{ab \bmod n}.$$
Then, it is easy to check that $\cdot$ is abelian, associative, that $\overline{1}$ is an identity element for $\cdot$, and that $\cdot$ is distributive on the left and on the right with respect to addition. This makes $\mathbb{Z}/n\mathbb{Z}$ into a commutative ring. We usually suppress the dot and write $\overline{a}\,\overline{b}$ instead of $\overline{a} \cdot \overline{b}$.

> **Proposition 2.17.** Given any integer $n \ge 1$, for any $a \in \mathbb{Z}$, the residue class $\overline{a} \in \mathbb{Z}/n\mathbb{Z}$ is invertible with respect to multiplication iff $\gcd(a, n) = 1$.

<!-- PAGE 47 -->

*Proof.* If $\overline{a}$ has inverse $\overline{b}$ in $\mathbb{Z}/n\mathbb{Z}$, then $\overline{a}\,\overline{b} = \overline{1}$, which means that
$$ab \equiv 1 \pmod{n},$$
that is $ab = 1 + nk$ for some $k \in \mathbb{Z}$, which is the Bézout identity
$$ab - nk = 1$$
and implies that $\gcd(a, n) = 1$. Conversely, if $\gcd(a, n) = 1$, then by Bézout's identity there exist $u, v \in \mathbb{Z}$ such that
$$au + nv = 1,$$
so $au = 1 - nv$, that is,
$$au \equiv 1 \pmod{n},$$
which means that $\overline{a}\,\overline{u} = \overline{1}$, so $\overline{a}$ is invertible in $\mathbb{Z}/n\mathbb{Z}$. $\square$

> **Definition 2.14.** The group (under multiplication) of invertible elements of the ring $\mathbb{Z}/n\mathbb{Z}$ is denoted by $(\mathbb{Z}/n\mathbb{Z})^*$. Note that this group is abelian and only defined if $n \ge 2$.

The Euler $\phi$-function plays an important role in the theory of the groups $(\mathbb{Z}/n\mathbb{Z})^*$.

> **Definition 2.15.** Given any positive integer $n \ge 1$, the *Euler $\phi$-function* (or *Euler totient function*) is defined such that $\phi(n)$ is the number of integers $a$, with $1 \le a \le n$, which are relatively prime to $n$; that is, with $\gcd(a, n) = 1$.[^1]

Then, by Proposition 2.17, we see that the group $(\mathbb{Z}/n\mathbb{Z})^*$ has order $\phi(n)$.

For $n = 2$, $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$, the trivial group. For $n = 3$, $(\mathbb{Z}/3\mathbb{Z})^* = \{1, 2\}$, and for $n = 4$, we have $(\mathbb{Z}/4\mathbb{Z})^* = \{1, 3\}$. Both groups are isomorphic to the group $\{-1, 1\}$. Since $\gcd(a, n) = 1$ for every $a \in \{1, \dots, n - 1\}$ iff $n$ is prime, by Proposition 2.17 we see that $(\mathbb{Z}/n\mathbb{Z})^* = \mathbb{Z}/n\mathbb{Z} - \{0\}$ iff $n$ is prime.

[^1]: We allow $a = n$ to accommodate the special case $n = 1$.
