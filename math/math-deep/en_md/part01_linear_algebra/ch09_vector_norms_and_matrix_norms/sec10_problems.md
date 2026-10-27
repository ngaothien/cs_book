# Problems


<!-- PAGE 382 -->
$\bullet$  Convergence of sequences of vectors in a normed vector space. $\bullet$  Cauchy sequences, complex normed vector spaces, Banach spaces. $\bullet$  Convergence of series. Absolute convergence. $\bullet$  The matrix exponential. $\bullet$  Skew symmetric matrices and orthogonal matrices.

## 9.10 Problems

Problem 9.1. Let $A$ be the following matrix:
$$A = \begin{pmatrix} \sqrt \\ 1\sqrt & 1/ & \overline{2} \\ 1/ & \overline{2} & 3/2 \end{pmatrix} .$$
Compute the operator 2-norm $\|A\|_{2}$ of $A$.
Problem 9.2. Prove Proposition 9.3, namely that the following inequalities hold for all $\mathbb{R}^{n} \mathbb{C}^{n} x \in$ (or $x \in$ ):
$$\|x\|_{\infty}\le \|x\|_{1} \le n\|x\|_{\infty},$$
$$\sqrt$$
$$\|x\|_{\infty}\le \|x\|_{2} \le \overline{n}\|x\|_{\infty},$$
$$\sqrt$$
$$\|x\|_{2} \le \|x\|_{1} \le \overline{n}\|x\|_{2}.$$
Problem 9.3. For any $p \ge 1$, prove that for all $x \in \mathbb{R}^{n}$,
$$lim\|x\|_{p} = \|x\|_{\infty}.$$
$$p\mapsto \infty$$
Problem 9.4. Let $A$ be an $n \times  n$ matrix which is strictly row diagonally dominant, which means that
$$|a_{i i}| > \sum_{j\neq i}  |a_{i j}|,$$
for $i = 1, \dots  , n$, and let
$$$$
$$\delta  = mini|a_{i i}| - \sum_{j\neq i}  |a_{i j}|.$$
The fact that $A$ is strictly row diagonally dominant is equivalent to the condition $\delta  > 0$.
$(1)$ For any nonzero vector $v$, prove that
$$\|Av\|_{\infty}\ge \|v\|_{\infty}\delta .$$
Use the above to prove that $A$ is invertible.

<!-- PAGE 383 -->
$(2)$ Prove that
$$A_{\infty}^{-1}

$\le \delta^{-1}$ .$$ Hint. Prove that
$$\|\|_{\infty}\|\|_{\infty}$$
$$supv\neq 0 \frac{A^{-1}v}{\|v\|_{\infty}} = supw\neq 0 \frac{w}{\|Aw\|_{\infty}} .$$
Problem 9.5. Let $A$ be any invertible complex $n \times  n$ matrix.
$$\mathbb{C}^{n} \mathbb{C}^{n} \mathbb{R}$$
$(1)$ For any vector norm $\|\|$ on , prove that the function $\|\|_{A}$ : $\to$  given by
$$\|x\|_{A} = \|Ax\|for allx \in \mathbb{C}^{n},$$
is a vector norm.
$(2)$ Prove that the operator norm induced by $\|\|_{A}$, also denoted by $\|\|_{A}$, is given by
$$\|B\|_{A} =

$ABA^{-1}$

for every $n \times  n$ matrixB,$$ where $\|ABA^{-1}\|$ uses the operator norm induced by $\|\|$.
$$\mathbb{C}^{n}$$
Problem 9.6. Give an example of a norm on and of a real matrix $A$ such that
$$\|A\|_{R} < \|A\|,$$
where $\|-\|_{R}$ and $\|-\|$ are the operator norms associated with the vector norm $\|-\|$. Hint. This can already be done for $n = 2$.
Problem 9.7. Let $\|\|$ be any operator norm. Given an invertible $n \times  n$ matrix $A$, if $c = 1/(2 \|A^{-1}\|)$, then for every $n \times  n$ matrix $H$, if $\|H\|\le c$, then $A + H$ is invertible. Furthermore, show that if $\|H\|\le c$, then $\|(A + H)^{-1}\|\le 1/c$.
Problem 9.8. Let $A$ be any $m\times n$ matrix and let $\lambda  \in \mathbb{R}$ be any positive real number $\lambda  > 0$.
$(1)$ Prove that $A^{\top}A + \lambda I_{n}$ and $AA^{\top} + \lambda I_{m}$ are invertible.
$(2)$ Prove that
$$A^{\top}(AA^{\top}+ \lambda I_{m})^{-1}= (A^{\top}A + \lambda I_{n})^{-1}A^{\top}.$$
Remark: The expressions above correspond to the matrix for which the function
$$\Phi (x) = (Ax -b)^{\top}(Ax -b) + \lambda x^{\top}x$$
achieves a minimum. It shows up in machine learning (kernel methods).
Problem 9.9. Let $Z$ be a $q \times  p$ real matrix. Prove that if $I_{p}$ - $Z^{\top}Z$ is positive definite, then the $(p + q) \times  (p + q)$ matrix
$$S = \begin{pmatrix} I_{p} & Z^{\top} \\ Z & I_{q} \end{pmatrix}$$
is symmetric positive definite.

<!-- PAGE 384 -->
Problem 9.10. Prove that for any real or complex square matrix $A$, we have
$$\|A\|_{2}^{2} \le \|A\|_{1} \|A\|_{\infty},$$
where the above norms are operator norms. Hint. Use Proposition 9.11 (among other things, it shows that $\|A\|_{1} =$

$A_{\infty}^{\top}$

).
Problem 9.11. Show that the map $A \mapsto \rho (A)$ (where $\rho (A)$ is the spectral radius of $A)$ is neither a norm nor a matrix norm. In particular, find two $2 \times  2$ matrices $A$ and $B$ such that
$$\rho (A + B) > \rho (A) + \rho (B) = 0and\rho (AB) > \rho (A)\rho (B) = 0.$$
Problem 9.12. Define the map $A \mapsto$ M(A) (defined on $n\times n$ real or complex $n\times n$ matrices) by
$$M(A) = \max{|a_{ij}| | 1 \le i, j \le n}.$$
$(1)$ Prove that
$$M(AB) \le nM(A)M(B)$$
for all $n \times  n$ matrices $A$ and $B$.
$(2)$ Give a counter-example of the inequality
$$M(AB) \le M(A)M(B).$$
$(3)$ Prove that the map $A \mapsto \|A\|_{M}$ given by
$$\|A\|_{M} = nM(A) = n \max{|a_{ij}| | 1 \le i, j \le n}$$
is a matrix norm.
Problem 9.13. Let $S$ be a real symmetric positive definite matrix.
$(1)$ Use the Cholesky factorization to prove that there is some upper-triangular matrix $C$, unique if its diagonal elements are strictly positive, such that $S = C^{\top}C$.
$(2)$ For any $x \in \mathbb{R}^{n}$, define
$$\|x\|_{S} = (x^{\top}Sx)^{1/2}.$$
Prove that
$$\|x\|_{S} = \|Cx\|_{2} ,$$
and that the map $x \mapsto \|x\|_{S}$ is a norm.
Problem 9.14. Let $A$ be a real $2 \times  2$ matrix
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} \\ a_{2 1} & a_{2 2} \end{pmatrix} .$$

<!-- PAGE 385 -->
$(1)$ Prove that the squares of the singular values $\sigma_{1}  \ge \sigma_{2}$  of $A$ are the roots of the quadratic equation
$$X^{2}-\mathrm{tr}(A^{\top}A)X + | \det(A)|^{2}= 0.$$
$(2)$ If we let
$$\mu (A) = \frac{a_{1 1}^{2}+ a_{1 2}^{2}+ a_{2 1}^{2}+ a_{2 2}^{2}}{2|a_{1 1}a_{2 2} -a_{1 2}a_{2 1}|} ,$$
prove that
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{2}} = \mu (A) + (\mu (A)^{2}-1)^{1/2}.$$
$(3)$ Consider the subset $\mathcal{S}$ of $2 \times  2$ invertible matrices whose entries $a_{i j}$ are integers such that $0 \le a_{ij} \le 100$. Prove that the functions $cond_{2}(A)$ and $\mu (A)$ reach a maximum on the $set\mathcal{S}$ for the same values of $A$. Check that for the matrix
$$A_{m} = \begin{pmatrix} 100 & 99 \\ 99 & 98 \end{pmatrix}$$
we have
$$\mu (A_{m}) = 19, 603det(A_{m}) = -1$$
and
$$cond_{2}(A_{m}) \approx 39, 206.$$
$(4)$ Prove that for all $A \in S$, if | det(A)| $\ge 2$ then $\mu (A) \le 10, 000$. Conclude that the maximum of $\mu (A)$ on $\mathcal{S}$ is achieved for matrices such that det(A) $= \pm 1$. Prove that finding matrices that maximize $\mu$  on $\mathcal{S}$ is equivalent to finding some integers $n_{1}, n_{2}, n_{3}, n_{4}$ such that
$$0 \le n_{4} \le n_{3} \le n_{2} \le n_{1} \le 100$$
$$+ 99_{2} + 99_{2} + 98_{2}$$
$$n_{1}^{2} + n_{2}^{2} + n_{3}^{2} + n_{4}^{2} \ge 100^{2}= 39, 206$$
$$|n_{1}n_{4} -n_{2}n_{3}| = 1.$$
You may use without proof that the fact that the only solution to the above constraints is the multiset
$${100, 99, 99, 98}.$$
$(5)$ Deduce from part $(4)$ that the matrices in $\mathcal{S}$ for which $\mu$  has a maximum value are
$$A_{m} = \begin{pmatrix} 100 & 99 \\ 99 & 98 \end{pmatrix} \begin{pmatrix} 98 & 99 \\ 99 & 100 \end{pmatrix} \begin{pmatrix} 99 & 100 \\ 98 & 99 \end{pmatrix} \begin{pmatrix} 99 \\ 98 \\ 100 & 99 \end{pmatrix}$$
and check that $\mu$  has the same value for these matrices. Conclude that
$$\max cond_{2}(A) = cond_{2}(A_{m}).$$
$$A\in S$$

<!-- PAGE 386 -->
$(6)$ Solve the system
$$\begin{pmatrix} 100 & 99 \\ 99 & 98 \\ by \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} 199 \\ 197 \end{pmatrix} .$$
Perturb the right-hand side $b$
$$\Delta b = \begin{pmatrix} -0.0097 \\ 0.0106 \end{pmatrix}$$
and solve the new system
$$A_{m}y = b + \Delta b$$
where $y = (y_{1}, y_{2})$. Check that
$$\Delta x = y -x = \begin{pmatrix} 2 \\ -2.0203 \end{pmatrix} .$$
Compute $\|x\|_{2}, \|\Delta x\|_{2}, \|b\|_{2}, \|\Delta b\|_{2}$, and estimate
$$c = \| \frac{\Delta x}{\|x\|_{2}} \|_{2} \begin{pmatrix} \|\Delta b \\ \|b\|_{2} \end{pmatrix} \|_{2}^{-1}.$$
Check that
$$c \approx cond_{2}(A_{m}) \approx 39, 206.$$
Problem 9.15. Consider a real $2 \times  2$ matrix with zero trace of the form
$$A = \begin{pmatrix} a & b \\ c & -a \end{pmatrix} .$$
$(1)$ Prove that
$$A^{2}= (a^{2}+ bc)I_{2} = -\det(A)I_{2}.$$
If $a^{2} +$ bc $= 0$, prove that
$$e^{A}= I_{2} + A.$$
$(2)$ If $a^{2} +$ bc $< 0$, let $\omega  > 0$ be such that $\omega^{2} = (a^{2} +$ bc). Prove that
$$e^{A} = \cos \omega  I_{2} + \frac{-\sin \omega}{\omega} A.$$
$(3)$ If $a^{2} +$ bc $> 0$, let $\omega  > 0$ be such that $\omega^{2} = a^{2} +$ bc. Prove that
$$e^{A} = cosh \omega  I_{2} + \frac{sinh \omega}{\omega} A.$$
$(3)$ Prove that in all cases
$$\det \begin{pmatrix} e^{A} \end{pmatrix} = 1andtr(A) \ge -2.$$
$(4)$ Prove that there exist some real $2 \times  2$ matrix $B$ with det(B) $= 1$ such that there is no real $2 \times  2$ matrix $A$ with zero trace such that $e^{A} = B$.

<!-- PAGE 387 -->
Problem 9.16. Recall that the Hilbert matrix is given by
$$H_{ij}^{(n)}= \begin{pmatrix} 1 \\ i + j -1 \end{pmatrix} .$$
$(1)$ Prove that
$$\cdots  -$$
$$\det(H^{(n)}) = \frac{(1!2! (n1)!)^{4}}{1!2! \cdots  (2n -1)!} ,$$
thus the reciprocal of an integer. Hint. Use Problem 7.13.
$(2)$ Amazingly, the entries of the inverse of $H^{(n)}$ are integers. Prove that $(H^{(n)})^{-1} = (\alpha_{ij}$ ), with
$$2^{2}$$
$$\alpha_{ij}  = (-1)^{i+j}(i + j -1) \begin{pmatrix} n + i -1 \\ n -j \end{pmatrix} \begin{pmatrix} n + j -1 \\ n -i \end{pmatrix} \begin{pmatrix} i + j - \\ i -1 \end{pmatrix} .$$

<!-- PAGE 388 -->
