# Newton's Method for Real Functions of a Real Argument


<!-- PAGE 1523 -->
Chapter $41$ Newton’s Method and Its Generalizations In Chapter $40$ we investigated the problem of determining when a function $J$ : $\Omega \to \mathbb{R}$ defined on some open subset $\Omega$ of a normed vector space $E$ has a local extremum. Proposition 40.1 gives a necessary condition when $J$ is differentiable: if $J$ has a local extremum at $u \in \Omega$ , then we must have
$$J'(u) = 0.$$
Thus we are led to the problem of finding the zeros of the derivative
$$J': \Omega \to E',$$
$$\mathbb{R} \mathbb{R}$$
where E' $= \mathcal{L}(E$; ) is the set of linear continuous functions from $E$ to ; that is, the dual of $E$, as defined in the remark after Proposition 40.8. This leads us to consider the problem in a more general form, namely, given a function $f$ : $\Omega \to Y$ from an open subset $\Omega$ of a normed vector space $X$ to a normed vector space $Y$ , find
$(i)$ Sufficient conditions which guarantee the existence of a zero of the function $f$; that is, an element $a \in \Omega$ such that f(a) $= 0$.
(ii) An algorithm for approximating such an a, that is, a sequence $(x_{k})$ of points of $\Omega$ whose limit is a. In this chapter we discuss Newton’s method and some of it generalizations to give (partial) answers to Problems $(i)$ and (ii).

## 41.1 Newton’s Method for Real Functions of a Real

$$Argument$$
When $X = Y =\mathbb{R}$, we can use Newton’s method to find a zero of a function $f$ : $\Omega \to \mathbb{R}$. We pick some initial element $x_{0} \in \mathbb{R}$ “close enough” to a zero a of $f$, and we define the sequence
$$1523$$

<!-- PAGE 1524 -->
$(x_{k})$ by
$$x_{k+1} = x_{k} - \frac{f(x_{k})}{f'(x_{k})} ,$$
for all $k \ge 0$, provided that f' $(x_{k}) \neq  0$. The idea is to define $x_{k+1}$ as the intersection of the x-axis with the tangent line to the graph of the function $x \mapsto$ f(x) at the point $(x_{k}, f(x_{k}))$. Indeed, the equation of this tangent line is
$$y -f(x_{k}) = f' (x_{k})(x -x_{k}),$$
and its intersection with the x-axis is obtained for $y = 0$, which yields
$$x = x_{k} - \frac{f(x_{k})}{f'(x_{k})} ,$$
as claimed. See Figure 41.1.
$$(x,f(       )x)$$
$$kk$$
$$(xk+1,f(        )x)$$
$$k+1$$
$$\overline{x}\overline{x}\overline{k+1}\overline{x}$$
$$k+2k$$
$$Figure 41.1: The construction of two stages in Newton’s method.$$

> **Example 41.1.** If $\alpha  > 0$ and f(x) $= x^{2}$ - $\alpha$ , Newton’s method yields the sequence
$$x_{k+1} = \frac{1}{2} \begin{pmatrix} \alpha \\ x_{k} + \\ x_{k} \end{pmatrix}$$
$$\sqrt \sqrt$$
to compute the square root $\overline{\alpha}$ of $\alpha$ . It can be shown that the method converges to $\overline{\alpha}$ for any $x_{0} > 0$; see Problem 41.1. Actually, the method also converges when $x_{0} < 0$! Find out what is the limit.
