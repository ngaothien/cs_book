# Affine Hyperplanes


<!-- PAGE 847 -->
$$a$$
$$a$$
$$bb$$
$$d$$
$$c$$
$$c$$
$$Figure 24.25: Desargues’s theorem (affine version).$$
Desargues’s theorem is illustrated in Figure 24.25. There is a fancier version of Desargues’s theorem, but it is easier to prove it using projective geometry. It should be noted that in axiomatic presentations of projective geometry, Desargues’s theorem is related to the associativity of the ground field $K$ (in the present case, $K = \mathbb{R})$. Also, Desargues’s theorem yields a geometric characterization of the affine dilatations. An affine dilatation $f$ on an affine space $E$ is a bijection that maps every line $D$ to a line f(D) parallel to $D$. We leave the proof as an exercise.

## 24.10 Affine Hyperplanes

We now consider affine forms and affine hyperplanes. In Section 24.5 we observed that the set $L$ of solutions of an equation
$$ax + by = c$$
$$\mathbb{A}^{2}$$
is an affine subspace of of dimension $1$, in fact, a line (provided that a and $b$ are not both null). It would be equally easy to show that the set $P$ of solutions of an equation
$$ax + by + cz = d$$
$$\mathbb{A}^{3}$$
is an affine subspace of of dimension $2$, in fact, a plane (provided that a, $b, c$ are not all null). More generally, the set $H$ of solutions of an equation
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
is an affine subspace $of\mathbb{A}^{m}$, and if $\lambda_{1} , \dots  , \lambda_{m}$  are not all null, it turns out that it is a subspace of dimension $m$ - $1$ called a hyperplane.

<!-- PAGE 848 -->
We can interpret the equation
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
$$\mathbb{R}^{m} \mathbb{R}$$
in terms of the map $f$ : $\to$  defined such that
$$f(x_{1}, \dots  , x_{m}) = \lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} -\mu$$
for all $(x_{1}, \dots  , x_{m}) \in \mathbb{R}^{m}$. It is immediately verified that this map is affine, and the set $H$ of solutions of the equation
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
$$\mathbb{A}^{m} \mathbb{R}$$
is the null set, or kernel, of the affine map $f$ : $\to$ , in the sense that
$$\mathbb{A}^{m}$$
$$H = f^{-1}(0) = {x \in | f(x) = 0},$$
where $x = (x_{1}, \dots  , x_{m})$. Thus, it is interesting to consider affine forms, which are just affine maps $f$ : $E \to \mathbb{R}$ from an affine space to $\mathbb{R}$. Unlike linear forms $f^{*}$ , for which Ker $f^{*}$ is never empty (since it always contains the vector $0)$, it is possible that $f^{-1} (0) = \emptyset$ for an affine form $f$. Given an affine map $f$ : $E \to \mathbb{R}$, we also denote $f^{-1} (0)$ by Ker $f$, and we call it the kernel of $f$. Recall that an (affine) hyperplane is an affine subspace of codimension $1$. The relationship between affine hyperplanes and affine forms is given by the following proposition.

> **Proposition 24.14.** Let $E$ be an affine space. The following properties hold:
(a) Given any nonconstant affine form $f$ : $E \to \mathbb{R}$, its kernel $H =$ Ker $f$ is a hyperplane.
$(b)$ For any hyperplane $H$ in $E$, there is a nonconstant affine form $f$ : $E \to \mathbb{R}$ such that $H =$ Ker $f$. For any other affine form $g: E \to \mathbb{R}$ such that $H =$ Ker $g$, there is some $\lambda  \in \mathbb{R}$ such that $g = \lambda f$ (with $\lambda  \neq  0)$.
$(c)$ Given any hyperplane $H$ in $E$ and any (nonconstant) affine form $f$ : $E \to \mathbb{R}$ such that $H =$ Ker $f$, every hyperplane H' parallel to $H$ is defined by a nonconstant affine form $g$ such that g(a) $=$ f(a) - $\lambda$ , for all $a \in E$ and some $\lambda  \in \mathbb{R}$.

*Proof.* The proof is straightforward, and is omitted. It is also given in Gallier $[71]$. When $E$ is of dimension $n$, given an affine frame $(a_{0}, (u_{1}, \dots  , u_{n}))$ of $E$ with origin $a_{0}$, recall from Definition 24.5 that every point of $E$ can be expressed uniquely as $x = a_{0} + x_{1}u_{1} + \cdots  + x_{n}u_{n}$, where $(x_{1}, \dots  , x_{n})$ are the coordinates of $x$ with respect to the affine frame $(a_{0}, (u_{1}, \dots  , u_{n}))$.
