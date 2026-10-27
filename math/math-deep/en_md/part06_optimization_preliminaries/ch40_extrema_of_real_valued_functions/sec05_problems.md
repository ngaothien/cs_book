# Problems


<!-- PAGE 1520 -->

## 40.5 Problems

Problem 40.1. Find the extrema of the function $J(v_{1}, v_{2}) = v_{2}^{2}$ on the subset $U$ given by
$$\mathbb{R}^{2}$$
$$U = {(v_{1}, v_{2}) \in | v_{1}^{2} + v_{2}^{2} -1 = 0}.$$
Problem 40.2. Find the extrema of the function $J(v_{1}, v_{2}) = v_{1} + (v_{2} -1)^{2}$ on the subset $U$ given by
$$\mathbb{R}^{2}$$
$$U = {(v_{1}, v_{2}) \in | v_{1}^{2} = 0}.$$
Problem 40.3. Let $A$ be an $n \times  n$ real symmetric matrix, $B$ an $n \times  n$ symmetric positive definite matrix, and let $b \in \mathbb{R}^{n}$.
$(1)$ Prove that a necessary condition for the function $J$ given by
$$J(v) = \frac{1}{2} v^{\top}Av -b^{\top}v$$
to have an extremum at $u \in U$, with $U$ defined by
$$\mathbb{R}^{n}$$
$$U = {v \in | v^{\top}Bv = 1},$$
is that there is some $\lambda  \in \mathbb{R}$ such that
$$Au -b = \lambda Bu.$$
$(2)$ Prove that there is a symmetric positive definite matrix $S$ such that $B = S^{2}$. Prove that if $b = 0$, then $\lambda$  is an eigenvalue of the symmetric matrix $S^{-1}AS^{-1}$.
$(3)$ Prove that for all $(u, \lambda$ ) $\in U \times \mathbb{R}$, if Au - $b = \lambda$ Bu, then
$$J(v) -J(u) = \frac{1}{2} (v -u)^{\top}(A -\lambda B)(v -u)$$
for all $v \in U$. Deduce that without additional assumptions, it is not possible to conclude that $u$ is an extremum of $J$ on $U$.
Problem 40.4. Let $E$ be a normed vector space, and let $U$ be a subset of $E$ such that for all $u, v \in U$, we have $(1/2)(u + v) \in U$.
$(1)$ Prove that if $U$ is closed, then $U$ is convex. Hint. Every real $\theta  \in (0, 1)$ can be written as
$$\theta  = \sum_{n\ge1}  \alpha_{n} 2^{-n},$$
with $\alpha_{n}  \in {0, 1}$.
$(2)$ Does the result in $(1)$ hold if $U$ is not closed?

<!-- PAGE 1521 -->
Problem 40.5. Prove that the function $f$ with domain dom(f) $=\mathbb{R} -{0}$ given by f(x) $= 1/x^{2}$ has the property that f''(x) $> 0$ for all $x \in$ dom(f), but it is not convex. Why isn’t Proposition 40.12 applicable?
$$\mathbb{R}\mathbb{R}$$
Problem 40.6. $(1)$ Prove that the function $x \mapsto e^{ax}$ (on ) is convex for any $a \in$ .
$$\mathbb{R}\mathbb{R}$$
$(2)$ Prove that the function $x \mapsto x^{a}$ is convex on ${x \in$  | $x > 0}$, for all $a \in$  such that $a \le 0$ or $a \ge 1$.
$$\mathbb{R}$$
Problem 40.7. $(1)$ Prove that the function $x \mapsto |x|^{p}$ is convex on  for all $p \ge 1$.
$(2)$ Prove that the function $x \mapsto$ log $x$ is concave on ${x \in \mathbb{R}$ | $x > 0}$.
$(3)$ Prove that the function $x \mapsto x$ log $x$ is convex on ${x \in \mathbb{R}$ | $x > 0}$.
Problem 40.8. $(1)$ Prove that the function $f$ given by $f(x_{1}, \dots  , x_{n}) = max{x_{1}, \dots  , x_{n}}$ is convex on $\mathbb{R}^{n}$.
$(2)$ Prove that the function $g$ given by $g(x_{1}, \dots  , x_{n}) = log(e^{x1} + \cdots  + e^{xn})$ is convex on $\mathbb{R}^{n}$. Prove that
$$\max{x_{1}, \dots  , x_{n}} \le g(x_{1}, \dots  , x_{n}) \le \max{x_{1}, \dots  , x_{n}} + \log n.$$
Problem 40.9. In Problem 39.6, it was shown that
$$df_{A}(X) = \mathrm{tr}(A^{-1}X)$$
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
for all $n \times  n$ real matrices $X, X_{1}, X_{2}$, where $f$ is the function defined on $GL^{+}(n,\mathbb{R})$ (the $n \times  n$ real invertible matrices of positive determinants), given by
$$f(A) = \log \det(A).$$
Assume that $A$ is symmetric positive definite and that $X$ is symmetric.
$(1)$ Prove that the eigenvalues of $A^{-1}X$ are real (even though $A^{-1}X$ may not be symmetric). Hint. Since $A$ is symmetric positive definite, then so is $A^{-1}$, so we can write $A^{-1} = S^{2}$ for some symmetric positive definite matrix $S$, and then
$$A^{-1}X = S^{2}X = S(SXS)S^{-1}.$$
$(2)$ Prove that the eigenvalues of $(A^{-1}X)^{2}$ are nonnegative. Deduce that
$$D^{2}f(A)(X, X) = -\mathrm{tr}((A^{-1}X)^{2}) < 0$$
for all nonzero symmetric matrices $X$ and SPD matrices $A$. Conclude that the function $X \mapsto$ log det $X$ is strictly concave on the set of symmetric positive definite matrices.

<!-- PAGE 1522 -->
