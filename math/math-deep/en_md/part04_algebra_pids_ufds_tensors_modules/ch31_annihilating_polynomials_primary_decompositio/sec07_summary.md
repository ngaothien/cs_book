# Summary


<!-- PAGE 1128 -->
we obtain
$$tB = t \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} = 3tI_{3} + \begin{pmatrix} 0 & t & 0 \\ 0 & 0 & t \\ 0 & 0 & 0 \end{pmatrix}$$
and so
$$e^{tB} = \begin{pmatrix} e^{3t} & 0 & 0 \\ 0 & e^{3t} & 0 \\ 0 & 0 & e^{3t} \end{pmatrix} \begin{pmatrix} 1 & t & (1/2)t^{2} \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{3t} & te^{3t} & (1/2)t^{2}e^{3t} \\ 0 & e^{3t} & te^{3t} \\ 0 & 0 & e^{3t} \end{pmatrix} .$$
The columns of $e^{tB}$ form a basis of the space of solutions of the system of linear differential equations
$$\frac{dY_{1}}{dt} = 3Y_{1} + Y_{2}$$
$$\frac{dY_{2}}{dt} = 3Y_{2} + Y_{3}$$
$$\frac{dY_{3}}{dt} = 3Y_{3},$$
in matrix form,
$$\begin{pmatrix} dY\overline{1} \\ \overline{dt} \\ dY\overline{2} \\ \overline{dt} \\ dY\overline{3} \end{pmatrix} = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} Y_{1} \\ Y_{2} \\ Y_{3} \end{pmatrix} .$$
$$\overline{dt}$$
Explicitly, the general solution of the above system is
$$\begin{pmatrix} Y_{1} \\ Y_{2} \\ Y_{3} \end{pmatrix} = c_{1} \begin{pmatrix} e^{3t} \\ 0 \\ 0 \end{pmatrix} + c_{2} \begin{pmatrix} te^{3t} \\ e^{3t} \\ 0 \end{pmatrix} + c_{3} \begin{pmatrix} (1/2)t^{2}e^{3t} \\ te^{3t} \\ e^{3t} \end{pmatrix} ,$$
with $c_{1}, c_{2}, c_{3} \in \mathbb{R}$. Solving systems of first-order linear differential equations is discussed in Artin $[7]$ and more extensively in Hirsh and Smale $[96]$.

## 31.7 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Ideals, principal ideals, greatest common divisors. $\bullet$  Monic polynomial, irreducible polynomial, relatively prime polynomials. $\bullet$  Annihilator of a linear map. $\bullet$  Minimal polynomial of a linear map.
