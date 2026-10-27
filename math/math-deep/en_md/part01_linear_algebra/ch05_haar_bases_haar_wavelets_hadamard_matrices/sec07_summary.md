# Summary


<!-- PAGE 173 -->
such a way that it is an orthogonal Hilbert basis of the Hilbert space $L^{2}([0, 1)]$; see Seberry, Wysocki and Wysocki $[160]$. The Sylvester–Hadamard matrix $H_{2m}$ plays a role in various algorithms for dimension reduction and low-rank matrix approximation. There is a type of structured dimensionreduction map known as the subsampled randomized Hadamard transform, for short SRHT; see Tropp $[183]$ and Halko, Martinsson and Tropp $[89]$. For $\ell \ll n = 2^{m}$, an SRHT matrix is an $\ell \times  n$ matrix of the form
$$r$$
$$\Phi  = \frac{\overline{n}}{\ell} RHD,$$
where $1. D$ is a random $n \times  n$ diagonal matrix whose entries are independent random signs. $2. H = n^{-1/2}H_{n}$, a normalized Sylvester–Hadamard matrix of dimension $n. 3. R$ is a random $\ell \times  n$ matrix that restricts an $n$-dimensional vector to $\ell$ coordinates, chosen uniformly at random.
$$It is explained \frac{inTropp[}{n^{-1}\log(n} 183] that for any input x such that \|x\|_{2} = 1, the probability$$
that $|(HDx)_{i}| \ge p$ ) for any $i$ is quite small. Thus HD has the effect of “flattening” the input $x$. The main result about the SRHT is that it preserves the geometry of an entire subspace of vectors; see Tropp $[183]$ (Theorem 1.3).

## 5.7 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Haar basis vectors and a glimpse at Haar wavelets. $\bullet$  Kronecker product (or tensor product) of matrices. $\bullet$  Hadamard and Sylvester–Hadamard matrices. $\bullet$  Walsh functions.
