# Making the QR Method More Efficient Using Shifts


<!-- PAGE 675 -->

## 18.3 Making the QR Method More Efficient

$$Using Shifts$$
To improve efficiency and cope with pairs of complex conjugate eigenvalues in the case of real matrices, the following steps are taken:
$(1)$ Initially reduce the matrix $A$ to upper Hessenberg form, as $A = UHU^{*}$ . Then apply the QR-algorithm to $H$ (actually, to its unreduced Hessenberg blocks). It is easy to see that the matrices $H_{k}$ produced by the QR algorithm remain upper Hessenberg.
$(2)$ To accelerate convergence, use shifts, and to deal with pairs of complex conjugate eigenvalues, use double shifts.
$(3)$ Instead of computing a QR-factorization explicitly while doing a shift, perform an implicit shift which computes $A_{k+1} = Q_{k}^{*}A_{k}Q_{k}$ without having to compute a QRfactorization (of $A_{k}$ - $\sigma_{k}$ I), and similarly in the case of a double shift. This is the most intricate modification of the basic QR algorithm and we will not discuss it here. This method is usually referred as bulge chasing. Details about this technique for real matrices can be found in Demmel $[48]$ (Section 4.4.8) and Golub and Van Loan $[83]$ (Section 7.5). Watkins discusses the QR algorithm with shifts as a bulge chasing method in the more general case of complex matrices $[193, 194]$. Let us repeat an important remark made in the previous section. If we start with a matrix $H$ in upper Hessenberg form, if at any stage of the QR algorithm we find that some subdiagonal entry $(H_{k})_{p+1p} = 0$ or is very small, then $H_{k}$ is of the form
$$H_{k} = \begin{pmatrix} H_{11} & H_{12} \\ 0 & H_{22} \end{pmatrix} ,$$
where both $H_{11}$ and $H_{22}$ are upper Hessenberg matrices (with $H_{11}$ a $p \times  p$ matrix and $H_{22}$ a $(n$ - $p) \times  (n$ - $p)$ matrix), and the eigenvalues of $H_{k}$ are the eigenvalues of $H_{11}$ and $H_{22}$. For example, in the matrix
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} ,$$
$$*$$
if $h_{43} = 0$, then we have the block matrix
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & 0 & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$

<!-- PAGE 676 -->
Then we can recursively apply the QR algorithm to $H_{11}$ and $H_{22}$. In particular, if $(H_{k})_{nn-1} = 0$ or is very small, then $(H_{k})_{nn}$ is a good approximation of an eigenvalue, so we can delete the last row and the last column of $H_{k}$ and apply the QR algorithm to this submatrix. This process is called deflation. If $(H_{k})_{n-1n-2} = 0$ or is very small, then the $2 \times  2$ “corner block”
$$\begin{pmatrix} (H_{k})_{n-1n-1} & (H_{k})_{n-1n} \\ (H_{k})_{nn-1} & (H_{k})_{nn} \end{pmatrix}$$
appears, and its eigenvalues can be computed immediately by solving a quadratic equation. Then we deflate $H_{k}$ by deleting its last two rows and its last two columns and apply the QR algorithm to this submatrix. Thus it would seem desirable to modify the basic QR algorithm so that the above situations arises, and this is what shifts are designed for. More precisely, under the hypotheses of Theorem 18.1, it can be shown (see Ciarlet $[41]$, Section 6.3) that the entry $(A_{k})_{ij}$ with $i > j$ converges to $0$ as $|\lambda_{i} /\lambda_{j} |^{k}$ converges to $0$. Also, if we let $r_{i}$ be defined by
$$







$$
$$r_{1} = \frac{\lambda_{2}}{\lambda_{1}} ,r_{i} = \max \frac{\lambda_{i}}{\lambda_{i-1}} , \frac{\lambda_{i+1}}{\lambda_{i}} ,2 \le i \le n -1,r_{n} = \frac{\lambda_{n}}{\lambda_{n-1}} ,$$
then there is a constant $C$ (independent of $k)$ such that
$$|(A_{k})_{ii} -\lambda_{i} | \le Cr_{i}^{k} ,1 \le i \le n.$$
In particular, if $H$ is upper Hessenberg, then the entry $(H_{k})_{i+1i}$ converges to $0$ as $|\lambda_{i+1} /\lambda_{i} |^{k}$ converges to $0$. Thus if we pick $\sigma_{k}$  close to $\lambda_{i}$ , we expect that $(H_{k}$ - $\sigma_{k} I)_{i+1i}$ converges to $0$ as $|(\lambda_{i+1}  -\sigma_{k} )/(\lambda_{i}  -\sigma_{k} )|^{k}$ converges to $0$, and this ratio is much smaller than $1$ as $\sigma_{k}$  is closer to $\lambda_{i}$ . Typically, we apply a shift to accelerate convergence to $\lambda_{n}$  (so $i = n$ - $1)$. In this case, both $(H_{k} -\sigma_{k} I)_{nn-1}$ and $|(H_{k} -\sigma_{k} I)_{nn} -\lambda_{n}$ | converge to $0$ as $|(\lambda_{n}  -\sigma_{k} )/(\lambda_{n-1}  -\sigma_{k} )|^{k}$ converges to $0$. A shift is the following modified QR-steps (switching back to an arbitrary matrix $A$, since the shift technique applies in general). Pick some $\sigma_{k}$ , hopefully close to some eigenvalue of $A$ (in general, $\lambda_{n}$ ), and QR-factor $A_{k}$ - $\sigma_{k}$ I as
$$A_{k} -\sigma_{k} I = Q_{k}R_{k},$$
and then form
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I.$$
Since
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I$$
$$= Q_{k}^{*}Q_{k}R_{k}Q_{k} + Q_{k}^{*}Q_{k}\sigma_{k}$$
$$= Q_{k}^{*}(Q_{k}R_{k} + \sigma_{k} I)Q_{k}$$
$$= Q_{k}^{*}A_{k}Q_{k},$$

<!-- PAGE 677 -->
$A_{k+1}$ is similar to $A_{k}$, as before. If $A_{k}$ is upper Hessenberg, then it is easy to see that $A_{k+1}$ is also upper Hessenberg. If $A$ is upper Hessenberg and if $\sigma_{i}$  is exactly equal to an eigenvalue, then $A_{k}$ - $\sigma_{k}$ I is singular, and forming the QR-factorization will detect that $R_{k}$ has some diagonal entry equal to $0$. Assuming that the QR-algorithm returns $(R_{k})_{nn} = 0$ (if not, the argument is easily adapted), then the last row of $R_{k}Q_{k}$ is $0$, so the last row of $A_{k+1} = R_{k}Q_{k} + \sigma_{k}$ I ends with $\sigma_{k}$  (all other entries being zero), so we are in the case where we can deflate $A_{k}$ (and $\sigma_{k}$  is indeed an eigenvalue). The question remains, what is a good choice for the shift $\sigma_{k}$ ? Assuming again that $H$ is in upper Hessenberg form, it turns out that when $(H_{k})_{nn-1}$ is small enough, then a good choice for $\sigma_{k}$  is $(H_{k})_{nn}$. In fact, the rate of convergence is quadratic, which means roughly that the number of correct digits doubles at every iteration. The reason is that shifts are related to another method known as inverse iteration, and such a method converges very fast. For further explanations about this connection, see Demmel $[48]$ (Section 4.4.4) and Trefethen and Bau $[182]$ (Lecture $29)$. One should still be cautious that the QR method with shifts does not necessarily converge, and that our convergence proof no longer applies, because instead of having the identity $A^{k} = P_{k}\mathcal{R}_{k}$, we have
$$(A -\sigma_{k} I) \cdots  (A -\sigma_{2} I)(A -\sigma_{1} I) = P_{k}\mathcal{R}_{k}.$$
Of course, the QR algorithm loops immediately when applied to an orthogonal matrix $A$. This is also the case when $A$ is symmetric but not positive definite. For example, both the QR algorithm and the QR algorithm with shifts loop on the matrix
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .$$
In the case of symmetric matrices, Wilkinson invented a shift which helps the QR algorithm with shifts to make progress. Again, looking at the lower corner of $A_{k}$, say
$$B = \begin{pmatrix} a_{n-1} & b_{n-1} \\ b_{n-1} & a_{n} \end{pmatrix} ,$$
the Wilkinson shift picks the eigenvalue of $B$ closer to $a_{n}$. If we let
$$-$$
$$\delta  = \frac{a_{n-1}a_{n}}{2} ,$$
it is easy to see that the eigenvalues of $B$ are given by
$$q$$
$$\lambda  = \frac{a_{n} + a_{n-1}}{2} \pm \delta^{2}  + b_{n-1}^{2}.$$

<!-- PAGE 678 -->
It follows that
$$q$$
$$\lambda  -a_{n} = \delta  \pm \delta^{2} + b_{n-1}^{2},$$
and from this it is easy to see that the eigenvalue closer to $a_{n}$ is given by
$$\mu  = a_{n} - \frac{sign(\delta )b_{n-1}^{2}}{(|\delta | +p\overline{\delta}^{2}\overline{+}\overline{b}_{n-1}^{2})} .$$
If $\delta  = 0$, then we pick arbitrarily one of the two eigenvalues. Observe that the Wilkinson shift applied to the matrix
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
is either $+1$ or $-1$, and in one step, deflation occurs and the algorithm terminates successfully. We now discuss double shifts, which are intended to deal with pairs of complex conjugate eigenvalues. Let us assume that $A$ is a real matrix. For any complex number $\sigma_{k}$  with nonzero imaginary part, a double shift consists of the following steps:
$$A_{k} -\sigma_{k} I = Q_{k}R_{k}$$
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I$$
$$A_{k+1} -\overline{\sigma}_{k}I = Q_{k+1}R_{k+1}$$
$$A_{k+2} = R_{k+1}Q_{k+1} +\overline{\sigma}_{k}I.$$
From the computation made for a single shift, we have $A_{k+1} = Q_{k}^{*}A_{k}Q_{k}$ and $A_{k+2} = Q_{k+1}^{*}A_{k+1}Q_{k+1}$, so we obtain
$$A_{k+2} = Q_{k+1}^{*}Q_{k}^{*}A_{k}Q_{k}Q_{k+1}.$$
The matrices $Q_{k}$ are complex, so we would expect that the $A_{k}$ are also complex, but remarkably we can keep the products $Q_{k}Q_{k+1}$ real, and so the $A_{k}$ also real. This is highly desirable to avoid complex arithmetic, which is more expensive. Observe that since
$$Q_{k+1}R_{k+1} = A_{k+1} -\overline{\sigma}_{k}I = R_{k}Q_{k} + (\sigma_{k}  -\overline{\sigma}_{k})I,$$
we have
$$Q_{k}Q_{k+1}R_{k+1}R_{k} = Q_{k}(R_{k}Q_{k} + (\sigma_{k}  -\overline{\sigma}_{k})I)R_{k}$$
$$= Q_{k}R_{k}Q_{k}R_{k} + (\sigma_{k}  -\overline{\sigma}_{k})Q_{k}R_{k}$$
$$= (A_{k} -\sigma_{k} I)^{2}+ (\sigma_{k}  -\overline{\sigma}_{k})(A_{k} -\sigma_{k} I)$$
$$= A_{k}^{2} -2(\mathcal{ℜ}\sigma_{k} )A_{k} + |\sigma_{k} |^{2}I.$$

<!-- PAGE 679 -->
If we assume by induction that matrix $A_{k}$ is real (with $k = 2\ell +1, \ell \ge 0)$, then the matrix $S = A_{k}^{2}$ - $2(\mathcal{ℜ}\sigma_{k} )A_{k} + |\sigma_{k} |^{2}I$ is also real, and since $Q_{k}Q_{k+1}$ is unitary and $R_{k+1}R_{k}$ is upper triangular, we see that
$$S = Q_{k}Q_{k+1}R_{k+1}R_{k}$$
is a QR-factorization of the real matrix $S$, thus $Q_{k}Q_{k+1}$ and $R_{k+1}R_{k}$ can be chosen to be real matrices, in which case $(Q_{k}Q_{k+1})^{*}$ is also real, and thus
$$A_{k+2} = Q_{k+1}^{*}Q_{k}^{*}A_{k}Q_{k}Q_{k+1} = (Q_{k}Q_{k+1})^{*}A_{k}Q_{k}Q_{k+1}$$
is real. Consequently, if $A_{1} = A$ is real, then $A_{2\ell+1}$ is real for all $\ell \ge 0$. The strategy that consists in picking $\sigma_{k}$  and $\overline{\sigma}_{k}$ as the complex conjugate eigenvalues of the corner block
$$\begin{pmatrix} (H_{k})_{n-1n-1} & (H_{k})_{n-1n} \\ (H_{k})_{nn-1} & (H_{k})_{nn} \end{pmatrix}$$
is called the Francis shift (here we are assuming that $A$ has be reduced to upper Hessenberg form). It should be noted that there are matrices for which neither a shift by $(H_{k})_{nn}$ nor the Francis shift works. For instance, the permutation matrix
$$A = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
has eigenvalues $e^{i2\pi /3}, e^{i4\pi /3}, +1$, and neither of the above shifts apply to the matrix
$$\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .$$
However, a shift by $1$ does work. There are other kinds of matrices for which the QR algorithm does not converge. Demmel gives the example of matrices of the form
$$\begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & h & 0 \\ 0 & -h & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
where $h$ is small. Algorithms implementing the QR algorithm with shifts and double shifts perform “exceptional” shifts every $10$ shifts. Despite the fact that the QR algorithm has been perfected since the 1960’s, it is still an open problem to find a shift strategy that ensures convergence of all matrices. Implicit shifting is based on a result known as the implicit $Q$ theorem. This theorem says that if $A$ is reduced to upper Hessenberg form as $A = UHU^{*}$ and if $H$ is unreduced
