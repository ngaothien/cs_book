# The Group SU(2) and the Skew Field H of Quaternions


<!-- PAGE 601 -->
Chapter $16$ Unit Quaternions and Rotations in SO(3) This chapter is devoted to the representation of rotations in SO(3) in terms of unit quaternions. Since we already defined the unitary groups SU(n), the quickest way to introduce the unit quaternions is to define them as the elements of the group SU(2). The skew $field\mathbb{H}$ of quaternions and the group SU(2) of unit quaternions are discussed in Section 16.1. In Section 16.2, we define a homomorphism $r$: SU(2) $\to$ SO(3) and prove that its kernel is ${-I, I}$. We compute the rotation matrix $R_{q}$ associated with the rotation $r_{q}$ induced by a unit quaternion $q$ in Section 16.3. In Section 16.4, we prove that the homomorphism $r$: SU(2) $\to$ SO(3) is surjective by providing an algorithm to construct a quaternion from a rotation matrix. In Section 16.5 we define the exponential map exp: $\mathfrak{su}(2) \to$ SU(2) where $\mathfrak{su}(2)$ is the real vector space of skew-Hermitian $2 \times  2$ matrices with zero trace. We prove that exponential map exp: $\mathfrak{su}(2) \to$ SU(2) is surjective and give an algorithm for finding a logarithm. We discuss quaternion interpolation and prove the famous slerp interpolation formula due to Ken Shoemake in Section 16.6. This formula is used in robotics and computer graphics to deal with interpolation problems. In Section 16.7, we prove that there is no “nice” section $s$: SO(3) $\to$ SU(2) of the homomorphism $r$: SU(2) $\to$ SO(3), in the sense that any section of $r$ is neither a homomorphism nor continuous.

## 16.1 The Group SU(2) of Unit Quaternions and the

$$\mathbb{H}$$
$$Skew Field of Quaternions$$

> **Definition 16.1.** The unit quaternions are the elements of the group SU(2), namely the group of $2 \times  2$ complex matrices of the form
$$\begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \alpha , \beta  \in \mathbb{C}, \overline{\alpha \alpha} +\overline{\beta \beta} = 1.$$
The quaternions are the elements of the real vector space $\mathbb{H} =\mathbb{R}$ SU(2).
$$601$$

<!-- PAGE 602 -->
Let $1, i, j, k$ be the matrices
$$1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,i = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} ,j = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} ,k = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} ,$$
then $\mathbb{H}$ is the set of all matrices of the form
$$X = a1 + bi + cj + dk,a, b, c, d \in \mathbb{R}.$$
Indeed, every matrix in $\mathbb{H}$ is of the form
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a, b, c, d \in \mathbb{R}.$$
It is easy (but a bit tedious) to verify that the quaternions $1, i, j, k$ satisfy the famous identities discovered by Hamilton:
$$i^{2}= j^{2}= k^{2}= ijk = -1,$$
$$ij = -ji = k,$$
$$jk = -kj = i,$$
$$ki = -ik = j.$$
Thus, the quaternions are a generalization of the complex numbers, but there are three square roots of $-1$ and multiplication is not commutative. Given any two quaternions $X = a1+bi+cj+dk$ and $Y = a'1+b'i+c'j+d'k$, Hamilton’s famous formula
$$XY = (aa'-bb'-cc'-dd')1 + (ab'+ ba'+ cd'-dc')i$$
$$+ (ac'+ ca'+ db'-bd')j + (ad'+ da'+ bc'-cb')k$$
looks mysterious, but it is simply the result of multiplying the two matrices
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} andY = \begin{pmatrix} a' + ib' & c'+ id' \\ -(c'-id') & a'-ib' \end{pmatrix} .$$
It is worth noting that this formula was discovered independently by Olinde Rodrigues in $1840$, a few years before Hamilton (Veblen and Young $[190])$. However, Rodrigues was working with a different formalism, homogeneous transformations, and he did not discover the quaternions. If
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a, b, c, d \in \mathbb{R},$$
it is immediately verified that
$$XX^{*}= X^{*}X = (a^{2}+ b^{2}+ c^{2}+ d^{2})1.$$
