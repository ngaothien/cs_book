# Roots of Polynomials


<!-- PAGE 1088 -->
Remark: Given any integer $d \in \mathbb{Z}$ such that $d \neq  0, 1$ and $d$ does not have any square factor
$$\sqrt$$
greater than one,  quadratic field $\mathbb{Q}( \overline{d})$ is the field consisting of all complex numbers
$$of the form a + ib\sqrt \frac{the}{-d} if d < 0,  of all the real numbers of the form a + b\sqrt{d} if d > 0,$$
$$with a, b \in \mathbb{Q}. The subring of \mathbb{Q}(\sqrt \frac{and}{d} ) consisting of all elements as above for which a, b \in \mathbb{Z}$$
$$\sqrt\sqrt$$
is denoted by $\mathbb{Z}[ \overline{d}]$. We define the ring of integers of the field $\mathbb{Q}( \overline{d})$ as the subring of $\sqrt \mathbb{Q}( \overline{d})$ consisting of the following elements:
$$\sqrt$$
$(1)$ If $d \equiv 2$ (mod $4)$ or $d \equiv 3$ (mod $4)$, then all elements of the form $a +$ ib $\overline{-}\overline{d}$ (if $d < 0)$
$$\sqrt$$
or all elements of the form $a + b \overline{d}$ (if $d > 0)$, with a, $b \mathbb{Z}$;
$$(2) If d \equiv 1 (\mathrm{mod} 4), then all elements of the form (a + ib\sqrt \frac{\in}{-d} )/2 (if d < 0) or all elements$$
$$\sqrt$$
of the form $(a+b \overline{d})/2$ (if $d > 0)$, with a, $b \in \mathbb{Z}$ and with a, $b$ either both even or both odd.
$$\sqrt$$
$$that when d \equiv 2 (\mathrm{mod} 4) or d \equiv 3 (\mathrm{mod} 4), the ring of integers of \mathbb{Q}(\overline{d}) is equal to$$
$$\mathbb{Z}[\sqrt \frac{Observe}{d} ].$$
$$\sqrt$$
It can be shown that the rings of integers of the $fields\mathbb{Q}( \overline{-}\overline{d})$ where $d = 19, 43, 67, 163$ are PID’s, but not Euclidean rings. The proof is hard and long. First, it can be shown that these rings are UFD’s (refer to Definition 32.2), see Stark $[170]$ (Chapter  Theorems 8.21
$$and 8.22). Then, we use the fact that the ring of integers of the field \mathbb{Q}(\sqrt \frac{8,}{d} ) (with d \neq  0, 1$$
any square-free integers) is a certain kind of integral domain called a Dedekind ring; see Atiyah-MacDonald $[8]$ (Chapter $9$, Theorem 9.5) or Samuel $[149]$ (Chapter III, Section 3.4). Finally, we use the fact that if a Dedekind ring is a UFD then it is a PID, which follows from Proposition 32.13.
$$\sqrt$$
Actually, the rings of integers $of\mathbb{Q}( \overline{d})$ that are Euclidean domains are completely determined but the proof is quite difficult. It turns out that there are twenty one such rings corresponding to the integers: -11, $-7, -3, -2, -1, 2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57$ and $73$, see Stark $[170]$ (Chapter $8)$. For more on quadratic fields and their rings of integers, see Stark $[170]$ (Chapter $8)$ or Niven, Zuckerman and Montgomery $[136]$ (Chapter $9)$. It is possible to characterize a larger class of rings (in terms of ideals), factorial rings (or unique factorization domains), for which unique factorization holds (see Section 32.1). We now consider zeros (or roots) of polynomials.

## 30.6 Roots of Polynomials

We go back to the general case of an arbitrary ring for a little while.

> **Definition 30.11.** Given a ring $A$ and any polynomial $f \in$ A[X], we say that some $\alpha  \in A$ is a zero of $f$, or a root of $f$, if $f(\alpha$ ) $= 0$. Similarly, given a polynomial $f \in A[X_{1}, \dots  , X_{n}]$, we say that $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A^{n}$ is a a zero of $f$, or a root of $f$, if $f(\alpha_{1} , \dots  , \alpha_{n}$ ) $= 0$. When $f \in$ A[X] is the null polynomial, every $\alpha  \in A$ is trivially a zero of $f$. This case being trivial, we usually assume that we are considering zeros of nonnull polynomials.

<!-- PAGE 1089 -->

> **Example 30.4.** Considering the polynomial f(X) $= X^{2}$ - $1$, both $+1$ and $-1$ are zeros of
$$\mathbb{C}$$
f(X). Over the field of reals, the polynomial g(X) $= X^{2} + 1$ has no zeros. Over the field of complex numbers, g(X) $= X^{2} + 1$ has two roots $i$ and $-i$, the square roots of $-1$, which are “imaginary numbers.” We have the following basic proposition showing the relationship between polynomial division and roots.

> **Proposition 30.19.** Let $f \in$ A[X] be any polynomial and $\alpha  \in A$ any element of $A$. If the result of dividing $f$ by $X$ - $\alpha$  is $f = (X$ - $\alpha )q + r$, then $r = 0$ iff $f(\alpha$ ) $= 0$, i.e., $\alpha$  is a root of $f$ iff $r = 0$.

*Proof.* We have $f = (X$ - $\alpha )q + r$, with deg(r) $< 1 =$ deg(X - $\alpha$ ). Thus, $r$ is a constant in $K$, and since $f(\alpha$ ) $= (\alpha$  - $\alpha )q(\alpha$ ) $+ r$, we get $f(\alpha$ ) $= r$, and the proposition is trivial. We now consider the issue of multiplicity of a root.

> **Proposition 30.20.** Let $f \in$ A[X] be any nonnull polynomial and $h \ge 0$ any integer. The following conditions are equivalent.
$(1) f$ is divisible by $(X$ - $\alpha )^{h}$ but not by $(X$ - $\alpha )^{h+1}$.
$(2)$ There is some $g \in$ A[X] such that $f = (X$ - $\alpha )^{h}g$ and $g(\alpha$ ) $\neq  0$.

*Proof.* Assume $(1)$. Then, we have $f = (X$ - $\alpha )^{h}g$ for some $g \in$ A[X]. If we had $g(\alpha$ ) $= 0$, by Proposition 30.19, $g$ would be divisible by $(X$ - $\alpha$ ), and then $f$ would be divisible by $(X$ - $\alpha )^{h+1}$, contradicting $(1)$. Assume $(2)$, that is, $f = (X$ - $\alpha )^{h}g$ and $g(\alpha$ ) $\neq  0$. If $f$ is divisible by $(X$ - $\alpha )^{h+1}$, then we have $f = (X$ - $\alpha )^{h+1}g_{1}$, for some $g_{1} \in$ A[X]. Then, we have
$$(X -\alpha )^{h}g = (X -\alpha )^{h+1}g_{1},$$
and thus
$$(X -\alpha )^{h}(g -(X -\alpha )g_{1}) = 0,$$
and since the leading coefficient of $(X$ - $\alpha )^{h}$ is $1$ (show this by induction), by Proposition 30.1, $(X$ - $\alpha )^{h}$ is not a zero divisor, and we get $g$ - $(X$ - $\alpha )g_{1} = 0$, i.e., $g = (X$ - $\alpha )g_{1}$, and so $g(\alpha$ ) $= 0$, contrary to the hypothesis. As a consequence of Proposition 30.20, for every nonnull polynomial $f \in$ A[X] and every $\alpha  \in A$, there is a unique integer $h \ge 0$ such that $f$ is divisible by $(X$ - $\alpha )^{h}$ but not by $(X$ - $\alpha )^{h+1}$. Indeed, since $f$ is divisible by $(X$ - $\alpha )^{h}$, we have $h \le$ deg(f). When $h = 0, \alpha$ is not a root of $f$, i.e., $f(\alpha$ ) $\neq  0$. The interesting case is when $\alpha$  is a root of $f$.

<!-- PAGE 1090 -->

> **Definition 30.12.** Given a ring $A$ and any nonnull polynomial $f \in$ A[X], given any $\alpha  \in A$, the unique $h \ge 0$ such that $f$ is divisible by $(X$ - $\alpha )^{h}$ but not by $(X$ - $\alpha )^{h+1}$ is called the order, or multiplicity, of $\alpha$ . We have $h = 0$ iff $\alpha$  is not a root of $f$, and when $\alpha$  is a root of $f$, if $h = 1$, we call $\alpha$  a simple root, if $h = 2$, a double root, and generally, a root of multiplicity $h \ge 2$ is called a multiple root. Observe that Proposition 30.20 $(2)$ implies that if $A \subseteq B$, where $A$ and $B$ are rings, for every nonnull polynomial $f \in$ A[X], if $\alpha  \in A$ is a root of $f$, then the multiplicity of $\alpha$  with respect to $f \in$ A[X] and the multiplicity of $\alpha$  with respect to $f$ considered as a polynomial in B[X], is the same. We now show that if the ring $A$ is an integral domain, the number of roots of a nonzero polynomial is at most its degree.

> **Proposition 30.21.** Let $f, g \in$ A[X] be nonnull polynomials, let $\alpha  \in A$, and let $h \ge 0$ and $k \ge 0$ be the multiplicities of $\alpha$  with respect to $f$ and $g$. The following properties hold.
$(1)$ If $l$ is the multiplicity of $\alpha$  with respect to $(f + g)$, then $l \ge$ min(h, $k)$. If $h \neq  k$, then $l =$ min(h, $k)$.
$(2)$ If $m$ is the multiplicity of $\alpha$  with respect to fg, then $m \ge h + k$. If $A$ is an integral domain, then $m = h + k$.

*Proof.* $(1)$ We have f(X) $= (X$ - $\alpha )^{h}f_{1}(X)$, g(X) $= (X$ - $\alpha )^{k}g_{1}(X)$, with $f_{1}(\alpha$ ) $\neq  0$ and $g_{1}(\alpha$ ) $\neq  0$. Clearly, $l \ge$ min(h, $k)$. If $h \neq  k$, assume $h < k$. Then, we have f(X) $+$ g(X) $= (X$ - $\alpha )^{h}f_{1}(X) + (X$ - $\alpha )^{k}g_{1}(X) = (X$ - $\alpha )^{h}(f_{1}(X) + (X$ - $\alpha )^{k-h}g_{1}(X))$, and since $(f_{1}(X) + (X$ - $\alpha )^{k-h}g_{1}(X))(\alpha$ ) $= f_{1}(\alpha$ ) $\neq  0$, we have $l = h =$ min(h, $k)$.
$(2)$ We have
$$f(X)g(X) = (X -\alpha )^{h+k}f_{1}(X)g_{1}(X),$$
with $f_{1}(\alpha$ )̸ $= 0$ and $g_{1}(\alpha$ )̸ $= 0$. Clearly, $m \ge h + k$. If $A$ is an integral domain, then $f_{1}(\alpha )g_{1}(\alpha$ ) $\neq  0$, and so $m = h + k$.

> **Proposition 30.22.** Let $A$ be an integral domain. Let $f$ be any nonnull polynomial $f \in$ A[X] and let $\alpha_{1} , \dots  , \alpha_{m}  \in A$ be $m \ge 1$ distinct roots of $f$ of respective multiplicities $k_{1}, \dots  , k_{m}$. Then, we have
$$f(X) = (X -\alpha_{1} )^{k1}\cdots  (X -\alpha_{m} )^{km}g(X),$$
where $g \in$ A[X] and $g(\alpha_{i}$ ) $\neq  0$ for all $i, 1 \le i \le m$.

*Proof.* We proceed by induction on $m$. The case $m = 1$ is obvious in view of Definition 30.12 (which itself, is justified by Proposition 30.20). If $m \ge 2$, by the induction hypothesis, we have
$$f(X) = (X -\alpha_{1} )^{k1}\cdots  (X -\alpha_{m-1} )^{km-1}g_{1}(X),$$

<!-- PAGE 1091 -->
where $g_{1} \in$ A[X] and $g_{1}(\alpha_{i}$ ) $\neq  0$, for $1 \le i \le m$ - $1$. Since $A$ is an integral domain and $\alpha_{i}  \neq  \alpha_{j}$  for $i \neq  j$, since $\alpha_{m}$  is a root of $f$, we have
$$0 = (\alpha_{m}  -\alpha_{1} )^{k1}\cdots  (\alpha_{m}  -\alpha_{m-1} )^{km-1}g_{1}(\alpha_{m} ),$$
which implies that $g_{1}(\alpha_{m}$ ) $= 0$. Now, by Proposition 30.21 $(2)$, since $\alpha_{m}$  is not a root of the
$$- \cdots  -$$
polynomial $(X \alpha_{1} )^{k1}  (X \alpha_{m-1} )^{km-1}$ and since $A$ is an integral domain, $\alpha_{m}$  must be a root of multiplicity $k_{m}$ of $g_{1}$, which means that
$$g_{1}(X) = (X -\alpha_{m} )^{km}g(X),$$
with $g(\alpha_{m}$ ) $\neq  0$. Since $g_{1}(\alpha_{i}$ ) $\neq  0$ for $1 \le i \le m$ - $1$ and $A$ is an integral domain, we must also have $g(\alpha_{i}$ ) $\neq  0$, for $1 \le i \le m$ - $1$. Thus, we have
$$f(X) = (X -\alpha_{1} )^{k1}\cdots  (X -\alpha_{m} )^{km}g(X),$$
where $g \in$ A[X], and $g(\alpha_{i}$ ) $\neq  0$ for $1 \le i \le m$. As a consequence of Proposition 30.22, we get the following important result.

> **Theorem 30.23.** Let $A$ be an integral domain. For every nonnull polynomial $f \in$ A[X], if the degree of $f$ is $n =$ deg(f) and $k_{1}, \dots  , k_{m}$ are the multiplicities of all the distinct roots of $f$ (where $m \ge 0)$, then $k_{1} + \cdots  + k_{m} \le n$.

*Proof.* Immediate from Proposition 30.22. Since fields are integral domains, Theorem 30.23 holds for nonnull polynomials over fields and in particular, $for\mathbb{R} and\mathbb{C}$. An important consequence of Theorem 30.23 is the following.

> **Proposition 30.24.** Let $A$ be an integral domain. For any two polynomials $f, g \in$ A[X], if deg(f) $\le n$, deg(g) $\le n$, and if there are $n + 1$ distinct elements $\alpha_{1} , \alpha_{2} , \dots  , \alpha_{n+1}  \in A$ (with $\alpha_{i}  \neq  \alpha_{j}$  for $i \neq  j)$ such that $f(\alpha_{i}$ ) $= g(\alpha_{i}$ ) for all $i, 1 \le i \le n + 1$, then $f = g$.

*Proof.* Assume $f \neq  g$, then, $(f -g)$ is nonnull, and since $f(\alpha_{i}$ ) $= g(\alpha_{i}$ ) for all $i, 1 \le i \le n+1$, the polynomial $(f$ - $g)$ has $n + 1$ distinct roots. Thus, $(f$ - $g)$ has $n + 1$ distinct roots and is of degree at most $n$, which contradicts Theorem 30.23. Proposition 30.24 is often used to show that polynomials coincide. We will use it to show some interpolation formulae due to Lagrange and Hermite. But first, we characterize the multiplicity of a root of a polynomial. For this, we need the notion of derivative familiar in analysis. Actually, we can simply define this notion algebraically. First, we need to rule out some undesirable behaviors. Given a field $K$, as we saw in Example 2.13, we can define a homomorphism $\chi$ : $\mathbb{Z} \to K$ given by
$$\chi (n) = n \cdot  1,$$

<!-- PAGE 1092 -->
where $1$ is the multiplicative identity of $K$. Recall that we define $n \cdot$  a by
$$n \cdot  a = a + \cdots  + a$$
$$|{z}$$
$$n$$
if $n \ge 0$ (with $0 \cdot  a = 0)$ and
$$n \cdot  a = -(-n) \cdot  a$$
if $n < 0$. We say that the field $K$ is of characteristic zero if the homomorphism $\chi$  is injective. Then, for any $a \in K$ with $a \neq  0$, we have $n \cdot  a \neq  0$ for all $n \neq  0$ The fields $\mathbb{Q}, \mathbb{R}$, and $\mathbb{C}$ are of characteristic zero. In fact, it is easy to see that every field of characteristic zero contains a subfield isomorphic $to\mathbb{Q}$. Thus, finite fields can’t be of characteristic zero.
Remark: If a field is not of characteristic zero, it is not hard to show that its characteristic, that is, the smallest $n \ge 2$ such that $n\cdot 1 = 0$, is a prime number $p$. The characteristic $p$ of $K$ is the generator of the principal ideal $p\mathbb{Z}$, the kernel of the homomorphism $\chi$ : $\mathbb{Z} \to K$. Thus, every finite field is of characteristic some prime $p$. Infinite fields of nonzero characteristic also exist.

> **Definition 30.13.** Let $A$ be a ring. The derivative f' , or Df, or $D^{1}f$, of a polynomial $f \in$ A[X] is defined inductively as follows:
$$f'= 0,if f = 0, the null polynomial,$$
$$f'= 0,if f = a, a \neq  0, a \in A,$$
$$f'= na_{n}X^{n-1}+ (n -1)a_{n-1}X^{n-2}+ \cdots  + 2a_{2}X + a_{1},$$
$$if f = a_{n}X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{0}, with n = deg(f) \ge 1.$$
If $A = K$ is a field of characteristic zero, if deg(f) $\ge 1$, the leading coefficient $na_{n}$ of f' is nonzero, and thus, f' is not the null polynomial. Thus, if $A = K$ is a field of characteristic zero, when $n =$ deg(f) $\ge 1$, we have deg(f' ) $= n$ - $1$.  For rings or for fields of characteristic $p \ge 2$, we could have f' $= 0$, for a polynomial $f$ of degree $\ge 1$. The following standard properties of derivatives are recalled without proof (prove them as an exercise). Given any two polynomials, $f, g \in$ A[X], we have
$$(f + g)'= f'+ g',$$
$$(fg)'= f'g + fg'.$$
For example, if $f = (X$ - $\alpha )^{k}g$ and $k \ge 1$, we have
$$f'= k(X -\alpha )^{k-1}g + (X -\alpha )^{k}g'.$$
We can now give a criterion for the existence of simple roots. The first proposition holds for any ring.

<!-- PAGE 1093 -->

> **Proposition 30.25.** Let $A$ be any ring. For every nonnull polynomial $f \in$ A[X], $\alpha  \in A$ is a simple root of $f$ iff $\alpha$  is a root of $f$ and $\alpha$  is not a root of f' .

*Proof.* Since $\alpha  \in A$ is a root of $f$, we have $f = (X$ - $\alpha )g$ for some $g \in$ A[X]. Now, $\alpha$  is a simple root of $f$ iff $g(\alpha$ ) $\neq  0$. However, we have f' $= g + (X$ - $\alpha$ )g', and so $f'(\alpha$ ) $= g(\alpha$ ). Thus, $\alpha$  is a simple root of $f$ iff f' $(\alpha$ ) $\neq  0$. We can improve the previous proposition as follows.

> **Proposition 30.26.** Let $A$ be any ring. For every nonnull polynomial $f \in$ A[X], let $\alpha  \in A$ be a root of multiplicity $k \ge 1$ of $f$. Then, $\alpha$  is a root of multiplicity at least $k$ - $1$ of f' . If $A$ is a field of characteristic zero, then $\alpha$  is a root of multiplicity $k$ - $1$ of f' .

*Proof.* Since $\alpha  \in A$ is a root of multiplicity $k$ of $f$, we have $f = (X -\alpha )^{k}g$ for some $g \in$ A[X] and $g(\alpha$ ) $\neq  0$. Since
$$f'= k(X -\alpha )^{k-1}g + (X -\alpha )^{k}g'= (X -\alpha )^{k-1}(kg + (X -\alpha )g'),$$
it is clear that the multiplicity of $\alpha$  w.r.t. f' is at least k-1. Now, $(kg+(X-\alpha )g')(\alpha$ ) $= kg(\alpha$ ), and if $A$ is of characteristic zero, since $g(\alpha$ )̸ $= 0$, then $kg(\alpha$ )̸ $= 0$. Thus, $\alpha$  is a root of multiplicity $k$ - $1$ of f' . As a consequence, we obtain the following test for the existence of a root of multiplicity $k$ for a polynomial $f$: Given a field $K$ of characteristic zero, for any nonnull polynomial $f \in$ K[X], any $\alpha  \in K$ is a root of multiplicity $k \ge 1$ of $f$ iff $\alpha$  is a root of $f, D^{1}f, D^{2}f, \dots  , D^{k-1}f$, but not a root of $D^{k}f$. We can now return to polynomial functions and tie up some loose ends. Given a ring $A$, recall that every polynomial $f \in A[X_{1}, \dots  , X_{n}]$ induces a function $f_{A}$ : $A^{n} \to A$ defined such that $f_{A}(\alpha_{1} , \dots  , \alpha_{n}$ ) $= f(\alpha_{1} , \dots  , \alpha_{n}$ ), for every $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A^{n}$. We now give a sufficient condition for the mapping $f \mapsto f_{A}$ to be injective.

> **Proposition 30.27.** Let $A$ be an integral domain. For every polynomial $f \in A[X_{1}, \dots  , X_{n}]$, if $A_{1}, \dots  , A_{n}$ are $n$ infinite subsets of $A$ such that $f(\alpha_{1} , \dots  , \alpha_{n}$ ) $= 0$ for all $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A_{1} \times \cdots \times A_{n}$, then $f = 0$, i.e., $f$ is the null polynomial. As a consequence, if $A$ is an infinite integral domain, then the map $f \mapsto f_{A}$ is injective.

*Proof.* We proceed by induction on $n$. Assume $n = 1$. If $f \in A[X_{1}]$ is nonnull, let $m =$ deg(f) be its degree. Since $A_{1}$ is infinite and $f(\alpha_{1}$ ) $= 0$ for all $\alpha_{1}  \in A_{1}$, then $f$ has an infinite number of roots. But since $f$ is of degree $m$, this contradicts Theorem 30.23. Thus, $f = 0$. If $n \ge 2$, we can view $f \in A[X_{1}, \dots  , X_{n}]$ as a polynomial
$$f = g_{m}X_{n}^{m} + g_{m-1}X_{n}^{m-1}+ \cdots  + g_{0},$$

<!-- PAGE 1094 -->
where the coefficients $g_{i}$ are polynomials in $A[X_{1}, \dots  , X_{n-1}]$. Now, for every $(\alpha_{1} , \dots  , \alpha_{n-1}$ ) $\in A_{1} \times  \cdots  \times  A_{n-1}, f(\alpha_{1} , \dots  , \alpha_{n-1} , X_{n})$ determines a polynomial $h(X_{n}) \in A[X_{n}]$, and since $A_{n}$ is infinite and $h(\alpha_{n}$ ) $= f(\alpha_{1} , \dots  , \alpha_{n-1} , \alpha_{n}$ ) $= 0$ for all $\alpha_{n}  \in A_{n}$, by the induction hypothesis, we have $g_{i}(\alpha_{1} , \dots  , \alpha_{n-1}$ ) $= 0$. Now, since $A_{1}, \dots  , A_{n-1}$ are infinite, using the induction hypothesis again, we get $g_{i} = 0$, which shows that $f$ is the null polynomial. The second part of the proposition follows immediately from the first, by letting $A_{i} = A$. When $A$ is an infinite integral domain, in particular an infinite field, since the map $f \mapsto f_{A}$ is injective, we identify the polynomial $f$ with the polynomial function $f_{A}$, and we write $f_{A}$ simply as $f$. The following proposition can be very useful to show polynomial identities.

> **Proposition 30.28.** Let $A$ be an infinite integral domain and $f, g_{1}, \dots  , g_{m} \in A[X_{1}, \dots  , X_{n}]$ be polynomials. If the $g_{i}$ are nonnull polynomials and if
$$f(\alpha_{1} , \dots  , \alpha_{n} ) = 0 whenever g_{i}(\alpha_{1} , \dots  , \alpha_{n} ) \neq  0 for all i, 1 \le i \le m,$$
for every $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A^{n}$, then
$$f = 0,$$
i.e., $f$ is the null polynomial.

*Proof.* If $f$ is not the null polynomial, since the $g_{i}$ are nonnull and $A$ is an integral domain, then the product $fg_{1} \cdots  g_{m}$ is nonnull. By Proposition 30.27, only the null polynomial maps to the zero function, and thus there must be some $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A^{n}$, such that
$$f(\alpha_{1} , \dots  , \alpha_{n} )g_{1}(\alpha_{1} , \dots  , \alpha_{n} ) \cdots  g_{m}(\alpha_{1} , \dots  , \alpha_{n} ) \neq  0,$$
but this contradicts the hypothesis. Proposition 30.28 is often called the principle of extension of algebraic identities. Another perhaps more illuminating way of stating this proposition is as follows: For any polynomial $g \in A[X_{1}, \dots  , X_{n}]$, let
$$V (g) = {(\alpha_{1} , \dots  , \alpha_{n} ) \in A^{n}| g(\alpha_{1} , \dots  , \alpha_{n} ) = 0},$$
the set of zeros of $g$. Note that $V (g_{1}) \cup \cdots  \cup V (g_{m}) = V (g_{1} \cdots  g_{m})$. Then, Proposition 30.28 can be stated as: If $f(\alpha_{1} , \dots  , \alpha_{n}$ ) $= 0$ for every $(\alpha_{1} , \dots  , \alpha_{n}$ ) $\in A^{n}$ - $V (g_{1} \cdots  g_{m})$, then $f = 0$. In other words, if the algebraic identity $f(\alpha_{1} , \dots  , \alpha_{n}$ ) $= 0$ holds on the complement of $V (g_{1}) \cup \cdots  \cup V (g_{m}) = V (g_{1} \cdots  g_{m})$, then $f(\alpha_{1} , \dots  , \alpha_{n}$ ) $= 0$ holds everywhere in $A^{n}$. With this second formulation, we understand better the terminology “principle of extension of algebraic identities.”
