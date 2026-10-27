# Proof of the Existence of a Basis in a Vector Space


<!-- PAGE 2194 -->
Remark: As we noted, the hypothesis of Zorn’s lemma implies that $S$ is nonempty (since the empty set must be bounded). A partially ordered set such that every chain is bounded is sometimes called inductive. We now give some applications of Zorn’s lemma.

## C.2 Proof of the Existence of a Basis in a Vector Space

Using Zorn’s lemma, we can prove that Theorem 3.8 holds for arbitrary vector spaces, and not just for finitely generated vector spaces, as promised in Chapter $3$.

> **Theorem C.2.** Given any family, $S = (u_{i})_{i\in I}$, generating a vector space $E$ and any linearly independent subfamily, $L = (u_{j})_{j\in J}$, of $S$ (where $J \subseteq$ I), there is a basis, $B$, of $E$ such that $L \subseteq B \subseteq S$.

*Proof.* Consider the set $\mathcal{L}$ of linearly independent families, $B$, such that $L \subseteq B \subseteq S$. Since $L \in L$, this set is nonempty. We claim that $\mathcal{L}$ is inductive. Consider any chain, $(B_{l})_{l\in\Lambda}$, of
$$linearly independent families B_{l} in\mathcal{L}, and look at B = \bigcup_{l}  \in  B_{l}. The family B is of the form$$
$B = (v_{h})_{h\in H}$, for some index set $H$, and it must be $linearly^{\Lambda}$ independent. Indeed, if this was not true, there would be some family $(\lambda_{h} )_{h\in H}$ of scalars, of finite support, so that
$$\sum_{h\in H}  \lambda_{h} v_{h} = 0,$$
$$where not all \lambda_{h}  are zero. Since B = \bigcup_{l}  B_{l} and only finitely many \lambda_{h}  are nonzero, there$$
is a finite subset, $F$, of $\Lambda$ , so that $v_{h} \in^{\in\Lambda} B_{fh}$ iff $\lambda_{h}  \neq  0$. But $(B_{l})_{l\in\Lambda}$ is a chain, and if we let $f = max{f_{h}$ | $f_{h} \in F}$, then $v_{h} \in B_{f}$, for all $v_{h}$ for which $\lambda_{h}  \neq  0$. Thus,
$$\sum_{h\in H}  \lambda_{h} v_{h} = 0$$
would be a nontrivial linear dependency among vectors from $B_{f}$, a contradiction. Therefore, $B \in L$, and since $B$ is obviously an upper bound for the $B_{l}’s$, we have proved that $\mathcal{L}$ is inductive. By Zorn’s lemma (Lemma C.1), the set $\mathcal{L}$ has some maximal element, say $B = (u_{h})_{h\in H}$. The rest of the proof is the same as in the proof of Theorem 3.8, but we repeat it for the reader’s convenience. We claim that $B$ generates $E$. Indeed, if $B$ does not generate $E$, then there is some $u_{p} \in S$ that is not a linear combination of vectors in $B$ (since $S$ generates $E)$, with $p \in / H$. Then, by Lemma 3.7, the family B' $= (u_{h})_{h\in H\cup {p}}$ is linearly independent, and since $L \subseteq B \subset$ B' $\subseteq S$, this contradicts the maximality of $B$. Thus, $B$ is a basis of $E$ such that $L \subseteq B \subseteq S$. Another important application of Zorn’s lemma is the existence of maximal ideals.
