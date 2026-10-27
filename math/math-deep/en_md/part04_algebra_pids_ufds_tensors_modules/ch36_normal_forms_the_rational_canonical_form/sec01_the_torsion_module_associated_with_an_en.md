# The Torsion Module Associated With An Endomorphism


<!-- PAGE 1319 -->
Chapter $36$ The Rational Canonical Form and Other Normal Forms

## 36.1 The Torsion Module Associated With An Endo-

$$morphism$$
We saw in Section 7.7 that given a linear map $f$ : $E \to E$ from a $K$-vector space $E$ into itself, we can define a scalar multiplication $\cdot$ : K[X] $\times  E \to E$ that makes $E$ into a K]X]-module. If $E$ is finite-dimensional, this K[X]-module denoted by $E_{f}$ is a torsion module, and the main results of this chapter yield important direct sum decompositions of $E$ into subspaces invariant under $f$. Recall that given any polynomial p(X) $= a_{0}X^{n} + a_{1}X^{n-1} + \cdots  + a_{n}$ with coefficients in the field $K$, we define the linear map p(f): $E \to E$ by
$$p(f) = a_{0}f^{n}+ a_{1}f^{n-1}+ \cdots  + a_{n}id,$$
where $f^{k} = f \circ \cdots  \circ f$, the k-fold composition of $f$ with itself. Note that
$$p(f)(u) = a_{0}f^{n} (u) + a_{1}f^{n-1} (u) + \cdots  + a_{n}u,$$
for every vector $u \in E$. Then, we define the scalar multiplication $\cdot$ : K[X] $\times  E \to E$ by polynomials as follows: for every polynomial p(X) $\in$ K[X], for every $u \in E$,
$$p(X) \cdot  u = p(f)(u).^{1}$$
It is easy to verify that this scalar multiplication satisfies the axioms M1, M2, M3, M4:
$$p \cdot  (u + v) = p \cdot  u + p \cdot  v$$
$$(p + q) \cdot  u = p \cdot  u + q \cdot  u$$
$$(pq) \cdot  u = p \cdot  (q \cdot  u)$$
$$1 \cdot  u = u,$$
$\overline{1}\overline{If} \overline{necessary} \overline{to} \overline{avoid} \overline{confusion,} \overline{we} \overline{use}$ the notion p(X) $\cdot_{f}  u$ instead of p(X) $\cdot  u$.
$$1319$$

<!-- PAGE 1320 -->
for all $p, q \in$ K[X] and all $u, v \in E$. Thus, with this new scalar multiplication, $E$ is a K[X]-module denoted by $E_{f}$. If $p = \lambda$  is just a scalar in $K$ (a polynomial of degree $0)$, then
$$\lambda  \cdot  u = (\lambda id)(u) = \lambda u,$$
which means that $K$ acts on $E$ by scalar multiplication as before. If p(X) $= X$ (the monomial $X)$, then
$$X \cdot  u = f(u).$$
Since $K$ is a field, the ring K[X] is a PID. If $E$ is finite-dimensional, say of dimension $n$, since $K$ is a subring of K[X] and since $E$ is finitely generated over $K$, the K[X]-module $E_{f}$ is finitely generated over K[X]. Furthermore, $E_{f}$ is a torsion module. This follows from the Cayley-Hamilton Theorem (Theorem 7.15), but this can also be shown in an elementary fashion as follows. The space Hom(E, $E)$ of linear maps of $E$ into itself is a vector space of dimension $n^{2}$, therefore the $n^{2}+1$ linear maps
$$id, f, f^{2} , \dots  , f^{n2}$$
are linearly dependent, which yields a nonzero polynomial $q$ such that q(f) $= 0$. We can now translate notions defined for modules into notions for endomorphisms of vector spaces. $1$. To say that $U$ is a submodule of $E_{f}$ means that $U$ is a subspace of $E$ invariant under $f$; that is, f(U) $\subseteq U. 2$. To say that $V$ is a cyclic submodule of $E_{f}$ means that there is some vector $u \in V$ , such that $V$ is spanned by $(u$, f(u), $\dots  , f^{k} (u), \dots$ ). If $E$ has finite dimension $n$, then $V$ is spanned by $(u$, f(u), $\dots  , f^{k} (u))$ for some $k \le n -1$. We say that $V$ is a cyclic subspace for $f$ with generator $u$. Sometimes, $V$ is denoted by Z(u; $f). 3$. To say that the ideal $\mathfrak{a} =$ (p(X)) (with p(X) a monic polynomial) is the annihilator of the submodule $V$ means that p(f)(u) $= 0$ for all $u \in V$ , and we call $p$ the minimal polynomial of $V$ . $4$. Suppose $E_{f}$ is cyclic and let $\mathfrak{a} = (q)$ be its annihilator, where
$$q(X) = X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{1}X + a_{0}.$$
Then, there is some vector $u$ such that $(u$, f(u), $\dots  , f^{k} (u))$ span $E_{f}$, and because $q$ is the minimal polynomial of $E_{f}$, we must have $k =$ n-1. The fact that q(f) $= 0$ implies that
$$f^{n} (u) = -a_{0}u -a_{1}f(u) -\cdots  -a_{n-1}f^{n-1} (u),$$

<!-- PAGE 1321 -->
and so $f$ is represented by the following matrix known as the companion matrix of q(X):
$$U = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{0} \\ 1 & 0 & 0 & \cdots & 0 & -a_{1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{n-2} \\ 0 & 0 & 0 & 1 & a_{n-1} \end{pmatrix} .$$
$$\cdots -$$
It is an easy exercise to prove that the characteristic polynomial $\chi_{U} (X)$ of $U$ gives back q(X):
$$\chi_{U} (X) = q(X).$$
We will need the following proposition to characterize when two linear maps are similar.

> **Proposition 36.1.** Let $f$ : $E \to E$ and f': E' $\to$ E' be two linear maps over the vector spaces $E$ and E'. A linear map $g: E \to$ E' can be viewed as a linear map between the K[X]-modules $E_{f}$ and $E_{f'}$ iff
$$g \circ f = f'\circ g.$$

*Proof.* First, suppose $g$ is K[X]-linear. Then, we have
$$g(p \cdot_{f}  u) = p \cdot_{f'}  g(u)$$
for all $p \in$ K[X] and all $u \in E$, so for $p = X$ we get
$$g(p \cdot_{f}  u) = g(X \cdot_{f}  u) = g(f(u))$$
and
$$p \cdot_{f'}  g(u) = X \cdot_{f'}  g(u) = f' (g(u)),$$
which means that $g \circ f =$ f' $\circ g$. Conversely, if $g \circ f =$ f' $\circ g$, we prove by induction that
$$g \circ f^{n}= f^{'n}\circ g,for all n \ge 1.$$
Indeed, we have
$$g \circ f^{n+1}= g \circ f^{n}\circ f$$
$$= f^{'n}\circ g \circ f$$
$$= f^{'n}\circ f'\circ g$$
$$= f^{'n+1}\circ g,$$

<!-- PAGE 1322 -->
$$establishing the induction step. It follows that for any polynomial p(X) = \sum_{k}  n=0 a_{k}X^{k}, we$$
have
$$g(p(X) \cdot_{f}  u) = g \begin{pmatrix} a_{k}f^{k}(u) \end{pmatrix} \sum_{k=0}^{n}$$
$$= \sum_{k=0}^{n}  a_{k}g \circ f^{k} (u)$$
$$= \sum_{k=0}^{n}  a_{k}f^{'k}\circ g(u)$$
$$= \begin{pmatrix} a_{k}f^{'k} \end{pmatrix} \sum_{k=0}^{n}  (g(u))$$
$$= p(X) \cdot_{f'}  g(u),$$
so, $g$ is indeed K[X]-linear.

> **Definition 36.1.** We say that the linear maps $f$ : $E \to E$ and f': E' $\to$ E' are similar iff there is an isomorphism $g: E \to$ E' such that
$$f'= g \circ f \circ g^{-1},$$
or equivalently,
$$g \circ f = f'\circ g.$$
Then, Proposition 36.1 shows the following fact:

> **Proposition 36.2.** With notation of Proposition 36.1, two linear maps $f$ and f' are similar iff $g$ is an isomorphism between $E_{f}$ and $E_{f'}'$. Later on, we will see that the isomorphism of finitely generated torsion modules can be characterized in terms of invariant factors, and this will be translated into a characterization of similarity of linear maps in terms of so-called similarity invariants. If $f$ and f' are represented by matrices $A$ and A' over bases of $E$ and E', then $f$ and f' are similar iff the matrices $A$ and A' are similar (there is an invertible matrix $P$ such that A' $= PAP^{-1})$. Similar matrices (and endomorphisms) have the same characteristic polynomial. It turns out that there is a useful relationship between $E_{f}$ and the module K[X] $\otimes_{K}  E$. Observe that the map $\cdot$ : K[X] $\times  E \to E$ given by
$$p \cdot  u = p(f)(u)$$
is K-bilinear, so it yields a $K$-linear map $\sigma$ : K[X] $\otimes_{K}  E \to E$ such that
$$\sigma (p \otimes u) = p \cdot  u = p(f)(u).$$

<!-- PAGE 1323 -->
We know from Section 35.6 that K[X] $\otimes_{K}  E$ is a K[X]-module (obtained from the inclusion $K \subseteq$ K[X]), which we will denote by E[X]. Since $E$ is a vector space, E[X] is a free K[X]-module, and if $(u_{1}, \dots  , u_{n})$ is a basis of $E$, then $(1 \otimes u_{1}, \dots  , 1 \otimes u_{n})$ is a basis of E[X]. The free K[X]-module E[X] is not as complicated as it looks. Over the basis $(1 \otimes u_{1}, \dots  , 1 \otimes u_{n})$, every element $z \in$ E[X] can be written uniquely as
$$z = p_{1}(1 \otimes u_{1}) + \cdots  + p_{n}(1 \otimes u_{n}) = p_{1} \otimes u_{1} + \cdots  + p_{n} \otimes u_{n},$$
where $p_{1}, \dots  , p_{n}$ are polynomials in K[X]. For notational simplicity, we may write
$$z = p_{1}u_{1} + \cdots  + p_{n}u_{n},$$
where $p_{1}, \dots  , p_{n}$ are viewed as coefficients in K[X]. With this notation, we see that E[X] is isomorphic to $(K[X])^{n}$, which is easy to understand. Observe that $\sigma$  is K[X]-linear, because
$$\sigma (q(p \otimes u)) = \sigma ((qp) \otimes u)$$
$$= (qp) \cdot  u$$
$$= q(f)(p(f)(u))$$
$$= q \cdot  (p(f)(u))$$
$$= q \cdot  \sigma (p \otimes u).$$
Therefore, $\sigma$  is a linear map of K[X]-modules, $\sigma$ : E[X] $\to E_{f}$. Using our simplified notation, if $z = p_{1}u_{1} + \cdots  + p_{n}u_{n} \in$ E[X], then
$$\sigma (z) = p_{1}(f)(u_{1}) + \cdots  + p_{n}(f)(u_{n}),$$
which amounts to plugging $f$ for $X$ and evaluating. Similarly, $f$ is a K[X]-linear map of $E_{f}$, because
$$f(p \cdot  u) = f(p(f)(u))$$
$$= (fp(f))(u)$$
$$= p(f)(f(u))$$
$$= p \cdot  f(u),$$
where we used the fact that fp(f) $=$ p(f)f because p(f) is a polynomial in $f$. By Proposition 35.40, the linear map $f$ : $E \to E$ induces a K[X]-linear map $\overline{f}\overline{:}$ E[X] $\to$ E[X] such that
$$\overline{f}(p \otimes u) = p \otimes f(u).$$
Observe that we have
$$f(\sigma (p \otimes u)) = f(p(f)(u)) = p(f)(f(u))$$

<!-- PAGE 1324 -->
and
$$\sigma (\overline{f}(p \otimes u)) = \sigma (p \otimes f(u)) = p(f)(f(u)),$$
so we get
$$\sigma  \circ \overline{f} = f \circ \sigma .(*)$$
Using our simplified notation,
$$\overline{f}(p_{1}u_{1} + \cdots  + p_{n}u_{n}) = p_{1}f(u_{1}) + \cdots  + p_{n}f(u_{n}).$$
Define the K[X]-linear map $\psi$ : E[X] $\to$ E[X] by
$$\psi (p \otimes u) = (Xp) \otimes u -p \otimes f(u).$$
Observe that $\psi  = X1_{E[X]} -\overline{f}$, which we abbreviate as $X1-\overline{f}$. Using our simplified notation
$$\psi (p_{1}u_{1} + \cdots  + p_{n}u_{n}) = Xp_{1}u_{1} + \cdots  + Xp_{n}u_{n} -(p_{1}f(u_{1}) + \cdots  + p_{n}f(u_{n})).$$
It should be noted that everything we did in Section 36.1 applies to modules over a commutative ring $A$, except for the statements that assume that A[X] is a PID. So, if $M$ is an A-module, we can define the A[X]-modules $M_{f}$ and M[X] $=$ A[X] $\otimes_{A}  M$, except that $M_{f}$ is generally not a torsion module, and all the results showed above hold. Then, we have the following remarkable result.

> **Theorem 36.3.** (The Characteristic Sequence) Let $A$ be a ring and let $E$ be an A-module. The following sequence of A[X]-linear maps is exact:
$$E/\psi  E/\sigma  E_{f}/ 0/$$
$$0[X][X].$$
This means that $\psi$  is injective, $\sigma$  is surjective, and that $Im(\psi$ ) $=$ Ker $(\sigma$ ). As a consequence, $E_{f}$ is isomorphic to the quotient of E[X] by Im(X1 - $\overline{f})$.

*Proof.* Because $\sigma (1 \otimes u) = u$ for all $u \in E$, the map $\sigma$  is surjective. We have
$$\sigma (X(p \otimes u)) = X \cdot  \sigma (p \otimes u)$$
$$= f(\sigma (p \otimes u)),$$
which shows that
$$\sigma  \circ X1 = f \circ \sigma  = \sigma  \circ \overline{f,}$$
using (*). This implies that
$$\sigma  \circ \psi  = \sigma  \circ (X1 -\overline{f})$$
$$= \sigma  \circ X1 -\sigma  \circ \overline{f}$$
$$= \sigma  \circ \overline{f} -\sigma  \circ \overline{f} = 0,$$

<!-- PAGE 1325 -->
and thus, $Im(\psi$ ) $\subseteq$ Ker $(\sigma$ ). It remains to prove that Ker $(\sigma$ ) $\subseteq Im(\psi$ ). Since the monomials $X^{k}$ form a basis of A[X], by Proposition 35.13 (with the roles of $M$ and $N$ exchanged), every $z \in$ E[X] $=$ A[X] $\otimes_{A}  E$ has a unique expression as
$$z = \sum_{k}  X^{k}\otimes u_{k},$$
for a family $(u_{k})$ of finite support of $u_{k} \in E$. If $z \in$ Ker $(\sigma$ ), then
$$0 = \sigma (z) = \sum_{k}  f^{k} (u_{k}),$$
which allows us to write
$$z = \sum_{k}  X^{k}\otimes u_{k} -1 \otimes 0$$
$$= \sum_{k}  X^{k} \otimes u_{k} -1 \otimes \begin{pmatrix} f^{k}(u_{k}) \end{pmatrix} \sum_{k}$$
$$= \sum_{k}  (X^{k}\otimes u_{k} -1 \otimes f^{k}(u_{k}))$$
$$= \sum_{k}  (X^{k}(1 \otimes u_{k}) -\overline{f}^{k}(1 \otimes u_{k}))$$
$$= \sum_{k}  (X^{k}1 -\overline{f}^{k})(1 \otimes u_{k}).$$
Now, X1 and $\overline{f}$ commute, since
$$(X1 \circ \overline{f})(p \otimes u) = (X1)(p \otimes f(u))$$
$$= (Xp) \otimes f(u)$$
and
$$(\overline{f} \circ X1)(p \otimes u) =\overline{f}((Xp) \otimes u)$$
$$= (Xp) \otimes f(u),$$
so we can write
$$X^{k}1 -\overline{f}^{k}= (X1 -\overline{f}) \begin{pmatrix} (X1)^{j}\overline{f}^{k-j-1} \end{pmatrix} \sum_{j=0}^{k-1}  ,$$
and
$$z = (X1 -\overline{f}) \begin{pmatrix}  \\ (X1)^{j}\overline{f}^{k-j-1} \end{pmatrix} \sum_{k}  \begin{pmatrix} (1 \otimes u_{k}) \end{pmatrix} \sum_{j=0}^{k-1}  ,$$

<!-- PAGE 1326 -->
which shows that $z = \psi (y)$ for some $y \in$ E[X]. Finally, we prove that $\psi$  is injective as follows. We have
$$\psi (z) = \psi \begin{pmatrix} X^{k}\otimes u_{k} \\  \end{pmatrix} \sum_{k}$$
$$= (X1 -\overline{f}) \begin{pmatrix} X^{k}\otimes u_{k} \end{pmatrix} \sum_{k}$$
$$= \sum_{k}  X^{k+1}\otimes (u_{k} -f(u_{k+1})),$$
where $(u_{k})$ is a family of finite support of $u_{k} \in E$. If $\psi (z) = 0$, then
$$\sum_{k}  X^{k+1}\otimes (u_{k} -f(u_{k+1})) = 0,$$
and because the $X^{k}$ form a basis of A[X], we must have
$$u_{k} -f(u_{k+1}) = 0,for all k.$$
Since $(u_{k})$ has finite support, there is a largest $k$, say $m+1$ so that $u_{m+1} = 0$, and then from
$$u_{k} = f(u_{k+1}),$$
we deduce that $u_{k} = 0$ for all $k$. Therefore, $z = 0$, and $\psi$  is injective.
Remark: The exact sequence of Theorem 36.3 yields a presentation of $M_{f}$. Since A[X] is a free A-module, $A[X]\otimes_{A} M$ is a free A-module, but $A[X]\otimes_{A} M$ is generally not a free A[X]-module. However, if $M$ is a free module, then M[X] is a free A[X]-module, since if $(u_{i})_{i\in I}$ is a basis for $M$, then $(1 \otimes u_{i})_{i\in I}$ is a basis for M[X]. This allows us to define the characterisctic polynomial $\chi_{f} (X)$ of an endomorphism of a free module $M$ as
$$\chi_{f} (X) = \det(X1 -\overline{f}).$$
Note that to have a correct definition, we need to define the determinant of a linear map allowing the indeterminate $X$ as a scalar, and this is what the definition of M[X] achieves (among other things). Theorem 36.3 can be used to give a short proof of the Cayley-Hamilton Theorem, see Bourbaki $[25]$ (Chapter III, Section $8$, Proposition $20)$. Proposition 7.10 is still the crucial ingredient of the proof.
