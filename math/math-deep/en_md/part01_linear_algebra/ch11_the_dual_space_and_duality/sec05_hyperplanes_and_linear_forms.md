# Hyperplanes and Linear Forms


<!-- PAGE 435 -->

## 11.5 Hyperplanes and Linear Forms

Actually Proposition 11.7 below follows from Parts $(c)$ and $(d)$ of Theorem 11.4, but we feel that it is also interesting to give a more direct proof.

> **Proposition 11.7.** Let $E$ be a vector space. The following properties hold:
(a) Given any nonnull linear form $f^{*} \in E^{*}$, its kernel $H =$ Ker $f^{*}$ is a hyperplane.
$(b)$ For any hyperplane $H$ in $E$, there is a (nonnull) linear form $f^{*} \in E^{*}$ such that $H =$ Ker $f^{*}$ .
$(c)$ Given any hyperplane $H$ in $E$ and any (nonnull) linear form $f^{*} \in E^{*}$ such that $H =$ Ker $f^{*}$ , for every linear form $g^{*} \in E^{*}, H =$ Ker $g^{*}$ iff $g^{*} = \lambda f^{*}$ for some $\lambda  \neq  0$ in $K$.

*Proof.* (a) If $f^{*} \in E^{*}$ is nonnull, there is some vector $v_{0} \in E$ such that $f^{*} (v_{0}) \neq  0$. Let $H =$ Ker $f^{*}$ . For every $v \in E$, we have
$$f^{*} \begin{pmatrix} f^{*}(v) \\ v - & v_{0} \\ f^{*}(v_{0}) \end{pmatrix} = f^{*} (v) - \frac{f^{*}(v)}{f^{*}(v_{0})} f^{*}(v_{0}) = f^{*}(v) -f^{*}(v) = 0.$$
Thus,
$$v - \frac{f^{*}(v)}{f^{*}(v_{0})} v_{0} = h \in H,$$
and
$$v = h + \frac{f^{*}(v)}{f^{*}(v_{0})} v_{0},$$
that is, $E = H + Kv_{0}$. Also since $f^{*} (v_{0}) \neq  0$, we have $v_{0} \in / H$, that is, $H \cap Kv_{0} = 0$. Thus, $E = H \oplus Kv_{0}$, and $H$ is a hyperplane.
$(b)$ If $H$ is a hyperplane, $E = H \oplus Kv_{0}$ for some $v_{0} \in / H$. Then every $v \in E$ can be written in a unique way as $v = h + \lambda v_{0}$. Thus there is a well-defined function $f^{*}$ : $E \to K$, such that, $f^{*} (v) = \lambda$ , for every $v = h + \lambda v_{0}$. We leave as a simple exercise the verification that $f^{*}$ is a linear form. Since $f^{*} (v_{0}) = 1$, the linear form $f^{*}$ is nonnull. Also, by definition, it is clear that $\lambda  = 0$ iff $v \in H$, that is, Ker $f^{*} = H$.
$(c)$ Let $H$ be a hyperplane in $E$, and let $f^{*} \in E^{*}$ be any (nonnull) linear form such that $H =$ Ker $f^{*}$ . Clearly, if $g^{*} = \lambda f^{*}$ for some $\lambda  \neq  0$, then $H =$ Ker $g^{*}$. Conversely, assume that $H =$ Ker $g^{*}$ for some nonnull linear form $g^{*}$. From (a), we have $E = H \oplus Kv_{0}$, for some $v_{0}$ such that $f^{*} (v_{0}) \neq  0$ and $g^{*}(v_{0}) \neq  0$. Then observe that
$$g^{*}- \frac{g^{*}(v_{0})}{f^{*}(v_{0})} f^{*}$$
is a linear form that vanishes on $H$, since both $f^{*}$ and $g^{*}$ vanish on $H$, but also vanishes on $Kv_{0}$. Thus, $g^{*} = \lambda f^{*}$ , with
$$\lambda  = \frac{g^{*}(v_{0})}{f^{*}(v_{0})} .$$
