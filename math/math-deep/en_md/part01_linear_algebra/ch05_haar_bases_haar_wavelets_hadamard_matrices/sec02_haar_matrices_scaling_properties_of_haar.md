# Haar Matrices, Scaling Properties of Haar Wavelets


<!-- PAGE 155 -->
$$6451$$
$$Figure 5.1: The original signal v.$$
$$2$$
$$1$$
$$55$$
$$33$$
$$-1$$
$$-2$$
$$Figure 5.2: First averages and first half differences.$$
again we compute averages and half differences obtaining Figure 5.3. We get the coefficients $c_{1} = 4$ and $c_{2} = 1$. Note that the original signal $v$ can be reconstructed from the two signals in Figure 5.2, and the signal on the left of Figure 5.2 can be reconstructed from the two signals in Figure 5.3. In particular, the data from Figure 5.2 gives us
$$-$$
$$5 + 1 = \frac{v_{1} + v_{2}}{2} + \frac{v_{1}v_{2}}{-2} = v_{1}$$
$$5 -1 = \frac{v_{1} + v_{2}}{2} - \frac{v_{1}v_{2}}{-2} = v_{2}$$
$$3 + 2 = \frac{v_{3} + v_{4}}{2} + \frac{v_{3}v_{4}}{-2} = v_{3}$$
$$3 -2 = \frac{v_{3} + v_{4}}{2} - \frac{v_{3}v_{4}}{2} = v_{4}.$$

## 5.2 Haar Bases and Haar Matrices, Scaling Properties

$$of Haar Wavelets$$
The method discussed in Section 5.1 can be generalized to signals of any length $2^{n}$. The previous case corresponds to $n = 2$. Let us consider the case $n = 3$. The Haar basis

<!-- PAGE 156 -->
$$11$$
$$4444$$
$$-1-1$$
$$Figure 5.3: Second averages and second half differences.$$
$(w_{1}, w_{2}, w_{3}, w_{4}, w_{5}, w_{6}, w_{7}, w_{8})$ is given by the matrix
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & -1 & 0 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & 1 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & -1 & 0 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & -1 & 0 \\ 1 & -1 & 0 & -1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
The columns of this matrix are orthogonal, and it is easy to see that
$$W^{-1}= \mathrm{diag}(1/8, 1/8, 1/4, 1/4, 1/2, 1/2, 1/2, 1/2)W^{\top}.$$
A pattern is beginning to emerge. It looks like the second Haar basis vector $w_{2}$ is the “mother” of all the other basis vectors, except the first, whose purpose is to perform averaging. Indeed, in general, given
$$w_{2} = (1, \dots  , 1, -1, \dots  , -1),$$
$$|{z}$$
$$2n$$
the other Haar basis vectors are obtained by a “scaling and shifting process.” Starting from $w_{2}$, the scaling process generates the vectors
$$w_{3}, w_{5}, w_{9}, \dots  , w_{2j+1}, \dots  , w_{2n-1+1},$$
such that $w_{2j+1+1}$ is obtained from $w_{2j+1}$ by forming two consecutive blocks of $1$ and $-1$ of half the size of the blocks in $w_{2j+1}$, and setting all other entries to zero. Observe that $w_{2j+1}$ has $2^{j}$ blocks of $2^{n-j}$ elements. The shifting process consists in shifting the blocks of $1$ and $-1$ in $w_{2j+1}$ to the right by inserting a block of $(k$ - $1)2^{n-j}$ zeros from the left, with $0 \le j \le n -1$ and $1 \le k \le 2^{j}$. Note that our convention is to use $j$ as the scaling index and $k$ as the shifting index. Thus, we obtain the following formula for $w_{2j+k}$:
$$01 \le i \le (k -1)2^{n-j}$$
$$$$
$$$$
$$1(k -1)2^{n-j}+ 1 \le i \le (k -1)2^{n-j}+ 2^{n-j-1}$$
$$$$
$$w_{2j+k}(i) =$$
$$-1(k -1)2^{n-j}+ 2^{n-j-1}+ 1 \le i \le k2^{n-j}$$
$$$$
$$$$
$$0k2^{n-j}+ 1 \le i \le 2^{n},$$
$$$$

<!-- PAGE 157 -->
with $0 \le j \le n$ - $1$ and $1 \le k \le 2^{j}$. Of course
$$w_{1} = (1, \dots  , 1).$$
$$|{z}$$
$$2n$$
The above formulae look a little better if we change our indexing slightly by letting $k$ vary from $0$ to $2^{j}$ - $1$, and using the index $j$ instead of $2^{j}$.

> **Definition 5.1.** The vectors of the Haar basis of dimension $2^{n}$ are denoted by
$$w_{1}, h_{0}^{0}, h_{0}^{1}, h_{1}^{1}, h_{0}^{2}, h_{1}^{2}, h_{2}^{2}, h_{3}^{2}, \dots  , h_{k}^{j}, \dots  , h_{2n-1-1}^{n-1},$$
where
$$01 \le i \le k2^{n-j}$$
$$$$
$$$$
$$1k2^{n-j}+ 1 \le i \le k2^{n-j}+ 2^{n-j-1}$$
$$$$
$$h_{k}^{j}(i) =$$
$$-1k2^{n-j}+ 2^{n-j-1}+ 1 \le i \le (k + 1)2^{n-j}$$
$$$$
$$$$
$$0(k + 1)2^{n-j}+ 1 \le i \le 2^{n},$$
$$$$
with $0 \le j \le n$ - $1$ and $0 \le k \le 2^{j}$ - $1$. The $2^{n} \times  2^{n}$ matrix whose columns are the vectors
$$w_{1}, h_{0}^{0}, h_{0}^{1}, h_{1}^{1}, h_{0}^{2}, h_{1}^{2}, h_{2}^{2}, h_{3}^{2}, \dots  , h_{k}^{j}, \dots  , h_{2n-1-1}^{n-1},$$
(in that order), is called the Haar matrix of dimension $2^{n}$, and is denoted by $W_{n}$. It turns out that there is a way to understand these formulae better if we interpret a vector $u = (u_{1}, \dots  , u_{m})$ as a piecewise linear function over the interval $[0, 1)$.

> **Definition 5.2.** Given a vector $u = (u_{1}, \dots  , u_{m})$, the piecewise linear $function^{1}$ plf(u) is defined such that
$$-$$
$$plf(u)(x) = u_{i}, \frac{i1}{m} \le x < \frac{i}{m} , 1 \le i \le m.$$
In words, the function plf(u) has the value $u_{1}$ on the interval $[0, 1/m)$, the value $u_{2}$ on $[1/m, 2/m)$, etc., and the value $u_{m}$ on the interval $[(m$ - $1)/m, 1)$. For example, the piecewise linear function associated with the vector
$$u = (2.4, 2.2, 2.15, 2.05, 6.8, 2.8, -1.1, -1.3)$$
is shown in Figure 5.4. Then each basis vector $h_{k}^{j}$ corresponds to the function
$$\psi_{k}^{j}  = plf(h_{k}^{j}).$$
$\overline{1}\overline{Piecewise} \overline{constant} \overline{function} \overline{might} \overline{be}$ a more accurate name.

<!-- PAGE 158 -->
$$7$$
$$6$$
$$5$$
$$4$$
$$3$$
$$2$$
$$1$$
$$0$$
$$-1$$
$$-2\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.4: The piecewise linear function plf(u).$$
In particular, for all $n$, the Haar basis vectors
$$h_{0}^{0} = w_{2} = (1, \dots  , 1, -1, \dots  , -1)$$
$$|{z}$$
$$2n$$
yield the same piecewise linear function $\psi$  given by
$$1if0 \le x < 1/2$$
$$$$
$$$$
$$\psi (x) =-1if1/2 \le x < 1$$
$$0otherwise,$$
$$$$
whose graph is shown in Figure 5.5. It is easy to see that $\psi_{k}^{j}$  is given by the simple expression
$$1$$
$$1$$
$$0$$
$$-1$$
$$Figure 5.5: The Haar wavelet \psi .$$
$$\psi_{k}^{j} (x) = \psi (2^{j}x -k),0 \le j \le n -1, 0 \le k \le 2^{j}-1.$$
The above formula makes it clear that $\psi_{k}^{j}$  is obtained from $\psi$  by scaling and shifting.

> **Definition 5.3.** The function $\varphi_{0}^{0}  = plf(w_{1})$ is the piecewise linear function with the constant value $1$ on $[0, 1)$, and the functions $\psi_{k}^{j}  = plf(h_{k}^{j})$ together with $\varphi_{0}^{0}$  are known as the Haar wavelets.

<!-- PAGE 159 -->
Rather than using $W^{-1}$ to convert a vector $u$ to a vector $c$ of coefficients over the Haar basis, and the matrix $W$ to reconstruct the vector $u$ from its Haar coefficients $c$, we can use faster algorithms that use averaging and differencing. If $c$ is a vector of Haar coefficients of dimension $2^{n}$, we compute the sequence of vectors $u^{0}, u^{1}, \dots , u^{n}$ as follows:
$$u^{0}= c$$
$$u^{j+1}= u^{j}$$
$$u^{j+1}(2i -1) = u^{j}(i) + u^{j}(2^{j}+ i)$$
$$u^{j+1}(2i) = u^{j}(i) -u^{j}(2^{j}+ i),$$
for $j = 0, \dots  , n$ - $1$ and $i = 1, \dots  , 2^{j}$. The reconstructed vector (signal) is $u = u^{n}$. If $u$ is a vector of dimension $2^{n}$, we compute the sequence of vectors $c^{n}, c^{n-1}, \dots  , c^{0}$ as follows:
$$c^{n}= u$$
$$c^{j}= c^{j+1}$$
$$c^{j}(i) = (c^{j+1}(2i -1) + c^{j+1}(2i))/2$$
$$c^{j}(2^{j}+ i) = (c^{j+1}(2i -1) -c^{j+1}(2i))/2,$$
for $j = n$ - $1, \dots  , 0$ and $i = 1, \dots  , 2^{j}$. The vector over the Haar basis is $c = c^{0}$. We leave it as an exercise to implement the above programs in Matlab using two variables $u$ and $c$, and by building iteratively $2^{j}$. Here is an example of the conversion of a vector to its Haar coefficients for $n = 3$. Given the sequence $u = (31, 29, 23, 17, -6, -8, -2, -4)$, we get the sequence $c^{3} = (31, 29, 23, 17, -6, -8, -2, -4)$
$$c^{2}= \begin{pmatrix} 31 + 2923 + 17-6 -8-2 -431 -2923 -17-6 -(-8)-2 -(-4) \\ , & , & , & , & , & , & , \\ 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 \end{pmatrix}$$
$= (30, 20, -7, -3, 1, 3, 1, 1)$
$$c^{1}= \begin{pmatrix} 30 + 20-7 -330 -20-7 -(-3) \\ , & , & , & , 1, 3, 1, 1 \\ 2 & 2 & 2 & 2 \end{pmatrix}$$
$= (25, -5, 5, -2, 1, 3, 1, 1)$
$$c^{0}= \begin{pmatrix} 25 -525 -(-5) \\ , & , 5, -2, 1, 3, 1, 1 \\ 2 & 2 \end{pmatrix} = (10, 15, 5, -2, 1, 3, 1, 1)$$
so $c = (10, 15, 5, -2, 1, 3, 1, 1)$. Conversely, given $c = (10, 15, 5, -2, 1, 3, 1, 1)$, we get the
