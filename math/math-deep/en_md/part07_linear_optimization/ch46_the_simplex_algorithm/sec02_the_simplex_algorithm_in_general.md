# The Simplex Algorithm in General


<!-- PAGE 1614 -->
In the first case, the point $(1 + \theta , \theta , 0, 3)$ is a feasible solution for all $\theta  \ge 0$ and the value of the objective function if $1 + \theta$ , and in the second case, the point $(1$ - $\theta , 0, \theta , 3$ - $\theta$ ) is a feasible solution iff0 $\le \theta  \le 1$ and the value of the objective function is $1$ - $\theta$ . This time, we are in the situation where the points
$$(1 + \theta , \theta , 0, 3) = (1, 0, 0, 3) + \theta (1, 1, 0, 0),\theta  \ge 0$$
form an infinite ray in the set of feasible solutions, and the objective function $1 + \theta$  is unbounded from above on this ray. This indicates that our linear program, although feasible, is unbounded. Let us now describe a step of the simplex algorithm in general.

## 46.2 The Simplex Algorithm in General

We assume that we already have an initial vertex $u_{0}$ to start from. This vertex corresponds to a basic feasible solution with basis $K_{0}$. We will show later that it is always possible to find a basic feasible solution of a Linear Program $(P)$ is standard form, or to detect that $(P)$ has no feasible solution. The idea behind the simplex algorithm is this: Given a pair $(u, K)$ consisting of a basic feasible solution $u$ and a basis $K$ for $u$, find another pair $(u^{+}, K^{+})$ consisting of another basic feasible solution $u^{+}$ and a basis $K^{+}$ for $u^{+}$, such that $K^{+}$ is obtained from $K$ by deleting some basic index $k^{-} \in K$ and adding some nonbasic index $j^{+} \in / K$, in such a way that the value of the objective function increases (preferably strictly). The step which consists in swapping the vectors $A^{k-}$ and $A^{j+}$ is called a pivoting step. Let $u$ be a given vertex corresponds to a basic feasible solution with basis $K$. Since the $m$ vectors $A^{k}$ corresponding to indices $k \in K$ are linearly independent, they form a basis, so for every nonbasic $j \in / K$, we write
$$A^{j}= \sum_{k\in K}  \gamma_{k}^{j} A^{k}.(*)$$
$$\mathbb{R}^{m}$$
We let $\gamma_{K}^{j}  \in$ be the vector given by $\gamma_{K}^{j}  = (\gamma_{k}^{j} )_{k\in K}$. Actually, since the vector $\gamma_{K}^{j}$  depends on $K$, to be very precise we should denote its components by $(\gamma_{K}^{j} )_{k}$, but to simplify notation we usually write $\gamma_{k}^{j}$  instead of $(\gamma_{K}^{j} )_{k}$ (unless confusion arises). We will explain later how the coefficients $\gamma_{k}^{j}$  can be computed efficiently. Since $u$ is a feasible solution we have $u \ge 0$ and Au $= b$, that is,
$$\sum_{k\in K}  u_{k}A^{k}= b.(**)$$
For every nonbasic $j \in / K$, a candidate for entering the basis $K$, we try to find a new vertex $u(\theta$ ) that improves the objective function, and for this we add $-\theta A^{j} + \theta A^{j} = 0$ to $b$ in

<!-- PAGE 1615 -->
Equation (**) and then replace the occurrence of $A^{j}$ in $-\theta A^{j}$ by the right hand side of Equation (*) to obtain
$$b = \sum_{k\in K}  u_{k}A^{k}-\theta A^{j}+ \theta A^{j}$$
$$= \sum_{k\in K}  u_{k}A^{k} -\theta \begin{pmatrix} \gamma_{k}^{j} A^{k} \end{pmatrix} \sum_{k\in K}  + \theta A^{j}$$
$$= \sum_{k\in K}  \begin{pmatrix} u_{k} -\theta \gamma_{k}^{j} \end{pmatrix} A^{k} + \theta A^{j}.$$
Consequently, the vector $u(\theta$ ) appearing on the right-hand side of the above equation given by
$$u_{i} -\theta \gamma_{i}^{j} if i \in K$$
$$$$
$$$$
$$u(\theta )_{i} =\theta if i = j$$
$$0if i \in /K \cup {j}$$
$$$$
automatically satisfies the constraints $Au(\theta$ ) $= b$, and this vector is a feasible solution iff
$$\theta  \ge 0andu_{k} \ge \theta \gamma_{k}^{j} for all k \in K.$$
Obviously $\theta  = 0$ is a solution, and if
$$



$$
$$\theta^{j} = \min \frac{u_{k}}{\gamma_{k}^{j}} \gamma_{k}^{j}  > 0, k \in K> 0,$$
then we have a range of feasible solutions for $0 \le \theta  \le \theta^{j}$ . The value of the objective function for $u(\theta$ ) is
$$cu(\theta ) = \sum_{k\in K}  c_{k}(u_{k} -\theta \gamma_{k}^{j} ) + \theta c_{j} = cu + \theta \begin{pmatrix} c_{j}- & \gamma_{k}^{j} c_{k} \end{pmatrix} \sum_{k\in K}  .$$
Since the potential change in the objective function is
$$\theta \begin{pmatrix} c_{j}- & \gamma_{k}^{j} c_{k} \end{pmatrix} \sum_{k\in K}$$
$$and \theta  \ge 0, if c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} \le 0, then the objective function can’t be increased.$$
$$However, if c_{j+} - \sum_{k}^{\in K}  \in K \gamma_{k}^{j+}  c_{k} > 0 for some j^{+}\in /K, and if \theta^{j+} > 0, then the objective$$
function can be strictly increased by choosing any $\theta  > 0$ such that $\theta  \le \theta^{j+}$ , so it is natural to zero at least one coefficient of $u(\theta$ ) by picking $\theta  = \theta^{j+}$ , which also maximizes the increase of the objective function. In this case (Case below (B2)), we obtain a new feasible solution $u^{+} = u(\theta^{j+}$ ). Now, if $\theta^{j+} > 0$, then there is some index $k \in K$ such $u_{k} > 0, \gamma_{k}^{j+} > 0$, and $\theta^{j+} = u_{k}/\gamma_{k}^{j+}$  , so we can pick such an index $k^{-}$ for the vector $A^{k-}$ leaving the basis $K$. We claim that

<!-- PAGE 1616 -->
$K^{+} = (K -{k^{-}}) \cup {j^{+}}$ is a basis. This is because the coefficient $\gamma_{k-}^{j+}$ associated with the column $A^{k-}$ is nonzero (in fact, $\gamma_{k-}^{j+} > 0)$, so Equation (*), namely
$$A^{j+} = \gamma_{k-}^{j+} A^{k-}+ \sum_{K-{k}  \gamma_{k}^{j+}  A^{k},$$
$$k\in -}$$
yields the equation
$$A^{k-}= (\gamma_{k-}^{j+} )^{-1}A^{j+}- \sum_{K-{k}  (\gamma_{k-}^{j+} )^{-1}\gamma_{k}^{j+}  A^{k},$$
$$k\in -}$$
and these equations imply that the subspaces spanned by the vectors $(A^{k})_{k\in K}$ and the vectors $(A^{k})_{k\in K+}$ are identical. However, $K$ is a basis of dimension $m$ so this subspace has dimension $m$, and since $K^{+}$ also has $m$ elements, it must be a basis. Therefore, $u^{+} = u(\theta^{j+}$ ) is a basic feasible solution. The above case is the most common one, but other situations may arise. In what follows, we discuss all eventualities. Case $(A)$.
$$We have c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} \le 0 for all j \in /K. Then it turns out that u is an optimal$$
solution. $Otherwise,^{\in K}$ we are in Case $(B)$. Case $(B)$.
$$We have c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} > 0 for some j \in /K (not necessarily unique). There are three$$
subcases. Case (B1). If for some $j \in / K$ as above we also have $\gamma_{k}^{j}  \le 0$ for all $k \in K$, since $u_{k} \ge 0$ for all $k \in K$, this places no restriction on $\theta$ , and the objective function is unbounded above. This is demonstrated by Example 46.3 with $K = {3, 4}$ and $j = 2$ since $\gamma_{{3,4}}^{2}  = (-1, 0)$. Case (B2). There is some index $j^{+} \in / K$ such that simultaneously
$$(1) c_{j+} - \sum_{k}  \gamma_{k}^{j+}  c_{k} > 0, which means that the objective function can potentially be$$
$increased;^{\in K}$
$(2)$ There is some $k \in K$ such that $\gamma_{k}^{j+} > 0$, and for every $k \in K$, if $\gamma_{k}^{j+} > 0$ then $u_{k} > 0$, which implies that $\theta^{j+} > 0$. If we pick $\theta  = \theta^{j+}$ where
$$



$$
$$\theta^{j+} = \min \frac{u_{k}}{\gamma_{k}^{j+}} \gamma_{k}^{j+} > 0, k \in K> 0,$$

<!-- PAGE 1617 -->
then the feasible solution $u^{+}$ given by
$$u_{i} -\theta^{j+} \gamma_{i}^{j+} if i \in K$$
$$$$
$$$$
$$u_{i}^{+} =\theta^{j+} if i = j^{+}$$
$$0if i \in /K \cup {j^{+}}$$
$$$$
is a vertex of $\mathcal{P}(A, b)$. If we pick any index $k^{-} \in K$ such that $\theta^{j+} = u_{k-}/\gamma_{k-}^{j+}$ , then $K^{+} = (K -{k^{-}})\cup {j^{+}}$ is a basis for $u^{+}$. The vector $A^{j+}$ enters the new basis $K^{+}$, and the vector $A^{k-}$ leaves the old basis $K$. This is a pivoting step. The objective function increases strictly. This is demonstrated by Example 46.2 with $K = {3, 4, 5}, j = 1$, and $k = 4$, Then $\gamma_{{3,4,5}}^{1}  = (-1, 1, 0)$, with $\gamma_{4}^{1}  = 1$. Since $u = (0, 0, 1, 3, 2), \theta^{1} =_{\gamma1}^{u4} = 3$, and the new optimal solutions becomes $u^{+} = (3, 0, 1$ - 3(-1), $3$ - 3(1), $2$ - 3(0)) $= (3^{4}, 0, 4, 0, 2)$. Case (B3).
$$There is some index j \in /K such that c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} > 0, and for each of the indices$$
$j \in / K$ satisfying the above property we have simultaneously
$$(1) c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} > 0, which means that the objective function can potentially be in-$$
$creased;^{\in K}$
$(2)$ There is some $k \in K$ such that $\gamma_{k}^{j}  > 0$, and $u_{k} = 0$, which implies that $\theta^{j} = 0$. Consequently, the objective function does not change. In this case, $u$ is a degenerate basic feasible solution. We can associate to $u^{+} = u$ a new basis $K^{+}$ as follows: Pick any index $j^{+} \in / K$ such that
$$c_{j+} - \sum_{k\in K}  \gamma_{k}^{j+}  c_{k} > 0,$$
and any index $k^{-} \in K$ such that
$$\gamma_{k-}^{j+} > 0,$$
and let $K^{+} = (K -{k^{-}}) \cup {j^{+}}$. As in Case (B2), The vector $A^{j+}$ enters the new basis $K^{+}$, and the vector $A^{k-}$ leaves the old basis $K$. This is a pivoting step. However, the objective function does not change since $\theta^{j+} = 0$. This is demonstrated by Example 46.1 with $K = {3, 4}, j = 2$, and $k = 3$. It is easy to prove that in Case $(A)$ the basic feasible solution $u$ is an optimal solution, and that in Case (B1) the linear program is unbounded. We already proved that in Case
(B2) the vector $u^{+}$ and its basis $K^{+}$ constitutes a basic feasible solution, and the proof in Case (B3) is similar. For details, see Ciarlet $[41]$ (Chapter $10)$.

<!-- PAGE 1618 -->
It is convenient to reinterpret the various cases considered by introducing the following sets:
$$no$$
$$B_{1} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  \le 0$$
$$


$$
$$no$$
$$B_{2} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  > 0, \min \frac{u_{k}}{\gamma_{k}^{j}} k \in K, \gamma_{k}^{j}  > 0> 0$$
$$


$$
$$no$$
$$B_{3} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  > 0, \min \frac{u_{k}}{\gamma_{k}^{j}} k \in K, \gamma_{k}^{j}  > 0= 0,$$
and
$$no$$
$$B = B_{1} \cup B_{2} \cup B_{3} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0.$$
Then it is easy to see that the following equivalences hold:
$$Case (A) \Leftarrow \Rightarrow B = \emptyset ,Case (B) \Leftarrow \Rightarrow B \neq  \emptyset$$
$$Case (B1) \Leftarrow \Rightarrow B_{1} \neq  \emptyset$$
$$Case (B2) \Leftarrow \Rightarrow B_{2} \neq  \emptyset$$
$$Case (B3) \Leftarrow \Rightarrow B_{3} \neq  \emptyset .$$
Furthermore, Cases $(A)$ and $(B)$, Cases (B1) and (B3), and Cases (B2) and (B3) are mutually exclusive, while Cases (B1) and (B2) are not. If Case (B1) and Case (B2) arise simultaneously, we opt for Case (B1) which says that the Linear Program $(P)$ is unbounded and terminate the algorithm. Here are a few remarks about the method. In Case (B2), which is the path followed by the algorithm most frequently, various choices have to be made for the index $j^{+} \in / K$ for which $\theta^{j+} > 0$ (the new index in $K^{+})$. Similarly, various choices have to be made for the index $k^{-} \in K$ leaving $K$, but such choices are typically less important. Similarly in Case (B3), various choices have to be made for the new index $j^{+} \in / K$ going into $K^{+}$. In Cases (B2) and (B3), criteria for making such choices are called pivot rules. Case (B3) only arises when $u$ is a degenerate vertex. But even if $u$ is degenerate, Case
(B2) may arise if $u_{k} > 0$ whenever $\gamma_{k}^{j}  > 0$. It may also happen that $u$ is nondegenerate but as a result of Case (B2), the new vertex $u^{+}$ is degenerate because at least two components $u_{k1}$ - $\theta^{j+} \gamma_{k1}^{j+}$  and $u_{k2}$ - $\theta^{j+} \gamma_{k2}^{j+}$  vanish for some distinct $k_{1}, k_{2} \in K$. Cases $(A)$ and (B1) correspond to situations where the algorithm terminates, and Case
(B2) can only arise a finite number of times during execution of the simplex algorithm, since the objective function is strictly increased from vertex to vertex and there are only finitely many vertices. Therefore, if the simplex algorithm is started on any initial basic feasible solution $u_{0}$, then one of three mutually exclusive situations may arise:

<!-- PAGE 1619 -->
$(1)$ There is a finite sequence of occurrences of Case (B2) $and/or$ Case (B3) ending with an occurrence of Case $(A)$. Then the last vertex produced by the algorithm is an optimal solution. This is what occurred in Examples 46.1 and 46.2.
$(2)$ There is a finite sequence of occurrences of Case (B2) $and/or$ Case (B3) ending with an occurrence of Case (B1). We conclude that the problem is unbounded, and thus has no solution. This is what occurred in Example 46.3.
$(3)$ There is a finite sequence of occurrences of Case (B2) $and/or$ Case (B3), followed by an infinite sequence of Case (B3). If this occurs, the algorithm visits the some basis twice. This a phenomenon known as cycling. In this eventually the algorithm fails to come to a conclusion. There are examples for which cycling occur, although this is rare in practice. Such an example is given in Chvatal $[40]$; see Chapter $3$, pages 31-32, for an example with seven variables and three equations that cycles after six iterations under a certain pivot rule. The third possibility can be avoided by the choice of a suitable pivot rule. Two of these rules are Bland’s rule and the lexicographic rule; see Chvatal $[40]$ (Chapter $3$, pages 34-38). Bland’s rule says: choose the smallest of the eligible incoming indices $j^{+} \in / K$, and similarly choose the smallest of the eligible outgoing indices $k^{-} \in K$. It can be proven that cycling cannot occur if Bland’s rule is chosen as the pivot rule. The proof is very technical; see Chvatal $[40]$ (Chapter $3$, pages 37-38), Matousek and Gardner $[127]$ (Chapter $5$, Theorem 5.8.1), and Papadimitriou and Steiglitz $[139]$ (Section 2.7). Therefore, assuming that some initial basic feasible solution is provided, and using a suitable pivot rule (such as Bland’s rule), the simplex algorithm always terminates and either yields an optimal solution or reports that the linear program is unbounded. Unfortunately, Bland’s rules is one of the slowest pivot rules. The choice of a pivot rule affects greatly the number of pivoting steps that the simplex algorithms goes through. It is not our intention here to explain the various pivot rules. We simply mention the following rules, referring the reader to Matousek and Gardner $[127]$ (Chapter $5$, Section 5.7) or to the texts cited in Section 44.1. $1$. Largest coefficient, or Dantzig’s rule. $2$. Largest increase. $3$. Steepest edge. $4$. Bland’s Rule. $5$. Random edge.

<!-- PAGE 1620 -->
The steepest edge rule is one of the most popular. The idea is to maximize the ratio
$$\frac{c(u^{+}u)}{\|u^{+}-u\|} -.$$
The random edge rule picks the index $j^{+} \in / K$ of the entering basis vector uniformly at random among all eligible indices. Let us now return to the issue of the initialization of the simplex algorithm. We use the Linear Program $(P)$ introduced during the proof of Theorem 45.7.
$$b$$
Consider a Linear Program (P2)
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
in standard form where $A$ is an $m \times  n$ matrix of rank $m$. First, observe that since the constraints are equations, we can ensure that $b \ge 0$, because every equation $a_{i}x = b_{i}$ where $b_{i} < 0$ can be replaced by $-a_{i}x = -b_{i}$. The next step is to introduce the Linear Program $(P)$ in standard form
$$b$$
$$maximize-(x_{n+1} + \cdots  + x_{n+m})$$
$$subject toAx = b andx \ge 0,$$
$$b b b$$
where $A$ and $x$ are given by $b  b$
$$Ab = \begin{pmatrix} A & I_{m} \end{pmatrix} ,xb = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n+m} \end{pmatrix} .$$
Since we assumed that $b \ge 0$, the vector $x = (0_{n}, b)$ is a feasible solution of $(P)$, in fact a basic
$$b b$$
feasible solutions since the matrix associated with the indices $n+1, \dots  , n+m$ is the identity matrix $I_{m}$. Furthermore, since $x_{i} \ge 0$ for all $i$, the objective function $-(x_{n+1} + \cdots  + x_{n+m})$ is bounded above by $0$. If we execute the simplex algorithm with a pivot rule that prevents cycling, starting with the basic feasible solution $(0_{n}, d)$, since the objective function is bounded by $0$, the simplex algorithm terminates with an optimal solution given by some basic feasible solution, say
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
$(u^{*}, w^{*})$, with $u^{*} \in$ and $w^{*} \in$ . As in the proof of Theorem 45.7, for every feasible solution $u \in$ P(A, $b)$, the vector $(u, 0_{m})$
$$̸$$
is an optimal solution of $(P)$. Therefore, if $w^{*} = 0$, then $\mathcal{P}(A, b) = \emptyset$ , since otherwise for
$$b$$
every feasible solution $u \in$ P(A, $b)$ the vector $(u, 0_{m})$ would yield a value of the objective function $-(x_{n+1} + \cdots  + x_{n+m})$ equal to $0$, but $(u^{*}, w^{*})$ yields a strictly negative value since $w^{*} \neq  0$.
