# Kernel -SV Regression


<!-- PAGE 2134 -->
$q_{m} = 19$. There are $13$ points strictly inside the slab. The last value of $\nu$  is $\nu  =$ 0.97, see Figure 56.15. We have $p_{f} = 23, q_{f} = 24, p_{m} = 25$ and $q_{m} = 25$. There are $0$ points strictly inside the slab. The slab is so narrow that it does not contain any of the points $x_{i}$ in it. Running the program with any value $\nu  >$ 0.97 yields $\epsilon  = 0$.
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.15: Running \nu -SV regression on a set of 50 points; \nu  = 0.97.$$

## 56.4 Kernel \nu -SV Regression

Since the formulae for $w, b$, and f(x),
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i}$$
$$b = \frac{1}{2} \begin{pmatrix} y_{i0}+ y_{j0}-w^{\top}(x_{i0}+ x_{j0}) \end{pmatrix}$$
$$f(x) = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i}^{\top} x + b,$$
only involve inner products among the data points $x_{i}$ and $x$, and since the objective function $-G(\alpha , \mu$ ) of the dual program also only involves inner products among the data points $x_{i}$, we can kernelize the $\nu$ -SV regression method.

<!-- PAGE 2135 -->
As in the previous section, we assume that our data points ${x_{1}, \dots  , x_{m}}$ belong to a $set\mathcal{X}$ and we pretend that we have feature space $(F, \langle$ -, $-\rangle$ ) and a feature embedding map $\phi$ : $\mathcal{X} \to F$, but we only have access to the kernel function $\kappa (x_{i}, x_{j}) = \langle \phi (x_{i}), \phi (x_{j})\rangle$ . We wish to perform $\nu$ -SV regression in the feature space $F$ on the data set ${(\phi (x_{1}), y_{1}), \dots  , (\phi (x_{m}), y_{m})}$. Going over the previous computation, we see that the primal program is given by Program kernel $\nu$ -SV Regression:
$$minimize \frac{1}{2} \langle w, w\rangle + C \begin{pmatrix} 1 \\ \nu \epsilon  + & (\xi_{i}  + \xi_{i}' ) \\ m \end{pmatrix} \sum_{i=1}^{m}$$
$$subject to$$
$$\langle w, \phi (x_{i})\rangle + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-\langle w, \phi (x_{i})\rangle -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m$$
$$\epsilon  \ge 0,$$
minimizing over the variables $w, \epsilon , b, \xi$ , and $\xi'$ . The Lagrangian is given by
$$*+$$
$$L(w, b, \lambda , \mu , \gamma , \xi , \xi' , \epsilon , \alpha , \beta ) = \frac{1}{2} \langle w, w\rangle +w, \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )\phi (x_{i})$$
$$!$$
$$+ \epsilon C\nu  -\gamma  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )+ \sum_{i=1}^{m}  \xi_{i} \begin{pmatrix} C \\ -\lambda_{i}  -\alpha_{i} \\ m \end{pmatrix}$$
$$!$$
$$+ \sum_{i=1}^{m}  \xi_{i}' \begin{pmatrix} C \\ -\mu_{i}  -\beta_{i} \\ m \end{pmatrix} + b \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )- \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}.$$
Setting the gradient $\nabla L_{w,\epsilon ,b,\xi ,\xi'}$ of the Lagrangian to zero, we also obtain the equations
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\phi (x_{i}),(*_{w})$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  + \gamma  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} .$$
Using the above equations, we find that the dual function $G$ is independent of the variables $\beta , \alpha , \beta$ , and we obtain the following dual program:

<!-- PAGE 2136 -->
Dual Program kernel $\nu$ -SV Regression:
$$minimize \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )\kappa (x_{i}, x_{j}) + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  \le C\nu$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m,$$
minimizing over $\alpha$  and $\mu$ . Everything we said before also applies to the kernel $\nu$ -SV regression method, except that $x_{i}$ is replaced by $\phi (x_{i})$ and that the inner product $\langle$ -, $-\rangle$ must be used, and we have the formulae
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\phi (x_{i})$$
$$!$$
$$b = \frac{1}{2} y_{i0} + y_{j0} - \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )(\kappa (x_{i}, x_{i0}) + \kappa (x_{i}, x_{j0}))$$
$$f(x) = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\kappa (x_{i}, x) + b,$$
expressions that only involve $\kappa$ .
Remark: There is a variant of $\nu$ -SV regression obtained by setting $\nu  = 0$ and holding $\epsilon  > 0$ fixed. This method is called $\epsilon$ -SV regression or (linear) $\epsilon$ -insensitive SV regression. The corresponding optimization program is Program $\epsilon$ -SV Regression:
$$minimize \frac{1}{2} w^{\top}w + \frac{C}{m} \sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' )$$
$$subject to$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m,$$
minimizing over the variables $w, b, \xi$ , and $\xi'$ , holding $\epsilon$  fixed. It is easy to see that the dual program is
