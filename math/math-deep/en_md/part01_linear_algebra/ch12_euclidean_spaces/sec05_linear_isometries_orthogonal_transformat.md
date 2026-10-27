# Linear Isometries (Orthogonal Transformations)


<!-- PAGE 479 -->
polynomials used in approximation theory and in physics arise by a suitable choice of the weight function $W$. Besides the previous two examples, the Hermite polynomials correspond to W(x) $= e^{-x2}$, the Laguerre polynomials to W(x) $= e^{-x}$, and the Jacobi polynomials to W(x) $= (1$ - $x)^{\alpha}(1 + x)^{\beta}$, with $\alpha , \beta  > -1$. Comprehensive treatments of orthogonal polynomials can be found in Lebedev $[118]$, Sansone $[150]$, and Andrews, Askey and Roy $[3]$. We can also prove the following proposition regarding orthogonal spaces.

> **Proposition 12.11.** Given any nontrivial Euclidean space $E$ of finite dimension $n \ge 1$, for any subspace $F$ of dimension $k$, the orthogonal complement $F^{\perp}$ of $F$ has dimension $n$ - $k$, and $E = F \oplus F^{\perp}$ . Furthermore, we have $F^{\perp \perp} = F$.

*Proof.* From Proposition 12.9, the subspace $F$ has some orthonormal basis $(u_{1}, \dots  , u_{k})$. This linearly independent family $(u_{1}, \dots  , u_{k})$ can be extended to a basis $(u_{1}, \dots  , u_{k}, v_{k+1}, \dots  , v_{n})$, and by Proposition 12.10, it can be converted to an orthonormal basis $(u_{1}, \dots  , u_{n})$, which contains $(u_{1}, \dots  , u_{k})$ as an orthonormal basis of $F$. Now any vector $w = w_{1}u_{1}+\cdots +w_{n}u_{n} \in E$ is orthogonal to $F$ iff $w \cdot  u_{i} = 0$, for every $i$, where $1 \le i \le k$, iff $w_{i} = 0$ for every $i$, where $1 \le i \le k$. Clearly, this shows that $(u_{k+1}, \dots  , u_{n})$ is a basis of $F^{\perp}$ , and thus $E = F \oplus F^{\perp}$ , and $F^{\perp}$ has dimension $n$ - $k$. Similarly, any vector $w = w_{1}u_{1} + \cdots  + w_{n}u_{n} \in E$ is orthogonal to $F^{\perp}$ iff $w \cdot  u_{i} = 0$, for every $i$, where $k + 1 \le i \le n$, iff $w_{i} = 0$ for every $i$, where $k + 1 \le i \le n$. Thus, $(u_{1}, \dots  , u_{k})$ is a basis of $F^{\perp \perp}$ , and $F^{\perp \perp} = F$.

## 12.5 Linear Isometries (Orthogonal Transformations)

In this section we consider linear maps between Euclidean spaces that preserve the Euclidean norm. These transformations, sometimes called rigid motions, play an important role in geometry.

> **Definition 12.5.** Given any two nontrivial Euclidean spaces $E$ and $F$ of the same finite dimension $n$, a function $f$ : $E \to F$ is an orthogonal transformation, or a linear isometry, if it is linear and
$$\|f(u)\|= \|u\|,for all u \in E.$$
Remarks:
$(1) A$ linear isometry is often defined as a linear map such that
$$\|f(v) -f(u)\|= \|v -u\|,$$
for all $u, v \in E$. Since the map $f$ is linear, the two definitions are equivalent. The second definition just focuses on preserving the distance between vectors.
$(2)$ Sometimes, a linear map satisfying the condition of Definition 12.5 is called a metric map, and a linear isometry is defined as a bijective metric map.

<!-- PAGE 480 -->
An isometry (without the word linear) is sometimes defined as a function $f$ : $E \to F$ (not necessarily linear) such that
$$\|f(v) -f(u)\|= \|v -u\|,$$
for all $u, v \in E$, i.e., as a function that preserves the distance. This requirement turns out to be very strong. Indeed, the next proposition shows that all these definitions are equivalent when $E$ and $F$ are of finite dimension, and for functions such that f(0) $= 0$.

> **Proposition 12.12.** Given any two nontrivial Euclidean spaces $E$ and $F$ of the same finite dimension $n$, for every function $f$ : $E \to F$, the following properties are equivalent:
$(1) f$ is a linear map and $\|f(u)\| = \|u\|$, for all $u \in E$;
$(2) \|f(v)$ - $f(u)\| = \|v$ - $u\|$, for all $u, v \in E$, and f(0) $= 0$;
$(3)$ f(u) $\cdot$  f(v) $= u \cdot  v$, for all $u, v \in E$. Furthermore, such a map is bijective.

*Proof.* Clearly, $(1)$ implies $(2)$, since in $(1)$ it is assumed that $f$ is linear. Assume that $(2)$ holds. In fact, we shall prove a slightly stronger result. We prove that if
$$\|f(v) -f(u)\|= \|v -u\|$$
for all $u, v \in E$, then for any vector $\tau  \in E$, the function $g: E \to F$ defined such that
$$g(u) = f(\tau  + u) -f(\tau )$$
for all $u \in E$ is a map satisfying Condition $(2)$, and that $(2)$ implies $(3)$. Clearly, g(0) $= f(\tau$ ) - $f(\tau$ ) $= 0$. Note that from the hypothesis
$$\|f(v) -f(u)\|= \|v -u\|$$
for all $u, v \in E$, we conclude that
$$\|g(v) -g(u)\|= \|f(\tau  + v) -f(\tau ) -(f(\tau  + u) -f(\tau ))\|,$$
$$= \|f(\tau  + v) -f(\tau  + u)\|,$$
$$= \|\tau  + v -(\tau  + u)\|,$$
$$= \|v -u\|,$$
for all $u, v \in E$. Since g(0) $= 0$, by setting $u = 0$ in
$$\|g(v) -g(u)\|= \|v -u\|,$$

<!-- PAGE 481 -->
we get
$$\|g(v)\|= \|v\|$$
for all $v \in E$. In other words, $g$ preserves both the distance and the norm. To prove that $g$ preserves the inner product, we use the simple fact that
$$2u \cdot  v = \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}$$
for all $u, v \in E$. Then since $g$ preserves distance and norm, we have
$$2g(u) \cdot  g(v) = \|g(u)\|^{2}+ \|g(v)\|^{2}-\|g(u) -g(v)\|^{2}$$
$$= \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}$$
$$= 2u \cdot  v,$$
and thus $g(u)\cdot$ g(v) $= u\cdot v$, for all $u, v \in E$, which is $(3)$. In particular, if f(0) $= 0$, by letting $\tau  = 0$, we have $g = f$, and $f$ preserves the scalar product, i.e., $(3)$ holds. Now assume that $(3)$ holds. Since $E$ is of finite dimension, we can pick an orthonormal basis $(e_{1}, \dots  , e_{n})$ for $E$. Since $f$ preserves inner products, $(f(e_{1}), \dots , f(e_{n}))$ is also orthonormal, and since $F$ also has dimension $n$, it is a basis of $F$. Then note that since $(e_{1}, \dots  , e_{n})$ and $(f(e_{1}), \dots  , f(e_{n}))$ are orthonormal bases, for any $u \in E$ we have
$$u = \sum_{i=1}^{n}  (u \cdot  e_{i})e_{i} = \sum_{i=1}^{n}  u_{i}e_{i}$$
and
$$f(u) = \sum_{i=1}^{n}  (f(u) \cdot  f(e_{i}))f(e_{i}),$$
and since $f$ preserves inner products, this shows that
$$f(u) = \sum_{i=1}^{n}  (f(u) \cdot  f(e_{i}))f(e_{i}) = \sum_{i=1}^{n}  (u \cdot  e_{i})f(e_{i}) = \sum_{i=1}^{n}  u_{i}f(e_{i}),$$
which proves that $f$ is linear. Obviously, $f$ preserves the Euclidean norm, and $(3)$ implies $(1)$. Finally, if f(u) $=$ f(v), then by linearity f(v - $u) = 0$, so that $\|f(v$ - $u)\| = 0$, and since $f$ preserves norms, we must have $\|v$ - $u\| = 0$, and thus $u = v$. Thus, $f$ is injective, and since $E$ and $F$ have the same finite dimension, $f$ is bijective.
Remarks:
$(i)$ The dimension assumption is needed only to prove that $(3)$ implies $(1)$ when $f$ is not known to be linear, and to prove that $f$ is surjective, but the proof shows that $(1)$ implies that $f$ is injective.
