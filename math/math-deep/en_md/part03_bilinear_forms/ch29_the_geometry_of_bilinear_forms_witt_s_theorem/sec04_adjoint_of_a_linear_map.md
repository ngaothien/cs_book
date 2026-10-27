# Adjoint of a Linear Map


<!-- PAGE 1028 -->

## 29.4 Adjoint of a Linear Map

Let $E_{1}$ and $E_{2}$ be two $K$-vector spaces, and let $\phi_{1}$  : $E_{1}\times E_{1} \to K$ be a sesquilinear form on $E_{1}$ and $\phi_{2}$  : $E_{2} \times  E_{2} \to K$ be a sesquilinear form on $E_{2}$. It is also possible to deal with the more general situation where we have four vector spaces $E_{1}, F_{1}, E_{2}, F_{2}$ and two sesquilinear forms $\phi_{1}$  : $E_{1} \times  F_{1} \to K$ and $\phi_{2}$  : $E_{2} \times  F_{2} \to K$, but we will leave this generalization as an exercise. We also assume that $l_{\phi1}$ and $r_{\phi1}$ are bijective, which implies that that $\phi_{1}$  is nondegenerate. This is automatic if the space $E_{1}$ is finite dimensional and $\phi_{1}$  is nondegenerate. Given any linear map $f$ : $E_{1} \to E_{2}$, for any fixed $u \in E_{2}$, we can consider the linear form in $E_{1}^{*}$ given by
$$x \mapsto \phi_{2} (f(x), u),x \in E_{1}.$$
$$\frac{Since}{E_{1}} r_{\phi1} : \overline{E}_{1} \to E_{1}^{*} is bijective, there is a unique y \in E_{1} (because the vector spaces E_{1} and$$
only differ by scalar multiplication), so that
$$\phi_{2} (f(x), u) = \phi_{1} (x, y),for all x \in E_{1}.$$
If we denote this unique $y \in E_{1}$ by $f^{*l} (u)$, then we have
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),for all x \in E_{1}, and all u \in E_{2}.$$
Thus, we get a function $f^{*l}$  : $E_{2} \to E_{1}$. We claim that this function is a linear map. For any $v_{1}, v_{2} \in E_{2}$, we have
$$\phi_{2} (f(x), v_{1} + v_{2}) = \phi_{2} (f(x), v_{1}) + \phi_{2} (f(x), v_{2})$$
$$= \phi_{1} (x, f^{*l} (v_{1})) + \phi_{1} (x, f^{*l} (v_{2}))$$
$$= \phi_{1} (x, f^{*l} (v_{1}) + f^{*l} (v_{2}))$$
$$= \phi_{1} (x, f^{*l} (v_{1} + v_{2})),$$
for all $x \in E_{1}$. Since $r_{\phi1}$ is injective, we conclude that
$$f^{*l} (v_{1} + v_{2}) = f^{*l} (v_{1}) + f^{*l} (v_{2}).$$
For any $\lambda  \in K$, we have
$$\phi_{2} (f(x), \lambda v) =\overline{\lambda \phi}_{2}(f(x), v)$$
$$=\overline{\lambda \phi}_{1}(x, f^{*l} (v))$$
$$= \phi_{1} (x, \lambda f^{*l} (v))$$
$$= \phi_{1} (x, f^{*l} (\lambda v)),$$
for all $x \in E_{1}$. Since $r_{\phi1}$ is injective, we conclude that
$$f^{*l} (\lambda v) = \lambda f^{*l} (v).$$

<!-- PAGE 1029 -->
Therefore, $f^{*l}$  is linear. We call it the left adjoint of $f$. Now, for any fixed $u \in E_{2}$, we can consider the linear form in $E_{1}^{*}$ given by
$$x \mapsto \overline{\phi}_{2}\overline{(}\overline{u, f}\overline{(}\overline{x}\overline{))} x \in E_{1}.$$
Since $l_{\phi1}$ : $\overline{E}_{1} \to E_{1}^{*}$ is bijective, there is a unique $y \in E_{1}$ so that
$$\overline{\phi}_{2}\overline{(}\overline{u, f}\overline{(}\overline{x}\overline{)) =}\overline{\phi}_{1}\overline{(}\overline{y, x}\overline{)},for all x \in E_{1}.$$
If we denote this unique $y \in E_{1}$ by $f^{*r} (u)$, then we have
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),for all x \in E_{1}, and all u \in E_{2}.$$
Thus, we get a function $f^{*r}$  : $E_{2} \to E_{1}$. As in the previous situation, it easy to check that $f^{*r}$  is linear. We call it the right adjoint of $f$. In summary, we make the following definition.

> **Definition 29.14.** Let $E_{1}$ and $E_{2}$ be two $K$-vector spaces, and let $\phi_{1}$  : $E_{1} \times  E_{1} \to K$ and $\phi_{2}$  : $E_{2} \times  E_{2} \to K$ be two sesquilinear forms. Assume that $l_{\phi1}$ and $r_{\phi1}$ are bijective, so that $\phi_{1}$  is nondegnerate. For every linear map $f$ : $E_{1} \to E_{2}$, there exist unique linear maps $f^{*l}$  : $E_{2} \to E_{1}$ and $f^{*r}$  : $E_{2} \to E_{1}$, such that
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),for all x \in E_{1}, and all u \in E_{2}$$
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),for all x \in E_{1}, and all u \in E_{2}.$$
The map $f^{*l}$  is called the left adjoint of $f$, and the map $f^{*r}$  is called the right adjoint of $f$. If $E_{1}$ and $E_{2}$ are finite-dimensional with bases $(e_{1}, \dots  , e_{m})$ and $(f_{1}, \dots  , f_{n})$, then we can work out the matrices $A^{*l}$ and $A^{*r}$ corresponding to the left adjoint $f^{*l}$  and the right adjoint $f^{*r}$  of $f$. Assumine that $f$ is represented by the $n \times  m$ matrix $A, \phi_{1}$  is represented by the $m \times  m$ matrix $M_{1}$, and $\phi_{2}$  is represented by the $n \times  n$ matrix $M_{2}$. Since
$$\phi_{1} (x, f^{*l} (u)) = (A^{*l}u)^{*}M_{1}x = u^{*}(A^{*l})^{*}M_{1}x$$
$$\phi_{2} (f(x), u) = u^{*}M_{2}Ax$$
we find that $(A^{*l})^{*}M_{1} = M_{2}A$, that is $(A^{*l})^{*} = M_{2}AM_{1}^{-1}$  , and similarly
$$\phi_{1} (f^{*r} (u), x) = x^{*}M_{1}A^{*r}u$$
$$\phi_{2} (u, f(x)) = (Ax)^{*}M_{2}u = x^{*}A^{*}M_{2}u,$$
we have $M_{1}A^{*r} = A^{*}M_{2}$, that is $A^{*r} = (M_{1})^{-1}A^{*}M_{2}$. Thus, we obtain
$$A^{*l}= (M_{1}^{*})^{-1}A^{*}M_{2}^{*}$$
$$A^{*r}= (M_{1})^{-1}A^{*}M_{2}.$$
