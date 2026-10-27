# The Rational Canonical Form


<!-- PAGE 1327 -->

## 36.2 The Rational Canonical Form

Let $E$ be a finite-dimensional vector space over a field $K$, and let $f$ : $E \to E$ be an endomorphism of $E$. We know from Section 36.1 that there is a K[X]-module $E_{f}$ associated with $f$, and that $E_{f}$ is a finitely generated torsion module over the PID K[X]. In this chapter, we show how Theorems from Sections 35.4 and 35.5 yield important results about the structure of the linear map $f$. Recall that the annihilator of a subspace $V$ is an ideal $(p)$ uniquely defined by a monic polynomial $p$ called the minimal polynomial of $V$ . Our first result is obtained by translating the primary decomposition theorem, Theorem 35.19. It is not too surprising that we obtain again Theorem 31.10!

> **Theorem 36.4.** (Primary Decomposition Theorem) Let $f$ : $E \to E$ be a linear map on the finite-dimensional vector space $E$ over the field $K$. Write the minimal polynomial $m$ of $f$ as
$$m = p_{1}^{r1} \cdots  p_{k}^{rk} ,$$
where the $p_{i}$ are distinct irreducible monic polynomials over $K$, and the $r_{i}$ are positive integers. Let
$$W_{i} = \mathrm{Ker} (p_{i}(f)^{ri}),i = 1, \dots  , k.$$
Then
(a) $E = W_{1} \oplus \cdots  \oplus W_{k}$.
$(b)$ Each $W_{i}$ is invariant under $f$ and the projection from $W$ onto $W_{i}$ is given by a polynomial in $f$.
$(c)$ The minimal polynomial of the restriction $f$ | $W_{i}$ of $f$ to $W_{i}$ is $p_{i}^{ri}$ .
$$\mathbb{R}^{4} \mathbb{R}^{4}$$

> **Example 36.1.** Let $f$ : $\to$ be defined as f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$. In terms of the standard basis, $f$ has the matrix representation
$$M = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} .$$
A basic calculation shows that $\chi_{f} (X) = X^{2}(X$ - $2)^{2}$ and that $m_{f}(X) =$ X(X - $2)$. The primary decomposition theorem implies that
$$\mathbb{R}^{4}$$
$$= W_{1} \oplus W_{2},W_{1} = \mathrm{Ker} (M),W_{2} = \mathrm{Ker} (M -2I).$$
Note that Ker $(M)$ corresponds to the eigenspace associated with eigenvalue $0$ and has basis $([-1, 0, 0, 1], [0, -1, 1, 0])$, while Ker $(M$ - 2I) corresponds to the eigenspace associated with eigenvalue $2$ and has basis $([1, 0, 0, 1], [0, 1, 1, 0])$.

<!-- PAGE 1328 -->
Next we apply the Invariant Factors Decomposition Theorem, Theorem 35.31, to $E_{f}$. This theorem says that $E_{f}$ is isomorphic to a direct sum
$$E_{f} \approx K[X]/(p_{1}) \oplus \cdots  \oplus K[X]/(p_{m})$$
of $m \le n$ cyclic modules, where the $p_{j}$ are uniquely determined monic polynomials of degree at least $1$, such that
$$p_{m} | p_{m-1} | \cdots  | p_{1}.$$
Each cyclic module $K[X]/(p_{i})$ is isomorphic to a cyclic subspace for $f$, say $V_{i}$, whose minimal polynomial is $p_{i}$. It is customary to renumber the polynomials $p_{i}$ as follows. The $n$ polynomials $q_{1}, \dots  , q_{n}$ are defined by:
$$($$
$$1if 1 \le j \le n -m$$
$$q_{j}(X) =$$
$$p_{n-j+1}(X)if n -m + 1 \le j \le n.$$
Then we see that
$$q_{1} | q_{2} | \cdots  | q_{n},$$
where the first $n$ - $m$ polynomials are equal to $1$, and we have the direct sum
$$E = E_{1} \oplus \cdots  \oplus E_{n},$$
where $E_{i}$ is a cyclic subspace for $f$ whose minimal polynomial is $q_{i}$. In particular, $E_{i} = (0)$ for $i = 1, \dots  , n$ - $m$. Theorem 35.31 also says that the minimal polynomial of $f$ is $q_{n} = p_{1}$. We sum all this up in the following theorem.

> **Theorem 36.5.** (Cyclic Decomposition Theorem, First Version) Let $f$ : $E \to E$ be an endomorphism on a $K$-vector space of dimension $n$. There exist $n$ monic polynomials $q_{1}, \dots  , q_{n} \in$ K[X] such that
$$q_{1} | q_{2} | \cdots  | q_{n},$$
and $E$ is the direct sum
$$E = E_{1} \oplus \cdots  \oplus E_{n}$$
of cyclic subspaces $E_{i} = Z(u_{i}; f)$ for $f$, such that the minimal polynomial of the restriction of $f$ to $E_{i}$ is $q_{i}$. The polynomials $q_{i}$ satisfying the above conditions are unique, and $q_{n}$ is the minimal polynomial of $f$. In view of translation point $(4)$ at the beginning of Section 36.1, we know that over the basis
$$(u_{i}, f(u_{i}), \dots  , f^{ni-1} (u_{i}))$$

<!-- PAGE 1329 -->
of the cyclic subspace $E_{i} = Z(u_{i}; f)$, with $n_{i} = deg(q_{i})$, the matrix of the restriction of $f$ to $E_{i}$ is the companion matrix of $p_{i}(X)$, of the form
$$\begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{0} \\ 1 & 0 & 0 & \cdots & 0 & -a_{1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{ni-2} \\ 0 & 0 & 0 & 1 & a_{ni-1} \end{pmatrix} .$$
$$\cdots -$$
If we put all these bases together, we obtain a block matrix whose blocks are of the above form. Therefore, we proved the following result.

> **Theorem 36.6.** (Rational Canonical Form, First Version) Let $f$ : $E \to E$ be an endomorphism on a $K$-vector space of dimension $n$. There exist $n$ monic polynomials $q_{1}, \dots  , q_{n} \in$ K[X] such that
$$q_{1} | q_{2} | \cdots  | q_{n},$$
with $q_{1} = \cdots  = q_{n-m} = 1$, and a basis of $E$ such that the matrix $M$ of $f$ is a block matrix of the form
$$M = \begin{pmatrix} M_{n-m+1} & 0 & \cdots & 0 & 0 \\ 0 & M_{n-m+2} & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & M_{n-1} & 0 \\ 0 & 0 & \cdots & 0 & M_{n} \end{pmatrix} ,$$
where each $M_{i}$ is the companion matrix of $q_{i}$. The polynomials $q_{i}$ satisfying the above conditions are unique, and $q_{n}$ is the minimal polynomial of $f$.

> **Definition 36.2.** A matrix $M$ as in Theorem 36.6 is called a matrix in rational form. The polynomials $q_{1}, \dots  , q_{n}$ arising in Theorems 36.5 and 36.6 are called the similarity invariants (or invariant factors) of $f$. Theorem 36.6 shows that every matrix is similar to a matrix in rational form. Such a matrix is unique. Example $1$ continued: We will calculate the rational canonical form for f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$. The difficulty in finding the rational canonical form lies in determining the invariant factors $q_{1}, q_{2}, q_{3}, q_{4}$. As we will shortly discover, the invariant factors of $f$ correspond to the invariant factors of $XI -M$. See Propositions 36.8 and 36.11. The invariant factors of $XI$ - $M$ are found by converting $XI$ - $M$ to Smith normal form. Section 36.5 describes an algorithmic procedure for computing the Smith normal form of a matrix. By applying the methodology of Section 36.5, we find that Smith normal form for

<!-- PAGE 1330 -->
$XI$ - $M$ is
$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & X(X-2) & 0 \\ 0 & 0 & 0 & X(X & 2) \end{pmatrix} .$$
$$-$$
Thus the invariant factors of $f$ are $q_{1} = 1 = q_{2}, q_{3} =$ X(X - $2) = q_{4}$, and Theorem 36.5 implies that
$$\mathbb{R}^{4}$$
$$= E_{1} \oplus E_{2},$$
$$\sim  \mathbb{R} - \sim  \mathbb{R} -$$
where $E_{1} = Z(u_{1}, f) = [X]/(X(X 2))$ and $E_{2} = Z(u_{2}, f) = [X]/(X(X 2))$. The subspace $E_{1}$ has basis $(u_{1}, Mu_{1})$ where $u_{1} = (1, 0, 1, 0)$ and $Mu_{1} = (1, 1, 1, 1)$, while the subspace $E_{2}$ has basis $(u_{2}, Mu_{2})$ where $u_{2} = (0, 0, 1, 0)$ and $Mu_{2} = (0, 1, 1, 0)$. Theorem 36.6 implies that rational canonical form of M(f) is
$$\begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
By Proposition 36.2, two linear maps $f$ and f' are similar iff there is an isomorphism between $E_{f}$ and $E_{f'}'$, and thus by the uniqueness part of Theorem 35.31, iff they have the same similarity invariants $q_{1}, \dots  , q_{n}$.

> **Proposition 36.7.** If $E$ and E' are two finite-dimensional vector spaces and if $f$ : $E \to E$ and f': E' $\to$ E' are two linear maps, then $f$ and f' are similar iff they have the same similarity invariants. The effect of extending the field $K$ to a field $L$ is the object of the next proposition.

> **Proposition 36.8.** Let $f$ : $E \to E$ be a linear map on a $K$-vector space $E$, and let $(q_{1}, \dots  , q_{n})$ be the similarity invariants of $f$. If $L$ is a field extension of $K$ (which means that $K \subseteq L)$, and if $E_{(L)} = L\otimes_{K}  E$ is the vector space obtained by extending the scalars, and $f_{(L)} = 1_{L} \otimes f$ the linear map of $E_{(L)}$ induced by $f$, then the similarity invariants of $f_{(L)}$ are $(q_{1}, \dots  , q_{n})$ viewed as polynomials in L[X].

*Proof.* We know that $E_{f}$ is isomorphic to the direct sum
$$E_{f} \approx K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]),$$
so by tensoring with L[X] and using Propositions 35.12 and 33.13, we get L[X] $\otimes_{K[X]}  E_{f} \approx$ L[X] $\otimes_{K[X]}  (K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]))$
$$\approx L[X] \otimes_{K[X]}  (K[X]/(q_{1}K[X])) \oplus \cdots  \oplus L[X] \otimes_{K[X]}  (K[X]/(q_{n}K[X]))$$
$$\approx (K[X]/(q_{1}K[X])) \otimes_{K[X]}  L[X] \oplus \cdots  \oplus (K[X]/(q_{n}K[X])) \otimes_{K[X]}  L[X].$$

<!-- PAGE 1331 -->
However, by Proposition 35.14, we have isomorphisms
$$(K[X]/(q_{i}K[X])) \otimes_{K[X]}  L[X] \approx L[X]/(q_{i}L[X]),$$
so we get
$$L[X] \otimes_{K[X]}  E_{f} \approx L[X]/(q_{1}L[X]) \oplus \cdots  \oplus L[X]/(q_{n}L[X]).$$
Since $E_{f}$ is a K[X]-module, the L[X] module $L[X]\otimes_{K[X]}  E_{f}$ is the module obtained from $E_{f}$ by the ring extension K[X] $\subseteq$ L[X]. The L-module $E_{(L)} = L\otimes_{K} E$ becomes the L[X]-module $E_{(L)f(L)}$ where
$$f_{(L)} = id_{L} \otimes_{K}  f.$$
We have the following proposition

> **Proposition 36.9.** For any field extension $K \subseteq L$, and any linear map $f$ : $E \to E$ where $E$ is a $K$-vector space, there is an isomorphism between the L[X]-modules L[X] $\otimes_{K[X]}  E_{f}$ and $E_{(L)f(L)}$.

*Proof.* First we define the map $\alpha$ : $L \times  E \to$ L[X] $\otimes_{K[X]}  E_{f}$ by
$$\alpha (\lambda , u) = \lambda  \otimes_{K[X]}  u.$$
It is immediately verified that $\alpha$  is K-bilinear, so we obtain a $K$-linear map $\alpha$ : $L \otimes_{K}  E \to$
$$e$$
L[X] $\otimes_{K[X]}  E_{f}$. Now $E_{(L)} = L \otimes_{K}  E$ is a L[X]-module $(L \otimes_{K}  E)_{f(L)}$, and let us denote this scalar multiplication by $\odot$ . To describe $\odot$ it is enough to define how a monomial $aX^{k} \in$ L[X] acts on a generator $(\lambda  \otimes_{K}  u) \in L \otimes_{K}  E$. We have
$$aX^{k}\odot (\lambda  \otimes_{K}  u) = a(id_{L} \otimes_{K}  f)^{k}(\lambda  \otimes_{K}  u)$$
$$= a(\lambda  \otimes_{K}  f^{k} (u))$$
$$= a\lambda  \otimes_{K}  f^{k} (u).$$
We claim that $\alpha$  is actually L[X]-linear. Indeed, we have
$$e$$
$$\alpha (aX^{k}\odot (\lambda  \otimes_{K}  u)) =\alpha (a\lambda  \otimes_{K}  f^{k}(u))$$
$$e e$$
$$= a\lambda  \otimes_{K[X]}  f^{k} (u),$$
and by the definition of scalar multiplication in the K[X]-module $E_{f}$, we have $f^{k} (u) = X^{k}\cdot_{f} u$, so we have
$$\alpha (aX^{k}\odot (\lambda  \otimes_{K}  u)) = a\lambda  \otimes_{K[X]}  f^{k}(u)$$
$$e$$
$$= a\lambda  \otimes_{K[X]}  X^{k}\cdot_{f}  u$$
$$= X^{k}\cdot  (a\lambda  \otimes_{K[X]}  u)$$
$$= aX^{k}\cdot  (\lambda  \otimes_{K[X]}  u),$$
which shows that $\alpha$  is L[X]-linear.
$$e$$

<!-- PAGE 1332 -->
We also define the map $\beta$  : L[X] $\times  E_{f} \to (L \otimes_{K}  E)_{f(L)}$ by
$$\beta (q(X), u) = q(X) \odot (1 \otimes_{K}  u).$$
Using a computation similar to the computation that we just performed, we can check that $\beta$  is K[X]-bilinear so we obtain a map $\beta$  : L[X] $\otimes_{K[X]}  E_{f} \to (L \otimes_{K}  E)_{f(L)}$. To finish the
$$e$$
proof, it suffices to prove that $\alpha  \circ \beta$  and $\beta  \circ \alpha$  are the identity on generators. We have
$$ee ee$$
$\alpha  \circ \beta$ (q(X) $\otimes_{K[X]}  u) = \alpha$ (q(X) $\odot (1 \otimes_{K}  u)) =$ q(X) $\cdot  (1 \otimes_{K[X]}  u)) =$ q(X) $\otimes_{K[X]}  u, e e  e$ and
$$\beta  \circ \alpha (\lambda  \otimes_{K}  u) =\beta (\lambda  \otimes_{K[X]}  u) = \lambda  \odot (1 \otimes_{K}  u) = \lambda  \otimes_{K}  u,$$
$$ee e$$
which finishes the proof. By Proposition 36.9,
$$E_{(L)f(L)} \approx L[X] \otimes_{K[X]}  E_{f} \approx L[X]/(q_{1}L[X]) \oplus \cdots  \oplus L[X]/(q_{n}L[X]),$$
which shows that $(q_{1}, \dots  , q_{n})$ are the similarity invariants of $f_{(L)}$. Proposition 36.8 justifies the terminology “invariant” in similarity invariants. Indeed, under a field extension $K \subseteq L$, the similarity invariants of $f_{(L)}$ remain the same. This is not true of the elementary divisors, which depend on the field; indeed, an irreducible polynomial $p \in$ K[X] may split over L[X]. Since $q_{n}$ is the minimal polynomial of $f$, the above reasoning also shows that the minimal polynomial of $f_{(L)}$ remains the same under a field extension. Proposition 36.8 has the following corollary.

> **Proposition 36.10.** Let $K$ be a field and let $L \supseteq K$ be a field extension of $K$. For any two square matrices $A$ and $B$ over $K$, if there is an invertible matrix $Q$ over $L$ such that $B = QAQ^{-1}$, then there is an invertible matrix $P$ over $K$ such that $B = PAP^{-1}$ . Recall from Theorem 36.3 that the sequence of K[X]-linear maps
$$E/\psi  E/\sigma  E_{f}/ 0/$$
$$0[X][X]$$
is exact, and as a consequence, $E_{f}$ is isomorphic to the quotient of E[X] by Im(X1 - $\overline{f})$. Furthermore, because $E$ is a vector space, E[X] is a free module with basis $(1\otimes u_{1}, \dots  , 1\otimes u_{n})$, where $(u_{1}, \dots  , u_{n})$ is a basis of $E$, and since $\psi$  is injective, the module Im(X1 - $\overline{f})$ has rank $n$. By Theorem 35.31, we have an isomorphism
$$E_{f} \approx K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]),$$
and by Proposition 35.32, $E[X]/Im(X1$ - $\overline{f})$ is isomorphic to a direct sum
$$E[X]/\mathrm{Im}(X1 -\overline{f}) \approx K[X]/(p_{1}K[X]) \oplus \cdots  \oplus K[X]/(p_{n}K[X]),$$

<!-- PAGE 1333 -->
where $p_{1}, \dots  , p_{n}$ are the invariant factors of Im(X1 - $\overline{f})$ with respect to E[X]. Since $E_{f} \approx E[X]/Im(X1$ - $\overline{f})$, by the uniqueness part of Theorem 35.31 and because the polynomials are monic, we must have $p_{i} = q_{i}$, for $i = 1, \dots  , n$. Therefore, we proved the following crucial fact:
$$Proposition 36.11. For any linear map f : E \to E over a K-vector space \frac{E}{f} of dimension$$
$n$, the similarity invariants of $f$ are equal to the invariant factors of Im(X1- ) with respect to E[X]. Proposition 36.11 is the key to computing the similarity invariants of a linear map. This can be done using a procedure to convert $XI$ - $M$ to its Smith normal form. Propositions 36.11 and 35.37 yield the following result.

> **Proposition 36.12.** For any linear map $f$ : $E \to E$ over a $K$-vector space $E$ of dimension $n$, if $(q_{1}, \dots  , q_{n})$ are the similarity invariants of $f$, for any matrix $M$ representing $f$ with respect to any basis, then for $k = 1, \dots  , n$ the product
$$d_{k}(X) = q_{1}(X) \cdots  q_{k}(X)$$
is the gcd of the $k \times$  k-minors of the matrix $XI$ - $M$. Note that the matrix $XI -M$ is none other than the matrix that yields the characteristic polynomial $\chi_{f} (X) =$ det(XI - $M)$ of $f$.

> **Proposition 36.13.** For any linear map $f$ : $E \to E$ over a $K$-vector space $E$ of dimension $n$, if $(q_{1}, \dots  , q_{n})$ are the similarity invariants of $f$, then the following properties hold:
$(1)$ If $\chi_{f} (X)$ is the characteristic polynomial of $f$, then
$$\chi_{f} (X) = q_{1}(X) \cdots  q_{n}(X).$$
$(2)$ The minimal polynomial m(X) $= q_{n}(X)$ of $f$ divides the characteristic polynomial $\chi_{f} (X)$ of $f$.
$(3)$ The characteristic polynomial $\chi_{f} (X)$ divides $m(X)^{n}$.
$(4) E$ is cyclic for $f$ iff m(X) $= \chi_{f} (X)$.

*Proof.* Property $(1)$ follows from Proposition 36.12 for $k = n$. It also follows from Theorem 36.6 and the fact that for the companion matrix associated with $q_{i}$, the characteristic polynomial of this matrix is also $q_{i}$. Property $(2)$ is obvious from $(1)$. Since each $q_{i}$ divides $q_{i+1}$, each $q_{i}$ divides $q_{n}$, so their product $\chi_{f} (X)$ divides $m(X)^{n} = q_{n}(X)^{n}$. The last condition says that $q_{1} = \cdots  = q_{n-1} = 1$, which means that $E_{f}$ has a single summand. Observe that Proposition 36.13 yields another proof of the Cayley–Hamilton Theorem. It also implies that a linear map is nilpotent iff its characteristic polynomial is $X^{n}$.
