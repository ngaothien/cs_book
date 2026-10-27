# Summary


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
