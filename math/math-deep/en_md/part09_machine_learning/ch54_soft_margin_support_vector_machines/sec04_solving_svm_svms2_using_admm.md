# Solving SVM (SVMs2) Using ADMM


<!-- PAGE 1993 -->
Dual of Soft margin kernel SVM $(SVM_{s2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
where $K$ is the $\ell \times  \ell$ kernel symmetric matrix (with $\ell = p + q)$ given at the end of Section 54.1. We also find that
$$w = \sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j}),$$
so
$$b = \frac{1}{2} \begin{pmatrix} \lambda_{i} (\kappa (u_{i}, u_{i0}) + \kappa (u_{i}, v_{j0})) - & \mu_{j} (\kappa (v_{j}, u_{i0}) + \kappa (v_{j}, v_{j0})) \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  ,$$
and the classification function
$$f(x) = sgn(\langle w, \phi (x)\rangle -b)$$
is given by
$$$$
$$f(x) = sgn \sum_{i=1}^{p}  \lambda_{i} (2\kappa (u_{i}, x) -\kappa (u_{i}, u_{i0}) -\kappa (u_{i}, v_{j0}))$$
$$$$
$$- \sum_{j=1}^{q}  \mu_{j} (2\kappa (v_{j}, x) -\kappa (v_{j}, u_{i0}) -\kappa (v_{j}, v_{j0})).$$

## 54.4 Solving SVM (SVM ) Using ADMM

$$s2$$
In order to solve $(SVM_{s2})$ using ADMM we need to write the matrix corresponding to the constraints in equational form,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\lambda_{i}  + \alpha_{i}  = K,i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K,j = 1, \dots  , q.$$
