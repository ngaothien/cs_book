# Summary


<!-- PAGE 1852 -->
In the special case where $J$ is an elliptic quadratic functional
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
where $A$ is symmetric positive definite, by $(\dagger_{2}$ ) an iteration of Uzawa’s method gives
$$Au^{k}-b + C^{\top}\lambda^{k} = 0$$
$$\lambda_{i}^{k+1} = \max{(\lambda^{k} + \rho (Cu^{k}-d))_{i}, 0},1 \le i \le m.$$
Theorem 50.21 implies that Uzawa’s method converges if
$$0 < \rho  < \frac{2\lambda_{1}}{\|C\|_{2}^{2}} ,$$
where $\lambda_{1}$  is the smallest eigenvalue of $A$. If we solve for $u^{k}$ using the first equation, we get
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho (-CA^{-1}C^{\top}\lambda^{k} + CA^{-1}b -d)).(*_{7})$$
In Example 50.7 we showed that the gradient of the dual function $G$ is given by
$$\nabla G_{\mu} = Cu_{\mu} -d = -CA^{-1}C^{\top}\mu  + CA^{-1}b -d,$$
so $(*_{7})$ can be written as
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \nabla G_{\lambda k});$$
this shows that Uzawa’s method is indeed the gradient method with fixed stepsize applied to the dual program.

## 50.14 Summary

The main concepts and results of this chapter are listed below: $\bullet$  The cone of feasible directions. $\bullet$  Cone with apex. $\bullet$  Active and inactive constraints. $\bullet$  Qualified constraint at $u. \bullet$  Farkas lemma. $\bullet$  Farkas–Minkowski lemma. $\bullet$  Karush–Kuhn–Tucker optimality conditions (or KKT-conditions).

<!-- PAGE 1853 -->
$\bullet$  Complementary slackness conditions. $\bullet$  Generalized Lagrange multipliers. $\bullet$  Qualified convex constraint. $\bullet$  Lagrangian of a minimization problem. $\bullet$  Equality constrained minimization. $\bullet$  KKT matrix. $\bullet$  Newton’s method with equality constraints (feasible start and infeasible start). $\bullet$  Hard margin support vector machine $\bullet$  Training data $\bullet$  Linearly separable sets of points. $\bullet$  Maximal margin hyperplane. $\bullet$  Support vectors $\bullet$  Saddle points. $\bullet$  Lagrange dual function. $\bullet$  Lagrange dual program. $\bullet$  Duality gap. $\bullet$  Weak duality. $\bullet$  Strong duality. $\bullet$  Handling equality constraints in the Lagrangian. $\bullet$  Dual of the Hard Margin SVM $(SVM_{h2}). \bullet$  Conjugate functions and Legendre dual functions. $\bullet$  Dual of the Hard Margin SVM $(SVM_{h1}). \bullet$  Uzawa’s Method.
