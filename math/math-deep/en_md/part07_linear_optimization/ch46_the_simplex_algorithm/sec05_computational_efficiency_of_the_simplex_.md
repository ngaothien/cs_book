# Computational Efficiency of the Simplex Method


<!-- PAGE 1634 -->
is always possible. Otherwise, $(\gamma_{K*} )_{i}^{j} = 0$ for all non-slack variables, so we detected that the ith equation is redundant and we can delete it. Other presentations of the tableau method can be found in Bertsimas and Tsitsiklis $[21]$ and Papadimitriou and Steiglitz $[139]$.

## 46.5 Computational Efficiency of the Simplex Method

Let us conclude with a few comments about the efficiency of the simplex algorithm. In practice, it was observed by Dantzig that for linear programs with $m < 50$ and $m+n < 200$, the simplex algorithms typically requires less than $3m/2$ iterations, but at most 3m iterations. This fact agrees with more recent empirical experiments with much larger programs that show that the number iterations is bounded by 3m. Thus, it was somewhat of a shock in $1972$ when Klee and Minty found a linear program with $n$ variables and $n$ equations for which the simplex algorithm with Dantzig’s pivot rule requires requires $2^{n}$ - $1$ iterations. This program (taken from Chvatal $[40]$, page $47)$ is reproduced below:
$$maximize \sum_{j=1}^{n}  10^{n-j}x_{j}$$
$$subject to$$
$$\begin{pmatrix} 2 & 10^{i-j}x_{j} \end{pmatrix} \sum_{j=1}^{i-1}  + x_{i} \le 100^{i-1}$$
$$x_{j} \ge 0,$$
for $i = 1, \dots  , n$ and $j = 1, \dots  , n$. If $p =$ max(m, $n)$, then, in terms of worse case behavior, for all currently known pivot rules, the simplex algorithm has exponential complexity in $p$. However, as we said earlier, in practice, nasty examples such as the Klee–Minty example seem to be rare, and the number of iterations appears to be linear in $m$. Whether or not a pivot rule (a clairvoyant rule) for which the simplex algorithms runs in polynomial time in terms of $m$ is still an open problem. The Hirsch conjecture claims that there is some pivot rule such that the simplex algorithm finds an optimal solution in O(p) steps. The best bound known so far due to Kalai and Kleitman is $m^{1+lnn} = (2n)^{lnm}$. For more on this topic, see Matousek and Gardner $[127]$ (Section 5.9) and Bertsimas and Tsitsiklis $[21]$ (Section 3.7). Researchers have investigated the problem of finding upper bounds on the expected number of pivoting steps if a randomized pivot rule is used. Bounds better than $2^{m}$ (but of course, not polynomial) have been found.
