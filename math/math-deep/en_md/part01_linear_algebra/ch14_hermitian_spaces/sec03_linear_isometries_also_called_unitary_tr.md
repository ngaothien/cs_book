# Linear Isometries (Also Called Unitary Transformations)


<!-- PAGE 544 -->

## 14.3 Linear Isometries (Also Called Unitary Transfor-

$$mations)$$
In this section we consider linear maps between Hermitian spaces that preserve the Hermitian norm. All definitions given for Euclidean spaces in Section 12.5 extend to Hermitian spaces, except that orthogonal transformations are called unitary transformation, but Proposition 12.12 extends only with a modified Condition $(2)$. Indeed, the old proof that $(2)$ implies
$(3)$ does not work, and the implication is in fact false! It can be repaired by strengthening Condition $(2)$. For the sake of completeness, we state the Hermitian version of Definition 12.5.

> **Definition 14.7.** Given any two nontrivial Hermitian spaces $E$ and $F$ of the same finite dimension $n$, a function $f$ : $E \to F$ is a unitary transformation, or a linear isometry, if it is linear and
$$\|f(u)\|= \|u\|,for all u \in E.$$
Proposition 12.12 can be salvaged by strengthening Condition $(2)$.

> **Proposition 14.14.** Given any two nontrivial Hermitian spaces $E$ and $F$ of the same finite dimension $n$, for every function $f$ : $E \to F$, the following properties are equivalent:
$(1) f$ is a linear map and $\|f(u)\| = \|u\|$, for all $u \in E$;
$(2) \|f(v)$ - $f(u)\| = \|v$ - $u\|$ and f(iu) $=$ if(u), for all $u, v \in E$.
$(3)$ f(u) $\cdot$  f(v) $= u \cdot  v$, for all $u, v \in E$. Furthermore, such a map is bijective.

*Proof.* The proof that $(2)$ implies $(3)$ given in Proposition 12.12 needs to be revised as follows. We use the polarization identity
$$2\phi (u, v) = (1 + i)(\|u\|^{2}+ \|v\|^{2}) -\|u -v\|^{2}-i\|u -iv\|^{2}.$$
Since f(iv) $=$ if(v), we get f(0) $= 0$ by setting $v = 0$, so the function $f$ preserves distance and norm, and we get
$$2\phi (f(u), f(v)) = (1 + i)(\|f(u)\|^{2}+ \|f(v)\|^{2}) -\|f(u) -f(v)\|^{2}$$
$$-i\|f(u) -if(v)\|^{2}$$
$$= (1 + i)(\|f(u)\|^{2}+ \|f(v)\|^{2}) -\|f(u) -f(v)\|^{2}$$
$$-i\|f(u) -f(iv)\|^{2}$$
$$= (1 + i)(\|u\|^{2}+ \|v\|^{2}) -\|u -v\|^{2}-i\|u -iv\|^{2}$$
$$= 2\phi (u, v),$$
which shows that $f$ preserves the Hermitian inner product as desired. The rest of the proof is unchanged.
