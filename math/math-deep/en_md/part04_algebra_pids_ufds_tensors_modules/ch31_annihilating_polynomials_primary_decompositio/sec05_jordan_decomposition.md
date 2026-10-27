# Jordan Decomposition


<!-- PAGE 1119 -->

> **Definition 31.5.** If $\lambda  \in K$ is an eigenvalue of $f$, we define a generalized eigenvector of $f$ as a nonzero vector $u \in E$ such that
$$(\lambda id -f)^{r}(u) = 0,for some r \ge 1.$$
The index of $\lambda$  is defined as the smallest $r \ge 1$ such that
$$\mathrm{Ker} (\lambda id -f)^{r}= \mathrm{Ker} (\lambda id -f)^{r+1}.$$
It is clear that Ker $(\lambda$ id - $f)^{i} \subseteq$ Ker $(\lambda$ id - $f)^{i+1}$ for all $i \ge 1$. By Theorem 31.11(d), if $\lambda  = \lambda_{i}$ , the index of $\lambda_{i}$  is equal to $r_{i}$.

## 31.5 Jordan Decomposition

Recall that a linear map $g: E \to E$ is said to be nilpotent if there is some positive integer $r$ such that $g^{r} = 0$. Another important consequence of Theorem 31.11 is that $f$ can be written as the sum of a diagonalizable and a nilpotent linear map (which commute). For example $\mathbb{R}^{2} \mathbb{R}^{2}  \mathbb{R} f$ : be the -linear map f(x, $y) = (x, x + y)$ with standard matrix representation
$$X_{f} = \begin{pmatrix} \to \\ 1 & 1 \\ 0 & 1 \\ that \end{pmatrix} . A basic calculation shows that m_{f}(x) = \chi_{f} (x) = (x -1)^{2}. By Theorem 31.6$$
we know  $f$ is not diagonalizable over $\mathbb{R}$. But since the eigenvalue $\lambda_{1}  = 1$ of $f$ does belong $to\mathbb{R}$, we may use the projection construction inherent within Theorem 31.11 to write $f = D + N$, where $D$ is a diagonalizable linear map and $N$ is a nilpotent linear map. The proof of Theorem 31.10 implies that
$$p_{1}^{r1} = (x -1)^{2},g_{1} = 1 = h_{1},\pi_{1}  = g_{1}(f)h_{1}(f) = id.$$
Then $D = \lambda_{1} \pi_{1}  =$ id, $N = f$ - $D =$ f(x, $y)$ - id(x, $y) = (x, x + y)$ - $(x, y) = (0, y)$, which is equivalent to the matrix decomposition
$$X_{f} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} .$$
This example suggests that the diagonal summand of $f$ is related to the projection constructions associated with the proof of the primary decomposition theorem. If we write
$$D = \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k} ,$$
where $\pi_{i}$  is the projection from $E$ onto the subspace $W_{i}$ defined in the proof of Theorem 31.10, since
$$\pi_{1}  + \cdots  + \pi_{k}  = id,$$

<!-- PAGE 1120 -->
we have
$$f = f\pi_{1}  + \cdots  + f\pi_{k} ,$$
and so we get
$$N = f -D = (f -\lambda_{1} id)\pi_{1}  + \cdots  + (f -\lambda_{k} id)\pi_{k} .$$
We claim that $N = f$ - $D$ is a nilpotent operator. Since by construction the $\pi_{i}$  are polynomials in $f$, they commute with $f$, using the properties of the $\pi_{i}$ , we get
$$N^{r}= (f -\lambda_{1} id)^{r}\pi_{1}  + \cdots  + (f -\lambda_{k} id)^{r}\pi_{k} .$$
Therefore, if $r = max{r_{i}}$, we have $(f$ - $\lambda_{k} id)^{r} = 0$ for $i = 1, \dots  , k$, which implies that
$$N^{r}= 0.$$
It remains to show that $D$ is diagonalizable. Since $N$ is a polynomial in $f$, it commutes with $f$, and thus with $D$. From
$$D = \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k} ,$$
and
$$\pi_{1}  + \cdots  + \pi_{k}  = id,$$
we see that $D$ - $\lambda_{i}$ id $= \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k}$  - $\lambda_{i} (\pi_{1}  + \cdots  + \pi_{k}$ )
$$= (\lambda_{1}  -\lambda_{i} )\pi_{1}  + \cdots  + (\lambda_{i-1}  -\lambda_{i} )\pi_{i-1}  + (\lambda_{i+1}  -\lambda_{i} )\pi_{i+1}  + \cdots  + (\lambda_{k}  -\lambda_{i} )\pi_{k} .$$
Since the projections $\pi_{j}$  with $j \neq  i$ vanish on $W_{i}$, the above equation implies that $D$ - $\lambda_{i}$ id vanishes on $W_{i}$ and that $(D$ - $\lambda_{j} id)(W_{i}) \subseteq W_{i}$, and thus that the minimal polynomial of $D$ is
$$(X -\lambda_{1} ) \cdots  (X -\lambda_{k} ).$$
Since the $\lambda_{i}$  are distinct, by Theorem 31.6, the linear map $D$ is diagonalizable. In summary we have shown that when all the eigenvalues of $f$ belong to $K$, there exist a diagonalizable linear map $D$ and a nilpotent linear map $N$ such that
$$f = D + N$$
$$DN = ND,$$
and $N$ and $D$ are polynomials in $f$.

> **Definition 31.6.** A decomposition of $f$ as $f = D + N$ as above is called a Jordan decomposition. In fact, we can prove more: the maps $D$ and $N$ are uniquely determined by $f$.

<!-- PAGE 1121 -->

> **Theorem 31.12.** (Jordan Decomposition) Let $f$ : $E \to E$ be a linear map on the finite-dimensional vector space $E$ over the field $K$. If all the eigenvalues $\lambda_{1} , \dots  , \lambda_{k}$  of $f$ belong to $K$, then there exist a diagonalizable linear map $D$ and a nilpotent linear map $N$ such that
$$f = D + N$$
$$DN = ND.$$
Furthermore, $D$ and $N$ are uniquely determined by the above equations and they are polynomials in $f$.

*Proof.* We already proved the existence part. Suppose we also have $f =$ D' $+$ N', with D'N' $=$ N'D', where D' is diagonalizable, N' is nilpotent, and both are polynomials in $f$. We need to prove that $D =$ D' and $N =$ N'. Since D' and N' commute with one another and $f =$ D' $+$ N', we see that D' and N' commute with $f$. Then D' and N' commute with any polynomial in $f$; hence they commute with $D$ and $N$. From
$$D + N = D'+ N',$$
we get
$$D -D'= N'-N,$$
and $D$, D', $N$, N' commute with one another. Since $D$ and D' are both diagonalizable and commute, by Proposition 31.7, they are simultaneousy diagonalizable, so $D$ - D' is diagonalizable. Since $N$ and N' commute, by the binomial formula, for any $r \ge 1$,
$$(N'-N)^{r}= \sum_{j=0}^{r}  (-1)^{j} \begin{pmatrix} r \\ j \end{pmatrix} (N')^{r-j}N^{j}.$$
Since both $N$ and N' are nilpotent, we have $N^{r1} = 0$ and $(N')^{r2} = 0$, for some $r_{1}, r_{2} > 0$, so for $r \ge r_{1} + r_{2}$, the right-hand side of the above expression is zero, which shows that N' $-N$ is nilpotent. (In fact, it is easy that $r_{1} = r_{2} = n$ works). It follows that $D$ - D' $=$ N' - $N$ is both diagonalizable and nilpotent. Clearly, the minimal polynomial of a nilpotent linear map is of the form $X^{r}$ for some $r > 0$ (and $r \le$ dim(E)). But $D$ - D' is diagonalizable, so its minimal polynomial has simple roots, which means that $r = 1$. Therefore, the minimal polynomial of $D$ - D' is $X$, which says that $D$ - D' $= 0$, and then $N =$ N'. If $K$ is an algebraically closed field, then Theorem 31.12 holds. This is the case when $K = \mathbb{C}$. This theorem reduces the study of linear maps (from $E$ to itself) to the study of nilpotent operators. There is a special normal form for such operators which is discussed in the next section.
