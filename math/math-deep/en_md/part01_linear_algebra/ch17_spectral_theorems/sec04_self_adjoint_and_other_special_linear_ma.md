# Self-Adjoint and Other Special Linear Maps


<!-- PAGE 636 -->

## 17.4 Self-Adjoint, Skew-Self-Adjoint, and Orthogonal

$$Linear Maps$$
We begin with self-adjoint maps.

> **Theorem 17.14.** Given a Euclidean space $E$ of dimension $n$, for every self-adjoint linear map $f$ : $E \to E$, there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ of eigenvectors of $f$ such that the matrix of $f$ w.r.t. this basis is a diagonal matrix
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
where $\lambda_{i}  \in \mathbb{R}$.

*Proof.* We already proved this; see Theorem 17.8. However, it is instructive to give a more direct method not involving the complexification of $\langle$ -, $-\rangle$ and Proposition 17.5. Since $\mathbb{C}$ is algebraically closed, $f_{C}$ has some eigenvalue $\lambda  + i\mu$ , and let $u +$ iv be some eigenvector of $f_{C}$ for $\lambda +i\mu$ , where $\lambda , \mu  \in \mathbb{R}$ and $u, v \in E$. We saw in the proof of Proposition 17.10 that
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.$$
Since $f = f^{*}$ ,
$$\langle f(u), v\rangle = \langle u, f(v)\rangle$$
for all $u, v \in E$. Applying this to
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v,$$
we get
$$\langle f(u), v\rangle = \langle \lambda u -\mu v, v\rangle = \lambda \langle u, v\rangle -\mu \langle v, v\rangle$$
and
$$\langle u, f(v)\rangle = \langle u, \mu u + \lambda v\rangle = \mu \langle u, u\rangle + \lambda \langle u, v\rangle ,$$
and thus we get
$$\lambda \langle u, v\rangle -\mu \langle v, v\rangle = \mu \langle u, u\rangle + \lambda \langle u, v\rangle ,$$
that is,
$$\mu (\langle u, u\rangle + \langle v, v\rangle ) = 0,$$
which implies $\mu  = 0$, since either $u \neq  0$ or $v \neq  0$. Therefore, $\lambda$  is a real eigenvalue of $f$. Now going back to the proof of Theorem 17.12, only the case where $\mu  = 0$ applies, and the induction shows that all the blocks are one-dimensional.

<!-- PAGE 637 -->
Theorem 17.14 implies that if $\lambda_{1} , \dots  , \lambda_{p}$  are the distinct real eigenvalues of $f$, and $E_{i}$ is the eigenspace associated with $\lambda_{i}$ , then
$$E = E_{1} \oplus \cdots  \oplus E_{p},$$
where $E_{i}$ and $E_{j}$ are orthogonal for all $i \neq  j$.
Remark: Another way to prove that a self-adjoint map has a real eigenvalue is to use a little bit of calculus. We learned such a proof from Herman Gluck. The idea is to consider the real-valued function $\Phi$ : $E \to \mathbb{R}$ defined such that
$$\Phi (u) = \langle f(u), u\rangle$$
for every $u \in E$. This function is $C^{\infty}$, and if we represent $f$ by a matrix $A$ over some orthonormal basis, it is easy to compute the gradient vector
$$\nabla \Phi (X) = \begin{pmatrix} \partial \\ \Phi & \partial \Phi \\ (X), \dots  , & (X) \\ \partial x_{1} & \partial x_{n} \end{pmatrix}$$
of $\Phi$  at $X$. Indeed, we find that
$$\nabla \Phi (X) = (A + A^{\top})X,$$
where $X$ is a column vector of size $n$. But since $f$ is self-adjoint, $A = A^{\top}$, and thus
$$\nabla \Phi (X) = 2AX.$$
The next step is to find the maximum of the function $\Phi$  on the sphere
$$\mathbb{R}^{n}$$
$$S^{n-1}= {(x_{1}, \dots  , x_{n}) \in | x_{1}^{2} + \cdots  + x_{n}^{2} = 1}.$$
Since $S^{n-1}$ is compact and $\Phi$  is continuous, and in fact $C^{\infty}, \Phi$  takes a maximum at some $X$ on $S^{n-1}$. But then it is well known that at an extremum $X$ of $\Phi$  we must have
$$d\Phi_{X} (Y ) = \langle \nabla \Phi (X), Y \rangle = 0$$
for all tangent vectors $Y$ to $S^{n-1}$ at $X$, and so $\nabla \Phi (X)$ is orthogonal to the tangent plane at $X$, which means that
$$\nabla \Phi (X) = \lambda X$$
for some $\lambda  \in \mathbb{R}$. Since $\nabla \Phi (X) =$ 2AX, we get
$$2AX = \lambda X,$$
and thus $\lambda /2$ is a real eigenvalue of $A$ (i.e., of $f)$. Next we consider skew-self-adjoint maps.

<!-- PAGE 638 -->

> **Theorem 17.15.** Given a Euclidean space $E$ of dimension $n$, for every skew-self-adjoint linear map $f$ : $E \to E$ there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ such that the matrix of $f$ w.r.t. this basis is a block diagonal matrix of the form
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
such that each block $A_{j}$ is either $0$ or a two-dimensional matrix of the form
$$A_{j} = \begin{pmatrix} 0 \\ -\mu_{j} \\ \mu_{j} & 0 \end{pmatrix} ,$$
where $\mu_{j}  \in \mathbb{R}$, with $\mu_{j}  > 0$. In particular, the eigenvalues of $f_{C}$ are pure imaginary of the form $\pm i\mu_{j}$  or $0$.

*Proof.* The case where $n = 1$ is trivial. As in the proof of Theorem 17.12, $f_{C}$ has some eigenvalue $z = \lambda  + i\mu$ , where $\lambda , \mu  \in \mathbb{R}$. We claim that $\lambda  = 0$. First we show that
$$\langle f(w), w\rangle = 0$$
for all $w \in E$. Indeed, since $f = -f^{*}$ , we get
$$\langle f(w), w\rangle = \langle w, f^{*} (w)\rangle = \langle w, -f(w)\rangle = -\langle w, f(w)\rangle = -\langle f(w), w\rangle ,$$
since $\langle$ -, $-\rangle$ is symmetric. This implies that
$$\langle f(w), w\rangle = 0.$$
Applying this to $u$ and $v$ and using the fact that
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v,$$
we get
$$0 = \langle f(u), u\rangle = \langle \lambda u -\mu v, u\rangle = \lambda \langle u, u\rangle -\mu \langle u, v\rangle$$
and
$$0 = \langle f(v), v\rangle = \langle \mu u + \lambda v, v\rangle = \mu \langle u, v\rangle + \lambda \langle v, v\rangle ,$$
from which, by addition, we get
$$\lambda (\langle v, v\rangle + \langle v, v\rangle ) = 0.$$
Since $u \neq  0$ or $v \neq  0$, we have $\lambda  = 0$. Then going back to the proof of Theorem 17.12, unless $\mu  = 0$, the case where $u$ and $v$ are orthogonal and span a subspace of dimension $2$ applies, and the induction shows that all the blocks are two-dimensional or reduced to $0$.

<!-- PAGE 639 -->
Remark: One will note that if $f$ is skew-self-adjoint, then $if_{C}$ is self-adjoint w.r.t. $\langle$ -, $-\rangle_{C}$ . By Proposition 17.5, the map $if_{C}$ has real eigenvalues, which implies that the eigenvalues of $f_{C}$ are pure imaginary or $0$. Finally we consider orthogonal linear maps.

> **Theorem 17.16.** Given a Euclidean space $E$ of dimension $n$, for every orthogonal linear map $f$ : $E \to E$ there is an orthonormal basis $(e_{1}, \dots  , e_{n})$ such that the matrix of $f$ w.r.t. this basis is a block diagonal matrix of the form
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
such that each block $A_{j}$ is either $1, -1$, or a two-dimensional matrix of the form
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
where $0 < \theta_{j}  < \pi$ . In particular, the eigenvalues of $f_{C}$ are of the form cos $\theta_{j}  \pm  i$ sin $\theta_{j} , 1$, or $-1$.

*Proof.* The case where $n = 1$ is trivial. It is immediately verified that $f \circ f^{*} = f^{*} \circ f =$ id implies that $f_{C} \circ f_{C}^{*}  = f_{C}^{*} \circ f_{C} =$ id, so the map $f_{C}$ is unitary. By Proposition 17.7, the eigenvalues of $f_{C}$ have absolute value $1$. As a consequence, the eigenvalues of $f_{C}$ are of the form cos $\theta  \pm  i$ sin $\theta , 1$, or $-1$. The theorem then follows immediately from Theorem 17.12, where the condition $\mu  > 0$ implies that sin $\theta_{j}  > 0$, and thus, $0 < \theta_{j}  < \pi$ . It is obvious that we can reorder the orthonormal basis of eigenvectors given by Theorem 17.16, so that the matrix of $f$ w.r.t. this basis is a block diagonal matrix of the form
$$\begin{pmatrix} A_{1} & \dots \\ \vdots & \ddots & \vdots & \vdots \\ \dots & A_{r} \\ -I_{q} \\ \dots & I_{p} \end{pmatrix}$$
where each block $A_{j}$ is a two-dimensional rotation matrix $A_{j} \neq  \pm I_{2}$ of the form
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
with $0 < \theta_{j}  < \pi$ .

<!-- PAGE 640 -->
The linear map $f$ has an eigenspace E(1, $f) =$ Ker $(f$ - id) of dimension $p$ for the eigenvalue $1$, and an eigenspace E(-1, $f) =$ Ker $(f +$ id) of dimension $q$ for the eigenvalue $-1$. If det(f) $= +1 (f$ is a rotation), the dimension $q$ of E(-1, $f)$ must be even, and the entries in $-I_{q}$ can be paired to form two-dimensional blocks, if we wish. In this case, every rotation in SO(n) has a matrix of the form
$$\begin{pmatrix} A_{1} & \dots \\ \vdots & \ddots & \vdots \\ \dots & A_{m} \\ \dots & I_{n-2m} \end{pmatrix}$$
where the first $m$ blocks $A_{j}$ are of the form
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
with $0 < \theta_{j}  \le \pi$ . Theorem 17.16 can be used to prove a version of the Cartan–Dieudonn´e theorem.

> **Theorem 17.17.** Let $E$ be a Euclidean space of dimension $n \ge 2$. For every isometry $f \in$ O(E), if $p =$ dim(E(1, $f)) =$ dim(Ker $(f$ - id)), then $f$ is the composition of $n$ - $p$ reflections, and $n$ - $p$ is minimal.

*Proof.* From Theorem 17.16 there are $r$ subspaces $F_{1}, \dots  , F_{r}$, each of dimension $2$, such that
$$E = E(1, f) \oplus E(-1, f) \oplus F_{1} \oplus \cdots  \oplus F_{r},$$
and all the summands are pairwise orthogonal. Furthermore, the restriction $r_{i}$ of $f$ to each $F_{i}$ is a rotation $r_{i} \neq  \pm$ id. Each 2D rotation $r_{i}$ can be written as the composition $r_{i} = s_{i}' \circ s_{i}$ of two reflections $s_{i}$ and $s_{i}'$ about lines in $F_{i}$ (forming an angle $\theta_{i} /2)$. We can extend $s_{i}$ and $s_{i}'$ to hyperplane reflections in $E$ by making them the identity on $F_{i}^{\perp}$ . Then
$$s_{r}' \circ s_{r} \circ \cdots  \circ s_{1}' \circ s_{1}$$
agrees with $f$ on $F_{1} \oplus \cdots  \oplus F_{r}$ and is the identity on E(1, $f) \oplus$ E(-1, $f)$. If E(-1, $f)$ has an orthonormal basis of eigenvectors $(v_{1}, \dots  , v_{q})$, letting $s_{j}''$ be the reflection about the hyperplane $(v_{j})^{\perp}$, it is clear that
$$s_{q}'' \circ \cdots  \circ s_{1}''$$
agrees with $f$ on E(-1, $f)$ and is the identity on E(1, $f) \oplus F_{1} \oplus \cdots  \oplus F_{r}$. But then
$$f = s_{q}'' \circ \cdots  \circ s_{1}'' \circ s_{r}' \circ s_{r} \circ \cdots  \circ s_{1}' \circ s_{1},$$
the composition of 2r $+ q = n$ - $p$ reflections.

<!-- PAGE 641 -->
If
$$f = s_{t} \circ \cdots  \circ s_{1},$$
for $t$ reflections $s_{i}$, it is clear that
$$F = \bigcap_{i=1}^{t}  E(1, s_{i}) \subseteq E(1, f),$$
where E(1, $s_{i})$ is the hyperplane defining the reflection $s_{i}$. By the Grassmann relation, if we intersect $t \le n$ hyperplanes, the dimension of their intersection is at least $n$ - $t$. Thus, n-t $\le p$, that is, $t \ge$ n-p, and n-p is the smallest number of reflections composing $f$. As a corollary of Theorem 17.17, we obtain the following fact: If the dimension $n$ of the Euclidean space $E$ is odd, then every rotation $f \in$ SO(E) admits $1$ as an eigenvalue.

*Proof.* The characteristic polynomial det(XI - $f)$ of $f$ has odd degree $n$ and has real coefficients, so it must have some real root $\lambda$ . Since $f$ is an isometry, its $n$ eigenvalues are of the form, $+1, -1$, and $e^{\pm i\theta}$, with $0 < \theta  < \pi$ , so $\lambda  = \pm 1$. Now the eigenvalues $e^{\pm i\theta}$ appear in conjugate pairs, and since $n$ is odd, the number of real eigenvalues of $f$ is odd. This implies that $+1$ is an eigenvalue of $f$, since otherwise $-1$ would be the only real eigenvalue of $f$, and since its multiplicity is odd, we would have det(f) $= -1$, contradicting the fact that $f$ is a rotation. When $n = 3$, we obtain the result due to Euler which says that every 3D rotation $R$ has an invariant axis $D$, and that restricted to the plane orthogonal to $D$, it is a 2D rotation. Furthermore, if (a, $b, c)$ is a unit vector defining the axis $D$ of the rotation $R$ and if the angle of the rotation is $\theta$ , if $B$ is the skew-symmetric matrix
$$B = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} ,$$
$$-$$
then the Rodigues formula (Proposition 12.15) states that
$$R = I + \sin \theta B + (1 -\cos \theta )B^{2}.$$
The theorems of this section and of the previous section can be immediately translated in terms of matrices. The matrix versions of these theorems is often used in applications so we briefly present them in the section.
