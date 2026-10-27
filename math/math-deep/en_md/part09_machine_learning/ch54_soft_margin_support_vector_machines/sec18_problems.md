# Problems


<!-- PAGE 2066 -->
This time we obtain $w, b, \eta , \epsilon$  and $\xi$  from $\lambda$  and $\mu$ :
$$w = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}$$
$$\epsilon  = \frac{\lambda}{2\mu K}$$
$$\xi  =K ,$$
$$2$$
and
$$(p + q)K_{s}\nu \eta  = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
The constraint
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
implies that either there is some $i_{0}$ such that $\lambda_{i0}  > 0$ or there is some $j_{0}$ such that $\mu_{j0}  > 0$, we have $\epsilon_{i0}  > 0$ or $\xi_{j0}  > 0$, which means that at least one point is misclassified, so Problem $(SVM_{s5})$ should only be used when the sets ${u_{i}}$ and ${v_{j}}$ are not linearly separable. These methods all have a kernelized version. We implemented all these methods in Matlab, solving the dual using ADMM. From a theoretical point of view, Problems $(SVM_{s4})$ and $(SVM_{s5})$ seem to have more advantages than the others since they determine $w, b, \eta$  and $b$ without requiring any condition about support vectors of type $1$. However, from a practical point of view, Problems $(SVM_{s4})$ and $(SVM_{s5})$ are less flexible that $(SVM_{s2'})$ and $(SVM_{s3})$, and we have observed that $(SVM_{s4})$ and $(SVM_{s5})$ are unable to produce as small a margin $\delta$  as $(SVM_{s2'})$ and $(SVM_{s3})$.

## 54.18 Problems

Problem 54.1. Prove the following inequality
$$ $$
$$\max \frac{1}{2p_{m}} , \frac{1}{2q_{m}} \le K \le \min \frac{1}{2p_{f}} , \frac{1}{2q_{f}}$$
stated just after Definition 54.1.

<!-- PAGE 2067 -->
Problem 54.2. Prove the averaging formulae
$$ \sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top}/|I_{\lambda}| +/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \\ i \end{pmatrix} \begin{pmatrix} v_{j} \\ j \end{pmatrix} $$
$$ \sum_{i\in I\lambda}  \sum_{j\in I\mu}  $$
$$\delta  = w^{\top}/|I_{\lambda}| -/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \end{pmatrix} \begin{pmatrix} v_{j} \end{pmatrix} $$
stated at the end of Section 54.1.
Problem 54.3. Prove that the matrix
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
has rank $p + q + 2$.
Problem 54.4. Prove that the dual program of the kernel version of $(SVM_{s1})$ is given by: Dual of Soft margin kernel SVM $(SVM_{s1})$:
$$minimize \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = \frac{1}{2}$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
where $K$ is the $\ell \times  \ell$ kernel symmetric matrix (with $\ell = p + q)$ given by
$$\kappa (u_{i}, u_{j})1 \le i \le p, 1 \le j \le q$$
$$$$
$$$$
$$-\kappa (u_{i}, v_{j-p})1 \le i \le p, p + 1 \le j \le p + q$$
$$$$
$$K_{ij} =$$
$$-\kappa (v_{i-p}, u_{j})p + 1 \le i \le p + q, 1 \le j \le p$$
$$$$
$$$$
$$\kappa (v_{i-p}, v_{j-q})p + 1 \le i \le p + q, p + 1 \le j \le p + q.$$
$$$$
Problem 54.5. Prove the averaging formula
$$\sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top} \begin{pmatrix}  \\ u_{i} \\ i \end{pmatrix} \begin{pmatrix}  \\ /|I_{\lambda}| + & v_{j} \\ j \end{pmatrix} /|I_{\mu}|/2$$
stated in Section 54.3.

<!-- PAGE 2068 -->
Problem 54.6. Prove that the kernel version of Program $(SVM_{s2})$ is given by: Dual of Soft margin kernel SVM $(SVM_{s2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
where $K$ is the $\ell \times  \ell$ kernel symmetric matrix (with $\ell = p + q)$ given at the end of Section 54.1.
Problem 54.7. Prove that the matrix
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
has rank $p + q + 1$.
Problem 54.8. Prove that the matrices
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & 0 \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & -1 \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} & 0_{p} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} & 0_{q} \end{pmatrix} andA_{2} = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
have rank $p + q + 2$.
Problem 54.9. Prove that the kernel version of Program $(SVM_{s2'})$ is given by:

<!-- PAGE 2069 -->
Dual of the Soft margin kernel SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1.
Problem 54.10. Prove the formulae determining $b$ in terms of $\eta$  stated just before Theorem 54.8.
Problem 54.11. Prove that the matrix
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
has rank $p + q + 1$.
Problem 54.12. Prove that the kernel version of Program $(SVM_{s3})$ is given by: Dual of the Soft margin kernel SVM $(SVM_{s3})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1.
Problem 54.13. Prove that the matrices
$$1_{p}^{\top}-1_{q}^{\top}0!1_{p}^{\top}-1_{q}^{\top}!$$
$$A =andA_{2} =$$
$$1_{p}^{\top}1_{q}^{\top}-11_{p}^{\top}1_{q}^{\top}$$
have rank $2$.

<!-- PAGE 2070 -->
Problem 54.14. Implement Program $(SVM_{s4})$ in Matlab. You may adapt the programs given in Section B.2 and Section B.3.
Problem 54.15. Prove that the kernel version of Program $(SVM_{s4})$ is given by: Dual of the Soft margin kernel SVM $(SVM_{s4})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$\begin{pmatrix} p + q \\ K + & I_{p+q} \\ 2 \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1.
Problem 54.16. Implement Program $(SVM_{s5})$ in Matlab. You may adapt the programs given in Section B.2 and Section B.3.
Problem 54.17. Prove that the kernel version of Program $(SVM_{s5})$ is given by: Dual of the Soft margin kernel SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} p + q \\ + & I_{p+q} \\ 2 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1.
