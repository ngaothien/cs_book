# Conditioning of Eigenvalue Problems


<!-- PAGE 585 -->

## 15.4 Conditioning of Eigenvalue Problems

The following $n \times  n$ matrix
$$A = \begin{pmatrix} 0 \\ 1 & 0 \\ 1 & 0 \\ \ddots & \ddots \\ 1 & 0 \\ 1 & 0 \end{pmatrix}$$
has the eigenvalue $0$ with multiplicity $n$. However, if we perturb the top rightmost entry of $A$ by $\epsilon$ , it is easy to see that the characteristic polynomial of the matrix
$$A(\epsilon ) = \begin{pmatrix} 0 & \epsilon \\ 1 & 0 \\ 1 & 0 \\ \ddots & \ddots \\ 1 & 0 \\ 1 & 0 \end{pmatrix}$$
is $X^{n}$ - $\epsilon$ . It follows that if $n = 40$ and $\epsilon  = 10^{-40}, A(10^{-40})$ has the eigenvalues $10^{-1}e^{k2\pi i/40}$ with $k = 1, \dots  , 40$. Thus, we see that a very small change $(\epsilon  = 10^{-40})$ to the matrix $A$ causes a significant change to the eigenvalues of $A$ (from $0$ to $10^{-1}e^{k2\pi i/40}$ ). Indeed, the relative error is $10^{-39}$. Worse, due to machine precision, since very small numbers are treated as $0$, the error on the computation of eigenvalues (for example, of the matrix $A(10^{-40}))$ can be very large. This phenomenon is similar to the phenomenon discussed in Section 9.5 where we studied the effect of a small perturbation of the coefficients of a linear system Ax $= b$ on its solution. In Section 9.5, we saw that the behavior of a linear system under small perturbations is governed by the condition number cond(A) of the matrix $A$. In the case of the eigenvalue problem (finding the eigenvalues of a matrix), we will see that the conditioning of the problem depends on the condition number of the change of basis matrix $P$ used in reducing the matrix $A$ to its diagonal form $D = P^{-1}$ AP, rather than on the condition number of $A$ itself. The following proposition in which we assume that $A$ is diagonalizable and that the matrix norm $\|\|$ satisfies a special condition (satisfied by the operator norms $\|\|_{p}$ for $p = 1, 2, \infty$ ), is due to Bauer and Fike $(1960)$.

> **Proposition 15.11.** Let $A \in M_{n}(\mathbb{C})$ be a diagonalizable matrix, $P$ be an invertible matrix, and $D$ be a diagonal matrix $D = diag(\lambda_{1} , \dots  , \lambda_{n}$ ) such that
$$A = PDP^{-1} ,$$

<!-- PAGE 586 -->
and let $\|\|$ be a matrix norm such that
$$\|\mathrm{diag}(\alpha_{1} , \dots  , \alpha_{n} )\|= \max |\alpha_{i} |,$$
$$1\le i\le n$$
for every diagonal matrix. Then for every perturbation matrix $\Delta A$, if we write
$$B_{i} = {z \in \mathbb{C} | |z -\lambda_{i} | \le cond(P) \|\Delta A\|},$$
for every eigenvalue $\lambda$  of $A + \Delta A$, we have
$$\lambda  \in \bigcup_{k=1}^{n}  B_{k}.$$

*Proof.* Let $\lambda$  be any eigenvalue of the matrix $A + \Delta A$. If $\lambda  = \lambda_{j}$  for some $j$, then the result is trivial. Thus assume that $\lambda$ ̸ $= \lambda_{j}$  for $j = 1, \dots  , n$. In this case the matrix $D$ - $\lambda$ I is invertible (since its eigenvalues are $\lambda$  - $\lambda_{j}$  for $j = 1, \dots  , n)$, and we have
$$P^{-1} (A + \Delta A -\lambda I)P = D -\lambda I + P^{-1} (\Delta A)P$$
$$= (D -\lambda I)(I + (D -\lambda I)^{-1}P^{-1} (\Delta A)P).$$
Since $\lambda$  is an eigenvalue of $A + \Delta A$, the matrix $A + \Delta A$ - $\lambda$ I is singular, so the matrix
$$I + (D -\lambda I)^{-1}P^{-1} (\Delta A)P$$
must also be singular. By Proposition 9.12(2), we have
$$1 \le

$(D -\lambda I)^{-1}P^{-1}(\Delta$ A)P

,$$ and since $\|\|$ is a matrix norm,
$$(D -\lambda I)^{-1}P^{-1}(\Delta A)P

$\le$

$(D -\lambda I)^{-1}$



$P^{-1}$

$\|\Delta A\|\|P\|,$$$ so we have
$$1 \le

$(D -\lambda I)^{-1}$



$P^{-1}$

$\|\Delta A\|\|P\|.$$$ Now $(D$ - $\lambda I)^{-1}$ is a diagonal matrix with entries $1/(\lambda_{i}$  - $\lambda$ ), so by our assumption on the norm,
$$(D -\lambda I)^{-1}

$= \frac{1}{min_{i}(|\lambda_{i}  -\lambda |)}$ .$$ As a consequence, since there is some index $k$ for which $min_{i}(|\lambda_{i}$  - $\lambda$ |) $= |\lambda_{k}$  - $\lambda$ |, we have
$$(D -\lambda I)^{-1}

$= \frac{1}{|\lambda_{k}  -\lambda |}$ ,$$ and we obtain
$$|\lambda  -\lambda_{k} | \le

$P^{-1}$

$\|\Delta A\|\|P\|=$ cond(P) $\|\Delta A\|,$$$ which proves our result.
