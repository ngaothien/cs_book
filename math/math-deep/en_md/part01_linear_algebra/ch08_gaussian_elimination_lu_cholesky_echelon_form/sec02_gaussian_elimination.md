# Gaussian Elimination


<!-- PAGE 261 -->
Once the above system is solved, the B´ezier cubics $C_{1}, \dots , C_{N}$ are determined as follows (we assume $N \ge 2)$: For $2 \le i \le N$ - $1$, the control points $(b_{0}^{i}, b_{1}^{i}, b_{2}^{i}, b_{3}^{i})$ of $C_{i}$ are given by
$$b_{0}^{i} = x_{i-1}$$
$$b_{1}^{i} = \frac{2}{3} d_{i-1} + \frac{1}{3} d_{i}$$
$$b_{2}^{i} = \frac{1}{3} d_{i-1} + \frac{2}{3} d_{i}$$
$$b_{3}^{i} = x_{i}.$$
The control points $(b_{0}^{1}, b_{1}^{1}, b_{2}^{1}, b_{3}^{1})$ of $C_{1}$ are given by
$$b_{0}^{1} = x_{0}$$
$$b_{1}^{1} = d_{0}$$
$$b_{2}^{1} = \frac{1}{2} d_{0} + \frac{1}{2} d_{1}$$
$$b_{3}^{1} = x_{1},$$
and the control points $(b_{0}^{N} , b_{1}^{N} , b_{2}^{N} , b_{3}^{N}$ ) of $C_{N}$ are given by
$$b_{0}^{N} = x_{N-1}$$
$$b_{1}^{N} = \frac{1}{2} d_{N-1} + \frac{1}{2} d_{N}$$
$$b_{2}^{N} = d_{N}$$
$$b_{3}^{N} = x_{N}.$$
Figure 8.5 illustrates this process spline interpolation for $N = 7$. We will now describe various methods for solving linear systems. Since the matrix of the above system is tridiagonal, there are specialized methods which are more efficient than the general methods. We will discuss a few of these methods.

## 8.2 Gaussian Elimination

$$\mathbb{R}^{n}$$
Let $A$ be an $n \times  n$ matrix, let $b \in$ be an $n$-dimensional vector and assume that $A$ is invertible. Our goal is to solve the system Ax $= b$. Since $A$ is assumed to be invertible, we know that this system has a unique solution $x = A^{-1}b$. Experience shows that two counter-intuitive facts are revealed:
$(1)$ One should avoid computing the inverse $A^{-1}$ of $A$ explicitly. This is inefficient since it would amount to solving the $n$ linear systems $Au^{(j)} = e_{j}$ for $j = 1, \dots  , n$, where
$$\mathbb{R}^{n}$$
$e_{j} = (0, \dots  , 1, \dots  , 0)$ is the jth canonical basis vector of (with a $1$ is the jth slot). By doing so, we would replace the resolution of a single system by the resolution of $n$ systems, and we would still have to multiply $A^{-1}$ by $b$.

<!-- PAGE 262 -->
$$d_{2}$$
$$b_{2}^{2}$$
$$b_{1}^{2}$$
$$d_{1}b_{1}^{3}$$
$$x_{2}$$
$$x_{1}b_{2}^{3}d_{7}=b_{2}^{7}$$
$$1$$
$$b_{2}$$
$$d_{3}b_{1}^{7}$$
$$x_{3}$$
$1 d_{0} d_{6} b = 4 1 b_{1}$
$$x_{6}$$
$$b_{2}^{6}$$
$$b_{2}^{4}$$
$$x_{4}$$
$$x_{5}$$
$$d_{4}b_{1}^{6}$$
$$b_{1}^{5}$$
$$b_{2}^{5}$$
$$d_{5}$$
$x_{0} = d_{1} x_{7} = d_{8}$

![Figure 8.5](../../assets/ch08/fig_8_5.png)

**Figure 8.5:** A $C^{2}$ cubic interpolation of $x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}$ with associated color coded B´ezier cubics.
$(2)$ One does not solve (large) linear systems by computing determinants (using Cramer’s formulae) since this method requires a number of additions (resp. multiplications) proportional to $(n + 1)$! (resp. $(n + 2)!)$. The key idea on which most direct methods (as opposed to iterative methods, that look for an approximation of the solution) are based is that if $A$ is an upper-triangular matrix, which means that $a_{ij} = 0$ for $1 \le j < i \le n$ (resp. lower-triangular, which means that $a_{ij} = 0$ for $1 \le i < j \le n)$, then computing the solution $x$ is trivial. Indeed, say $A$ is an upper-triangular matrix
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & \cdots & a_{1n-2} & a_{1n-1} & a_{1n} \\ 0 & a_{2 2} & \cdots & a_{2n-2} & a_{2n-1} & a_{2n} \\ 0 & 0 & \ddots & \vdots & \vdots & \vdots \\ \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 0 & a_{n-1n-1} & a_{n-1n} \\ 0 & 0 & 0 & 0 & a_{n n} \end{pmatrix} .$$
$$\cdots$$
Then det(A) $= a_{1 1}a_{2 2} \cdots  a_{n n} \neq  0$, which implies that $a_{i i} \neq  0$ for $i = 1, \dots  , n$, and we can solve the system Ax $= b$ from bottom-up by back-substitution. That is, first we compute

<!-- PAGE 263 -->
$x_{n}$ from the last equation, next plug this value of $x_{n}$ into the next to the last equation and compute $x_{n-1}$ from it, etc. This yields
$$x_{n}=a_{n n}^{-1}b_{n}$$
$$x_{n-1}=a_{n-1n-1}^{-1}(b_{n-1} -a_{n-1n}x_{n})$$
$$\vdots$$
$$x_{1}=a_{1 1}^{-1}(b_{1} -a_{1 2}x_{2} -\cdots  -a_{1n}x_{n}).$$
Note that the use of determinants can be avoided to prove that if $A$ is invertible then $a_{i i} \neq  0$ for $i = 1, \dots  , n$. Indeed, it can be shown directly (by induction) that an upper (or lower) triangular matrix is invertible iff all its diagonal entries are nonzero. If $A$ is lower-triangular, we solve the system from top-down by forward-substitution. Thus, what we need is a method for transforming a matrix to an equivalent one in uppertriangular form. This can be done by elimination. Let us illustrate this method on the following example:
$$2x+y+z=5$$
$$4x-6y=-2$$
$$-2x+7y+2z=9.$$
We can eliminate the variable $x$ from the second and the third equation as follows: Subtract twice the first equation from the second and add the first equation to the third. We get the new system
$$2x+y+z=5$$
$$-8y-2z=-12$$
$$8y+3z=14.$$
This time we can eliminate the variable $y$ from the third equation by adding the second equation to the third:
$$2x+y+z=5$$
$$-8y-2z=-12$$
$$z=2.$$
This last system is upper-triangular. Using back-substitution, we find the solution: $z = 2, y = 1, x = 1$. Observe that we have performed only row operations. The general method is to iteratively eliminate variables using simple row operations (namely, adding or subtracting a multiple of a row to another row of the matrix) while simultaneously applying these operations to the vector $b$, to obtain a system, MAx $=$ Mb, where MA is upper-triangular. Such a method is called Gaussian elimination. However, one extra twist is needed for the method to work in all cases: It may be necessary to permute rows, as illustrated by the following example:
$$x+y+z= 1$$
$$x+y+3z= 1$$
$$2x+5y+8z= 1.$$

<!-- PAGE 264 -->
In order to eliminate $x$ from the second and third row, we subtract the first row from the second and we subtract twice the first row from the third:
$$x+y+z= 1$$
$$2z= 0$$
$$3y+6z= -1.$$
Now the trouble is that $y$ does not occur in the second row; so, we can’t eliminate $y$ from the third row by adding or subtracting a multiple of the second row to it. The remedy is simple: Permute the second and the third row! We get the system:
$$x+y+z= 1$$
$$3y+6z= -1$$
$$2z= 0,$$
which is already in triangular form. Another example where some permutations are needed is:
$$z=1$$
$$-2x+7y+2z=1$$
$$4x-6y=-1.$$
First we permute the first and the second row, obtaining
$$-2x+7y+2z=1$$
$$z=1$$
$$4x-6y=-1,$$
and then we add twice the first row to the third, obtaining:
$$-2x+7y+2z=1$$
$$z=1$$
$$8y+4z=1.$$
Again we permute the second and the third row, getting
$$-2x+7y+2z=1$$
$$8y+4z=1$$
$$z=1,$$
an upper-triangular system. Of course, in this example, $z$ is already solved and we could have eliminated it first, but for the general method, we need to proceed in a systematic fashion. We now describe the method of Gaussian elimination applied to a linear system Ax $= b$, where $A$ is assumed to be invertible. We use the variable $k$ to keep track of the stages of elimination. Initially, $k = 1$.

<!-- PAGE 265 -->
$(1)$ The first step is to pick some nonzero entry $a_{i1}$ in the first column of $A$. Such an entry must exist, since $A$ is invertible (otherwise, the first column of $A$ would be the zero vector, and the columns of $A$ would not be linearly independent. Equivalently, we would have det(A) $= 0)$. The actual choice of such an element has some impact on the numerical stability of the method, but this will be examined later. For the time being, we assume that some arbitrary choice is made. This chosen element is called the pivot of the elimination step and is denoted $\pi_{1}$  (so, in this first step, $\pi_{1}  = a_{i1})$.
$(2)$ Next we permute the row $(i)$ corresponding to the pivot with the first row. Such a step is called pivoting. So after this permutation, the first element of the first row is nonzero.
$(3)$ We now eliminate the variable $x_{1}$ from all rows except the first by adding suitable multiples of the first row to these rows. More precisely we add $-a_{i1}/\pi_{1}$  times the first row to the ith row for $i = 2, \dots  , n$. At the end of this step, all entries in the first column are zero except the first.
$(4)$ Increment $k$ by $1$. If $k = n$, stop. Otherwise, $k < n$, and then iteratively repeat Steps $(1), (2), (3)$ on the $(n$ - $k + 1) \times  (n$ - $k + 1)$ subsystem obtained by deleting the first $k$ - $1$ rows and $k$ - $1$ columns from the current system. If we let $A_{1} = A$ and $A_{k} = (a_{i j}^{(k)}$ ) be the matrix obtained after $k$ - $1$ elimination steps $(2 \le k \le n)$, then the kth elimination step is applied to the matrix $A_{k}$ of the form
$$A_{k} = \begin{pmatrix} a_{1 1}^{(k)} & a_{1 2}^{(k)} & \cdots & \cdots & \cdots & a_{1n}^{(k)} \\ 0 & a_{2 2}^{(k)} & \cdots & \cdots & \cdots & a_{2}^{(k)} \\ \vdots & \ddots & \ddots & \vdots & \ddots \\ 0 & 0 & 0 & a_{k k}^{(k)} & \cdots & a_{k n}^{(k)} \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & a_{n k}^{(k)} & a_{n n}^{(k)} \end{pmatrix} .$$
$$\cdots$$
Actually, note that
$$a_{i j}^{(k)} = a_{i j}^{(i)}$$
for all $i, j$ with $1 \le i \le k$ - $2$ and $i \le j \le n$, since the first $k$ - $1$ rows remain unchanged after the $(k$ - 1)th step. We will prove later that $det(A_{k}) = \pm$  det(A). Consequently, $A_{k}$ is invertible. The fact that $A_{k}$ is invertible iff $A$ is invertible can also be shown without determinants from the fact that there is some invertible matrix $M_{k}$ such that $A_{k} = M_{k}A$, as we will see shortly. Since $A_{k}$ is invertible, some entry $a_{i k}^{(k)}$ with $k \le i \le n$ is nonzero. Otherwise, the last $n$ - $k + 1$ entries in the first $k$ columns of $A_{k}$ would be zero, and the first $k$ columns of $A_{k}$ would yield $k$ vectors in $\mathbb{R}^{k-1}$. But then the first $k$ columns of $A_{k}$ would be linearly
