# Commuting Families of Linear Maps


<!-- PAGE 1110 -->
Remark: Proposition 31.5 can be used to give a quick proof of Theorem 15.5.

## 31.3 Commuting Families of Diagonalizable and Trian-

$$gulable Maps$$
Using Theorem 31.6, we can give a short proof about commuting diagonalizable linear maps.

> **Definition 31.4.** If $\mathcal{F}$ is a family of linear maps on a vector space $E$, we say that $\mathcal{F}$ is a commuting family iff $f \circ g = g \circ f$ for all $f, g \in F$.

> **Proposition 31.7.** Let $\mathcal{F}$ be a finite commuting family of diagonalizable linear maps on a vector space $E$. There exists a basis of $E$ such that every linear map in $\mathcal{F}$ is represented in that basis by a diagonal matrix.

*Proof.* We proceed by induction on $n =$ dim(E). If $n = 1$, there is nothing to prove. If $n > 1$, there are two cases. If all linear maps in $\mathcal{F}$ are of the form $\lambda$ id for some $\lambda  \in K$, then the proposition holds trivially. In the second case, let $f \in F$ be some linear map in $\mathcal{F}$ which is not a scalar multiple of the identity. In this case, $f$ has at least two distinct eigenvalues $\lambda_{1} , \dots  , \lambda_{k}$ , and because $f$ is diagonalizable, $E$ is the direct sum of the corresponding eigenspaces $E_{\lambda1}, \dots  , E_{\lambda k}$. For every index $i$, the eigenspace $E_{\lambda i}$ is invariant under $f$ and under every other linear map $g$ in $\mathcal{F}$, since for any $g \in F$ and any $u \in E_{\lambda i}$, because $f$ and $g$ commute, we have
$$f(g(u)) = g(f(u)) = g(\lambda_{i} u) = \lambda_{i} g(u)$$
so g(u) $\in E_{\lambda i}$. Let $\mathcal{F}_{i}$ be the family obtained by restricting each $f \in F$ to $E_{\lambda i}$. By Proposition 31.3, the minimal polynomial of every linear map $f$ | $E_{\lambda i}$ in $\mathcal{F}_{i}$ divides the minimal polynomial $m_{f}$ of $f$, and since $f$ is diagonalizable, $m_{f}$ is a product of distinct linear factors, so the minimal polynomial of $f$ | $E_{\lambda i}$ is also a product of distinct linear factors. By Theorem 31.6, the linear map $f$ | $E_{\lambda i}$ is diagonalizable. Since $k > 1$, we have $dim(E_{\lambda i}) <$ dim(E) for $i = 1, \dots  , k$, and by the induction hypothesis, for each $i$ there is a basis of $E_{\lambda i}$ over which $f$ | $E_{\lambda i}$ is represented by a diagonal matrix. Since the above argument holds for all $i$, by combining the bases of the $E_{\lambda i}$, we obtain a basis of $E$ such that the matrix of every linear map $f \in F$ is represented by a diagonal matrix.
Remark: Proposition 31.7 also holds for infinite commuting families $\mathcal{F}$ of diagonalizable linear maps, because $E$ being finite dimensional, there is a finite subfamily of linearly independent linear maps in $\mathcal{F}$ spanning $\mathcal{F}$. There is also an analogous result for commuting families of linear maps represented by upper triangular matrices. To prove this we need the following proposition.

> **Proposition 31.8.** $Let\mathcal{F}$ be a nonempty finite commuting family of triangulable linear maps on a finite-dimensional vector space $E$. Let $W$ be a proper subspace of $E$ which is invariant under $\mathcal{F}$. Then there exists a vector $u \in E$ such that:

<!-- PAGE 1111 -->
$1. u \in / W. 2$. For every $f \in F$, the vector f(u) belongs to the subspace $W \oplus$ Ku spanned by $W$ and $u$.

*Proof.* By renaming the elements of $\mathcal{F}$ if necessary, we may assume that $(f_{1}, \dots  , f_{r})$ is a basis of the subspace of End(E) spanned $by\mathcal{F}$. We prove by induction on $r$ that there exists some vector $u \in E$ such that $1. u \in / W. 2. (f_{i}$ - $\alpha_{i}$ id)(u) $\in W$ for $i = 1, \dots  , r$, for some scalars $\alpha_{i}  \in K$. Consider the base case $r = 1$. Since $f_{1}$ is triangulable, its eigenvalues all belong to $K$ since they are the diagonal entries of the triangular matrix associated with $f_{1}$ (this is the easy direction of Theorem 15.5), so the minimal polynomial of $f_{1}$ is of the form
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
where the eigenvalues $\lambda_{1} , \dots  , \lambda_{k}$  of $f_{1}$ belong to $K$. We conclude by applying Proposition 31.5. Next assume that $r \ge 2$ and that the induction hypothesis holds for $f_{1}, \dots  , f_{r-1}$. Thus, there is a vector $u_{r-1} \in E$ such that $1. u_{r-1} \in / W. 2. (f_{i}$ - $\alpha_{i} id)(u_{r-1}) \in W$ for $i = 1, \dots  , r$ - $1$, for some scalars $\alpha_{i}  \in K$. Let
$$V_{r-1} = {w \in E | (f_{i} -\alpha_{i} id)(w) \in W, i = 1, \dots  , r -1}.$$
Clearly, $W \subseteq V_{r-1}$ and $u_{r-1} \in V_{r-1}$. We claim that $V_{r-1}$ is invariant under $\mathcal{F}$. This is because, for any $v \in V_{r-1}$ and any $f \in F$, since $f$ and $f_{i}$ commute, we have
$$(f_{i} -\alpha_{i} id)(f(v)) = f((f_{i} -\alpha_{i} id)(v)),1 \le i \le r -1.$$
Now $(f_{i} -\alpha_{i}$ id)(v) $\in W$ because $v \in V_{r-1}$, and $W$ is invariant $under\mathcal{F}$, so $f(f_{i} -\alpha_{i}$ id)(v)) $\in W$, that is, $(f_{i}$ - $\alpha_{i}$ id)(f(v)) $\in W$. Consider the restriction $g_{r}$ of $f_{r}$ to $V_{r-1}$. The minimal polynomial of $g_{r}$ divides the minimal polynomial of $f_{r}$, and since $f_{r}$ is triangulable, just as we saw for $f_{1}$, the minimal polynomial of $f_{r}$ is of the form
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
where the eigenvalues $\lambda_{1} , \dots  , \lambda_{k}$  of $f_{r}$ belong to $K$, so the minimal polynomial of $g_{r}$ is of the same form. By Proposition 31.5, there is some vector $u_{r} \in V_{r-1}$ such that

<!-- PAGE 1112 -->
$1. u_{r} \in / W. 2. (g_{r}$ - $\alpha_{r} id)(u_{r}) \in W$ for some scalars $\alpha_{r}  \in K$. Now since $u_{r} \in V_{r-1}$, we have $(f_{i} -\alpha_{i} id)(u_{r}) \in W$ for $i = 1, \dots  , r -1$, so $(f_{i} -\alpha_{i} id)(u_{r}) \in W$ for $i = 1, \dots  , r$ (since $g_{r}$ is the restriction of $f_{r})$, which concludes the proof of the induction step. Finally, since every $f \in F$ is the linear combination of $(f_{1}, \dots  , f_{r})$, Condition $(2)$ of the inductive claim implies Condition $(2)$ of the proposition. We can now prove the following result.

> **Proposition 31.9.** $Let\mathcal{F}$ be a nonempty finite commuting family of triangulable linear maps on a finite-dimensional vector space $E$. There exists a basis of $E$ such that every linear map in $\mathcal{F}$ is represented in that basis by an upper triangular matrix.

*Proof.* Let $n =$ dim(E). We construct inductively a basis $(u_{1}, \dots  , u_{n})$ of $E$ such that if $W_{i}$ is the subspace spanned by $(u_{1} \dots  , u_{i})$, then for every $f \in F$,
$$f(u_{i}) = a_{1i}^{f}u_{1} + \cdots  + a_{ii}^{f}u_{i},$$
for some $a_{ij}^{f} \in K$; that is, $f(u_{i})$ belongs to the subspace $W_{i}$. We begin by applying Proposition 31.8 to the subspace $W_{0} = (0)$ to get $u_{1}$ so that for all $f \in F$,
$$f(u_{1}) = \alpha_{1}^{f} u_{1}.$$
For the induction step, since $W_{i}$ invariant $under\mathcal{F}$, we apply Proposition 31.8 to the subspace $W_{i}$, to get $u_{i+1} \in E$ such that $1. u_{i+1} \in / W_{i}. 2$. For every $f \in F$, the vector $f(u_{i+1})$ belong to the subspace spanned by $W_{i}$ and $u_{i+1}$. Condition $(1)$ implies that $(u_{1}, \dots  , u_{i}, u_{i+1})$ is linearly independent, and Condition $(2)$ means that for every $f \in F$,
$$f(u_{i+1}) = a_{1i+1}^{f}u_{1} + \cdots  + a_{i+1i+1}^{f}u_{i+1},$$
for some $a_{i+1j}^{f} \in K$, establishing the induction step. After $n$ steps, each $f \in F$ is represented by an upper triangular matrix. Observe that if $\mathcal{F}$ consists of a single linear map $f$ and if the minimal polynomial of $f$ is of the form
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
with all $\lambda_{i}  \in K$, using Proposition 31.5 instead of Proposition 31.8, the proof of Proposition 31.9 yields another proof of Theorem 15.5.
