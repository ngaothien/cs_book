# Summary


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
