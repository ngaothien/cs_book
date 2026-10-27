# Problems


<!-- PAGE 590 -->

## 15.7 Problems

Problem 15.1. Let $A$ be the following $2 \times  2$ matrix
$$A = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix} .$$
$(1)$ Prove that $A$ has the eigenvalue $0$ with multiplicity $2$ and that $A^{2} = 0$.
$(2)$ Let $A$ be any real $2 \times  2$ matrix
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} .$$
Prove that if bc $> 0$, then $A$ has two distinct real eigenvalues. Prove that if a, $b, c, d > 0$, then there is a positive eigenvector $u$ associated with the largest of the two eigenvalues of $A$, which means that if $u = (u_{1}, u_{2})$, then $u_{1} > 0$ and $u_{2} > 0$.
$(3)$ Suppose now that $A$ is any complex $2 \times  2$ matrix as in $(2)$. Prove that if $A$ has the eigenvalue $0$ with multiplicity $2$, then $A^{2} = 0$. Prove that if $A$ is real symmetric, then $A = 0$.
Problem 15.2. Let $A$ be any complex $n \times  n$ matrix. Prove that if $A$ has the eigenvalue $0$ with multiplicity $n$, then $A^{n} = 0$. Give an example of a matrix $A$ such that $A^{n} = 0$ but $A \neq  0$.
Problem 15.3. Let $A$ be a complex $2 \times  2$ matrix, and let $\lambda_{1}$  and $\lambda_{2}$  be the eigenvalues of $A$. Prove that if $\lambda_{1}  \neq  \lambda_{2}$ , then
$$- -$$
$$e^{A}= \frac{\lambda_{1} e^{\lambda2}\lambda_{2} e^{\lambda1}}{\lambda_{1}  -\lambda_{2}} I + \frac{e^{\lambda1}e^{\lambda2}}{\lambda_{1}  -\lambda_{2}} A.$$
Problem 15.4. Let $A$ be the real symmetric $2 \times  2$ matrix
$$A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} .$$
$(1)$ Prove that the eigenvalues of $A$ are real and given by
$$\overline{-}  - \overline{-}$$
$$\lambda_{1}  = \frac{a + c +p\overline{4}\overline{b}^{2}\overline{+ (}\overline{a}\overline{c}\overline{)}^{2}}{2} ,\lambda_{2}  = \frac{a + cp\overline{4}\overline{b}^{2}\overline{+ (}\overline{a}\overline{c}\overline{)}^{2}}{2} .$$
$(2)$ Prove that $A$ has a double eigenvalue $(\lambda_{1}  = \lambda_{2}  = a)$ if and only if $b = 0$ and $a = c$; that is, $A$ is a diagonal matrix.
$(3)$ Prove that the eigenvalues of $A$ are nonnegative iff $b^{2} \le$ ac and $a + c \ge 0$.
$(4)$ Prove that the eigenvalues of $A$ are positive iff $b^{2} <$ ac, a $> 0$ and $c > 0$.

<!-- PAGE 591 -->
Problem 15.5. Find the eigenvalues of the matrices
$$A = \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix} ,B = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix} ,C = A + B = \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} .$$
Check that the eigenvalues of $A + B$ are not equal to the sums of eigenvalues of $A$ plus eigenvalues of $B$.
Problem 15.6. Let $A$ be a real symmetric $n\times n$ matrix and $B$ be a real symmetric positive definite $n \times  n$ matrix. We would like to solve the generalized eigenvalue problem: find $\lambda  \in \mathbb{R}$ and $u \neq  0$ such that
$$Au = \lambda Bu.(*)$$
$(1)$ Use the Cholesky decomposition $B = CC^{\top}$ to show that $\lambda$  and $u$ are solutions of the generalized eigenvalue problem (*) iff $\lambda$  and $v$ are solutions of the (ordinary) eigenvalue problem
$$C^{-1}A(C^{\top})^{-1}v = \lambda v,with v = C^{\top}u.$$
Check that $C^{-1}A(C^{\top})^{-1}$ is symmetric.
$(2)$ Prove that if $Au_{1} = \lambda_{1} Bu_{1}, Au_{2} = \lambda_{2} Bu_{2}$, with $u_{1} \neq  0, u_{2} \neq  0$ and $\lambda_{1}  \neq  \lambda_{2}$ , then $u_{1}^{\top} Bu_{2} = 0$.
$(3)$ Prove that $B^{-1}A$ and $C^{-1}A(C^{\top})^{-1}$ have the same eigenvalues.
Problem 15.7. The sequence of Fibonacci numbers, $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$  , is given by the recurrence
$$F_{n+2} = F_{n+1} + F_{n},$$
with $F_{0} = 0$ and $F_{1} = 1$. In matrix form, we can write
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_{n} \\ F_{n-1} \end{pmatrix} ,n \ge 1, \begin{pmatrix} F_{1} \\ F_{0} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
$(1)$ Show that
$$1^{n}$$
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} = \begin{pmatrix} 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
$(2)$ Prove that the eigenvalues of the matrix
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
are
$$\pm$$
$$\lambda  = \frac{1\sqrt{5}}{2} .$$
The number
$$\phi  = \frac{1 +\sqrt{5}}{2}$$

<!-- PAGE 592 -->
is called the golden ratio. Show that the eigenvalues of $A$ are $\phi$  and $-\phi^{-1}$ .
$(3)$ Prove that $A$ is diagonalized as
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} =\sqrt \frac{1}{\overline{5}} \begin{pmatrix} \phi & -\phi^{-1} \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \phi & 0 \\ 0 & -\phi^{-1} \end{pmatrix} \begin{pmatrix} 1 & \phi^{-1} \\ -1 & \phi \end{pmatrix} .$$
Prove that
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} =\sqrt \frac{1}{\overline{5}} \begin{pmatrix} \phi & -\phi^{-1} \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \phi^{n} \\ -(-\phi^{-1} )^{n} \end{pmatrix} ,$$
and thus
$$" !!#$$
$$- \overline{5}^{n} -\overline{5}^{n}$$
$$F_{n} =\sqrt \frac{1}{\overline{5}} (\phi^{n} (-\phi^{-1} )^{n}) =\sqrt \frac{1}{\overline{5}} \frac{1 +\sqrt}{2} - \frac{1\sqrt}{2} ,n \ge 0.$$
Problem 15.8. Let $A$ be an $n \times  n$ matrix. For any subset I of ${1, \dots  , n}$, let $A_{I,I}$ be the matrix obtained from $A$ by first selecting the columns whose indices belong to I, and then the rows whose indices also belong to I. Prove that
$$\tau_{k} (A) = \sum_{\subseteq {1,...,n}  \det(A_{I,I}).$$
$$I}$$
$$|I|=k$$
Problem 15.9. $(1)$ Consider the matrix
$$A = \begin{pmatrix} 0 & 0 & -a_{3} \\ 1 & 0 & -a_{2} \\ 0 & 1 & a_{1} \end{pmatrix} .$$
$$-$$
Prove that the characteristic polynomial $\chi_{A} (z) =$ det(zI - $A)$ of $A$ is given by
$$\chi_{A} (z) = z^{3}+ a_{1}z^{2}+ a_{2}z + a_{3}.$$
$(2)$ Consider the matrix
$$A = \begin{pmatrix} 0 & 0 & 0 & -a_{4} \\ 1 & 0 & 0 & -a_{3} \\ 0 & 1 & 0 & -a_{2} \\ 0 & 0 & 1 & a_{1} \end{pmatrix} .$$
$$-$$
Prove that the characteristic polynomial $\chi_{A} (z) =$ det(zI - $A)$ of $A$ is given by
$$\chi_{A} (z) = z^{4}+ a_{1}z^{3}+ a_{2}z^{2}+ a_{3}z + a_{4}.$$

<!-- PAGE 593 -->
$(3)$ Consider the $n \times  n$ matrix (called a companion matrix)
$$A = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{n} \\ 1 & 0 & 0 & \cdots & 0 & -a_{n-1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{n-2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{2} \\ 0 & 0 & 0 & 1 & a_{1} \end{pmatrix} .$$
$$\cdots -$$
Prove that the characteristic polynomial $\chi_{A} (z) =$ det(zI - $A)$ of $A$ is given by
$$\chi_{A} (z) = z^{n}+ a_{1}z^{n-1}+ a_{2}z^{n-2}+ \cdots  + a_{n-1}z + a_{n}.$$
Hint. Use induction. Explain why finding the roots of a polynomial (with real or complex coefficients) and finding the eigenvalues of a (real or complex) matrix are equivalent problems, in the sense that if we have a method for solving one of these problems, then we have a method to solve the other.
Problem 15.10. Let $A$ be a complex $n \times  n$ matrix. Prove that if $A$ is invertible and if the eigenvalues of $A$ are $(\lambda_{1} , \dots  , \lambda_{n}$ ), then the eigenvalues of $A^{-1}$ are $(\lambda_{1}^{-1}  , \dots  , \lambda_{n}^{-1}$  ). Prove that if $u$ is an eigenvector of $A$ for $\lambda_{i}$ , then $u$ is an eigenvector of $A^{-1}$ for $\lambda_{i}^{-1}$  .
Problem 15.11. Prove that every complex matrix is the limit of a sequence of diagonalizable matrices that have distinct eigenvalues.
Problem 15.12. Consider the following tridiagonal $n \times  n$ matrices
$$A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ \ddots & \ddots & \ddots \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} ,S = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ \ddots & \ddots & \ddots \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} .$$
Observe that $A =$ 2I - $S$ and show that the eigenvalues of $A$ are $\lambda_{k}  = 2$ - $\mu_{k}$ , where the $\mu_{k}$ are the eigenvalues of $S$.
$(2)$ Using Problem 10.6, prove that the eigenvalues of the matrix $A$ are given by
$$\lambda_{k}  = 4 \sin^{2} \begin{pmatrix} k\pi \\ 2(n + 1) \end{pmatrix} ,k = 1, \dots  , n.$$
Show that $A$ is symmetric positive definite.
$(3)$ Find the condition number of $A$ with respect to the 2-norm.
$(4)$ Show that an eigenvector $(y_{1}^{(k)} , \dots  , y_{n}^{(k)}$ ) associated wih the eigenvalue $\lambda_{k}$  is given by
$$y_{j}^{(k)}= \sin \begin{pmatrix} kj\pi \\ n + 1 \end{pmatrix} ,j = 1, \dots  , n.$$

<!-- PAGE 594 -->
Problem 15.13. Consider the following real tridiagonal symmetric $n \times  n$ matrix
$$A = \begin{pmatrix} c & 1 & 0 \\ 1 & c & 1 \\ \ddots & \ddots & \ddots \\ 1 & c & 1 \\ 0 & 1 & c \end{pmatrix} .$$
$(1)$ Using Problem 10.6, prove that the eigenvalues of the matrix $A$ are given by
$$\lambda_{k}  = c + 2 \cos \begin{pmatrix} k\pi \\ n + 1 \end{pmatrix} ,k = 1, \dots  , n.$$
$(2)$ Find a condition on $c$ so that $A$ is positive definite. It is satisfied by $c = 4$?
Problem 15.14. Let $A$ be an $m \times  n$ matrix and $B$ be an $n \times  m$ matrix (over $\mathbb{C})$.
$(1)$ Prove that
$$\det(I_{m} -AB) = \det(I_{n} -BA).$$
Hint. Consider the matrices
$$X = \begin{pmatrix} I_{m} & A \\ B & I_{n} \end{pmatrix} andY = \begin{pmatrix} I \\ 0 \\ -^{m}B & I_{n} \end{pmatrix} .$$
$(2)$ Prove that
$$\lambda^{n} \det(\lambda I_{m} -AB) = \lambda^{m} \det(\lambda I_{n} -BA).$$
Hint. Consider the matrices
$$X = \begin{pmatrix} \lambda I_{m} & A \\ B & I_{n} \end{pmatrix} andY = \begin{pmatrix} I \\ 0 \\ -^{m}B & \lambda I_{n} \end{pmatrix} .$$
Deduce that $AB$ and BA have the same nonzero eigenvalues with the same multiplicity.
Problem 15.15. The purpose of this problem is to prove that the characteristic polynomial of the matrix
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & \cdots & n \\ 2 & 3 & 4 & 5 & \cdots & n + 1 \\ 3 & 4 & 5 & 6 & \cdots & n + 2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ n & n + 1 & n + 2 & n + 3 & \cdots & 2n -1 \end{pmatrix}$$
is
$$P_{A}(\lambda ) = \lambda^{n-2} \begin{pmatrix} 1 & - \\ \lambda^{2} -n^{2}\lambda  - & n^{2}(n^{2} & 1) \\ 12 \end{pmatrix} .$$

<!-- PAGE 595 -->
$(1)$ Prove that the characteristic polynomial $P_{A}(\lambda$ ) is given by
$$P_{A}(\lambda ) = \lambda^{n-2} P(\lambda ),$$
with
$$\lambda  -1-2-3-4\cdots -n + 3-n + 2-n + 1-n$$
$$-\lambda  -1\lambda  -1-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$$P(\lambda ) =.$$
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
$(2)$ Prove that the sum of the roots $\lambda_{1} , \lambda_{2}$  of the (degree two) polynomial $P(\lambda$ ) is
$$\lambda_{1}  + \lambda_{2}  = n^{2}.$$
The problem is thus to compute the product $\lambda_{1} \lambda_{2}$  of these roots. Prove that
$$\lambda_{1} \lambda_{2}  = P(0).$$
$(3)$ The problem is now to evaluate $d_{n} =$ P(0), where
$$-1-2-3-4\cdots -n + 3-n + 2-n + 1-n$$
$$-1-1-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$$d_{n} =$$
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
I suggest the following strategy: cancel out the first entry in row $1$ and row $2$ by adding a suitable multiple of row $3$ to row $1$ and row $2$, and then subtract row $2$ from row $1$.

<!-- PAGE 596 -->
Do this twice. You will notice that the first two entries on row $1$ and the first two entries on row $2$ change, but the rest of the matrix looks the same, except that the dimension is reduced. This suggests setting up a recurrence involving the entries $u_{k}, v_{k}, x_{k}, y_{k}$ in the determinant
$$u_{k}x_{k}-3-4\cdots -n + k -3-n + k -2-n + k -1-n + k$$
$$v_{k}y_{k}-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$D_{k} =$ ,
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
starting with $k = 0$, with
$$u_{0} = -1,v_{0} = -1,x_{0} = -2,y_{0} = -1,$$
and ending with $k = n$ - $2$, so that
$$u_{n-3}x_{n-3}-3$$
$$u_{n-2}x_{n-2}$$
$$d_{n} = D_{n-2} =v_{n-3}y_{n-3}-1= .$$
$$v_{n-2}y_{n-2}$$
$$1-21$$
Prove that we have the recurrence relations
$$\begin{pmatrix} u_{k+1} \\ v_{k+1} \\ x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 \\ 0 & 2 & 0 & 1 \\ -1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ -2 \\ 1 \end{pmatrix} .$$
$$--$$
These appear to be nasty affine recurrence relations, so we will use the trick to convert this affine map to a linear map.
$(4)$ Consider the linear map given by
$$\begin{pmatrix} u_{k+1} \\ v_{k+1} \\ x_{k+1} \\ y_{k+1} \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \\ 1 \end{pmatrix} ,$$

<!-- PAGE 597 -->
and show that its action on $u_{k}, v_{k}, x_{k}, y_{k}$ is the same as the affine action of Part $(3)$. Use Matlab to find the eigenvalues of the matrix
$$T = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
You will be stunned! Let $N$ be the matrix given by
$$N = T -I.$$
Prove that
$$N^{4}= 0.$$
Use this to prove that
$$+$$
$$T^{k} = I + kN + \frac{1}{2} k(k -1)N^{2} \frac{1}{6} k(k -1)(k -2)N^{3},$$
for all $k \ge 0$.
$(5)$ Prove that
$$k$$
$$\begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \\ 1 \end{pmatrix} = T^{k} \begin{pmatrix} -1 \\ -1 \\ -2 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} -1 \\ -1 \\ -2 \\ -1 \\ 1 \end{pmatrix} ,$$
for $k \ge 0$. Prove that
$$T^{k}  = \begin{pmatrix} k + 1 & -k(k + 1) & k & -k^{2} & 1(k -1)k(2k -7) \\ \overline{6} \\ 0 & k + 1 & 0 & k & -_{2}^{1}(k -1)k \\ -k & k^{2} & 1 -k & (k -1)k & -_{3}^{1}k((k -6)k + 11) \\ 0 & -k & 0 & 1 -k & 1(k -3)k \\ \overline{2} \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
and thus that
$$\begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \end{pmatrix} = \begin{pmatrix} 1(2k^{3} + 3k^{2} -5k -6) \\ \overline{6} \\ -_{2}^{1}(k^{2} + 3k + 2) \\ 1(-k^{3} + k -6) \\ \overline{3} \\ 1(k^{2} + k & 2) \end{pmatrix} ,$$
$$-$$
$$\overline{2}$$

<!-- PAGE 598 -->
and that
$$u_{k}x_{k}$$
$$- -$$
$$v_{k}y_{k} = -1 - \frac{7}{3} k - \frac{23}{12} k^{2} \frac{2}{3} k^{3} \frac{1}{12} k^{4}.$$
As a consequence, prove that amazingly
$$-$$
$$d_{n} = D_{n-2} = - \frac{1}{12} n^{2}(n^{2}1).$$
$(6)$ Prove that the characteristic polynomial of $A$ is indeed
$$P_{A}(\lambda ) = \lambda^{n-2} \begin{pmatrix} 1 & - \\ \lambda^{2} -n^{2}\lambda  - & n^{2}(n^{2} & 1) \\ 12 \end{pmatrix} .$$
Use the above to show that the two nonzero eigenvalues of $A$ are
$$\sqrt!$$
$$\lambda  = \frac{n}{2} n \pm \frac{\sqrt{3}}{3} \overline{4}\overline{n}^{2} \overline{-}\overline{1}.$$
The negative eigenvalue $\lambda_{1}$  can also be expressed as
$$-r$$
$$\lambda_{1}  = n^{2} \frac{(32\sqrt{3)}}{6} 1 - \frac{\overline{1}}{4n^{2}} .$$
Use this expression to explain the following phenomenon: if we add any number greater than or equal to $(2/25)n^{2}$ to every diagonal entry of $A$ we get an invertible matrix. What about $0.077351n^{2}$? Try it!
Problem 15.16. Let $A$ be a symmetric tridiagonal $n \times n$-matrix
$$A = \begin{pmatrix} b_{1} & c_{1} \\ c_{1} & b_{2} & c_{2} \\ c_{2} & b_{3} & c_{3} \\ \ddots & \ddots & \ddots \\ c_{n-2} & b_{n-1} & c_{n-1} \\ c_{n-1} & b_{n} \end{pmatrix} ,$$
where it is assumed that $c_{i} \neq  0$ for all $i, 1 \le i \le n$ - $1$, and let $A_{k}$ be the $k \times$  k-submatrix consisting of the first $k$ rows and columns of $A, 1 \le k \le n$. We define the polynomials $P_{k}(x)$ as follows: $(0 \le k \le n)$.
$$P_{0}(x) = 1,$$
$$P_{1}(x) = b_{1} -x,$$
$$P_{k}(x) = (b_{k} -x)P_{k-1}(x) -c_{k-1}^{2}P_{k-2}(x),$$

<!-- PAGE 599 -->
where $2 \le k \le n$.
$(1)$ Prove the following properties:
$(i) P_{k}(x)$ is the characteristic polynomial of $A_{k}$, where $1 \le k \le n$.
(ii) $lim_{x\to -\infty} P_{k}(x) = +\infty$ , where $1 \le k \le n$.
(iii) If $P_{k}(x) = 0$, then $P_{k-1}(x)P_{k+1}(x) < 0$, where $1 \le k \le n$ - $1$.
(iv) $P_{k}(x)$ has $k$ distinct real roots that separate the $k + 1$ roots of $P_{k+1}(x)$, where $1 \le k \le n$ - $1$.
$(2)$ Given any real number $\mu  > 0$, for every $k, 1 \le k \le n$, define the function $sg_{k}(\mu$ ) as follows:
$$sign of P_{k}(\mu )if P_{k}(\mu ) \neq  0,$$
$$sg_{k}(\mu ) =$$
$$sign of P_{k-1}(\mu )if P_{k}(\mu ) = 0.$$
We encode the sign of a positive number as $+$, and the sign of a negative number as -. Then let E(k, $\mu$ ) be the ordered list
$$E(k, \mu ) = \langle +, sg_{1}(\mu ), sg_{2}(\mu ), \dots  , sg_{k}(\mu )\rangle ,$$
and let N(k, $\mu$ ) be the number changes of sign between consecutive signs in E(k, $\mu$ ). Prove that $sg_{k}(\mu$ ) is well defined and that N(k, $\mu$ ) is the number of roots $\lambda$  of $P_{k}(x)$ such that $\lambda  < \mu$ .
Remark: The above can be used to compute the eigenvalues of a (tridiagonal) symmetric matrix (the method of Givens-Householder).

<!-- PAGE 600 -->
