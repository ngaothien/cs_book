# Adjoint of a Linear Map


<!-- PAGE 469 -->
where $A = (a_{ij})$. It is immediately verified that $s$ is a linear form. It is easy to check that the unique matrix $Z$ such that
$$\langle Z, A\rangle = s(A)for all A \in M_{n}(\mathbb{R})$$
is the matrix $Z =$ ones(n, $n)$ whose entries are all equal to $1$.

## 12.3 Adjoint of a Linear Map

The existence of the isomorphism $\flat$ : $E \to E^{*}$ is crucial to the existence of adjoint maps. The importance of adjoint maps stems from the fact that the linear maps arising in physical problems are often self-adjoint, which means that $f = f^{*}$ . Moreover, self-adjoint maps can be diagonalized over orthonormal bases of eigenvectors. This is the key to the solution of many problems in mechanics and engineering in general (see Strang $[175])$. Let $E$ be a Euclidean space of finite dimension $n$, and let $f$ : $E \to E$ be a linear map. For every $u \in E$, the map
$$v \mapsto u \cdot  f(v)$$
is clearly a linear form in $E^{*}$, and by Theorem 12.6, there is a unique vector in $E$ denoted by $f^{*} (u)$ such that
$$f^{*} (u) \cdot  v = u \cdot  f(v),$$
for every $v \in E$. The following simple proposition shows that the map $f^{*}$ is linear.

> **Proposition 12.8.** Given a Euclidean space $E$ of finite dimension, for every linear map $f$ : $E \to E$, there is a unique linear map $f^{*}$ : $E \to E$ such that
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E.$$

*Proof.* Given $u_{1}, u_{2} \in E$, since the inner product is bilinear, we have
$$(u_{1} + u_{2}) \cdot  f(v) = u_{1} \cdot  f(v) + u_{2} \cdot  f(v),$$
for all $v \in E$, and
$$(f^{*} (u_{1}) + f^{*} (u_{2})) \cdot  v = f^{*} (u_{1}) \cdot  v + f^{*} (u_{2}) \cdot  v,$$
for all $v \in E$, and since by assumption,
$$f^{*} (u_{1}) \cdot  v = u_{1} \cdot  f(v)andf^{*} (u_{2}) \cdot  v = u_{2} \cdot  f(v),$$
for all $v \in E$. Thus we get
$$(f^{*} (u_{1}) + f^{*} (u_{2})) \cdot  v = (u_{1} + u_{2}) \cdot  f(v) = f^{*} (u_{1} + u_{2}) \cdot  v,$$
for all $v \in E$. Since our inner product is positive definite, this implies that
$$f^{*} (u_{1} + u_{2}) = f^{*} (u_{1}) + f^{*} (u_{2}).$$

<!-- PAGE 470 -->
Similarly,
$$(\lambda u) \cdot  f(v) = \lambda (u \cdot  f(v)),$$
for all $v \in E$, and
$$(\lambda f^{*} (u)) \cdot  v = \lambda (f^{*} (u) \cdot  v),$$
for all $v \in E$, and since by assumption,
$$f^{*} (u) \cdot  v = u \cdot  f(v),$$
for all $v \in E$, we get
$$(\lambda f^{*} (u)) \cdot  v = \lambda (u \cdot  f(v)) = (\lambda u) \cdot  f(v) = f^{*} (\lambda u) \cdot  v$$
for all $v \in E$. Since $\flat$ is bijective, this implies that
$$f^{*} (\lambda u) = \lambda f^{*} (u).$$
Thus, $f^{*}$ is indeed a linear map, and it is unique since $\flat$ is a bijection.

> **Definition 12.4.** Given a Euclidean space $E$ of finite dimension, for every linear map $f$ : $E \to E$, the unique linear map $f^{*}$ : $E \to E$ such that
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E$$
given by Proposition 12.8 is called the adjoint of $f$ (w.r.t. to the inner product). Linear maps $f$ : $E \to E$ such that $f = f^{*}$ are called self-adjoint maps. Self-adjoint linear maps play a very important role because they have real eigenvalues, and because orthonormal bases arise from their eigenvectors. Furthermore, many physical problems lead to self-adjoint linear maps (in the form of symmetric matrices).
Remark: Proposition 12.8 still holds if the inner product on $E$ is replaced by a nondegenerate symmetric bilinear form $\phi$ . Linear maps such that $f^{-1} = f^{*}$, or equivalently
$$f^{*} \circ f = f \circ f^{*} = id,$$
also play an important role. They are linear isometries, or isometries. Rotations are special kinds of isometries. Another important class of linear maps are the linear maps satisfying the property
$$f^{*} \circ f = f \circ f^{*} ,$$
called normal linear maps. We will see later on that normal maps can always be diagonalized over orthonormal bases of eigenvectors, but this will require using a Hermitian inner product (over $\mathbb{C})$.
