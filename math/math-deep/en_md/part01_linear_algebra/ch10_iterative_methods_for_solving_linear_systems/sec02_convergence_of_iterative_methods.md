# Convergence of Iterative Methods


<!-- PAGE 392 -->

## 10.2 Convergence of Iterative Methods

Recall that iterative methods for solving a linear system Ax $= b$ (with $A \in M_{n}(\mathbb{C})$ invertible) consists in finding some matrix $B$ and some vector $c$, such that I - $B$ is invertible, and the unique solution $x$ of Ax $= b$ is equal to the unique solution $u$ of $u =$ Bu $+ c$. Then starting
$$e e$$
from any vector $u_{0}$, compute the sequence $(u_{k})$ given by
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N},$$
and say that the iterative method is convergent iff
$$limu_{k} =u,$$
$$k\mapsto \infty  e$$
for every initial vector $u_{0}$. Here is a fundamental criterion for the convergence of any iterative methods based on a matrix $B$, called the matrix of the iterative method.

> **Theorem 10.3.** Given a system $u = Bu+c$ as above, where I $-B$ is invertible, the following statements are equivalent:
$(1)$ The iterative method is convergent.
$(2) \rho (B) < 1$.
$(3) \|B\| < 1$, for some subordinate matrix norm $\|\|$.

*Proof.* Define the vector $e_{k}$ (error vector) by
$$e_{k} = u_{k} -u,$$
$$e$$
where $u$ is the unique solution of the system $u =$ Bu $+ c$. Clearly, the iterative method is $e$ convergent iff
$$lime_{k} = 0.$$
$$k\mapsto \infty$$
We claim that
$$e_{k} = B^{k}e_{0},k \ge 0,$$
where $e_{0} = u_{0}$ - $u$.
$$e$$
This is proven by induction on $k$. The base case $k = 0$ is trivial. By the induction hypothesis, $e_{k} = B^{k}e_{0}$, and since $u_{k+1} = Bu_{k} + c$, we get
$$u_{k+1} -u = Bu_{k} + c -u,$$
$$ee$$
and because $u =$ Bu $+ c$ and $e_{k} = B^{k}e_{0}$ (by the induction hypothesis), we obtain
$$ee$$
$$u_{k+1} -u = Bu_{k} -Bu = B(u_{k} -u) = Be_{k} = BB^{k}e_{0} = B^{k+1}e_{0},$$
$$eee$$
proving the induction step. Thus, the iterative method converges iff
$$limB^{k}e_{0} = 0.$$
$$k\mapsto \infty$$
Consequently, our theorem follows by Theorem 10.1.

<!-- PAGE 393 -->
The next proposition is needed to compare the rate of convergence of iterative methods. It shows that asymptotically, the error vector $e_{k} = B^{k}e_{0}$ behaves at worst like $(\rho (B))^{k}$.

> **Proposition 10.4.** Let $\|\|$ be any vector norm, let $B \in M_{n}(\mathbb{C})$ be a matrix such that I - $B$ is invertible, and let $u$ be the unique solution of $u =$ Bu $+ c$.
$$e$$
$(1)$ If $(u_{k})$ is any sequence defined iteratively by
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N},$$
then
$$$$
$$limsup\|u_{k} -u\|^{1/k}= \rho (B).$$
$$k\mapsto \infty e$$
$$\|u0-u\|=1$$
$$e$$
$(2)$ Let $B_{1}$ and $B_{2}$ be two matrices such that I - $B_{1}$ and I - $B_{2}$ are invertible, assume that both $u = B_{1}u + c_{1}$ and $u = B_{2}u + c_{2}$ have the same unique solution $u$, and consider any
$$e$$
two sequences $(u_{k})$ and $(v_{k})$ defined inductively by
$$u_{k+1} = B_{1}u_{k} + c_{1}$$
$$v_{k+1} = B_{2}v_{k} + c_{2},$$
with $u_{0} = v_{0}$. If $\rho (B_{1}) < \rho (B_{2})$, then for any $\epsilon  > 0$, there is some integer $N(\epsilon$ ), such that for all $k \ge N(\epsilon$ ), we have
$$\| -\|^{1/k}$$
$$\sup \frac{v_{k}u}{\|u_{k} -ue\|} e\ge \frac{\rho (B_{2})}{\rho (B_{1}) + \epsilon} .$$
$$\|u0-u\|=1$$
$$e$$

*Proof.* Let $\|\|$ be the subordinate matrix norm. Recall that
$$u_{k} -u = B^{k}e_{0},$$
$$e$$
with $e_{0} = u_{0}$ - $u$. For every $k \in \mathbb{N}$, we have
$$e$$
$$(\rho (B))^{k}= \rho (B^{k}) \le \|B^{k}\|= \sup\|B^{k}e_{0}\|,$$
$$\|e0\|=1$$
which implies
$$\rho (B) = \sup\|B^{k}e_{0}\|^{1/k}= \|B^{k}\|^{1/k},$$
$$\|e0\|=1$$
and Statement $(1)$ follows from Proposition 10.2. Because $u_{0} = v_{0}$, we have
$$u_{k} -u = B_{1}^{k}e_{0}$$
$$e$$
$$v_{k} -u = B_{2}^{k}e_{0},$$
$$e$$
