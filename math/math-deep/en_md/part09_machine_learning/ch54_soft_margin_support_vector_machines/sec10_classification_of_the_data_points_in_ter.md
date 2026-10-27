# Classification of the Data Points in Terms of  (SVMs3)


<!-- PAGE 2029 -->
with $K_{s} = 1/(p + q)$. Tracing through the derivation of the dual program, we obtain Dual of the Soft margin kernel SVM $(SVM_{s3})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
where $K$ is the kernel matrix of Section 54.1. We obtain
$$w = \sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j})$$
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$
The classification function
$$f(x) = sgn(\langle w, \phi (x)\rangle -b)$$
is given by
$$f(x) = sgn \begin{pmatrix} \lambda_{i} (\kappa (u_{i}, x) + 1) - & \mu_{j} (\kappa (v_{j}, x) + 1) \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  .$$

## 54.10 Classification of the Data Points in Terms of \nu

$$(SVM)$$
$$s3$$
The equations $(\dagger$ ) and the box inequalities
$$0 \le \lambda_{i}  \le K_{s},0 \le \mu_{j}  \le K_{s}$$
also imply the following facts (recall that $\delta  = \eta / \|w\|)$:

> **Proposition 54.5.** If Problem $(SVM_{s3})$ has an optimal solution with $w \neq  0$ and $\eta  > 0$ then the following facts hold:

<!-- PAGE 2030 -->
$(1)$ Let $p_{f}$ be the number of points $u_{i}$ such that $\lambda_{i}  = K_{s}$, and let $q_{f}$ the number of points $v_{j}$ such that $\mu_{j}  = K_{s}$. Then $p_{f} + q_{f} \le (p + q)\nu$ .
$(2)$ Let $p_{m}$ be the number of points $u_{i}$ such that $\lambda_{i}  > 0$, and let $q_{m}$ the number of points $v_{j}$ such that $\mu_{j}  > 0$. Then $p_{m} + q_{m} \ge (p + q)\nu$ . We have $p_{m} + q_{m} \ge 1$.
$(3)$ If $p_{f} \ge 1$ or $q_{f} \ge 1$, then $\nu  \ge 1/(p + q)$.

*Proof.* $(1)$ Recall that for an optimal solution with $w \neq  0$ and $\eta  > 0$ we have the equation
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu .$$
Since there are $p_{f}$ points $u_{i}$ such that $\lambda_{i}  = K_{s} = 1/(p + q)$ and $q_{f}$ points $v_{j}$ such that $\mu_{j}  = K_{s} = 1/(p + q)$, we have
$$\nu  = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \frac{p_{f}+ q_{f}}{p + q} ,$$
so
$$p_{f} + q_{f} \le \nu (p + q).$$
$(2)$ If
$$I_{\lambda >0} = {i \in {1, \dots  , p} | \lambda_{i}  > 0}andp_{m} = |I_{\lambda >0}|$$
and
$$I_{\mu >0} = {j \in {1, \dots  , q} | \mu_{j}  > 0}andq_{m} = |I_{\mu >0}|,$$
then
$$\nu  = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j} ,$$
and since $\lambda_{i} , \mu_{j}  \le K_{s} = 1/(p + q)$, we have
$$\nu  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j}  \le \frac{p_{m} + q_{m}}{p + q} ,$$
which yields
$$p_{m} + q_{m} \ge \nu (p + q).$$
We already noted earlier that $p_{m} + q_{m} \ge 1$.
$(3)$ This follows immediately from $(1)$.
