# Pairing and Duality Between E and E*


<!-- PAGE 422 -->
For another example of the use of Einstein’s notation, if the vectors $(v_{1}, \dots  , v_{n})$ are linear combinations of the vectors $(u_{1}, \dots  , u_{n})$, with
$$v_{i} = \sum_{j=1}^{n}  a_{ij}u_{j},1 \le i \le n,$$
then the above equations are written as
$$v_{i} = a_{i}^{j}u_{j},1 \le i \le n.$$
Thus, in Einstein’s notation, the $n \times  n$ matrix $(a_{ij})$ is denoted by $(a_{i}^{j})$, a $(1$, 1)-tensor.  Beware that some authors view a matrix as a mapping between coordinates, in which case the matrix $(a_{ij})$ is denoted by $(a_{j}^{i})$.

## 11.2 Pairing and Duality Between E and E*

Given a linear form $u^{*} \in E^{*}$ and a vector $v \in E$, the result $u^{*}(v)$ of applying $u^{*}$ to $v$ is also denoted by $\langle u^{*}, v\rangle$ . This defines a binary operation $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$ satisfying the following properties:
$$\langle u_{1}^{*} + u_{2}^{*}, v\rangle = \langle u_{1}^{*}, v\rangle + \langle u_{2}^{*}, v\rangle$$
$$\langle u^{*}, v_{1} + v_{2}\rangle = \langle u^{*}, v_{1}\rangle + \langle u^{*}, v_{2}\rangle$$
$$\langle \lambda u^{*}, v\rangle = \lambda \langle u^{*}, v\rangle$$
$$\langle u^{*}, \lambda v\rangle = \lambda \langle u^{*}, v\rangle .$$
The above identities mean that $\langle$ -, $-\rangle$ is a bilinear map, since it is linear in each argument. It is often called the canonical pairing between $E^{*}$ and $E$. In view of the above identities, given any fixed vector $v \in E$, the map $eval_{v}$ : $E^{*} \to K$ (evaluation at $v)$ defined such that
$$eval_{v}(u^{*}) = \langle u^{*}, v\rangle = u^{*}(v)for every u^{*}\in E^{*}$$
is a linear map from $E^{*}$ to $K$, that is, $eval_{v}$ is a linear form in $E^{**}$. Again, from the above identities, the map $eval_{E}$ : $E \to E^{**}$, defined such that
$$eval_{E}(v) = eval_{v}for every v \in E,$$
is a linear map. Observe that
$$eval_{E}(v)(u^{*}) = eval_{v}(u^{*}) = \langle u^{*}, v\rangle = u^{*}(v),for all v \in E and all u^{*}\in E^{*}.$$
We shall see that the map $eval_{E}$ is injective, and that it is an isomorphism when $E$ has finite dimension.

<!-- PAGE 423 -->
We now formalize the notion of the set $V^{0}$ of linear equations vanishing on all vectors in a given subspace $V \subseteq E$, and the notion of the set $U^{0}$ of common solutions of a given set $U \subseteq E^{*}$ of linear equations. The duality theorem (Theorem 11.4) shows that the dimensions of $V$ and $V^{0}$ , and the dimensions of $U$ and $U^{0}$ , are related in a crucial way. It also shows that, in finite dimension, the maps $V \mapsto V^{0}$ and $U \mapsto U^{0}$ are inverse bijections from subspaces of $E$ to subspaces of $E^{*}$.

> **Definition 11.3.** Given a vector space $E$ and its dual $E^{*}$, we say that a vector $v \in E$ and a linear form $u^{*} \in E^{*}$ are orthogonal iff $\langle u^{*}, v\rangle = 0$. Given a subspace $V$ of $E$ and a subspace $U$ of $E^{*}$, we say that $V$ and $U$ are orthogonal iff $\langle u^{*}, v\rangle = 0$ for every $u^{*} \in U$ and every $v \in V$ . Given a subset $V$ of $E$ (resp. a subset $U$ of $E^{*})$, the orthogonal $V^{0}$ of $V$ is the subspace $V^{0}$ of $E^{*}$ defined such that
$$V^{0}= {u^{*}\in E^{*}| \langle u^{*}, v\rangle = 0, for every v \in V }$$
(resp. the orthogonal $U^{0}$ of $U$ is the subspace $U^{0}$ of $E$ defined such that
$$U^{0}= {v \in E | \langle u^{*}, v\rangle = 0, for every u^{*}\in U}).$$
The subspace $V^{0} \subseteq E^{*}$ is also called the annihilator of $V$ . The subspace $U^{0} \subseteq E$ annihilated by $U \subseteq E^{*}$ does not have a special name. It seems reasonable to call it the linear subspace (or linear variety) defined by $U$. Informally, $V^{0}$ is the set of linear equations that vanish on $V$ , and $U^{0}$ is the set of common zeros of all linear equations in $U$. We can also define $V^{0}$ by
$$V^{0}= {u^{*}\in E^{*}| V \subseteq \mathrm{Ker} u^{*}}$$
and $U^{0}$ by
$$U^{0}  = \bigcap_{u*\in U}  \mathrm{Ker} u^{*}.$$
Observe that $E^{0} = {0} = (0)$, and ${0}^{0} = E^{*}$.

> **Proposition 11.2.** If $V_{1} \subseteq V_{2} \subseteq E$, then $V_{2}^{0}  \subseteq V_{1}^{0}  \subseteq E^{*}$, and if $U_{1} \subseteq U_{2} \subseteq E^{*}$, then $U_{2}^{0}  \subseteq U_{1}^{0} \subseteq E$. See Figure 11.2.

*Proof.* Indeed, if $V_{1} \subseteq V_{2} \subseteq E$, then for any $f^{*} \in V_{2}^{0}$  we have $f^{*}(v) = 0$ for all $v \in V_{2}$, and thus $f^{*} (v) = 0$ for all $v \in V_{1}$, so $f^{*} \in V_{1}^{0}$  . Similarly, if $U_{1} \subseteq U_{2} \subseteq E^{*}$, then for any $v \in U_{2}^{0}$, we have $f^{*} (v) = 0$ for all $f^{*} \in U_{2}$, so $f^{*} (v) = 0$ for all $f^{*} \in U_{1}$, which means that $v \in U_{1}^{0}$ . Here are some examples.

<!-- PAGE 424 -->
$$V0VV0$$
$$VVV$$
$$2112$$
$$EE*$$
$$UU00$$
$$1U2U$$
$$21$$
$$E*E$$

![Figure 11.2](../../assets/ch11/fig_11_2.png)

**Figure 11.2:** The top pair of figures schematically illustrates the relation if $V_{1} \subseteq V_{2} \subseteq E$, then $V_{2}^{0}  \subseteq V_{1}^{0}  \subseteq E^{*}$, while the bottom pair of figures illustrates the relationship if $U_{1} \subseteq U_{2} \subseteq E^{*}$, then $U_{2}^{0}  \subseteq U_{1}^{0} \subseteq E$.

> **Example 11.2.** Let $E = M_{2}(\mathbb{R})$, the space of real $2\times 2$ matrices, and let $V$ be the subspace of $M_{2}(\mathbb{R})$ spanned by the matrices
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} , \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} , \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} .$$
We check immediately that the subspace $V$ consists of all matrices of the form
$$\begin{pmatrix} b & a \\ a & c \end{pmatrix} ,$$
that is, all symmetric matrices. The matrices
$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$
in $V$ satisfy the equation
$$a_{12} -a_{21} = 0,$$
and all scalar multiples of these equations, so $V^{0}$ is the subspace of $E^{*}$ spanned by the linear form given by $u^{*}(a_{11}, a_{12}, a_{21}, a_{22}) = a_{12}$ - $a_{21}$. By the duality theorem (Theorem 11.4) we have
$$\dim(V^{0} ) = \dim(E) -\dim(V ) = 4 -3 = 1.$$

> **Example 11.3.** The above example generalizes to $E = M_{n}(\mathbb{R})$ for any $n \ge 1$, but this time, consider the space $U$ of linear forms asserting that a matrix $A$ is symmetric; these are the linear forms spanned by the n(n - $1)/2$ equations
$$a_{ij} -a_{ji} = 0,1 \le i < j \le n;$$

<!-- PAGE 425 -->
Note there are no constraints on diagonal entries, and half of the equations
$$a_{ij} -a_{ji} = 0,1 \le i \neq  j \le n$$
are redundant. It is easy to check that the equations (linear forms) for which $i < j$ are linearly independent. To be more precise, let $U$ be the space of linear forms in $E^{*}$ spanned by the linear forms
$$u_{ij}^{*}(a_{11}, \dots  , a_{1n}, a_{21}, \dots  , a_{2n}, \dots  , a_{n1}, \dots  , a_{nn}) = a_{ij} -a_{ji},1 \le i < j \le n.$$
The dimension of $U$ is n(n - $1)/2$. Then the set $U^{0}$ of common solutions of these equations is the space S(n) of symmetric matrices. By the duality theorem (Theorem 11.4), this space has dimension
$$-$$
$$\frac{n(n + 1)}{2} = n^{2}- \frac{n(n1)}{2} .$$
We leave it as an exercise to find a basis of S(n).

> **Example 11.4.** If $E = M_{n}(\mathbb{R})$, consider the subspace $U$ of linear forms in $E^{*}$ spanned by the linear forms
$$u_{ij}^{*}(a_{11}, \dots  , a_{1n}, a_{21}, \dots  , a_{2n}, \dots  , a_{n1}, \dots  , a_{nn}) = a_{ij} + a_{ji},1 \le i < j \le n$$
$$u_{ii}^{*}(a_{11}, \dots  , a_{1n}, a_{21}, \dots  , a_{2n}, \dots  , a_{n1}, \dots  , a_{nn}) = a_{ii},1 \le i \le n.$$
It is easy to see that these linear forms are linearly independent, so dim(U) $=$ n(n $+ 1)/2$.
$$\mathbb{R}$$
The space $U^{0}$ of matrices $A \in M_{n}($ ) satifying all of the above equations is clearly the space Skew(n) of skew-symmetric matrices. By the duality theorem (Theorem 11.4), the dimension of $U^{0}$ is
$$-$$
$$\frac{n(n1)}{2} = n^{2}- \frac{n(n + 1)}{2} .$$
We leave it as an exercise to find a basis of Skew(n).

> **Example 11.5.** For yet another example with $E = M_{n}(\mathbb{R})$, for any $A \in M_{n}(\mathbb{R})$, consider the linear form in $E^{*}$ given by
$$\mathrm{tr}(A) = a_{11} + a_{22} + \cdots  + a_{nn},$$
called the trace of $A$. The subspace $U^{0}$ of $E$ consisting of all matrices $A$ such that tr(A) $= 0$ is a space of dimension $n^{2}$ - $1$. We leave it as an exercise to find a basis of this space. The dimension equations
$$\dim(V ) + \dim(V^{0} ) = \dim(E)$$
$$\dim(U) + \dim(U^{0} ) = \dim(E)$$
are always true (if $E$ is finite-dimensional). This is part of the duality theorem (Theorem 11.4).

<!-- PAGE 426 -->
Remark: In contrast with the previous examples, given a matrix $A \in M_{n}(\mathbb{R})$, the equations asserting that $A^{\top}A =$ I are not linear constraints. For example, for $n = 2$, we have
$$a_{11}^{2} + a_{21}^{2} = 1$$
$$a_{21}^{2} + a_{22}^{2} = 1$$
$$a_{11}a_{12} + a_{21}a_{22} = 0.$$
Remarks:
$(1)$ The notation $V^{0}$ (resp. $U^{0})$ for the orthogonal of a subspace $V$ of $E$ (resp. a subspace $U$ of $E^{*})$ is not universal. Other authors use the notation $V^{\perp}$ (resp. $U^{\perp}$ ). However, the notation $V^{\perp}$ is also used to denote the orthogonal complement of a subspace $V$ with respect to an inner product on a space $E$, in which case $V^{\perp}$ is a subspace of $E$ and not a subspace of $E^{*}$ (see Chapter $12)$. To avoid confusion, we prefer using the notation $V^{0}$ .
$(2)$ Since linear forms can be viewed as linear equations (at least in finite dimension), given a subspace (or even a subset) $U$ of $E^{*}$, we can define the set $\mathcal{Z}(U)$ of common zeros of the equations in $U$ by
$$\mathcal{Z}(U) = {v \in E | u^{*}(v) = 0, for all u^{*}\in U}.$$
Of course $\mathcal{Z}(U) = U^{0}$ , but the notion $\mathcal{Z}(U)$ can be generalized to more general kinds of equations, namely polynomial equations. In this more general setting, $U$ is a set of polynomials in $n$ variables with coefficients in a field $K$ (where $n =$ dim(E)). Sets of the form $\mathcal{Z}(U)$ are called algebraic varieties. Linear forms correspond to the special case where homogeneous polynomials of degree $1$ are considered. If $V$ is a subset of $E$, it is natural to associate with $V$ the set of polynomials in $K[X_{1}, \dots  , X_{n}]$ that vanish on $V$ . This set, usually denoted $\mathcal{I}(V$ ), has some special properties that make it an ideal. If $V$ is a linear subspace of $E$, it is natural to restrict our attention to the space $V^{0}$ of linear forms that vanish on $V$ , and in this case we identify $\mathcal{I}(V$ ) and $V^{0}$ (although technically, $\mathcal{I}(V$ ) is no longer an ideal). For any arbitrary set of polynomials $U \subseteq K[X_{1}, \dots  , X_{n}]$ (resp. subset $V \subseteq E)$, the relationship between $\mathcal{I}(\mathcal{Z}(U))$ and $U$ (resp. $\mathcal{Z}(\mathcal{I}(V$ )) and $V$ ) is generally not simple, even though we always have
$$U \subseteq I(\mathcal{Z}(U))(resp.V \subseteq Z(\mathcal{I}(V ))).$$
However, when the field $K$ is algebraically closed, $then\mathcal{I}(\mathcal{Z}(U))$ is equal to the radical of the ideal $U$, a famous result due to Hilbert known as the Nullstellensatz (see Lang $[113]$ or Dummit and Foote $[55])$. The study of algebraic varieties is the main subject
