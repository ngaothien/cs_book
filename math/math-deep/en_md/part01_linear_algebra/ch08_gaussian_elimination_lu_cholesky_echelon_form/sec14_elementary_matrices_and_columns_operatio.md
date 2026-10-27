# Elementary Matrices and Columns Operations


<!-- PAGE 318 -->
and since each row (and column) sums to the same number, this common value (the magic sum) is
$$\frac{n(n^{2}+ 1)}{2} .$$
It is easy to see that there are no normal magic squares for $n = 2$. For $n = 3$, the magic sum is $15$, for $n = 4$, it is $34$, and for $n = 5$, it is $65$. In the case $n = 3$, we have the additional condition that the rows and columns add up to $15$, so we end up with a solution parametrized by two numbers $x_{1}, x_{2}$; namely,
$$\begin{pmatrix} x_{1} + x_{2} -5 & 10 -x_{2} & 10 -x_{1} \\ 20 -2x_{1} -x_{2} & 5 & 2x_{1} + x_{2} -10 \\ x_{1} & x_{2} & 15 & x_{1} & x_{2} \end{pmatrix} .$$
$$- -$$
Thus, in order to find a normal magic square, we have the additional inequality constraints
$$x_{1} + x_{2} > 5$$
$$x_{1} < 10$$
$$x_{2} < 10$$
$$2x_{1} + x_{2} < 20$$
$$2x_{1} + x_{2} > 10$$
$$x_{1} > 0$$
$$x_{2} > 0$$
$$x_{1} + x_{2} < 15,$$
and all $9$ entries in the matrix must be distinct. After a tedious case analysis, we discover the remarkable fact that there is a unique normal magic square (up to rotations and reflections):
$$\begin{pmatrix} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{pmatrix} .$$
It turns out that there are $880$ different normal magic squares for $n = 4$, and $275, 305, 224$ normal magic squares for $n = 5$ (up to rotations and reflections). Even for $n = 4$, it takes a fair amount of work to enumerate them all! Finding the number of magic squares for $n > 5$ is an open problem!

## 8.14 Elementary Matrices and Columns Operations

Instead of performing elementary row operations on a matrix $A$, we can perform elementary columns operations, which means that we multiply $A$ by elementary matrices on the right. As elementary row and column operations, P(i, $k), E_{i,j;\beta}, E_{i,\lambda}$ perform the following actions:
