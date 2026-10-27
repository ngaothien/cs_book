# Convergence of Sequences of Vectors and Matrices


<!-- PAGE 389 -->
Chapter $10$ Iterative Methods for Solving Linear Systems

## 10.1 Convergence of Sequences of Vectors and Matri-

$$ces$$
In Chapter $8$ we discussed some of the main methods for solving systems of linear equations. These methods are direct methods, in the sense that they yield exact solutions (assuming infinite precision!). Another class of methods for solving linear systems consists in approximating solutions using iterative methods. The basic idea is this: Given a linear system Ax $= b$ (with $A$ a square invertible matrix in $M_{n}(\mathbb{C}))$, find another matrix $B \in M_{n}(\mathbb{C})$ and a vector $c \in \mathbb{C}^{n}$, such that $1$. The matrix $I$ - $B$ is invertible $2$. The unique solution $x$ of the system Ax $= b$ is identical to the unique solution $u$ of the
$$e e$$
system
$$u = Bu + c,$$
and then starting from any vector $u_{0}$, compute the sequence $(u_{k})$ given by
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N}.$$
Under certain conditions (to be clarified soon), the sequence $(u_{k})$ converges to a limit $u$
$$e$$
which is the unique solution of $u =$ Bu $+ c$, and thus of Ax $= b$. Consequently, it is important to find conditions that ensure the convergence of the above sequences and to have tools to compare the “rate” of convergence of these sequences. Thus, we begin with some general results about the convergence of sequences of vectors and matrices.
$$389$$

<!-- PAGE 390 -->
Let $(E, \|\|)$ be a normed vector space. Recall from Section 9.7 that a sequence $(u_{k})$ of vectors $u_{k} \in E$ converges to a limit $u \in E$, if for every $\epsilon  > 0$, there some natural number $N$ such that
$$\|u_{k} -u\|\le \epsilon ,for all k \ge N.$$
We write
$$u = limu_{k}.$$
$$k\mapsto \infty$$
If $E$ is a finite-dimensional vector space and dim(E) $= n$, we know from Theorem 9.6 that any two norms are equivalent, and if we choose the norm $\|\|_{\infty}$, we see that the convergence of the sequence of vectors $u_{k}$ is equivalent to the convergence of the $n$ sequences of scalars formed by the components of these vectors (over any basis). The same property applies to the finite-dimensional vector space $M_{m,n}(K)$ of $m \times  n$ matrices (with $K = \mathbb{R}$ or $K = \mathbb{C})$, which means that the convergence of a sequence of matrices $A_{k} = (a_{ij}^{(k)}$ ) is equivalent to the convergence of the $m \times  n$ sequences of scalars $(a_{ij}^{(k)}$ ), with $i, j$ fixed $(1 \le i \le m, 1 \le j \le n)$. The first theorem below gives a necessary and sufficient condition for the sequence $(B^{k})$ of powers of a matrix $B$ to converge to the zero matrix. Recall that the spectral radius $\rho (B)$ of a matrix $B$ is the maximum of the moduli $|\lambda_{i}$ | of the eigenvalues of $B$.

> **Theorem 10.1.** For any square matrix $B$, the following conditions are equivalent:
$(1) lim_{k\mapsto \infty} B^{k} = 0$,
$(2) lim_{k\mapsto \infty} B^{k}v = 0$, for all vectors $v$,
$(3) \rho (B) < 1$,
$(4) \|B\| < 1$, for some subordinate matrix norm $\|\|$.

*Proof.* Assume $(1)$ and let $\|\|$ be a vector norm on $E$ and $\|\|$ be the corresponding matrix norm. For every vector $v \in E$, because $\|\|$ is a matrix norm, we have
$$\|B^{k}v\|\le \|B^{k}\|\|v\|,$$
and since $lim_{k\mapsto \infty} B^{k} = 0$ means that $lim_{k\mapsto \infty} \|B^{k}\| = 0$, we conclude that $lim_{k\mapsto \infty} \|B^{k}v\| = 0$, that is, $lim_{k\mapsto \infty} B^{k}v = 0$. This proves that $(1)$ implies $(2)$. Assume $(2)$. If we had $\rho (B) \ge 1$, then there would be some eigenvector $u(\neq  0)$ and some eigenvalue $\lambda$  such that
$$Bu = \lambda u,|\lambda | = \rho (B) \ge 1,$$
but then the sequence $(B^{k}u)$ would not converge to $0$, because $B^{k}u = \lambda^{k} u$ and $|\lambda^{k}$ | $= |\lambda |^{k} \ge 1$. It follows that $(2)$ implies $(3)$. Assume that $(3)$ holds, that is, $\rho (B) < 1$. By Proposition 9.13, we can find $\epsilon  > 0$ small enough that $\rho (B) + \epsilon  < 1$, and a subordinate matrix norm $\|\|$ such that
$$\|B\|\le \rho (B) + \epsilon ,$$

<!-- PAGE 391 -->
which is $(4)$. Finally, assume $(4)$. Because $\|\|$ is a matrix norm,
$$\|B^{k}\|\le \|B\|^{k},$$
and since $\|B\| < 1$, we deduce that $(1)$ holds. The following proposition is needed to study the rate of convergence of iterative methods.

> **Proposition 10.2.** For every square matrix $B \in M_{n}(\mathbb{C})$ and every matrix norm $\|\|$, we have
$$lim\|B^{k}\|^{1/k}= \rho (B).$$
$$k\mapsto \infty$$

*Proof.* We know from Proposition 9.7 that $\rho (B) \le \|B\|$, and since $\rho (B) = (\rho (B^{k}))^{1/k}$, we deduce that
$$\rho (B) \le \|B^{k}\|^{1/k}for all k \ge 1.$$
Now let us prove that for every $\epsilon  > 0$, there is some integer $N(\epsilon$ ) such that
$$\|B^{k}\|^{1/k}\le \rho (B) + \epsilon for all k \ge N(\epsilon ).$$
Together with the fact that
$$\rho (B) \le \|B^{k}\|^{1/k}for all k \ge 1,$$
we deduce that $lim_{k\mapsto \infty} \|B^{k}\|^{1/k}$ exists and that
$$lim\|B^{k}\|^{1/k}= \rho (B).$$
$$k\mapsto \infty$$
For any given $\epsilon  > 0$, let $B_{\epsilon}$ be the matrix
$$B_{\epsilon} = \frac{B}{\rho (B) + \epsilon} .$$
Since $\rho (B_{\epsilon}) < 1$, Theorem 10.1 implies that $lim_{k\mapsto \infty} B_{\epsilon}^{k} = 0$. Consequently, there is some integer $N(\epsilon$ ) such that for all $k \ge N(\epsilon$ ), we have
$$\|\|$$
$$\|B_{\epsilon}^{k} \|= \frac{B^{k}}{(\rho (B) + \epsilon )^{k}} \le 1,$$
which implies that
$$\|B^{k}\|^{1/k}\le \rho (B) + \epsilon ,$$
as claimed. We now apply the above results to the convergence of iterative methods.
