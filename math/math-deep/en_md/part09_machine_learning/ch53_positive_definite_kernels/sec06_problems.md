# Problems


<!-- PAGE 1965 -->

## 53.6 Problems

Problem 53.1. Referring back to Example 53.3, prove that if $\phi_{1}$  : $X \to \mathbb{R}_{1}^{n}$ and $\phi_{2}$  : $X \to \mathbb{R}_{2}^{n}$ are two feature maps and if $\kappa_{1} (x, y) = \langle \phi_{1} (x), \phi_{1} (y)\rangle$ and $\kappa_{2} (x, y) = \langle \phi_{2} (x), \phi_{2} (y)\rangle$ are the corresponding kernel functions, then the map defined by
$$\kappa (x, y) = \kappa_{1} (x, y)\kappa_{2} (x, y)$$
$$\mathbb{R}_{1}^{n} \times \mathbb{R}_{2}^{n}$$
is a kernel function, for the feature space and the feature map
$$\phi (x)_{(i,j)} = (\phi_{1} (x))_{i}(\phi_{2} (x))_{j},1 \le i \le n_{1}, 1 \le j \le n_{2}.$$
Problem 53.2. Referring back to Example 53.3, prove that the feature embedding $\phi$ : $X \to \mathbb{R}(_{m}^{n+m-1})$
$$given by$$
$$1/2$$
$$\phi_{(i1,...,in)} (x) = \begin{pmatrix} m \\ i_{1} \cdots  i_{n} \end{pmatrix} (\phi_{1} (x))_{1}^{i1} (\phi_{1} (x))_{1}^{i2} \cdots  (\phi_{1} (x))_{1}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} = m, i_{j} \in \mathbb{N},$$
where the $n$-tuples $(i_{1}, \dots  , i_{n})$ are ordered lexicographically, defines the kernel function $\kappa$ given by $\kappa (x, y) = (\kappa_{1} (x, y))^{m}$.
Problem 53.3. In Example 53.6, prove that for any two subsets $A_{1}$ and $A_{2}$ of $D$,
$$\langle \phi (A_{1}), \phi (A_{2})\rangle = 2^{|A1\cap A2|},$$
the number of common subsets of $A_{1}$ and $A_{2}$.
Problem 53.4. Prove that the pointwise limit of positive definite kernels is also a positive definite kernel.
Problem 53.5. Prove that if $\kappa_{1}$  is a positive definite kernel, then
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\kappa1(x,x)+\kappa1(y,y2)-2\kappa1(x,y)}$$
is a positive definite kernel.

<!-- PAGE 1966 -->
