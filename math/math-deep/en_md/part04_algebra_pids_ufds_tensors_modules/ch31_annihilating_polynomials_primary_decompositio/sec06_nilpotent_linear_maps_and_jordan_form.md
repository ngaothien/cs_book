# Nilpotent Linear Maps and Jordan Form


<!-- PAGE 1122 -->

## 31.6 Nilpotent Linear Maps and Jordan Form

This section is devoted to a normal form for nilpotent maps. We follow Godement’s exposition $[79]$. Let $f$ : $E \to E$ be a nilpotent linear map on a finite-dimensional vector space over a field $K$, and assume that $f$ is not the zero map. There is a smallest positive integer $r \ge 1$ such $f^{r} \neq  0$ and $f^{r+1} = 0$. Clearly, the polynomial $X^{r+1}$ annihilates $f$, and it is the minimal polynomial of $f$ since $f^{r} \neq  0$. It follows that $r + 1 \le n =$ dim(E). Let us define the subspaces $N_{i}$ by
$$N_{i} = \mathrm{Ker} (f^{i} ),i \ge 0.$$
Note that $N_{0} = (0), N_{1} =$ Ker $(f)$, and $N_{r+1} = E$. Also, it is obvious that
$$N_{i} \subseteq N_{i+1},i \ge 0.$$

> **Proposition 31.13.** Given a nilpotent linear map $f$ with $f^{r} \neq  0$ and $f^{r+1} = 0$ as above, the inclusions in the following sequence are strict:
$$(0) = N_{0} \subset N_{1} \subset \cdots  \subset N_{r} \subset N_{r+1} = E.$$

*Proof.* We proceed by contradiction. Assume that $N_{i} = N_{i+1}$ for some $i$ with $0 \le i \le r$. Since $f^{r+1} = 0$, for every $u \in E$, we have
$$0 = f^{r+1} (u) = f^{i+1} (f^{r-i} (u)),$$
which shows that $f^{r-i} (u) \in N_{i+1}$. Since $N_{i} = N_{i+1}$, we get $f^{r-i} (u) \in N_{i}$, and thus $f^{r} (u) = 0$. Since this holds for all $u \in E$, we see that $f^{r} = 0$, a contradiction.
$$̸$$

> **Proposition 31.14.** Given a nilpotent linear map $f$ with $f^{r} = 0$ and $f^{r+1} = 0$, for any integer $i$ with $1 \le i \le r$, for any subspace $U$ of $E$, if $U \cap N_{i} = (0)$, then f(U) $\cap N_{i-1} = (0)$, and the restriction of $f$ to $U$ is an isomorphism onto f(U).

*Proof.* Pick $v \in$ f(U) $\cap N_{i-1}$. We have $v =$ f(u) for some $u \in U$ and $f^{i-1} (v) = 0$, which means that $f^{i} (u) = 0$. Then $u \in U \cap N_{i}$, so $u = 0$ since $U \cap N_{i} = (0)$, and $v =$ f(u) $= 0$. Therefore, f(U) $\cap N_{i-1} = (0)$. The restriction of $f$ to $U$ is obviously surjective on f(U). Suppose that f(u) $= 0$ for some $u \in U$. Then $u \in U \cap N_{1} \subseteq U \cap N_{i} = (0)$ (since $i \ge 1)$, so $u = 0$, which proves that $f$ is also injective on $U$.

> **Proposition 31.15.** Given a nilpotent linear map $f$ with $f^{r} \neq  0$ and $f^{r+1} = 0$, there exists a sequence of subspace $U_{1}, \dots  , U_{r+1}$ of $E$ with the following properties:
$(1) N_{i} = N_{i-1} \oplus U_{i}$, for $i = 1, \dots  , r + 1$.
$(2)$ We have $f(U_{i}) \subseteq U_{i-1}$, and the restriction of $f$ to $U_{i}$ is an injection, for $i = 2, \dots  , r+1$. See Figure 31.2.

<!-- PAGE 1123 -->
$$f$$
$$f(U r+1)$$
$$E = N^{r}4^{Ur+1}$$
$$0$$
$$N^{r}U r+1$$
$$f$$
$$f(U   )f(U     )$$
$$rr+1$$
$$N^{r}=N_{r-1}4Ur$$
$$0$$
$$N_{r-1}Ur$$
$$f$$
$$f(U_{r-1})N_{r-1}=N_{r-2}4U_{r-1}$$
$$f(U   )r$$
$$0$$
$$N_{r-2}U_{r-1}$$

![Figure 31.2](../../assets/ch31/fig_31_2.png)

**Figure 31.2:** A schematic illustration of $N_{i} = N_{i-1}\oplus U_{i}$ with $f(U_{i}) \subseteq U_{i-1}$ for $i = r+1, r$, r-1.

*Proof.* We proceed inductively, by defining the sequence $U_{r+1}, U_{r}, \dots  , U_{1}$. We pick $U_{r+1}$ to be any supplement of $N_{r}$ in $N_{r+1} = E$, so that
$$E = N_{r+1} = N_{r} \oplus U_{r+1}.$$
Since $f^{r+1} = 0$ and $N_{r} =$ Ker $(f^{r})$, we have $f(U_{r+1}) \subseteq N_{r}$, and by Proposition 31.14, as $U_{r+1} \cap N_{r} = (0)$, we have $f(U_{r+1})\cap N_{r-1} = (0)$. As a consequence, we can pick a supplement $U_{r}$ of $N_{r-1}$ in $N_{r}$ so that $f(U_{r+1}) \subseteq U_{r}$. We have
$$N_{r} = N_{r-1} \oplus U_{r}andf(U_{r+1}) \subseteq U_{r}.$$
By Proposition 31.14, $f$ is an injection from $U_{r+1}$ to $U_{r}$. Assume inductively that $U_{r+1}, \dots  , U_{i}$ have been defined for $i \ge 2$ and that they satisfy $(1)$ and $(2)$. Since
$$N_{i} = N_{i-1} \oplus U_{i},$$

<!-- PAGE 1124 -->
we have $U_{i} \subseteq N_{i}$, so $f^{i-1} (f(U_{i})) = f^{i} (U_{i}) = (0)$, which implies that $f(U_{i}) \subseteq N_{i-1}$. Also, since $U_{i} \cap N_{i-1} = (0)$, by Proposition 31.14, we have $f(U_{i})\cap N_{i-2} = (0)$. It follows that there is a supplement $U_{i-1}$ of $N_{i-2}$ in $N_{i-1}$ that contains $f(U_{i})$. We have
$$N_{i-1} = N_{i-2} \oplus U_{i-1}andf(U_{i}) \subseteq U_{i-1}.$$
The fact that $f$ is an injection from $U_{i}$ into $U_{i-1}$ follows from Proposition 31.14. Therefore, the induction step is proven. The construction stops when $i = 1$. Because $N_{0} = (0)$ and $N_{r+1} = E$, we see that $E$ is the direct sum of the $U_{i}$:
$$E = U_{1} \oplus \cdots  \oplus U_{r+1},$$
with $f(U_{i}) \subseteq U_{i-1}$, and $f$ an injection from $U_{i}$ to $U_{i-1}$, for $i = r + 1, \dots  , 2$. By a clever choice of bases in the $U_{i}$, we obtain the following nice theorem.

> **Theorem 31.16.** For any nilpotent linear map $f$ : $E \to E$ on a finite-dimensional vector space $E$ of dimension $n$ over a field $K$, there is a basis of $E$ such that the matrix $N$ of $f$ is of the form
$$N = \begin{pmatrix} 0 & \nu_{1} & 0 & \cdots & 0 & 0 \\ 0 & 0 & \nu_{2} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & \nu_{n} \\ 0 & 0 & 0 & \cdots & 0 & 0 \end{pmatrix} ,$$
where $\nu_{i}  = 1$ or $\nu_{i}  = 0$.
$$Proof. First apply Proposition 31.15 to obtain a direct sum E = \bigoplus_{i}  r=1+1 U_{i}. Then we define$$
a basis of $E$ inductively as follows. First we choose a basis
$$e_{1}^{r+1}, \dots  , e_{nr+1}^{r+1}$$
of $U_{r+1}$. Next, for $i = r + 1, \dots  , 2$, given the basis
$$e_{1}^{i}, \dots  , e_{ni}^{i}$$
of $U_{i}$, since $f$ is injective on $U_{i}$ and $f(U_{i}) \subseteq U_{i-1}$, the vectors $f(e_{1}^{i}), \dots  , f(e_{ni}^{i})$ are linearly independent, so we define a basis of $U_{i-1}$ by completing $f(e_{1}^{i}), \dots  , f(e_{ni}^{i})$ to a basis in $U_{i-1}$:
$$e_{1}^{i-1}, \dots  , e_{ni}^{i-1} , e_{ni+1}^{i-1}, \dots  , e_{ni-1}^{i-1}$$
with
$$e_{j}^{i-1}= f(e_{j}^{i}),j = 1 \dots  , n_{i}.$$
Since $U_{1} = N_{1} =$ Ker $(f)$, we have
$$f(e_{j}^{1}) = 0,j = 1, \dots  , n_{1}.$$

<!-- PAGE 1125 -->
These basis vectors can be arranged as the rows of the following matrix:
$$\begin{pmatrix} e_{1}^{r+1} & \cdots & e_{nr}^{r+1} \\ \vdots & \ddots \\ e_{1}^{r} & \cdots & e_{nr+1}^{r} & e_{nr+1+1}^{r} & \cdots & e_{nr}^{r} \\ \vdots & \vdots & \vdots & \vdots \\ e_{1}^{r-1} & \cdots & e_{nr}^{r-1} & e_{nr+1+1}^{r-1} & \cdots & e_{n}^{r-1} & e_{nr}^{r-1} & \cdots & e_{nr}^{r-1} \\ \vdots & \ddots & \vdots & \vdots & \ddots & \ddots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ e_{1}^{1} & e_{nr+1}^{1} & e_{nr+1+1}^{1} & e_{nr}^{1} & e_{nr+1}^{1} & e_{nr-1}^{1} & e_{n1}^{1} \end{pmatrix}$$
$$\cdots \cdots \cdots \cdots \cdots$$
Finally, we define the basis $(e_{1}, \dots  , e_{n})$ by listing each column of the above matrix from the bottom-up, starting with column one, then column two, etc. This means that we list the vectors $e_{j}^{i}$ in the following order: For $j = 1, \dots  , n_{r+1}$, list $e_{j}^{1}, \dots  , e_{j}^{r+1}$; In general, for $i = r, \dots  , 1$,
$$for j = n_{i+1} + 1, \dots  , n_{i}, list e_{j}^{1}, \dots  , e_{j}^{i}.$$
Then because $f(e_{j}^{1}) = 0$ and $e_{j}^{i-1} = f(e_{j}^{i})$ for $i \ge 2$, either
$$f(e_{i}) = 0orf(e_{i}) = e_{i-1},$$
which proves the theorem. As an application of Theorem 31.16, we obtain the Jordan form of a linear map.

> **Definition 31.7.** A Jordan block is an $r \times  r$ matrix $J_{r}(\lambda$ ), of the form
$$J_{r}(\lambda ) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & \lambda \end{pmatrix} ,$$
$$\cdots$$
where $\lambda  \in K$, with $J_{1}(\lambda$ ) $= (\lambda$ ) if $r = 1$. A Jordan matrix, $J$, is an $n \times  n$ block diagonal matrix of the form
$$J = \begin{pmatrix} J_{r1}(\lambda_{1} ) & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & J_{rm}(\lambda_{m} ) \end{pmatrix} ,$$
where each $J_{rk}(\lambda_{k}$ ) is a Jordan block associated with some $\lambda_{k}  \in K$, and with $r_{1}+\cdots +r_{m} = n$.

<!-- PAGE 1126 -->
To simplify notation, we often write $J(\lambda$ ) for $J_{r}(\lambda$ ). Here is an example of a Jordan matrix with four blocks:
$$J = \begin{pmatrix} \lambda & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & \lambda & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & \lambda & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & \lambda & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & \lambda & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & \lambda & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & \mu & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & \mu \end{pmatrix} .$$

> **Theorem 31.17.** (Jordan form) Let $E$ be a vector space of dimension $n$ over a field $K$ and let $f$ : $E \to E$ be a linear map. The following properties are equivalent:
$(1)$ The eigenvalues of $f$ all belong to $K$ (i.e. the roots of the characteristic polynomial $\chi_{f}$ all belong to $K)$.
$(2)$ There is a basis of $E$ in which the matrix of $f$ is a Jordan matrix.
$$Proof. Assume (1). First we apply Theorem 31.11, and we get a direct sum E = \bigoplus_{j}  k=1 W_{k},$$
such that the restriction of $g_{i} = f$ - $\lambda_{j}$ id to $W_{i}$ is nilpotent. By Theorem 31.16, there is a basis of $W_{i}$ such that the matrix of the restriction of $g_{i}$ is of the form
$$G_{i} = \begin{pmatrix} 0 & \nu_{1} & 0 & \cdots & 0 & 0 \\ 0 & 0 & \nu_{2} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & \nu_{ni} \\ 0 & 0 & 0 & \cdots & 0 & 0 \end{pmatrix} ,$$
where $\nu_{i}  = 1$ or $\nu_{i}  = 0$. Furthermore, over any basis, $\lambda_{i}$ id is represented by the diagonal matrix $D_{i}$ with $\lambda_{i}$  on the diagonal. Then it is clear that we can split $D_{i} + G_{i}$ into Jordan blocks by forming a Jordan block for every uninterrupted chain of 1s. By putting the bases of the $W_{i}$ together, we obtain a matrix in Jordan form for $f$. Now assume $(2)$. If $f$ can be represented by a Jordan matrix, it is obvious that the diagonal entries are the eigenvalues of $f$, so they all belong to $K$. Observe that Theorem 31.17 applies if $K = \mathbb{C}$. It turns out that there are uniqueness properties of the Jordan blocks. There are also other fundamental normal forms for linear maps, such as the rational canonical form, but to prove these results, it is better to develop more powerful machinery about finitely generated modules over a PID. To accomplish this most effectively, we need some basic knowledge about tensor products.

<!-- PAGE 1127 -->
If a complex $n \times  n$ matrix $A$ is expressed in terms of its Jordan decomposition as $A = D + N$, since $D$ and $N$ commute, by Proposition 9.22, the exponential of $A$ is given by
$$e^{A}= e^{D}e^{N},$$
and since $N$ is an $n \times  n$ nilpotent matrix, $N^{n-1} = 0$, so we obtain
$$e^{A}= e^{D} \begin{pmatrix} N & N^{2} & N^{n-1} \\ I+ & + & + \cdots  + \\ 1! & 2! & (n -1)! \end{pmatrix} .$$
In particular, the above applies if $A$ is a Jordan matrix. This fact can be used to solve (at least in theory) systems of first-order linear differential equations. Such systems are of the form
$$\frac{dX}{dt} = AX,(*)$$
where $A$ is an $n \times  n$ matrix and $X$ is an $n$-dimensional vector of functions of the parameter $t$. It can be shown that the columns of the matrix $e^{tA}$ form a basis of the vector space of solutions of the system of linear differential equations (*); see Artin $[7]$ (Chapter $4)$. Furthermore, for any matrix $B$ and any invertible matrix $P$, if $A = PBP^{-1}$ , then the system (*) is equivalent to
$$P^{-1} \frac{dX}{dt} = BP^{-1}X,$$
so if we make the change of variable $Y = P^{-1} X$, we obtain the system
$$\frac{dY}{dt} = BY.(**)$$
Consequently, if $B$ is such that the exponential $e^{tB}$ can be easily computed, we obtain an explicit solution $Y$ of (**) , and $X = PY$ is an explicit solution of (*). This is the case when $B$ is a Jordan form of $A$. In this case, it suffices to consider the Jordan blocks of $B$. Then we have
$$J_{r}(\lambda ) = \lambda I_{r} + \begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \lambda I_{r} + N,$$
$$\cdots$$
and the powers $N^{k}$ are easily computed. For example, if
$$B = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} = 3I_{3} + \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
