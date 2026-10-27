# Multisets


<!-- PAGE 1067 -->
Chapter $30$ Polynomials, Ideals and PID’s

## 30.1 Multisets

This chapter contains a review of polynomials and their basic properties. First, multisets are defined. Polynomials in one variable are defined next. The notion of a polynomial function in one argument is defined. Polynomials in several variable are defined, and so is the notion of a polynomial function in several arguments. The Euclidean division algorithm is presented, and the main consequences of its existence are derived. Ideals are defined, and the characterization of greatest common divisors of polynomials in one variables (gcd’s) in terms of ideals is shown. We also prove the Bezout identity. Next, we consider the factorization of polynomials in one variables into irreducible factors. The unique factorization of polynomials in one variable into irreducible factors is shown. Roots of polynomials and their multiplicity are defined. It is shown that a nonnull polynomial in one variable and of degree $m$ over an integral domain has at most $m$ roots. The chapter ends with a brief treatment of polynomial interpolation: Lagrange, Newton, and Hermite interpolants are introduced. In this chapter, it is assumed that all rings considered are commutative. Recall that a
(commutative) ring $A$ is an integral domain (or an entire ring) if $1 \neq  0$, and if ab $= 0$, then either $a = 0$ or $b = 0$, for all a, $b \in A$. This second condition is equivalent to saying that if $a \neq  0$ and $b \neq  0$, then ab $\neq  0$. Also, recall that $a \neq  0$ is not a zero divisor if ab $\neq  0$ whenever $b \neq  0$. Observe that a field is an integral domain. Our goal is to define polynomials in one or more indeterminates (or variables) $X_{1}, \dots  , X_{n}$, with coefficients in a ring $A$. This can be done in several ways, and we choose a definition that has the advantage of extending immediately from one to several variables. First, we need to review the notion of a (finite) multiset.

> **Definition 30.1.** Given a set $I$, a (finite) multiset over I is any function $M$ : I $\to \mathbb{N}$ such that M(i) $\neq  0$ for finitely many $i \in$ I. The multiset $M$ such that M(i) $= 0$ for all $i \in$ I is the empty multiset, and it is denoted by $0$. If M(i) $= k \neq  0$, we say that $i$ is a member of $M$ of multiplicity $k$. The union $M_{1} + M_{2}$ of two multisets $M_{1}$ and $M_{2}$ is defined such that $(M_{1} + M_{2})(i) = M_{1}(i) + M_{2}(i)$, for every $i \in$ I. If I is finite, say $I = {1, \dots  , n}$, the multiset
$$1067$$
