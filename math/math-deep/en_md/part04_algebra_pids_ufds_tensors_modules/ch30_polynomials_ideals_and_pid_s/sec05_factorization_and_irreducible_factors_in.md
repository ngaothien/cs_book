# Factorization and Irreducible Factors in K[X]


<!-- PAGE 1084 -->
In addition, $d \neq  0$, and $d$ is unique up to multiplication by a nonzero scalar in $K$. As a consequence of Proposition 30.15, some polynomials $f_{1}, \dots  , f_{n} \in$ K[X] are relatively prime iff there exist $u_{1}, \dots  , u_{n} \in$ K[X] such that
$$u_{1}f_{1} + \cdots  + u_{n}f_{n} = 1.$$
The identity
$$u_{1}f_{1} + \cdots  + u_{n}f_{n} = 1$$
of part $(2)$ of Proposition 30.15 is also called the Bezout identity. We now consider the factorization of polynomials of a single variable into irreducible factors.

## 30.5 Factorization and Irreducible Factors in K[X]


> **Definition 30.9.** Given a field $K$, a polynomial $p \in$ K[X] is irreducible or indecomposable or prime if deg(p) $\ge 1$ and if $p$ is not divisible by any polynomial $q \in$ K[X] such that $1 \le$ deg(q) $<$ deg(p). Equivalently, $p$ is irreducible if deg(p) $\ge 1$ and if $p = q_{1}q_{2}$, then either $q_{1} \in K$ or $q_{2} \in K$ (and of course, $q_{1} \neq  0, q_{2} \neq  0)$.

> **Example 30.2.** Every polynomial aX $+ b$ of degree $1$ is irreducible. Over the field $\mathbb{R}$, the polynomial $X^{2} + 1$ is irreducible (why?), but $X^{3} + 1$ is not irreducible, since
$$X^{3}+ 1 = (X + 1)(X^{2}-X + 1).$$
$$\mathbb{R}$$
The polynomial $X^{2}$ - $X + 1$ is irreducible over  (why?). It would seem that $X^{4} + 1$ is irreducible over $\mathbb{R}$, but in fact,
$$\sqrt\sqrt$$
$$X^{4}+ 1 = (X^{2}-\overline{2} X + 1)(X^{2}+\overline{2} X + 1).$$
$$\mathbb{Q}$$
However, in view of the above factorization, $X^{4} + 1$ is irreducible over . It can be shown that the irreducible polynomials $over\mathbb{R}$ are the polynomials of degree $1$, or the polynomials of degree $2$ of the form $aX^{2} +$ bX $+ c$, for which $b^{2}$ - 4ac $< 0$ (i.e., those having no real roots). This is not easy to prove! Over the complex numbers $\mathbb{C}$, the only irreducible polynomials are those of degree $1$. This is a version of a fact often referred to as the “Fundamental theorem of Algebra”, or, as the French sometimes say, as “d’Alembert’s theorem”! We already observed that for any two nonzero polynomials $f, g \in$ K[X], $f$ divides $g$ iff
$(g) \subseteq (f)$. In view of the definition of a maximal ideal given in Definition 30.4, we now prove that a polynomial $p \in$ K[X] is irreducible iff(p) is a maximal ideal in K[X].

> **Proposition 30.16.** A polynomial $p \in$ K[X] is irreducible iff $(p)$ is a maximal ideal in K[X].

<!-- PAGE 1085 -->

*Proof.* Since K[X] is an integral domain, for all nonzero polynomials $p, q \in$ K[X], deg(pq) $=$ deg(p) $+$ deg(q), and thus, $(p) \neq$  K[X] iff deg(p) $\ge 1$. Assume that $p \in$ K[X] is irreducible. Since every ideal in K[X] is a principal ideal, every ideal in K[X] is of the form $(q)$, for some $q \in$ K[X]. If $(p) \subseteq (q)$, with deg(q) $\ge 1$, then $q$ divides $p$, and since $p \in$ K[X] is irreducible, this implies that $p = \lambda q$ for some $\lambda  \neq  0$ in $K$, and so, $(p) = (q)$. Thus, $(p)$ is a maximal ideal. Conversely, assume that $(p)$ is a maximal ideal. Then, as we showed above, deg(p) $\ge 1$, and if $q$ divides $p$, with deg(q) $\ge 1$, then $(p) \subseteq (q)$, and since $(p)$ is a maximal ideal, this implies that $(p) = (q)$, which means that $p = \lambda q$ for some $\lambda  \neq  0$ in $K$, and so, $p$ is irreducible. Let $p \in$ K[X] be irreducible. Then, for every nonzero polynomial $g \in$ K[X], either $p$ and $g$ are relatively prime, or $p$ divides $g$. Indeed, if $d$ is any gcd of $p$ and $g$, if $d$ is a constant, then $p$ and $g$ are relatively prime, and if not, because $p$ is irreducible, we have $d = \lambda p$ for some $\lambda  \neq  0$ in $K$, and thus, $p$ divides $g$. As a consequence, if $p, q \in$ K[X] are both irreducible, then either $p$ and $q$ are relatively prime, or $p = \lambda q$ for some $\lambda  \neq  0$ in $K$. In particular, if $p, q \in$ K[X] are both irreducible monic polynomials and $p \neq  q$, then $p$ and $q$ are relatively prime. We now prove the (unique) factorization of polynomials into irreducible factors.

> **Theorem 30.17.** Given any field $K$, for every nonzero polynomial
$$f = a_{d}X^{d}+ a_{d-1}X^{d-1}+ \cdots  + a_{0}$$
of degree $d =$ deg(f) $\ge 1$ in K[X], there exists a unique set ${\langle p_{1}, k_{1}\rangle , \dots  , \langle p_{m}, k_{m}\rangle$ } such that
$$f = a_{d}p_{1}^{k1} \cdots  p_{m}^{km} ,$$
where the $p_{i} \in$ K[X] are distinct irreducible monic polynomials, the $k_{i}$ are (not necessarily distinct) integers, and $m \ge 1, k_{i} \ge 1$.

*Proof.* First, we prove the existence of such a factorization by induction on $d =$ deg(f). Clearly, it is enough to prove the result for monic polynomials $f$ of degree $d =$ deg(f) $\ge 1$. If $d = 1$, then $f = X + a_{0}$, which is an irreducible monic polynomial. Assume $d \ge 2$, and assume the induction hypothesis for all monic polynomials of degree $< d$. Consider the set $S$ of all monic polynomials $g$ such that deg(g) $\ge 1$ and $g$ divides $f$. Since $f \in S$, the set $S$ is nonempty, and thus, $S$ contains some monic polynomial $p_{1}$ of minimal degree. Since $deg(p_{1}) \ge 1$, the monic polynomial $p_{1}$ must be irreducible. Otherwise we would have $p_{1} = g_{1}g_{2}$, for some monic polynomials $g_{1}, g_{2}$ such that $deg(p_{1}) > deg(g_{1}) \ge 1$ and $deg(p_{1}) > deg(g_{2}) \ge 1$, and since $p_{1}$ divide $f$, then $g_{1}$ would divide $f$, contradicting the minimality of the degree of $p_{1}$. Thus, we have $f = p_{1}q$, for some irreducible monic polynomial $p_{1}$, with $q$ also monic. Since $deg(p_{1}) \ge 1$, we have deg(q) $<$ deg(f), and we can apply the induction hypothesis to $q$. Thus, we obtain a factorization of the desired form.

<!-- PAGE 1086 -->
We now prove uniqueness. Assume that
$$f = a_{d}p_{1}^{k1} \cdots  p_{m}^{km} ,$$
and
$$f = a_{d}q_{1}^{h1} \cdots  q_{n}^{hn} .$$
Thus, we have
$$a_{d}p_{1}^{k1} \cdots  p_{m}^{km} = a_{d}q_{1}^{h1} \cdots  q_{n}^{hn} .$$
We prove that $m = n, p_{i} = q_{i}$ and $h_{i} = k_{i}$, for all $i$, with $1 \le i \le n$. The proof proceeds by induction on $h_{1} + \cdots  + h_{n}$. If $h_{1} + \cdots  + h_{n} = 1$, then $n = 1$ and $h_{1} = 1$. Then, since K[X] is an integral domain, we have
$$p_{1}^{k1} \cdots  p_{m}^{km} = q_{1},$$
and since $q_{1}$ and the $p_{i}$ are irreducible monic, we must have $m = 1$ and $p_{1} = q_{1}$. If $h_{1} + \cdots  + h_{n} \ge 2$, since K[X] is an integral domain and since $h_{1} \ge 1$, we have
$$p_{1}^{k1} \cdots  p_{m}^{km} = q_{1}q,$$
with
$$q = q_{1}^{h1-1}\cdots  q_{n}^{hn} ,$$
where $(h_{1}$ - $1) + \cdots  + h_{n} \ge 1$ (and $q_{1}^{h1-1} = 1$ if $h_{1} = 1)$. Now, if $q_{1}$ is not equal to any of the $p_{i}$, by a previous remark, $q_{1}$ and $p_{i}$ are relatively prime, and by Proposition 30.14, $q_{1}$ and $p_{1}^{k1} \cdots  p_{m}^{km}$ are relatively prime. But this contradicts the fact that $q_{1}$ divides $p_{1}^{k1} \cdots  p_{m}^{km}$ . Thus, $q_{1}$ is equal to one of the $p_{i}$. Without loss of generality, we can assume that $q_{1} = p_{1}$. Then, since K[X] is an integral domain, we have
$$p_{1}^{k1-1}\cdots  p_{m}^{km} = q_{1}^{h1-1}\cdots  q_{n}^{hn} ,$$
where $p_{1}^{k1-1} = 1$ if $k_{1} = 1$, and $q_{1}^{h1-1} = 1$ if $h_{1} = 1$. Now, $(h_{1}$ - $1) + \cdots  + h_{n} < h_{1} + \cdots  + h_{n}$, and we can apply the induction hypothesis to conclude that $m = n, p_{i} = q_{i}$ and $h_{i} = k_{i}$, with $1 \le i \le n$. The above considerations about unique factorization into irreducible factors can be extended almost without changes to more general rings known as Euclidean domains. In such rings, some abstract version of the division theorem is assumed to hold.

> **Definition 30.10.** A Euclidean domain (or Euclidean ring) is an integral domain $A$ such that there exists a function $\phi$ : $A \to \mathbb{N}$ with the following property: For all a, $b \in A$ with $b \neq  0$, there are some $q, r \in A$ such that
$$a = bq + rand\phi (r) < \phi (b).$$

<!-- PAGE 1087 -->
Note that the pair $(q, r)$ is not necessarily unique. Actually, unique factorization holds in principal ideal domains (PID’s), see Theorem 32.12. As shown below, every Euclidean domain is a PID, and thus, unique factorization holds for Euclidean domains.

> **Proposition 30.18.** Every Euclidean domain $A$ is a PID.

*Proof.* Let $\mathfrak{I}$ be a nonnull ideal in $A$. Then, the set
$${\phi (a) | a \in \mathfrak{I}}$$
is nonempty, and thus, has a smallest element $m$. Let $b$ be any (nonnull) element of $\mathfrak{I}$ such that $m = \phi (b)$. We claim that $\mathfrak{I} = (b)$. Given any $a \in \mathfrak{I}$, we can write
$$a = bq + r$$
for some $q, r \in A$, with $\phi (r) < \phi (b)$. Since $b \in \mathfrak{I}$ and $\mathfrak{I}$ is an ideal, we also have bq $\in \mathfrak{I}$, and since a, bq $\in \mathfrak{I}$ and $\mathfrak{I}$ is an ideal, then $r \in \mathfrak{I}$ with $\phi (r) < \phi (b) = m$, contradicting the minimality of $m$. Thus, $r = 0$ and $a \in (b)$. But then,
$$\mathfrak{I} \subseteq (b),$$
and since $b \in \mathfrak{I}$, we get
$$\mathfrak{I} = (b),$$
and $A$ is a PID. As a corollary of Proposition 30.18, the $ring\mathbb{Z}$ is a Euclidean domain (using the function $\phi (a) =$ |a|) and thus, a PID. If $K$ is a field, the function $\phi$  on K[X] defined such that
$$0$$
$$if f = 0,$$
$$\phi (f) =$$
$$deg(f) + 1if f \neq  0,$$
shows that K[X] is a Euclidean domain.

> **Example 30.3.** A more interesting example of a Euclidean domain is the $ring\mathbb{Z}[i]$ of Gaussian integers, i.e., the subring of $\mathbb{C}$ consisting of all complex numbers of the form $a +$ ib, where a, $b \in \mathbb{Z}$. Using the function $\phi$  defined such that
$$\phi (a + ib) = a^{2}+ b^{2},$$
we leave it as an interesting exercise to prove that $\mathbb{Z}[i]$ is a Euclidean domain.  Not every PID is a Euclidean ring.
