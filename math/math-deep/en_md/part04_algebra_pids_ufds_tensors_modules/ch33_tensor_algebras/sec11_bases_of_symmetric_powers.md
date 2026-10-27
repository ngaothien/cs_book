# Bases of Symmetric Powers


<!-- PAGE 1218 -->

> **Definition 33.23.** Symmetric tensors in $S^{n}(E)$ are called symmetric n-tensors, and tensors of the form $u_{1} \odot \cdots  \odot u_{n}$, where $u_{i} \in E$, are called simple (or decomposable) symmetric n- tensors. Those symmetric n-tensors that are not simple are often called compound symmetric n-tensors. Given a linear maps $f$ : $E \to$ E', since the map $\iota_{\odot}' \circ (f \times  f)$ is bilinear and symmetric, there is a unique linear map $f \odot f$ : $S^{2}(E) \to S^{2}(E')$ making the following diagram commute.
$$\iota \odot  /$$
$$E^{2}S^{2}(E)$$
$$f\times ff\odot f$$
$$(E')^{2} /S^{2}(E').$$
$$\overline{\iota}\overline{'}$$
$$\odot$$
Observe that $f \odot f$ is determined by
$$(f \odot f)(u \odot v) = f(u) \odot f(v).$$

> **Proposition 33.36.** Given any two linear maps $f$ : $E \to$ E' and f': E' $\to$ E'',we have
$$(f'\circ f) \odot (f'\circ f) = (f'\odot f') \circ (f \odot f).$$
By using the proof techniques of Proposition 33.13 $(3)$, we can show the following property of symmetric tensor products.

> **Proposition 33.37.** We have the following isomorphism:
$$\oplus  \sim^{n} M \otimes$$
$$S^{n}(EF)=S^{k}(E)S^{n-k}(F).$$
$$k=0$$
The generalization to the symmetric tensor product $f \odot \cdots  \odot f$ of $n \ge 3$ copies of the linear map $f$ : $E \to$ E' is immediate, and left to the reader.

## 33.11 Bases of Symmetric Powers

The vectors $u_{1} \odot \cdots  \odot u_{m}$ where $u_{1}, \dots  , u_{m} \in E$ generate $S^{m}(E)$, but they are not linearly independent. We will prove a version of Proposition 33.12 for symmetric tensor powers using multisets. Recall that a (finite) multiset over a set $I$ is a function $M$ : I $\to \mathbb{N}$, such that M(i) $\neq  0$
$$\mathbb{N}^{(I)}$$
for finitely many $i \in$ I. The set of all multisets over I is denoted as and we let dom(M) $= {i \in$ I | M(i) $\neq  0}$, the finite set of elements in I that actually occur in $M$. The
$$size of the multiset M is |M| = \sum_{a}  \in A M(a).$$

<!-- PAGE 1219 -->
To explain the idea of the proof, consider the case when $m = 2$ and $E$ has dimension $3$. Given a basis $(e_{1}, e_{2}, e_{3})$ of $E$, we would like to prove that
$$e_{1} \odot e_{1},e_{1} \odot e_{2},e_{1} \odot e_{3},e_{2} \odot e_{2},e_{2} \odot e_{3},e_{3} \odot e_{3}$$
are linearly independent. To prove this, it suffices to show that for any vector space $F$, if $w_{11}, w_{12}, w_{13}, w_{22}, w_{23}, w_{33}$ are any vectors in $F$, then there is a symmetric bilinear map $h: E^{2} \to F$ such that
$$h(e_{i}, e_{j}) = w_{ij},1 \le i \le j \le 3.$$
Because $h$ yields a unique linear map $h_{\odot}: S^{2}(E) \to F$ such that
$$h_{\odot}(e_{i} \odot e_{j}) = w_{ij},1 \le i \le j \le 3,$$
by Proposition 33.4, the vectors
$$e_{1} \odot e_{1},e_{1} \odot e_{2},e_{1} \odot e_{3},e_{2} \odot e_{2},e_{2} \odot e_{3},e_{3} \odot e_{3}$$
are linearly independent. This suggests understanding how a symmetric bilinear function $f$ : $E^{2} \to F$ is expressed in terms of its values $f(e_{i}, e_{j})$ on the basis vectors $(e_{1}, e_{2}, e_{3})$, and this can be done easily. Using bilinearity and symmetry, we obtain $f(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}e_{1} + v_{2}e_{2} + v_{3}e_{3}) = u_{1}v_{1}f(e_{1}, e_{1}) + (u_{1}v_{2} + u_{2}v_{1})f(e_{1}, e_{2})$
$$+ (u_{1}v_{3} + u_{3}v_{1})f(e_{1}, e_{3}) + u_{2}v_{2}f(e_{2}, e_{2})$$
$$+ (u_{2}v_{3} + u_{3}v_{2})f(e_{2}, e_{3}) + u_{3}v_{3}f(e_{3}, e_{3}).$$
Therefore, given $w_{11}, w_{12}, w_{13}, w_{22}, w_{23}, w_{33} \in F$, the function $h$ given by
$$h(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}e_{1} + v_{2}e_{2} + v_{3}e_{3}) = u_{1}v_{1}w_{11} + (u_{1}v_{2} + u_{2}v_{1})w_{12}$$
$$+ (u_{1}v_{3} + u_{3}v_{1})w_{13} + u_{2}v_{2}w_{22}$$
$$+ (u_{2}v_{3} + u_{3}v_{2})w_{23} + u_{3}v_{3}w_{33}$$
is clearly bilinear symmetric, and by construction $h(e_{i}, e_{j}) = w_{ij}$, so it does the job. The generalization of this argument to any $m \ge 2$ and to a space $E$ of any dimension (even infinite) is conceptually clear, but notationally messy. If dim(E) $= n$ and if $(e_{1}, \dots  , e_{n})$
$$is a basis  of E, for any m vectors v_{j} = \sum_{i}  n=1 u_{i,j}e_{i} in E, for any symmetric multilinear map$$
$f$ : $E^{m} \to F$, we have $f(v_{1}, \dots  , v_{m})$
$$= \sum_{\cdot \cdot \cdot+kn}  \sum_{In={1}  \prod_{i1\in I1}  u_{1,i1}!\cdots \prod_{in\in In}  u_{n,in}!!f(e_{1}, \dots  , e_{1}, \dots  , e_{n}, \dots  , e_{n}).$$
$k + =m$ I $\cup \cdot \cdot \cdot \cup ,...,m}$ | ${z$ } | ${z$ } $1 1$ k1 kn
$$Ii\cap Ij=\emptyset , i\neq j, |Ij|=kj$$

<!-- PAGE 1220 -->

> **Definition 33.24.** Given any set $J$ of $n \ge 1$ elements, say $J = {j_{1}, \dots  , j_{n}}$, and given any $m \ge 2$, for any sequence $(k_{1} \dots  , k_{n})$ of natural numbers $k_{i} \in \mathbb{N}$ such that $k_{1} + \cdots  + k_{n} = m$, the multiset $M$ of size $m$
$$M = {j_{1}, \dots  , j_{1}, j_{2}, \dots  , j_{2}, \dots  , j_{n}, \dots  , j_{n}}$$
$$|{z}|{z}|{z}$$
$$k1k2kn$$
is denoted by M(m, $J, k_{1}, \dots  , k_{n})$. Note that $M(j_{i}) = k_{i}$, for $i = 1, \dots  , n$. Given any $k \ge 1$, and any $u \in E$, we denote $u \odot \cdots  \odot u$ as $u^{\odot k}$.
$$|{z}$$
$$k$$
We can now prove the following proposition.

> **Proposition 33.38.** Given a vector space $E$, if $(e_{i})_{i\in I}$ is a basis for $E$, then the family of vectors
$$\begin{pmatrix} e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)} \end{pmatrix} M\in \mathbb{N}(I), |M|=m,$$
$${i1,...,ik}=dom(M)$$
is a basis of the symmetric $m$-th tensor power $S^{m}(E)$.

*Proof.* The proof is very similar to that of Proposition 33.12. First assume that $E$ has finite
$$\mathbb{N}^{(I)}$$
dimension $n$. In this case $I = {1, \dots  , n}$, and any multiset $M \in$ of size |M| $= m$ is of the form M(m, ${1, \dots  , n}, k_{1}, \dots  , k_{n})$, with $k_{i} =$ M(i) and $k_{1} + \cdots  + k_{n} = m$. For any nontrivial vector space $F$, for any family of vectors
$$(w_{M})_{M\in N(I),|M|=m},$$
we show the existence of a symmetric multilinear map $h: S^{m}(E) \to F$, such that for every $\mathbb{N}^{(I)} M \in$ with |M| $= m$, we have
$$h(e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)}) = w_{M},$$
where ${i_{1}, \dots  , i_{k}} =$ dom(M). We define the map $f$ : $E^{m} \to F$ as follows: for any $m$ vectors
$$v_{1}, \dots  , v_{m} \in E we can write v_{k} = \sum_{i}  n=1 u_{i,k}e_{i} for k = 1, \dots  , m and we set$$
$f(v_{1}, \dots  , v_{m})$
$$= \sum_{\cdot \cdot \cdot+kn}  \sum_{In={1}  \prod_{i1\in I1}  u_{1,i1}!\cdots \prod_{in\in In}  u_{n,in}!!w_{M(m,{1,...,n},k1,...,kn)}.$$
$$k1+=mI1\cup \cdot \cdot \cdot \cup ,...,m}$$
$$Ii\cap Ij=\emptyset , i\neq j, |Ij|=kj$$
It is not difficult to verify that $f$ is symmetric and multilinear. By the universal mapping property of the symmetric tensor product, the linear map $f_{\odot}: S^{m}(E) \to F$ such that $f = f_{\odot} \circ \phi$ , is the desired map $h$. Then by Proposition 33.4, it follows that the family
$$\begin{pmatrix} e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)} \end{pmatrix} M\in \mathbb{N}(I), |M|=m,$$
$${i1,...,ik}=dom(M)$$
