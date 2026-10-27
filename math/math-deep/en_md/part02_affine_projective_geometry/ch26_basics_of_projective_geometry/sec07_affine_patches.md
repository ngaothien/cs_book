# Affine Patches


<!-- PAGE 917 -->
$$p$$
$$2\alpha$$
$$1   +-  f$$
$$- p3 \alpha q$$
$$p p4 22$$
$$2=$$
$$p  -   p1\lambda$$
$$p313q31  +-$$
$$-$$
$$q  2q\lambda$$
$$pq 4 2$$
$$11- q=$$
$$q31$$
$$3q$$
$$1$$
$$p1$$
$$\alpha   p4$$
$$p31+ -  f$$
$$- \alpha  2$$
$$p 2=$$
$$p  -   p 1$$
$$p313$$
$$p2$$
$$q$$
$$2$$
$$q3\lambda$$
$$-  1+-  q$$
$$q  2 \lambda 4$$
$$q  2$$
$$1- q=$$
$$q31$$
$$3q$$
$$1$$
$$Figure 26.17: Case (4)$$
and
$$\frac{(adbc)(x1)}{(c + d)(cx + d)} - -$$
have opposite signs when $0 < x < 1$, which means that the image of $[0, 1]$ is the interval $[b/d, (a + b)/(c + d)]$ (or $[(a + b)/(c + d), b/d])$. We now consider the projective completion of an affine space. First, we introduce the notion of affine patch.

## 26.7 Affine Patches

$$\longrightarrow$$
Given an affine space $E$ with associated vector space $E$ , we can form the vector space $E$,
$$b$$
the homogenized version of $E$, and then, the projective space $P$ induced by $E$. This
$$projective space, also denoted byE, has some very interesting properties. \begin{pmatrix} Eb \end{pmatrix} In fact, it satisfies b$$
$$e$$
a universal property, but before we can say what it is, we have to take a closer look at $E$.
$$e$$
Since the vector space $E$ is the disjoint union of elements of the form $\langle a, \lambda \rangle$ , where $a \in E$
$$b\longrightarrow$$
and $\lambda  \in K -{0}$, and elements of the form $u \in E$ , observe that if $\sim$ is the equivalence

<!-- PAGE 918 -->
relation on $E$ used to define the projective space $P$ , then the equivalence class $[\langle a, \lambda \rangle ]_{\sim}$
$$of a weighted b point contains the special representative \begin{pmatrix} Eb \end{pmatrix} a = \langle a, 1\rangle , and the equivalence class$$
$$\longrightarrow$$
$$[u]_{\sim}of a nonzero vector u \in E is just a point of the projective space P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} . Thus, there is$$
a bijection
$$P \begin{pmatrix} Eb \end{pmatrix} \leftarrow \to E \cup P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix}$$
$$between P \begin{pmatrix} Eb \\ in \end{pmatrix} and the disjoint union E \cup P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} , which allows us to view E as being$$
$$embedded  P \begin{pmatrix} Eb \\ hyperplane \end{pmatrix} . The points of P \begin{pmatrix} Eb \end{pmatrix} in P \begin{pmatrix} \longrightarrow \\ E \\ hyperplane \end{pmatrix} will be called points at infinity, and the$$
$$projective  P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} is called the  at infinity. We will also denote the$$
$$point [u]_{\sim}of P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} (where u \neq  0) by u_{\infty}.$$
Thus, we can think of $E = P$ as the projective completion of the affine space $E$
$$obtained by adding points  ate infinity \begin{pmatrix} Eb \end{pmatrix} forming the hyperplane P. As we commented in$$
$$Section 26.2 when we presented the hyperplane model of P(E), the notion of point at infinity \begin{pmatrix} \longrightarrow \\ E \end{pmatrix}$$
is really an affine notion. But even if a vector space $E$ doesn’t arise from the completion of an affine space, there is an affine structure on the complement of any hyperplane P(H) in the projective space P(E). In the case of $E$, the complement $E$ of the projective hyperplane
$$e$$
$$P \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} is indeed an affine space. This is a general property that is needed in order to figure$$
out the universal property of $E$.
$$e$$

> **Proposition 26.16.** Given a vector space $E$ and a hyperplane $H$ in $E$, the complement $E_{H} =$ P(E) - P(H) of the projective hyperplane P(H) in the projective space P(E) can be given an affine structure such that the associated vector space of $E_{H}$ is $H$. The affine structure on $E_{H}$ depends only on $H$, and under this affine structure, $E_{H}$ is isomorphic to an affine hyperplane in $E$.

*Proof.* Since $H$ is a hyperplane in $E$, there is some $w \in$ E-H such that $E = Kw\oplus H$. Thus, every vector $u$ in E-H can be written in a unique way as $\lambda w+h$, where $\lambda  \neq  0$ and $h \in H$. As a consequence, for every point $[u]$ in $E_{H}$, the equivalence class $[u]$ contains a representative of the form $w + \lambda^{-1} h$, with $\lambda  \neq  0$. Then we see that the map $\phi$ : $(w + H) \to E_{H}$, defined such that
$$\phi (w + h) = [w + h],$$
is a bijection. In order to define an affine structure on $E_{H}$, we define $+: E_{H} \times  H \to E_{H}$ as follows: For every point $[w + h_{1}] \in E_{H}$ and every $h_{2} \in H$, we let
$$[w + h_{1}] + h_{2} = [w + h_{1} + h_{2}].$$
The axioms of an affine space are immediately verified. Now, $w + H$ is an affine hyperplane is $E$, and under the affine structure just given to $E_{H}$, the map $\phi$ : $(w +H) \to E_{H}$ is an affine map that is bijective. Thus, $E_{H}$ is isomorphic to the affine hyperplane $w + H$. If we had chosen a different vector w' $\in E -H$ such that $E = Kw'\oplus H$, then $E_{H}$ would be isomorphic to the affine hyperplane w' $+ H$ parallel to $w + H$. But these two hyperplanes are clearly isomorphic by translation, and thus the affine structure on $E_{H}$ depends only on $H$.
