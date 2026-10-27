# Summary


<!-- PAGE 1939 -->
where $A$ is an $m \times  n$ matrix, $F$ is a $p \times  n$ matrix, and either $A$ has rank $n$ or $F$ has rank $n$. This problem is converted to the ADMM problem
$$minimize\|Ax -b\|_{2}^{2} + \tau  \|z\|_{1}$$
$$subject to Fx -z = 0,$$
$$and the corresponding ADMM procedure (in scaled form) is$$
$$x^{k+1}= (A^{\top}A + \rho F^{\top}F)^{-1}(A^{\top}b + \rho F^{\top}(z^{k}-u^{k}))$$
$$z^{k+1}= S_{\tau /\rho}(Fx^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ Fx^{k+1}-z^{k+1}.$$
$(6)$ Group Lasso. This a generalization of $(3)$. Here we assume that $x$ is split as $x = (x_{1}, \dots  , x_{N})$, with $x_{i} \in \mathbb{R}_{i}^{n}$ and $n_{1} + \cdots  + x_{N} = n$, and the regularizing term $\|x\|_{1}$ is replaced by
$$\sum_{i}  N=1 \|x_{i}\|_{2}. When n_{i} = 1, this reduces to (3). The z-update of the ADMM   procedure$$
needs to modified. We define the soft thresholding operator $\mathcal{S}_{c}$ : $\mathbb{R}^{m} \to \mathbb{R}^{m}$ given by
$$\mathcal{S}_{c}(v) = \begin{pmatrix} c \\ 1 - \\ \|v \end{pmatrix} \|_{2+}v,$$
with $\mathcal{S}_{c}(0) = 0$. Then the z-update consists of the $N$ updates
$$z_{i}^{k+1}=\mathcal{S}_{\tau /\rho}(x_{i}^{k+1}+ u^{k}),i = 1, \dots  , N.$$
The method can be extended to deal with overlapping groups; see Boyd et al. $[28]$ (Section 6.4). There are many more applications of ADMM discussed in Boyd et al. $[28]$, including consensus and sharing. See also Strang $[177]$ for a brief overview.

## 52.9 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Dual ascent. $\bullet$  Augmented Lagrangian. $\bullet$  Penalty parameter. $\bullet$  Method of multipliers. $\bullet$  ADMM (alternating direction method of multipliers).
