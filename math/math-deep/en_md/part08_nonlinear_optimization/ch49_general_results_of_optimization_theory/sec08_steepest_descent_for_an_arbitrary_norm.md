# Steepest Descent for an Arbitrary Norm


<!-- PAGE 1735 -->
Another rule for choosing the stepsize is Armijo’s rule. These methods, and others, are discussed in detail in Berstekas $[17]$. Boyd and Vandenberghe discuss steepest descent methods for various types of norms besides the Euclidean norm; see Boyd and Vandenberghe $[29]$ (Section 9.4). Here is brief summary.

## 49.8 Steepest Descent for an Arbitrary Norm

The idea is to make $\langle \nabla J_{uk}, d_{k}\rangle$ as negative as possible. To make the question sensible, we have to limit the size of $d_{k}$ or normalize by the length of $d_{k}$. Let $\|\|$ be any norm on $\mathbb{R}^{n}$. Recall from Section 14.7 that the dual norm is defined by
$$\|y\|^{D}= \sup|\langle x, y\rangle |.$$
$$x\in \mathbb{R} n$$
$$\|x\|=1$$

> **Definition 49.8.** A normalized steepest descent direction (with respect to the norm $\|\|)$ is any unit vector $d_{nsd,k}$ which achieves the minimum of the set of reals
$${\langle \nabla J_{uk}, d\rangle | \|d\|= 1}.$$
By definition, $\|d_{nsd,k}\| = 1$. A unnormalized steepest descent direction $d_{sd,k}$ is defined as
$$d_{sd,k} = \|\nabla J_{uk}\|^{D}d_{nsd,k}.$$
It can be shown that
$$\langle \nabla J_{uk}, d_{sd,k}\rangle = -(\|\nabla J_{uk}\|^{D})^{2};$$
see Boyd and Vandenberghe $[29]$ (Section 9.4). The steepest descent method (with respect to the norm $\|\|)$ consists of the following steps: Given a starting point $u_{0} \in$ dom(J) do: repeat
$(1)$ Compute the steepest descent direction $d_{sd,k}$.
$(2)$ Line search. Perform an exact or backtracking line search to find $\rho_{k}$ .
$(3)$ Update. $u_{k+1} = u_{k} + \rho_{k} d_{sd,k}$.

<!-- PAGE 1736 -->
until stopping criterion is satisfied. If $\|\|$ is the $\ell^{2}$ -norm, then we see immediately that $d_{sd,k} = -\nabla J_{uk}$, so in this case the method coincides with the steepest descent method for the Euclidean norm as defined at the beginning of Section 49.6 in $(3)$ and $(4)$. If $P$ is a symmetric positive definite matrix, it is easy to see that $\|z\|_{P} = (z^{\top}Pz)^{1/2} = P^{1/2}z_{2}$ is a norm. Then it can be shown that the normalized steepest descent direction is
$$d_{nsd,k} = -(\nabla J_{uk}^{\top}P^{-1}\nabla J_{uk})^{-1/2}P^{-1}\nabla J_{uk},$$
the dual norm is $\|z\|^{D} =$

$P^{-1/2}z_{2}$, and the steepest descent direction with respect to $\|\|_{P}$ is given by
$$d_{sd,k} = -P^{-1} \nabla J_{uk}.$$
A judicious choice for $P$ can speed up the rate of convergence of the gradient descent method; see see Boyd and Vandenberghe $[29]$ (Section 9.4.1 and Section 9.4.4). If $\|\|$ is the $\ell^{1}$ -norm, then it can be shown that $d_{nsd,k}$ is determined as follows: let $i$ be any index for which $\|\nabla J_{uk}\|_{\infty} = |(\nabla J_{uk})_{i}|$. Then
$$d_{nsd,k} = -sign \begin{pmatrix} \partial J \\ (u_{k}) \\ \partial x_{i} \end{pmatrix} e_{i},$$
where $e_{i}$ is the ith canonical basis vector, and
$$d_{sd,k} = - \frac{\partial J}{\partial x_{i}} (u_{k})e_{i}.$$
For more details, see Boyd and Vandenberghe $[29]$ (Section 9.4.2 and Section 9.4.4). It is also shown in Boyd and Vandenberghe $[29]$ (Section 9.4.3) that the steepest descent method converges for any norm $\|\|$ and any strictly convex function $J$. One of the main goals in designing a gradient descent method is to ensure that the convergence factor is as small as possible, which means that the method converges as quickly as possible. Machine learning has been a catalyst for finding such methods. A method discussed in Strang $[177]$ (Chapter VI, Section $4)$ consists in adding a momentum term to the gradient. In this method, $u_{k+1}$ and $d_{k+1}$ are determined by the following system of equations:
$$u_{k+1} = u_{k} -\rho d_{k}$$
$$d_{k+1} -\nabla J_{uk+1} = \beta d_{k}.$$
Of course the trick is to choose $\rho$  and $\beta$  in such a way that the convergence factor is as small as possible. If $J$ is given by a quadratic functional, say $(1/2)u^{\top}Au$ - $b^{\top}u$, then $\nabla J_{uk+1} = Au_{k+1}-b$ so we obtain a linear system. It turns out that the rate of convergence of
