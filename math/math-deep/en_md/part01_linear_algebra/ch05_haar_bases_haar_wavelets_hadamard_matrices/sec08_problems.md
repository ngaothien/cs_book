# Problems


<!-- PAGE 174 -->

## 5.8 Problems

Problem 5.1. (Haar extravaganza) Consider the matrix
$$W_{3,3} = \begin{pmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
$(1)$ Show that given any vector $c = (c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8})$, the result $W_{3,3}c$ of applying $W_{3,3}$ to $c$ is
$$W_{3,3}c = (c_{1} + c_{5}, c_{1} -c_{5}, c_{2} + c_{6}, c_{2} -c_{6}, c_{3} + c_{7}, c_{3} -c_{7}, c_{4} + c_{8}, c_{4} -c_{8}),$$
the last step in reconstructing a vector from its Haar coefficients.
$(2)$ Prove that the inverse of $W_{3,3}$ is $(1/2)W_{3,3}^{\top}$ . Prove that the columns and the rows of $W_{3,3}$ are orthogonal.
$(3)$ Let $W_{3,2}$ and $W_{3,1}$ be the following matrices:
$$W_{3,2} = \begin{pmatrix} 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,W_{3,1} = \begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Show that given any vector $c = (c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8})$, the result $W_{3,2}c$ of applying $W_{3,2}$ to $c$ is
$$W_{3,2}c = (c_{1} + c_{3}, c_{1} -c_{3}, c_{2} + c_{4}, c_{2} -c_{4}, c_{5}, c_{6}, c_{7}, c_{8}),$$
the second step in reconstructing a vector from its Haar coefficients, and the result $W_{3,1}c$ of applying $W_{3,1}$ to $c$ is
$$W_{3,1}c = (c_{1} + c_{2}, c_{1} -c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8}),$$
the first step in reconstructing a vector from its Haar coefficients. Conclude that
$$W_{3,3}W_{3,2}W_{3,1} = W_{3},$$

<!-- PAGE 175 -->
the Haar matrix
$$W_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & -1 & 0 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & 1 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & -1 & 0 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & -1 & 0 \\ 1 & -1 & 0 & -1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Hint. First check that
$$W_{3,2}W_{3,1} = \begin{pmatrix} W_{2} & 0_{4,4} \\ 0_{4,4} & I_{4} \end{pmatrix} ,$$
where
$$W_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$--$$
$(4)$ Prove that the columns and the rows of $W_{3,2}$ and $W_{3,1}$ are orthogonal. Deduce from this that the columns of $W_{3}$ are orthogonal, and the rows of $W_{3}^{-1}$ are orthogonal. Are the rows of $W_{3}$ orthogonal? Are the columns of $W_{3}^{-1}$ orthogonal? Find the inverse of $W_{3,2}$ and the inverse of $W_{3,1}$.
Problem 5.2. This is a continuation of Problem 5.1.
$(1)$ For any $n \ge 2$, the $2^{n} \times  2^{n}$ matrix $W_{n,n}$ is obtained form the two rows
$$1, 0, \dots  , 0, 1, 0, \dots  , 0$$
$$|{z}|{z}$$
$$2n-12n-1$$
$$1, 0, \dots  , 0, -1, 0, \dots  , 0$$
$$|{z}|{z}$$
$$2n-12n-1$$
by shifting them $2^{n-1}$ - $1$ times over to the right by inserting a zero on the left each time. Given any vector $c = (c_{1}, c_{2}, \dots  , c_{2n})$, show that $W_{n,n}c$ is the result of the last step in the process of reconstructing a vector from its Haar coefficients $c$. Prove that $W_{n,n}^{-1}  = (1/2)W_{n,n}^{\top}$, and that the columns and the rows of $W_{n,n}$ are orthogonal.
$(2)$ Given a $m \times  n$ matrix $A = (a_{ij})$ and a $p \times  q$ matrix $B = (b_{ij})$, the Kronecker product (or tensor product) $A \otimes B$ of $A$ and $B$ is the mp $\times$  nq matrix
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$

<!-- PAGE 176 -->
It can be shown (and you may use these facts without proof) that $\otimes$ is associative and that
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
whenever AC and BD are well defined. Check that
$$W_{n,n} = \begin{pmatrix} 1 \\ I_{2n-1}\otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
and that
$$W_{n} = \begin{pmatrix} 1 \\ W_{n-1} \otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Use the above to reprove that
$$W_{n,n}W_{n,n}^{\top}  = 2I_{2n}.$$
Let
$$B_{1} = 2 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$
and for $n \ge 1$,
$$B_{n+1} = 2 \begin{pmatrix} B_{n} & 0 \\ 0 & I_{2n} \end{pmatrix} .$$
Prove that
$$W_{n}^{\top}  W_{n} = B_{n},for all n \ge 1.$$
$(3)$ The matrix $W_{n,i}$ is obtained from the matrix $W_{i,i} (1 \le i \le n$ - $1)$ as follows:
$$W_{n,i} = \begin{pmatrix} W_{i,i} & 0_{2i,2n-2i} \\ 0_{2n-2i,2i} & I_{2n-2i} \end{pmatrix} .$$
It consists of four blocks, where $0_{2i,2n-2i}$ and $0_{2n-2i,2i}$ are matrices of zeros and $I_{2n-2i}$ is the identity matrix of dimension $2^{n}$ - $2^{i}$. Explain what $W_{n,i}$ does to $c$ and prove that
$$W_{n,n}W_{n,n-1} \cdots  W_{n,1} = W_{n},$$
where $W_{n}$ is the Haar matrix of dimension $2^{n}$. Hint. Use induction on $k$, with the induction hypothesis
$$W_{n,k}W_{n,k-1} \cdots  W_{n,1} = \begin{pmatrix} W_{k} & 0_{2k,2n-2k} \\ 0_{2n-2k,2k} & I_{2n-2k} \end{pmatrix} .$$

<!-- PAGE 177 -->
Prove that the columns and rows of $W_{n,k}$ are orthogonal, and use this to prove that the columns of $W_{n}$ and the rows of $W_{n}^{-1}$ are orthogonal. Are the rows of $W_{n}$ orthogonal? Are the columns of $W_{n}^{-1}$ orthogonal? Prove that
$$W_{n,k}^{-1}  = \begin{pmatrix} 1W_{k,k}^{\top} & 0_{2k,2n-2k} \\ 0_{2n-2k,2k}^{2} & I_{2n-2k} \end{pmatrix} .$$
Problem 5.3. Prove that if $H$ is a Hadamard matrix of dimension $n$, then the block matrix of dimension 2n,
$$\begin{pmatrix} H & H \\ H & -H \end{pmatrix} ,$$
is a Hadamard matrix.
Problem 5.4. Plot the graphs of the eight Walsh functions Wal(k, $t)$ for $k = 0, 1, \dots  , 7$.
Problem 5.5. Describe a recursive algorithm to compute the product $H_{2m} x$ of the Sylvester– Hadamard matrix $H_{2m}$ by a vector $x \in \mathbb{R}^{2m}$ that uses $m$ recursive calls.

<!-- PAGE 178 -->
