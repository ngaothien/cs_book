# Ky Fan Norms and Schatten Norms


<!-- PAGE 763 -->
can also be used to determine the rank of a matrix when other methods such as Gaussian elimination produce very small pivots. One of the main applications of the SVD is the computation of the pseudo-inverse. Pseudo-inverses are the key to the solution of various optimization problems, in particular the method of least squares. This topic is discussed in the next chapter (Chapter $23)$. Applications of the material of this chapter can be found in Strang $[176, 175]$; Ciarlet $[41]$; Golub and Van Loan $[83]$, which contains many other references; Demmel $[48]$; and Trefethen and Bau $[182]$.

## 22.5 Ky Fan Norms and Schatten Norms

The singular values of a matrix can be used to define various norms on matrices which have found recent applications in quantum information theory and in spectral graph theory. Following Horn and Johnson $[99]$ (Section 3.4) we can make the following definitions:

> **Definition 22.5.** For any matrix $A \in M_{m,n}(\mathbb{C})$, let $q = min{m, n}$, and if $\sigma_{1}  \ge \cdots  \ge \sigma_{q}$  are the singular values of $A$, for any $k$ with $1 \le k \le q$, let
$$N_{k}(A) = \sigma_{1}  + \cdots  + \sigma_{k} ,$$
called the Ky Fan k-norm of $A$. More generally, for any $p \ge 1$ and any $k$ with $1 \le k \le q$, let
$$N_{k;p}(A) = (\sigma_{1}^{p}  + \cdots  + \sigma_{k}^{p} )^{1/p},$$
called the Ky Fan p-k-norm of $A$. When $k = q, N_{q;p}$ is also called the Schatten p-norm. Observe that when $k = 1, N_{1}(A) = \sigma_{1}$ , and the Ky Fan norm $N_{1}$ is simply the spectral norm from Chapter $9$, which is the subordinate matrix norm associated with the Euclidean norm. When $k = q$, the Ky Fan norm $N_{q}$ is given by
$$N_{q}(A) = \sigma_{1}  + \cdots  + \sigma_{q}  = \mathrm{tr}((A^{*}A)^{1/2})$$
and is called the trace norm or nuclear norm. When $p = 2$ and $k = q$, the Ky Fan $N_{q;2}$ norm is given by
$$p$$
$$N_{k;2}(A) = (\sigma_{1}^{2}  + \cdots  + \sigma_{q}^{2} )^{1/2}=\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} \|A\|_{F} ,$$
which is the Frobenius norm of $A$. It can be shown that $N_{k}$ and $N_{k;p}$ are unitarily invariant norms, and that when $m = n$, they are matrix norms; see Horn and Johnson $[99]$ (Section 3.4, Corollary 3.4.4 and Problem $3)$.
