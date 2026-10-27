# Summary


<!-- PAGE 620 -->
Another way (due to Jean Dieudonn´e) to prove that a section $s$ of $\rho$  is not a homomorphism is to prove that any unit quaternion is the product of two unit pure quaternions. Indeed, if $q = [a, u]$ is a unit quaternion, if we let $q_{1} = [0, u_{1}]$, where $u_{1}$ is any unit vector orthogonal to $u$, then
$$q_{1}q = [-u_{1} \cdot  u, au_{1} + u_{1} \times  u] = [0, au_{1} + u_{1} \times  u] = q_{2}$$
is a nonzero unit pure quaternion. This is because if $a \neq  0$ then $au_{1}+u_{1}\times u \neq  0$ (since $u_{1}\times u$ is orthogonal to $au_{1} \neq  0)$, and if $a = 0$ then $u \neq  0$, so $u_{1} \times  u \neq  0$ (since $u_{1}$ is orthogonal to $u)$. But then, $q_{1}^{-1} = [0, -u_{1}]$ is a unit pure quaternion and we have
$$q = q_{1}^{-1} q_{2},$$
a product of two pure unit quaternions. We also observe that for any two pure quaternions $q_{1}, q_{2}$, there is some unit quaternion $q$ such that
$$q_{2} = qq_{1}q^{-1}.$$
This is just a restatement of the fact that the group SO(3) is transitive. Since the kernel of $\rho$ : SU(2) $\to$ SO(3) is ${I, -I}$, the subgroup s(SO(3)) would be a normal subgroup of index $2$ in SU(2). Then we would have a surjective homomorphism $\eta$  from SU(2) onto the quotient group $SU(2)/s(SO(3))$, which is isomorphic to ${1, -1}$. Now, since any two pure quaternions are conjugate of each other, $\eta$  would have a constant value on the unit pure quaternions. Since $k =$ ij, we would have
$$\eta (k) = \eta (ij) = (\eta (i))^{2}= 1.$$
Consequently, $\eta$  would map all pure unit quaternions to $1$. But since every unit quaternion is the product of two pure quaternions, $\eta$  would map every unit quaternion to $1$, contradicting the fact that it is surjective onto ${-1, 1}$.

## 16.8 Summary

The main concepts and results of this chapter are listed below: $\bullet$  The group SU(2) of unit quaternions. $\bullet$  The skew field $\mathbb{H}$ of quaternions. $\bullet$  Hamilton’s identities. $\bullet$  The (real) vector space $\mathfrak{su}(2)$ of $2 \times  2$ skew Hermitian matrices with zero trace. $\bullet$  The adjoint representation of SU(2).
