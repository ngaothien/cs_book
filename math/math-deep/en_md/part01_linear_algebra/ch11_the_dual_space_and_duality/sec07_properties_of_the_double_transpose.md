# Properties of the Double Transpose


<!-- PAGE 443 -->

> **Proposition 11.17.** Given any $m\times n$ matrix $A$ over a field $K$ (typically $K =\mathbb{R}$ or $K =\mathbb{C})$, the rank of $A$ is the maximum natural number $r$ such that there is an $r \times  r$ submatrix $B$ of $A$ obtained by selecting $r$ rows and $r$ columns of $A$, such that det(B) $\neq  0$. This is not a very efficient way of finding the rank of a matrix. We will see that there are better ways using various decompositions such as LU, QR, or SVD.

## 11.7 Properties of the Double Transpose

First we have the following property showing the naturality of the eval map.

> **Proposition 11.18.** For any linear map $f$ : $E \to F$, we have
$$f^{\top \top} \circ eval_{E} = eval_{F} \circ f,$$
or equivalently the following diagram commutes:
$$E^{**f\top \top} F^{**}/$$
$$evalEevalF$$
$$E F./$$
$$\overline{f}$$

*Proof.* For every $u \in E$ and every $\phi  \in F^{*}$ , we have
$$(f^{\top \top} \circ eval_{E})(u)(\phi ) = \langle f^{\top \top} (eval_{E}(u)), \phi \rangle$$
$$= \langle eval_{E}(u), f^{\top} (\phi )\rangle$$
$$= \langle f^{\top} (\phi ), u\rangle$$
$$= \langle \phi , f(u)\rangle$$
$$= \langle eval_{F}(f(u)), \phi \rangle$$
$$= \langle (eval_{F} \circ f)(u), \phi \rangle$$
$$= (eval_{F} \circ f)(u)(\phi ),$$
which proves that $f^{\top \top} \circ eval_{E} = eval_{F} \circ f$, as claimed. If $E$ and $F$ are finite-dimensional, then $eval_{E}$ and $eval_{F}$ are isomorphisms, so Proposition 11.18 shows that
$$f^{\top \top} = eval_{F} \circ f \circ eval_{E}^{-1} .(*)$$
The above equation is often interpreted as follows: if we identify $E$ with its bidual $E^{**}$ and $F$ with its bidual $F^{**}$ , then $f^{\top \top} = f$. This is an abuse of notation; the rigorous statement is (*). As a corollary of Proposition 11.18, we obtain the following result.

<!-- PAGE 444 -->

> **Proposition 11.19.** If dim(E) is finite, then we have
$$\mathrm{Ker} (f^{\top \top} ) = eval_{E}(\mathrm{Ker} (f)).$$

*Proof.* Indeed, if $E$ is finite-dimensional, the map $eval_{E}$ : $E \to E^{**}$ is an isomorphism, so every $\phi  \in E^{**}$ is of the form $\phi  = eval_{E}(u)$ for some $u \in E$, the map $eval_{F}$ : $F \to F^{**}$ is injective, and we have
$$f^{\top \top} (\phi ) = 0ifff^{\top \top} (eval_{E}(u)) = 0$$
$$iff eval_{F}(f(u)) = 0$$
$$iff f(u) = 0$$
$$iff u \in \mathrm{Ker} (f)$$
$$iff\phi  \in eval_{E}(\mathrm{Ker} (f)),$$
which proves that Ker $(f^{\top \top}$ ) $= eval_{E}(Ker (f))$.
Remarks: If dim(E) is finite, following an argument of Dan Guralnik, the fact that rk(f) $= rk(f^{\top}$ ) can be proven using Proposition 11.19.

*Proof.* We know from Proposition 11.11 applied to $f^{\top}$ : $F^{*} \to E^{*}$ that
$$\mathrm{Ker} (f^{\top \top} ) = (\mathrm{Im} f^{\top} )^{0},$$
and we showed in Proposition 11.19 that
$$\mathrm{Ker} (f^{\top \top} ) = eval_{E}(\mathrm{Ker} (f)).$$
It follows (since $eval_{E}$ is an isomorphism) that
$$\dim((\mathrm{Im} f^{\top} )^{0}) = \dim(\mathrm{Ker} (f^{\top \top} )) = \dim(\mathrm{Ker} (f)) = \dim(E) -\dim(\mathrm{Im} f),$$
and since
$$\dim(\mathrm{Im} f^{\top} ) + \dim((\mathrm{Im} f^{\top} )^{0}) = \dim(E),$$
we get
$$\dim(\mathrm{Im} f^{\top} ) = \dim(\mathrm{Im} f).$$
As indicated by Dan Guralnik, if dim(E) is finite, the above result can be used to prove the following result.

> **Proposition 11.20.** If dim(E) is finite, then for any linear map $f$ : $E \to F$, we have
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}.$$
