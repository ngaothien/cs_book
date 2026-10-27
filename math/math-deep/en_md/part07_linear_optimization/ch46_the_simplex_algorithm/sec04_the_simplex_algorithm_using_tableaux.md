# The Simplex Algorithm Using Tableaux


<!-- PAGE 1625 -->

## 46.4 The Simplex Algorithm Using Tableaux

We now describe a formalism for presenting the simplex algorithm, namely (full) tableaux. This is the traditional formalism used in all books, modulo minor variations. A particularly nice feature of the tableau formalism is that the update of a tableau can be performed using elementary row operations identical to the operations used during the reduction of a matrix to row reduced echelon form (rref). What differs is the criterion for the choice of the pivot. Since the quantities $c_{j} -c_{K}\gamma_{K}^{j}$  play a crucial role in determining which column $A^{j}$ should come into the basis, the notation $\overline{c}_{j}$ is used to denote $c_{j}$ - $c_{K}\gamma_{K}^{j}$ , which is called the reduced cost of the variable $x_{j}$. The reduced costs actually depend on $K$ so to be very precise we should denote them by $(\overline{c}_{K})_{j}$, but to simplify notation we write $\overline{c}_{j}$ instead of $(\overline{c}_{K})_{j}$. We will see shortly how $(\overline{c}_{K+})_{i}$ is computed in terms of $(\overline{c}_{K})_{i}$. Observe that the data needed to execute the next step of the simplex algorithm are
$(1)$ The current basic solution $u_{K}$ and its basis $K = (k_{1}, \dots  , k_{m})$.
$(2)$ The reduced costs $\overline{c}_{j} = c_{j}$ - $c_{K}A_{K}^{-1} A^{j} = c_{j}$ - $c_{K}\gamma_{K}^{j}$ , for all $j \in / K$.
$(3)$ The vectors $\gamma_{K}^{j}  = (\gamma_{ki}^{j} )_{i=1}^{m}$ for all $j \in / K$, that allow us to express each $A^{j}$ as $A_{K}\gamma_{K}^{j}$ . All this information can be packed into a $(m + 1) \times  (n + 1)$ matrix called a (full) tableau organized as follows:
$$\frac{\overline{c}_{K}\overline{u}_{K}\overline{c}_{1}\overline{c}_{j}\overline{c}_{n}}{u_{k1}\gamma_{1}^{1} \cdots \gamma_{1}^{j} \cdots \gamma_{1}^{n}} \overline{\cdots}\overline{\cdots}$$
$$\vdots \vdots \vdots \vdots$$
$$u_{km}\gamma_{m}^{1} \cdots \gamma_{m}^{j} \cdots \gamma_{m}^{n}$$
It is convenient to think as the first row as Row $0$, and of the first column as Column $0$. Row $0$ contains the current value of the objective function and the reduced costs. Column $0$, except for its top entry, contains the components of the current basic solution $u_{K}$, and the remaining columns, except for their top entry, contain the vectors $\gamma_{K}^{j}$ . Observe that the $\gamma_{K}^{j}$  corresponding to indices $j$ in $K$ constitute a permutation of the identity matrix $I_{m}$. The entry $\gamma_{k}^{j+}$ is called the pivot element. A tableau together with the new basis $K^{+} = (K -{k^{-}})^{-} \cup {j^{+}}$ contains all the data needed to compute the new $u_{K+}$, the new $\gamma_{K+}^{j}$ , and the new reduced costs $(\overline{c}_{K+})_{j}$. If we define the $m \times  n$ matrix $\Gamma$  as the matrix $\Gamma  = [\gamma_{K}^{1}  \cdots  \gamma_{K}^{n}$ ] whose jth column is $\gamma_{K}^{j}$ , and $\overline{c}$ as the row vector $\overline{c} = (\overline{c}_{1} \cdots  \overline{c}_{n})$, then the above tableau is denoted concisely by
$$\frac{\overline{c}_{K}\overline{u}_{K}\overline{c}}{u_{K}\Gamma}$$

<!-- PAGE 1626 -->
We now show that the update of a tableau can be performed using elementary row operations identical to the operations used during the reduction of a matrix to row reduced echelon form (rref). If $K = (k_{1}, \dots  , k_{m}), j^{+}$ is the index of the incoming basis vector, $k^{-} = k_{\ell}$ is the index of the column leaving the basis, and if $K^{+} = (k_{1}, \dots  , k_{\ell-1}, j^{+}, k_{\ell+1}, \dots  , k_{m})$, since $A_{K+} = A_{K}E(\gamma_{K}^{j+}$  ), the new columns $\gamma_{K+}^{j}$  are computed in terms of the old columns $\gamma_{K}^{j}$  using $(*_{\gamma})$ and the equations
$$\gamma_{K+}^{j}  = A_{K+}^{-1}A^{j}= E(\gamma_{K}^{j+}  )^{-1}A_{K}^{-1} A^{j}= E(\gamma_{K}^{j+}  )^{-1}\gamma_{K}^{j} .$$
Consequently, the matrix $\Gamma^{+}$ is given in terms of $\Gamma$  by
$$\Gamma^{+} = E(\gamma_{K}^{j+}  )^{-1}\Gamma .$$
But the matrix $E(\gamma_{K}^{j+}  )^{-1}$ is of the form
$$E(\gamma_{K}^{j+}  )^{-1} = \begin{pmatrix} 1 & -(\gamma_{k-}^{j+} )^{-1}\gamma_{k1}^{j+} \\ \ddots & \vdots \\ 1 & -(\gamma_{k-}^{j+} )^{-1}\gamma_{k\ell-1}^{j+} \\ (\gamma_{k-}^{j+} )^{-1} \\ -(\gamma_{k-}^{j+} )^{-1}\gamma_{k\ell+1}^{j+} & 1 \\ \vdots & \ddots \\ (\gamma_{k-}^{j+} )^{-1}\gamma_{km}^{j+} & 1 \end{pmatrix} ,$$
$$-$$
with the column involving the $\gamma s$ in the $\ell$ th column, and $\Gamma^{+}$ is obtained by applying the following elementary row operations to $\Gamma$ : $1$. Multiply Row $\ell$ by $1/\gamma_{k-}^{j+}$ (the inverse of the pivot) to make the entry on Row $\ell$ and Column $j^{+}$ equal to $1. 2$. Subtract $\gamma_{ki}^{j+}  \times$  (the normalized) Row $\ell$ from Row $i$, for $i = 1, \dots  , \ell$ - $1, \ell + 1, \dots  , m$. These are exactly the elementary row operations that reduce the $\ell$ th column $\gamma_{K}^{j+}$  of $\Gamma$ to the $\ell$ th column of the identity matrix $I_{m}$. Thus, this step is identical to the sequence of steps that the procedure to convert a matrix to row reduced echelon from executes on the $\ell$ th column of the matrix. The only difference is the criterion for the choice of the pivot. Since the new basic solution $u_{K+}$ is given by $u_{K+} = A_{K+}^{-1}b$, we have
$$u_{K+} = E(\gamma_{K}^{j+}  )^{-1}A_{K}^{-1} b = E(\gamma_{K}^{j+}  )^{-1}u_{K}.$$
This means that $u_{+}$ is obtained from $u_{K}$ by applying exactly the same elementary row operations that were applied to $\Gamma$ . Consequently, just as in the procedure for reducing a

<!-- PAGE 1627 -->
matrix to rref, we can apply elementary row operations to the matrix $[u_{k} \Gamma$ ], which consists of rows $1, \dots  , m$ of the tableau. Once the new matrix $\Gamma^{+}$ is obtained, the new reduced costs are given by the following proposition.

> **Proposition 46.2.** Given any Linear Program (P2) in standard form
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
where $A$ is an $m \times  n$ matrix of rank $m$, if $(u, K)$ is a basic (not necessarily feasible) solution of (P2) and if $K^{+} = (K -{k^{-}}) \cup {j^{+}}$, with $K = (k_{1}, \dots  , k_{m})$ and $k^{-} = k_{\ell}$, then for $i = 1, \dots  , n$ we have
$$c_{i} -c_{K+}\gamma_{K+}^{i}  = c_{i} -c_{K}\gamma_{K}^{i}  - \frac{\gamma_{k-}^{i}}{\gamma_{k-}^{j+}} (c_{j+} -c_{K}\gamma_{K}^{j+}  ).$$
Using the reduced cost notation, the above equation is
$$(\overline{c}_{K+})_{i} = (\overline{c}_{K})_{i} - \frac{\gamma_{k-}^{i}}{\gamma_{k-}^{j+}} (\overline{c}_{K})_{j+}.$$

*Proof.* Without any loss of generality and to simplify notation assume that $K = (1, \dots  , m)$ and write $j$ for $j^{+}$ and $\ell$ for $k_{m}$. Since $\gamma_{K}^{i}  = A_{K}^{-1} A^{i}, \gamma_{K+}^{i}  = A_{K+}^{-1}A^{i}$, and $A_{K+} = A_{K}E(\gamma_{K}^{j}$ ), we have $c_{i}$ - $c_{K+}\gamma_{K+}^{i}  = c_{i}$ - $c_{K+}A_{K+}^{-1}A^{i} = c_{i}$ - $c_{K+}E(\gamma_{K}^{j} )^{-1}A_{K}^{-1} A^{i} = c_{i}$ - $c_{K+}E(\gamma_{K}^{j} )^{-1}\gamma_{K}^{i}$ , where
$$E(\gamma_{K}^{j} )^{-1} = \begin{pmatrix} 1 & -(\gamma_{\ell}^{j} )^{-1}\gamma_{1}^{j} \\ \ddots & \vdots \\ 1 & -(\gamma_{\ell}^{j} )^{-1}\gamma_{\ell-1}^{j} \\ (\gamma_{\ell}^{j} )^{-1} \\ -(\gamma_{\ell}^{j} )^{-1}\gamma_{\ell+1}^{j} & 1 \\ \vdots & \ddots \\ (\gamma_{\ell}^{j} )^{-1}\gamma_{m}^{j} & 1 \end{pmatrix}$$
$$-$$
where the $\ell$ th column contains the $\gamma s$. Since $c_{K+} = (c_{1}, \dots  , c_{\ell-1}, c_{j}, c_{\ell+1}, \dots  , c_{m})$, we have
$$c_{K+}E(\gamma_{K}^{j} )^{-1} = \begin{pmatrix} c_{j} & \gamma_{k}^{j} \\ c_{1}, \dots  , c_{\ell-1}, & - & c_{k} & , c_{\ell+1}, \dots  , c_{m} \\ \gamma_{\ell}^{j} & k & \ell & \gamma_{\ell}^{j} \end{pmatrix} \sum_{=1,k\neq}^{m}  ,$$

<!-- PAGE 1628 -->
and
$$c_{K+}E(\gamma_{K}^{j} )^{-1}\gamma_{K}^{i}  =c_{1}\dots c_{\ell-1} \frac{c_{j}}{\gamma_{\ell}^{j}} - \sum_{=1,k\neq}^{m}  c_{k} \frac{\gamma_{k}^{j}}{\gamma_{\ell}^{j}} c_{\ell+1}\dots c_{m}! \begin{pmatrix} \gamma_{1}^{i} \\ \vdots \\ \gamma_{\ell-1}^{i} \\ \gamma_{\ell}^{i} \\ \gamma_{\ell+1}^{i} \\ \vdots \\ \gamma_{m}^{i} \end{pmatrix}$$
$$k\ell$$
$$= \sum_{=1,k\neq}^{m}  c_{k}\gamma_{k}^{i}  + \frac{\gamma_{\ell}^{i}}{\gamma_{\ell}^{j}} \begin{pmatrix} c_{j}- & c_{k}\gamma_{k}^{j} \\ k & \ell \end{pmatrix} \sum_{=1,k\neq}^{m}$$
$$k\ell$$
$$= \sum_{=1,k\neq}^{m}  c_{k}\gamma_{k}^{i}  + \frac{\gamma_{\ell}^{i}}{\gamma_{\ell}^{j}} \begin{pmatrix} c_{j}+ c_{\ell}\gamma_{\ell}^{j} - & c_{k}\gamma_{k}^{j} \end{pmatrix} \sum_{k=1}^{m}$$
$$k\ell$$
$$= \sum_{k=1}^{m}  c_{k}\gamma_{k}^{i}  + \frac{\gamma_{\ell}^{i}}{\gamma_{\ell}^{j}} \begin{pmatrix} c_{j}- & c_{k}\gamma_{k}^{j} \end{pmatrix} \sum_{k=1}^{m}$$
$$= c_{K}\gamma_{K}^{i}  + \frac{\gamma_{\ell}^{i}}{\gamma_{\ell}^{j}} (c_{j} -c_{K}\gamma_{K}^{j} ),$$
and thus
$$c_{i} -c_{K+}\gamma_{K+}^{i}  = c_{i} -c_{K+}E(\gamma_{K}^{j} )^{-1}\gamma_{K}^{i}  = c_{i} -c_{K}\gamma_{K}^{i}  - \frac{\gamma_{\ell}^{i}}{\gamma_{\ell}^{j}} (c_{j} -c_{K}\gamma_{K}^{j} ),$$
as claimed. Since $(\gamma_{k-}^{1} , \dots  , \gamma_{k-}^{n}$ ) is the $\ell$ th row of $\Gamma$ , we see that Proposition 46.2 shows that
$$\overline{c}_{K+} =\overline{c}_{K} - \frac{(\overline{c}_{K})_{j+}}{\gamma_{k-}^{j+}} \Gamma_{\ell} ,(\dagger )$$
where $\Gamma_{\ell}$ denotes the $\ell$ -th row of $\Gamma$  and $\gamma_{k-}^{j+}$ is the pivot. This means that $\overline{c}_{K+}$ is obtained by the elementary row operations which consist of first normalizing the $\ell$ th row by dividing it by the pivot $\gamma_{k-}^{j+}$ , and then subtracting $(\overline{c}_{K})_{j+}\times$  the normalized Row $\ell from\overline{c}_{K}$. These are exactly the row operations that make the reduced cost $(\overline{c}_{K})_{j+}$ zero.
Remark: It easy easy to show that we also have
$$\overline{c}_{K+} = c -c_{K+}\Gamma^{+} .$$

<!-- PAGE 1629 -->
We saw in Section 46.2 that the change in the objective function after a pivoting step during which column $j^{+}$ comes in and column $k^{-}$ leaves is given by
$$\theta^{j+} \begin{pmatrix} c_{j+}- & \gamma_{k}^{j+} c_{k} \end{pmatrix} \sum_{k\in K}  = \theta^{j+} (\overline{c}_{K})_{j+},$$
where
$$\theta^{j+} = \frac{u_{k-}}{\gamma_{k-}^{j+}} .$$
If we denote the value of the objective function $c_{K}u_{K}$ by $z_{K}$, then we see that
$$z_{K+} = z_{K} + \frac{(\overline{c}_{K})_{j+}}{\gamma_{k-}^{j+}} u_{k-}.$$
This means that the new value $z_{K+}$ of the objective function is obtained by first normalizing the $\ell$ th row by dividing it by the pivot $\gamma_{k-}^{j+}$ , and then adding $(\overline{c}_{K})_{j+}\times$  the zeroth entry of the normalized $\ell$ th line by $(\overline{c}_{K})_{j+}$ to the zeroth entry of line $0$. In updating the reduced costs, we subtract rather than add $(\overline{c}_{K})_{j+}\times$  the normalized row $\ell$ from row $0$. This suggests storing $-z_{K}$ as the zeroth entry on line $0$ rather than $z_{K}$, because then all the entries row $0$ are updated by the same elementary row operations. Therefore, from now on, we use tableau of the form
$$\frac{\overline{c}_{K}\overline{u}_{K}\overline{c}_{1}\overline{c}_{j}\overline{c}_{n}}{u_{k1}\gamma_{1}^{1} \cdots \gamma_{1}^{j} \cdots \gamma_{1}^{n}} \overline{-}\overline{\cdots}\overline{\cdots}$$
$$\vdots \vdots \vdots \vdots$$
$$\frac{u_{km}\gamma_{m}^{1} \gamma_{m}^{j} \gamma_{m}^{n}}{firstchooses the incoming column j^{+}} \cdots \cdots$$
The simplex algorithm  by picking some column for $which\overline{c}_{j} > 0$, and then chooses the outgoing column $k^{-}$ by considering the ratios $u_{k}/\gamma_{k}^{j+}$ for which $\gamma_{k}^{j+} > 0$ (along column $j^{+})$, and picking $k^{-}$ to achieve the minimum of these ratios. Here is an illustration of the simplex algorithm using elementary row operations on an example from Papadimitriou and Steiglitz $[139]$ (Section 2.9).

> **Example 46.4.** Consider the linear program
$$maximize-2x_{2} -x_{4} -5x_{7}$$
$$subject to$$
$$x_{1} + x_{2} + x_{3} + x_{4} = 4$$
$$x_{1} + x_{5} = 2$$
$$x_{3} + x_{6} = 3$$
$$3x_{2} + x_{3} + x_{7} = 6$$
$$x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7} \ge 0.$$

<!-- PAGE 1630 -->
We have the basic feasible solution $u = (0, 0, 0, 4, 2, 3, 6)$, with $K = (4, 5, 6, 7)$. Since $c_{K} = (-1, 0, 0, -5)$ and $c = (0, -2, 0, -1, 0, 0$ - $5)$ the first tableau is
$$\frac{\overline{34}\overline{1}\overline{14}\overline{6}\overline{0}\overline{0}\overline{0}\overline{0}}{u_{4}= 41111000}$$
$$\frac{u_{5}= 21000100}{u_{6}= 30010010}$$
$$u_{7} = 60310001$$
Since $\overline{c}_{j} = c_{j}$ - $c_{K}\gamma_{K}^{j}$ , Row $0$ is obtained by subtracting $-1\times$  Row $1$ and $-5\times$  Row $4$ from $c = (0, -2, 0, -1, 0, 0, -5)$. Let us pick Column $j^{+} = 1$ as the incoming column. We have the ratios (for positive entries on Column $1)$
$$4/1, 2/1,$$
and since the minimum is $2$, we pick the outgoing column to be Column $k^{-} = 5$. The pivot $1$ is indicated in red. The new basis is $K = (4, 1, 6, 7)$. Next we apply row operations to reduce Column $1$ to the second vector of the identity matrix $I_{4}$. For this, we subtract Row $2$ from Row $1$. We get the tableau
$$\frac{\overline{34}\overline{1}\overline{14}\overline{6}\overline{0}\overline{0}\overline{0}\overline{0}}{u_{4}= 20111-100}$$
$$\frac{u_{1}= 21000100}{u_{6}= 30010010}$$
$$u_{7} = 60310001$$
To compute the new reduced costs, we want to set $\overline{c}_{1}$ to $0$, so we apply the identical row operations and subtract Row $2$ from Row $0$ to obtain the tableau
$$\frac{\overline{32}\overline{0}\overline{14}\overline{6}\overline{0}\overline{1}\overline{0}\overline{0}}{u_{4}= 20111-100}$$
$$\frac{\overline{-}}{u_{1}= 21000100}$$
$$\frac{u_{6}= 30010010}{u_{7}= 60310001}$$
Next, pick Column $j^{+} = 3$ as the incoming column. We have the ratios (for positive entries on Column $3)$
$$2/1, 3/1, 6/1,$$
and since the minimum is $2$, we pick the outgoing column to be Column $k^{-} = 4$. The pivot $1$ is indicated in red and the new basis is $K = (3, 1, 6, 7)$. Next we apply row operations to reduce Column $3$ to the first vector of the identity matrix $I_{4}$. For this, we subtract Row $1$ from Row $3$ and from Row $4$ and obtain the tableau:

<!-- PAGE 1631 -->
$$\frac{\overline{32}\overline{0}\overline{14}\overline{6}\overline{0}\overline{1}\overline{0}\overline{0}}{u_{3}= 20111-100}$$
$$\frac{\overline{-}}{u_{1}= 21000100}$$
$$\frac{u_{6}= 10101110}{u_{7}= 4020-1101} --$$
To compute the new reduced costs, we want to $set\overline{c}_{3}$ to $0$, so we subtract $6\times$  Row $1$ from Row $0$ to get the tableau
$$\frac{\overline{20}\overline{0}\overline{8}\overline{0}\overline{6}\overline{5}\overline{0}\overline{0}}{u_{3}= 20111-100}$$
$$\frac{\overline{-}}{u_{1}= 21000100}$$
$$\frac{u_{6}= 10101110}{u_{7}= 4020-1101} --$$
Next we pick $j^{+} = 2$ as the incoming column. We have the ratios (for positive entries on Column $2)$
$$2/1, 4/2,$$
and since the minimum is $2$, we pick the outgoing column to be Column $k^{-} = 3$. The pivot $1$ is indicated in red and the new basis is $K = (2, 1, 6, 7)$. Next we apply row operations to reduce Column $2$ to the first vector of the identity matrix $I_{4}$. For this, we add Row $1$ to Row $3$ and subtract $2\times$  Row $1$ from Row $4$ to obtain the tableau:
$$\frac{\overline{20}\overline{0}\overline{8}\overline{0}\overline{6}\overline{5}\overline{0}\overline{0}}{u_{2}= 20111-100}$$
$$\frac{\overline{-}}{u_{1}= 21000100}$$
$$\frac{u_{6}= 30010010}{u_{7}= 000-2-3301}$$
To compute the new reduced costs, we want to $set\overline{c}_{2}$ to $0$, so we subtract $8\times$  Row $1$ from Row $0$ to get the tableau
$$\frac{\overline{4}\overline{0}\overline{0}\overline{8}\overline{14}\overline{13}\overline{0}\overline{0}}{u_{2}= 20111-100}$$
$$\frac{\overline{-}\overline{-}}{u_{1}= 21000100}$$
$$\frac{u_{6}= 30010010}{u_{7}= 000-2-3301}$$
The only possible incoming column corresponds to $j^{+} = 5$. We have the ratios (for positive entries on Column $5)$
$$2/1, 0/3,$$

<!-- PAGE 1632 -->
and since the minimum is $0$, we pick the outgoing column to be Column $k^{-} = 7$. The pivot $3$ is indicated in red and the new basis is $K = (2, 1, 6, 5)$. Since the minimum is $0$, the basis $K = (2, 1, 6, 5)$ is degenerate (indeed, the component corresponding to the index $5$ is $0)$. Next we apply row operations to reduce Column $5$ to the fourth vector of the identity matrix $I_{4}$. For this, we multiply Row $4$ by $1/3$, and then add the normalized Row $4$ to Row $1$ and subtract the normalized Row $4$ from Row $2$ to obtain the tableau:
$$400-8-141300$$
$$u_{2} = 2011/30001/3$$
$$u_{1} = 2102/3100-1/3$$
$$u_{6} = 30010010$$
$$u_{5} = 000-2/3-1101/3$$
To compute the new reduced costs, we want to set $\overline{c}_{5}$ to $0$, so we subtract $13\times$  Row $4$ from Row $0$ to get the tableau
$$4002/3-100-13/3$$
$$u_{2} = 2011/30001/3$$
$$u_{1} = 2102/3100-1/3$$
$$u_{6} = 30010010$$
$$u_{5} = 000-2/3-1101/3$$
The only possible incoming column corresponds to $j^{+} = 3$. We have the ratios (for positive entries on Column $3)$
$$2/(1/3) = 6, 2/(2/3) = 3, 3/1 = 3,$$
and since the minimum is $3$, we pick the outgoing column to be Column $k^{-} = 1$. The pivot $2/3$ is indicated in red and the new basis is $K = (2, 3, 6, 5)$. Next we apply row operations to reduce Column $3$ to the second vector of the identity matrix $I_{4}$. For this, we multiply Row $2$ by $3/2$, subtract $(1/3)\times$  (normalized Row $2)$ from Row $1$, and subtract normalized Row $2$ from Row $3$, and add $(2/3)\times$  (normalized Row $2)$ to Row $4$ to obtain the tableau:
$$4002/3-100-13/3$$
$$u_{2} = 1-1/210-1/2001/2$$
$$u_{3} = 33/2013/200-1/2$$
$$u_{6} = 0-3/200-3/2011/2$$
$$u_{5} = 21000100$$
To compute the new reduced costs, we want to set $\overline{c}_{3}$ to $0$, so we subtract $(2/3)\times$  Row $2$ from Row $0$ to get the tableau

<!-- PAGE 1633 -->
$$2-100-200-4$$
$$u_{2} = 1-1/210-1/2001/2$$
$$u_{3} = 33/2013/200-1/2$$
$$u_{6} = 0-3/200-3/2011/2$$
$$u_{5} = 21000100$$
Since all the reduced cost are $\le 0$, we have reached an optimal solution, namely $(0, 1, 3, 0, 2, 0, 0, 0)$, with optimal value $-2$. The progression of the simplex algorithm from one basic feasible solution to another corresponds to the visit of vertices of the polyhedron $\mathcal{P}$ associated with the constraints of the linear program illustrated in Figure 46.4.
$$x$$
$$3$$
$$(0,0,3)$$
$$6$$
$$(1,0,3)$$
$$(0,1,3)$$
$$x$$
$$1 +  x$$
$$+$$
$$2 x$$
$$3     =$$
$$4$$
$$33$$
$$x  (0,2,2)$$
$$2$$
$$+ x 1$$
$$3$$
$$=$$
$$(2,0,0) 6$$
$$x$$
$$2$$
$$x      =   2$$
$$1$$
$$(0,2,0)$$
$$(2,2,0)$$
$$4=5x$$
$$1$$

![Figure 46.4](../../assets/ch46/fig_46_4.png)

**Figure 46.4:** The polytope $\mathcal{P}$ associated with the linear program optimized by the tableau method. The red arrowed path traces the progression of the simplex method from the origin to the vertex $(0, 1, 3)$. As a final comment, if it is necessary to run Phase I of the simplex algorithm, in the event that the simplex algorithm terminates with an optimal solution $(u^{*}, 0_{m})$ and a basis $K^{*}$ such that some $u_{i} = 0$, then the basis $K^{*}$ contains indices of basic columns $A^{j}$ corresponding to slack variables that need to be driven out of the basis. This is easy to achieve by performing a pivoting step involving some other column $j^{+}$ corresponding to one of the original variables (not a slack variable) for which $(\gamma_{K*} )_{i}^{j+} = 0$. In such a step, it doesn’t matter whether $(\gamma_{K*} )_{i}^{j+} < 0$ or $(\overline{c}_{K*})_{j+} \le 0$. If the original matrix $A$ has no redundant equations, such a step
