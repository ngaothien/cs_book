# Affine Groups


<!-- PAGE 841 -->
It is easy to check that the point $a = (6, -3)$ is fixed by $f$, which means that f(a) $= a$, so by translating the coordinate frame to the origin a, the affine map behaves like a linear map. If $f$ : $E \to$ E' is a bijective affine map, given any three collinear points a, $b, c$ in $E$, with $a \neq  b$, where, say, $c = (1$ - $\lambda )a + \lambda b$, since $f$ preserves barycenters, we have f(c) $= (1-\lambda )f(a)+\lambda$ f(b), which shows that f(a), f(b), f(c) are collinear in E'. There is a converse to this property, which is simpler to state when the ground field is $K = \mathbb{R}$. The converse states that given any bijective function $f$ : $E \to$ E' between two real affine spaces of the same dimension $n \ge 2$, if $f$ maps any three collinear points to collinear points, then $f$ is affine. The proof is rather long (see Berger $[11]$ or Samuel $[148])$. Given three collinear points a, $b, c$, where a̸ $= c$, we have $b = (1$ - $\beta )a + \beta c$ for some unique $\beta$ , and we define the ratio of the sequence a, $b, c$, as
$$ratio(a, b, c) = \frac{\beta}{(1 -\beta )} = \frac{\longrightarrow ab}{bc} \longrightarrow ,$$
provided that $\beta  \neq  1$, i.e., $b \neq  c$. When $b = c$, we agree that ratio(a, $b, c) = \infty$ . We warn our readers that other authors define the ratio of a, $b, c$ as -ratio(a, $b, c) =_{-\to bc}^{-\to ba}$. Since affine maps preserve barycenters, it is clear that affine maps preserve the ratio of three points.

## 24.8 Affine Groups

We now take a quick look at the bijective affine maps. Given an affine space $E$, the set of affine bijections $f$ : $E \to E$ is clearly a group, called the affine group of $E$, and denoted by
$$\longrightarrow$$
GA(E). Recall that the group of bijective linear maps of the vector space $E$ is denoted by $\longrightarrow \longrightarrow \longrightarrow$ GL(E ). Then, the map $f \mapsto f$ defines a group homomorphism $L$: GA(E) $\to$ GL(E ). The kernel of this map is the set of translations on $E$. The subset of all linear maps of the form $\lambda  id_{E}\longrightarrow$  , where $\lambda  \in \mathbb{R} -{0}$, is a subgroup of $\longrightarrow$ GL(E ), and is denoted $by\mathbb{R}^{*}id_{E}\longrightarrow$  (where $\lambda  id_{E}\longrightarrow  (u) = \lambda u, and\mathbb{R}^{*} =\mathbb{R}-{0})$. The subgroup DIL(E) $= L^{-1}(\mathbb{R}^{*}id_{E}\longrightarrow$  ) of GA(E) is particularly interesting. It turns out that it is the disjoint union of the translations and of the dilatations of ratio $\lambda$ ̸ $= 1$. The elements of DIL(E) are called affine dilatations. Given any point $a \in E$, and any scalar $\lambda  \in \mathbb{R}$, a dilatation or central dilatation (or homothety) of center a and ratio $\lambda$  is a map $H_{a,\lambda}$ defined such that
$$\longrightarrow$$
$$H_{a,\lambda}(x) = a + \lambda ax,$$
for every $x \in E$.
Remark: The terminology does not seem to be universally agreed upon. The terms affine dilatation and central dilatation are used by Pedoe $[141]$. Snapper and Troyer use the term

<!-- PAGE 842 -->
dilation for an affine dilatation and magnification for a central dilatation $[168]$. Samuel uses homothety for a central dilatation, a direct translation of the French “homoth´etie” $[148]$. Since dilation is shorter than dilatation and somewhat easier to pronounce, perhaps we should use that! Observe that $H_{a,\lambda}(a) = a$, and when $\lambda  \neq  0$ and $x \neq$  a, $H_{a,\lambda}(x)$ is on the line defined by
$$\longrightarrow$$
a and $x$, and is obtained by “scaling” ax by $\lambda$ . Figure 24.21 shows the effect of a central dilatation of center $d$. The triangle (a, $b, c)$ is magnified to the triangle (a', b', c'). Note how every line is mapped to a parallel line.
$$a$$
$$a$$
$$bb$$
$$d$$
$$c$$
$$c$$
$$Figure 24.21: The effect of a central dilatation H_{d,\lambda}(x).$$
$$-\longrightarrow$$
When $\lambda  = 1, H_{a,1}$ is the identity. Note that $H_{a,\lambda} = \lambda  id_{E}\longrightarrow$  . When $\lambda  \neq  0$, it is clear that $H_{a,\lambda}$ is an affine bijection. It is immediately verified that
$$H_{a,\lambda} \circ H_{a,\mu} = H_{a,\lambda \mu}.$$
We have the following useful result.
$$\longrightarrow$$

> **Proposition 24.9.** Given any affine space $E$, for any affine bijection $f \in$ GA(E), if $f = \lambda  id_{E}\longrightarrow$ , for some $\lambda  \in \mathbb{R}^{*}$ with $\lambda  \neq  1$, then there is a unique point $c \in E$ such that $f = H_{c,\lambda}$.

*Proof.* The proof is straightforward, and is omitted. It is also given in Gallier $[71]$.
$$\longrightarrow$$
Clearly, if $f = id_{E}\longrightarrow$  , the affine map $f$ is a translation. Thus, the group of affine dilatations DIL(E) is the disjoint union of the translations and of the dilatations of ratio $\lambda  \neq  0, 1$. Affine dilatations can be given a purely geometric characterization.
