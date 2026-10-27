# Rayleigh–Ritz Theorems and Eigenvalue Interlacing


<!-- PAGE 645 -->
Recall from Proposition 14.15 that when $E$ is a Hermitian space and $(e_{1}, \dots , e_{n})$ is an orthonormal basis for $E$, if $A$ is the matrix of a linear map $f$ : $E \to E$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, then $A^{*}$ is the matrix of the adjoint $f^{*}$ of $f$. Consequently, a normal linear map has a normal matrix, a self-adjoint linear map has a Hermitian matrix, a skew-self-adjoint linear map has a skew-Hermitian matrix, and a unitary linear map has a unitary matrix. Furthermore, if $(u_{1}, \dots  , u_{n})$ is another orthonormal basis for $E$ and $P$ is the change of basis matrix whose columns are the components of the $u_{i}$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, then $P$ is unitary, and for any linear map $f$ : $E \to E$, if $A$ is the matrix of $f$ w.r.t $(e_{1}, \dots  , e_{n})$ and $B$ is the matrix of $f$ w.r.t. $(u_{1}, \dots  , u_{n})$, then
$$B = P^{*} AP.$$
Theorem 17.13 and Proposition 17.7 can be restated in terms of matrices as follows.

> **Theorem 17.22.** For every complex normal matrix $A$ there is a unitary matrix $U$ and a diagonal matrix $D$ such that $A = UDU^{*}$ . Furthermore, if $A$ is Hermitian, then $D$ is a real matrix; if $A$ is skew-Hermitian, then the entries in $D$ are pure imaginary or zero; and if $A$ is unitary, then the entries in $D$ have absolute value $1$.

## 17.6 Rayleigh–Ritz Theorems and Eigenvalue Interlac-

$$ing$$
A fact that is used frequently in optimization problems is that the eigenvalues of a symmetric matrix are characterized in terms of what is known as the Rayleigh ratio, defined by
$$R(A)(x) = \frac{x^{\top}Ax}{x^{\top}x} ,x \in \mathbb{R}^{n}, x \neq  0.$$
The following proposition is often used to prove the correctness of various optimization or approximation problems (for example PCA; see Section 23.4). It is also used to prove Proposition 17.25, which is used to justify the correctness of a method for graph-drawing (see Chapter $21)$.

> **Proposition 17.23.** (Rayleigh–Ritz) If $A$ is a symmetric $n \times  n$ matrix with eigenvalues $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$  and if $(u_{1}, \dots  , u_{n})$ is any orthonormal basis of eigenvectors of $A$, where $u_{i}$ is a unit eigenvector associated with $\lambda_{i}$ , then
$$maxx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{n}$$
(with the maximum attained for $x = u_{n})$, and
$$x\neq 0,x\in {umax,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{n-k}$$
$$n-k+1n$$

<!-- PAGE 646 -->
(with the maximum attained for $x = u_{n-k})$, where $1 \le k \le n$ - $1$. Equivalently, if $V_{k}$ is the subspace spanned by $(u_{1}, \dots  , u_{k})$, then
$$\lambda_{k}  =x\neq 0max,x\in V \frac{x^{\top}Ax}{x^{\top}x} ,k = 1, \dots  , n.$$
$$k$$

*Proof.* First observe that
$$maxx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = maxx {x^{\top}Ax | x^{\top}x = 1},$$
and similarly,
$$x\neq 0,x\in {umax,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = maxxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1).$$
$$n-k+1n$$
Since $A$ is a symmetric matrix, its eigenvalues are real and it can be diagonalized with respect to an orthonormal basis of eigenvectors, so let $(u_{1}, \dots  , u_{n})$ be such a basis. If we write
$$x = \sum_{i=1}^{n}  x_{i}u_{i},$$
a simple computation shows that
$$x^{\top}Ax = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} .$$
$$If x^{\top}x = 1, then \sum_{i}  n=1 x_{i}^{2} = 1, and since we assumed that \lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n} , we get$$
$$x^{\top}Ax = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} \le \lambda_{n} \begin{pmatrix} x_{i}^{2} \end{pmatrix} \sum_{i=1}^{n}  = \lambda_{n} .$$
Thus,
$$\maxx^{\top}Ax | x^{\top}x = 1\le \lambda_{n} ,$$
$$x$$
and since this maximum is achieved for $e_{n} = (0, 0, \dots  , 1)$, we conclude that
$$\maxx^{\top}Ax | x^{\top}x = 1= \lambda_{n} .$$
$$x$$
Next observe that $x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}$ and $x^{\top}x = 1$ iff $x_{n-k+1} = \cdots  = x_{n} = 0$ and
$$\sum_{i}  n=1-k x_{i}^{2} = 1. Consequently, for such an x, we have$$
$$x^{\top}Ax = \sum_{i=1}^{n-k}  \lambda_{i} x_{i}^{2} \le \lambda_{n-k} \begin{pmatrix} x_{i}^{2} \end{pmatrix} \sum_{i=1}^{n-k}  = \lambda_{n-k} .$$

<!-- PAGE 647 -->
Thus,
$$\maxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1)\le \lambda_{n-k} ,$$
$$x$$
and since this maximum is achieved for $e_{n-k} = (0, \dots  , 0, 1, 0, \dots  , 0)$ with a $1$ in position $n$ - $k$, we conclude that
$$\maxx^{\top}Ax | (x \in {u_{n-k+1}, \dots  , u_{n}}^{\perp}) \wedge (x^{\top}x = 1)= \lambda_{n-k} ,$$
$$x$$
as claimed. For our purposes we need the version of Proposition 17.23 applying to min instead of max, whose proof is obtained by a trivial modification of the proof of Proposition 17.23.

> **Proposition 17.24.** (Rayleigh–Ritz) If $A$ is a symmetric $n \times  n$ matrix with eigenvalues $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$  and if $(u_{1}, \dots  , u_{n})$ is any orthonormal basis of eigenvectors of $A$, where $u_{i}$ is a unit eigenvector associated with $\lambda_{i}$ , then
$$minx\neq 0 \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{1}$$
(with the minimum attained for $x = u_{1})$, and
$$x\neq 0,x\in {minu,...,u}\perp \frac{x^{\top}Ax}{x^{\top}x} = \lambda_{i}$$
$$1i-1$$
(with the minimum attained for $x = u_{i})$, where $2 \le i \le n$. Equivalently, if $W_{k} = V_{k-1}^{\perp}$ denotes the subspace spanned by $(u_{k}, \dots  , u_{n})$ (with $V_{0} = (0))$, then
$$\lambda_{k}  =x\neq 0min,x\in W \frac{x^{\top}Ax}{x^{\top}x} =x\neq 0min,x\in V\perp \frac{x^{\top}Ax}{x^{\top}x} ,k = 1, \dots  , n.$$
$$kk -1$$
Propositions 17.23 and 17.24 together are known as the Rayleigh–Ritz theorem. Observe that Proposition 17.24 immediately implies that if $A$ is a symmetric matrix, then $A$ is positive definite iff all its eigenvalues are positive. We also prove this fact in Section 22.1; see Proposition 22.3. As an application of Propositions 17.23 and 17.24, we prove a proposition which allows us to compare the eigenvalues of two symmetric matrices $A$ and $B = R^{\top}AR$, where $R$ is a rectangular matrix satisfying the equation $R^{\top}R =$ I. First we need a definition.

> **Definition 17.5.** Given an $n \times  n$ symmetric matrix $A$ and an $m \times  m$ symmetric $B$, with $m \le n$, if $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$  are the eigenvalues of $A$ and $\mu_{1}  \le \mu_{2}  \le \cdots  \le \mu_{m}$  are the eigenvalues of $B$, then we say that the eigenvalues of $B$ interlace the eigenvalues of $A$ if
$$\lambda_{i}  \le \mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m.$$

<!-- PAGE 648 -->
For example, if $n = 5$ and $m = 3$, we have
$$\lambda_{1}  \le \mu_{1}  \le \lambda_{3}$$
$$\lambda_{2}  \le \mu_{2}  \le \lambda_{4}$$
$$\lambda_{3}  \le \mu_{3}  \le \lambda_{5} .$$

> **Proposition 17.25.** Let $A$ be an $n \times  n$ symmetric matrix, $R$ be an $n \times  m$ matrix such that $R^{\top}R =$ I (with $m \le n)$, and let $B = R^{\top}AR$ (an $m \times  m$ matrix). The following properties hold:
(a) The eigenvalues of $B$ interlace the eigenvalues of $A$.
$(b)$ If $\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$  are the eigenvalues of $A$ and $\mu_{1}  \le \mu_{2}  \le \cdots  \le \mu_{m}$  are the eigenvalues of $B$, and if $\lambda_{i}  = \mu_{i}$ , then there is an eigenvector $v$ of $B$ with eigenvalue $\mu_{i}$  such that Rv is an eigenvector of $A$ with eigenvalue $\lambda_{i}$ .

*Proof.* (a) Let $(u_{1}, \dots  , u_{n})$ be an orthonormal basis of eigenvectors for $A$, and let $(v_{1}, \dots  , v_{m})$ be an orthonormal basis of eigenvectors for $B$. Let $U_{j}$ be the subspace spanned by $(u_{1}, \dots  , u_{j})$ and let $V_{j}$ be the subspace spanned by $(v_{1}, \dots  , v_{j})$. For any $i$, the subspace $V_{i}$ has dimension $i$ and the subspace $R^{\top}U_{i-1}$ has dimension at most $i$ - $1$. Therefore, there is some nonzero vector $v \in V_{i} \cap (R^{\top}U_{i-1})^{\perp}$, and since
$$v^{\top}R^{\top}u_{j} = (Rv)^{\top}u_{j} = 0,j = 1, \dots  , i -1,$$
we have Rv $\in (U_{i-1})^{\perp}$. By Proposition 17.24 and using the fact that $R^{\top}R =$ I, we have
$$\lambda_{i}  \le \frac{(Rv)^{\top}ARv}{(Rv)^{\top}Rv} = \frac{v^{\top}Bv}{v^{\top}v} .$$
On the other hand, by Proposition 17.23,
$$\mu_{i}  =x\neq 0,x\in {maxv,...,v}\perp \frac{x^{\top}Bx}{x^{\top}x} =x\neq 0,xmax\in {v,...,v} \frac{x^{\top}Bx}{x^{\top}x} ,$$
$$i+1n1i$$
so
$$\frac{w^{\top}Bw}{w^{\top}w} \le \mu_{i} for all w \in V_{i},$$
and since $v \in V_{i}$, we have
$$\lambda_{i}  \le \frac{v^{\top}Bv}{v^{\top}v} \le \mu_{i} ,i = 1, \dots  , m.$$
We can apply the same argument to the symmetric matrices $-A$ and $-B$, to conclude that
$$-\lambda_{n-m+i}  \le -\mu_{i} ,$$

<!-- PAGE 649 -->
that is,
$$\mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m.$$
Therefore,
$$\lambda_{i}  \le \mu_{i}  \le \lambda_{n-m+i} ,i = 1, \dots  , m,$$
as desired.
$(b)$ If $\lambda_{i}  = \mu_{i}$ , then
$$\lambda_{i}  = \frac{(Rv)^{\top}ARv}{(Rv)^{\top}Rv} = \frac{v^{\top}Bv}{v^{\top}v} = \mu_{i} ,$$
so $v$ must be an eigenvector for $B$ and Rv must be an eigenvector for $A$, both for the eigenvalue $\lambda_{i}  = \mu_{i}$ . Proposition 17.25 immediately implies the Poincar´e separation theorem. It can be used in situations, such as in quantum mechanics, where one has information about the inner products $u_{i}^{\top} Au_{j}$.

> **Proposition 17.26.** (Poincar´e separation theorem) Let $A$ be a $n\times n$ symmetric (or Hermitian) matrix, let $m$ be some integer with $1 \le m \le n$, and let $(u_{1}, \dots  , u_{m})$ be $m$ orthonormal vectors. Let $B = (u_{i}^{\top} Au_{j})$ (an $m \times  m$ matrix), let $\lambda_{1} (A) \le \dots  \le \lambda_{n} (A)$ be the eigenvalues of $A$ and $\lambda_{1} (B) \le \dots  \le \lambda_{m} (B)$ be the eigenvalues of $B$; then we have
$$\lambda_{k} (A) \le \lambda_{k} (B) \le \lambda_{k+n-m} (A),k = 1, \dots  , m.$$
Observe that Proposition 17.25 implies that
$$\lambda_{1}  + \cdots  + \lambda_{m}  \le \mathrm{tr}(R^{\top}AR) \le \lambda_{n-m+1}  + \cdots  + \lambda_{n} .$$
If $P_{1}$ is the the $n \times  (n$ - $1)$ matrix obtained from the identity matrix by dropping its last column, we have $P_{1}^{\top}  P_{1} =$ I, and the matrix $B = P_{1}^{\top} AP_{1}$ is the matrix obtained from $A$ by deleting its last row and its last column. In this case the interlacing result is
$$\lambda_{1}  \le \mu_{1}  \le \lambda_{2}  \le \mu_{2}  \le \cdots  \le \mu_{n-2}  \le \lambda_{n-1}  \le \mu_{n-1}  \le \lambda_{n} ,$$
a genuine interlacing. We obtain similar results with the matrix $P_{n-m}$ obtained by dropping the last $n -m$ columns of the identity matrix and setting $B = P_{n-m}^{\top} AP_{n-m} (B$ is the $m \times  m$ matrix obtained from $A$ by deleting its last $n$ - $m$ rows and columns). In this case we have the following interlacing inequalities known as Cauchy interlacing theorem:
$$\lambda_{k}  \le \mu_{k}  \le \lambda_{k+n-m} ,k = 1, \dots  , m.(*)$$
