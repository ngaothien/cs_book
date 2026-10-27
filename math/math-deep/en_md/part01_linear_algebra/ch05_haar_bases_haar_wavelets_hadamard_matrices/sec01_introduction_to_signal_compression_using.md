# Introduction to Signal Compression Using Haar Wavelets


<!-- PAGE 153 -->
Chapter $5$ Haar Bases, Haar Wavelets, Hadamard Matrices In this chapter, we discuss two types of matrices that have applications in computer science and engineering:
$(1)$ Haar matrices and the corresponding Haar wavelets, a fundamental tool in signal processing and computer graphics. $2)$ Hadamard matrices which have applications in error correcting codes, signal processing, and low rank approximation.

## 5.1 Introduction to Signal Compression Using Haar

$$Wavelets$$
We begin by considering Haar wavelets in $\mathbb{R}^{4}$. Wavelets play an important role in audio and video signal processing, especially for compressing long signals into much smaller ones that still retain enough information so that when they are played, we can’t see or hear any difference. Consider the four vectors $w_{1}, w_{2}, w_{3}, w_{4}$ given by
$$w_{1} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} w_{2} = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} w_{3} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix} w_{4} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} .$$
$$--$$
Note that these vectors are pairwise orthogonal, which means that their inner product is $0$ (see Section 12.1, Example 12.1, and Section 12.2, Definition 12.2), so they are indeed linearly independent (see Proposition 12.4). Let $\mathcal{W} = {w_{1}, w_{2}, w_{3}, w_{4}}$ be the Haar basis, and let
$$153$$

<!-- PAGE 154 -->
$\mathcal{U} = {e_{1}, e_{2}, e_{3}, e_{4}}$ be the canonical basis $of\mathbb{R}^{4}$. The change of basis matrix $W = P_{W,U}$ from $\mathcal{U}$ to $\mathcal{W}$ is given by
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
and we easily find that the inverse of $W$ is given by
$$W^{-1}  = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$-$$
Observe that the second matrix in the above product is $W^{\top}$ and the first matrix in this product is $(W^{\top} W)^{-1}$. So the vector $v = (6, 4, 5, 1)$ over the $basis\mathcal{U}$ becomes $c = (c_{1}, c_{2}, c_{3}, c_{4})$ over the Haar basis $\mathcal{W}$, with
$$\begin{pmatrix} c_{1} \\ c_{2} \\ c_{3} \\ c_{4} \end{pmatrix} = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 6 \\ 4 \\ 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 1 \\ 2 \end{pmatrix} .$$
$$-$$
Given a signal $v = (v_{1}, v_{2}, v_{3}, v_{4})$, we first transform $v$ into its coefficients $c = (c_{1}, c_{2}, c_{3}, c_{4})$ over the Haar basis by computing $c = W^{-1} v$. Observe that
$$c_{1} = \frac{v_{1} + v_{2} + v_{3} + v_{4}}{4}$$
is the overall average value of the signal $v$. The coefficient $c_{1}$ corresponds to the background of the image (or of the sound). Then, $c_{2}$ gives the coarse details of $v$, whereas, $c_{3}$ gives the details in the first part of $v$, and $c_{4}$ gives the details in the second half of $v$. Reconstruction of the signal consists in computing $v =$ Wc. The trick for good compression is to throw away some of the coefficients of $c$ (set them to zero), obtaining a compressed signal $c$, and still retain enough crucial information so that the reconstructed signal $v =$ Wc $b  b b$ looks almost as good as the original signal $v$. Thus, the steps are: input $v \longrightarrow$ coefficients $c = W^{-1} v \longrightarrow$ compressed $c \longrightarrow$ compressed $v =$ Wc.
$$b bb$$
This kind of compression scheme makes modern video conferencing possible. It turns out that there is a faster way to find $c = W^{-1} v$, without actually using $W^{-1}$ . This has to do with the multiscale nature of Haar wavelets. Given the original signal $v = (6, 4, 5, 1)$ shown in Figure 5.1, we compute averages and half differences obtaining Figure 5.2. We get the coefficients $c_{3} = 1$ and $c_{4} = 2$. Then
