# Convergence of ADMM


<!-- PAGE 1917 -->
then we have
$$\lambda^{\top} r + (\rho /2) \|r\|_{2}^{2} = (\rho /2) \|r + (1/\rho )\lambda \|_{2}^{2} -(1/(2\rho )) \|\lambda \|_{2}^{2}$$
$$= (\rho /2) \|r + \mu \|_{2}^{2} -(\rho /2) \|\mu \|_{2}^{2} .$$
The scaled form of ADMM consists of the following steps:
$$x^{k+1}= arg minx \begin{pmatrix} f(x) + (\rho /2) & Ax + Bz^{k} -c + \mu_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= arg minz \begin{pmatrix} g(z) + (\rho /2) & Ax^{k+1} + Bz -c + \mu_{2}^{k2} \end{pmatrix}$$
$$\mu^{k+1} = \mu^{k} + Ax^{k+1}+ Bz^{k+1}-c.$$
If we define the residual $r^{k}$ at step $k$ as
$$r^{k}= Ax^{k}+ Bz^{k}-c = \mu^{k} -\mu^{k-1} = (1/\rho )(\lambda^{k} -\lambda^{k-1} ),$$
then we see that
$$r = u^{0} + \sum_{j=1}^{k}  r^{j}.$$
The formulae in the scaled form are often shorter than the formulae in the unscaled form. We now discuss the convergence of ADMM.
$$⊛$$

## 52.4 Convergence of ADMM

Let us repeat the steps of ADMM: Given some initial $(z^{0}, \lambda^{0}$ ), do:
$$x^{k+1}= arg minL_{\rho}(x, z^{k}, \lambda^{k} )(x-update)$$
$$x$$
$$z^{k+1}= arg minL_{\rho}(x^{k+1}, z, \lambda^{k} )(z-update)$$
$$z$$
$$\lambda^{k+1} = \lambda^{k} + \rho (Ax^{k+1}+ Bz^{k+1}-c).(\lambda -update)$$
The convergence of ADMM can be proven under the following three assumptions:
$(1)$ The functions $f$ : $\mathbb{R} \to \mathbb{R}\cup {+\infty$ } and $g: \mathbb{R} \to \mathbb{R}\cup {+\infty$ } are proper and closed convex functions (see Section 51.1) such that relint(dom(f)) $\cap$ relint(dom(g)) $\neq  \emptyset$ .
$(2)$ The $n \times  n$ matrix $A^{\top}A$ is invertible and the $m \times  m$ matrix $B^{\top}B$ is invertible. Equivalently, the $p \times  n$ matrix $A$ has rank $n$ and the $p \times  m$ matrix has rank $m$.
$(3)$ The unaugmented Lagrangian $L_{0}(x, z, \lambda$ ) $= f(x)+g(z)+\lambda^{\top} (Ax+Bz -c)$ has a saddle point, which means there exists $x^{*}, z^{*}, \lambda^{*}$ (not necessarily unique) such that
$$L_{0}(x^{*}, z^{*}, \lambda ) \le L_{0}(x^{*}, z^{*}, \lambda^{*} ) \le L_{0}(x, z, \lambda^{*} )$$
for all $x, z, \lambda$ .

<!-- PAGE 1918 -->
Recall that the augmented Lagrangian is given by
$$L_{\rho}(x, z, \lambda ) = f(x) + g(z) + \lambda^{\top} (Ax + Bz -c) + (\rho /2) \|Ax + Bz -c\|_{2}^{2} .$$
For $z$ (and $\lambda$ ) fixed, we have $L_{\rho}(x, z, \lambda$ ) $=$ f(x) $+$ g(z) $+ \lambda^{\top}$ (Ax $+$ Bz - $c) + (\rho /2)(Ax +$ Bz - $c)^{\top}(Ax +$ Bz - $c)$
$$= f(x) + (\rho /2)x^{\top}A^{\top}Ax + (\lambda^{\top} + \rho (Bz -c)^{\top})Ax$$
$$+ g(z) + \lambda^{\top} (Bz -c) + (\rho /2)(Bz -c)^{\top}(Bz -c).$$
Assume that $(1)$ and $(2)$ hold. Since $A^{\top}A$ is invertible, then it is symmetric positive definite, and by Proposition 51.37 the x-minimization step has a unique solution (the minimization problem succeeds with a unique minimizer). Similarly, for $x$ (and $\lambda$ ) fixed, we have $L_{\rho}(x, z, \lambda$ ) $=$ f(x) $+$ g(z) $+ \lambda^{\top}$ (Ax $+$ Bz - $c) + (\rho /2)(Ax +$ Bz - $c)^{\top}(Ax +$ Bz - $c)$
$$= g(z) + (\rho /2)z^{\top}B^{\top}Bz + (\lambda^{\top} + \rho (Ax -c)^{\top})Bz$$
$$+ f(x) + \lambda^{\top} (Ax -c) + (\rho /2)(Ax -c)^{\top}(Ax -c).$$
Since $B^{\top}B$ is invertible, then it is symmetric positive definite, and by Proposition 51.37 the z-minimization step has a unique solution (the minimization problem succeeds with a unique minimizer). By Theorem 51.41, Assumption $(3)$ is equivalent to the fact that the KKT equations are satisfied by some triple $(x^{*}, z^{*}, \lambda^{*}$ ), namely
$$Ax^{*}+ Bz^{*}-c = 0(*)$$
and
$$0 \in \partial f(x^{*}) + \partial g(z^{*}) + A^{\top}\lambda^{*} + B^{\top}\lambda^{*} ,(\dagger )$$
Assumption $(3)$ is also equivalent to Conditions (a) and $(b)$ of Theorem 51.41. In particular, our program has an optimal solution $(x^{*}, z^{*})$. By Theorem 51.43, $\lambda^{*}$ is maximizer of the dual function $G(\lambda$ ) $= inf_{x,z} L_{0}(x, z, \lambda$ ) and strong duality holds, that is, $G(\lambda^{*}$ ) $= f(x^{*}) + g(z^{*})$ (the duality gap is zero). We will see after the proof of Theorem 52.1 that Assumption $(2)$ is actually implied by Assumption $(3)$. This allows us to prove a convergence result stronger than the convergence result proven in Boyd et al. $[28]$ under the exact same assumptions $(1)$ and $(3)$.
$$\mathbb{R}^{m+p}$$
Let $p^{*}$ be the minimum value of $f+g$ over the convex set ${(x, z) \in$ | $Ax+Bz-c = 0}$, and let $(p^{k})$ be the sequence given by $p^{k} = f(x^{k})+g(z^{k})$, and recall that $r^{k} = Ax^{k}+Bz^{k}-c$. Our main goal is to prove the following result.

> **Theorem 52.1.** Suppose the following assumptions hold:

<!-- PAGE 1919 -->
$(1)$ The functions $f$ : $\mathbb{R} \to \mathbb{R}\cup {+\infty$ } and $g: \mathbb{R} \to \mathbb{R}\cup {+\infty$ } are proper and closed convex functions (see Section 51.1) such that relint(dom(f)) $\cap$ relint(dom(g)) $\neq  \emptyset$ .
$(2)$ The $n \times  n$ matrix $A^{\top}A$ is invertible and the $m \times  m$ matrix $B^{\top}B$ is invertible. Equivalently, the $p \times  n$ matrix $A$ has rank $n$ and the $p \times  m$ matrix has rank $m$. (This assumption is actually redundant, because it is implied by Assumption $(3))$.
$(3)$ The unaugmented Lagrangian $L_{0}(x, z, \lambda$ ) $= f(x)+g(z)+\lambda^{\top} (Ax+Bz -c)$ has a saddle point, which means there exists $x^{*}, z^{*}, \lambda^{*}$ (not necessarily unique) such that
$$L_{0}(x^{*}, z^{*}, \lambda ) \le L_{0}(x^{*}, z^{*}, \lambda^{*} ) \le L_{0}(x, z, \lambda^{*} )$$
for all $x, z, \lambda$ . Then for any initial values $(z^{0}, \lambda^{0}$ ), the following properties hold:
$(1)$ The sequence $(r^{k})$ converges to $0$ (residual convergence).
$(2)$ The sequence $(p^{k})$ converge to $p^{*}$ (objective convergence).
$(3)$ The sequences $(x^{k})$ and $(z^{k})$ converge to an optimal solution (x,z) of Problem $(P_{admm})$
$$e e$$
and the sequence $(\lambda^{k}$ ) converges an optimal solution $\lambda$  of the dual problem (primal and
$$e$$
dual variable convergence).

*Proof.* The core of the proof is due to Boyd et al. $[28]$, but there are new steps because we have the stronger hypothesis $(2)$, which yield the stronger result $(3)$. The proof consists of several steps. It is not possible to prove directly that the sequences $(x^{k}), (z^{k})$, and $(\lambda^{k}$ ) converge, so first we prove that the sequence $(r^{k+1})$ converges to zero, and that the sequences $(Ax^{k+1})$ and $(Bz^{k+1})$ also converge. Step $1$. Prove the inequality (A1) below. Consider the sequence of reals $(V^{k}$ ) given by
$$-



-$$
$$V^{k}= (1/\rho )\lambda^{k} \lambda_{2}^{*2}  + \rho B(z^{k}z^{*})_{2}^{2} .$$
It can be shown that the $V^{k}$ satisfy the following inequality:
$$-$$
$$V^{k+1}\le V^{k}-\rho r_{2}^{k+12} -\rho B(z^{k+1}z^{k})_{2}^{2} .(A1)$$
This is rather arduous. Since a complete proof is given in Boyd et al. $[28]$, we will only provide some of the key steps later. Inequality (A1) shows that the sequence $(V^{k}$ ) in nonincreasing. If we write these inequalities for $k, k$ - $1, \dots  , 0$, we have
$$-$$
$$V^{k+1}\le V^{k}-\rho r_{2}^{k+12} -\rho B(z^{k+1}z^{k})_{2}^{2}$$
$$-$$
$$V^{k}\le V^{k-1}-\rho r_{2}^{k2} -\rho B(z^{k}z^{k-1})_{2}^{2}$$
$$\vdots$$
$$-$$
$$V^{1}\le V^{0}-\rho r_{2}^{12} -\rho B(z^{1}z^{0})_{2}^{2} ,$$

<!-- PAGE 1920 -->
and by adding up these inequalities, we obtain
$$





-

$$
$$V^{k+1}\le V^{0}-\rho \sum_{j=0}^{k}  r_{2}^{j+12} +B(z^{j+1}z^{j})_{2}^{2},$$
which implies that
$$





-

$$
$$\rho \sum_{j=0}^{k}  r_{2}^{j+12} +B(z^{j+1}z^{j})_{2}^{2}\le V_{0} -V^{k+1}\le V^{0},(B)$$
since $V^{k+1} \le V^{0}$. Step $2$. Prove that the sequence $(r^{k})$ converges to $0$, and that the sequences $(Ax^{k+1})$ and $(Bz^{k+1})$ also converge.
$$\infty  \infty$$
$$Inequality (B) implies that the series \sum_{k}  r^{k}and \sum  k=0 B(z^{k+1}-z^{k}) converge absolutely.$$
In particular, the sequence $(r^{k}) converges^{=1}$ to $0$.
$$\infty  -$$
$$The nth partial sum of the series \sum_{k}  =0 B(z^{k+1}z^{k}) is$$
$$\sum_{k=0}^{n}  B(z^{k+1}-z^{k}) = B(z^{n+1}-z^{0}),$$
$$\infty$$
$$and since the series \sum_{k+1k}  =0 B(z^{k+1} -z^{k}) converges, we deduce that the sequence (Bz^{k+1})$$
converges. Since Ax $+ Bz^{k+1}$ - $c = r^{k+1}$, the convergence of $(r^{k+1})$ and $(Bz^{k+1})$ implies that the sequence $(Ax^{k+1})$ also converges. Step $3$. Prove that the sequences $(x^{k+1})$ and $(z^{k+1})$ converge. By Assumption $(2)$, the matrices $A^{\top}A$ and $B^{\top}B$ are invertible, so multiplying each vector $Ax^{k+1}$ by $(A^{\top}A)^{-1}A^{\top}$, if the sequence $(Ax^{k+1})$ converges to $u$, then the sequence $(x^{k+1})$ converges to $(A^{\top}A)^{-1}A^{\top}u$. Siimilarly, if the sequence $(Bz^{k+1})$ converges to $v$, then the sequence $(z^{k+1})$ converges to $(B^{\top}B)^{-1}B^{\top}v$. Step $4$. Prove that the sequence $(\lambda^{k}$ ) converges. Recall that
$$\lambda^{k+1} = \lambda^{k} + \rho r^{k+1}.$$
It follows by induction that
$$\lambda^{k+p} = \lambda^{k} + \rho (r^{k+1}+ \cdots  + \rho^{k+p} ),p \ge 2.$$
As a consequence, we get
$$-

$\le$



$+$$$
$$\lambda^{k+p} \lambda^{k} \rho (r^{k+1} \cdots  +r^{k+p}).$$

<!-- PAGE 1921 -->
$$Since the series \sum_{k}  \infty

$r^{k}$

converges, the partial sums form a Cauchy sequence, and this$$ immediately $implies^{=1}$ that for any $\epsilon  > 0$ we can find $N > 0$ such that
$$\rho (

$r^{k+1}$

$+ \cdots  +$

$r^{k+p}$

) $< \epsilon$ ,for all $k, p + k \ge$ N,$$ so the sequence $(\lambda^{k}$ ) is also a Cauchy sequence, thus it converges. Step $5$. Prove that the sequence $(p^{k})$ converges to $p^{*}$. For this, we need two more inequalities. Following Boyd et al. $[28]$, we need to prove that
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}-\rho (B(z^{k+1}-z^{k}))^{\top}(-r^{k+1}+ B(z^{k+1}-z^{*}))(A2)$$
and
$$p^{*}-p^{k+1}\le (\lambda^{*} )^{\top}r^{k+1}.(A3)$$
Since we proved that the sequence $(r^{k})$ and $B(z^{k+1}$ - $z^{k})$ converge to $0$, and that the sequence $(\lambda^{k+1}$ ) converges, from $(\lambda^{k+1} )^{\top}r^{k+1} + \rho (B(z^{k+1}$ - $z^{k}))^{\top}(-r^{k+1} + B(z^{k+1}$ - $z^{*})) \le p^{*}$ - $p^{k+1} \le (\lambda^{*} )^{\top}r^{k+1}$, we deduce that in the limit, $p^{k+1}$ converges to $p^{*}$. Step $6$. Prove (A3). Since $(x^{*}, y^{*}, \lambda^{*}$ ) is a saddle point, we have
$$L_{0}(x^{*}, z^{*}, \lambda^{*} ) \le L_{0}(x^{k+1}, z^{k+1}, \lambda^{*} ).$$
Since $Ax^{*} + Bz^{*} = c$, we have $L_{0}(x^{*}, z^{*}, \lambda^{*}$ ) $= p^{*}$, and since $p^{k+1} = f(x^{k+1}) + g(z^{k+1})$, we have
$$L_{0}(x^{k+1}, z^{k+1}, \lambda^{*} ) = p^{k+1}+ (\lambda^{*} )^{\top}r^{k+1},$$
so we obtain
$$p^{*}\le p^{k+1}+ (\lambda^{*} )^{\top}r^{k+1},$$
which yields (A3). Step $7$. Prove (A2). By Proposition 51.34, $z^{k+1}$ minimizes $L_{\rho}(x^{k+1}, z, \lambda^{k}$ ) iff
$$0 \in \partial g(z^{k+1}) + B^{\top}\lambda^{k} + \rho B^{\top}(Ax^{k+1}+ Bz^{k+1}-c)$$
$$= \partial g(z^{k+1}) + B^{\top}\lambda^{k} + \rho B^{\top}r^{k+1}$$
$$= \partial g(z^{k+1}) + B^{\top}\lambda^{k+1} ,$$
since $r^{k+1} = Ax^{k+1} + Bz^{k+1}$ - $c$ and $\lambda^{k+1} = \lambda^{k} + \rho (Ax^{k+1} + Bz^{k+1}$ - $c)$. In summary, we have
$$0 \in \partial g(z^{k+1}) + B^{\top}\lambda^{k+1} ,(\dagger_{1} )$$

<!-- PAGE 1922 -->
which shows that $z^{k+1}$ minimizes the function
$$z \mapsto g(z) + (\lambda^{k+1} )^{\top}Bz.$$
Consequently, we have
$$g(z^{k+1}) + (\lambda^{k+1} )^{\top}Bz^{k+1}\le g(z^{*}) + (\lambda^{k+1} )^{\top}Bz^{*}.(B1)$$
Similarly, $x^{k+1}$ minimizes $L_{\rho}(x, z^{k}, \lambda^{k}$ ) iff
$$0 \in \partial f(x^{k+1}) + A^{\top}\lambda^{k} + \rho A^{\top}(Ax^{k+1}+ Bz^{k}-c)$$
$$= \partial f(x^{k+1}) + A^{\top}(\lambda^{k} + \rho r^{k+1}+ \rho B(z^{k}-z^{k+1}))$$
$$= \partial f(x^{k+1}) + A^{\top}\lambda^{k+1} + \rho A^{\top}B(z^{k}-z^{k+1})$$
since $r^{k+1}$ - $Bz^{k+1} = Ax^{k+1}$ - $c$ and $\lambda^{k+1} = \lambda^{k} + \rho (Ax^{k+1} + Bz^{k+1}$ - $c) = \lambda^{k} + \rho r^{k+1}$. Equivalently, the above derivation shows that
$$0 \in \partial f(x^{k+1}) + A^{\top}(\lambda^{k+1} -\rho B(z^{k+1}-z^{k})),(\dagger_{2} )$$
which shows that $x^{k+1}$ minimizes the function
$$x \mapsto f(x) + (\lambda^{k+1} -\rho B(z^{k+1}-z^{k}))^{\top}Ax.$$
Consequently, we have $f(x^{k+1}) + (\lambda^{k+1}$ - $\rho B(z^{k+1}$ - $z^{k}))^{\top}Ax^{k+1} \le f(x^{*}) + (\lambda^{k+1}$ - $\rho B(z^{k+1}$ - $z^{k}))^{\top}Ax^{*}$. (B2) Adding up Inequalities (B1) and (B2), using the equation $Ax^{*} + Bz^{*} = c$, and rearranging, we obtain inequality (A2). Step $8$. Prove that $(x^{k}), (z^{k})$, and $(\lambda^{k}$ ) converge to optimal solutions. Recall that $(r^{k})$ converges to $0$, and that $(x^{k}), (z^{k})$, and $(\lambda^{k}$ ) converge to limits $x, z$, and
$$+ - e e$$
$\lambda$ . Since $r^{k} = Ax^{k}  Bz^{k} c$, in the limit, we have $e$
$$Ax + Bz -c = 0.(*_{1})$$
$$ee$$
Using $(\dagger_{1}$ ), in the limit, we obtain
$$0 \in \partial g(z) + B^{\top}\lambda .(*_{2})$$
$$ee$$
Since $(B(z^{k+1}$ - $z^{k}))$ converges to $0$, using $(\dagger_{2}$ ), in the limit, we obtain
$$0 \in \partial f(x) + A^{\top}\lambda .(*_{3})$$
$$ee$$
From $(*_{2})$ and $(*_{3})$, we obtain
$$0 \in \partial f(x) + \partial g(z) + A^{\top}\lambda  + B^{\top}\lambda .(*_{4})$$
$$eeee$$

<!-- PAGE 1923 -->
But $(*_{1})$ and $(*_{4})$ are exactly the KKT equations, and by Theorem 51.41, we conclude that $x,z,\lambda$  are optimal solutions. $e  e  e$ Step $9$. Prove (A1). This is the most tedious step of the proof. We begin by adding up
(A2) and (A3), and then perform quite a bit or rewriting and manipulation. The complete derivation can be found in Boyd et al. $[28]$.
Remarks:
$(1)$ In view of Theorem 51.42, we could replace Assumption $(3)$ by the slightly stronger assumptions that the optimum value of our program is finite and that the constraints are qualified. Since the constraints are affine, this means that there is some feasible solution in relint(dom(f)) $\cap$ relint(dom(g)). These assumptions are more practical than Assumption $(3)$.
$(2)$ Actually, Assumption $(3)$ implies Assumption $(2)$. Indeed, we know from Theorem 51.41 that the existence of a saddle point implies that our program has a finite optimal solution. However, if either $A^{\top}A$ or $B^{\top}B$ is not invertible, then Program $(P)$ may not have a finite optimal solution, as shown by the following counterexample.

> **Example 52.5.** Let
$$f(x, y) = x,g(z) = 0,y -z = 0.$$
Then
$$L_{\rho}(x, y, z, \lambda ) = x + \lambda (y -z) + (\rho /2)(y -z)^{2},$$
but minimizing over $(x, y)$ with $z$ held constant yields $-\infty$ , which implies that the above program has no finite optimal solution. See Figure 52.4. The problem is that
$$A = \begin{pmatrix} 0 & 1 \end{pmatrix} ,B = \begin{pmatrix} -1 \end{pmatrix} ,$$
but
$$A^{\top}A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$
is not invertible.
$(3)$ Proving (A1), (A2), (A3), and the convergence of $(r^{k})$ to $0$ and of $(p^{k})$ to $p^{*}$ does not require Assumption $(2)$. The proof, using the ingeneous Inequality (A1) (and $(B))$ is the proof given in Boyd et al. $[28]$. We were also able to prove that $(\lambda^{k}$ ), $(Ax^{k})$ and $(Bz^{k})$ converge without Assumption $(2)$, but to prove that $(x^{k}), (y^{k})$, and $(\lambda^{k}$ ) converge to optimal solutions, we had to use Assumption $(2)$.

<!-- PAGE 1924 -->
$$graph of f(x,y) = x$$
$$f(x,y) = x intersected with y=z,$$
$$z fixed.$$

![Figure 52.4](../../assets/ch52/fig_52_4.png)

**Figure 52.4:** A graphical representation of the Example 52.5. This is an illustration of the $x$ minimization step when $z$ is held fixed. Since the intersection of the two planes is an unbounded line, we “see” that minimizing over $x$ yields $-\infty$ .
$(4)$ Bertsekas discusses ADMM in $[17]$, Sections 2.2 and 5.4. His formulation of ADMM is slightly different, namely
$$minimizef(x) + g(z)$$
$$subject to Ax = z.$$
Bertsekas states a convergence result for this version of ADMM under the hypotheses that either dom(f) is compact or that $A^{\top}A$ is invertible, and that a saddle point exists; see Proposition 5.4.1. The proof is given in Bertsekas $[20]$, Section 3.4, Proposition 4.2. It appears that the proof makes use of gradients, so it is not clear that it applies in the more general case where $f$ and $g$ are not differentiable.
$(5)$ Versions of ADMM are discussed in Gabay $[70]$ (Sections $4$ and $5)$. They are more general than the version discussed here. Some convergence proofs are given, but because Gabay’s framework is more general, it is not clear that they apply to our setting. Also, these proofs rely on earlier result by Lions and Mercier, which makes the comparison difficult.

<!-- PAGE 1925 -->
$(5)$ Assumption $(2)$ does not imply that the system Ax $+$ Bz $= c$ has any solution. For example, if
$$A = \begin{pmatrix} 1 \\ 1 \end{pmatrix} ,B = \begin{pmatrix} -1 \\ -1 \end{pmatrix} ,c = \begin{pmatrix} 1 \\ 0 \end{pmatrix} ,$$
the system
$$x -z = 1$$
$$x -z = 0$$
has no solution. However, since Assumption $(3)$ implies that the program has an optimal solution, it implies that $c$ belongs to the column space of the $p \times  (n + m)$
$$matrix \begin{pmatrix} A & B \\ example \end{pmatrix} .$$
Here is an  where ADMM diverges for a problem whose optimum value is $-\infty$ .

> **Example 52.6.** Consider the problem given by
$$f(x) = x,g(z) = 0,x -z = 0.$$
Since f(x) $+$ g(z) $= x$, and $x = z$, the variable $x$ is unconstrained and the above function goes to $-\infty$ when $x$ goes to $-\infty$ . The augmented Lagrangian is
$$L_{\rho}(x, z, \lambda ) = x + \lambda (x -z) + \frac{\rho}{2} (x -z)^{2}$$
$$-  +$$
$$= \frac{\rho}{2} x^{2}\rho xz + \frac{\rho}{2} z^{2} x + \lambda x -\lambda z.$$
The matrix
$$\begin{pmatrix} 1 & -_{2}^{1} \\ -_{2}^{1}\overline{2} & 1 \\ \overline{2} \end{pmatrix}$$
is singular and $L_{\rho}(x, z, \lambda$ ) goes to $-\infty$ in when $(x, z) =$ t(1, $1)$ and $t$ goes to $-\infty$ . The ADMM steps are:
$$-$$
$$x^{k+1}= z^{k}- \frac{1}{\rho} \lambda^{k} \frac{1}{\rho}$$
$$z^{k+1}= x^{k+1}+ \frac{1}{\rho} \lambda^{k}$$
$$\lambda^{k+1} = \lambda^{k} + \rho (x^{k+1}-z^{k+1}),$$
and these equations hold for all $k \ge 0$. From the last two equations we deduce that
$$\lambda^{k+1} = \lambda^{k} + \rho (x^{k+1}-z^{k+1}) = \lambda^{k} + \rho (- \frac{1}{\rho} \lambda^{k} ) = 0,for all k \ge 0,$$
so
$$z^{k+2}= x^{k+2}+ \frac{1}{\rho} \lambda^{k+1} = x^{k+2},for all k \ge 0.$$
