# Summary


<!-- PAGE 653 -->
However,
$$\dim(F) + \dim(G) + \dim(H) = i + j + n -k + 1$$
and $i + j = k + n$, so we have
$$\dim(F \cap G \cap H) \ge i + j + n -k + 1 -2n = k + n + n -k + 1 -2n = 1,$$
which shows that $F \cap G \cap H \neq  (0)$. Then for any unit vector $z \in F \cap G \cap H \neq  (0)$, we have
$$\lambda_{k} (A + B) \le z^{\top}(A + B)z,\lambda_{i} (A) \ge z^{\top}Az,\lambda_{j} (B) \ge z^{\top}Bz,$$
establishing the desired inequality $\lambda_{k} (A + B) \le \lambda_{i} (A) + \lambda_{j} (B)$. In the special case $i = j = k$, we obtain
$$\lambda_{1} (A) + \lambda_{1} (B) \le \lambda_{1} (A + B),\lambda_{n} (A + B) \le \lambda_{n} (A) + \lambda_{n} (B).$$
It follows that $\lambda_{1}$  (as a function) is concave, while $\lambda_{n}$  (as a function) is convex. If $i = k$ and $j = 1$, we obtain
$$\lambda_{k} (A) + \lambda_{1} (B) \le \lambda_{k} (A + B),$$
and if $i = k$ and $j = n$, we obtain
$$\lambda_{k} (A + B) \le \lambda_{k} (A) + \lambda_{n} (B),$$
and combining them, we get
$$\lambda_{k} (A) + \lambda_{1} (B) \le \lambda_{k} (A + B) \le \lambda_{k} (A) + \lambda_{n} (B).$$
In particular, if $B$ is positive semidefinite, since its eigenvalues are nonnegative, we obtain the following inequality known as the monotonicity theorem for symmetric (or Hermitian) matrices: if $A$ and $B$ are symmetric (or Hermitian) and $B$ is positive semidefinite, then
$$\lambda_{k} (A) \le \lambda_{k} (A + B)k = 1, \dots  , n.$$
The reader is referred to Horn and Johnson $[98]$ (Chapters $4$ and $7)$ for a very complete treatment of matrix inequalities and interlacing results, and also to Lax $[117]$ and Serre $[162]$.

## 17.8 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Normal linear maps, self-adjoint linear maps, skew-self-adjoint linear maps, and orthogonal linear maps.
