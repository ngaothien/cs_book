# Finitely Generated Modules over a PID


<!-- PAGE 1297 -->

## 35.5 Finitely Generated Modules over a PID; Invariant

$$Factor Decomposition$$
There are several ways of obtaining the decomposition of a finitely generated module as a direct sum of cyclic modules. One way to proceed is to first use the Primary Decomposition Theorem and then to show how each primary module $M_{p}$ is the direct sum of cyclic modules of the form $A/(p^{n})$. This is the approach followed by Lang $[113]$ (Chapter III, section $7)$, among others. We prefer to use a proposition that produces a particular basis for a submodule of a finitely generated free module, because it yields more information. This is the approach followed in Dummitt and Foote $[55]$ (Chapter $12)$ and Bourbaki $[26]$ (Chapter VII). The proof that we present is due to Pierre Samuel.

> **Proposition 35.23.** Let $F$ be a finitely generated free module over a PID $A$, and let $M$ be any submodule of $F$. Then, $M$ is a free module and there is a basis $(e_{1}$, ..., $e_{n})$ of $F$, some $q \le n$, and some nonzero elements $a_{1}, \dots  , a_{q} \in A$, such that $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ is a basis of $M$ and $a_{i}$ divides $a_{i+1}$ for all $i$, with $1 \le i \le q$ - $1$.

*Proof.* The proposition is trivial when $M = {0}$, thus assume that $M$ is nontrivial. Pick some basis $(u_{1}, \dots  , u_{n})$ for $F$. Let L(F, $A)$ be the set of linear forms on $F$. For any $f \in$ L(F, $A)$, it is immediately verified that f(M) is an ideal in $A$. Thus, f(M) $= a_{h}A$, for some $a_{h} \in A$, since every ideal in $A$ is a principal ideal. Since $A$ is a PID, any nonempty family of ideals in $A$ has a maximal element, so let $f$ be a linear map such that $a_{h}A$ is a maximal ideal in $A$. Let $\pi_{i}$  : $F \to A$ be the $i$-th projection, i.e., $\pi_{i}$  is defined such that $\pi_{i} (x_{1}u_{1} + \cdots  + x_{n}u_{n}) = x_{i}$. It is clear that $\pi_{i}$  is a linear map, and since $M$ is nontrivial, one of the $\pi_{i} (M)$ is nontrivial, and $a_{h} \neq  0$. There is some e' $\in M$ such that f(e') $= a_{h}$. We claim that, for every $g \in$ L(F, $A)$, the element $a_{h} \in A$ divides g(e'). Indeed, if $d$ is the gcd of $a_{h}$ and g(e'), by the B´ezout identity, we can write
$$d = ra_{h} + sg(e'),$$
for some $r, s \in A$, and thus
$$d = rf(e') + sg(e') = (rf + sg)(e').$$
However, rf $+$ sg $\in$ L(F, $A)$, and thus,
$$a_{h}A \subseteq dA \subseteq (rf + sg)(M),$$
since $d$ divides $a_{h}$, and by maximality of $a_{h}A$, we must have $a_{h}A =$ dA, which implies that $d = a_{h}$, and thus, $a_{h}$ divides g(e'). In particular, $a_{h}$ divides each $\pi_{i}$ (e') and let $\pi_{i}$ (e') $= a_{h}b_{i}$, with $b_{i} \in A$. Let $e = b_{1}u_{1} + \cdots  + b_{n}u_{n}$. Note that
$$e'= \pi_{1} (e')u_{1} + \cdots  + \pi_{n} (e')u_{n} = a_{h}b_{1}u_{1} + \cdots  + a_{h}b_{n}u_{n},$$

<!-- PAGE 1298 -->
and thus, e' $= a_{h}e$. Since $a_{h} =$ f(e') $= f(a_{h}e) = a_{h}f(e)$, and since $a_{h} \neq  0$, we must have f(e) $= 1$. Next, we claim that
$$F = Ae \oplus f^{-1} (0)$$
and
$$M = Ae'\oplus (M \cap f^{-1}(0)),$$
with e' $= a_{h}e$. Indeed, every $x \in F$ can be written as
$$x = f(x)e + (x -f(x)e),$$
and since f(e) $= 1$, we have f(x - f(x)e) $=$ f(x) - f(x)f(e) $=$ f(x) - f(x) $= 0$. Thus, $F =$ Ae $+ f^{-1} (0)$. Similarly, for any $x \in M$, we have f(x) $= ra_{h}$, for some $r \in A$, and thus,
$$x = f(x)e + (x -f(x)e) = ra_{h}e + (x -f(x)e) = re'+ (x -f(x)e),$$
we still have $x$ - f(x)e $\in f^{-1}(0)$, and clearly, $x$ - f(x)e $= x$ - $ra_{h}e = x$ - re' $\in M$, since e' $\in M$. Thus, $M =$ Ae' $+ (M \cap f^{-1}(0))$. To prove that we have a direct sum, it is enough to prove that Ae $\cap f^{-1} (0) = {0}$. For any $x =$ re $\in$ Ae, if f(x) $= 0$, then f(re) $=$ rf(e) $= r = 0$, since f(e) $= 1$ and, thus, $x = 0$. Therefore, the sums are direct sums. We can now prove that $M$ is a free module by induction on the size, $q$, of a maximal linearly independent family for $M$. If $q = 0$, the result is trivial. Otherwise, since
$$M = Ae'\oplus (M \cap f^{-1}(0)),$$
it is clear that $M \cap f^{-1} (0)$ is a submodule of $F$ and that every maximal linearly independent family in $M \cap f^{-1} (0)$ has at most $q$ - $1$ elements. By the induction hypothesis, $M \cap f^{-1} (0)$ is a free module, and by adding e' to a basis of $M \cap f^{-1}(0)$, we obtain a basis for $M$, since the sum is direct. The second part is shown by induction on the dimension $n$ of $F$. The case $n = 0$ is trivial. Otherwise, since
$$F = Ae \oplus f^{-1} (0),$$
and since, by the previous argument, $f^{-1} (0)$ is also free, $f^{-1} (0)$ has dimension $n$ - $1$. By the induction hypothesis applied to its submodule $M \cap f^{-1} (0)$, there is a basis $(e_{2}, \dots  , e_{n})$ of $f^{-1} (0)$, some $q \le n$, and some nonzero elements $a_{2}, \dots  , a_{q} \in A$, such that, $(a_{2}e_{2}, \dots  , a_{q}e_{q})$ is a basis of $M \cap f^{-1} (0)$, and $a_{i}$ divides $a_{i+1}$ for all $i$, with $2 \le i \le q$ - $1$. Let $e_{1} = e$, and $a_{1} = a_{h}$, as above. It is clear that $(e_{1}, \dots  , e_{n})$ is a basis of $F$, and that that $(a_{1}e_{1}, \dots  , a_{q}e_{q})$

<!-- PAGE 1299 -->
is a basis of $M$, since the sums are direct, and e' $= a_{1}e_{1} = a_{h}e$. It remains to show that $a_{1}$ divides $a_{2}$. Consider the linear map $g: F \to A$ such that $g(e_{1}) = g(e_{2}) = 1$, and $g(e_{i}) = 0$, for all $i$, with $3 \le i \le n$. We have $a_{h} = a_{1} = g(a_{1}e_{1}) =$ g(e') $\in$ g(M), and thus $a_{h}A \subseteq$ g(M). Since $a_{h}A$ is maximal, we must have g(M) $= a_{h}A = a_{1}A$. Since $a_{2} = g(a_{2}e_{2}) \in$ g(M), we have $a_{2} \in a_{1}A$, which shows that $a_{1}$ divides $a_{2}$. We need the following basic proposition.

> **Proposition 35.24.** For any commutative ring $A$, if $F$ is a free A-module and if $(e_{1}, \dots  , e_{n})$ is a basis of $F$, for any elements $a_{1}, \dots  , a_{n} \in A$, there is an isomorphism
$$F/(Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{n}e_{n}) \approx (A/a_{1}A) \oplus \cdots  \oplus (A/a_{n}A).$$

*Proof.* Let $\sigma$ : $F \to A/(a_{1}A) \oplus \cdots  \oplus A/(a_{n}A)$ be the linear map given by
$$\sigma (x_{1}e_{1} + \cdots  + x_{n}e_{n}) = (\overline{x}_{1}\overline{, \dots  , x}_{n}),$$
where $\overline{x}_{i}$ is the equivalence class of $x_{i}$ in $A/a_{i}A$. The map $\sigma$  is clearly surjective, and its kernel consists of all vectors $x_{1}e_{1} + \cdots  + x_{n}e_{n}$ such that $x_{i} \in a_{i}A$, for $i = 1, \dots  , n$, which means that
$$\mathrm{Ker} (\sigma ) = Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{n}e_{n}.$$
Since $M/Ker (\sigma$ ) is isomorphic to $Im(\sigma$ ), we get the desired isomorphism. We can now prove the existence part of the structure theorem for finitely generated modules over a PID.

> **Theorem 35.25.** Let $M$ be a finitely generated nontrivial A-module, where $A$ a PID. Then, $M$ is isomorphic to a direct sum of cyclic modules
$$M \approx A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
where the $\mathfrak{a}_{i}$ are proper ideals of $A$ (possibly zero) such that
$$\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A.$$
More precisely, if $\mathfrak{a}_{1} = \cdots  =\mathfrak{a}_{r} = (0)$ and $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$, then
$$M \approx A^{r}\oplus (A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}),$$
where $A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$ is the torsion submodule of $M$. The module $M$ is free iff $r = m$, and a torsion-module iff $r = 0$. In the latter case, the annihilator of $M$ is $\mathfrak{a}_{1}$.

<!-- PAGE 1300 -->

*Proof.* Since $M$ is finitely generated and nontrivial, there is a surjective homomorphism $\phi$ : $A^{n} \to M$ for some $n \ge 1$, and $M$ is isomorphic to $A^{n}/Ker (\phi$ ). Since Ker $(\phi$ ) is a submodule of the free module $A^{n}$, by Proposition 35.23, Ker $(\phi$ ) is a free module and there is a basis $(e_{1}, \dots  , e_{n})$ of $A^{n}$ and some nonzero elements $a_{1}, \dots  , a_{q} (q \le n)$ such that $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ is a basis of Ker $(\phi$ ) and $a_{1}$ | $a_{2}$ | $\cdots$  | $a_{q}$. Let $a_{q+1} = \dots  = a_{n} = 0$. By Proposition 35.24, we have an isomorphism
$$A^{n}/\mathrm{Ker} (\phi ) \approx A/a_{1}A \oplus \cdots  \oplus A/a_{n}A.$$
Whenever $a_{i}$ is unit, the factor $A/a_{i}A = (0)$, so we can weed out the units. Let $r = n$ - $q$, and let $s \in \mathbb{N}$ be the smallest index such that $a_{s+1}$ is not a unit. Note that $s = 0$ means that there are no units. Also, as $M \neq  (0), s < n$. Then,
$$M \approx A^{n}/\mathrm{Ker} (\phi ) \approx A/a_{s+1}A \oplus \cdots  \oplus A/a_{n}A.$$
Let $m = r + q$ - $s = n$ - $s$. Then, we have the sequence
$$a_{s+1}, \dots  , a_{q}, a_{q+1}, \dots  , a_{n},$$
$$|{z}|{z}$$
$$q-sr=n-q$$
where $a_{s+1}$ | $a_{s+2}$ | $\cdots$  | $a_{q}$ are nonzero and nonunits and $a_{q+1} = \cdots  = a_{n} = 0$, so we define the $m$ ideals $\mathfrak{a}_{i}$ as follows:
$$($$
$$(0)if 1 \le i \le r$$
$$\mathfrak{a}_{i} =$$
$$a_{r+q+1-i}Aif r + 1 \le i \le m.$$
With these definitions, the ideals $\mathfrak{a}_{i}$ are proper ideals and we have
$$\mathfrak{a}_{i} \subseteq \mathfrak{a}_{i+1},i = 1, \dots  , m -1.$$
When $r = 0$, since $a_{s+1}$ | $a_{s+2}$ | $\cdots$  | $a_{n}$, it is clear that $\mathfrak{a}_{1} = a_{n}A$ is the annihilator of $M$. The other statements of the theorem are clear.

> **Example 35.1.** Here is an example of Theorem 35.25. Let $M$ be $a\mathbb{Z}-module$ with generators ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject to the relations $6e_{3} = 0, 2e_{4} = 0$. Then
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}\mathbb{Z} \oplus \mathbb{Z}\mathbb{Z}$$
$$M=/6/2,$$
where
$$\mathfrak{a}_{1} = (0),\mathfrak{a}_{2} = (0),\mathfrak{a}_{3} = (6),\mathfrak{a}_{4} = (2).$$

<!-- PAGE 1301 -->
The natural number $r$ is called the free rank or Betti number of the module $M$. The generators $\alpha_{1} , \dots  , \alpha_{m}$  of the ideals $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ (defined up to a unit) are often called the invariant factors of $M$ (in the notation of Theorem 35.25, the generators of the ideals $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ are denoted by $a_{q}, \dots  , a_{s+1}, s \le q)$. As corollaries of Theorem 35.25, we obtain again the following facts established in Section 35.1: $1$. A finitely generated module over a PID is the direct sum of its torsion module and a free module. $2$. A finitely generated torsion-free module over a PID is free. It turns out that the ideals $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m}$ ̸ $= A$ are uniquely determined by the module $M$. Uniqueness proofs found in most books tend to be intricate and not very intuitive. The shortest proof that we are aware of is from Bourbaki $[26]$ (Chapter VII, Section $4)$, and uses wedge products. The following preliminary results are needed.

> **Proposition 35.26.** If $A$ is a commutative ring and if $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ are ideals of $A$, then there is an isomorphism
$$A/\mathfrak{a}_{1} \otimes \cdots  \otimes A/\mathfrak{a}_{m} \approx A/(\mathfrak{a}_{1} + \cdots  +\mathfrak{a}_{m}).$$
Sketch of proof. We proceed by induction on $m$. For $m = 2$, we define the map $\phi$ : $A/\mathfrak{a}_{1} \times  A/\mathfrak{a}_{2} \to A/(\mathfrak{a}_{1} +\mathfrak{a}_{2})$ by
$$\phi (\overline{a, b}) = ab(\mathrm{mod} \mathfrak{a}_{1} +\mathfrak{a}_{2}).$$
It is well-defined because if a' $= a + a_{1}$ and b' $= b + a_{2}$ with $a_{1} \in \mathfrak{a}_{1}$ and $a_{2} \in \mathfrak{a}_{2}$, then
$$a'b'= (a + a_{1})(b + a_{2}) = ab + ba_{1} + aa_{2} + a_{1}a_{2},$$
and so
$$a'b'\equiv ab(\mathrm{mod} \mathfrak{a}_{1} +\mathfrak{a}_{2}).$$
It is also clear that this map is bilinear, so it induces a linear map $\phi$ : $A/\mathfrak{a}_{1} \otimes A/\mathfrak{a}_{2} \to A/(\mathfrak{a}_{1} +\mathfrak{a}_{2})$ such that $\phi (\overline{a} \otimes \overline{b}) =$ ab (mod $\mathfrak{a}_{1} +\mathfrak{a}_{2})$. Next, observe that any arbitrary tensor
$$\overline{a}_{1} \otimes \overline{b}_{1} + \cdots  +\overline{a}_{n} \otimes \overline{b}_{n}$$
in $A/\mathfrak{a}_{1} \otimes A/\mathfrak{a}_{2}$ can be rewritten as
$$\overline{1} \otimes (\overline{a}_{1}\overline{b}_{1} + \cdots  +\overline{a}_{n}\overline{b}_{n}),$$
which is of the form $\overline{1} \otimes \overline{s}$, with $s \in A$. We can use this fact to show that $\phi$  is injective and surjective, and thus an isomorphism.

<!-- PAGE 1302 -->
For example, if $\phi \overline{(1} \otimes \overline{s}) = 0$, because $\phi \overline{(1} \otimes \overline{s}) = s$ (mod $\mathfrak{a}_{1} +\mathfrak{a}_{2})$, we have $s \in \mathfrak{a}_{1} +\mathfrak{a}_{2}$, so we can write $s = a + b$ with $a \in \mathfrak{a}_{1}$ and $b \in \mathfrak{a}_{2}$. Then
$$\overline{1} \otimes \overline{s}\overline{= 1} \otimes \overline{a}\overline{+}\overline{b}$$
$$\overline{= 1} \otimes (\overline{a} +\overline{b})$$
$$\overline{= 1} \otimes \overline{a}\overline{+ 1} \otimes \overline{b}$$
$$=\overline{a} \otimes \overline{1 + 1} \otimes \overline{b}$$
$$= 0 + 0 = 0,$$
since $a \in \mathfrak{a}_{1}$ and $b \in \mathfrak{a}_{2}$, which proves injectivity. Recall that the exterior algebra of an A-module $M$ is defined by
$$k$$
$$^M =M^(M).$$
$$k\ge 0$$

> **Proposition 35.27.** If $A$ is a commutative ring, then for any $n$ modules $M_{i}$, there is an isomorphism
$$nn$$
$$^(MM_{i}) \approx O^M_{i}.$$
$$i=1i=1$$
A proof can be found in Bourbaki $[25]$ (Chapter III, Section $7$, No $7$, Proposition $10)$.

> **Proposition 35.28.** Let $A$ be a commutative ring and let $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ be $n$ ideals of $A$. If the module $M$ is the direct sum of $n$ cyclic modules
$$M = A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{n},$$
$$p$$
$$then for every p > 0, the exterior power \bigwedge  M is isomorphic to the direct sum of the modules$$
$A/\mathfrak{a}_{H}$, where $H$ ranges over all subsets $H \subseteq {1, \dots  , n}$ with $p$ elements, and with
$$\mathfrak{a}_{H} = \sum_{h\in H}  \mathfrak{a}_{h}.$$

*Proof.* If $u_{i}$ is the image of $1$ in $A/\mathfrak{a}_{i}$, then $A/\mathfrak{a}_{i}$ is equal to $Au_{i}$. By Proposition 35.27, we have
$$n$$
$$^M \approx O^(Au_{i}).$$
$$i=1$$
We also have
$$k$$
$$^(Au_{i}) =M^(Au_{i}) \approx A \oplus Au_{i},$$
$$k\ge 0$$

<!-- PAGE 1303 -->
since $au_{i} \wedge bu_{i} = 0$, and it follows that
$$p$$
$$^M \approx M(Au_{k1}) \otimes \cdots  \otimes (Au_{kp}).$$
$$H\subseteq {1,...,n}$$
$$H={k1,...,kp}$$
However, by Proposition 35.26, we have
$$(Au_{k1}) \otimes \cdots  \otimes (Au_{kp}) = A/\mathfrak{a}_{k1} \otimes \cdots  \otimes A/\mathfrak{a}_{kp} \approx A/(\mathfrak{a}_{k1} + \cdots  +\mathfrak{a}_{kp}) = A/\mathfrak{a}_{H}.$$
Therefore,
$$p$$
$$^M \approx MA/\mathfrak{a}_{H},$$
$$H\subseteq {1,...,n}$$
$$|H|=p$$
as claimed. Example 35.1 continued: Recall that $M$ is the $\mathbb{Z}-module$ generated by ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject to $6e_{3} = 0, 2e_{2} = 0$. Then
$$1$$
$$^M = span{e_{1}, e_{2}, e_{3}, e_{4}}$$
$$2$$
$$^M = span{e_{1} \wedge e_{2}, e_{1} \wedge e_{3}, e_{1} \wedge e_{4}, e_{2} \wedge e_{3}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}.$$
Since $6e_{3} = 0$, each element of ${e_{1} \wedge e_{3}, e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{3}}$ is annihilated by $6\mathbb{Z} = (6)$. Since $2e_{4} = 0$, each element of ${e_{1}\wedge e_{4}, e_{2}\wedge e_{4}, e_{3}\wedge e_{4}, e_{1}\wedge e_{2}\wedge e_{4}, e_{1}\wedge e_{3}\wedge e_{4}, e_{2}\wedge e_{3}\wedge e_{4}, e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}}$ is annihilated by $2\mathbb{Z} = (2)$. We have shown that
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}$$
$$M=/(6)/(2),$$
where $\mathfrak{a}_{1} = (0) =\mathfrak{a}_{2}, \mathfrak{a}_{3} =$ (6),and $\mathfrak{a}_{4} = (2)$. Then Proposition 35.28 implies that $1 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \oplus \mathbb{Z} \mathfrak{a}_{2} \oplus \mathbb{Z} \mathfrak{a}_{3} \oplus \mathbb{Z} \mathfrak{a}_{4} \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}  \oplus \mathbb{Z}$
$$M=//// =/(6)/(2)$$
$2 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{2} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{2} \mathfrak{a}_{3}$
$$M=/( +)/( +)/( +)/( +)/( +)$$
$$\oplus \mathbb{Z}/(\mathfrak{a}_{3} +\mathfrak{a}_{4}) =\mathbb{Z} \oplus \mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(2)$$
$3 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3} \mathfrak{a}_{4}$
$$M=/( + +)/( + +)/( + +)/( + +)$$
$$=\mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}(2)$$
$4 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{3} \mathfrak{a}_{4} \mathbb{Z}$
$$M=/( + + +) =/(2).$$

<!-- PAGE 1304 -->
When the ideals $\mathfrak{a}_{i}$ form a chain of inclusions $\mathfrak{a}_{1} \subseteq \cdots  \subseteq \mathfrak{a}_{n}$, we get the following remarkable result.

> **Proposition 35.29.** Let $A$ be a commutative ring and let $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ be $n$ ideals of $A$ such that $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{n}$. If the module $M$ is the direct sum of $n$ cyclic modules
$$M = A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{n},$$
$$p$$
$$then for every p withp  1 \le p \le n, the ideal \mathfrak{a}_{p} is the annihilatorp  of the exterior power \bigwedge  M.$$
$$If \mathfrak{a}_{n} \neq  A, then \bigwedge  M \neq  (0) for p = 1, \dots  , n, and \bigwedge  M = (0) for p > n.$$

*Proof.* With the notation of Proposition 35.28, we have $\mathfrak{a}_{H} =\mathfrak{a}_{max(H)}$, where max(H) is the greatest element in the set $H$. Since max(H) $\ge p$ for any subset with $p$ elements and since max(H) $= p$ when $H = {1, \dots  , p}$, we see that
$$\mathfrak{a}_{p} = \bigcap_{\subseteq {1,...,n}  \mathfrak{a}_{H}.$$
$$H}$$
$$|H|=p$$
By Proposition 35.28, we have
$$p$$
$$^M \approx MA/\mathfrak{a}_{H}$$
$$H\subseteq {1,...,n}$$
$$|H|=p$$
$$p$$
$$which proves that \mathfrak{a}_{p} is indeed the annihilator of \bigwedge  M. The rest is clear.$$
Example 35.1 continued: Recall that $M$ is the $\mathbb{Z}-module$ generated by ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject to $6e_{3} = 0, 2e_{2} = 0$. Then
$$1$$
$$^M = span{e_{1}, e_{2}, e_{3}, e_{4}}$$
$$2$$
$$^M = span{e_{1} \wedge e_{2}, e_{1} \wedge e_{3}, e_{1} \wedge e_{4}, e_{2} \wedge e_{3}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}.$$
Since $e_{1}$ and $e_{2}$ are free, $e_{1} \wedge e_{2}$ is also free. Since $6e_{3} = 0$, each element of ${e_{1} \wedge e_{3}, e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{3}}$ is annihilated by $6\mathbb{Z} = (6)$. Since $2e_{4} = 0$, each element of ${e_{1} \wedge e_{4}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}, e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}$ is annihilated by $2\mathbb{Z} = (2)$.

<!-- PAGE 1305 -->
Then
$$1$$
$$Ann(^M) = Ann e_{1} = (0)$$
$$2$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} = (0)$$
$$3$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} \wedge e_{3} = (6)$$
$$4$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4} = (2),$$
and Proposition 35.29 provides another verification of
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}$$
$$M=/(6)/(2).$$
Propostion 35.29 immediately implies the following crucial fact.

> **Proposition 35.30.** Let $A$ be a commutative ring and let $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ be $m$ ideals of $A$ and $\mathfrak{a}_{1}', \dots  ,\mathfrak{a}_{n}'$ be $n$ ideals of $A$ such that $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$ and $\mathfrak{a}_{1}' \subseteq \mathfrak{a}_{2}' \subseteq \cdots  \subseteq \mathfrak{a}_{n}'$ ̸ $= A$ If we have an isomorphism
$$A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m} \approx A/\mathfrak{a}_{1}' \oplus \cdots  \oplus A/\mathfrak{a}_{n}',$$
then $m = n$ and $\mathfrak{a}_{i} =\mathfrak{a}_{i}'$ for $i = 1, \dots  , n$. Proposition 35.30 yields the uniqueness of the decomposition in Theorem 35.25.

> **Theorem 35.31.** (Invariant Factors Decomposition) Let $M$ be a finitely generated nontrivial A-module, where $A$ a PID. Then, $M$ is isomorphic to a direct sum of cyclic modules
$$M \approx A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
where the $\mathfrak{a}_{i}$ are proper ideals of $A$ (possibly zero) such that
$$\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A.$$
More precisely, if $\mathfrak{a}_{1} = \cdots  =\mathfrak{a}_{r} = (0)$ and $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$, then
$$M \approx A^{r}\oplus (A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}),$$
where $A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$ is the torsion submodule of $M$. The module $M$ is free iff $r = m$, and a torsion-module iff $r = 0$. In the latter case, the annihilator of $M$ is $\mathfrak{a}_{1}$. Furthermore, the integer $r$ and ideals $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$ are uniquely determined by $M$.

*Proof.* By Theorem 35.7, since $M_{tor} = A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$, we know that the dimension $r$ of the free summand only depends on $M$. The uniqueness of the sequence of ideals follows from Proposition 35.30.

<!-- PAGE 1306 -->
In view of the uniqueness part of Theorem 35.31, we make the following definition.

> **Definition 35.12.** Given a finitely generated module $M$ over a PID $A$ as in Theorem 35.31, the ideals $\mathfrak{a}_{i} = \alpha_{i} A$ are called the invariant factors of $M$. The generators $\alpha_{i}$  of these ideals (uniquely defined up to a unit) are also called the invariant factors of $M$. Proposition 35.23 can be sharpened as follows:

> **Proposition 35.32.** Let $F$ be a finitely generated free module over a PID $A$, and let $M$ be any submodule of $F$. Then, $M$ is a free module and there is a basis $(e_{1}$, ..., $e_{n})$ of $F$, some $q \le n$, and some nonzero elements $a_{1}, \dots  , a_{q} \in A$, such that $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ is a basis of $M$ and $a_{i}$ divides $a_{i+1}$ for all $i$, with $1 \le i \le q$ - $1$. Furthermore, the free module M' with basis $(e_{1}, \dots  , e_{q})$ and the ideals $a_{1}A, \dots  , a_{q}A$ are uniquely determined by $M$; the quotient module M' $/M$ is the torsion module of $F/M$, and we have an isomorphism
$$M' /M \approx A/a_{1}A \oplus \cdots  \oplus A/a_{q}A.$$

*Proof.* Since $a_{i} \neq  0$ for $i = 1, \dots  , q$, observe that
$$M'= {x \in F | (\exists \beta  \in A, \beta  \neq  0)(\beta x \in M)},$$
which shows that $M'/M$ is the torsion module of $F/M$. Therefore, M' is uniquely determined. Since
$$M = Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{q}e_{q},$$
by Proposition 35.24 we have an isomorphism
$$M' /M \approx A/a_{1}A \oplus \cdots  \oplus A/a_{q}A.$$
Now, it is possible that the first $s$ elements $a_{i}$ are units, in which case $A/a_{i}A = (0)$, so we can eliminate such factors and we get
$$M' /M \approx A/a_{s+1}A \oplus \cdots  \oplus A/a_{q}A,$$
with $a_{q}A \subseteq a_{q-1}A \subseteq \cdots  \subseteq a_{s+1}A \neq  A$. By Proposition 35.30, $q$ - $s$ and the ideals $a_{j}A$ are uniquely determined for $j = s + 1, \dots  , q$, and since $a_{1}A = \cdots  = a_{s}A = A$, the $q$ ideals $a_{i}A$ are uniquely determined. The ideals $a_{1}A, \dots  , a_{q}A$ of Proposition 35.32 are called the invariant factors of $M$ with respect to $F$. They should not be confused with the invariant factors of a module $M$. It turns out that $a_{1}, \dots  , a_{q}$ can also be computed in terms of gcd’s of minors of a certain matrix. Recall that if $X$ is an $m \times  n$ matrix, then a $k \times  k$ minor of $X$ is the determinant of any $k\times k$ matrix obtained by picking $k$ columns of $X$, and then $k$ rows from these $k$ columns.

<!-- PAGE 1307 -->

> **Proposition 35.33.** Let $F$ be a free module of finite dimension over a PID, $(u_{1}, \dots  , u_{n})$ be a basis of $F, M$ be a submodule of $F$, and $(x_{1}, \dots  , x_{m})$ be a set of generators of $M$. If $a_{1}A, \dots  , a_{q}A$ are the invariant factors of $M$ with respect to $F$ as in Proposition 35.32, then for $k = 1, \dots  , q$, the product $a_{1} \cdots  a_{k}$ is a gcd of the $k \times  k$ minors of the $n \times  m$ matrix $X_{U}$ whose columns are the coordinates of the $x_{j}$ over the $u_{i}$.

*Proof.* Proposition 35.23 shows that $M \subseteq a_{1}F$. Consequently, the coordinates of any element of $M$ are multiples of $a_{1}$. On the other hand, we know that there is a linear form $f$ for which $a_{1}A$ is a maximal ideal and some e' $\in M$ such that f(e') $= a_{1}$. If we write e' as a linear combination of the $x_{i}$, we see that $a_{1}$ belongs to the ideal spanned by the coordinates of the $x_{i}$ over the basis $(u_{1}, \dots  , u_{n})$. Since these coordinates are all multiples of $a_{1}$, it follows that $a_{1}$ is their gcd, which proves the case $k = 1$.
$$k$$
$$For any k \ge 2, consider the exterior power \bigwedge  M.Using the notationk  of the proof$$
$$of Proposition 35.23, the module M has the basis (a_{1}e_{1}, \dots  , a_{q}e_{q}), so \bigwedge  M has a basis$$
consisting of elements of the form
$$a_{i1}e_{i1} \wedge \cdots  \wedge a_{ik}e_{ik} = a_{i1} \cdots  a_{ik} e_{i1} \wedge \cdots  \wedge e_{ik},$$
for all sequences $(i_{1}, \dots  , i_{k})$ such that $1 \le i_{1} < i_{2} < \cdots  < i_{k} \le q$. However, the vectors
$$k k k$$
$$e_{i1} \wedge \cdots  \wedge e_{ik} form a basis of \bigwedge  F. Thus, the  map from \bigwedge  M into \bigwedge  F induced  by the$$
$$inclusion M \subseteq F defines an isomorphism of \bigwedge  kM onto the submodule of \bigwedge_{i}  kF having the$$
elements $a_{i1} \cdots  a_{ik} e_{i1} \wedge \cdots  \wedge e_{ik}$ as a basis. Since $a_{j}$ is a multiple of the a  for $i < j$, the products $a_{i1} \cdots  a_{ik}$ are all multiples of $\delta_{k}  = a_{1} \cdots  a_{k}$, and one of these is equal to $\delta_{k}$ . The reasoning used for $k = 1$ shows that $\delta_{k}$  is a gcd of the set of coordinates of any spanning set of $k M k F k F$
$$\bigwedge  over any basis of \bigwedge_{k}  . If we pick as basis of \bigwedge_{i1}  the wedge products u_{i1} \wedge \cdots  \wedge u_{ik},$$
$$and as generators of \bigwedge  M the wedge products x \wedge \cdots  \wedge x_{ik}, it is easy to see that the$$
coordinates of the $x_{i1} \wedge \cdots  \wedge x_{ik}$ are indeed determinants which are the $k \times  k$ minors of the matrix $X_{U}$. Proposition 35.33 yields $a_{1}, \dots  , a_{q}$ (up to units) as follows: First, $a_{1}$ is a gcd of the entries in $X_{U}$. Having computed $a_{1}, \dots  , a_{k}$, let $b_{k} = a_{1} \cdots  , a_{k}$, compute $b_{k+1} = a_{1} \cdots  a_{k}a_{k+1}$ as a gcd of all the $(k + 1) \times  (k + 1)$ minors of $X_{U}$, and then $a_{k+1}$ is obtained by dividing $b_{k+1}$ by $b_{k}$ (recall that a PID is an integral domain). We also have the following interesting result about linear maps between free modules over a PID.

> **Proposition 35.34.** Let $A$ be a PID, let $F$ be a free module of dimension $n$, F' be a free module of dimension $m$, and $f$ : $F \to$ F' be a linear map from $F$ to F'. Then, there exist a basis $(e_{1}, \dots  , e_{n})$ of $F$, a basis $(e_{1}', \dots  , e_{m}')$ of F', and some nonzero elements $\alpha_{1} , \dots  \alpha_{r}  \in A$ such that
$$($$
$$\alpha_{i} e_{i}'if 1 \le i \le r$$
$$f(e_{i}) =$$
$$0if r + 1 \le i \le n,$$

<!-- PAGE 1308 -->
and $\alpha_{1}$  | $\alpha_{2}$  | $\cdots$  | $\alpha_{r}$ . Furthermore, the ideals $\alpha_{1} A, \dots  , \alpha_{r} A$ are the invariant factors of f(F) with respect F' .

*Proof.* Let $F_{0}$ be the kernel of $f$. Since M' $=$ f(F) is a submodule of the free module F', it is free, and similarly $F_{0}$ is free as a submodule of the free module $F$ (by Proposition 35.23). By Proposition 35.2, we have
$$F = F_{0} \oplus F_{1},$$
where $F_{1}$ is a free module, and the restriction of $f$ to $F_{1}$ is an isomorphism onto M' $=$ f(F). Proposition 35.32 applied to F' and M' yields a basis $(e_{1}', \dots  , e_{m}')$ of F' such that $(\alpha_{1} e_{1}', \dots  , \alpha_{r} e_{r}')$ is a basis of M', where $\alpha_{1} A, \dots  , \alpha_{r} A$ are the invariant factors for M' with respect to F' . Since the restriction of $f$ to $F_{1}$ is and isomorphism, there is a basis $(e_{1}, \dots  , e_{r})$ of $F_{1}$ such that
$$f(e_{i}) = \alpha_{i} e_{i}',i = 1, \dots  , r.$$
We can extend this basis to a basis of $F$ by picking a basis of $F_{0}$ (a free module), which yields the desired result. The matrix version of Proposition 35.34 is the following proposition.

> **Proposition 35.35.** If $X$ is an $m\times n$ matrix of rank $r$ over a PID $A$, then there exist some invertible $n \times  n$ matrix $P$, some invertible $m \times  m$ matrix $Q$, and a $m \times  n$ matrix $D$ of the form
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
for some nonzero $\alpha_{i}  \in A$, such that
$(1) \alpha_{1}$  | $\alpha_{2}$  | $\cdots$  | $\alpha_{r}$ ,
$(2) X = QDP^{-1}$ , and
$(3)$ The $\alpha_{i} s$ are uniquely determined up to a unit. The ideals $\alpha_{1} A, \dots  , \alpha_{r} A$ are called the invariant factors of the matrix $X$. Recall that two $m \times  n$ matrices $X$ and $Y$ are equivalent iff
$$Y = QXP^{-1} ,$$
for some invertible matrices, $P$ and $Q$. Then, Proposition 35.35 implies the following fact.

<!-- PAGE 1309 -->

> **Proposition 35.36.** Two $m \times  n$ matrices $X$ and $Y$ are equivalent iff they have the same invariant factors. If $X$ is the matrix of a linear map $f$ : $F \to$ F' with respect to some basis $(u_{1}, \dots  , u_{n})$ of $F$ and some basis $(u_{1}', \dots  , u_{m}')$ of F', then the columns of $X$ are the coordinates of the $f(u_{j})$ over the $u_{i}'$, where the $f(u_{j})$ generate f(F), so Proposition 35.33 applies and yields the following result:

> **Proposition 35.37.** If $X$ is a $m \times  n$ matrix or rank $r$ over a PID $A$, and if $\alpha_{1} A, \dots  , \alpha_{r} A$ are its invariant factors, then $\alpha_{1}$  is a gcd of the entries in $X$, and for $k = 2, \dots  , r$, the product $\alpha_{1}  \cdots  \alpha_{k}$  is a gcd of all $k \times  k$ minors of $X$. There are algorithms for converting a matrix $X$ over a PID to the form $X = QDP^{-1}$ as described in Proposition 35.35. For Euclidean domains, this can be achieved by using the elementary row and column operations P(i, $k), E_{i,j;\beta}$, and $E_{i,\lambda}$ described in Chapter $8$, where we require the scalar $\lambda$  used in $E_{i,\lambda}$ to be a unit. For an arbitrary PID, another kind of elementary matrix (containing some $2 \times  2$ submatrix in addition to diagonal entries) is needed. These procedures involve computing gcd’s and use the Bezout identity to mimic division. Such methods are presented in $D$. Serre $[162]$, Jacobson $[101]$, and Van Der Waerden $[185]$, and sketched in Artin $[7]$. We describe and justify several of these methods in Section 36.5. Proposition 35.32 has the following two applications. First, consider a finitely presented module $M$ over a PID given by some $m \times  n$ matrix $R$. By Proposition 35.35, the matrix $R$ can be diagonalized as $R = QDP^{-1}$ where $D$ is a diagonal matrix. Then, we see that $M$ has a presentation with $m$ generators and $r$ relations of the form
$$\alpha_{i} e_{i} = 0,$$
where $\alpha_{i}  \neq  0$ and $\alpha_{1}$  | $\alpha_{2}$  | $\cdots$  | $\alpha_{r}$ . For the second application, let $F$ be a free module with basis $(e_{1}, \dots  , e_{n})$, and let $M$ be a submodule of $F$ generated by $m$ vectors $v_{1}, \dots  , v_{m}$ in $F$. The module $M$ can be viewed as the set of linear combinations of the columns of the $n\times m$ matrix also denoted $M$ consisting of the coordinates of the vectors $v_{1}, \dots  , v_{m}$ over the basis $(e_{1}, \dots  , e_{n})$. Then by Proposition 35.35, the matrix $R$ can be diagonalized as $R = QDP^{-1}$ where $D$ is a diagonal matrix. The columns of $Q$ form a basis $(e_{1}', \dots  , e_{n}')$ of $F$, and since $RP = QD$, the nonzero columns of $RP$ form the basis $(a_{1}e_{1}', \dots  , a_{q}e_{q}')$ of $M$. When the ring $A$ is a Euclidean domain, Theorem 36.18 shows that $P$ and $Q$ are products of elementary row and column operations. In particular, when $A = \mathbb{Z}$, in which cases our $\mathbb{Z}-modules$ are abelian groups, we can find $P$ and $Q$ using Euclidean division.
$$\mathbb{Z} \mathbb{Z}^{n}$$
If $A =$ , a finitely generated submodule $M$ of is called a lattice. It is given as the set of integral linear combinations of a finite set of integral vectors.

<!-- PAGE 1310 -->
Here is an example taken from Artin $[7]$ (Chapter $12$, Section $4)$. Let $F$ be the free $\mathbb{Z}-module \mathbb{Z}^{2}$, and let $M$ be the lattice generated by the columns of the matrix
$$R = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} .$$
The columns $(u_{1}, u_{2})$ of $R$ are linearly independent, but they are not a basis of $\mathbb{Z}^{2}$. For example, in order to obtain $e_{1}$ as a linear combination of these columns, we would need to solve the linear system
$$2x -y = 1$$
$$x + 2y = 0.$$
From the second equation, we get $x =$ -2y, which yields
$$-5y = 1.$$
But, $y = -1/5$ is not an integer. We leave it as an exercise to check that
$$\begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} ,$$
which means that
$$\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} ,$$
so $R = QDP^{-1}$ with
$$Q = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} ,D = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} ,P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} .$$
$$\mathbb{Z}^{2}$$
The new basis $(u_{1}', u_{2}')$ for consists of the columns of $Q$ and the new basis for $M$ consists of the columns $(u_{1}', 5u_{2}')$ of $QD$, where
$$QD = \begin{pmatrix} 1 & 0 \\ 3 & 5 \end{pmatrix} .$$
A picture of the lattice and its generators $(u_{1}, u_{2})$ and of the same lattice with the new basis $(u_{1}', 5u_{2}')$ is shown in Figure 35.1, where the lattice points are displayed as stars. The invariant factor decomposition of a finitely generated module $M$ over a PID $A$ given by Theorem 35.31 says that
$$M_{tor} \approx A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
a direct sum of cyclic modules, with (0)̸ $= \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m}$ ̸ $= A$. Using the Chinese Remainder Theorem (Theorem 32.16), we can further decompose each module $A/\alpha_{i} A$ into a direct sum of modules of the form $A/p^{n}A$, where $p$ is a prime in $A$.

<!-- PAGE 1311 -->
$$**$$
$$****$$
* * * *
$$**$$
$$****$$
$$**$$
$$****$$
* * * *
$$**$$
$$****$$
$$Figure 35.1: Diagonalization applied to a lattice$$

> **Theorem 35.38.** (Elementary Divisors Decomposition) Let $M$ be a finitely generated nontrivial A-module, where $A$ a PID. Then, $M$ is isomorphic to the direct sum $A^{r} \oplus M_{tor}$, where $A^{r}$ is a free module and where the torsion module $M_{tor}$ is a direct sum of cyclic modules of the form $A/p_{i}^{ni,j}$, for some primes $p_{1}, \dots  , p_{t} \in A$ and some positive integers $n_{i,j}$, such that for each $i = 1, \dots  , t$, there is a sequence of integers
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
with $s_{i} \ge 1$, and where $n_{i,j}$ occurs $m_{i,j} \ge 1$ times, for $j = 1, \dots  , s_{i}$. Furthermore, the irreducible elements $p_{i}$ and the integers $r, t, n_{i,j}, s_{i}, m_{i,j}$ are uniquely determined.

*Proof.* By Theorem 35.31, we already know that $M \approx A^{r} \oplus M_{tor}$, where $r$ is uniquely determined, and where
$$M_{tor} \approx A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
a direct sum of cyclic modules, with $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$. Then, $each\mathfrak{a}_{i}$ is a principal ideal of the form $\alpha_{i} A$, where $\alpha_{i}$  ̸ $= 0$ and $\alpha_{i}$  is not a unit. Using the Chinese Remainder Theorem (Theorem 32.16), if we factor $\alpha_{i}$  into prime factors as
$$\alpha_{i}  = up_{1}^{k1} \cdots  p_{h}^{kh} ,$$
with $k_{j} \ge 1$, we get an isomorphism
$$A/\alpha_{i} A \approx A/p_{1}^{k1} A \oplus \cdots  \oplus A/p_{h}^{kh} A.$$

<!-- PAGE 1312 -->
This implies that $M_{tor}$ is the direct sum of modules of the form $A/p_{i}^{ni,j}$, for some primes $p_{i} \in A$. To prove uniqueness, observe that the $p_{i}-primary$ component of $M_{tor}$ is the direct sum
$$(A/p_{i}^{ni,1}A)^{mi,1}\oplus \cdots  \oplus (A/p_{i}^{ni,si}A)^{mi,si},$$
and these are uniquely determined. Since $n_{i,1} < \cdots  < n_{i,si}$, we have
$$p_{i}^{ni,si}A \subseteq \cdots  \subseteq p_{i}^{ni,1}A \neq  A,$$
Proposition 35.30 implies that the irreducible elements $p_{i}$ and $n_{i,j}, s_{i}$, and $m_{i,j}$ are unique. In view of Theorem 35.38, we make the following definition.

> **Definition 35.13.** Given a finitely generated module $M$ over a PID $A$ as in Theorem 35.38, the ideals $p_{i}^{ni,j}A$ are called the elementary divisors of $M$, and the $m_{i,j}$ are their multiplicities. The ideal $(0)$ is also considered to be an elementary divisor and $r$ is its multiplicity.
Remark: Theorem 35.38 shows how the elementary divisors are obtained from the invariant factors: the elementary divisors are the prime power factors of the invariant factors. Conversely, we can get the invariant factors from the elementary divisors. We may assume that $M$ is a torsion module. Let
$$m = \max{m_{i,1} + \cdots  + m_{i,si}},$$
$$1\le i\le t$$
and construct the $t \times  m$ matrix $C = (c_{ij})$ whose ith row is the sequence
$$n_{i,si}, \dots  , n_{i,si}, \dots  , n_{i,2}, \dots  , n_{i,2}, n_{i,1}, \dots  , n_{i,1}, 0, \dots  , 0,$$
$$|{z}|{z}|{z}$$
$$mi,simi,2mi,1$$
padded with 0’s if necessary to make it of length $m$. Then, the jth invariant factor is
$$\alpha_{j} A = p_{1}^{c1j} p_{2}^{c2j} \cdots  p_{t}^{ctj} A.$$
Observe that because the last column contains at least one prime, the $\alpha_{i}$  are not units, and $\alpha_{m}$  | $\alpha_{m-1}$  | $\cdots$  | $\alpha_{1}$ , so that $\alpha_{1} A \subseteq \cdots  \subseteq \alpha_{m-1} A \subseteq \alpha_{m} A \neq  A$, as desired. From a computational point of view, finding the elementary divisors is usually practically impossible, because it requires factoring. For example, if $A =$ K[X] where $K$ is a field, such as $K =\mathbb{R}$ or $K =\mathbb{C}$, factoring amounts to finding the roots of a polynomial, but by Galois theory, in general, this is not algorithmically doable. On the other hand, the invariant factors can be computed using elementary row and column operations. It can also be shown that $A$ and the modules of the form $A/p^{n}A$ are indecomposable (with $n > 0)$. A module $M$ is said to be indecomposable if $M$ cannot be written as a direct
