# Multiresolution Signal Analysis with Haar Bases


<!-- PAGE 162 -->
It can be shown that $\otimes$ is associative and that
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
whenever AC and BD are well defined. Then it is immediately verified that $W_{n}$ is given by the following neat recursive equations:
$$W_{n} = \begin{pmatrix} 1 \\ W_{n-1} \otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
with $W_{0} = (1)$. If we let
$$B_{1} = 2 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$
and for $n \ge 1$,
$$B_{n+1} = 2 \begin{pmatrix} B_{n} & 0 \\ 0 & I_{2n} \end{pmatrix} ,$$
then it is not hard to use the Kronecker product formulation of $W_{n}$ to obtain a rigorous proof of the equation
$$W_{n}^{\top}  W_{n} = B_{n},for all n \ge 1.$$
The above equation offers a clean justification of the fact that the columns of $W_{n}$ are pairwise orthogonal. Observe that the right block (of size $2^{n} \times  2^{n-1})$ shows clearly how the detail coefficients in the second half of the vector $c$ are added and subtracted to the entries in the first half of the partially reconstructed vector after $n$ - $1$ steps.

## 5.4 Multiresolution Signal Analysis with Haar Bases

An important and attractive feature of the Haar basis is that it provides a multiresolution analysis of a signal. Indeed, given a signal $u$, if $c = (c_{1}, \dots  , c_{2n})$ is the vector of its Haar coefficients, the coefficients with low index give coarse information about $u$, and the coefficients with high index represent fine information. For example, if $u$ is an audio signal corresponding to a Mozart concerto played by an orchestra, $c_{1}$ corresponds to the “background noise,” $c_{2}$ to the bass, $c_{3}$ to the first cello, $c_{4}$ to the second cello, $c_{5}, c_{6}, c_{7}, c_{7}$ to the violas, then the violins, etc. This multiresolution feature of wavelets can be exploited to compress a signal, that is, to use fewer coefficients to represent it. Here is an example. Consider the signal
$$u = (2.4, 2.2, 2.15, 2.05, 6.8, 2.8, -1.1, -1.3),$$
whose Haar transform is
$$c = (2, 0.2, 0.1, 3, 0.1, 0.05, 2, 0.1).$$

<!-- PAGE 163 -->
The piecewise-linear curves corresponding to $u$ and $c$ are shown in Figure 5.6. Since some of the coefficients in $c$ are small (smaller than or equal to 0.2) we can compress $c$ by replacing them by $0$. We get
$$c_{2} = (2, 0, 0, 3, 0, 0, 2, 0),$$
and the reconstructed signal is
$$u_{2} = (2, 2, 2, 2, 7, 3, -1, -1).$$
The piecewise-linear curves corresponding to $u_{2}$ and $c_{2}$ are shown in Figure 5.7.
$$73$$
$$6$$
$$2.5$$
$$5$$
$$42$$
$$3$$
$$1.5$$
$$2$$
$$11$$
$$0$$
$$0.5$$
$$1$$
$$20\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.6: A signal and its Haar transform.$$
$$73$$
$$6$$
$$2.5$$
$$5$$
$$2$$
$$4$$
$$31.5$$
$$2$$
$$1$$
$$1$$
$$0.5$$
$$0$$
$$1\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 10\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.7: A compressed signal and its compressed Haar transform.$$
An interesting (and amusing) application of the Haar wavelets is to the compression of audio signals. It turns out that if your type load handel in Matlab an audio file will be loaded in a vector denoted by $y$, and if you type sound(y), the computer will play this piece of music. You can convert $y$ to its vector of Haar coefficients $c$. The length of $y$ is $73113$,
