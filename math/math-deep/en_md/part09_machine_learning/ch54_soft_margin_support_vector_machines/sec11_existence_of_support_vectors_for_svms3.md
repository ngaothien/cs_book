# Existence of Support Vectors for (SVMs3)


<!-- PAGE 2031 -->
Note that if $\nu$  is chosen so that $\nu  < 1/(p + q)$, then $p_{f} = q_{f} = 0$, which means that none of the data points are misclassified; in other words, the $u_{i}s$ and $v_{j}s$ are linearly separable. Thus we see that if the $u_{i}s$ and $v_{j}s$ are not linearly separable we must pick $\nu$  such that $1/(p + q) \le \nu  \le 1$ for the method to succeed. In fact, by Proposition 54.5, we must choose $\nu$  so that
$$\frac{p_{f}+ q_{f}}{p + q} \le \nu  \le \frac{p_{m} + q_{m}}{p + q} .$$
Furthermore, in order to be able to determine $b$, we must have the strict inequality
$$\frac{p_{f}+ q_{f}}{p + q} < \nu .$$

## 54.11 Existence of Support Vectors for (SVM )

$$s3$$
The following proposition is the version of Proposition 54.2 for Problem $(SVM_{s3})$.

> **Proposition 54.6.** For every optimal solution $(w, b, \eta , \epsilon , \xi$ ) of Problem $(SVM_{s3})$ with $w \neq  0$ and $\eta  > 0$, if $\nu  < 1$ and if no $u_{i}$ is a support vector and no $v_{j}$ is a support vector, then there is another optimal solution such that some $u_{i0}$ or some $v_{j0}$ is a support vector.

*Proof.* We may assume that $K_{s} = 1/(p + q)$ and we proceed by contradiction. Thus we assume that for all $i \in {1, \dots  , p}$, if $\epsilon_{i}  = 0$, then the constraint $w^{\top}u_{i}$ - $b \ge \eta$  is not active, namely $w^{\top}u_{i} -b > \eta$ , and for all $j \in {1, \dots  , q}$, if $\xi_{j}  = 0$, then the constraint $-w^{\top}v_{j} +b \ge \eta$ is not active, namely $-w^{\top}v_{j} + b > \eta$ . Let $E_{\lambda} = {i \in {1, \dots  , p}$ | $\epsilon_{i}  > 0}$ and let $E_{\mu} = {j \in {1, \dots  , q}$ | $\xi_{j}  > 0}$. By definition, $p_{sf} = |E_{\lambda}|, q_{sf} = |E_{\mu}|, p_{sf} \le p_{f}$ and $q_{sf} \le q_{f}$, so by Proposition 54.1,
$$\frac{p_{sf}+ q_{sf}}{p + q} \le \frac{p_{f}+ q_{f}}{p + q} \le \nu .$$
Therefore, if $\nu  < 1$, then $p_{sf} + q_{sf} < p + q$, which implies that either there is some $i \in / E_{\lambda}$ such that $\epsilon_{i}  = 0$ or there is some $j \in / E_{\mu}$ such that $\xi_{j}  = 0$. By complementary slackness all the constraints for which $i \in E_{\lambda}$ and $j \in E_{\mu}$ are active, so our hypotheses are
$$w^{\top}u_{i} -b = \eta  -\epsilon_{i} \epsilon_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}v_{j} + b = \eta  -\xi_{j} \xi_{j}  > 0j \in E_{\mu}$$
$$w^{\top}u_{i} -b > \eta i \in /E_{\lambda}$$
$$-w^{\top}v_{j} + b > \eta j \in /E_{\mu},$$
and either there is some $i \in / E_{\lambda}$ or there is some $j \in / E_{\mu}$. Our strategy, as illustrated in Figures 54.8 and 54.9, is to increase the width $\eta$  of the slab keeping the separating hyperplane unchanged. Let us pick $\theta$  such that
$$\theta  = \min{w^{\top}u_{i} -b -\eta , -w^{\top}v_{j} + b -\eta  | i \in /E_{\lambda}, j \in /E_{\mu}}.$$

<!-- PAGE 2032 -->
Our hypotheses imply that $\theta  > 0$. We can write
$$w^{\top}u_{i} -b = \eta  + \theta  -(\epsilon_{i}  + \theta )\epsilon_{i}  + \theta  > 0i \in E_{\lambda}$$
$$-w^{\top}v_{j} + b = \eta  + \theta  -(\xi_{j}  + \theta )\xi_{j}  + \theta  > 0j \in E_{\mu}$$
$$w^{\top}u_{i} -b \ge \eta  + \theta i \in /E_{\lambda}$$
$$-w^{\top}v_{j} + b \ge \eta  + \theta j \in /E_{\mu},$$
and by the choice of $\theta$ , either
$$w^{\top}u_{i} -b = \eta  + \theta for some i \in /E_{\lambda}$$
or
$$-w^{\top}v_{j} + b = \eta  + \theta for some j \in /E_{\mu}.$$
The original value of the objective function is
$$\omega (0) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu \eta  + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  ,$$
$$\begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix}$$
and the new value is
$$\omega (\theta ) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu (\eta  + \theta ) + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}$$
$$\begin{pmatrix} (\epsilon_{i}  + \theta ) + & (\xi_{j} + \theta ) \\  & p_{sf}+ \end{pmatrix}$$
$$= \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu \eta  + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  - \begin{pmatrix} q_{sf} \\ \nu  - \\ p + q \end{pmatrix} \theta .$$
$$\begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix}$$
By Proposition 54.1,
$$\frac{p_{sf}+ q_{sf}}{p + q} \le \frac{p_{f}+ q_{f}}{p + q} \le \nu ,$$
so
$$\nu  - \frac{p_{sf}+ q_{sf}}{p + q} \ge 0,$$
and so $\omega (\theta$ ) $\le \omega (0)$. If the inequality is strict, then this contradicts the optimality of the original solution. Therefore, $\omega (\theta$ ) $= \omega (0)$ and $(w, b, \eta  + \theta , \epsilon  + \theta , \xi  + \theta$ ) is an optimal solution such that either
$$w^{\top}u_{i} -b = \eta  + \theta for some i \in /E_{\lambda}$$
or
$$-w^{\top}v_{j} + b = \eta  + \theta for some j \in /E_{\mu},$$
as desired. Proposition 54.6 cannot be strengthened to claim that there is some support vector $u_{i0}$ and some support vector $v_{j0}$. We found examples for which the above condition fails for $\nu$ large enough. The proof of Proposition 54.6 reveals that $(p_{sf} + q_{sf})/(p + q)$ is a critical value for $\nu$ . if this value is avoided we have the following corollary.
