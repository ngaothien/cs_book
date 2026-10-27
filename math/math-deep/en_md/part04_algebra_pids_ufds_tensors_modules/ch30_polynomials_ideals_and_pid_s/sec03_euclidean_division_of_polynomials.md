# Euclidean Division of Polynomials


<!-- PAGE 1074 -->
$$Given any nonnull polynomial P(X_{1}, \dots  , X_{n}) = \sum_{(}  k1,...,k\mathbb{N}(n) a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}in$$
$A[X_{1}, \dots  , X_{n}]$, where $n \ge 2, P(X_{1}, \dots  , X$ ) can be $uniquely^{n)\in}$ written as
$$P(X_{1}, \dots  , X_{n}) = \sum^{n}  Q_{kn}(X_{1}, \dots  , X_{n-1})X_{n}^{kn} ,$$
where each polynomial $Q_{kn}(X_{1}, \dots  , X_{n-1})$ is in $A[X_{1}, \dots  , X_{n-1}]$. Even if $A$ is a field, $A[X_{1}, \dots  , X_{n-1}]$ is not a field, which confirms that it is useful (and necessary!) to consider polynomials over rings that are not necessarily fields. It is not difficult to show that $A[X_{1}, \dots  , X_{n}]$ and $A[X_{1}, \dots  , X_{n-1}][X_{n}]$ are isomorphic rings. This way, it is often possible to prove properties of polynomials in several variables $X_{1}, \dots  , X_{n}$, by induction on the number $n$ of variables. For example, given two nonnull polynomials $P(X_{1}, \dots  , X_{n})$ of total degree $p$ and $Q(X_{1}, \dots  , X_{n})$ of total degree $q$, since we assumed that $A$ is an integral domain, we can prove that
$$deg(PQ) = deg(P) + deg(Q),$$
and that $A[X_{1}, \dots  , X_{n}]$ is an integral domain. Next, we will consider the division of polynomials (in one variable).

## 30.3 Euclidean Division of Polynomials

We know that every natural number $n \ge 2$ can be written uniquely as a product of powers of prime numbers and that prime numbers play a very important role in arithmetic. It would be nice if every polynomial could be expressed (uniquely) as a product of “irreducible” factors. This is indeed the case for polynomials over a field. The fact that there is a division algorithm for the natural numbers is essential for obtaining many of the arithmetical properties of the natural numbers. As we shall see next, there is also a division algorithm for polynomials in A[X], when $A$ is a field.

> **Proposition 30.4.** Let $A$ be a ring, let f(X), g(X) $\in$ A[X] be two polynomials of degree $m =$ deg(f) and $n =$ deg(g) with f(X) $\neq  0$, and assume that the leading coefficient $a_{m}$ of f(X) is invertible. Then, there exist unique polynomials q(X) and r(X) in A[X] such that
$$g = fq + randdeg(r) < deg(f) = m.$$

*Proof.* We first prove the existence of $q$ and $r$. Let
$$f = a_{m}X^{m}+ a_{m-1}X^{m-1}+ \cdots  + a_{0},$$
and
$$g = b_{n}X^{n}+ b_{n-1}X^{n-1}+ \cdots  + b_{0}.$$
If $n < m$, then let $q = 0$ and $r = g$. Since deg(g) $<$ deg(f) and $r = g$, we have deg(r) $<$ deg(f).

<!-- PAGE 1075 -->
If $n \ge m$, we proceed by induction on $n$. If $n = 0$, then $g = b_{0}, m = 0, f = a_{0} \neq  0$, and we let $q = a_{0}^{-1} b_{0}$ and $r = 0$. Since deg(r) $=$ deg(0) $= -\infty$ and deg(f) $= deg(a_{0}) = 0$ because $a_{0} \neq  0$, we have deg(r) $<$ deg(f). If $n \ge 1$, since $n \ge m$, note that $g_{1}(X) =$ g(X) - $b_{n}a_{m}^{-1} X^{n-m}f(X)$
$$+ +$$
$$= b_{n}X^{n}+ b_{n-1}X^{n-1}+ \cdots  + b_{0} -b_{n}a_{m}^{-1} X^{n-m}(a_{m}X^{m} a_{m-1}X^{m-1} \cdots  + a_{0})$$
is a polynomial of degree $deg(g_{1}) < n$, since the terms $b_{n}X^{n}$ and $b_{n}a_{m}^{-1} X^{n-m}a_{m}X^{m}$ of degree $n$ cancel out. Now, since $deg(g_{1}) < n$, by the induction hypothesis, we can find $q_{1}$ and $r$ such that
$$g_{1} = fq_{1} + randdeg(r) < deg(f) = m,$$
and thus,
$$g_{1}(X) = g(X) -b_{n}a_{m}^{-1} X^{n-m}f(X) = f(X)q_{1}(X) + r(X),$$
$$+$$
from which, letting q(X) $= b_{n}a_{m}^{-1} X^{n-m}  q_{1}(X)$, we get
$$g = fq + randdeg(r) < m = deg(f).$$
We now prove uniqueness. If
$$g = fq_{1} + r_{1} = fq_{2} + r_{2},$$
with $deg(r_{1}) <$ deg(f) and $deg(r_{2}) <$ deg(f), we get
$$f(q_{1} -q_{2}) = r_{2} -r_{1}.$$
If $q_{2} -q_{1} \neq  0$, since the leading coefficient $a_{m}$ of $f$ is invertible, by Proposition 30.1, we have
$$deg(r_{2} -r_{1}) = deg(f(q_{1} -q_{2})) = deg(f) + deg(q_{2} -q_{1}),$$
and so, $deg(r_{2}-r_{1}) \ge$ deg(f), which contradicts the fact that $deg(r_{1}) <$ deg(f) and $deg(r_{2}) <$ deg(f). Thus, $q_{1} = q_{2}$, and then also $r_{1} = r_{2}$. It should be noted that the proof of Proposition 30.4 actually provides an algorithm for finding the quotient $q$ and the remainder $r$ of the division of $g$ by $f$. This algorithm is called the Euclidean algorithm, or division algorithm. Note that the division of $g$ by $f$ is always possible when $f$ is a monic polynomial, since $1$ is invertible. Also, when $A$ is a field, $a_{m} \neq  0$ is always invertible, and thus, the division can always be performed. We say that $f$ divides $g$ when $r = 0$ in the result of the division $g =$ fq $+ r$. We now draw some important consequences of the existence of the Euclidean algorithm.
