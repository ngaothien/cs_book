# Inverse Matrices and Determinants


<!-- PAGE 236 -->
since $det(e_{1}, \dots  , e_{n}) = 1$. Now letting
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = B \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} ,$$
we get
$$\det(v_{1}, \dots  , v_{n}) = \det(B),$$
and since
$$\begin{pmatrix} w_{1} \\ w_{2} \\ \vdots \\ w_{n} \end{pmatrix} = A \begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} ,$$
we get
$$\det(w_{1}, \dots  , w_{n}) = \det(A) \det(v_{1}, \dots  , v_{n}) = \det(A) \det(B).$$
It should be noted that all the results of this section, up to now, also hold when $K$ is a commutative ring and not necessarily a field. We can now characterize when an $n\times n$-matrix $A$ is invertible in terms of its determinant det(A).

## 7.4 Inverse Matrices and Determinants

In the next two sections, $K$ is a commutative ring and when needed a field.

> **Definition 7.7.** Let $K$ be a commutative ring. Given a matrix $A \in M_{n}(K)$, let $A = (b_{i j})$
$$e$$
be the matrix defined such that
$$b_{i j} = (-1)^{i+j}\det(A_{j i}),$$
the cofactor of $a_{j i}$. The matrix $A$ is called the adjugate of $A$, and each matrix $A_{j i}$ is called
$$e$$
a minor of the matrix $A$. For example, if
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 237 -->
we have
$$-2-2



11$$
$$b_{11} = \det(A_{11}) = = 12b_{12} = -\det(A_{21}) = - = 6$$
$$3-33-3$$
$$11



2-2$$
$$b_{13} = \det(A_{31}) = = 0b_{21} = -\det(A_{12}) = - = 0$$
$$-2-23-3$$
$$11



11$$
$$b_{22} = \det(A_{22}) = = -6b_{23} = -\det(A_{32}) = - = 4$$
$$3-32-2$$
$$2-2



11$$
$$b_{31} = \det(A_{13}) = = 12b_{32} = -\det(A_{23}) = - = 0$$
$$3333$$
$$11$$
$$b_{33} = \det(A_{33}) = = -4,$$
$$2-2$$
we find that
$$Ae = \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} .$$
$$-$$
 Note the reversal of the indices in
$$b_{i j} = (-1)^{i+j}\det(A_{j i}).$$
Thus, $A$ is the transpose of the matrix of cofactors of elements of $A. e$ We have the following proposition.

> **Proposition 7.10.** Let $K$ be a commutative ring. For every matrix $A \in M_{n}(K)$, we have
$$AA =AA = \det(A)I_{n}.$$
$$e e$$
As a consequence, $A$ is invertible iff det(A) is invertible, and if so, $A^{-1} = (det(A))^{-1}A$.
$$e$$

*Proof.* If $A = (b_{i j})$ and $AA = (c_{i j})$, we know that the entry $c_{i j}$ in row $i$ and column $j$ of $AA$
$$e e e$$
is
$$c_{i j} = a_{i1}b_{1j} + \cdots  + a_{i k}b_{k j} + \cdots  + a_{i n}b_{n j},$$
which is equal to
$$a_{i1}(-1)^{j+1}\det(A_{j1}) + \cdots  + a_{i n}(-1)^{j+n}\det(A_{j n}).$$
If $j = i$, then we recognize the expression of the expansion of det(A) according to the $i$-th row:
$$c_{i i} = \det(A) = a_{i1}(-1)^{i+1}\det(A_{i1}) + \cdots  + a_{i n}(-1)^{i+n}\det(A_{i n}).$$
If j̸ $= i$, we can form the matrix A' by replacing the $j$-th row of $A$ by the $i$-th row of $A$. Now the matrix $A_{j k}$ obtained by deleting row $j$ and column $k$ from $A$ is equal to the matrix

<!-- PAGE 238 -->
$A_{j k}'$ obtained by deleting row $j$ and column $k$ from A', since $A$ and A' only differ by the $j$-th row. Thus,
$$\det(A_{j k}) = \det(A_{j k}'),$$
and we have
$$\det($$
$$c_{i j} = a_{i1}(-1)^{j+1}\det(A_{j1}') + \cdots  + a_{i n}(-1)^{j+n}A_{j n}').$$
However, this is the expansion of det(A') according to the $j$-th row, since the $j$-th row of A' is equal to the $i$-th row of $A$. Furthermore, since A' has two identical rows $i$ and $j$, because det is an alternating map of the rows (see an earlier remark), we have det(A') $= 0$. Thus, we have shown that $c_{i i} =$ det(A), and $c_{i j} = 0$, when $j \neq  i$, and so
$$AA = \det(A)I_{n}.$$
$$e$$
It is also obvious from the definition of $A$, that
$$e$$
$$A^{\top}=A^{\top}.$$
$$ef$$
Then applying the first part of the argument to $A^{\top}$, we have
$$A^{\top}A^{\top}= \det(A^{\top})I_{n},$$
$$f$$
and since $det(A^{\top}) =$ det(A), $A^{\top} = A^{\top}$, and $(AA)^{\top} = A^{\top}A^{\top}$, we get
$$efee$$
$$\det(A)I_{n} = A^{\top}A^{\top}= A^{\top}A^{\top}= (AA)^{\top},$$
$$fee$$
that is,
$$(AA)^{\top}= \det(A)I_{n},$$
$$e$$
which yields
$$AA = \det(A)I_{n},$$
$$e$$
since $I_{n}^{\top} = I_{n}$. This proves that
$$AA =AA = \det(A)I_{n}.$$
$$e e$$
As a consequence, if det(A) is invertible, we have $A^{-1} = (det(A))^{-1}A$. Conversely, if $A$ is
$$e$$
invertible, from $AA^{-1} = I_{n}$, by Proposition 7.9, we have det(A) $det(A^{-1}) = 1$, and det(A) is invertible. For example, we saw earlier that
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} andAe = \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} ,$$
$$--$$
