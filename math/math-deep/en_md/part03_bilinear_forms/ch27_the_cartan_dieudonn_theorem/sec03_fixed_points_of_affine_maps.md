# Fixed Points of Affine Maps


<!-- PAGE 985 -->
$$\longrightarrow$$
for all $u \in E , f$ will be affine if we can show that $g$ is linear, and $f$ will be an affine isometry if we can show that $g$ is a linear isometry. Observe that
$$--------\longrightarrow --------\longrightarrow$$
$$g(v) -g(u)=f(\Omega )f(\Omega + v) -f(\Omega )f(\Omega + u)$$
$$-----------\longrightarrow$$
$$=f(\Omega + u)f(\Omega + v).$$
Then, the hypothesis
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|$$
for all a, $b \in E$, implies that
$$-----------\longrightarrow ---------\longrightarrow$$
$$\|g(v) -g(u)\|= \|f(\Omega + u)f(\Omega + v)\|= \|(\Omega + u)(\Omega + v)\|= \|v -u\|.$$
Thus, $g$ preserves the distance. Also, by definition, we have
$$g(0) = 0.$$
Thus, we can apply Lemma 12.12, which shows that $g$ is indeed a linear isometry, and thus $f$ is an affine isometry. In order to understand the structure of affine isometries, it is important to investigate the fixed points of an affine map.

## 27.3 Fixed Points of Affine Maps

$$\longrightarrow$$
$$Recall that E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} denotes the eigenspace of the linear \longrightarrow mapf associated \longrightarrow  with the scalar$$
$1$, that is, the subspace consisting of all vectors $u \in E$ such that $f (u) = u$. Clearly,
$$\mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} = E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} . Given some origin \Omega \in E, since$$
$$\longrightarrow  \longrightarrow \longrightarrow$$
$$f(a) = f(\Omega +\Omega a) = f(\Omega ) +f (\Omega a),$$
$$-----\longrightarrow  \longrightarrow \longrightarrow$$
we have $f(\Omega$ )f(a) $= f (\Omega$ a), and thus
$$--\longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow$$
$$\Omega f(a) =\Omega f(\Omega ) +f (\Omega a).$$
From the above, we get
$$--\longrightarrow \longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(a) -\Omega a =\Omega f(\Omega ) +f (\Omega a) -\Omega a.$$
Using this, we show the following lemma, which holds for arbitrary affine spaces of finite dimension and for arbitrary affine maps.

<!-- PAGE 986 -->

> **Proposition 27.8.** Let $E$ be any affine space of finite dimension. For every affine map $f$ : $E \to E$, let Fix(f) $= {a \in E$ | f(a) $= a}$ be the set of fixed points of $f$. The following properties hold:
$(1)$ If $f$ has some fixed point a, so that Fix(f) $\neq  \emptyset$ , then Fix(f) is an affine subspace of $E$ such that
$$Fix(f) = a + E \begin{pmatrix} \longrightarrow \\ 1,f \\ linear \end{pmatrix} = a + \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \\ forthe \end{pmatrix} ,$$
$$\longrightarrow$$
$$where E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} is the eigenspace of the  mapf   eigenvalue 1.$$
$$(2) The affine map f has a unique fixed point iff E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} = {0}.$$

*Proof.* $(1)$ Since the identity
$$--\longrightarrow \longrightarrow  ---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(b) -\Omega b =\Omega f(\Omega ) +f (\Omega b) -\Omega b$$
$$--\longrightarrow$$
holds for all $\Omega , b \in E$, if f(a) $= a$, then af(a) $= 0$, and thus, letting $\Omega = a$, for any $b \in E$ we have
$$--\longrightarrow \longrightarrow  --\longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$af(b) -ab =af(a) +f (ab) -ab =f (ab) -ab,$$
and so
$$f(b) = b$$
iff
$$--\longrightarrow \longrightarrow$$
$$af(b) -ab = 0$$
iff
$$\longrightarrow \longrightarrow \longrightarrow$$
$$f (ab) -ab = 0$$
iff
$$\longrightarrow$$
$$ab \in E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} ,$$
which proves that
$$Fix(f) = a + E \begin{pmatrix} \longrightarrow \\ 1,f \end{pmatrix} = a + \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} .$$
$(2)$ Again, fix some origin $\Omega$ . Some a satisfies f(a) $= a$ iff
$$--\longrightarrow \longrightarrow$$
$$\Omega f(a) -\Omega a = 0$$
iff
$$---\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$\Omega f(\Omega ) +f (\Omega a) -\Omega a = 0,$$
which can be rewritten as
$$\longrightarrow ---\longrightarrow$$
$$\begin{pmatrix} \longrightarrow \\ f-id \\ = & 0 \end{pmatrix} (\Omega a) = -\Omega f(\Omega ).$$
$$\longrightarrow  \longrightarrow$$
$$We have E \begin{pmatrix} \longrightarrow \\ 1,f \\ \longrightarrow \\ f- \end{pmatrix} = \mathrm{Ker} \begin{pmatrix} \longrightarrow \\ f-id \\ surjective, \end{pmatrix} {} iff f -id is injective, and sinceE has finite$$
dimension,  id is also  and thus, there is indeed some $a \in E$ such that
$$\longrightarrow ---\longrightarrow$$
$$\begin{pmatrix} \longrightarrow \\ f-id \end{pmatrix} (\Omega a) = -\Omega f(\Omega ),$$
