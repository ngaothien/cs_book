# Summary


<!-- PAGE 325 -->

> **Proposition 8.27.** Let $E$ be any finite-dimensional vector space. For every transvection $\tau_{\phi ,u}  (u \neq  0)$ and every linear map $g \in$ GL(E), the map $g \circ \tau_{\phi ,u}  \circ g^{-1}$ is the transvection of hyperplane g(H) and direction g(u) (that is, $g \circ \tau_{\phi ,u}  \circ g^{-1} = \tau_{\phi\circ g-1,g(u)}$ ). For every other
$$̸$$
transvection $\tau_{\psi ,u'}$  (u' $= 0)$, there is some $g \in$ GL(E) such $\tau_{\psi ,u'}  = g \circ \tau_{\phi ,u}  \circ g^{-1}$; in other words any two transvections $(\neq$  id) are conjugate in GL(E). Moreover, if $n \ge 3$, then the linear isomorphism $g$ as above can be chosen so that $g \in$ SL(E).

*Proof.* We just need to prove that if $n \ge 3$, then for any two transvections $\tau_{\phi ,u}$  and $\tau_{\psi ,u'} (u$, u' $\neq  0)$, there is some $g \in$ SL(E) such that $\tau_{\psi ,u'}  = g\circ \tau_{\phi ,u} \circ g^{-1}$. As before, we pick a basis $(v, u, e_{2}, \dots  , e_{n-1})$ where $(u, e_{2}, \dots  , e_{n-1})$ is a basis of $H$, we pick a basis (v', u', $e_{2}', \dots  , e_{n-1}')$ where (u', $e_{2}', \dots  , e_{n-1}')$ is a basis of H', and we define $g$ as the unique linear map such that g(v) $=$ v', g(u) $=$ u', and $g(e_{i}) = e_{i}'$, for $i = 1, \dots  , n$ - $1$. But in this case, both $H$ and H' $=$ g(H) have dimension at least $2$, so in any basis of H' including u', there is some basis vector $e_{2}'$ independent of u', and we can rescale $e_{2}'$ in such a way that the matrix of $g$ over the two bases has determinant $+1$.

## 8.16 Summary

The main concepts and results of this chapter are listed below: $\bullet$  One does not solve (large) linear systems by computing determinants. $\bullet$  Upper-triangular (lower-triangular) matrices. $\bullet$  Solving by back-substitution (forward-substitution). $\bullet$  Gaussian elimination. $\bullet$  Permuting rows. $\bullet$  The pivot of an elimination step; pivoting. $\bullet$  Transposition matrix; elementary matrix. $\bullet$  The Gaussian elimination theorem (Theorem 8.1). $\bullet$  Gauss-Jordan factorization. $\bullet$  LU-factorization; Necessary and sufficient condition for the existence of an LU-factorization (Proposition 8.2). $\bullet$  LDU-factorization. $\bullet$  “PA $= LU$ theorem” (Theorem 8.5). $\bullet  LDL^{\top}-factorization$ of a symmetric matrix.
