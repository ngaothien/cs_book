# Transpose of a Linear Map and of a Matrix


<!-- PAGE 436 -->
We leave as an exercise the fact that every subspace V̸ $= E$ of a vector space $E$ is the intersection of all hyperplanes that contain $V$ . We now consider the notion of transpose of a linear map and of a matrix.

## 11.6 Transpose of a Linear Map and of a Matrix

Given a linear map $f$ : $E \to F$, it is possible to define a map $f^{\top}$ : $F^{*} \to E^{*}$ which has some interesting properties.

> **Definition 11.5.** Given a linear map $f$ : $E \to F$, the transpose $f^{\top}$ : $F^{*} \to E^{*}$ of $f$ is the linear map defined such that
$$f^{\top} (v^{*}) = v^{*}\circ f,for every v^{*}\in F^{*} ,$$
as shown in the diagram below:
$$EF$$
$$\overline{B}^{f}\overline{B}$$
$$\overline{B} B$$
$$BB$$
$$BB^{v*}$$
$$f\top (v*)$$
$$K.$$
Equivalently, the linear map $f^{\top}$ : $F^{*} \to E^{*}$ is defined such that
$$\langle v^{*}, f(u)\rangle = \langle f^{\top} (v^{*}), u\rangle ,(*)$$
for all $u \in E$ and all $v^{*} \in F^{*}$ . It is easy to verify that the following properties hold:
$$(f + g)^{\top}= f^{\top} + g^{\top}$$
$$(g \circ f)^{\top}= f^{\top} \circ g^{\top}$$
$$id_{E}^{\top} = id_{E*}.$$
 Note the reversal of composition on the right-hand side of $(g \circ f)^{\top} = f^{\top} \circ g^{\top}$. The equation $(g \circ f)^{\top} = f^{\top} \circ g^{\top}$ implies the following useful proposition.

> **Proposition 11.8.** If $f$ : $E \to F$ is any linear map, then the following properties hold:
$(1)$ If $f$ is injective, then $f^{\top}$ is surjective.
$(2)$ If $f$ is surjective, then $f^{\top}$ is injective.

<!-- PAGE 437 -->

*Proof.* If $f$ : $E \to F$ is injective, then it has a retraction $r: F \to E$ such that $r \circ f = id_{E}$, and if $f$ : $E \to F$ is surjective, then it has a section $s: F \to E$ such that $f \circ s = id_{F}$. Now if $f$ : $E \to F$ is injective, then we have
$$(r \circ f)^{\top}= f^{\top} \circ r^{\top}= id_{E*},$$
which implies that $f^{\top}$ is surjective, and if $f$ is surjective, then we have
$$(f \circ s)^{\top}= s^{\top}\circ f^{\top} = id_{F*},$$
which implies that $f^{\top}$ is injective. The following proposition gives a natural interpretation of the dual $(E/U)^{*}$ of a quotient space $E/U$.

> **Proposition 11.9.** For any subspace $U$ of a vector space $E$, if $p: E \to E/U$ is the canonical surjection onto $E/U$, then $p^{\top}$ is injective and
$$\mathrm{Im}(p^{\top}) = U^{0}= (\mathrm{Ker} (p))^{0}.$$
Therefore, $p^{\top}$ is a linear isomorphism between $(E/U)^{*}$ and $U^{0}$ .

*Proof.* Since $p$ is surjective, by Proposition 11.8, the map $p^{\top}$ is injective. Obviously, $U =$ Ker $(p)$. Observe that $Im(p^{\top})$ consists of all linear forms $\psi  \in E^{*}$ such that $\psi  = \phi  \circ p$ for some $\phi  \in (E/U)^{*}$, and since Ker $(p) = U$, we have $U \subseteq$ Ker $(\psi$ ). Conversely for any linear form $\psi  \in E^{*}$, if $U \subseteq$ Ker $(\psi$ ), then $\psi$  factors through $E/U$ as $\psi  = \overline{\psi} \circ p$ as shown in the following commutative diagram
$$EE/U$$
$$\overline{C}^{p}\overline{C}$$
$$\overline{C} C$$
$$CC$$
$$CC$$
$$\psi C^{\psi}!$$
$$K,$$
where $\overline{\psi}: E/U \to K$ is given by
$$\overline{\psi}(\overline{v}) = \psi (v),v \in E,$$
$$where \overline{v} \in E/U denotes the equivalence class of v \in E. \frac{The}{v'} map \overline{\psi} does  not depend on the$$
representative chosen in the equivalence class $\overline{v}$, since if $=\overline{v}$, that is v' - $v = u \in U$, then $\psi$ (v') $= \psi (v + u) = \psi (v) + \psi (u) = \psi (v) + 0 = \psi (v)$. Therefore, we have
$$\mathrm{Im}(p^{\top}) = {\phi  \circ p | \phi  \in (E/U)^{*}}$$
$$= {\psi : E \to K | U \subseteq \mathrm{Ker} (\psi )}$$
$$= U^{0} ,$$
which proves our result.

<!-- PAGE 438 -->
Proposition 11.9 yields another proof of part $(b)$ of the duality theorem (theorem 11.4) that does not involve the existence of bases (in infinite dimension).

> **Proposition 11.10.** For any vector space $E$ and any subspace $V$ of $E$, we have $V^{00} = V$ .

*Proof.* We begin by observing that $V^{0} = V^{000}$. This is because, for any subspace $U$ of $E^{*}$, we have $U \subseteq U^{00}$, so $V^{0} \subseteq V^{000}$. Furthermore, $V \subseteq V^{00}$ holds, and for any two subspaces $M, N$ of $E$, if $M \subseteq N$ then $N^{0} \subseteq N^{0}$, so we get $V^{000} \subseteq V^{0}$. Write $V_{1} = V^{00}$, so that $V_{1}^{0} = V^{000} = V^{0}$. We wish to prove that $V_{1} = V$ . Since $V \subseteq V_{1} = V^{00}$ , the canonical projection $p_{1}$ : $E \to E/V_{1}$ factors as $p_{1} = f \circ p$ as in the diagram below,
$$EE/V$$
$$\overline{C}^{p}\overline{C}$$
$$\overline{C} C$$
$$CC$$
$$CCf$$
$$p1C$$
$$!$$
$$E/V_{1}$$
where $p: E \to E/V$ is the canonical projection onto $E/V$ and $f$ : $E/V \to E/V_{1}$ is the quotient map induced by $p_{1}$, with $f(\overline{u}_{E/V}$ ) $= p_{1}(u) = \overline{u}_{E/V1}$, for all $u \in E$ (since $V \subseteq V_{1}$, if $u$ - u' $= v \in V$ , then $u$ - u' $= v \in V_{1}$, so $p_{1}(u) = p_{1}(u'))$. Since $p_{1}$ is surjective, so is $f$. We wish to prove that $f$ is actually an isomorphism, and for this, it is enough to show that $f$ is injective. By transposing all the maps, we get the commutative diagram
$$\top$$
$$E^{*}(E/V )^{*}$$
$$\overline{d}^{p}\overline{HHHHHHHHHH}$$
$$f\top$$
$$p\top$$
$$1$$
$$(E/V_{1})^{*},$$
but by Proposition 11.9, the maps $p^{\top}: (E/V )^{*} \to V^{0}$ and $p_{1}^{\top}$ : $(E/V_{1})^{*} \to V_{1}^{0}$ are isomorphism, and since $V^{0} = V_{1}^{0}$ , we have the following diagram where both $p^{\top}$ and $p_{1}^{\top}$ are isomorphisms:
$$\top$$
$$V^{0} (E/V )^{*}$$
$$\overline{d}^{p}\overline{HHHHHHHHHH}$$
$$f\top$$
$$p\top$$
$$1$$
$$(E/V_{1})^{*}.$$
Therefore, $f^{\top} = (p^{\top})^{-1}\circ p_{1}^{\top}$ is an isomorphism. We claim that this implies that $f$ is injective. If $f$ is not injective, then there is some $x \in E/V$ such that x̸ $= 0$ and f(x) $= 0$, so for every $\phi  \in (E/V_{1})^{*}$, we have $f^{\top} (\phi )(x) = \phi$ (f(x)) $= 0$. However, there is linear form $\psi  \in (E/V )^{*}$ such that $\psi (x) = 1$, so $\psi  \neq  f^{\top} (\phi$ ) for all $\phi  \in (E/V_{1})^{*}$, contradicting the fact that $f^{\top}$ is surjective. To find such a linear form $\psi$ , pick any supplement $W$ of Kx in $E/V$ , so that $E/V =$ Kx $\oplus W (W$ is a hyperplane in $E/V$ not containing $x)$, and define $\psi$  to be zero

<!-- PAGE 439 -->
on $W$ and $1$ on $x.^{1}$ Therefore, $f$ is injective, and since we already know that it is surjective, it is bijective. This means that the canonical map $f$ : $E/V \to E/V_{1}$ with $V \subseteq V_{1}$ is an isomorphism, which implies that $V = V_{1} = V^{00}$ (otherwise, if $v \in V_{1}$ - $V$ , then $p_{1}(v) = 0$, so f(p(v)) $= p_{1}(v) = 0$, but p(v) $\neq  0$ since $v \in / V$ , and $f$ is not injective). The following proposition shows the relationship between orthogonality and transposition.

> **Proposition 11.11.** Given a linear map $f$ : $E \to F$, for any subspace $V$ of $E$, we have
$$f(V )^{0}= (f^{\top})^{-1}(V^{0}) = {w^{*}\in F^{*}| f^{\top}(w^{*}) \in V^{0}}.$$
As a consequence,
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}.$$
We also have
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}.$$

*Proof.* We have
$$\langle w^{*}, f(v)\rangle = \langle f^{\top} (w^{*}), v\rangle ,$$
for all $v \in E$ and all $w^{*} \in F^{*}$ , and thus, we have $\langle w^{*}, f(v)\rangle = 0$ for every $v \in V$ , i.e. $w^{*} \in$ f(V $)^{0}$ iff $\langle f^{\top}(w^{*}), v\rangle = 0$ for every $v \in V$ iff $f^{\top}(w^{*}) \in V^{0}$, i.e. $w^{*} \in (f^{\top})^{-1}(V^{0})$, proving that
$$f(V )^{0}= (f^{\top})^{-1}(V^{0}).$$
Since we already observed that $E^{0} = (0)$, letting $V = E$ in the above identity we obtain that
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}.$$
From the equation
$$\langle w^{*}, f(v)\rangle = \langle f^{\top} (w^{*}), v\rangle ,$$
we deduce that $v \in$ (Im $f^{\top})^{0}$ iff $\langle f^{\top}(w^{*}), v\rangle = 0$ for all $w^{*} \in F^{*}$ iff $\langle w^{*}, f(v)\rangle = 0$ for all $w^{*} \in F^{*}$ . Assume that $v \in$ (Im $f^{\top} )^{0}$. If we pick a basis $(w_{i})_{i\in I}$ of $F$, then we have the linear forms $w_{i}^{*}$ : $F \to K$ such that $w_{i}^{*} (w_{j}) = \delta_{ij}$ , and since we must have $\langle w_{i}^{*} , f(v)\rangle = 0$ for all $i \in$ I and $(w_{i})_{i\in I}$ is a basis of $F$, we conclude that f(v) $= 0$, and thus $v \in$ Ker $f$ (this is because $\langle w_{i}^{*} , f(v)\rangle$ is the coefficient of f(v) associated with the basis vector $w_{i})$. Conversely, if $v \in$ Ker $f$, then $\langle w^{*}, f(v)\rangle = 0$ for all $w^{*} \in F^{*}$ , so we conclude that $v \in$ (Im $f^{\top} )^{0}$. Therefore, $v \in$ (Im $f^{\top})^{0}$ iff $v \in$ Ker $f$; that is,
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0},$$
as claimed. $\overline{1}\overline{Using} \overline{Zorn’s} \overline{lemma,} \overline{we} \overline{pick} \overline{W} \overline{maximal}$ among all subspaces of $E/V$ such that Kx $\cap W = (0)$; then, $E/V =$ Kx $\oplus W$.

<!-- PAGE 440 -->
The following theorem shows the relationship between the rank of $f$ and the rank of $f^{\top}$ .

> **Theorem 11.12.** Given a linear map $f$ : $E \to F$, the following properties hold.
(a) The dual (Im $f)^{*}$ of Im $f$ is isomorphic to Im $f^{\top} = f^{\top} (F^{*}$ ); that is,
$$\sim$$
$$(\mathrm{Im} f)^{*}= \mathrm{Im} f^{\top}.$$
$(b)$ If $F$ is finite dimensional, then rk(f) $= rk(f^{\top}$ ).

*Proof.* (a) Consider the linear maps
$$pj$$
$$E\longrightarrow \mathrm{Im} f\longrightarrow F,$$
$$pfj$$
where $E \longrightarrow$ Im $f$ is the surjective map induced by $E \longrightarrow F$, and Im $f \longrightarrow F$ is the injective inclusion map of Im $f$ into $F$. By definition, $f = j \circ p$. To simplify the notation,
$$p$$
let $I =$ Im $f$. By Proposition 11.8, since $E \longrightarrow$ I is surjective, $I^{*p\top}\longrightarrow E^{*}$ is injective, and
$$j$$
since Im $f \longrightarrow F$ is injective, $F^{*j\top}\longrightarrow I^{*}$ is surjective. Since $f = j \circ p$, we also have
$$f^{\top} = (j \circ p)^{\top}= p^{\top}\circ j^{\top},$$
$$j\top p\top$$
and since $F^{*} \longrightarrow I^{*}$ is surjective, and $I^{*} \longrightarrow E^{*}$ is injective, we have an isomorphism between (Im $f)^{*}$ and $f^{\top} (F^{*}$ ).
$(b)$ We already noted that Part (a) of Theorem 11.4 shows that dim(F) $= dim(F^{*}$ ), for every vector space $F$ of finite dimension. Consequently, dim(Im $f) =$ dim((Im $f)^{*})$, and thus, by Part (a) we have rk(f) $= rk(f^{\top}$ ).
Remark: When both $E$ and $F$ are finite-dimensional, there is also a simple proof of $(b)$ that doesn’t use the result of Part (a). By Theorem 11.4(c)
$$\dim(\mathrm{Im} f) + \dim((\mathrm{Im} f)^{0}) = \dim(F),$$
and by Theorem 6.16
$$\dim(\mathrm{Ker} f^{\top} ) + \dim(\mathrm{Im} f^{\top} ) = \dim(F^{*} ).$$
Furthermore, by Proposition 11.11, we have
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0},$$
and since $F$ is finite-dimensional dim(F) $= dim(F^{*}$ ), so we deduce
$$\dim(\mathrm{Im} f) + \dim((\mathrm{Im} f)^{0}) = \dim((\mathrm{Im} f)^{0}) + \dim(\mathrm{Im} f^{\top} ),$$
which yields dim(Im $f) =$ dim(Im $f^{\top}$ ); that is, rk(f) $= rk(f^{\top}$ ).

<!-- PAGE 441 -->

> **Proposition 11.13.** If $f$ : $E \to F$ is any linear map, then the following identities hold:
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
$$\mathrm{Ker} (f^{\top} ) = (\mathrm{Im} f)^{0}$$
$$\mathrm{Im} f = (\mathrm{Ker} (f^{\top} )^{0}$$
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0}.$$

*Proof.* The equation Ker $(f^{\top}) =$ (Im $f)^{0}$ has already been proven in Proposition 11.11. By the duality theorem (Ker $(f))^{00} =$ Ker $(f)$, so from Im $f^{\top} =$ (Ker $(f))^{0}$ we get Ker $(f) =$ (Im $f^{\top})^{0}$. Similarly, (Im $f)^{00} =$ Im $f$, so from Ker $(f^{\top}) =$ (Im $f)^{0}$ we get Im $f =$ (Ker $(f^{\top} )^{0}$. Therefore, what is left to be proven is that Im $f^{\top} =$ (Ker $(f))^{0}$. Let $p: E \to E/Ker (f)$ be the canonical surjection, $\overline{f}\overline{:} E/Ker (f) \to$ Im $f$ be the isomorphism induced by $f$, and $j$ : Im $f \to F$ be the inclusion map. Then, we have
$$f = j \circ \overline{f} \circ p,$$
which implies that
$$f^{\top} = p^{\top}\circ \overline{f}^{\top}\circ j^{\top}.$$
Since $p$ is surjective, $p^{\top}$ is injective, since $j$ is injective, $j^{\top}$ is surjective, and since $\overline{f}$ is bijective, $\overline{f}^{\top}$ is also bijective. It follows that $(E/Ker (f))^{*} = Im(\overline{f}^{\top} \circ j^{\top})$, and we have
$$\mathrm{Im} f^{\top} = \mathrm{Im} p^{\top}.$$
Since $p: E \to E/Ker (f)$ is the canonical surjection, by Proposition 11.9 applied to $U =$ Ker $(f)$, we get
$$\mathrm{Im} f^{\top} = \mathrm{Im} p^{\top}= (\mathrm{Ker} (f))^{0},$$
as claimed. In summary, the equation
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
applies in any dimension, and it implies that
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0}.$$
The following proposition shows the relationship between the matrix representing a linear map $f$ : $E \to F$ and the matrix representing its transpose $f^{\top}$ : $F^{*} \to E^{*}$.

> **Proposition 11.14.** Let $E$ and $F$ be two vector spaces, and let $(u_{1}, \dots  , u_{n})$ be a basis for $E$ and $(v_{1}, \dots  , v_{m})$ be a basis for $F$. Given any linear map $f$ : $E \to F$, if M(f) is the $m \times$  n- matrix representing $f$ w.r.t. the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$, then the $n \times m$-matrix $M(f^{\top}$ ) representing $f^{\top}$ : $F^{*} \to E^{*}$ w.r.t. the dual bases $(v_{1}^{*}, \dots  , v_{m}^{*})$ and $(u_{1}^{*}, \dots  , u_{n}^{*})$ is the transpose $M(f)^{\top}$ of M(f).

<!-- PAGE 442 -->

*Proof.* Recall that the entry $a_{i j}$ in row $i$ and column $j$ of M(f) is the $i$-th coordinate of $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$. By definition of $v_{i}^{*}$ , we have $\langle v_{i}^{*} , f(u_{j})\rangle = a_{i j}$. The entry $a_{j i}^{\top}$ in row $j$ and column $i$ of $M(f^{\top})$ is the $j$-th coordinate of
$$f^{\top} (v_{i}^{*} ) = a_{1i}^{\top}u_{1}^{*} + \cdots  + a_{j i}^{\top}u_{j}^{*} + \cdots  + a_{n i}^{\top}u_{n}^{*}$$
over the basis $(u_{1}^{*}, \dots  , u_{n}^{*})$, which is just $a_{j i}^{\top} = f^{\top}(v_{i}^{*} )(u_{j}) = \langle f^{\top}(v_{i}^{*}$ ), $u_{j}\rangle$ . Since
$$\langle v_{i}^{*} , f(u_{j})\rangle = \langle f^{\top}(v_{i}^{*} ), u_{j}\rangle ,$$
we have $a_{i j} = a_{j i}^{\top}$, proving that $M(f^{\top}) = M(f)^{\top}$. We now can give a very short proof of the fact that the rank of a matrix is equal to the rank of its transpose.

> **Proposition 11.15.** Given an $m \times  n$ matrix $A$ over a field $K$, we have rk(A) $= rk(A^{\top})$.

*Proof.* The matrix $A$ corresponds to a linear map $f$ : $K^{n} \to K^{m}$, and by Theorem 11.12, rk(f) $= rk(f^{\top}$ ). By Proposition 11.14, the linear map $f^{\top}$ corresponds to $A^{\top}$. Since rk(A) $=$ rk(f), and $rk(A^{\top}) = rk(f^{\top}$ ), we conclude that rk(A) $= rk(A^{\top})$. Thus, given an $m\times n$-matrix $A$, the maximum number of linearly independent columns is equal to the maximum number of linearly independent rows. There are other ways of proving this fact that do not involve the dual space, but instead some elementary transformations on rows and columns. Proposition 11.15 immediately yields the following criterion for determining the rank of a matrix:

> **Proposition 11.16.** Given any $m\times n$ matrix $A$ over a field $K$ (typically $K =\mathbb{R}$ or $K =\mathbb{C})$, the rank of $A$ is the maximum natural number $r$ such that there is an invertible $r\times r$ submatrix of $A$ obtained by selecting $r$ rows and $r$ columns of $A$. For example, the $3 \times  2$ matrix
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$
has rank $2$ iff one of the three $2 \times  2$ matrices
$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{pmatrix} \begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$
is invertible. If we combine Proposition 7.11 with Proposition 11.16, we obtain the following criterion for finding the rank of a matrix.
