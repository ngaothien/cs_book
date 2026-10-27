# Vector Spaces


<!-- PAGE 69 -->
over all matrices A' of rank at most $k$, for some given $k \ll min{m, n}$. Some advantages of a low-rank approximation are: $1$. Fewer elements are required to represent $A$; namely, k(m $+ n)$ instead of mn. Thus less storage and fewer operations are needed to reconstruct $A. 2$. Often, the process for obtaining the decomposition exposes the underlying structure of the data. Thus, it may turn out that “most” of the significant data are concentrated along some directions called principal directions. Low-rank decompositions of a set of data have a multitude of applications in engineering, including computer science (especially computer vision), statistics, and machine learning. As we will see later in Chapter $23$, the singular value decomposition (SVD) provides a very satisfactory solution to the low-rank approximation problem. Still, in many cases, the data sets are so large that another ingredient is needed: randomization. However, as a first step, linear algebra often yields a good initial solution. We will now be more precise as to what kinds of operations are allowed on vectors. In the late 1880’s, the notion of a vector space emerged as a convenient and unifying framework for working with “linear” objects. An axiomatic definition of vector spaces was first given by Peano in $1888$ and was anticipated by Grassmann.

## 3.2 Vector Spaces

$$\mathbb{R}^{n}$$
For every $n \ge 1$, let be the set of $n$-tuples $x = (x_{1}, \dots  , x_{n})$. Addition can be extended to $\mathbb{R}^{n}$ as follows: $(x_{1}, \dots  , x_{n}) + (y_{1}, \dots  , y_{n}) = (x_{1} + y_{1}, \dots  , x_{n} + y_{n})$.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
We can also define an operation $\cdot$ :  $\times \to$ as follows: $\lambda  \cdot  (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n})$. The resulting algebraic structure has some interesting properties, those of a vector space. However, keep in mind that vector spaces are not just algebraic
$$objects; they are also geometric objects.$$
Vector spaces are defined as follows.

> **Definition 3.1.** Given a field $K$ (with addition $+$ and multiplication *), a vector space over $K$ (or $K$-vector space) is a set $E$ (of vectors) together with two operations $+_{E}$ : $E \times  E \to E$ (called vector addition),and $\cdot_{E}$  : $K \times  E \to E$ (called scalar multiplication) satisfying the following conditions for all $\alpha , \beta  \in K$ and all $u, v \in E$;
(V0) $E$ is an abelian group w.r.t. $+_{E}$, with identity element $0_{E}$;

<!-- PAGE 70 -->
(V1) $\alpha  \cdot_{E}  (u +_{E} v) = (\alpha  \cdot_{E}  u) +_{E} (\alpha  \cdot_{E}  v)$;
(V2) $(\alpha  + \beta$ ) $\cdot_{E}  u = (\alpha  \cdot_{E}  u) +_{E} (\beta  \cdot_{E}  u)$;
(V3) $(\alpha$  * $\beta$ ) $\cdot_{E}  u = \alpha  \cdot_{E}  (\beta  \cdot_{E}  u)$;
(V4) $1 \cdot_{E}  u = u$. In (V1), $+$ denotes addition in the field $K$, and in (V3), * denotes multiplication in $K$. Given $\alpha , \beta  \in K$ and $v \in E$, for simplicity of notation, the element $\alpha  \cdot_{E}  v$ is denoted by $\alpha v$ and $\alpha$  * $\beta$  by $\alpha \beta$ . The field $K$ is often called the field of scalars. Unless specified otherwise or unless we are dealing with several different fields, in the rest of this chapter, we assume that all $K$-vector spaces are defined with respect to a fixed field $K$. Thus, we will refer to a $K$-vector space simply as a vector space. In most cases, the field $K$ will be the field $\mathbb{R}$ of reals. From (V0), a vector space always contains the null vector $0_{E}$, and thus is nonempty. From (V1), we get $\alpha  \cdot_{E}  0_{E} = 0_{E}$, and $\alpha  \cdot_{E}  (-_{E}v) = -_{E}(\alpha  \cdot_{E}  v)$. From (V2), we get $0 \cdot_{E}  v = 0_{E}$, and $(-\alpha$ ) $\cdot_{E}  v = -_{E}(\alpha  \cdot_{E}  v)$. Another important consequence of the axioms is the following fact:

> **Proposition 3.1.** For any $u \in E$ and any $\lambda  \in K$, if $\lambda  \neq  0$ and $\lambda  \cdot_{E}  u = 0_{E}$, then $u = 0_{E}$.

*Proof.* Indeed, since $\lambda  \neq  0$, it has a multiplicative inverse $\lambda^{-1}$ , so from $\lambda  \cdot_{E}  u = 0_{E}$, we get
$$\lambda^{-1} \cdot_{E}  (\lambda  \cdot_{E}  u) = \lambda^{-1} \cdot_{E}  0_{E}.$$
However, we just observed that $\lambda^{-1} \cdot_{E}  0_{E} = 0_{E}$, and from (V3) and (V4), we have
$$\lambda^{-1} \cdot_{E}  (\lambda  \cdot_{E}  u) = (\lambda^{-1} \lambda ) \cdot_{E}  u = 1 \cdot_{E}  u = u,$$
and we deduce that $u = 0_{E}$.
Remark: One may wonder whether axiom (V4) is really needed. Could it be derived from
$$\mathbb{R}^{n}$$
the other axioms? The answer is no. For example, one can take $E =$ and define $\mathbb{R} \mathbb{R}^{n} \mathbb{R}^{n} \cdot$ :  $\times \to$ by
$$\lambda  \cdot  (x_{1}, \dots  , x_{n}) = (0, \dots  , 0)$$
$$\mathbb{R}^{n} \mathbb{R}$$
for all $(x_{1}, \dots  , x_{n}) \in$ and all $\lambda  \in$ . Axioms (V0)–(V3) are all satisfied, but (V4) fails. Less trivial examples can be given using the notion of a basis, which has not been defined yet. The field $K$ itself can be viewed as a vector space over itself, addition of vectors being addition in the field, and multiplication by a scalar being multiplication in the field.

<!-- PAGE 71 -->
One quickly realizes that although it is of course important to distinguish between addition $+_{E}$ in $E$ with addition $+$ in the field $K$, the zero vector $0_{E}$ in $E$ with zero $0$ in the field, and multiplication $\cdot_{E}$  by a scalar (in the field $K)$ with multiplication * (or $\cdot$ ) in the field, using all these subscripts becomes a notational burden. Thus, unless confusion may arise, we denote addition in $E$ and $K$ by the same symbol $+$, the zero in $E$ and in $K$ by $0$, and scalar multiplication by $\cdot$  (we even write $\alpha u$ instead of $\alpha  \cdot u)$. Systematic use of different symbols for denoting scalars (say $\alpha , \beta , \gamma , \delta , \lambda$ ) and vectors say $(u, v, x, y, z)$ is usually enough to avoid confusion. To avoid confusing zero in $E$ and zero in $K$, we can use $0$ for the zero vector.

> **Example 3.1.** $1$. The fields $\mathbb{R}$ and $\mathbb{C}$ are vector spaces over $\mathbb{R}$.
$$\mathbb{R}^{n}  \mathbb{C}^{n}  \mathbb{R}$$
$2$. The groups and are vector spaces over , with scalar multiplication given by
$$\lambda (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n}),$$
$$\mathbb{R}\mathbb{R}^{n} \mathbb{C}^{n} \mathbb{C}^{n}$$
for any $\lambda  \in$  and with $(x_{1}, \dots  , x_{n}) \in$ or $(x_{1}, \dots  , x_{n}) \in$ , and is a vector space over $\mathbb{C}$ with scalar multiplication as above, but with $\lambda  \in \mathbb{C}. 3$. The ring $\mathbb{R}[X]_{n}$ of polynomials of degree at most $n$ with real coefficients is a vector space over $\mathbb{R}$, and the ring $\mathbb{C}[X]_{n}$ of polynomials of degree at most $n$ with complex coefficients is a vector space $over\mathbb{C}$, with scalar multiplication $\lambda \cdot$ P(X) of a polynomial
$$P(X) = a_{0}X^{m}+ a_{1}X^{m-1}+ \cdots  + a_{m-1}X + a_{m}$$
(with $a_{i} \in \mathbb{R}$ or $a_{i} \in \mathbb{C})$ by the scalar $\lambda$  (in $\mathbb{R}$ or $\mathbb{C})$, with $m \le n$, given by
$$\lambda  \cdot  P(X) = \lambda a_{0}X^{m}+ \lambda a_{1}X^{m-1}+ \cdots  + \lambda a_{m-1}X + \lambda a_{m}.$$
$4$. The $ring\mathbb{R}[X]$ of all polynomials with real coefficients is a vector space $over\mathbb{R}$, and the ring $\mathbb{C}[X]$ of all polynomials with complex coefficients is a vector space over $\mathbb{C}$, with the same scalar multiplication as above. $5$. The ring of $n \times  n$ matrices $M_{n}(\mathbb{R})$ is a vector space over $\mathbb{R}. 6$. The set of $m \times  n$ matrices $M_{m,n}(\mathbb{R})$ is a vector space over $\mathbb{R}. 7$. The ring $\mathcal{C}(a, b)$ of continuous functions $f$ : (a, $b) \to \mathbb{R}$ is a vector space over $\mathbb{R}$, with the scalar multiplication $\lambda f$ of a function $f$ : (a, $b) \to \mathbb{R}$ by a scalar $\lambda  \in \mathbb{R}$ given by
$$(\lambda f)(x) = \lambda f(x),for all x \in (a, b).$$
