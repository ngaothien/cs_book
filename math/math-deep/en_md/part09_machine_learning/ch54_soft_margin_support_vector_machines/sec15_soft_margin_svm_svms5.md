# Soft Margin SVM; (SVMs5)


<!-- PAGE 2047 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.22: Running (SVM_{s4}) on two sets of 30 points; K = 190.$$
Our second run was made with $K = 1/12000$; see Figure 54.23. We have $p_{m} = 30$ and $q_{m} = 30$ and we see that the width of the slab is a bit excessive. This example demonstrates that the margin lines need not contain data points.

## 54.15 Soft Margin SVM; (SVM )

$$s5$$
In this section we consider the version of Problem $(SVM_{s4})$ in which we add the term $(1/2)b^{2}$ to the objective function. We also drop the constraint $\eta  \ge 0$ which is redundant. Soft margin SVM $(SVM_{s5})$:
$$+ ($$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + & (\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) \\ p + q \end{pmatrix}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q,$$
where $\nu$  and $K_{s}$ are two given positive constants. As we saw earlier, it is convenient to pick $K_{s} = 1/(p + q)$. When writing a computer program, it is preferable to assume that $K_{s}$ is arbitrary. In this case $\nu$  must be replaced by $(p + q)K_{s}\nu$  in all the formulae. One of the advantages of this methods is that $\epsilon$  is determined by $\lambda , \xi$  is determined by $\mu$  (as in $(SVM_{s4}))$, and both $\eta$  and $b$ determined by $\lambda$  and $\mu$ . As the previous method, this

<!-- PAGE 2048 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.23: Running (SVM_{s4}) on two sets of 30 points; K = 1/12000.$$
method does not require support vectors to compute $b$. We can omit the constraint $\eta  \ge 0$, because for an optimal solution it can be shown using duality that $\eta  \ge 0$. A drawback of Program $(SVM_{s5})$ is that for fixed $K_{s}$, the quantity $\delta  = \eta / \|w\|$ and the hyperplanes $H_{w,b}, H_{w,b+\eta}$ and $H_{w,b-\eta}$ are independent of $\nu$ . This will be shown in Theorem 54.9. Thus this method is less flexible than $(SVM_{s2'})$ and $(SVM_{s3})$. The Lagrangian is given by
$$-$$
$$L(w, \epsilon , \xi , b, \eta , \lambda , \mu ) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$\epsilon^{\top} \lambda  -\xi^{\top} \mu  + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu )$$
$$= \frac{-1}{2} w^{\top}w + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  -\nu )$$
$$+ K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) -\epsilon^{\top} \lambda  -\xi^{\top} \mu  + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \frac{1}{2} b^{2}.$$
To find the dual function $G(\lambda , \mu$ ) we minimize L(w, $\epsilon , \xi , b, \eta , \lambda , \mu$ ) with respect to $w, \epsilon , \xi , b$, and $\eta$ . Since the Lagrangian is convex and $(w, \epsilon , \xi , b, \eta$ ) $\in \mathbb{R}^{n}\times \mathbb{R}^{p}\times \mathbb{R}^{q}\times \mathbb{R}\times \mathbb{R}$, a convex open set, by Theorem 40.13, the Lagrangian has a minimum in $(w, \epsilon , \xi , b, \eta$ ) iff $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$, so

<!-- PAGE 2049 -->
we compute $\nabla L_{w,\epsilon ,\xi ,b,\eta}$. The gradient $\nabla L_{w,\epsilon ,\xi ,b,\eta}$ is given by
$$\begin{pmatrix}\end{pmatrix}$$
$$\nabla L_{w,\epsilon ,\xi ,b,\eta} = \begin{pmatrix} \lambda  \\ w + X & \mu \\ 2K_{s}\epsilon  -\lambda \\ 2K_{s}\xi  -\mu \\ b + 1_{p}^{\top}\lambda  -1_{q}^{\top}\mu \\ 1_{p}^{\top}\lambda  + 1_{q}^{\top}\mu & \nu \end{pmatrix} .$$
$$-$$
By setting $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$ we get the equations
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,(*_{w})$$
$$2K_{s}\epsilon  = \lambda$$
$$2K_{s}\xi  = \mu$$
$$b = -(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu )$$
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = \nu .$$
As we said earlier, both $w$ an $b$ are determined by $\lambda$  and $\mu$ . We can use the equations to obtain the following expression for the dual function $G(\lambda , \mu , \gamma$ ),
$$G(\lambda , \mu , \gamma ) = - \frac{1}{4K_{s}} (\lambda^{\top} \lambda  + \mu^{\top} \mu ) - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \frac{b^{2}}{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\ isequivalenttotheminimization \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Consequently the dual program      program Dual of the Soft margin SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q.$$
It is shown in Section 54.16 how the dual program is solved using ADMM from Section 52.6. If the primal problem is solvable, this yields solutions for $\lambda$  and $\mu$ . The constraint
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$

<!-- PAGE 2050 -->
implies that either there is some $i_{0}$ such that $\lambda_{i0}  > 0$ or there is some $j_{0}$ such that $\mu_{j0}  > 0$, so we have $\epsilon_{i0}  > 0$ or $\xi_{j0}  > 0$, which means that at least one point is misclassified. Thus Problem $(SVM_{s5})$ should only be used when the sets ${u_{i}}$ and ${v_{j}}$ are not linearly separable. We can use the fact that the duality gap is $0$ to find $\eta$ . We have
$$\frac{1}{2} w^{\top}w + \frac{b^{2}}{2} -\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi )$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
so we get
$$\nu \eta  = K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\  \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 4K_{s} \\  \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$= \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
The above confirms that at optimality we have $\eta  \ge 0$.
Remark: If we do not assume that $K_{s} = 1/(p+q)$, then the above formula must be replaced by
$$(p + q)K_{s}\nu \eta  = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\ 54.8statingthatforafixed \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
There is a version of Theorem       $K_{s}$, the solution to Problem $(SVM_{s5})$ is unique and independent of the value of $\nu$ .

> **Theorem 54.9.** For $K_{s}$ and $\nu$  fixed, if Problem $(SVM_{s5})$ succeeds then it has a unique solution. If Problem $(SVM_{s5})$ succeeds and returns $(\lambda , \mu , \eta , w, b)$ for the value $\nu$  and $(\lambda^{\kappa} , \mu^{\kappa} , \eta^{\kappa} , w^{\kappa}, b^{\kappa})$ for the value $\kappa \nu$  with $\kappa  > 0$, then
$$\lambda^{\kappa} = \kappa \lambda , \mu^{\kappa} = \kappa \mu , \eta^{\kappa} = \kappa \eta , w^{\kappa}= \kappa w, b^{\kappa}= \kappa b.$$
As a consequence, $\delta  = \eta / \|w\| = \eta^{\kappa} / \|w^{\kappa}\| = \delta^{\kappa}$ , and the hyperplanes $H_{w,b}, H_{w,b+\eta}$ and $H_{w,b-\eta}$ are independent of $\nu$ .

*Proof.* The proof is an easy adaptation of the proof of Theorem 54.8 so we only give a sketch. The two crucial points are that the matrix
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} + \frac{1}{2K_{s}} I_{p+q}$$
is symmetric positive definite and that we have the single equational constraint
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = (p + q)K_{s}\nu$$
