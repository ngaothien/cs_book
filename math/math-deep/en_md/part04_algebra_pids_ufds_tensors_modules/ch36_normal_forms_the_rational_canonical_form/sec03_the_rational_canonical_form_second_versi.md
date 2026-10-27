# The Rational Canonical Form, Second Version


<!-- PAGE 1334 -->

## 36.3 The Rational Canonical Form, Second Version

Let us now translate the Elementary Divisors Decomposition Theorem, Theorem 35.38, in terms of $E_{f}$. We obtain the following result.

> **Theorem 36.14.** (Cyclic Decomposition Theorem, Second Version) Let $f$ : $E \to E$ be an endomorphism on a $K$-vector space of dimension $n$. Then, $E$ is the direct sum of of cyclic subspaces $E_{j} = Z(u_{j}; f)$ for $f$, such that the minimal polynomial of $E_{j}$ is of the form $p_{i}^{ni,j}$, for some irreducible monic polynomials $p_{1}, \dots  , p_{t} \in$ K[X] and some positive integers $n_{i,j}$, such that for each $i = 1, \dots  , t$, there is a sequence of integers
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
with $s_{i} \ge 1$, and where $n_{i,j}$ occurs $m_{i,j} \ge 1$ times, for $j = 1, \dots  , s_{i}$. Furthermore, the monic polynomials $p_{i}$ and the integers $r, t, n_{i,j}, s_{i}, m_{i,j}$ are uniquely determined.
$$Note that there are \mu  = \sum  m_{i,j} cyclic subspaces Z(u_{j}; f). Using bases for the cyclic$$
subspaces $Z(u_{j}; f)$ as in Theorem 36.6, we get the following theorem.

> **Theorem 36.15.** (Rational Canonical Form, Second Version) Let $f$ : $E \to E$ be an endomorphism on a $K$-vector space of dimension $n$. There exist $t$ distinct irreducible monic polynomials $p_{1}, \dots  , p_{t} \in$ K[X] and some positive integers $n_{i,j}$, such that for each $i = 1, \dots  , t$, there is a sequence of integers
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
with $s_{i} \ge 1$, and where $n_{i,j}$ occurs $m_{i,j} \ge 1$ times, for $j = 1, \dots  , s_{i}$, and there is a basis of $E$ such that the matrix $M$ of $f$ is a block matrix of the form
$$M = \begin{pmatrix} M_{1} & 0 & \cdots & 0 & 0 \\ 0 & M_{2} & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & M_{\mu-1} & 0 \\ 0 & 0 & \cdots & 0 & M_{\mu} \end{pmatrix} ,$$
$$where each M_{j} is the companion matrix of some p_{i}^{ni,j}, and \mu  = \sum  m_{i,j}. The monic polyno-$$
mials $p_{1}, \dots  , p_{t}$ and the integers $r, t, n_{i,j}, s_{i}, m_{i,j}$ are uniquely determined The polynomials $p_{i}^{ni,j}$ are called the elementary divisors of $f$ (and $M)$. These polynomials are factors of the minimal polynomial. Example $1$ continued: Recall that f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$ has two nontrivial invariant factors $q_{1} =$ x(x - $2) = q_{2}$. Thus the elementary factors of $f$ are $p_{1} = x = p_{2}$ and $p_{3} = x$ - $2 = p_{4}$. Theorem 36.14 implies that
$$\mathbb{R}^{4}$$
$$= E_{1} \oplus E_{2} \oplus E_{3} \oplus E_{4},$$
