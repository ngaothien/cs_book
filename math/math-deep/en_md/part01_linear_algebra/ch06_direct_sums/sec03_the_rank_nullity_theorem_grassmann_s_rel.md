# The Rank-Nullity Theorem; Grassmann's Relation


<!-- PAGE 202 -->
By block multiplication we get
$$TC + UW = I_{n}$$
$$TV + \beta U = 0_{n,1}$$
$$\alpha W = 0_{1,n}$$
$$\alpha \beta  = 1.$$
From the above equations we deduce that $\alpha , \beta  \neq  0$ and $\beta  = \alpha^{-1}$ . Since $\alpha  \neq  0$, the equation $\alpha W = 0_{1,n}$ yields $W = 0_{1,n}$, and so
$$TC = I_{n},TV + \beta U = 0_{n,1}.$$
It follows that $T$ is invertible and $C$ is its inverse, and since $T$ is upper triangular, by the induction hypothesis, $C$ is also upper triangular. The above argument can be easily modified to prove that if $A$ is invertible, then its diagonal entries are nonzero. We are now ready to prove a very crucial result relating the rank and the dimension of the kernel of a linear map.

## 6.3 The Rank-Nullity Theorem; Grassmann’s Relation

We begin with the following fundamental proposition.

> **Proposition 6.15.** Let $E, F$ and $G$, be three vector spaces, $f$ : $E \to F$ an injective linear map, $g: F \to G$ a surjective linear map, and assume that Im $f =$ Ker $g$. Then, the following properties hold. (a) For any section $s: G \to F$ of $g$, we have $F =$ Ker $g \oplus$ Im $s$, and the linear map $f + s: E \oplus G \to F$ is an $isomorphism.^{1}$
$(b)$ For any retraction $r: F \to E$ of $f$, we have $F =$ Im $f \oplus$ Ker $r.^{2}$
$$f F/g G/$$
$$E$$
$$\overline{r}\overline{s}$$

*Proof.* (a) Since $s: G \to F$ is a section of $g$, we have $g \circ s = id_{G}$, and for every $u \in F$,
$$g(u -s(g(u))) = g(u) -g(s(g(u))) = g(u) -g(u) = 0.$$
Thus, $u$ - s(g(u)) $\in$ Ker $g$, and we have $F =$ Ker $g +$ Im $s$. On the other hand, if $u \in$ Ker $g \cap$ Im $s$, then $u =$ s(v) for some $v \in G$ because $u \in$ Im $s$, g(u) $= 0$ because $u \in$ Ker $g$, and so,
$$g(u) = g(s(v)) = v = 0,$$
$\overline{1}\overline{The} \overline{existence} \overline{of} \overline{a} \overline{section} \overline{s}\overline{:} \overline{G}\overline{\to} \overline{F} \overline{of} g$ follows from Proposition 6.11. 2The existence of a retraction $r: F \to E$ of $f$ follows from Proposition 6.11.

<!-- PAGE 203 -->
because $g \circ s = id_{G}$, which shows that $u =$ s(v) $= 0$. Thus, $F =$ Ker $g \oplus$ Im $s$, and since by assumption, Im $f =$ Ker $g$, we have $F =$ Im $f \oplus$ Im $s$. But then, since $f$ and $s$ are injective, $f + s: E \oplus G \to F$ is an isomorphism. The proof of $(b)$ is very similar. Note that we can choose a retraction $r: F \to E$ so that Ker $r =$ Im $s$, since $F =$ Ker $g \oplus$ Im $s =$ Im $f \oplus$ Im $s$ and $f$ is injective so we can set $r \equiv 0$ on Im $s$.
$$fg$$
Given a sequence of linear maps $E \longrightarrow F \longrightarrow G$, when Im $f =$ Ker $g$, we say that the
$$fg$$
sequence $E \longrightarrow F \longrightarrow G$ is exact at $F$. If in addition to being exact at $F, f$ is injective and $g$ is surjective, we say that we have a short exact sequence, and this is denoted as
$$fg$$
$$0 \longrightarrow E\longrightarrow F\longrightarrow G \longrightarrow 0.$$
The property of a short exact sequence given by Proposition 6.15 is often described by saying
$$fg$$
that $0 \longrightarrow E \longrightarrow F \longrightarrow G \longrightarrow 0$ is a (short) split exact sequence. As a corollary of Proposition 6.15, we have the following result which shows that given a linear map $f$ : $E \to F$, its domain $E$ is the direct sum of its kernel Ker $f$ with some isomorphic copy of its image Im $f$.

> **Theorem 6.16.** (Rank-nullity theorem) Let $E$ and $F$ be vector spaces, and let $f$ : $E \to F$ be a linear map. Then, $E$ is isomorphic to Ker $f \oplus$ Im $f$, and thus,
$$\dim(E) = \dim(\mathrm{Ker} f) + \dim(\mathrm{Im} f) = \dim(\mathrm{Ker} f) + rk(f).$$
See Figure 6.3.

*Proof.* Consider
$$\longrightarrow i\longrightarrow$$
$$\mathrm{Ker} fE^{f'}\mathrm{Im} f,$$
$$if'$$
where Ker $f \longrightarrow E$ is the inclusion map, and $E \longrightarrow$ Im $f$ is the surjection associated
$$fs$$
with $E \longrightarrow F$. Then, we apply Proposition 6.15 to any section Im $f \longrightarrow E$ of f' to get an isomorphism between $E$ and Ker $f \oplus$ Im $f$, and Proposition 6.7, to get dim(E) $=$ dim(Ker $f) +$ dim(Im $f)$.

> **Definition 6.10.** The dimension dim(Ker $f)$ of the kernel of a linear map $f$ is called the nullity of $f$. We now derive some important results using Theorem 6.16.

> **Proposition 6.17.** Given a vector space $E$, if $U$ and $V$ are any two subspaces of $E$, then
$$\dim(U) + \dim(V ) = \dim(U + V ) + \dim(U \cap V ),$$
an equation known as Grassmann’s relation.

<!-- PAGE 204 -->
$$\mathrm{Ker} f$$
$$s (f(u)) = (1,1,2)$$
$$f(x,y,z) = (x,y)$$
$$h = (0,0,-1)$$
$$u = (1,1,1)$$
$$u =f  =  f(u  ) = (0, 1)$$
$$1 (1,0,,1)22f(u) = (1,1)$$
$$1)(0,1$$
$$=$$
$$u 2$$
$$\overline{f  = f(u  ) = (1,0)} 11$$
$$s(x,y) = (x,y,x+y)$$
$$\mathbb{R}^{3}  \mathbb{R}^{2}$$

![Figure 6.3](../../assets/ch06/fig_6_3.png)

**Figure 6.3:** Let $f$ : $E \to F$ be the linear map from to given by f(x, $y, z) = (x, y)$.
$$\mathbb{R}^{2} \mathbb{R}^{3}  \mathbb{R}^{2}$$
Then $s: \to$ is given by s(x, $y) = (x, y, x + y)$ and maps the pink isomorphically
$$\mathbb{R}^{3}$$
onto the slanted pink plane of whose equation is $-x$ - $y + z = 0$. Theorem 6.16 shows $\mathbb{R}^{3}$ that is the direct sum of the plane $-x$ - $y + z = 0$ and the kernel of $f$ which the orange z-axis.

*Proof.* Recall that $U + V$ is the image of the linear map
$$a: U \times  V \to E$$
given by
$$a(u, v) = u + v,$$
and that we proved earlier that the kernel Ker a of a is isomorphic to $U \cap V$ . By Theorem 6.16,
$$\dim(U \times  V ) = \dim(\mathrm{Ker} a) + \dim(\mathrm{Im} a),$$
but dim(U $\times  V$ ) $=$ dim(U) $+$ dim(V ), dim(Ker $a) =$ dim(U $\cap V$ ), and Im $a = U + V$ , so the Grassmann relation holds. The Grassmann relation can be very useful to figure out whether two subspace have a nontrivial intersection in spaces of dimension $> 3$. For example, it is easy to see that in $\mathbb{R}^{5}$, there are subspaces $U$ and $V$ with dim(U) $= 3$ and dim(V ) $= 2$ such that $U \cap V = (0)$; for example, let $U$ be generated by the vectors $(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0)$, and $V$ be generated by the vectors $(0, 0, 0, 1, 0)$ and $(0, 0, 0, 0, 1)$. However, we claim that if dim(U) $= 3$ and dim(V ) $= 3$, then dim(U $\cap V$ ) $\ge 1$. Indeed, by the Grassmann relation, we have
$$\dim(U) + \dim(V ) = \dim(U + V ) + \dim(U \cap V ),$$
namely
$$3 + 3 = 6 = \dim(U + V ) + \dim(U \cap V ),$$

<!-- PAGE 205 -->
and since $U + V$ is a subspace of $\mathbb{R}^{5}$, dim(U $+ V$ ) $\le 5$, which implies
$$6 \le 5 + \dim(U \cap V ),$$
that is $1 \le$ dim(U $\cap V$ ). As another consequence of Proposition 6.17, if $U$ and $V$ are two hyperplanes in a vector space of dimension $n$, so that dim(U) $= n$ - $1$ and dim(V ) $= n$ - $1$, the reader should show that
$$\dim(U \cap V ) \ge n -2,$$
and so, if $U \neq  V$ , then
$$\dim(U \cap V ) = n -2.$$
Here is a characterization of direct sums that follows directly from Theorem 6.16.

> **Proposition 6.18.** If $U_{1}, \dots  , U_{p}$ are any subspaces of a finite dimensional vector space $E$, then
$$\dim(U_{1} + \cdots  + U_{p}) \le \dim(U_{1}) + \cdots  + \dim(U_{p}),$$
and
$$\dim(U_{1} + \cdots  + U_{p}) = \dim(U_{1}) + \cdots  + \dim(U_{p})$$
iff the $U_{i}s$ form a direct sum $U_{1} \oplus \cdots  \oplus U_{p}$.

*Proof.* If we apply Theorem 6.16 to the linear map
$$a: U_{1} \times  \cdots  \times  U_{p} \to U_{1} + \cdots  + U_{p}$$
given by $a(u_{1}, \dots  , u_{p}) = u_{1} + \cdots  + u_{p}$, we get
$$\dim(U_{1} + \cdots  + U_{p}) = \dim(U_{1} \times  \cdots  \times  U_{p}) -\dim(\mathrm{Ker} a)$$
$$= \dim(U_{1}) + \cdots  + \dim(U_{p}) -\dim(\mathrm{Ker} a),$$
so the inequality follows. Since a is injective iff Ker $a = (0)$, the $U_{i}s$ form a direct sum iff the second equation holds. Another important corollary of Theorem 6.16 is the following result:

> **Proposition 6.19.** Let $E$ and $F$ be two vector spaces with the same finite dimension dim(E) $=$ dim(F) $= n$. For every linear map $f$ : $E \to F$, the following properties are equivalent:
(a) $f$ is bijective.
$(b) f$ is surjective.
$(c) f$ is injective.

<!-- PAGE 206 -->
$(d)$ Ker $f = (0)$.

*Proof.* Obviously, (a) implies $(b)$. If $f$ is surjective, then Im $f = F$, and so dim(Im $f) = n$. By Theorem 6.16,
$$\dim(E) = \dim(\mathrm{Ker} f) + \dim(\mathrm{Im} f),$$
and since dim(E) $= n$ and dim(Im $f) = n$, we get dim(Ker $f) = 0$, which means that Ker $f = (0)$, and so $f$ is injective (see Proposition 3.19). This proves that $(b)$ implies $(c)$. If $f$ is injective, then by Proposition 3.19, Ker $f = (0)$, so $(c)$ implies $(d)$. Finally, assume that Ker $f = (0)$, so that dim(Ker $f) = 0$ and $f$ is injective (by Proposition 3.19). By Theorem 6.16,
$$\dim(E) = \dim(\mathrm{Ker} f) + \dim(\mathrm{Im} f),$$
and since dim(Ker $f) = 0$, we get
$$\dim(\mathrm{Im} f) = \dim(E) = \dim(F),$$
which proves that $f$ is also surjective, and thus bijective. This proves that $(d)$ implies (a) and concludes the proof. One should be warned that Proposition 6.19 fails in infinite dimension. Here are a few applications of Proposition 6.19. Let $A$ be an $n \times  n$ matrix and assume that $A$ some right inverse $B$, which means that $B$ is an $n \times  n$ matrix such that
$$AB = I.$$
The linear map associated with $A$ is surjective, since for every $u \in \mathbb{R}^{n}$, we have A(Bu) $= u$. By Proposition 6.19, this map is bijective so $B$ is actually the inverse of $A$; in particular $BA =$ I. Similarly, assume that $A$ has a left inverse $B$, so that
$$BA = I.$$
This time the linear map associated with $A$ is injective, because if Au $= 0$, then BAu $=$ B0 $= 0$, and since $BA =$ I we get $u = 0$. Again, by Proposition 6.19, this map is bijective so $B$ is actually the inverse of $A$; in particular $AB =$ I. Now assume that the linear system Ax $= b$ has some solution for every $b$. Then the linear map associated with $A$ is surjective and by Proposition 6.19, $A$ is invertible. Finally assume that the linear system Ax $= b$ has at most one solution for every $b$. Then the linear map associated with $A$ is injective and by Proposition 6.19, $A$ is invertible. The following Proposition will also be useful.

<!-- PAGE 207 -->

> **Proposition 6.20.** Let $E$ be a vector space. If $E = U \oplus V$ and $E = U \oplus W$, then there is an isomorphism $f$ : $V \to W$ between $V$ and $W$.

*Proof.* Let $R$ be the relation between $V$ and $W$, defined such that
$$\langle v, w\rangle \in Riffw -v \in U.$$
We claim that $R$ is a functional relation that defines a linear isomorphism $f$ : $V \to W$ between $V$ and $W$, where f(v) $= w$ iff $\langle v, w\rangle \in R (R$ is the graph of $f)$. If $w$ - $v \in U$ and w' - $v \in U$, then w' - $w \in U$, and since $U \oplus W$ is a direct sum, $U \cap W = (0)$, and thus w' - $w = 0$, that is w' $= w$. Thus, $R$ is functional. Similarly, if $w$ - $v \in U$ and $w$ - v' $\in U$, then v' - $v \in U$, and since $U \oplus V$ is a direct sum, $U \cap V = (0)$, and v' $= v$. Thus, $f$ is injective. Since $E = U \oplus V$ , for every $w \in W$, there exists a unique pair $\langle u, v\rangle \in U \times  V$ , such that $w = u + v$. Then, $w$ - $v \in U$, and $f$ is surjective. We also need to verify that $f$ is linear. If
$$w -v = u$$
and
$$w'-v'= u',$$
where $u$, u' $\in U$, then, we have
$$(w + w') -(v + v') = (u + u'),$$
where $u +$ u' $\in U$. Similarly, if
$$w -v = u$$
where $u \in U$, then we have
$$\lambda w -\lambda v = \lambda u,$$
where $\lambda u \in U$. Thus, $f$ is linear. Given a vector space $E$ and any subspace $U$ of $E$, Proposition 6.20 shows that the dimension of any subspace $V$ such that $E = U \oplus V$ depends only on $U$. We call dim(V ) the codimension of $U$, and we denote it by codim(U). A subspace $U$ of codimension $1$ is called a hyperplane. The notion of rank of a linear map or of a matrix is an important one, both theoretically and practically, since it is the key to the solvability of linear equations. Recall from Definition 3.19 that the rank rk(f) of a linear map $f$ : $E \to F$ is the dimension dim(Im $f)$ of the image subspace Im $f$ of $F$. We have the following simple proposition.

> **Proposition 6.21.** Given a linear map $f$ : $E \to F$, the following properties hold:
$(i)$ rk(f) $=$ codim(Ker $f)$.

<!-- PAGE 208 -->
(ii) rk(f) $+$ dim(Ker $f) =$ dim(E).
(iii) rk(f) $\le$ min(dim(E), dim(F)).

*Proof.* Since by Proposition 6.16, dim(E) $=$ dim(Ker $f) +$ dim(Im $f)$, and by definition, rk(f) $=$ dim(Im $f)$, we have rk(f) $=$ codim(Ker $f)$. Since rk(f) $=$ dim(Im $f)$, (ii) follows from dim(E) $=$ dim(Ker $f) +$ dim(Im $f)$. As for (iii), since Im $f$ is a subspace of $F$, we have rk(f) $\le$ dim(F), and since rk(f) $+$ dim(Ker $f) =$ dim(E), we have rk(f) $\le$ dim(E). The rank of a matrix is defined as follows.

> **Definition 6.11.** Given a $m \times n$-matrix $A = (a_{i j})$ over the field $K$, the rank rk(A) of the matrix $A$ is the maximum number of linearly independent columns of $A$ (viewed as vectors in $K^{m})$. In view of Proposition 3.9, the rank of a matrix $A$ is the dimension of the subspace of $K^{m}$ generated by the columns of $A$. Let $E$ and $F$ be two vector spaces, and let $(u_{1}, \dots  , u_{n})$ be a basis of $E$, and $(v_{1}, \dots  , v_{m})$ a basis of $F$. Let $f$ : $E \to F$ be a linear map, and let M(f) be its matrix w.r.t. the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{m})$. Since the rank rk(f) of $f$ is the dimension of Im $f$, which is generated by $(f(u_{1}), \dots  , f(u_{n}))$, the rank of $f$ is the maximum number of linearly independent vectors in $(f(u_{1}), \dots  , f(u_{n}))$, which is equal to the number of linearly independent columns of M(f), since $F$ and $K^{m}$ are isomorphic. Thus, we have rk(f) $=$ rk(M(f)), for every matrix representing $f$. We will see later, using duality, that the rank of a matrix $A$ is also equal to the maximal number of linearly independent rows of $A$. If $U$ is a hyperplane, then $E = U \oplus V$ for some subspace $V$ of dimension $1$. However, a subspace $V$ of dimension $1$ is generated by any nonzero vector $v \in V$ , and thus we denote $V$ by Kv, and we write $E = U \oplus$ Kv. Clearly, $v \in / U$. Conversely, let $x \in E$ be a vector such that $x \in / U$ (and thus, x̸ $= 0)$. We claim that $E = U \oplus$ Kx. Indeed, since $U$ is a hyperplane, we have $E = U \oplus$ Kv for some $v \in / U$ (with $v \neq  0)$. Then, $x \in E$ can be written in a unique way as $x = u + \lambda v$, where $u \in U$, and since $x \in / U$, we must have $\lambda  \neq  0$, and thus, $v = -\lambda^{-1} u + \lambda^{-1} x$. Since $E = U \oplus$ Kv, this shows that $E = U +$ Kx. Since $x \in / U$, we have $U \cap$ Kx $= 0$, and thus $E = U \oplus$ Kx. This argument shows that a hyperplane is a maximal proper subspace $H$ of $E$. Theorem 6.16 also yields a characterization of hyperplanes in terms of linear forms. Recall that given a vector space $E$, a hyperplane $H$ in $E$ is subspace of codimension $1$, which means that there is a one-dimensional subspace $L$ such that
$$E = H \oplus L.$$

> **Proposition 6.22.** Given a nontrivial vector space $E$ over a field $K$, a subspace $H$ of $E$ is a hyperplane iff there is a nonzero linear form $\phi$ : $E \to K$ such that
$$H = \mathrm{Ker} \phi .$$

<!-- PAGE 209 -->
Furthermore, if $\phi_{1}$  and $\phi_{2}$  are any two nonzero linear forms defining the same hyperplane $H$, in the sense that $H =$ Ker $\phi_{1}  =$ Ker $\phi_{2}$ , then there is some nonzero $\alpha  \in K$ such that $\phi_{2}  = \alpha \phi_{1}$ .

*Proof.* First assume that $\phi$ : $E \to K$ is a nonzero linear form and that $H =$ Ker $\phi$ . Then there is a nonzero vector $u_{0} \in E$ such that $\phi (u_{0}) = \lambda_{0}  \neq  0$ for some $\lambda_{0}  \in K$, and so for every $\lambda  \in K$, we have
$$\phi (\lambda \lambda_{0}^{-1}  u_{0}) = \lambda \lambda_{0}^{-1}  \phi (u_{0}) = \lambda \lambda_{0}^{-1}  \lambda_{0}  = \lambda ,$$
which means that $\phi$  is surjective onto $K$. It follows that in Theorem 6.16 we can define $s$ by $s(\lambda_{0}$ ) $= u_{0}$, so the subspace $L =$ Im $s = Ku_{0}$ is a one-dimensional space and we have
$$E = \mathrm{Ker} \phi  \oplus L = H \oplus L,$$
so $H$ is a hyperplane. Conversely assume that $H$ is a hyperplane, so that $E = H \oplus L$ where $L$ is a subspace of dimension $1$. If we pick a nonzero vector $u_{0} \in L$, since $L$ has dimension $1$ and $E = H \oplus L$, every $u \in E$ can be written uniquely as $u = h + \lambda u_{0}$ for some $h \in H$ and some $\lambda  \in K$. If we define the map $\phi$ : $E \to K$ by
$$\phi (u + \lambda u_{0}) = \lambda ,$$
we check immediately that $\phi$  is linear and that its kernel is $H$. Assume that $H =$ Ker $\phi_{1}  =$ Ker $\phi_{2}$  for some nonzero linear forms $\phi_{1}$  and $\phi_{2}$ . We just proved that $E = H \oplus Ku_{0}$ for some $u_{0} \in E$ such that $\phi_{1} (u_{0}) \neq  0$, and we must also have $\phi_{2} (u_{0}) \neq  0$, since otherwise, as $H =$ Ker $\phi_{2}$ , the linear form $\phi_{2}$  would be zero on $E$. Then observe that
$$\phi_{2}  - \frac{\phi_{2} (u_{0})}{\phi_{1} (u_{0})} \phi_{1}$$
is a linear form that vanishes on $H$ since both $\phi_{1}$  and $\phi_{2}$  vanish on $H$, but also vanishes on $Ku_{0}$ since
$$\begin{pmatrix} \phi_{2} (u_{0}) \\ \phi_{2}  - & \phi_{1} \\ \phi_{1} (u_{0}) \end{pmatrix} (\lambda u_{0}) = \phi_{2} (\lambda u_{0}) - \frac{\phi_{2} (u_{0})}{\phi_{1} (u_{0})} \phi_{1} (\lambda u_{0})$$
$$= \lambda \phi_{2} (u_{0}) -\lambda \frac{\phi_{2} (u_{0})}{\phi_{1} (u_{0})} \phi_{1} (u_{0}) = \lambda \phi_{2} (u_{0}) -\lambda \phi_{2} (u_{0}) = 0$$
for all $\lambda  \in K$. Since $E = H \oplus Ku_{0}$, we deduce that $\phi_{2}$  - $\alpha \phi_{2}$  vanishes on $E$, with
$$\alpha  = \frac{\phi_{2} (u_{0})}{\phi_{1} (u_{0})̸} = 0,$$
and so $\phi_{2}  = \alpha \phi_{1}$ , as claimed.
