# A One-Dimensional Problem: Bending of a Beam


<!-- PAGE 691 -->
Chapter $19$ Variational Approximation of Boundary-Value Problems; Introduction to the Finite Elements Method

## 19.1 A One-Dimensional Problem: Bending of a Beam

Consider a beam of unit length supported at its ends in $0$ and $1$, stretched along its axis by a force $P$, and subjected to a transverse load f(x)dx per element dx, as illustrated in Figure 19.1.
$$01$$
$$dx$$
$$-PP$$
$$f(x)dx$$
$$Figure 19.1: Vertical deflection of a beam$$
The bending moment u(x) at the absissa $x$ is the solution of a boundary problem (BP) of the form
$$-u''(x) + c(x)u(x) = f(x),0 < x < 1$$
$$u(0) = \alpha$$
$$u(1) = \beta ,$$
$$691$$

<!-- PAGE 692 -->
where c(x) $= P/(EI(x))$, where $E$ is the Young’s modulus of the material of which the beam is made and I(x) is the principal moment of inertia of the cross-section of the beam at the abcissa $x$, and with $\alpha  = \beta  = 0$. For this problem, we may assume that c(x) $\ge 0$ for all $x \in [0, 1]$.
Remark: The vertical deflection w(x) of the beam and the bending moment u(x) are related by the equation
$$EI$$
$$u(x) = - \frac{d^{2}w}{dx^{2}} .$$
If we seek a solution $u \in C^{2}([0, 1])$, that is, a function whose first and second derivatives exist and are continuous, then it can be shown that the problem has a unique solution (assuming $c$ and $f$ to be continuous functions on $[0, 1])$. Except in very rare situations, this problem has no closed-form solution, so we are led to seek approximations of the solutions. One one way to proceed is to use the finite difference method, where we discretize the problem and replace derivatives by differences. Another way is to use a variational approach. In this approach, we follow a somewhat surprising path in which we come up with a so-called “weak formulation” of the problem, by using a trick based on integrating by parts! First, let us observe that we can always assume that $\alpha  = \beta  = 0$, by looking for a solution of the form u(x) $-(\alpha (1 -x) + \beta x)$. This turns out to be crucial when we integrate by parts. There are a lot of subtle mathematical details involved to make what follows rigorous, but here, we will take a “relaxed” approach. First, we need to specify the space of “weak solutions.” This will be the vector space $V$ of continuous functions $f$ on $[0, 1]$, with f(0) $=$ f(1) $= 0$, and which are piecewise continuously differentiable on $[0, 1]$. This means that there is a finite number of points $x_{0}, \dots  , x_{N+1}$ with $x_{0} = 0$ and $x_{N+1} = 1$, such that $f'(x_{i})$ is undefined for $i = 1, \dots  , N$, but otherwise f' is defined and continuous on each interval $(x_{i}, x_{i+1})$ for $i = 0, \dots  , N.^{1}$ The space $V$ becomes a Euclidean vector space under the inner product
$$\langle f, g\rangle_{V}  = \int_{0}^{}  1(f(x)g(x) + f' (x)g'(x))dx,$$
for all $f, g \in V$ . The associated norm is
$$\|f\|_{V} = \int_{0}^{}  1/2.$$
$$\begin{pmatrix} 1 \\ (f(x)^{2}+ f'(x)^{2})dx \end{pmatrix}$$
Assume that $u$ is a solution of our original boundary problem (BP), so that
$$-u''(x) + c(x)u(x) = f(x),0 < x < 1$$
$$u(0) = 0$$
$$u(1) = 0.$$
$\overline{1}\overline{We} \overline{also} \overline{assume} \overline{that} \overline{f}'\overline{(}\overline{x}\overline{)} \overline{has} \overline{a} \overline{limit}$ when $x$ tends to a boundary of $(x_{i}, x_{i+1})$.

<!-- PAGE 693 -->
Multiply the differential equation by any arbitrary test function $v \in V$ , obtaining
$$-u''(x)v(x) + c(x)u(x)v(x) = f(x)v(x),(*)$$
and integrate this equation! We get
$$- \int_{0}^{}  1u''(x)v(x)dx + \int_{0}^{}  1c(x)u(x)v(x)dx = \int_{0}^{}  1f(x)v(x)dx.(\dagger )$$
Now, the trick is to use integration by parts on the first term. Recall that
$$(u'v)'= u''v + u'v',$$
and to be careful about discontinuities, write
$$\int_{0}^{}  1u''(x)v(x)dx = \sum_{i=0}^{N}  \int_{x}^{}  xi+1u''(x)v(x)dx.$$
$$i$$
Using integration by parts, we have
$$\int_{x}^{}  xi+1u''(x)v(x)dx = \int_{x}^{}  xi+1(u'(x)v(x))'dx - \int_{x}^{}  xi+1u'(x)v'(x)dx$$
$$iii$$
$$= [u'(x)v(x)]_{x=xi}^{x=xi+1}- \int_{x}^{}  xi+1u'(x)v'(x)dx$$
$$i$$
$$= u'(x_{i+1})v(x_{i+1}) -u'(x_{i})v(x_{i}) - \int_{x}^{}  xi+1u'(x)v'(x)dx.$$
$$i$$
It follows that
$$\int_{0}^{}  1u''(x)v(x)dx = \sum_{i=0}^{N}  \int_{x}^{}  xi+1u''(x)v(x)dx$$
$$i$$
$$= \sum_{i=0}^{N}  \begin{pmatrix} xi+1 \\ u'(x_{i+1})v(x_{i+1}) -u'(x_{i})v(x_{i}) - & u'(x)v'(x)dx \\ i \\ 1 \end{pmatrix} \int_{x}^{}$$
$$= u'(1)v(1) -u'(0)v(0) - \int_{0}^{}  u'(x)v'(x)dx.$$
However, the test function $v$ satisfies the boundary conditions v(0) $=$ v(1) $= 0$ (recall that $v \in V$ ), so we get
$$\int_{0}^{}  1u''(x)v(x)dx = - \int_{0}^{}  1u'(x)v'(x)dx.$$
Consequently, the equation $(\dagger$ ) becomes
$$\int_{0}^{}  1u'(x)v'(x)dx + \int_{0}^{}  1c(x)u(x)v(x)dx = \int_{0}^{}  1f(x)v(x)dx,$$

<!-- PAGE 694 -->
or
$$\int_{0}^{}  1(u'v' + cuv)dx = \int_{0}^{}  1fvdx,for all v \in V.(**)$$
Thus, it is natural to introduce the bilinear form a: $V \times  V \to \mathbb{R}$ given by
$$a(u, v) = \int_{0}^{}  1(u'v' + cuv)dx,for all u, v \in V ,$$
and the linear form $f$ : $V \to \mathbb{R}$ given by
$$e$$
$$f(v) = \int_{0}^{}  1f(x)v(x)dx,for all v \in V .$$
$$e$$
Then, (**) becomes
$$a(u, v) =f(v),for all v \in V.$$
$$e$$
We also introduce the energy function $J$ given by
$$J(v) = \frac{1}{2} a(v, v) -fe(v)v \in V.$$
Then, we have the following theorem.

> **Theorem 19.1.** Let $u$ be any solution of the boundary problem (BP).
$(1)$ Then we have
$$a(u, v) =f(v),for all v \in V,(WF)$$
$$e$$
where
$$a(u, v) = \int_{0}^{}  1(u'v' + cuv)dx,for all u, v \in V ,$$
and
$$f(v) = \int_{0}^{}  1f(x)v(x)dx,for all v \in V .$$
$$e$$
$(2)$ If c(x) $\ge 0$ for all $x \in [0, 1]$, then a function $u \in V$ is a solution of $(WF)$ iff $u$ minimizes J(v), that is,
$$J(u) = \inf J(v),$$
$$v\in V$$
with
$$J(v) = \frac{1}{2} a(v, v) -fe(v)v \in V.$$
Furthermore, $u$ is unique.

<!-- PAGE 695 -->

*Proof.* We already proved $(1)$. To prove $(2)$, first we show that
$$\|v\|_{V}^{2} \le 2a(v, v),for all v \in V.$$
For this, it suffices to prove that
$$\|v\|_{V}^{2} \le 2 \int_{0}^{}  1(f' (x))^{2}dx,for all v \in V.$$
However, by Cauchy-Schwarz for functions, for every $x \in [0, 1]$, we have
$$|v(x)| = \int_{0}^{}  xv'(t)dt



$\le \int_{0}^{}$  1|v'(t)|dt $\le \int_{0}^{}  1/2,$$$
$$\begin{pmatrix} 1 \\ |v'(t)|^{2}dt \end{pmatrix}$$
and so
$$\|v\|_{V}^{2} = \int_{0}^{}  1((v(x))^{2} + (v'(x))^{2})dx \le 2 \int_{0}^{}  1(v'(x))^{2}dx \le 2a(v, v),$$
since
$$a(v, v) = \int_{0}^{}  1((v')^{2} + cv^{2})dx.$$
Next, it is easy to check that
$$J(u + v) -J(u) = a(u, v) -fe(v) + \frac{1}{2} a(v, v),for all u, v \in V .$$
Then, if $u$ is a solution of $(WF)$, we deduce that
$$J(u + v) -J(u) = \frac{1}{2} a(v, v) \ge \frac{1}{4} \|v\|_{V} \ge 0for all v \in V.$$
since a(u, $v)$ - f(v) $= 0$ for all $v \in V$ . Therefore, $J$ achieves a minimun for $u$.
$$e$$
We also have
$$J(u + \theta v) -J(u) = \theta (a(u, v) -f(v)) + \frac{\theta^{2}}{2} a(v, v)for all \theta  \in \mathbb{R},$$
and so J(u $+ \theta v)$ - J(u) $\ge 0$ for all $\theta  \in \mathbb{R}$. Consequently, if $J$ achieves a minimum for $u$, then a(u, $v) =$ f(v), which means that $u$ is a solution of $(WF)$.
$$e$$
Finally, assuming that c(x) $\ge 0$, we claim that if $v \in V$ and $v \neq  0$, then a(v, $v) > 0$. This is because if a(v, $v) = 0$, since
$$\|v\|_{V}^{2} \le 2a(v, v)for all v \in V,$$
we would have $\|v\|_{V} = 0$, that is, $v = 0$. Then, if $v \neq  0$, from
$$J(u + v) -J(u) = \frac{1}{2} a(v, v)for all v \in V$$
we see that J(u $+ v) >$ J(u), so the minimum $u$ is unique

<!-- PAGE 696 -->
Theorem 19.1 shows that every solution $u$ of our boundary problem (BP) is a solution (in fact, unique) of the equation (WF). The equation (WF) is called the weak form or variational equation associated with the boundary problem. This idea to derive these equations is due to Ritz and Galerkin. Now, the natural question is whether the variational equation (WF) has a solution, and whether this solution, if it exists, is also a solution of the boundary problem (it must belong to $C^{2}([0, 1])$, which is far from obvious). Then, (BP) and (WF) would be equivalent. Some fancy tools of analysis can be used to prove these assertions. The first difficulty is that the vector space $V$ is not the right space of solutions, because in order for the variational problem to have a solution, it must be complete. So, we must construct a completion of the vector space $V$ . This can be done and we get the Sobolev space $H_{0}^{1}(0, 1)$. Then, the question of the regularity of the “weak solution” can also be tackled. We will not worry about all this. Instead, let us find approximations of the problem (WF). Instead of using the infinite-dimensional vector space $V$ , we consider finite-dimensional subspaces $V_{a}$ (with $dim(V_{a}) = n)$ of $V$ , and we consider the discrete problem: Find a function $u^{(a)} \in V_{a}$, such that
$$a(u^{(a)}, v) =f(v),for all v \in V_{a}.(DWF)$$
$$e$$
Since $V_{a}$ is finite dimensional (of dimension $n)$, let us pick a basis of functions $(w_{1}, \dots  , w_{n})$ in $V_{a}$, so that every function $u \in V_{a}$ can we written as
$$u = u_{1}w_{1} + \cdots  + u_{n}w_{n}.$$
Then, the equation (DWF) holds iff
$$a(u, w_{j}) =f(w_{j}),j = 1, \dots  , n,$$
$$e$$
and by plugging $u_{1}w_{1} + \cdots  + u_{n}w_{n}$ for $u$, we get a system of $k$ linear equations
$$\sum_{i=1}^{n}  a(w_{i}, w_{j})u_{i} = fe(w_{j}),1 \le j \le n.$$
Because a(v, $v) \ge_{2}^{1}  \|v\|_{Va}$, the bilinear form a is symmetric positive definite, and thus the matrix $(a(w_{i}, w_{j}))$ is symmetric positive definite, and thus invertible. Therefore, (DWF) has a solution given by a linear system! From a practical point of view, we have to compute the integrals
$$a_{ij} = a(w_{i}, w_{j}) = \int_{0}^{}  1(w_{i}'w_{j}' + cw_{i}w_{j})dx,$$
and
$$b_{j} =f(w_{j}) = \int_{0}^{}  1f(x)w_{j}(x)dx.$$
$$e$$

<!-- PAGE 697 -->
However, if the basis functions are simple enough, this can be done “by hand.” Otherwise, numerical integration methods must be used, but there are some good ones. Let us also remark that the proof of Theorem 19.1 also shows that the unique solution of
(DWF) is the unique minimizer of $J$ over all functions in $V_{a}$. It is also possible to compare the approximate solution $u^{(a)} \in V_{a}$ with the exact solution $u \in V$ .

> **Theorem 19.2.** Suppose c(x) $\ge 0$ for all $x \in [0, 1]$. For every finite-dimensional subspace $V_{a} (dim(V_{a}) = n)$ of $V$ , for every basis $(w_{1}, \dots  , w_{n})$ of $V_{a}$, the following properties hold:
$(1)$ There is a unique function $u^{(a)} \in V_{a}$ such that
$$a(u^{(a)}, v) =f(v),for all v \in V_{a},(DWF)$$
$$e$$
and if $u^{(a)} = u_{1}w_{1} + \cdots  + u_{n}w_{n}$, then $u = (u_{1}, \dots  , u_{n})$ is the solution of the linear system
$$Au = b,(*)$$
with $A = (a_{ij}) = (a(w_{i}, w_{j}))$ and $b_{j} = f(w_{j}), 1 \le i, j \le n$. Furthermore, the matrix
$$e$$
$A = (a_{ij})$ is symmetric positive definite.
$(2)$ The unique solution $u^{(a)} \in V_{a}$ of $(DWF)$ is the unique minimizer of $J$ over $V_{a}$, that is,
$$J(u^{(a)}) = \inf J(v),$$
$$v\in Va$$
$(3)$ There is a constant $C$ independent of $V_{a}$ and of the unique solution $u \in V$ of $(WF)$, such that
$$u -u_{V}^{(a)}

$\le C \inf \|u -v\|_{V}$ .$$
$$v\in Va$$
We proved $(1)$ and $(2)$, but we will omit the proof of $(3)$ which can be found in Ciarlet $[41]$. Let us now give examples of the subspaces $V_{a}$ used in practice. They usually consist of piecewise polynomial functions. Pick an integer $N \ge 1$ and subdivide $[0, 1]$ into $N + 1$ intervals $[x_{i}, x_{i+1}]$, where
$$x_{i} = hi,h = \frac{1}{N+ 1} ,i = 0, \dots  , N + 1.$$
We will use the following fact: every polynomial P(x) of degree 2m $+ 1 (m \ge 0)$ is completely determined by its values as well as the values of its first $m$ derivatives at two distinct points $\alpha , \beta  \in \mathbb{R}$.

<!-- PAGE 698 -->
There are various ways to prove this. One way is to use the Bernstein basis, because the kth derivative of a polynomial is given by a formula in terms of its control points. For example, for $m = 1$, every degree $3$ polynomial can be written as
$$P(x) = (1 -x)^{3}b_{0} + 3(1 -x)^{2}x b_{1} + 3(1 -x)x^{2}b_{2} + x^{3}b_{3},$$
with $b_{0}, b_{1}, b_{2}, b_{3} \in \mathbb{R}$, and we showed that
$$P' (0) = 3(b_{1} -b_{0})$$
$$P' (1) = 3(b_{3} -b_{2}).$$
Given P(0) and P(1), we determine $b_{0}$ and $b_{3}$, and from P' $(0)$ and P' $(1)$, we determine $b_{1}$ and $b_{2}$. In general, for a polynomial of degree $m$ written as
$$P(x) = \sum_{j=0}^{m}  b_{j}B_{j}^{m} (x)$$
in terms of the Bernstein basis $(B_{0}^{m} (x), \dots  , B_{m}^{m}(x))$ with
$$B_{j}^{m} (x) = \begin{pmatrix} m \\ j \end{pmatrix} (1 -x)^{m-j}x^{j},$$
it can be shown that the kth derivative of $P$ at zero is given by
$$P^{(k)}(0) = m(m -1) \cdots  (m -k + 1) \begin{pmatrix} k \\ i \end{pmatrix} \sum_{i=0}^{k}  \begin{pmatrix} (-1)^{k-i}b_{i} \end{pmatrix} ,$$
and there is a similar formula for $P^{(k)} (1)$. Actually, we need to use the Bernstein basis of polynomials $B_{k}^{m} [r, s]$, where
$$x^{m-j}r^{j}$$
$$B_{j}^{m} [r, s](x) = \begin{pmatrix} m \\ j \end{pmatrix} \begin{pmatrix} s - \\ s -r \end{pmatrix} \begin{pmatrix} x - \\ s -r \end{pmatrix} ,$$
with $r < s$, in which case
$$- \cdots  -$$
$$P^{(k)} (0) = \frac{m(m1) (mk + 1)}{(s -r)^{k}} \begin{pmatrix} k \\ i \end{pmatrix} \sum_{i=0}^{k}  \begin{pmatrix} (-1)^{k-i}b_{i} \end{pmatrix} ,$$
with a similar formula for $P^{(k)} (1)$. In our case, we set $r = x_{i}, s = x_{i+1}$. Now, if the 2m $+ 2$ values
$$P(0), P^{(1)} (0), \dots  , P^{(m)} (0), P(1), P^{(1)} (1), \dots  , P^{(m)} (1)$$

<!-- PAGE 699 -->
are given, we obtain a triangular system that determines uniquely the 2m $+ 2$ control points $b_{0}, \dots  , b_{2m+1}$. Recall that $C^{m}([0, 1])$ denotes the set of $C^{m}$ functions $f$ on $[0, 1]$, which means that $f, f^{(1)}, \dots  , f^{(m)}$ exist are are continuous on $[0, 1]$. We define the vector space $V_{N}^{m}$  as the subspace of $C^{m}([0, 1])$ consisting of all functions $f$ such that $1$. f(0) $=$ f(1) $= 0. 2$. The restriction of $f$ to $[x_{i}, x_{i+1}]$ is a polynomial of degree 2m $+ 1$, for $i = 0, \dots  , N$. Observe that the functions in $V_{N}^{0}$  are the piecewise affine functions $f$ with f(0) $=$ f(1) $= 0$; an example is shown in Figure 19.2.
$$y$$
$$x$$
$$0ih1$$
$$Figure 19.2: A piecewise affine function$$
This space has dimension $N$, and a basis consists of the “hat functions” $w_{i}$, where the only two nonflat parts of the graph of $w_{i}$ are the line segments from $(x_{i-1}, 0)$ to $(x_{i}, 1)$, and from $(x_{i}, 1)$ to $(x_{i+1}, 0)$, for $i = 1, \dots  , N$, see Figure 19.3. The basis functions $w_{i}$ have a small support, which is good because in computing the integrals giving $a(w_{i}, w_{j})$, we find that we get a tridiagonal matrix. They also have the nice property that every function $v \in V_{N}^{0}$  has the following expression on the basis $(w_{i})$:
$$v(x) = \sum_{i=1}^{N}  v(ih)w_{i}(x),x \in [0, 1].$$

<!-- PAGE 700 -->
$$y$$
$$w$$
$$i$$
$$x$$
$$(i -1)hih(i + 1)h$$
$$Figure 19.3: A basis “hat function”$$
In general, it it not hard to see that $V_{N}^{m}$  has dimension mN $+$ 2(m - $1)$. Going back to our problem (the bending of a beam), assuming that $c$ and $f$ are constant functions, it is not hard to show that the linear system (*) becomes
$$\frac{1}{h} \begin{pmatrix} 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ -1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ \ddots & \ddots & \ddots \\ -1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ 1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{N-1} \\ u_{N} \end{pmatrix} = h \begin{pmatrix} f \\ f \\ \vdots \\ f \\ f \end{pmatrix} .$$
$$-$$
We can also find a basis of 2N $+ 2$ cubic functions for $V_{N}^{1}$  consisting of functions with small support. This basis consists of the $N$ functions $w_{i}^{0}$ and of the $N + 2$ functions $w_{i}^{1}$

<!-- PAGE 701 -->
uniquely determined by the following conditions:
$$w_{i}^{0} (x_{j}) = \delta_{ij} ,1 \le j \le N, 1 \le i \le N$$
$$(w_{i}^{0} )'(x_{j}) = 0,0 \le j \le N + 1, 1 \le i \le N$$
$$w_{i}^{1} (x_{j}) = 0,1 \le j \le N, 0 \le i \le N + 1$$
$$(w_{i}^{1} )'(x_{j}) = \delta_{ij} ,0 \le j \le N + 1, 0 \le i \le N + 1$$
with $\delta_{ij}  = 1$ iff $i = j$ and $\delta_{ij}  = 0$ if $i \neq  j$. Some of these functions are displayed in Figure 19.4. The function $w_{i}^{0}$ is given explicitly by
$$w_{i}^{0} (x) = \frac{1}{h^{3}} (x -(i -1)h)^{2}((2i + 1)h -2x),(i -1)h \le x \le ih,$$
$$w_{i}^{0} (x) = \frac{1}{h^{3}} ((i + 1)h -x)^{2}(2x -(2i -1)h),ih \le x \le (i + 1)h,$$
for $i = 1, \dots  , N$. The function $w_{j}^{1}$ is given explicitly by
$$w_{j}^{1}(x) = - \frac{1}{h^{2}} (ih -x)(x -(i -1)h)^{2},(i -1)h \le x \le ih,$$
and
$$w_{j}^{1}(x) = \frac{1}{h^{2}} ((i + 1)h -x)^{2}(x -ih),ih \le x \le (i + 1)h,$$
for $j = 0, \dots  , N + 1$. Furthermore, for every function $v \in V_{N}^{1}$ , we have
$$v(x) = \sum_{i=1}^{N}  v(ih)w_{i}^{0} (x) + \sum_{j=0}^{N+1}  v'jih)w_{j}^{1}(x),x \in [0, 1].$$
If we order these basis functions as
$$w_{0}^{1}, w_{1}^{0}, w_{1}^{1}, w_{2}^{0}, w_{2}^{1}, \dots  , w_{N}^{0}, w_{N}^{1}, w_{N+1}^{1},$$
we find that if $c = 0$, the matrix $A$ of the system (*) is tridiagonal by blocks, where the blocks are $2 \times  2, 2 \times  1$, or $1 \times  2$ matrices, and with single entries in the top left and bottom right corner. A different order of the basis vectors would mess up the tridiagonal block structure of $A$. We leave the details as an exercise. Let us now take a quick look at a two-dimensional problem, the bending of an elastic membrane.
