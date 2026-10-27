# How to Perform a Pivoting Step Efficiently


<!-- PAGE 1621 -->
Otherwise, $w^{*} = 0$, and $u^{*}$ is a feasible solution of (P2). Since $(u^{*}, 0_{m})$ is a basic feasible solution of $(P)$ the columns corresponding to nonzero components of $u^{*}$ are linearly
$$b$$
independent. Some of the coordinates of $u^{*}$ could be equal to $0$, but since $A$ has rank $m$ we can add columns of $A$ to obtain a basis $K^{*}$ associated with $u^{*}$, and $u^{*}$ is indeed a basic feasible solution of (P2). Running the simplex algorithm on the Linear Program $P$ to obtain an initial feasible
$$b$$
solution $(u_{0}, K_{0})$ of the linear program (P2) is called Phase I of the simplex algorithm. Running the simplex algorithm on the Linear Program (P2) with some initial feasible solution $(u_{0}, K_{0})$ is called Phase II of the simplex algorithm. If a feasible solution of the Linear Program (P2) is readily available then Phase I is skipped. Sometimes, at the end of Phase I, an optimal solution of (P2) is already obtained. In summary, we proved the following fact worth recording.

> **Proposition 46.1.** For any Linear Program (P2)
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
in standard form, where $A$ is an $m \times  n$ matrix of rank $m$ and $b \ge 0$, consider the Linear Program $(P)$ in standard form
$$b$$
$$maximize-(x_{n+1} + \cdots  + x_{n+m})$$
$$subject toAx = b andx \ge 0.$$
$$b b b$$
The simplex algorithm with a pivot rule that prevents cycling started on the basic feasible solution $x = (0_{n}, b)$ of $(P)$ terminates with an optimal solution $(u^{*}, w^{*})$.
$$b b$$
$(1)$ If $w^{*} \neq  0$, then $\mathcal{P}(A, b) = \emptyset$ , that is, the Linear Program (P2) has no feasible solution.
$(2)$ If $w^{*} = 0$, then $\mathcal{P}(A, b) \neq  \emptyset$ , and $u^{*}$ is a basic feasible solution of (P2) associated with some basis $K$. Proposition 46.1 shows that determining whether the polyhedron $\mathcal{P}(A, b)$ defined by a system of equations Ax $= b$ and inequalities $x \ge 0$ is nonempty is decidable. This decision procedure uses a fail-safe version of the simplex algorithm (that prevents cycling), and the proof that it always terminates and returns an answer is nontrivial.

## 46.3 How to Perform a Pivoting Step Efficiently

We now discuss briefly how to perform the computation of $(u^{+}, K^{+})$ from a basic feasible solution $(u, K)$. In order to avoid applying permutation matrices it is preferable to allow a basis $K$ to be a sequence of indices, possibly out of order. Thus, for any $m \times  n$ matrix $A$ (with $m \le n)$

<!-- PAGE 1622 -->
and any sequence $K = (k_{1}, k_{2}, \cdots  , k_{m})$ of $m$ elements with $k_{i} \in {1, \dots  , n}$, the matrix $A_{K}$ denotes the $m \times  m$ matrix whose ith column is the $k_{i}th$ column of $A$, and similarly for any
$$\mathbb{R}^{n} \mathbb{R}^{n}\mathbb{R}^{m}$$
vector $u \in$ (resp. any linear form $c \in$ ( $)^{*})$, the vector $u_{K} \in$ (the linear form $c_{K} \in (\mathbb{R}^{m})^{*})$ is the vector whose ith entry is the $k_{i}th$ entry in $u$ (resp. the linear whose ith entry is the $k_{i}th$ entry in $c)$. For each nonbasic $j \in / K$, we have
$$A^{j}= \gamma_{k1}^{j} A^{k1}+ \cdots  + \gamma_{km}^{j} A^{km}= A_{K}\gamma_{K}^{j} ,$$
so the vector $\gamma_{K}^{j}$  is given by $\gamma_{K}^{j}  = A_{K}^{-1} A^{j}$, that is, by solving the system
$$A_{K}\gamma_{K}^{j}  = A^{j}.(*_{\gamma})$$
To be very precise, since the vector $\gamma_{K}^{j}$  depends on $K$ its components should be denoted by $(\gamma_{K}^{j} )_{ki}$, but as we said before, to simplify notation we write $\gamma_{ki}^{j}$  instead of $(\gamma_{K}^{j} )_{ki}$. In order to decide which case applies $((A)$, (B1), (B2), (B3)), we need to compute the
$$numbers c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} for all j \in /K. For this, observe that$$
$$c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} = c_{j} -c_{K}\gamma_{K}^{j}  = c_{j} -c_{K}A_{K}^{-1} A^{j}.$$
If we write $\beta_{K}  = c_{K}A_{K}^{-1}$ , then
$$c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} = c_{j} -\beta_{K} A^{j},$$
$$\mathbb{R}^{m}$$
and we see that $\beta_{K}^{\top}  \in$ is the solution of the system $\beta_{K}^{\top}  = (A_{K}^{-1} )^{\top}c_{k}^{\top}$ , which means that $\beta_{K}^{\top}$  is the solution of the system
$$A_{K}^{\top}\beta_{K}^{\top}  = c_{K}^{\top}.(*_{\beta})$$
Remark: Observe that since $u$ is a basis feasible solution of $(P)$, we have $u_{j} = 0$ for all $j \in / K$, so $u$ is the solution of the equation $A_{K}u_{K} = b$. As a consequence, the value of the objective function for $u$ is cu $= c_{K}u_{K} = c_{K}A_{K}^{-1} b$. This fact will play a crucial role in Section 47.2 to show that when the simplex algorithm terminates with an optimal solution of the Linear Program $(P)$, then it also produces an optimal solution of the Dual Linear Program $(D)$. Assume that we have a basic feasible solution $u$, a basis $K$ for $u$, and that we also have the matrix $A_{K}$ as well its inverse $A_{K}^{-1}$ (perhaps implicitly) and also the inverse $(A_{K}^{\top})^{-1}$ of $A_{K}^{\top}$ (perhaps implicitly). Here is a description of an iteration step of the simplex algorithm, following almost exactly Chvatal (Chvatal $[40]$, Chapter $7$, Box 7.1). An Iteration Step of the (Revised) Simplex Method

<!-- PAGE 1623 -->
$$Step 1. Compute the numbers c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} = c_{j} -\beta_{K} A^{j}for all j \in /K, and for this,$$
compute $\beta_{K}^{\top}$  as the solution of the $system^{\in K}$
$$A_{K}^{\top}\beta_{K}^{\top}  = c_{K}^{\top}.$$
If $c_{j}$ - $\beta_{K} A^{j} \le 0$ for all $j \in / K$, stop and return the optimal solution $u$ (Case $(A))$. Step $2$. If Case $(B)$ arises, use a pivot rule to determine which index $j^{+} \in / K$ should enter the new basis $K^{+}$ (the condition $c_{j+}$ - $\beta_{K} A^{j+} > 0$ should hold). Step $3$. Compute $max_{k\in K} \gamma_{k}^{j+}$  . For this, solve the linear system
$$A_{K}\gamma_{K}^{j+}  = A^{j+}.$$
Step $4$. If $max_{k\in K} \gamma_{k}^{j+} \le 0$, then stop and report that Linear Program $(P)$ is unbounded (Case (B1)). Step $5$. If $max_{k\in K} \gamma_{k}^{j+} > 0$, use the ratios $u_{k}/\gamma_{k}^{j+}$ for all $k \in K$ such that $\gamma_{k}^{j+} > 0$ to compute $\theta^{j+}$ , and use a pivot rule to determine which index $k^{-} \in K$ such that $\theta^{j+} = u_{k-}/\gamma_{k-}^{j+}$ should leave $K$ (Case (B2)). If $max_{k\in K} \gamma_{k}^{j+} = 0$, then use a pivot rule to determine which index $k^{-}$ for which $\gamma_{k-}^{j+} > 0$ should leave the basis $K$ (Case (B3)). Step $6$. Update $u, K$, and $A_{K}$, to $u^{+}$ and $K^{+}$, and $A_{K+}$. During this step, given the basis $K$ specified by the sequence $K = (k_{1}, \dots  , k_{\ell}, \dots  , k_{m})$, with $k^{-} = k_{\ell}$, then $K^{+}$ is the sequence obtained by replacing $k_{\ell}$ by the incoming index $j^{+}$, so $K^{+} = (k_{1}, \dots  , j^{+}, \dots  , k_{m})$ with $j^{+}$ in the $\ell$ th slot. The vector $u$ is easily updated. To compute $A_{K+}$ from $A_{K}$ we take advantage of the fact that $A_{K}$ and $A_{K+}$ only differ by a single column, namely the $\ell$ th column $A^{j+}$, which is given by the linear combination
$$A^{j+}= A_{K}\gamma_{K}^{j+}  .$$
To simplify notation, denote $\gamma_{K}^{j+}$  by $\gamma$ , and recall that $k^{-} = k_{\ell}$. If $K = (k_{1}, \dots  , k_{m})$, then
$$\cdots \cdots$$
$A_{K} = [A^{k1}  A^{k-}  A^{im}]$, and since $A_{K+}$ is the result of replacing the $\ell$ th column $A^{k-}$ of $A_{K}$ by the column $A^{j+}$, we have
$$A_{K+} = [A^{k1}\cdots  A^{j+}\cdots  A^{im}] = [A^{k1}\cdots  A_{K}\gamma  \cdots  A^{im}] = A_{K}E(\gamma ),$$
where $E(\gamma$ ) is the following invertible matrix obtained from the identity matrix $I_{m}$ by replacing its $\ell$ th column by $\gamma$ :
$$E(\gamma ) = \begin{pmatrix} 1 & \gamma_{1} \\ \ddots & \vdots \\ 1 & \gamma_{\ell-1} \\ \gamma_{\ell} \\ \gamma_{\ell+1} & 1 \\ \vdots & \ddots \\ \gamma_{m} & 1 \end{pmatrix} .$$

<!-- PAGE 1624 -->
Since $\gamma_{\ell} = \gamma_{k-}^{j+} > 0$, the matrix $E(\gamma$ ) is invertible, and it is easy to check that its inverse is given by
$$E(\gamma )^{-1} = \begin{pmatrix} 1 & -\gamma_{\ell}^{-1} \gamma_{1} \\ \ddots & \vdots \\ 1 & -\gamma_{\ell}^{-1} \gamma_{\ell-1} \\ \gamma_{\ell}^{-1} \\ -\gamma_{\ell}^{-1} \gamma_{\ell+1} & 1 \\ \vdots & \ddots \\ \gamma_{\ell}^{-1} \gamma_{m} & 1 \end{pmatrix} ,$$
$$-$$
which is very cheap to compute. We also have
$$A_{K+}^{-1} = E(\gamma )^{-1}A_{K}^{-1} .$$
Consequently, if $A_{K}$ and $A_{K}^{-1}$ are available, then $A_{K+}$ and $A_{K+}^{-1}$ can be computed cheaply in terms of $A_{K}$ and $A_{K}^{-1}$ and matrices of the form $E(\gamma$ ). Then the systems $(*_{\gamma})$ to find the vectors $\gamma_{K}^{j}$  can be solved cheaply. Since
$$A_{K+}^{\top} = E(\gamma )^{\top}A_{K}^{\top}$$
and
$$(A_{K+}^{\top})^{-1}= (A_{K}^{\top})^{-1}(E(\gamma )^{\top})^{-1},$$
$$can also be computed cheaply from$$
the matrices $A_{K+}^{\top}$ and $(A_{K+}^{\top})^{-1}  A_{K}^{\top}, (A_{K}^{\top})^{-1}$, and matrices of the form $E(\gamma )^{\top}$. Thus the systems $(*_{\beta})$ to find the linear forms $\beta_{K}$  can also be solved cheaply. A matrix of the form $E(\gamma$ ) is called an eta matrix; see Chvatal $[40]$ (Chapter $7)$. We showed that the matrix $A_{Ks}$ obtained after $s$ steps of the simplex algorithm can be written as
$$A_{Ks} = A_{Ks-1}E_{s}$$
for some eta matrix $E_{s}$, so $A_{ks}$ can be written as the product
$$A_{Ks} = E_{1}E_{2} \cdots  E_{s}$$
of $s$ eta matrices. Such a factorization is called an eta factorization. The eta factorization can be used to either invert $A_{Ks}$ or to solve a system of the form $A_{Ks}\gamma  = A^{j+}$ iteratively. Which method is more efficient depends on the sparsity of the $E_{i}$. In summary, there are cheap methods for finding the next basic feasible solution $(u^{+}, K^{+})$ from $(u, K)$. We simply wanted to give the reader a flavor of these techniques. We refer the reader to texts on linear programming for detailed presentations of methods for implementing efficiently the simplex method. In particular, the revised simplex method is presented in Chvatal $[40]$, Papadimitriou and Steiglitz $[139]$, Bertsimas and Tsitsiklis $[21]$, and Vanderbei $[187]$.
