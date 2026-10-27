# The Four Fundamental Subspaces


<!-- PAGE 445 -->

*Proof.* From
$$\langle f^{\top} (\phi ), u\rangle = \langle \phi , f(u)\rangle$$
for all $\phi  \in F^{*}$ and all $u \in E$, we see that if $u \in$ Ker $(f)$, then $\langle f^{\top} (\phi$ ), $u\rangle = \langle \phi , 0\rangle = 0$, which means that $f^{\top} (\phi$ ) $\in$ (Ker $(f))^{0}$, and thus, Im $f^{\top} \subseteq$ (Ker $(f))^{0}$. For the converse, since dim(E) is finite, we have
$$\dim((\mathrm{Ker} (f))^{0}) = \dim(E) -\dim(\mathrm{Ker} (f)) = \dim(\mathrm{Im} f),$$
but we just proved that dim(Im $f^{\top}$ ) $=$ dim(Im $f)$, so we get
$$\dim((\mathrm{Ker} (f))^{0}) = \dim(\mathrm{Im} f^{\top} ),$$
and since Im $f^{\top} \subseteq$ (Ker $(f))^{0}$, we obtain
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0},$$
as claimed.
Remarks: $1$. By the duality theorem, since (Ker $(f))^{00} =$ Ker $(f)$, the above equation yields another proof of the fact that
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0},$$
when $E$ is finite-dimensional. $2$. The equation
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
is actually valid even if when $E$ if infinite-dimensional, but we will not prove this here.

## 11.8 The Four Fundamental Subspaces

Given a linear map $f$ : $E \to F$ (where $E$ and $F$ are finite-dimensional), Proposition 11.11 revealed that the four spaces
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top}$$
play a special role. They are often called the fundamental subspaces associated with $f$. These spaces are related in an intimate manner, since Proposition 11.11 shows that
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}$$
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0},$$

<!-- PAGE 446 -->
and Theorem 11.12 shows that
$$rk(f) = rk(f^{\top} ).$$
It is instructive to translate these relations in terms of matrices (actually, certain linear algebra books make a big deal about this!). If dim(E) $= n$ and dim(F) $= m$, given any basis $(u_{1}, \dots  , u_{n})$ of $E$ and a basis $(v_{1}, \dots  , v_{m})$ of $F$, we know that $f$ is represented by an $m \times  n$ matrix $A = (a_{i j})$, where the jth column of $A$ is equal to $f(u_{j})$ over the basis $(v_{1}, \dots  , v_{m})$. Furthermore, the transpose map $f^{\top}$ is represented by the $n \times  m$ matrix $A^{\top}$ (with respect to the dual bases). Consequently, the four fundamental spaces
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top}$$
correspond to
$$\mathbb{R}^{m}$$
$(1)$ The column space of $A$, denoted by Im $A$ or $\mathcal{R}(A)$; this is the subspace of spanned by the columns of $A$, which corresponds to the image Im $f$ of $f$.
$(2)$ The kernel or nullspace of $A$, denoted by Ker $A$ or $\mathcal{N}(A)$; this is the subspace of $\mathbb{R}^{n}$
$$\mathbb{R}^{n}$$
consisting of all vectors $x \in$ such that Ax $= 0$.
$$\mathbb{R}^{n}$$
$(3)$ The row space of $A$, denoted by Im $A^{\top}$ or $\mathcal{R}(A^{\top})$; this is the subspace of spanned by the rows of $A$, or equivalently, spanned by the columns of $A^{\top}$, which corresponds to the image Im $f^{\top}$ of $f^{\top}$ .
$(4)$ The left kernel or left nullspace of $A$ denoted by Ker $A^{\top}$ or $\mathcal{N}(A^{\top})$; this is the kernel
$$\mathbb{R}^{m} \mathbb{R}^{m}$$
(nullspace) of $A^{\top}$, the subspace of consisting of all vectors $y \in$ such that $A^{\top}y = 0$, or equivalently, $y^{\top}A = 0$. Recall that the dimension $r$ of Im $f$, which is also equal to the dimension of the column space Im $A = \mathcal{R}(A)$, is the rank of $A$ (and $f)$. Then, some our previous results can be reformulated as follows: $1$. The column space $\mathcal{R}(A)$ of $A$ has dimension $r. 2$. The nullspace $\mathcal{N}(A)$ of $A$ has dimension $n$ - $r. 3$. The row space $\mathcal{R}(A^{\top})$ has dimension $r. 4$. The left nullspace $\mathcal{N}(A^{\top})$ of $A$ has dimension $m$ - $r$. The above statements constitute what Strang calls the Fundamental Theorem of Linear Algebra, Part I (see Strang $[176])$. The two statements
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}$$
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}$$
translate to

<!-- PAGE 447 -->
$(1)$ The nullspace of $A$ is the orthogonal of the row space of $A$.
$(2)$ The left nullspace of $A$ is the orthogonal of the column space of $A$. The above statements constitute what Strang calls the Fundamental Theorem of Linear Algebra, Part II (see Strang $[176])$. Since vectors are represented by column vectors and linear forms by row vectors (over a
$$\mathbb{R}^{n}$$
basis in $E$ or $F)$, a vector $x \in$ is orthogonal to a linear form $y$ iff
$$yx = 0.$$
$$\mathbb{R}^{n}$$
Then, a vector $x \in$ is orthogonal to the row space of $A$ iff $x$ is orthogonal to every row of $A$, namely Ax $= 0$, which is equivalent to the fact that $x$ belong to the nullspace of $A$.
$$\mathbb{R}^{m}$$
Similarly, the column vector $y \in$ (representing a linear form over the dual basis of $F^{*})$ belongs to the nullspace of $A^{\top}$ iff $A^{\top}y = 0$, iff $y^{\top}A = 0$, which means that the linear form given by $y^{\top}$ (over the basis in $F)$ is orthogonal to the column space of $A$. Since $(2)$ is equivalent to the fact that the column space of $A$ is equal to the orthogonal of the left nullspace of $A$, we get the following criterion for the solvability of an equation of the form Ax $= b$: The equation Ax $= b$ has a solution iff for all $y \in \mathbb{R}^{m}$, if $A^{\top}y = 0$, then $y^{\top}b = 0$. Indeed, the condition on the right-hand side says that $b$ is orthogonal to the left nullspace of $A$; that is, $b$ belongs to the column space of $A$. This criterion can be cheaper to check that checking directly that $b$ is spanned by the columns of $A$. For example, if we consider the system
$$x_{1} -x_{2} = b_{1}$$
$$x_{2} -x_{3} = b_{2}$$
$$x_{3} -x_{1} = b_{3}$$
which, in matrix form, is written Ax $= b$ as below:
$$\begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} = \begin{pmatrix} b_{1} \\ b_{2} \\ b_{3} \end{pmatrix} ,$$
$$-$$
we see that the rows of the matrix $A$ add up to $0$. In fact, it is easy to convince ourselves that the left nullspace of $A$ is spanned by $y = (1, 1, 1)$, and so the system is solvable iff $y^{\top}b = 0$, namely
$$b_{1} + b_{2} + b_{3} = 0.$$
Note that the above criterion can also be stated negatively as follows:
$$\mathbb{R}^{m}$$
The equation Ax $= b$ has no solution iff there is some $y \in$ such that $A^{\top}y = 0$ and $y^{\top}b \neq  0$.
