# The Smith Normal Form


<!-- PAGE 1338 -->
In terms of the basis $(x_{1}, x_{2}, x_{3})$, the map f(x, $y, z) = (x + y + z, y + z, z)$ has the Jordan
$$block matrix representation \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} since$$
$$f(x_{1}) = f(1, 0, 0) = (1, 0, 0) = x_{1}$$
$$f(x_{2}) = f(1, 1, 0) = (2, 1, 0) = x_{1} + x_{2}$$
$$f(x_{3}) = f(1, 0, 1) = (2, 1, 1) = x_{2} + x_{3}.$$
Combining Theorem 36.15 and Proposition 36.16, we obtain a strong version of the Jordan form.

> **Theorem 36.17.** (Jordan Canonical Form) Let $E$ be finite-dimensional $K$-vector space. The following properties are equivalent:
$(1)$ The eigenvalues of $f$ all belong to $K$.
$(2)$ There is a basis of $E$ in which the matrix of $f$ is upper (or lower) triangular.
$(3)$ There exist a basis of $E$ in which the matrix $A$ of $f$ is Jordan matrix. Furthermore, the number of Jordan blocks $J_{r}(\lambda$ ) appearing in $A$, for fixed $r$ and $\lambda$ , is uniquely determined by $f$.

*Proof.* The implication $(1) =\Rightarrow (3)$ follows from Theorem 36.15 and Proposition 36.16. The implications $(3) =\Rightarrow (2)$ and $(2) =\Rightarrow (1)$ are trivial. Compared to Theorem 31.17, the new ingredient is the uniqueness assertion in $(3)$, which is not so easy to prove. Observe that the minimal polynomial of $f$ is the least common multiple of the polynomials $(X$ - $\lambda )^{r}$ associated with the Jordan blocks $J_{r}(\lambda$ ) appearing in $A$, and the characteristic polynomial of $A$ is the product of these polynomials. We now return to the problem of computing effectively the similarity invariants of a matrix $M$. By Proposition 36.11, this is equivalent to computing the invariant factors of $XI$ - $M$. In principle, this can be done using Proposition 35.35. A procedure to do this effectively for the ring $A =$ K[X] is to convert $XI$ - $M$ to its Smith normal form. This will also yield the rational canonical form for $M$.

## 36.5 The Smith Normal Form

The Smith normal form is the special case of Proposition 35.35 applied to the PID K[X] where $K$ is a field, but it also says that the matrices $P$ and $Q$ are products of elementary matrices. It turns out that such a result holds for any Euclidean ring, and the proof is basically the same.

<!-- PAGE 1339 -->
Recall from Definition 30.10 that a Euclidean ring is an integral domain $A$ such that there exists a function $\sigma$ : $A \to \mathbb{N}$ with the following property: For all a, $b \in A$ with $b \neq  0$, there are some $q, r \in A$ such that
$$a = bq + rand\sigma (r) < \sigma (b).$$
Note that the pair $(q, r)$ is not necessarily unique. We make use of the elementary row and column operations P(i, $k), E_{i,j;\beta}$, and $E_{i,\lambda}$ described in Chapter $8$, where we require the scalar $\lambda$  used in $E_{i,\lambda}$ to be a unit.

> **Theorem 36.18.** If $M$ is an $m \times  n$ matrix over a Euclidean ring $A$, then there exist some invertible $n \times  n$ matrix $P$ and some invertible $m \times  m$ matrix $Q$, where $P$ and $Q$ are products of elementary matrices, and a $m \times  n$ matrix $D$ of the form
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
for some nonzero $\alpha_{i}  \in A$, such that
$(1) \alpha_{1}$  | $\alpha_{2}$  | $\cdots$  | $\alpha_{r}$ , and
$(2) M = QDP^{-1}$ .

*Proof.* We follow Jacobson’s proof $[101]$ (Chapter $3$, Theorem 3.8). We proceed by induction on $m + n$. If $m = n = 1$, let $P = (1)$ and $Q = (1)$. For the induction step, if $M = 0$, let $P = I_{n}$ and $Q = I_{m}$. If M̸ $= 0$, the stategy is to apply a sequence of elementary transformations that converts $M$ to a matrix of the form
$$M'  = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
where $Y$ is a $(m$ - $1) \times  (n$ - 1)-matrix such that $\alpha_{1}$  divides every entry in $Y$ . Then, we proceed by induction on $Y$ . To find M' , we perform the following steps. Step $1$. Pick some nonzero entry $a_{ij}$ in $M$ such that $\sigma (a_{ij})$ is minimal. Then permute column $j$ and column $1$, and permute row $i$ and row $1$, to bring this entry in position $(1, 1)$. We denote this new matrix again by $M$.

<!-- PAGE 1340 -->
Step 2a. If $m = 1$ go to Step 2b. If $m > 1$, then there are two possibilities:
$(i) M$ is of the form
$$\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
If $n = 1$, stop; else go to Step 2b.
(ii) There is some nonzero entry $a_{i1} (i > 1)$ below $a_{11}$ in the first column.
(a) If there is some entry $a_{k1}$ in the first column such that $a_{11}$ does not divide $a_{k1}$, then pick such an entry (say, with the smallest index $i$ such that $\sigma (a_{i1})$ is minimal), and divide $a_{k1}$ by $a_{11}$; that is, find $b_{k}$ and $b_{k1}$ such that
$$a_{k1} = a_{11}b_{k} + b_{k1},with\sigma (b_{k1}) < \sigma (a_{11}).$$
Subtract $b_{k}$ times row $1$ from row $k$ and permute row $k$ and row $1$, to obtain a matrix of the form
$$M = \begin{pmatrix} b_{k1} & b_{k2} & \cdots & b_{kn} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
Go back to Step 2a.
$(b)$ If $a_{11}$ divides every (nonzero) entry $a_{i1}$ for $i \ge 2$, say $a_{i1} = a_{11}b_{i}$, then subtract $b_{i}$ times row $1$ from row $i$ for $i = 2, \dots  , m$; go to Step 2b. Observe that whenever we return to the beginning of Step 2a, we have $\sigma (b_{k1}) < \sigma (a_{11})$. Therefore, after a finite number of steps, we must exit Step 2a with a matrix in which all entries in column $1$ but the first are zero and go to Step 2b. Step 2b. This step is reached only if $n > 1$ and if the only nonzero entry in the first column is $a_{11}$.
(a) If $M$ is of the form
$$\begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$
and $m = 1$ stop; else go to Step $3$.

<!-- PAGE 1341 -->
$(b)$ If there is some entry $a_{1k}$ in the first row such that $a_{11}$ does not divide $a_{1k}$, then pick such an entry (say, with the smallest index $j$ such that $\sigma (a_{1j})$ is minimal), and divide $a_{1k}$ by $a_{11}$; that is, find $b_{k}$ and $b_{1k}$ such that
$$a_{1k} = a_{11}b_{k} + b_{1k},with\sigma (b_{1k}) < \sigma (a_{11}).$$
Subtract $b_{k}$ times column $1$ from column $k$ and permute column $k$ and column $1$, to obtain a matrix of the form
$$M = \begin{pmatrix} b_{1k} & a_{k2} & \cdots & a_{kn} \\ b_{2k} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{mk} & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
Go back to Step 2b.
$(c)$ If $a_{11}$ divides every (nonzero) entry $a_{1j}$ for $j \ge 2$, say $a_{1j} = a_{11}b_{j}$, then subtract $b_{j}$ times column $1$ from column $j$ for $j = 2, \dots  , n$; go to Step $3$. As in Step 2a, whenever we return to the beginning of Step 2b, we have $\sigma (b_{1k}) < \sigma (a_{11})$. Therefore, after a finite number of steps, we must exit Step 2b with a matrix in which all entries in row $1$ but the first are zero. Step $3$. This step is reached only if the only nonzero entry in the first row is $a_{11}$.
$(i)$ If
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
go to Step $4$.
(ii) If Step 2b ruined column $1$ which now contains some nonzero entry below $a_{11}$, go back to Step 2a. We perform a sequence of alternating steps between Step 2a and Step 2b. Because the $\sigma$ -value of the $(1$, 1)-entry strictly decreases whenever we reenter Step 2a and Step 2b, such a sequence must terminate with a matrix of the form
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
Step $4$. If $a_{11}$ divides all entries in $Y$ , stop.

<!-- PAGE 1342 -->
Otherwise, there is some column, say $j$, such that $a_{11}$ does not divide some entry $a_{ij}$, so add the jth column to the first column. This yields a matrix of the form
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ b_{2j} \\ \vdots & Y \\ b_{mj} \end{pmatrix}$$
where the ith entry in column $1$ is nonzero, so go back to Step 2a, Again, since the $\sigma$ -value of the $(1$, 1)-entry strictly decreases whenever we reenter Step 2a and Step 2b, such a sequence must terminate with a matrix of the form
$$M'  = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
where $\alpha_{1}$  divides every entry in $Y$ . Then, we apply the induction hypothesis to $Y$ . If the PID $A$ is the polynomial ring K[X] where $K$ is a field, the $\alpha_{i}$  are nonzero polynomials, so we can apply row operations to normalize their leading coefficients to be $1$. We obtain the following theorem.

> **Theorem 36.19.** (Smith Normal Form) If $M$ is an $m \times  n$ matrix over the polynomial ring K[X], where $K$ is a field, then there exist some invertible $n\times n$ matrix $P$ and some invertible $m \times  m$ matrix $Q$, where $P$ and $Q$ are products of elementary matrices with entries in K[X], and a $m \times  n$ matrix $D$ of the form
$$D = \begin{pmatrix} q_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & q_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & q_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
for some nonzero monic polynomials $q_{i} \in$ k[X], such that
$(1) q_{1}$ | $q_{2}$ | $\cdots$  | $q_{r}$, and
$(2) M = QDP^{-1}$ .

<!-- PAGE 1343 -->
In particular, if we apply Theorem 36.19 to a matrix $M$ of the form $M = XI -A$, where $A$ is a square matrix, then det(XI $-A) = \chi_{A} (X)$ is never zero, and since $XI -A = QDP^{-1}$ with $P, Q$ invertible, all the entries in $D$ must be nonzero and we obtain the following result showing that the similarity invariants of $A$ can be computed using elementary operations.

> **Theorem 36.20.** If $A$ is an $n \times  n$ matrix over the field $K$, then there exist some invertible $n \times  n$ matrices $P$ and $Q$, where $P$ and $Q$ are products of elementary matrices with entries in K[X], and a $n \times  n$ matrix $D$ of the form
$$D = \begin{pmatrix} 1 & \cdots & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & 0 & \cdots & 0 \\ 0 & \cdots & 0 & q_{1} & 0 & \cdots & 0 \\ 0 & \cdots & 0 & 0 & q_{2} & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & q_{m} \end{pmatrix}$$
$$\cdots \cdots$$
for some nonzero monic polynomials $q_{i} \in$ k[X] of degree $\ge 1$, such that
$(1) q_{1}$ | $q_{2}$ | $\cdots$  | $q_{m}$,
$(2) q_{1}, \dots  q_{m}$ are the similarity invariants of $A$, and
$(3) XI$ - $A = QDP^{-1}$ . The matrix $D$ in Theorem 36.20 is often called Smith normal form of $A$, even though this is confusing terminology since $D$ is really the Smith normal form of $XI$ - $A$. Of course, we know from previous work that in Theorem 36.19, the $\alpha_{1} , \dots  , \alpha_{r}$  are unique, and that in Theorem 36.20, the $q_{1}, \dots  , q_{m}$ are unique. This can also be proved using some simple properties of minors, but we leave it as an exercise (for help, look at Jacobson $[101]$, Chapter $3$, Theorem 3.9). The rational canonical form of $A$ can also be obtained from $Q^{-1}$ and $D$, but first, let us consider the generalization of Theorem 36.19 to PID’s that are not necessarily Euclidean rings. We need to find a “norm” that assigns a natural number $\sigma$ (a) to any nonzero element of a PID $A$, in such a way that $\sigma$ (a) decreases whenever we return to Step 2a and Step 2b. Since a PID is a UFD, we use the number
$$\sigma (a) = k_{1} + \cdots  + k_{r}$$
of prime factors in the factorization of a nonunit element
$$a = up_{1}^{k1} \cdots  p_{r}^{kr} ,$$

<!-- PAGE 1344 -->
and we set
$$\sigma (u) = 0$$
if $u$ is a unit. We can’t divide anymore, but we can find gcd’s and use Bezout to mimic division. The key ingredient is this: for any two nonzero elements a, $b \in A$, if a does not divide $b$ then let $d \neq  0$ be a gcd of a and $b$. By Bezout, there exist $x, y \in A$ such that
$$ax + by = d.$$
We can also write $a =$ td and $b =$ -sd, for some $s, t \in A$, so that tdx - sdy $= d$, which implies that
$$tx -sy = 1,$$
since $A$ is an integral domain. Observe that
$$\begin{pmatrix} t & -s \\ -y & x \end{pmatrix} \begin{pmatrix} x & s \\ y & t \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,$$
which shows that both matrices on the left of the equation are invertible, and so is the transpose of the second one,
$$\begin{pmatrix} x & y \\ s & t \end{pmatrix}$$
(they all have determinant $1)$. We also have
$$as + bt = tds -sdt = 0,$$
so
$$\begin{pmatrix} x & y \\ s & t \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} d \\ 0 \end{pmatrix}$$
and
$$\begin{pmatrix} a & b \end{pmatrix} \begin{pmatrix} x & s \\ y & t \end{pmatrix} = \begin{pmatrix} d & 0 \end{pmatrix} .$$
Because a does not divide $b$, their gcd $d$ has strictly fewer prime factors than a, so
$$\sigma (d) < \sigma (a).$$
Using matrices of the form
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
with xt - ys $= 1$, we can modify Steps 2a and Step 2b to obtain the following theorem.

<!-- PAGE 1345 -->

> **Theorem 36.21.** If $M$ is an $m \times  n$ matrix over a PID $A$, then there exist some invertible $n \times  n$ matrix $P$ and some invertible $m \times  m$ matrix $Q$, where $P$ and $Q$ are products of elementary matrices and matrices of the form
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
with xt - ys $= 1$, and a $m \times  n$ matrix $D$ of the form
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
for some nonzero $\alpha_{i}  \in A$, such that
$(1) \alpha_{1}$  | $\alpha_{2}$  | $\cdots$  | $\alpha_{r}$ , and
$(2) M = QDP^{-1}$ . Proof sketch. In Step 2a, if $a_{11}$ does not divide $a_{k1}$, then first permute row $2$ and row $k$ (if $k \neq  2)$. Then, if we write $a = a_{11}$ and $b = a_{k1}$, if $d$ is a gcd of a and $b$ and if $x, y, s, t$ are determined as explained above, multiply on the left by the matrix
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
to obtain a matrix of the form
$$\begin{pmatrix} d & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ a_{31} & a_{32} & \cdots & a_{3n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$

<!-- PAGE 1346 -->
with $\sigma (d) < \sigma (a_{11})$. Then, go back to Step 2a. In Step 2b, if $a_{11}$ does not divide $a_{1k}$, then first permute column $2$ and column $k$ (if $k \neq  2)$. Then, if we write $a = a_{11}$ and $b = a_{1k}$, if $d$ is a gcd of a and $b$ and if $x, y, s, t$ are determined as explained above, multiply on the right by the matrix
$$\begin{pmatrix} x & s & 0 & 0 & \cdots & 0 \\ y & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
to obtain a matrix of the form
$$\begin{pmatrix} d & 0 & a_{13} & \cdots & a_{1n} \\ a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn} \end{pmatrix}$$
with $\sigma (d) < \sigma (a_{11})$. Then, go back to Step 2b. The other steps remain the same. Whenever we return to Step 2a or Step 2b, the $\sigma$ -value of the $(1$, 1)-entry strictly decreases, so the whole procedure terminates. We conclude this section by explaining how the rational canonical form of a matrix $A$ can be obtained from the canonical form $QDP^{-1}$ of $XI$ - $A$. Let $f$ : $E \to E$ be a linear map over a $K$-vector space of dimension $n$. Recall from Theorem 36.3 (see Section 36.1) that as a K[X]-module, $E_{f}$ is the image of the free module E[X] by the map $\sigma$ : E[X] $\to E_{f}$, where E[X] consists of all linear combinations of the form
$$p_{1}e_{1} + \cdots  + p_{n}e_{n},$$
where $(e_{1}, \dots  , e_{n})$ is a basis of $E$ and $p_{1}, \dots  , p_{n} \in$ K[X] are polynomials, and $\sigma$  is given by
$$\sigma (p_{1}e_{1} + \cdots  + p_{n}e_{n}) = p_{1}(f)(e_{1}) + \cdots  + p_{n}(f)(e_{n}).$$
Furthermore, the kernel of $\sigma$  is equal to the image of the map $\psi$ : E[X] $\to$ E[X], where
$$\psi (p_{1}e_{1} + \cdots  + p_{n}e_{n}) = Xp_{1}e_{1} + \cdots  + Xp_{n}e_{n} -(p_{1}f(e_{1}) + \cdots  + p_{n}(e_{n})).$$
The matrix $A$ is the representation of a linear map $f$ over the canonical basis $(e_{1}, \dots  , e_{n})$ of $E = K^{n}$, and and $XI$ - $A$ is the matrix of $\psi$  with respect to the basis $(e_{1}, \dots  , e_{n})$

<!-- PAGE 1347 -->
(over K[X]). What Theorem 36.20 tells us is that there are K[X]-bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$ of $E_{f}$ with respect to which the matrix of $\psi$  is $D$. Then
$$\psi (u_{i}) = v_{i},i = 1, \dots  , n -m,$$
$$\psi (u_{n-m+i}) = q_{i}v_{n-m+i},i = 1, \dots  , m,$$
and because $Im(\psi$ ) $=$ Ker $(\sigma$ ), this implies that
$$\sigma (v_{i}) = 0,i = 1, \dots  , n -m.$$
Consequently, $w_{1} = \sigma (v_{n-m+1}), \dots  , w_{m} = \sigma (v_{n})$ span $E_{f}$ as a K[X]-module, with $w_{i} \in E$, and we have
$$M(f) = K[X]w_{1} \oplus \cdots  \oplus K[X]w_{m},$$
where $K[X]w_{i} \approx K[X]/(q_{i})$ as a cyclic K[X]-module. Since $Im(\psi$ ) $=$ Ker $(\sigma$ ), we have
$$0 = \sigma (\psi (u_{n-m+i})) = \sigma (q_{i}v_{n-m+i}) = q_{i}\sigma (v_{n-m+i}) = q_{i}w_{i},$$
so as a $K$-vector space, the cyclic subspace $Z(w_{i}; f) = K[X]w_{i}$ has $q_{i}$ as annihilator, and by a remark from Section 36.1, it has the basis (over $K)$
$$(w_{i}, f(w_{i}), \dots  , f^{ni-1} (w_{i})),n_{i} = deg(q_{i}).$$
Furthermore, over this basis, the restriction of $f$ to $Z(w_{i}; f)$ is represented by the companion matrix of $q_{i}$. By putting all these bases together, we obtain a block matrix which is the canonical rational form of $f$ (and $A)$. Now, $XI -A = QDP^{-1}$ is the matrix of $\psi$  with respect to the canonical basis $(e_{1}, \dots  , e_{n})$ (over K[X]), and $D$ is the matrix of $\psi$  with respect to the bases $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$ (over K[X]), which tells us that the columns of $Q$ consist of the coordinates (in K[X]) of the basis vectors $(v_{1}, \dots  , v_{n})$ with respect to the basis $(e_{1}, \dots  , e_{n})$. Therefore, the coordinates (in $K)$ of the vectors $(w_{1}, \dots  , w_{m})$ spanning $E_{f}$ over K[X], where $w_{i} = \sigma (v_{n-m+i})$, are obtained by substituting the matrix $A$ for $X$ in the coordinates of the columns vectors of $Q$, and evaluating the resulting expressions. Since
$$D = Q^{-1}(XI -A)P,$$
the matrix $D$ is obtained from $A$ by a sequence of elementary row operations whose product is $Q^{-1}$ and a sequence of elementary column operations whose product is $P$. Therefore, to compute the vectors $w_{1}, \dots  , w_{m}$ from $A$, we simply have to figure out how to construct $Q$ from the sequence of elementary row operations that yield $Q^{-1}$. The trick is to use column operations to gather a product of row operations in reverse order. Indeed, if $Q^{-1}$ is the product of elementary row operations
$$Q^{-1}= E_{k} \cdots  E_{2}E_{1},$$

<!-- PAGE 1348 -->
then
$$Q = E_{1}^{-1} E_{2}^{-1}\cdots  E_{k}^{-1} .$$
Now, row operations operate on the left and column operations operate on the right, so the product $E_{1}^{-1} E_{2}^{-1} \cdots  E_{k}^{-1}$ can be computed from left to right as a sequence of column operations. Let us review the meaning of the elementary row and column operations P(i, $k), E_{i,j;\beta}$, and $E_{i,\lambda}. 1$. As a row operation, P(i, $k)$ permutes row $i$ and row $k. 2$. As a column operation, P(i, $k)$ permutes column $i$ and column $k. 3$. The inverse of P(i, $k)$ is P(i, $k)$ itself. $4$. As a row operation, $E_{i,j;\beta}$ adds $\beta$  times row $j$ to row $i. 5$. As a column operation, $E_{i,j;\beta}$ adds $\beta$  times column $i$ to column $j$ (note the switch in the indices). $6$. The inverse of $E_{i,j;\beta}$ is $E_{i,j;-\beta}. 7$. As a row operation, $E_{i,\lambda}$ multiplies row $i$ by $\lambda$ . $8$. As a column operation, $E_{i,\lambda}$ multiplies column $i$ by $\lambda$ . $9$. The inverse of $E_{i,\lambda}$ is $E_{i,\lambda-1}$. Given a square matrix $A$ (over $K)$, the row and column operations applied to $XI -A$ in converting it to its Smith normal form may involve coefficients that are polynomials and it is necessary to explain what is the action of an operation $E_{i,j;\beta}$ in this case. If the coefficient $\beta$  in $E_{i,j;\beta}$ is a polynomial over $K$, as a row operation, the action of $E_{i,j;\beta}$ on a matrix $X$ is to multiply the jth row of $M$ by the matrix $\beta (A)$ obtained by substituting the matrix $A$ for $X$ and then to add the resulting vector to row $i$. Similarly, as a column operation, the action of $E_{i,j;\beta}$ on a matrix $X$ is to multiply the ith column of $M$ by the matrix $\beta (A)$ obtained by substituting the matrix $A$ for $X$ and then to add the resulting vector to column $j$. An algorithm to compute the rational canonical form of a matrix can now be given. We apply the elementary column operations $E_{i}^{-1}$ for $i = 1, \dots  k$, starting with the identity matrix. Algorithm for Converting an $n \times  n$ matrix to Rational Canonical Form While applying elementary row and column operations to compute the Smith normal form $D$ of $XI$ - $A$, keep track of the row operations and perform the following steps: $1$. Let P' $= I_{n}$, and for every elementary row operation $E$ do the following:
$$(a) If E = P(i, k), permute column i and column k of P' .$$

<!-- PAGE 1349 -->
$$(b) If E = E_{i,j;\beta}, multiply the ith column of P'by the matrix \beta (A) obtained by$$
$$substituting the matrix A for X, and then subtract the resulting vector from$$
$$column j.$$
$$(c) If E = E_{i,\lambda} where \lambda  \in K, then multiply the ith column of P'by \lambda^{-1} .$$
$2$. When step $(1)$ terminates, the first $n$ - $m$ columns of P' are zero and the last $m$ are linearly independent. For $i = 1, \dots  , m$, multiply the $(n$ - $m +$ i)th column $w_{i}$ of P' successively by I, $A^{1}, A^{2}, A^{ni-1}$, where $n_{i}$ is the degree of the polynomial $q_{i}$ (appearing in $D)$, and form the $n \times  n$ matrix $P$ consisting of the vectors
$$w_{1}, Aw_{1}, \dots  , A^{n1-1}w_{1}, w_{2}, Aw_{2}, \dots  , A^{n2-1}w_{2}, \dots  , w_{m}, Aw_{m}, \dots  , A^{nm-1}w_{m}.$$
Then, $P^{-1}$ AP is the canonical rational form of $A$. Here is an example taken from Dummit and Foote $[55]$ (Chapter $12$, Section 12.2). Let $A$ be the matrix
$$A = \begin{pmatrix} 1 & 2 & -4 & 4 \\ 2 & -1 & 4 & -8 \\ 1 & 0 & 1 & -2 \\ 0 & 1 & 2 & 3 \end{pmatrix} .$$
$$-$$
One should check that the following sequence of row and column operations produces the Smith normal form $D$ of $XI$ - $A$: row P(1, $3)$ row $E_{1,-1}$ row $E_{2,1;2}$ row $E_{3,1;-(X-1)}$ column $E_{1,3;X-1}$ column $E_{1,4;2}$ row P(2, $4) rowE_{2,-1}$ row $E_{3,2;2}$ row $E_{4,2;-(X+1)}$ column $E_{2,3;2}$ column $E_{2,4;X-3}$, with
$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & (X-1)^{2} & 0 \\ 0 & 0 & 0 & (X & 1)^{2} \end{pmatrix} .$$
$$-$$
Then, applying Step $1$ of the above algorithm, we get the sequence of column operations: 1 $0 0$ 0 0 $0 1$ 0  $0 0 1$ 0 $0 1 0 0$ P(1,3) $0 1 0 0 E 0 1 0 0 E$   $\longrightarrow$   $\longrightarrow^{1}$ 1,-   $\longrightarrow^{2}$ 2,1,- 0 $0 1$ 0 1 $0 0$ 0 -1 $0 0$ 0       $0 0 0 1 0 0 0 1 0 0 0 1$  $0 0 1$ 0 0 $0 1$ 0 0 $0 1$ 0 $-2 1 0 0 E 0 1 0 0$ P(2,4) $0 0 0 1 E$   $3\longrightarrow^{-I}$ ,1,A   $\longrightarrow$   $\longrightarrow^{1}$ 2,- -1 $0 0$ 0 0 $0 0$ 0 0 $0 0$ 0       $0 0 0 1 0 0 0 1 0 1 0 0$ 0 $0 1$ 0 0 $-2 1$ 0 0 $0 1$ 0 $0 0 0 1 E 0 0 0 1 E 0 0 0 1$   $\longrightarrow^{2}$ 3,2,-   $4\longrightarrow^{+I}$ ,2;A   $=$ P'. 0 $0 0$ 0 0 $0 0$ 0 0 $0 0$ 0       $0 -1 0 0 0 -1 0 0 0 0 0 0$

<!-- PAGE 1350 -->
Step $2$ of the algorithm yields the vectors
$$\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} ,A \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 1 \\ 0 \end{pmatrix} , \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} ,A \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ 0 \\ 1 \end{pmatrix} ,$$
so we get
$$P = \begin{pmatrix} 1 & 1 & 0 & 2 \\ 0 & 2 & 1 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
We find that
$$P^{-1}  = \begin{pmatrix} 1 & 0 & -1 & -2 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,$$
and thus, the rational canonical form of $A$ is
$$P^{-1} AP = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
