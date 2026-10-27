# Existence of Maximal Proper Ideals


<!-- PAGE 2195 -->

## C.3 Existence of Maximal Ideals Containing a Given

$$Proper Ideal$$
Let $A$ be a commutative ring with identity element. Recall that an ideal $\mathfrak{A}$ in $A$ is a proper ideal if $\mathfrak{A} \neq  A$. The following theorem holds:

> **Theorem C.3.** Given any proper ideal, $\mathfrak{A} \subseteq A$, there is a maximal ideal, $\mathfrak{B}$, containing $\mathfrak{A}$.

*Proof.* Let $\mathcal{I}$ be the set of all proper ideals, $\mathfrak{B}$, in $A$ that contain $\mathfrak{A}$. The set $\mathcal{I}$ is nonempty, since $\mathfrak{A} \in$ I. We claim that $\mathcal{I}$ is inductive. Consider any chain $(\mathfrak{A}_{i})_{i\in I}$ of ideals $\mathfrak{A}_{i}$ in $A$.
$$One can easily check that \mathfrak{B} = \bigcup_{i}  \mathfrak{A}_{i} is an ideal. Furthermore, \mathfrak{B} is a proper ideal, since$$
otherwise, the identity element $1^{\in I}$ would belong to $\mathfrak{B} = A$, and so, we would have $1 \in \mathfrak{A}_{i}$ for some $i$, which would imply $\mathfrak{A}_{i} = A$, a contradiction. Also, $\mathfrak{B}$ is obviously an upper bound for all the $\mathfrak{A}_{i}’s$. By Zorn’s lemma (Lemma C.1), the set $\mathcal{I}$ has a maximal element, say $\mathfrak{B}$, and $\mathfrak{B}$ is a maximal ideal containing $\mathfrak{A}$.

<!-- PAGE 2196 -->
