# Problems


<!-- PAGE 522 -->

## 13.3 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Symmetry (or reflection) with respect to $F$ and parallel to $G. \bullet$  Orthogonal symmetry (or reflection) with respect to $F$ and parallel to $G$; reflections, flips. $\bullet$  Hyperplane reflections and Householder matrices. $\bullet  A$ key fact about reflections (Proposition 13.2). $\bullet$  QR-decomposition in terms of Householder transformations (Theorem 13.4).

## 13.4 Problems

Problem 13.1. $(1)$ Given a unit vector (-sin $\theta$ , cos $\theta$ ), prove that the Householder matrix determined by the vector (-sin $\theta$ , cos $\theta$ ) is
$$\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix} .$$
Give a geometric interpretation (i.e., why the choice (-sin $\theta$ , cos $\theta$ )?).
$(2)$ Given any matrix
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Prove that there is a Householder matrix $H$ such that $AH$ is lower triangular, i.e.,
$$AH = \begin{pmatrix} a' & 0 \\ c' & d' \end{pmatrix}$$
$$\mathbb{R}$$
for some a', c', d' $\in$ .
Problem 13.2. Given a Euclidean space $E$ of dimension $n$, if $h$ is a reflection about some hyperplane orthogonal to a nonzero vector $u$ and $f$ is any isometry, prove that $f \circ h \circ f^{-1}$ is the reflection about the hyperplane orthogonal to f(u).
Problem 13.3. $(1)$ Given a matrix
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
prove that there are Householder matrices $G, H$ such that
$$GAH = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = D,$$

<!-- PAGE 523 -->
where $D$ is a diagonal matrix, iff the following equations hold:
$$(b + c) \cos(\theta  + \phi ) = (a -d) \sin(\theta  + \phi ),$$
$$(c -b) \cos(\theta  -\phi ) = (a + d) \sin(\theta  -\phi ).$$
$(2)$ Discuss the solvability of the system. Consider the following cases: Case $1: a$ - $d = a + d = 0$. Case 2a: $a$ - $d = b + c = 0, a + d \neq  0$. Case 2b: $a$ - $d = 0, b + c \neq  0, a + d \neq  0$. Case 3a: $a + d = c$ - $b = 0, a$ - $d \neq  0$. Case 3b: $a + d = 0, c$ - $b \neq  0, a$ - $d \neq  0$. Case $4: a + d \neq  0, a$ - $d \neq  0$. Show that the solution in this case is
$$$$
$$\theta  = \frac{1}{2} arctan \begin{pmatrix} b \\ + c \\ ba -d \\ + c \end{pmatrix} + arctan \begin{pmatrix} c \\ -b \\ ca + d \\ b \end{pmatrix} ,$$
$$$$
$$\phi  = \frac{1}{2} arctan \begin{pmatrix} a -d \end{pmatrix} -arctan \begin{pmatrix} - \\ a + d \end{pmatrix} .$$
If $b = 0$, show that the discussion is simpler: basically, consider $c = 0$ or $c \neq  0$.
$(3)$ Expressing everything in terms of $u =$ cot $\theta$  and $v =$ cot $\phi$ , show that the equations in $(2)$ become
$$(b + c)(uv -1) = (u + v)(a -d),$$
$$(c -b)(uv + 1) = (-u + v)(a + d).$$
Problem 13.4. Let $A$ be an $n \times  n$ real invertible matrix.
$(1)$ Prove that $A^{\top}A$ is symmetric positive definite.
$(2)$ Use the Cholesky factorization $A^{\top}A = R^{\top}R$ with $R$ upper triangular with positive diagonal entries to prove that $Q = AR^{-1}$ is orthogonal, so that $A = QR$ is the QR-factorization of $A$.
Problem 13.5. Modify the function houseqr so that it applies to an $m \times  n$ matrix with $m \ge n$, to produce an $m \times  n$ upper-triangular matrix whose last $m$ - $n$ rows are zeros.
Problem 13.6. The purpose of this problem is to prove that given any self-adjoint linear map $f$ : $E \to E$ (i.e., such that $f^{*} = f)$, where $E$ is a Euclidean space of dimension $n \ge 3$, given an orthonormal basis $(e_{1}, \dots  , e_{n})$, there are $n$ - $2$ isometries $h_{i}$, hyperplane reflections or the identity, such that the matrix of
$$h_{n-2} \circ \cdots  \circ h_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{n-2}$$

<!-- PAGE 524 -->
is a symmetric tridiagonal matrix.
$(1)$ Prove that for any isometry $f$ : $E \to E$, we have $f = f^{*} = f^{-1}$ iff $f \circ f =$ id. Prove that if $f$ and $h$ are self-adjoint linear maps $(f^{*} = f$ and $h^{*} = h)$, then $h \circ f \circ h$ is a self-adjoint linear map.
$(2)$ Let $V_{k}$ be the subspace spanned by $(e_{k+1}, \dots  , e_{n})$. Proceed by induction. For the base case, proceed as follows. Let
$$f(e_{1}) = a_{1}^{0}e_{1} + \cdots  + a_{n}^{0}e_{n},$$
and let
$$r_{1,2} =

$a_{2}^{0}e_{2} + \cdots  + a_{n}^{0}e_{n}$

.$$ Find an isometry $h_{1}$ (reflection or id) such that
$$h_{1}(f(e_{1}) -a_{1}^{0}e_{1}) = r_{1,2} e_{2}.$$
Observe that
$$w_{1} = r_{1,2} e_{2} + a_{1}^{0}e_{1} -f(e_{1}) \in V_{1},$$
and prove that $h_{1}(e_{1}) = e_{1}$, so that
$$h_{1} \circ f \circ h_{1}(e_{1}) = a_{1}^{0}e_{1} + r_{1,2} e_{2}.$$
Let $f_{1} = h_{1} \circ f \circ h_{1}$. Assuming by induction that
$$f_{k} = h_{k} \circ \cdots  \circ h_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{k}$$
has a tridiagonal matrix up to the kth row and column, $1 \le k \le n$ - $3$, let
$$f_{k}(e_{k+1}) = a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} + \cdots  + a_{n}^{k}e_{n},$$
and let
$$r_{k+1, k+2} =

$a_{k+2}^{k}e_{k+2} + \cdots  + a_{n}^{k}e_{n}$

.$$ Find an isometry $h_{k+1}$ (reflection or id) such that
$$h_{k+1}(f_{k}(e_{k+1}) -a_{k}^{k}e_{k} -a_{k+1}^{k}e_{k+1}) = r_{k+1, k+2} e_{k+2}.$$
Observe that
$$w_{k+1} = r_{k+1, k+2} e_{k+2} + a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} -f_{k}(e_{k+1}) \in V_{k+1},$$
and prove that $h_{k+1}(e_{k}) = e_{k}$ and $h_{k+1}(e_{k+1}) = e_{k+1}$, so that
$$h_{k+1} \circ f_{k} \circ h_{k+1}(e_{k+1}) = a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} + r_{k+1, k+2} e_{k+2}.$$

<!-- PAGE 525 -->
Let $f_{k+1} = h_{k+1} \circ f_{k} \circ h_{k+1}$, and finish the proof.
$(3)$ Prove that given any symmetric $n\times n$-matrix $A$, there are n-2 matrices $H_{1}, \dots  , H_{n-2}$, Householder matrices or the identity, such that
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
is a symmetric tridiagonal matrix.
$(4)$ Write a computer program implementing the above method.
Problem 13.7. Recall from Problem 6.6 that an $n \times  n$ matrix $H$ is upper Hessenberg if $h_{jk} = 0$ for all $(j, k)$ such that $j$ - $k \ge 0$. Adapt the proof of Problem 13.6 to prove that given any $n \times n$-matrix $A$, there are $n -2 \ge 1$ matrices $H_{1}, \dots  , H_{n-2}$, Householder matrices or the identity, such that
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
is upper Hessenberg.
Problem 13.8. The purpose of this problem is to prove that given any linear map $f$ : $E \to E$, where $E$ is a Euclidean space of dimension $n \ge 2$, given an orthonormal basis $(e_{1}, \dots  , e_{n})$, there are isometries $g_{i}, h_{i}$, hyperplane reflections or the identity, such that the matrix of
$$g_{n} \circ \cdots  \circ g_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{n}$$
is a lower bidiagonal matrix, which means that the nonzero entries (if any) are on the main descending diagonal and on the diagonal below it.
$(1)$ Let $U_{k}'$  be the subspace spanned by $(e_{1}, \dots  , e_{k})$ and $U_{k}''$ be the subspace spanned by $(e_{k+1}, \dots  , e_{n}), 1 \le k \le n$ - $1$. Proceed by induction For the base case, proceed as follows. Let $v_{1} = f^{*} (e_{1})$ and $r_{1,1} = \|v_{1}\|$. Find an isometry $h_{1}$ (reflection or id) such that
$$h_{1}(f^{*} (e_{1})) = r_{1,1}e_{1}.$$
Observe that $h_{1}(f^{*} (e_{1})) \in U_{1}'$ , so that
$$\langle h_{1}(f^{*} (e_{1})), e_{j}\rangle = 0$$
for all $j, 2 \le j \le n$, and conclude that
$$\langle e_{1}, f \circ h_{1}(e_{j})\rangle = 0$$
for all $j, 2 \le j \le n$. Next let
$$u_{1} = f \circ h_{1}(e_{1}) = u_{1}' + u_{1}'',$$
where $u_{1}' \in U_{1}'$ and $u_{1}'' \in U_{1}''$ , and let $r_{2,1} = \|u_{1}''\|$. Find an isometry $g_{1}$ (reflection or id) such that
$$g_{1}(u_{1}'') = r_{2,1}e_{2}.$$

<!-- PAGE 526 -->
Show that $g_{1}(e_{1}) = e_{1}$,
$$g_{1} \circ f \circ h_{1}(e_{1}) = u_{1}' + r_{2,1}e_{2},$$
and that
$$\langle e_{1}, g_{1} \circ f \circ h_{1}(e_{j})\rangle = 0$$
for all $j, 2 \le j \le n$. At the end of this stage, show that $g_{1} \circ f \circ h_{1}$ has a matrix such that all entries on its first row except perhaps the first are zero, and that all entries on the first column, except perhaps the first two, are zero. Assume by induction that some isometries $g_{1}, \dots  , g_{k}$ and $h_{1}, \dots  , h_{k}$ have been found, either reflections or the identity, and such that
$$f_{k} = g_{k} \circ \cdots  \circ g_{1} \circ f \circ h_{1} \cdots  \circ h_{k}$$
has a matrix which is lower bidiagonal up to and including row and column $k$, where $1 \le k \le n$ - $2$. Let
$$v_{k+1} = f_{k}^{*} (e_{k+1}) = v_{k+1}' + v_{k+1}'',$$
where $v_{k+1}' \in U_{k}'$ and $v_{k+1}'' \in U_{k}''$ , and let $r_{k+1, k+1} =$

$v_{k+1}''$

. Find an isometry $h_{k+1}$ (reflection or id) such that
$$h_{k+1}(v_{k+1}'') = r_{k+1, k+1}e_{k+1}.$$
Show that if $h_{k+1}$ is a reflection, then $U_{k}'  \subseteq H_{k+1}$, where $H_{k+1}$ is the hyperplane defining the reflection $h_{k+1}$. Deduce that $h_{k+1}(v_{k+1}') = v_{k+1}'$, and that
$$h_{k+1}(f_{k}^{*} (e_{k+1})) = v_{k+1}' + r_{k+1, k+1}e_{k+1}.$$
Observe that $h_{k+1}(f_{k}^{*} (e_{k+1})) \in U_{k+1}'$, so that
$$\langle h_{k+1}(f_{k}^{*} (e_{k+1})), e_{j}\rangle = 0$$
for all $j, k + 2 \le j \le n$, and thus,
$$\langle e_{k+1}, f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
for all $j, k + 2 \le j \le n$. Next let
$$u_{k+1} = f_{k} \circ h_{k+1}(e_{k+1}) = u_{k+1}' + u_{k+1}'',$$
where $u_{k+1}' \in U_{k+1}'$ and $u_{k+1}'' \in U_{k+1}''$, and let $r_{k+2, k+1} =$

$u_{k+1}''$

. Find an isometry $g_{k+1}$ (reflection or id) such that
$$g_{k+1}(u_{k+1}'') = r_{k+2, k+1}e_{k+2}.$$
Show that if $g_{k+1}$ is a reflection, then $U_{k+1}'  \subseteq G_{k+1}$, where $G_{k+1}$ is the hyperplane defining the reflection $g_{k+1}$. Deduce that $g_{k+1}(e_{i}) = e_{i}$ for all $i, 1 \le i \le k + 1$, and that
$$g_{k+1} \circ f_{k} \circ h_{k+1}(e_{k+1}) = u_{k+1}' + r_{k+2, k+1}e_{k+2}.$$

<!-- PAGE 527 -->
Since by induction hypothesis,
$$\langle e_{i}, f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
for all $i, j, 1 \le i \le k + 1, k + 2 \le j \le n$, and since $g_{k+1}(e_{i}) = e_{i}$ for all $i, 1 \le i \le k + 1$, conclude that
$$\langle e_{i}, g_{k+1} \circ f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
for all $i, j, 1 \le i \le k + 1, k + 2 \le j \le n$. Finish the proof.

<!-- PAGE 528 -->
