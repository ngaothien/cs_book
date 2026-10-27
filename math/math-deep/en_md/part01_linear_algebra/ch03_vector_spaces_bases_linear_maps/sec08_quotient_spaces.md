# Quotient Spaces


<!-- PAGE 111 -->

> **Definition 3.23.** When $E = F$, a linear map $f$ : $E \to E$ is also called an endomorphism. The space Hom(E, $E)$ is also denoted by End(E). It is also important to note that composition confers to Hom(E, $E)$ a ring structure. Indeed, composition is an operation $\circ$ : Hom(E, $E) \times$  Hom(E, $E) \to$ Hom(E, $E)$, which is associative and has an identity $id_{E}$, and the distributivity properties hold:
$$(g_{1} + g_{2}) \circ f = g_{1} \circ f + g_{2} \circ f;$$
$$g \circ (f_{1} + f_{2}) = g \circ f_{1} + g \circ f_{2}.$$
The ring Hom(E, $E)$ is an example of a noncommutative ring. It is easily seen that the set of bijective linear maps $f$ : $E \to E$ is a group under composition.

> **Definition 3.24.** Bijective linear maps $f$ : $E \to E$ are also called automorphisms. The group of automorphisms of $E$ is called the general linear group (of $E)$, and it is denoted by GL(E), or by Aut(E), or when $E =\mathbb{R}^{n}$, by $GL(n,\mathbb{R})$, or even by GL(n). Although in this book, we will not have many occasions to use quotient spaces, they are fundamental in algebra. The next section may be omitted until needed.

## 3.8 Quotient Spaces

Let $E$ be a vector space, and let $M$ be any subspace of $E$. The subspace $M$ induces a relation $\equiv_{M}$  on $E$, defined as follows: For all $u, v \in E, u \equiv_{M}  v$ iff $u$ - $v \in M$. We have the following simple proposition.

> **Proposition 3.25.** Given any vector space $E$ and any subspace $M$ of $E$, the relation $\equiv_{M}$ is an equivalence relation with the following two congruential properties: $1$. If $u_{1} \equiv_{M}  v_{1}$ and $u_{2} \equiv_{M}  v_{2}$, then $u_{1} + u_{2} \equiv_{M}  v_{1} + v_{2}$, and $2$. if $u \equiv_{M}  v$, then $\lambda u \equiv_{M}  \lambda v$.

*Proof.* It is obvious that $\equiv_{M}$  is an equivalence relation. Note that $u_{1} \equiv_{M}  v_{1}$ and $u_{2} \equiv_{M}  v_{2}$ are equivalent to $u_{1}$ - $v_{1} = w_{1}$ and $u_{2}$ - $v_{2} = w_{2}$, with $w_{1}, w_{2} \in M$, and thus,
$$(u_{1} + u_{2}) -(v_{1} + v_{2}) = w_{1} + w_{2},$$
and $w_{1} + w_{2} \in M$, since $M$ is a subspace of $E$. Thus, we have $u_{1} + u_{2} \equiv_{M}  v_{1} + v_{2}$. If $u$ - $v = w$, with $w \in M$, then
$$\lambda u -\lambda v = \lambda w,$$
and $\lambda w \in M$, since $M$ is a subspace of $E$, and thus $\lambda u \equiv_{M}  \lambda v$.
