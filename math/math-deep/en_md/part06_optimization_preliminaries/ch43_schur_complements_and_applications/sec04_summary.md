# Summary


<!-- PAGE 1571 -->

## 43.4 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Schur complements. $\bullet$  The matrix inversion lemma. $\bullet$  Symmetric positive definite matrices and Schur complements. $\bullet$  Symmetric positive semidefinite matrices and Schur complements.

## 43.5 Problems

Problem 43.1. Prove that maximizing the function $g(\lambda$ ) given by
$$g(\lambda ) = c_{0} + \lambda c_{1} -(b_{0} + \lambda b_{1})^{\top}(A_{0} + \lambda A_{1})^{+}(b_{0} + \lambda b_{1}),$$
subject to
$$A_{0} + \lambda A_{1} ⪰0,b_{0} + \lambda b_{1} \in range(A_{0} + \lambda A_{1}),$$
with $A_{0}, A_{1}$ some $n\times n$ symmetric positive semidefinite matrices, $b_{0}, b_{1} \in \mathbb{R}^{n}$, and $c_{0}, c_{1} \in \mathbb{R}$, is equivalent to maximizing $\gamma$  subject to the constraints
$$\lambda  \ge 0$$
$$\begin{pmatrix} A_{0} + \lambda A_{1} & b_{0} + \lambda b_{1} \\ (b_{0} + \lambda b_{1})^{\top} & c_{0} + \lambda c_{1} -\gamma \end{pmatrix} ⪰0.$$
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Problem 43.2. Let $a_{1}, \dots  , a_{m}$ be $m$ vectors in and assume that they span .
$(1)$ Prove that the matrix
$$\sum_{k=1}^{m}  a_{k}a_{k}^{\top}$$
is symmetric positive definite.
$(2)$ Define the matrix $X$ by
$$!-1$$
$$X = \sum_{k=1}^{m}  a_{k}a_{k}^{\top}.$$
Prove that
$$\sum_{k}  m=1 a_{k}a_{k}^{\top}a_{i}!⪰$$
$$0,i = 1, \dots  , m.$$
$$a_{i}^{\top}1$$
Deduce that
$$a_{i}^{\top} Xa_{i} \le 1,1 \le i \le m.$$
