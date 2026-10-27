# Another Construction of


<!-- PAGE 863 -->
Now that we have defined $E$ and investigated the relationship between affine frames in
$$b \longrightarrow$$
$E$ and bases in $E$, we can give another construction of a vector $space\mathcal{F}$ from $E$ and $E$ that
$$b$$
will allow us to “visualize” in a much more intuitive fashion the structure of $E$ and of its
$$b$$
operations $+$ and $\cdot$ .
$$b$$

## 25.3 Another Construction of E

$$b$$
One would probably wish that we could start with this construction of $\mathcal{F}$ first, and then define $E$ using the isomorphism $\Omega$ : $E \to F$ defined below. Unfortunately, we first need the $b  b  b$ vector space structure on $E$ to show that $\Omega$ is linear!
$$b b$$
$$Definition \longrightarrow  25.1. Given any affine space \begin{pmatrix} \longrightarrow \\ E,E \end{pmatrix} , we define the vector space\mathcal{F} as the direct$$
sum $E \oplus \mathbb{R}, where\mathbb{R}$ denotes the $field\mathbb{R}$ considered as a vector space (over itself). Denoting
$$\longrightarrow$$
the unit vector $in\mathbb{R}$ by $1, since\mathcal{F} = E \oplus \mathbb{R}$, every vector $v \in F$ can be written as $v = u+\lambda 1$,
$$\longrightarrow$$
for some unique $u \in E$ and some unique $\lambda  \in \mathbb{R}$. Then, for any choice of an origin $\Omega_{1}$  in $E$, we define the map $\Omega$ : $E \to F$, as follows:
$$b b$$
$$-\longrightarrow$$
$$\lambda (1 +\Omega_{1} a)if \theta  = \langle a, \lambda \rangle , where a \in E and \lambda  \neq  0;$$
$$\Omega (\theta ) =\longrightarrow$$
$$b$$
$$uif \theta  = u, where u \in E .$$
The idea is that, once again, viewing $\mathcal{F}$ as an affine space under its canonical structure,
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$E$ is embedded in $\mathcal{F}$ as the hyperplane $H = 1 + E$ , with direction $E$ , the hyperplane $E$ in
$$-\longrightarrow$$
$\mathcal{F}$. Then, every point $a \in E$ is in bijection with the point $A = 1 + \Omega_{1}$ a, in the hyperplane $H$. If we denote the origin $0$ of the canonical affine space $\mathcal{F}$ by $\Omega$ , the map $\Omega$ maps a point
$$b$$
$\langle a, \lambda \rangle \in E$ to a point $in\mathcal{F}$, as follows: $\Omega (\langle a, \lambda \rangle$ ) is the point on the line passing through both
$$b -\longrightarrow  \longrightarrow$$
the origin $\Omega$ of $\mathcal{F}$ and the point $A = 1 + \Omega_{1}$ a in the hyperplane $H = 1 + E$ , such that
$$\longrightarrow  -\longrightarrow$$
$$\Omega (\langle a, \lambda \rangle ) = \lambda \Omega A = \lambda (1 +\Omega_{1} a).$$
$$b$$
The following proposition shows that $\Omega$ is an isomorphism of vector spaces.
$$b$$
$$\longrightarrow$$

> **Proposition 25.4.** Given any affine space $(E, E$ ), for any choice $\Omega_{1}$  of an origin in $E$, the map $\Omega$ : $E \to F$ is a linear isomorphism between $E$ and the vector space $\mathcal{F}$ of Definition $b  b  b$ 25.1. The inverse of $\Omega$ is given by
$$b$$
$$\langle \Omega_{1}  + \lambda^{-1} u, \lambda \rangle )if \lambda  \neq  0;$$
$$\Omega^{-1} (u + \lambda 1) =$$
$$buif \lambda  = 0.$$

*Proof.* It is a straightforward verification. We check that $\Omega$ is invertible, leaving the verifi-
$$b$$
cation that it is linear as an exercise. We have
$$-\longrightarrow  -\longrightarrow$$
$$\langle a, \lambda \rangle \mapsto \lambda 1 + \lambda \Omega_{1} a \mapsto \langle \Omega_{1}  +\Omega_{1} a, \lambda \rangle = \langle a, \lambda \rangle$$

<!-- PAGE 864 -->
and
$$u + \lambda 1 \mapsto \langle \Omega_{1}  + \lambda^{-1} u, \lambda \rangle \mapsto u + \lambda 1,$$
$$\longrightarrow$$
and since $\Omega$ is the identity on $E$ , we have shown that $\Omega \circ \Omega^{-1} =$ id, and $\Omega^{-1} \circ \Omega =$ id. This
$$b bb bb$$
shows that $\Omega$ is a bijection.
$$b$$
Figure 25.4 illustrates the embedding of the affine space $E$ into the vector $space\mathcal{F}$, when $E$ is an affine plane.
$$\overline{\lambda}\overline{\Omega}\overline{A}$$
$$A = 1 + \overline{\Omega}_{1}\overline{a}$$
$$1H = 1 + \overline{E}$$
$$\Omega$$
$$\overline{\Omega}_{1}\overline{a}$$
$$\overline{E}$$
$$Figure 25.4: Embedding an affine space into a vector space \mathcal{F}.$$
Proposition 25.4 gives a nice interpretation of the sum operation $+$ of $E$. Given two
$$b b$$
weighted points $\langle a_{1}, \lambda_{1} \rangle$ and $\langle a_{2}, \lambda_{2} \rangle$ , we have
$$\langle a_{1}, \lambda_{1} \rangle + \langle a_{2}, \lambda_{2} \rangle =\Omega^{-1} (\Omega (\langle a_{1}, \lambda_{1} \rangle ) +\Omega (\langle a_{2}, \lambda_{2} \rangle )).$$
$$b bb b$$
The operation $\Omega (\langle a_{1}, \lambda_{1} \rangle )+\Omega (\langle a_{2}, \lambda_{2} \rangle$ ) has a simple geometric interpretation. If $\lambda_{1}  +\lambda_{2}  \neq  0$,
$$b b$$
then find the points $M_{1}$ and $M_{2}$ on the lines passing through the origin $\Omega of\mathcal{F}$ and the points
$$-\longrightarrow -\longrightarrow  -\longrightarrow$$
$A_{1} = \Omega (a_{1})$ and $A_{2} = \Omega (a_{2})$ in the hyperplane $H$, such that $\Omega M_{1} = \lambda_{1} \Omega A_{1}$ and $\Omega M_{2} = -\longrightarrow  b   b-\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow \lambda_{2} \Omega A_{2}$, add the vectors $\Omega M_{1}$ and $\Omega M_{2}$, getting a point $N$ such that $\Omega N = \Omega M_{1} + \Omega M_{2}$, and consider the intersection $G$ of the line passing through $\Omega$ and $N$ with the hyperplane $H$. Then, $G$ is the barycenter of $A_{1}$ and $A_{2}$ assigned the weights $\lambda_{1} /(\lambda_{1}  + \lambda_{2}$ ) and $\lambda_{2} /(\lambda_{1}  + \lambda_{2}$ ),
$$\longrightarrow -\longrightarrow$$
and if $g = \Omega^{-1} (\Omega G)$, then $\Omega^{-1} (\Omega N) = \langle g, \lambda_{1}  + \lambda_{2} \rangle$ . See Figure 25.5.
$$b b$$
$$-\longrightarrow  -\longrightarrow$$
Instead of adding the vectors $\Omega M_{1}$ and $\Omega M_{2}$, we can take the middle N' of the segment $M_{1}M_{2}$, and $G$ is the intersection of the line passing through $\Omega$ and N' with the hyperplane $H$ as illustrated in Figure 25.5.

<!-- PAGE 865 -->
$$N$$
$$\overline{\lambda} \overline{\Omega}\overline{A}$$
$$22$$
$$\overline{\Omega}\overline{N}$$
$$\overline{\lambda} \overline{\Omega}\overline{A}$$
$$11M$$
$$A = 1 + \overline{\Omega}\overline{a} 2N’$$
$$A = 1 + \overline{\Omega} a1\overline{1} 1M$$
$$\overline{1}\Omega 1$$
$$221H = 1 + \overline{E} M$$
$$2A$$
$$1$$
$$\Omega A$$
$$2M1$$
$$\overline{\Omega}\overline{a}\Omega$$
$$12\overline{\Omega}\overline{a}$$
$$\overline{1} 1\overline{\Omega}$$
$$\overline{E}$$
$$\overline{E}$$
$$N$$
$$MM$$
$$2N’ 1$$
$$GA$$
$$1$$
$$AH = 1 + \overline{E}$$
$$2$$
$$\overline{\Omega}$$
$$\overline{E}$$

![Figure 25.5](../../assets/ch25/fig_25_5.png)

**Figure 25.5:** The geometric construction of $\Omega (\langle a_{1}, \lambda_{1} \rangle$ ) $+ \Omega (\langle a_{2}, \lambda_{2} \rangle$ ) for $\lambda_{1}  + \lambda_{2}  \neq  0$.
$$b b$$
If $\lambda_{1}  + \lambda_{2}  = 0$, then $\langle a_{1}, \lambda_{1} \rangle + \langle a_{2}, \lambda_{2} \rangle$ is a vector determined as follows. Again, find the
$$b$$
points $M_{1}$ and $M_{2}$ on the lines passing through the origin $\Omega of\mathcal{F}$ and the points $A_{1} = \Omega (a_{1})$
$$-\longrightarrow -\longrightarrow  -\longrightarrow -\longrightarrow  b$$
and $A_{2} = \Omega (a_{2})$ in the hyperplane $H$, such that $\Omega M_{1} = \lambda_{1} \Omega A_{1}$ and $\Omega M_{2} = \lambda_{2} \Omega A_{2}$, and add
$$b -\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow$$
the vectors $\Omega M_{1}$ and $\Omega M_{2}$, getting a point $N$ such that $\Omega N = \Omega M_{1} + \Omega M_{2}$. The desired
$$-\longrightarrow$$
vector is $\Omega N$, which is parallel to the line $A_{1}A_{2}$. Equivalently, let N' be the middle of the
$$-\longrightarrow$$
segment $M_{1}M_{2}$, and the desired vector is $2\Omega$ N' . See Figure 25.6. We can also give a geometric interpretation of $\langle a, \lambda \rangle +u$. Let $A = \Omega$ (a) in the hyperplane
$$b -\longrightarrow \longrightarrow$$
$H$, let $D$ be the line determined by $A$ and $u$, let $M_{1}$ be the point such that $\Omega M_{1} = \lambda \Omega A$, and
$$-\longrightarrow$$
let $M_{2}$ be the point such that $\Omega M_{2} = u$, that is, $M_{2} = \Omega + u$. By construction, the line $D$ is
$$-\longrightarrow$$
in the hyperplane $H$, and it is parallel to $\Omega M_{2}$, so that $D, M_{1}$, and $M_{2}$ are coplanar. Then,
$$-\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow  -\longrightarrow$$
add the vectors $\Omega M_{1}$ and $\Omega M_{2}$, getting a point $N$ such that $\Omega N = \Omega M_{1} + \Omega M_{2}$, and let $G$
$$\longrightarrow$$
be the intersection of the line determined by $\Omega$ and $N$ with the line $D$. If $g = \Omega^{-1} (\Omega G)$,
$$-\longrightarrow  b$$
then, $\Omega^{-1} (\Omega N) = \langle g, \lambda \rangle$ . Equivalently, if N' is the middle of the segment $M_{1}M_{2}$, then $G$ is $b$ the intersection of the line determined by $\Omega$ and N' , with the line $D$; see Figure 25.7. We now consider the universal property of $E$ mentioned at the beginning of this section.
$$b$$
