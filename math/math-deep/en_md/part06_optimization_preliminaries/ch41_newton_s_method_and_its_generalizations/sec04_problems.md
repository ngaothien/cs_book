# Problems


<!-- PAGE 1534 -->
$$\mathbb{R}^{n}$$
where $\nabla J(x_{k})$ is the gradient of $J$ at $x_{k}$ (here, we identify E' with ). In particular, Newton’s original method picks $A_{k} =$ J'', and the iteration step is of the form
$$x_{k+1} = x_{k} -(\nabla^{2} J(x_{k}))^{-1}\nabla J(x_{k}),k \ge 0,$$
where $\nabla^{2} J(x_{k})$ is the Hessian of $J$ at $x_{k}$.

> **Example 41.3.** Let us apply Newton’s original method to the function $J$ given by J(x) $= 1$  -  - $x^{3}$ 4x. We have J'(x) $= x^{2} 4$ and J''(x) $=$ 2x, so the Newton step is given by $\overline{3}$
$$-$$
$$x_{k+1} = x_{k} - \frac{x_{k}^{2}4}{2x_{k}} = \frac{1}{2} \begin{pmatrix} 4 \\ x_{k} + \\ x_{k} \end{pmatrix} .$$
This is the sequence of Example 41.1 to compute the square root of $4$. Starting with any $x_{0} > 0$ it converges very quickly to $2$. As remarked in Ciarlet $[41]$ (Section 7.5), generalized Newton methods have a very wide range of applicability. For example, various versions of gradient descent methods can be viewed as instances of Newton method. See Section 49.9 for an example. Newton’s method also plays an important role in convex optimization, in particular, interior-point methods. A variant of Newton’s method dealing with equality constraints has been developed. We refer the reader to Boyd and Vandenberghe $[29]$, Chapters $10$ and $11$, for a comprehensive exposition of these topics.

## 41.3 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Newton’s method for functions $f$ : $\mathbb{R} \to \mathbb{R}. \bullet$  Generalized Newton methods. $\bullet$  The Newton-Kantorovich theorem.

## 41.4 Problems

Problem 41.1. If $\alpha  > 0$ and f(x) $= x^{2}$ - $\alpha$ , Newton’s method yields the sequence
$$x_{k+1} = \frac{1}{2} \begin{pmatrix} \alpha \\ x_{k} + \\ x_{k} \end{pmatrix}$$
$$\sqrt$$
to compute the square root $\overline{\alpha}$ of $\alpha$ .

<!-- PAGE 1535 -->
$(1)$ Prove that if $x_{0} > 0$, then $x_{k} > 0$ and
$$\sqrt\sqrt$$
$$x_{k+1} -\overline{\alpha} = \frac{1}{2x_{k}} (x_{k} -\overline{\alpha})^{2}$$
$$x_{k+2} -x_{k+1} = \frac{1}{2x_{k+1}} (\alpha  -x_{k+1}^{2})$$
$$\sqrt$$
for all $k \ge 0$. Deduce that Newton’s method converges to $\overline{\alpha}$ for any $x_{0} > 0$.
$$\sqrt$$
$(2)$ Prove that if $x_{0} < 0$, then Newton’s method converges to - $\overline{\alpha}$.
Problem 41.2. $(1)$ If $\alpha  > 0$ and f(x) $= x^{2}$ - $\alpha$ , show that the conditions of Theorem 41.1 are satisfied by any $\beta  \in (0, 1)$ and any $x_{0}$ such that
$$-$$
$$|x_{0}^{2} -\alpha | \le \frac{4\beta (1\beta )}{(\beta  + 2)^{2}} x_{0}^{2},$$
with
$$r = \frac{\beta}{\beta  + 2} x_{0},M = \frac{\beta  + 2}{4x_{0}} .$$
$(2)$ Prove that the maximum of the function defined on $[0, 1]$ by
$$-$$
$$\beta  \mapsto \frac{4\beta (1\beta )}{(\beta  + 2)^{2}}$$
has a maximum for $\beta  = 2/5$. For this value of $\beta$ , check that $r = (1/6)x_{0}, M = 3/(5x_{0})$, and
$$\frac{6}{7} \alpha  \le x_{0}^{2} \le \frac{6}{5} \alpha .$$
Problem 41.3. Consider generalizing Problem 41.1 to the matrix function $f$ given by f(X) $= X^{2}$ - $C$, where $X$ and $C$ are two real $n \times  n$ matrices with $C$ symmetric positive definite. The first step is to determine for which $A$ does the inverse $df_{A}^{-1}$ exist. Let $g$ be the function given by g(X) $= X^{2}$. From Problem 39.1 we know that the derivative at $A$ of the function $g$ is $dg_{A}(X) = AX + XA$, and obviously $df_{A} = dg_{A}$. Thus we are led to figure out when the linear matrix map $X \mapsto AX + XA$ is invertible. This can be done using the Kronecker product. Given an $m \times  n$ matrix $A = (a_{ij})$ and a $p \times  q$ matrix $B = (b_{ij})$, the Kronecker product (or tensor product) $A \otimes B$ of $A$ and $B$ is the mp $\times$  nq matrix
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$

<!-- PAGE 1536 -->
It can be shown (and you may use these facts without proof) that $\otimes$ is associative and that
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
whenever AC and BD are well defined. Given any $n \times  n$ matrix $X$, let vec(X) be the vector in $\mathbb{R}^{n2}$ obtained by concatenating the rows of $X$.
$(1)$ Prove that $AX = Y$ iff
$$(A \otimes I_{n})vec(X) = vec(Y )$$
and $XA = Y$ iff
$$(I_{n} \otimes A^{\top})vec(X) = vec(Y ).$$
Deduce that $AX + XA = Y$ iff
$$((A \otimes I_{n}) + (I_{n} \otimes A^{\top}))vec(X) = vec(Y ).$$
In the case where $n = 2$ and if we write
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
check that
$$A \otimes I_{2} + I_{2} \otimes A^{\top}= \begin{pmatrix} 2a & c & b & 0 \\ b & a + d & 0 & b \\ c & 0 & a + d & c \\ 0 & c & b & 2d \end{pmatrix} .$$
The problem is to determine when the matrix $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ is invertible.
Remark: The equation $AX + XA = Y$ is a special case of the equation $AX + XB = C$ (sometimes written $AX$ - $XB = C)$, called the Sylvester equation, where $A$ is an $m \times  m$ matrix, $B$ is an $n \times  n$ matrix, and $X, C$ are $m \times  n$ matrices; see Higham $[94]$ (Appendix $B)$.
$(2)$ In the case where $n = 2$, prove that
$$\det(A \otimes I_{2} + I_{2} \otimes A^{\top}) = 4(a + d)^{2}(ad -bc).$$
$(3)$ Let $A$ and $B$ be any two $n\times n$ complex matrices. Use Schur factorizations $A = UT_{1}U^{*}$ and $B = V T_{2}V^{*}$ (where $U$ and $V$ are unitary and $T_{1}, T_{2}$ are upper-triangular) to prove that if $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $A$ and $\mu_{1} , \dots  , \mu_{n}$  are the eigenvalues of $B$, then the scalars $\lambda_{i} \mu_{j}$  are the eigenvalues of $A \otimes B$, for $i, j = 1, \dots  , n$. Hint. Check that $U \otimes V$ is unitary and that $T_{1} \otimes T_{2}$ is upper triangular.

<!-- PAGE 1537 -->
$(4)$ Prove that the eigenvalues of $(A \otimes I_{n}) + (I_{n} \otimes B)$ are the scalars $\lambda_{i}  + \mu_{j}$ , for $i, j = 1, \dots  , n$. Deduce that the eigenvalues of $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ are $\lambda_{i}  + \lambda_{j}$ , for $i, j = 1, \dots  , n$. Thus $(A\otimes I_{n})+(I_{n} \otimes A^{\top})$ is invertible iff $\lambda_{i}  +\lambda_{j}  \neq  0$, for $i, j = 1, \dots  , n$. In particular, prove that if $A$ is symmetric positive definite, then so is $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$. Hint. Use $(3)$.
$(5)$ Prove that if $A$ and $B$ are symmetric and $(A \otimes I_{n}) + (I_{n} \otimes A^{\top})$ is invertible, then the unique solution $X$ of the equation $AX + XA = B$ is symmetric.
$(6)$ Starting with a symmetric positive definite matrix $X_{0}$, the general step of Newton’s method is
$$X_{k+1} = X_{k} -(f_{Xk}' )^{-1}(X_{k}^{2} -C) = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2} -C),$$
and since $g_{Xk}'$ is linear, this is equivalent to
$$X_{k+1} = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2}) + (g_{Xk}')^{-1}(C).$$
But since $X_{k}$ is SPD, $(g_{Xk}')^{-1}(X_{k}^{2})$ is the unique solution of
$$X_{k}Y + Y X_{k} = X_{k}^{2}$$
whose solution is obviously $Y = (1/2)X_{k}$. Therefore the Newton step is
$$X_{k+1} = X_{k} -(g_{Xk}')^{-1}(X_{k}^{2}) + (g_{Xk}')^{-1}(C) = X_{k} - \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C) = \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C),$$
so we have
$$X_{k+1} = \frac{1}{2} X_{k} + (g_{Xk}')^{-1}(C) = (g_{Xk}')^{-1}(X_{k}^{2} + C).$$
Prove that if $X_{k}$ and $C$ are symmetric positive definite, then $(g_{Xk}')^{-1}(C)$ is symmetric positive definite, and if $C$ is symmetric positive semidefinite, then $(g_{Xk}')^{-1}(C)$ is symmetric positive semidefinite. Hint. By $(5)$ the unique solution $Z$ of the equation $X_{k}Z +ZX_{k} = C$ (where $C$ is symmetric) is symmetric so it can be diagonalized as $Z = QDQ^{\top}$ with $Q$ orthogonal and $D$ a real diagonal matrix. Prove that
$$Q^{\top}X_{k}QD + DQ^{\top}X_{k}Q = Q^{\top}CQ,$$
and solve the system using the diagonal elements. Deduce that if $X_{k}$ and $C$ are SPD, then $X_{k+1}$ is SPD. Since $C = P\Sigma P^{\top}$ is SPD, it has an SPD square root (in fact unique) $C^{1/2} = P\Sigma^{1/2} P^{\top}$. Prove that
$$X_{k+1} -C^{1/2}= (g_{Xk}')^{-1}(X_{k} -C^{1/2})^{2}.$$
Prove that
$$(g_{Xk}')_{2}^{-1}

$\ge \frac{1}{2 \|X_{k}\|_{2}}$ .$$

<!-- PAGE 1538 -->
Open problem: Does Theorem 41.1 apply for some suitable $r, M, \beta$ ?
$(7)$ Prove that if $C$ and $X_{0}$ commute, provided that the equation $X_{k}Z + ZX_{k} = C$ has a unique solution for all $k$, then $X_{k}$ and $C$ commute for all $k$ and $Z$ is given by
$$Z = \frac{1}{2} X_{k}^{-1} C = \frac{1}{2} CX_{k}^{-1} .$$
Deduce that
$$X_{k+1} = \frac{1}{2} (X_{k} + X_{k}^{-1} C) = \frac{1}{2} (X_{k} + CX_{k}^{-1} ).$$
This is the matrix analog of the formula given in Problem 41.1(1). Prove that if $C$ and $X_{0}$ have positive eigenvalues and $C$ and $X_{0}$ commute, then $X_{k+1}$ has positive eigenvalues for all $k \ge 0$ and thus the sequence $(X_{k})$ is defined. Hint. Because $X_{k}$ and $C$ commute, $X_{k}^{-1}$ and $C$ commute, and obviously $X_{k}$ and $X_{k}^{-1}$ commute. By Proposition 31.9, $X_{k}, X_{k}^{-1}$ , and $C$ are triangulable in a common basis, so there is some orthogonal matrix $P$ and some upper-triangular matrices $T_{1}, T_{2}$ such that
$$X_{k} = PT_{1}P^{\top} ,X_{k}^{-1}= PT_{1}^{-1}  P^{\top},C = PT_{2}P^{\top} .$$
It follows that
$$X_{k+1} = \frac{1}{2} P(T_{1} + T_{1}^{-1} T_{2})P^{\top}.$$
Also recall that the diagonal entries of an upper-triangular matrix are the eigenvalues of that matrix. We conjecture that if $C$ has positive eigenvalues, then the Newton sequence converges starting with any $X_{0}$ of the form $X_{0} = \mu I_{n}$, with $\mu  > 0$.
$(8)$ Implement the above method in Matlab (there is a command kron(A, $B)$ to form the Kronecker product of $A$ and $B)$. Test your program on diagonalizable and nondiagonalizable matrices, including
$$W = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} ,A_{1} = \begin{pmatrix} 5 & 4 & 1 & 1 \\ 4 & 5 & 1 & 1 \\ 1 & 1 & 4 & 2 \\ 1 & 1 & 2 & 4 \end{pmatrix} ,$$
and
$$A_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 0.01 & 0 & 0 \\ -1 & -1 & 100 & 100 \\ 1 & 1 & 100 & 100 \end{pmatrix} ,A_{3} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,A_{4} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$---$$
What happens with
$$C = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} ,X_{0} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} .$$

<!-- PAGE 1539 -->
The problem of determining when square roots of matrices exist and procedures for finding them are thoroughly investigated in Higham $[94]$ (Chapter $6)$.
Problem 41.4. $(1)$ Show that Newton’s method applied to the function
$$f(x) = \alpha  - \frac{1}{x}$$
with $\alpha  \neq  0$ and $x \in \mathbb{R} -{0}$ yields the sequence $(x_{k})$ with
$$x_{k+1} = x_{k}(2 -\alpha x_{k}),k \ge 0.$$
$(2)$ If we let $r_{k} = 1$ - $\alpha x_{k}$, prove that $r_{k+1} = r_{k}^{2}$ for all $k \ge 0$. Deduce that Newton’s method converges to $1/\alpha$  if $0 < \alpha x_{0} < 2$.
Problem 41.5. $(1)$ Show that Newton’s method applied to the matrix function
$$f(X) = A -X^{-1},$$
with $A$ and $X$ invertible $n \times  n$ matrices and started with any $n \times  n$ matrix $X_{0}$ yields the sequence $(X_{k})$ with
$$X_{k+1} = X_{k}(2I -AX_{k}),k \ge 0.$$
$(2)$ If we let $R_{k} =$ I - $AX_{k}$, prove that
$$R_{k+1} = I -(I -R_{k})(I + R_{k}) = R_{k}^{2}$$
for all $k \ge 0$. Deduce that Newton’s method converges to $A^{-1}$ iff the spectral radius of I - $AX_{0}$ is strictly smaller than $1$, that is, $\rho$ (I - $AX_{0}) < 1$.
$(3)$ Assume that $A$ is symmetric positive definite and let $X_{0} = \mu$ I. Prove that the condition $\rho$ (I - $AX_{0}) < 1$ is equivalent to
$$0 < \mu  < \frac{2}{\rho (A)} .$$
$(4)$ Write a Matlab program implementing Newton’s method specified in $(1)$. Test your program with the $n \times  n$ matrix
$$A_{n} = \begin{pmatrix} 2 & -1 & 0 & \cdots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & -1 & 2 & -1 \\ 0 & \cdots & 0 & -1 & 2 \end{pmatrix} ,$$
and with $X_{0} = \mu I_{n}$, for various values of $n$, including $n = 8, 10, 20$, and various values of $\mu$ such that $0 < \mu  \le 1/2$. Find some $\mu  > 1/2$ causing divergence.

<!-- PAGE 1540 -->
$$\mathbb{R}$$
Problem 41.6. A method for computing the nth root $x^{1/n}$ of a positive real number $x \in$ , with $n \in \mathbb{N}$ a positive integer $n \ge 2$, proceeds as follows: define the sequence $(x_{k})$, where $x_{0}$ is any chosen positive real, and
$$x_{k+1} = \frac{1}{n} \begin{pmatrix} x \\ (n -1)x_{k} + \\ x_{k}^{n-1} \end{pmatrix} ,k \ge 0.$$
$(1)$ Implement the above method in Matlab and test it for various input values of $x, x_{0}$, and of $n \ge 2$, by running successively your program for $m = 2, 3, \dots  , 100$ iterations. Have your program plot the points $(i, x_{i})$ to watch how quickly the sequence converges. Experiment with various choices of $x_{0}$. One of these choices should be $x_{0} = x$. Compare your answers with the result of applying the of Matlab function $x \mapsto x^{1/n}$. In some case, when $x_{0}$ is small, the number of iterations has to be at least $1000$. Exhibit this behavior.
Problem 41.7. Refer to Problem 41.6 for the definition of the sequence $(x_{k})$.
$(1)$ Define the relative error $\epsilon_{k}$  as
$$\epsilon_{k}  = \frac{x_{k}}{x^{1/n}} -1,k \ge 0.$$
Prove that
$$\epsilon_{k+1}  = \frac{x^{(1-1/n)}}{nx_{k}^{n-1}} \begin{pmatrix} (n -1)x_{k}^{n} & nx_{k}^{n-1} \\ - & + 1 \\ x & x^{(1-1/n)} \end{pmatrix} ,$$
and then that
$$\epsilon_{k+1}  = \frac{1}{n(\epsilon_{k}  + 1)^{n-1}} \begin{pmatrix} \epsilon_{k} (\epsilon_{k}  + 1)^{n-2}((n -1)\epsilon_{k}  + (n -2)) + 1 -(\epsilon_{k}  + 1)^{n-2} \end{pmatrix} ,$$
for all $k \ge 0$.
$(2)$ Since
$$\epsilon_{k}  + 1 = \frac{x_{k}}{x^{1/n}} ,$$
and since we assumed $x_{0}, x > 0$, we have $\epsilon_{0}  + 1 > 0$. We would like to prove that
$$\epsilon_{k}  \ge 0,for allk \ge 1.$$
For this consider the variations of the function $f$ given by
$$f(u) = (n -1)u^{n}-nx^{1/n}u^{n-1}+ x,$$
for $u \in \mathbb{R}$. Use the above to prove that f(u) $\ge 0$ for all $u \ge 0$. Conclude that
$$\epsilon_{k}  \ge 0,for allk \ge 1.$$

<!-- PAGE 1541 -->
$(3)$ Prove that if $n = 2$, then
$$0 \le \epsilon_{k+1}  = \frac{\epsilon_{k}^{2}}{2(\epsilon_{k}  + 1)} ,for allk \ge 0,$$
else if $n \ge 3$, then
$$-$$
$$0 \le \epsilon_{k+1}  \le \frac{(n1)}{n} \epsilon_{k} ,for allk \ge 1.$$
Prove that the sequence $(x_{k})$ converges to $x^{1/n}$ for every initial value $x_{0} > 0$.
$(4)$ When $n = 2$, we saw in Problem 41.7(3) that
$$0 \le \epsilon_{k+1}  = \frac{\epsilon_{k}^{2}}{2(\epsilon_{k}  + 1)} ,for allk \ge 0.$$
For $n = 3$, prove that
$$\epsilon_{k+1}  = \frac{2\epsilon_{k}^{2} (3/2 + \epsilon_{k} )}{3(\epsilon_{k}  + 1)^{2}} ,for allk \ge 0,$$
and for $n = 4$, prove that
$$\epsilon_{k+1}  = \frac{3\epsilon_{k}^{2}}{4(\epsilon_{k}  + 1)^{3}} \begin{pmatrix} 2 + (8/3)\epsilon_{k}  + \epsilon_{k}^{2} \end{pmatrix} ,for allk \ge 0.$$
Let $\mu_{3}$  and $\mu_{4}$  be the functions given by
$$\mu_{3} (a) = \frac{3}{2} + a$$
$$\mu_{4} (a) = 2 + \frac{8}{3} a + a^{2},$$
so that if $n = 3$, then
$$\epsilon_{k+1}  = \frac{2\epsilon_{k}^{2} \mu_{3} (\epsilon_{k} )}{3(\epsilon_{k}  + 1)^{2}} ,for allk \ge 0,$$
and if $n = 4$, then
$$\epsilon_{k+1}  = \frac{3\epsilon_{k}^{2} \mu_{4} (\epsilon_{k} )}{4(\epsilon_{k}  + 1)^{3}} ,for allk \ge 0.$$
Prove that
$$a\mu_{3} (a) \le (a + 1)^{2}-1,for alla \ge 0,$$
and
$$a\mu_{4} (a) \le (a + 1)^{3}-1,for alla \ge 0.$$
Let $\eta_{3,k}  = \mu_{3} (\epsilon_{1} )\epsilon_{k}$  when $n = 3$, and $\eta_{4,k}  = \mu_{4} (\epsilon_{1} )\epsilon_{k}$  when $n = 4$. Prove that
$$\eta_{3,k+1}  \le \frac{2}{3} \eta_{3,k}^{2} ,for allk \ge 1,$$

<!-- PAGE 1542 -->
and
$$\eta_{4,k+1}  \le \frac{3}{4} \eta_{4,k}^{2} ,for allk \ge 1.$$
Deduce from the above that the rate of convergence of $\eta_{i,k}$  is very fast, for $i = 3, 4$ (and $k \ge 1)$.
Remark: If we let $\mu_{2} (a) = a$ for all a and $\eta_{2,k}  = \epsilon_{k}$ , we then proved that
$$\eta_{2,k+1}  \le \frac{1}{2} \eta_{2,k}^{2} ,for allk \ge 1.$$
Problem 41.8. This is a continuation of Problem 41.7.
$(1)$ Prove that for all $n \ge 2$, we have
$$\epsilon_{k+1}  = \begin{pmatrix} n -1 \\ n \end{pmatrix} \frac{\epsilon_{k}^{2} \mu_{n} (\epsilon_{k} )}{(\epsilon_{k}  + 1)^{n-1}} ,for allk \ge 0,$$
where $\mu_{n}$  is given by
$$\mu_{n} (a) = \frac{1}{2} n + \sum_{j=1}^{n-4}  \frac{1}{n -1} \begin{pmatrix} n -2 \\ (n -1) \\ j \end{pmatrix} \begin{pmatrix} n -2 \\ + (n -2) \\ j + 1 \end{pmatrix} \begin{pmatrix} n -2 \\ - \\ j + 2 \end{pmatrix} \begin{pmatrix}\end{pmatrix} a^{j}$$
$$+ \frac{n(n2)}{n -1} - a^{n-3} + a^{n-2}.$$
Furthermore, prove that $\mu_{n}$  can be expressed as
$$\mu_{n} (a) = \frac{1}{2} n + \frac{n(n2)}{3} -a + \sum_{j=2}^{n-4}  \frac{(j + 1)n}{(j + 2)(n -1)} \begin{pmatrix} n -1 \\ j + 1 \end{pmatrix} a^{j} + \frac{n(n2)}{n -1} - a^{n-3} + a^{n-2}.$$
$(2)$ Prove that for every $j$, with $1 \le j \le n$ - $1$, the coefficient of $a^{j}$ in $a\mu_{n}$ (a) is less than or equal to the coefficient of $a^{j}$ in $(a + 1)^{n-1}$ - $1$, and thus
$$a\mu_{n} (a) \le (a + 1)^{n-1}-1,for alla \ge 0,$$
with strict inequality if $n \ge 3$. In fact, prove that if $n \ge 3$, then for every $j$, with $3 \le j \le$ n-2, the coefficient of $a^{j}$ in $a\mu_{n}$ (a) is strictly less than the coefficient of $a^{j}$ in $(a+1)^{n-1}-1$, and if $n \ge 4$, this also holds for $j = 2$. Let $\eta_{n,k}  = \mu_{n} (\epsilon_{1} )\epsilon_{k}  (n \ge 2)$. Prove that
$$\eta_{n,k+1}  \le \begin{pmatrix} n -1 \\ n \end{pmatrix} \eta_{n,k}^{2} ,for allk \ge 1.$$
