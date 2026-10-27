# A Two-Dimensional Problem: An Elastic Membrane


<!-- PAGE 702 -->
$$y$$
$$w_{i}^{0}$$
$$w_{0}^{1}w_{j}^{1}w_{N+1}^{1}$$
$$x$$
$$0ihjh1$$
$$Figure 19.4: The basis functions w_{i}^{0} and w_{j}^{1}$$

## 19.2 A Two-Dimensional Problem: An Elastic

$$Membrane$$
Consider an elastic membrane attached to a round contour whose projection on the $(x_{1}, x_{2})-$ plane is the boundary $\Gamma$  of an open, connected, bounded region $\Omega$ in the $(x_{1}, x_{2})-plane$, as illustrated in Figure 19.5. In other words, we view the membrane as a surface consisting of the set of points $(x, z)$ given by an equation of the form
$$z = u(x),$$
with $x = (x_{1}, x_{2}) \in \overline{\Omega$ ,} where $u: \overline{\Omega} \to \mathbb{R}$ is some sufficiently regular function, and we think of u(x) as the vertical displacement of this membrane. We assume that this membrane is under the action of a vertical force $\tau$ f(x)dx per surface element in the horizontal plane (where $\tau$  is the tension of the membrane). The problem is

<!-- PAGE 703 -->
$$\tau f(x)dx$$
$$g(y)$$
$$u(x)$$
$$x_{2}$$
$$\Omega$$
$$dxx$$
$$y$$
$$x_{1}\Gamma$$
$$Figure 19.5: An elastic membrane$$
to find the vertical displacement $u$ as a function of $x$, for $x \in \overline{\Omega$ .} It can be shown (under some assumptions on $\Omega , \Gamma$ , and $f)$, that u(x) is given by a PDE with boundary condition, of the form
$$-\Delta u(x) = f(x),x \in \Omega$$
$$u(x) = g(x),x \in \Gamma ,$$
$$where g: \Gamma  \to \mathbb{R} represents \frac{the}{(\Omega ).} height of the contour of the membrane. We are looking for$$
a function $u$ in $C^{2}(\Omega$ ) $\cap C^{1}$  The operator $\Delta$ is the Laplacian, and it is given by
$$\Delta u(x) = \frac{\partial^{2} u}{\partial x_{1}^{2}} (x) + \frac{\partial^{2} u}{\partial x_{2}^{2}} (x).$$
This is an example of a boundary problem, since the solution $u$ of the PDE must satisfy the condition u(x) $=$ g(x) on the boundary of the domain $\Omega$ . The above equation is known as Poisson’s equation, and when $f = 0$ as Laplace’s equation. It can be proved that if the data $f, g$ and $\Gamma$  are sufficiently smooth, then the problem has a unique solution. To get a weak formulation of the problem, first we have to make the boundary condition homogeneous, which means that g(x) $= 0$ on $\Gamma$ . It turns out that $g$ can be extended to the whole of $\overline{\Omega as}$ some sufficiently smooth function $h$, so we can look for a solution of the form
$$b$$
$u$ - $h$, but for simplicity, let us assume that the contour of $\Omega$ lies in a plane parallel to the $b (x_{1}, x_{2})-$ plane, so that $g = 0$. We let $V$ be the subspace of $C^{2}(\Omega$ ) $\cap C^{1}\overline{(\Omega$ )} consisting of functions $v$ such that $v = 0$ on $\Gamma$ .

<!-- PAGE 704 -->
As before, we multiply the PDE by a test function $v \in V$ , getting
$$-\Delta u(x)v(x) = f(x)v(x),$$
and we “integrate by parts.” In this case, this means that we use a version of Stokes formula known as Green’s first identity, which says that
$$\int_{\Omega}  -\Delta u v dx = \int_{\Omega}  (grad u) \cdot  (grad v) dx - \int_{\Gamma}  (grad u) \cdot  n vd\sigma$$
(where $n$ denotes the outward pointing unit normal to the surface). Because $v = 0$ on $\Gamma$ , the
$$integral \int_{\Gamma}  drops out, and we get an equation of the form$$
$$a(u, v) =f(v)for all v \in V,$$
$$e$$
where a is the bilinear form given by
$$a(u, v) = \int_{\Omega}  \begin{pmatrix} \partial u \\ \partial v & \partial u\partial v \\ + \\ \partial x_{1}\partial x_{1} & \partial x_{2}\partial x_{2} \end{pmatrix} dx$$
and $f$ is the linear form given by
$$e \int_{\Omega}$$
$$f(v) =fvdx.$$
$$e$$
We get the same equation as in section 19.2, but over a set of functions defined on a two-dimensional domain. As before, we can choose a finite-dimensional subspace $V_{a}$ of $V$ and consider the discrete problem with respect to $V_{a}$. Again, if we pick a basis $(w_{1}, \dots  , w_{n})$ of $V_{a}$, a vector $u = u_{1}w_{1} + \cdots  + u_{n}w_{n}$ is a solution of the Weak Formulation of our problem iff $u = (u_{1}, \dots  , u_{n})$ is a solution of the linear system
$$Au = b,$$
with $A = (a(w_{i}, w_{j}))$ and $b = (f(w_{j}))$. However, the integrals that give the entries in $A$ and
$$e$$
$b$ are much more complicated. An approach to deal with this problem is the method of finite elements. The idea is to also discretize the boundary curve $\Gamma$ . If we assume that $\Gamma$  is a polygonal line, then we can triangulate the domain $\Omega$ , and then we consider spaces of functions which are piecewise defined on the triangles of the triangulation of $\Omega$ . The simplest functions are piecewise affine and look like tents erected above groups of triangles. Again, we can define base functions with small support, so that the matrix $A$ is tridiagonal by blocks. The finite element method is a vast subject and it is presented in many books of various degrees of difficulty and obscurity. Let us simply state three important requirements of the finite element method:
