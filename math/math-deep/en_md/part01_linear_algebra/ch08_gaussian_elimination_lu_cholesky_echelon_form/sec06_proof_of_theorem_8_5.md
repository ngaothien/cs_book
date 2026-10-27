# Proof of Theorem 8.5


<!-- PAGE 283 -->
$$⊛$$

## 8.6 Proof of Theorem 8.5


*Proof.* $(1)$ The only part that has not been proven is the uniqueness part (when $P =$ I). Assume that $A$ is invertible and that $A = L_{1}U_{1} = L_{2}U_{2}$, with $L_{1}, L_{2}$ unit lower-triangular and $U_{1}, U_{2}$ upper-triangular. Then we have
$$L_{2}^{-1} L_{1} = U_{2}U_{1}^{-1} .$$
However, it is obvious that $L_{2}^{-1}$ is lower-triangular and that $U_{1}^{-1}$ is upper-triangular, and so $L_{2}^{-1} L_{1}$ is lower-triangular and $U_{2}U_{1}^{-1}$ is upper-triangular. Since the diagonal entries of $L_{1}$ and $L_{2}$ are $1$, the above equality is only possible if $U_{2}U_{1}^{-1} =$ I, that is, $U_{1} = U_{2}$, and so $L_{1} = L_{2}$.
$(2)$ When $P =$ I, we have $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n-1}^{-1}$, where $E_{k}$ is the product of $n$ - $k$ elementary matrices of the form $E_{i,k;-\ell i}$, where $E_{i,k;-\ell i}$ subtracts $\ell_{i}$  times row $k$ from row $i$, with $\ell_{ik}  = a_{ik}^{(k)} /a_{kk}^{(k)} , 1 \le k \le n$ - $1$, and $k + 1 \le i \le n$. Then it is immediately verified that
$$E_{k} = \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -\ell_{k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} ,$$
$$\cdots -\cdots$$
and that
$$E_{k}^{-1}= \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} .$$
$$\cdots \cdots$$
If we define $L_{k}$ by
$$L_{k} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & \vdots & 0 \\ \ell_{21} & 1 & 0 & 0 & 0 & \vdots & 0 \\ \ell_{31} & \ell_{32} & \ddots & 0 & 0 & \vdots & 0 \\ \vdots & \vdots & \ddots & 1 & 0 & \vdots & 0 \\ \ell_{k+11} & \ell_{k+12} & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & 0 & \vdots & 0 \\ \ell_{n1} & \ell_{n2} & \ell_{nk} & 0 & 1 \end{pmatrix}$$
$$\cdots \cdots$$
for $k = 1, \dots  , n$ - $1$, we easily check that $L_{1} = E_{1}^{-1}$ , and that
$$L_{k} = L_{k-1}E_{k}^{-1} ,2 \le k \le n -1,$$

<!-- PAGE 284 -->
because multiplication on the right by $E_{k}^{-1}$ adds $\ell_{i}$  times column $i$ to column $k$ (of the matrix $L_{k-1})$ with $i > k$, and column $i$ of $L_{k-1}$ has only the nonzero entry $1$ as its ith element. Since
$$L_{k} = E_{1}^{-1}\cdots  E_{k}^{-1} ,1 \le k \le n -1,$$
we conclude that $L = L_{n-1}$, proving our claim about the shape of $L. (3)$ Step $1$. Prove $(\dagger_{1}$ ). First we prove by induction on $k$ that
$$A_{k+1} = E_{k}^{k} \cdots  E_{1}^{k}P_{k} \cdots  P_{1}A,k = 1, \dots  , n -2.$$
For $k = 1$, we have $A_{2} = E_{1}P_{1}A = E_{1}^{1}P_{1}A$, since $E_{1}^{1} = E_{1}$, so our assertion holds trivially. Now if $k \ge 2$,
$$A_{k+1} = E_{k}P_{k}A_{k},$$
and by the induction hypothesis,
$$A_{k} = E_{k-1}^{k-1} \cdots  E_{2}^{k-1}E_{1}^{k-1}P_{k-1} \cdots  P_{1}A.$$
Because $P_{k}$ is either the identity or a transposition, $P_{k}^{2}  =$ I, so by inserting occurrences of $P_{k}P_{k}$ as indicated below we can write
$$A_{k+1} = E_{k}P_{k}A_{k}$$
$$= E_{k}P_{k}E_{k-1}^{k-1} \cdots  E_{2}^{k-1}E_{1}^{k-1}P_{k-1} \cdots  P_{1}A$$
$$= E_{k}P_{k}E_{k-1}^{k-1}(P_{k}P_{k}) \cdots  (P_{k}P_{k})E_{2}^{k-1}(P_{k}P_{k})E_{1}^{k-1}(P_{k}P_{k})P_{k-1} \cdots  P_{1}A$$
$$= E_{k}(P_{k}E_{k-1}^{k-1}P_{k}) \cdots  (P_{k}E_{2}^{k-1}P_{k})(P_{k}E_{1}^{k-1}P_{k})P_{k}P_{k-1} \cdots  P_{1}A.$$
Observe that $P_{k}$ has been “moved” to the right of the elimination steps. However, by definition,
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},j = 1, \dots  , k -1$$
$$E_{k}^{k} = E_{k},$$
so we get
$$A_{k+1} = E_{k}^{k}E_{k-1}^{k} \cdots  E_{2}^{k}E_{1}^{k}P_{k} \cdots  P_{1}A,$$
establishing the induction hypothesis. For $k = n$ - $2$, we get
$$U = A_{n-1} = E_{n-1}^{n-1} \cdots  E_{1}^{n-1}P_{n-1} \cdots  P_{1}A,$$
as claimed, and the factorization $PA = LU$ with
$$P = P_{n-1} \cdots  P_{1}$$
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}$$

<!-- PAGE 285 -->
is clear. Step $2$. Prove that the matrices $(E_{j}^{k} )^{-1}$ are lower-triangular. To achieve this, we prove that the matrices $\mathcal{E}_{j}^{k}$ are strictly lower triangular matrices of a very special form. Since for $j = 1, \dots  , n$ - $2$, we have $E_{j}^{j} = E_{j}$,
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},k = j + 1, \dots  , n -1,$$
since $E_{n-1}^{n-1} = E_{n-1}$ and $P_{k}^{-1} = P_{k}$, we get $(E_{j}^{j})^{-1} = E_{j}^{-1}$ for $j = 1, \dots  , n$ - $1$, and for $j = 1, \dots  , n$ - $2$, we have
$$(E_{j}^{k} )^{-1}= P_{k}(E_{j}^{k-1})^{-1}P_{k},k = j + 1, \dots  , n -1.$$
Since
$$(E_{j}^{k-1})^{-1}= I +\mathcal{E}_{j}^{k-1}$$
and $P_{k} =$ P(k, $i)$ is a transposition or $P_{k} =$ I, so $P_{k}^{2}  =$ I, and we get $(E_{j}^{k} )^{-1} = P_{k}(E_{j}^{k-1})^{-1}P_{k} = P_{k}(I +\mathcal{E}_{j}^{k-1})P_{k} = P_{k}^{2} + P_{k} \mathcal{E}_{j}^{k-1} P_{k} =$ I $+ P_{k}\mathcal{E}_{j}^{k-1} P_{k}$. Therefore, we have
$$(E_{j}^{k} )^{-1}= I + P_{k} \mathcal{E}_{j}^{k-1}P_{k},1 \le j \le n -2, j + 1 \le k \le n -1.$$
We prove for $j = 1, \dots  , n$ - $1$, that for $k = j, \dots  , n$ - $1$, each $\mathcal{E}_{j}^{k}$ is a lower triangular matrix of the form
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$
and that
$$\mathcal{E}_{j}^{k} = P_{k} \mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
with $P_{k} =$ I or $P_{k} =$ P(k, $i)$ for some $i$ such that $k + 1 \le i \le n$. For each $j (1 \le j \le n$ - $1)$ we proceed by induction on $k = j, \dots  , n$ - $1$. Since $(E_{j}^{j})^{-1} = E_{j}^{-1}$ and since $E_{j}^{-1}$ is of the above form, the base case holds. For the induction step, we only need to consider the case where $P_{k} =$ P(k, $i)$ is a transposition, since the case where $P_{k} =$ I is trivial. We have to figure out what $P_{k}\mathcal{E}_{j}^{k-1} P_{k} =$

<!-- PAGE 286 -->
P(k, $i)\mathcal{E}_{j}^{k-1}$ P(k, $i)$ is. However, since
$$\mathcal{E}_{j}^{k-1}= \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1}^{(k-1)} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k-1)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$
and because $k + 1 \le i \le n$ and $j \le k$ - $1$, multiplying $\mathcal{E}_{j}^{k-1}$ on the right by P(k, $i)$ will permute columns $i$ and $k$, which are columns of zeros, so
$$P(k, i)\mathcal{E}_{j}^{k-1}P(k, i) = P(k, i)\mathcal{E}_{j}^{k-1},$$
and thus,
$$(E_{j}^{k} )^{-1}= I + P(k, i)\mathcal{E}_{j}^{k-1}.$$
But since
$$(E_{j}^{k} )^{-1}= I +\mathcal{E}_{j}^{k} ,$$
we deduce that
$$\mathcal{E}_{j}^{k} = P(k, i)\mathcal{E}_{j}^{k-1}.$$
We also know that multiplying $\mathcal{E}_{j}^{k-1}$ on the left by P(k, $i)$ will permute rows $i$ and $k$, which shows that $\mathcal{E}_{j}^{k}$ has the desired form, as claimed. Since all $\mathcal{E}_{j}^{k}$ are strictly lower triangular, all $(E_{j}^{k} )^{-1} =$ I $+\mathcal{E}_{j}^{k}$ are lower triangular, so the product
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}$$
is also lower triangular. Step $3$. Express $L$ as $L =$ I $+ \Lambda_{n-1}$ , with $\Lambda_{n-1}  =\mathcal{E}_{1}^{1} + \cdots  +\mathcal{E}_{n-1}^{n-1}$. From Step $1$ of Part $(3)$, we know that
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1}.$$
We prove by induction on $k$ that
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k}^{k})^{-1}$$
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
for $k = 1, \dots  , n$ - $1$.

<!-- PAGE 287 -->
If $k = 1$, we have $E_{1}^{1} = E_{1}$ and
$$E_{1} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ -\ell_{21}^{(1)} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 1 \end{pmatrix} .$$
$$-\cdots$$
We also get
$$(E_{1}^{-1} )^{-1} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ \ell_{21}^{(1)} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 1 \end{pmatrix} = I + \Lambda_{1} .$$
$$\cdots$$
Since $(E_{1}^{-1} )^{-1} =$ I $+\mathcal{E}_{1}^{1}$, we find that we get $\Lambda_{1}  =\mathcal{E}_{1}^{1}$, and the base step holds. Since $(E_{j}^{k} )^{-1} =$ I $+\mathcal{E}_{j}^{k}$ with
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
and $\mathcal{E}_{i}^{k} \mathcal{E}_{j}^{k} = 0$ if $i < j$, as in part $(2)$ for the computation involving the products of $L_{k}’s$, we get
$$(E_{1}^{k-1})^{-1}\cdots  (E_{k-1}^{k-1})^{-1}= I +\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1},2 \le k \le n.(*)$$
Similarly, from the fact that $\mathcal{E}_{j}^{k-1}$ P(k, $i) =\mathcal{E}_{j}^{k-1}$ if $i \ge k + 1$ and $j \le k$ - $1$ and since
$$(E_{j}^{k} )^{-1}= I + P_{k}\mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
we get
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}= I + P_{k}(\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1}),2 \le k \le n -1.(**)$$
By the induction hypothesis,
$$I + \Lambda_{k-1}  = (E_{1}^{k-1})^{-1}\cdots  (E_{k-1}^{k-1})^{-1},$$
and from (*), we get
$$\Lambda_{k-1}  =\mathcal{E}_{1}^{k-1}+ \cdots  +\mathcal{E}_{k-1}^{k-1}.$$
Using (**), we deduce that
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}= I + P_{k}\Lambda_{k-1} .$$
