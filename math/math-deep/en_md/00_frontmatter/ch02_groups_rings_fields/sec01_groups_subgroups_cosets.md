# 2.1 Groups, Subgroups, Cosets

> **Source Pages:** 21–44

The set $\mathbb{R}$ of real numbers has two operations $+ : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ (addition) and $* : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ (multiplication) satisfying properties that make $\mathbb{R}$ into an abelian group under $+$, and $\mathbb{R} - \{0\} = \mathbb{R}^*$ into an abelian group under $*$.

Before stating the formal definition of a group, we begin with some concrete examples. Many sets of geometric transformations have a group structure.

1. Translations
2. Rotations
3. Magnifications
4. Rigid motions, which combine rotations and translations
5. Reflections
6. Orthogonal transformations (the combination of rotations and reflections)
7. Rigid motions and indirect rigid motions
8. More generally, affine invertible transformations.

<!-- PAGE 22 -->

> **Example 2.1.** A translation in the plane $\mathbb{R}^2$ is a map $T_u : \mathbb{R}^2 \to \mathbb{R}^2$ specified by a vector
> $$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \in \mathbb{R}^2, \quad \text{with } u_1, u_2 \in \mathbb{R},$$
> such that the action of $T_u$ on a vector (also called point)
> $$x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in \mathbb{R}^2, \quad \text{with } x_1, x_2 \in \mathbb{R},$$
> is given by $T_u(x) = x + u$, that is,
> $$T_u(x) = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} x_1 + u_1 \\ x_2 + u_2 \end{pmatrix}.$$
> So the point $x$ in the plane ($\mathbb{R}^2$) is translated "along the vector $u$."
>
> Denote the set of translations of the plane $\mathbb{R}^2$ as $T(\mathbb{R}^2)$. Translations can be composed. Given two translations $T_u$ and $T_v$ specified by
> $$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \in \mathbb{R}^2,$$
> we can first apply $T_u$ to $x$, and then apply $T_v$ to $T_u(x)$, and we get
> $$(T_v \circ T_u)(x) = T_v(T_u(x)) = \left(\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}\right) + \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} x_1 + u_1 \\ x_2 + u_2 \end{pmatrix} + \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$$
> $$= \begin{pmatrix} (x_1 + u_1) + v_1 \\ (x_2 + u_2) + v_2 \end{pmatrix} = \begin{pmatrix} x_1 + (u_1 + v_1) \\ x_2 + (u_2 + v_2) \end{pmatrix} = T_{u+v}(x),$$
> so $T_v \circ T_u$ is defined by the vector $u + v$, which means that
> $$T_v \circ T_u = T_{u+v}.$$
>
> We have defined a binary operation
> $$\circ : T(\mathbb{R}^2) \times T(\mathbb{R}^2) \to T(\mathbb{R}^2)$$
> on the set of translations (on $\mathbb{R}^2$) given by
> $$T_v \circ T_u = T_{u+v}.$$
> Observe that
> $$T_v \circ T_u = T_u \circ T_v, \tag{Ab}$$
> <!-- PAGE 23 -->
> since $T_v \circ T_u = T_{u+v} = T_{v+u} = T_u \circ T_v$, and $u + v = v + u$ (as vectors in $\mathbb{R}^2$). We say that this operation is commutative.
>
> For $u = 0_2$, the zero vector
> $$0_2 = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
> we obtain the translation $T_{0_2}$ that does nothing, namely
> $$T_{0_2}(x) = x, \quad x \in \mathbb{R}^2.$$
> Observe that for any translation $T_u$, we have
> $$T_u \circ T_{0_2} = T_{0_2} \circ T_u = T_u. \tag{G2}$$
> We say that $T_{0_2}$ is an identity (or neutral) element for the binary operation $\circ$.
>
> For any three translations $T_u, T_v, T_w$, we have the identity
> $$(T_u \circ T_v) \circ T_w = T_u \circ (T_v \circ T_w), \tag{G1}$$
> since both are equal to $T_{u+v+w}$, because $(u + v) + w = u + (v + w)$, as vectors in $\mathbb{R}^2$. We say that $\circ$ is associative.
>
> Also observe that $T_{-u}$ is the inverse of $T_u$, in the sense that
> $$T_{-u} \circ T_u = T_{0_2} = T_u \circ T_{-u}, \tag{G3}$$
> since $T_{-u} \circ T_u = T_{-u+u} = T_{0_2} = T_{u+(-u)} = T_u \circ T_{-u}$.
>
> Since Conditions G1, G2, G3 (see Definition 2.1) hold for $\circ$ on the set $T(\mathbb{R}^2)$ of translations (of $\mathbb{R}^2$), we say that the set $T(\mathbb{R}^2)$ is a group.
>
> Because $(\mathrm{Ab})$ also holds, we say that this group is commutative or abelian. But $\mathbb{R}^2$ under addition of vectors is also an abelian group with identity element $0_2$.
>
> The map $u \mapsto T_u$ is a bijection from the group $\mathbb{R}^2$ to the group $T(\mathbb{R}^2)$ of translations on $\mathbb{R}^2$. It is a group isomorphism.
>
> Note that the elements of the group $T(\mathbb{R}^2)$ are transformations (maps from $\mathbb{R}^2$ to $\mathbb{R}^2$), but the elements of $\mathbb{R}^2$ are vectors. The generalization to $\mathbb{R}^n$ and the group of translations on $\mathbb{R}^n$ is immediate.

<!-- PAGE 24 -->

> **Example 2.2.** A point $(x, y)$ in the plane $\mathbb{R}^2$ can be defined by its polar coordinates $(r, \alpha)$, since we can write
> $$\begin{aligned} x &= r \cos \alpha \\ y &= r \sin \alpha, \end{aligned}$$
> for any
> $$\begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2,$$
> and if $(x, y) \neq (0, 0)$, then $r > 0$ and $\alpha$ are uniquely determined, if we require $0 \le \alpha < 2\pi$.
>
> Equivalently, we consider $\alpha$ modulo $2\pi$, which means that we consider $\alpha_1$ and $\alpha_2$ equivalent iff
> $$\alpha_2 - \alpha_1 = 2\pi k, \quad k \in \mathbb{Z}.$$
> We obtain the set of equivalence classes $\mathbb{R}/(2\pi\mathbb{Z})$. (It is a group under addition $\bmod\; 2\pi\mathbb{Z}$!).
>
> A rotation $R_\theta$ by the angle $\theta$ is the map $R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ given by
> $$\begin{aligned} R_\theta(0, 0) &= (0, 0) \\ R_\theta(r, \alpha) &= (r, \alpha + \theta), \quad (r \neq 0). \end{aligned}$$
> The rotation $R_\theta$ rotates the point with polar coordinates $(r, \alpha)$ by the angle $\theta$ to the point $(r, \alpha + \theta)$.
>
> Since the polar coordinates of $R_\theta(r, \alpha)$ are
> $$(r \cos(\alpha + \theta), r \sin(\alpha + \theta)),$$
> and since
> $$\begin{aligned} \cos(\alpha + \theta) &= \cos \alpha \cos \theta - \sin \alpha \sin \theta \\ \sin(\alpha + \theta) &= \sin \alpha \cos \theta + \cos \alpha \sin \theta, \end{aligned}$$
> we see that in terms of matrices,
> $$\begin{pmatrix} r \cos(\alpha + \theta) \\ r \sin(\alpha + \theta) \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} r \cos \alpha \\ r \sin \alpha \end{pmatrix}.$$
> In terms of the cartesian coordinates $(x, y)$,
> $$R_\theta \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
> Using some trigonometric identities, we check that the map
> $$\theta \mapsto M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}, \quad \theta \in \mathbb{R}/2\pi\mathbb{Z},$$
> has the property that
> $$M_\theta M_\phi = M_{\theta + \phi}.$$
> We say that $M_\theta$ is the matrix representing the rotation $R_\theta$.
> <!-- PAGE 25 -->
> We can check that Conditions G1, G2, G3 (see Definition 2.1) and $(\mathrm{Ab})$ hold, so the set of matrices of the form
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix},$$
> denoted $\mathbf{SO}(2)$, is an abelian group under matrix multiplication
> $$\cdot : \mathbf{SO}(2) \times \mathbf{SO}(2) \to \mathbf{SO}(2).$$
> Geometrically, $\mathbf{SO}(2)$ is the unit circle, denoted $S^1$. (Also the set of complex numbers of unit length,
> $$\mathbf{U}(1) = \{\cos \theta + i \sin \theta \mid \theta \in \mathbb{R}/2\pi\mathbb{Z}\}.)$$
> And recall, $\cos \theta + i \sin \theta = e^{i\theta}$.
>
> The identity element is the matrix $M_0$, with
> $$M_0 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2,$$
> and the inverse of $R_\theta$ is the rotation $R_{-\theta}$, corresponding to the matrix
> $$M_{-\theta} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix}.$$
> Note that the operation on $\mathbf{SO}(2)$ is matrix multiplication, not addition, which would yield matrices that are not rotations. Observe that the matrix $M_{-\theta}$ associated with $R_{-\theta}$ is the transpose of the matrix $M_\theta$ associated with $R_\theta$.

> **Example 2.3.** For any $r > 0$, we have the magnification $\mu_r : \mathbb{R}^2 \to \mathbb{R}^2$ of ratio $r$, given by
> $$\mu_r(x) = r \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} rx \\ ry \end{pmatrix}.$$
> We denote the set of magnifications on $\mathbb{R}^2$ by $\mathbf{Mag}(2)$. We immediately check that (for $r_1, r_2 > 0$),
> $$\mu_{r_1} \circ \mu_{r_2} = \mu_{r_2} \circ \mu_{r_1} = \mu_{r_1 * r_2},$$
> and this defines a multiplication operation $\cdot : \mathbf{Mag}(2) \times \mathbf{Mag}(2) \to \mathbf{Mag}(2)$ given by
> $$\mu_{r_1} \cdot \mu_{r_2} = \mu_{r_1 * r_2}.$$
> We can check that Conditions G1, G2, G3 (see Definition 2.1) and $(\mathrm{Ab})$ hold, so we obtain the commutative group $\mathbf{Mag}(2)$ with identity element $\mu_1$, and the inverse of $\mu_r$ is $\mu_{1/r}$.
>
> The set of all compositions $\mu_r \circ R_\theta$ corresponds to all matrices of the form
> $$\begin{pmatrix} r \cos \theta & -r \sin \theta \\ r \sin \theta & r \cos \theta \end{pmatrix}.$$
> <!-- PAGE 26 -->
> We check easily that this is the set $\mathbf{SIM}_{\mathbb{R}}(2)$ of matrices of the form
> $$\begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \quad a^2 + b^2 \neq 0.$$
> The inverse of such a matrix is
> $$\frac{1}{a^2 + b^2} \begin{pmatrix} a & b \\ -b & a \end{pmatrix}.$$
> We can check that Conditions G1, G2, G3 (see Definition 2.1) and $(\mathrm{Ab})$ hold, so the set $\mathbf{SIM}_{\mathbb{R}}(2)$ under matrix multiplication is a commutative group.

> **Example 2.4.** In addition to the rotation matrices
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix},$$
> let us add all matrices of the form
> $$\rho_\phi = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix},$$
> called reflections, and make all possible products.
>
> Contrary to what we might think, reflections are not rotation matrices. For one thing, if you know what the determinant of a matrix is, rotation matrices have determinant $+1$, but reflections have determinant $-1$. Also if we consider the special reflection for $\phi = 0$,
> $$\rho_0 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},$$
> the reflection about the $x$-axis, then we have
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi & -\sin \phi \\ \sin \phi & \cos \phi \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = M_\phi \rho_0,$$
> so
> $$\rho_\phi = M_\phi \rho_0.$$
> We will see later that $\rho_\phi = M_{\phi/2} \rho_0 M_{-\phi/2}$, namely
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ -\sin \phi/2 & \cos \phi/2 \end{pmatrix},$$
> which means that geometrically, $\rho_\phi$ is the reflection about the line corresponding to the angle $\phi/2$.
> <!-- PAGE 27 -->
> Observe that since
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix}^2 = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix}$$
> $$= \begin{pmatrix} \cos^2 \phi + \sin^2 \phi & \cos \phi \sin \phi - \sin \phi \cos \phi \\ \sin \phi \cos \phi - \cos \phi \sin \phi & \sin^2 \phi + \cos^2 \phi \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},$$
> we have
> $$\rho_\phi^2 = \rho_\phi \rho_\phi = I_2,$$
> so the inverse of a reflection is itself.
>
> We also easily verify that
> $$\rho_0 M_\theta \rho_0 = M_{-\theta}.$$
> Indeed,
> $$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
> $$= \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix} = \begin{pmatrix} \cos(-\theta) & -\sin(-\theta) \\ \sin(-\theta) & \cos(-\theta) \end{pmatrix}.$$
>
> Let $\mathbf{O}(2)$ be the set given by
> $$\begin{aligned} \mathbf{O}(2) &= \mathbf{SO}(2) \cup \{M_\phi \rho_0 \mid M_\phi \in \mathbf{SO}(2)\} \\ &= \mathbf{SO}(2) \cup \{\rho_\phi \mid \phi \in \mathbb{R}/(2\pi\mathbb{Z})\}. \end{aligned}$$
> Since $\rho_0 \rho_0 = I_2$ and $\rho_0 M_\theta \rho_0 = M_{-\theta}$, the following equations hold:
> $$\begin{aligned} M_\theta M_\phi &= M_{\theta + \phi} \\ M_\theta \rho_\phi &= M_\theta (M_\phi \rho_0) = (M_\theta M_\phi)\rho_0 = M_{\theta + \phi}\rho_0 = \rho_{\theta + \phi} \\ \rho_\theta M_\phi &= (M_\theta \rho_0)M_\phi = (M_\theta \rho_0)(M_\phi \rho_0 \rho_0) = M_\theta(\rho_0 M_\phi \rho_0)\rho_0 \\ &= (M_\theta M_{-\phi})\rho_0 = M_{\theta - \phi}\rho_0 = \rho_{\theta - \phi} \\ \rho_\theta \rho_\phi &= (M_\theta \rho_0)(M_\phi \rho_0) = M_\theta(\rho_0 M_\phi \rho_0) \\ &= M_\theta M_{-\phi} = M_{\theta - \phi}. \end{aligned}$$
> As a summary,
> $$\begin{aligned} M_\theta M_\phi &= M_{\theta + \phi} \tag{RR} \\ M_\theta \rho_\phi &= \rho_{\theta + \phi} \tag{$R\rho$} \\ \rho_\theta M_\phi &= \rho_{\theta - \phi} \tag{$\rho R$} \\ \rho_\theta \rho_\phi &= M_{\theta - \phi}. \tag{$\rho\rho$} \end{aligned}$$
> Using the above equations, we can check that Conditions G1, G2, G3 (see Definition 2.1) hold, so $\mathbf{O}(2)$ is a group under matrix multiplication. But the group $\mathbf{O}(2)$ is not commutative! Compare $\rho_0 M_\phi$ and $M_\phi \rho_0$.
> <!-- PAGE 28 -->
> The group $\mathbf{O}(2)$ is the semidirect product of the group $\mathbf{SO}(2)$ and the group $\{I_2, \rho_0\}$.
>
> Using ($\rho R$) and ($R\rho$), we have
> $$M_{\phi/2}\rho_0 M_{-\phi/2} = M_{\phi/2}\rho_{\phi/2} = \rho_{\phi/2 + \phi/2} = \rho_\phi,$$
> thus
> $$\rho_\phi = M_{\phi/2}\rho_0 M_{-\phi/2},$$
> or more explicitly
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ -\sin \phi/2 & \cos \phi/2 \end{pmatrix}.$$
> We say that the matrix $\rho_\phi$ is diagonalized.
>
> Geometrically, this is a rotation by the angle $-\phi/2$ followed by the reflection about the $x$-axis, followed by the rotation by the angle $\phi/2$.
>
> Given a point $p$, this amounts to rotating by $-\phi/2$ the point $p$ and the coordinate system whose $x$-axis is the line making an angle $\phi/2$ with the $x$-axis and whose $y$-axis is orthogonal to this line, so that this coordinate system (making an angle $\phi/2$ with the standard one) is now identical to the standard coordinate system, then perform on $M_{-\phi/2}(p)$ the reflection about the $x$-axis, and finally rotate $\rho_0(M_{-\phi/2}(p))$ and the standard coordinate system by $\phi/2$.
>
> The above shows that $\rho_\phi$ is a reflection with respect to the line making an angle $\phi/2$ with the $x$-axis.
>
> By ($\rho R$), we obtain
> $$\rho_\phi M_{\phi/2} = \rho_{\phi/2},$$
> or
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ \sin \phi/2 & -\cos \phi/2 \end{pmatrix},$$
> which shows that
> $$\begin{aligned} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix} &= \begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix} \\ \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix} &= -\begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix}. \end{aligned}$$
> <!-- PAGE 29 -->
> We say that $\begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix}$ is an eigenvector of $\rho_\phi$ for the eigenvalue $1$ and $\begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix}$ is an eigenvector of $\rho_\phi$ for the eigenvalue $-1$.
>
> In contrast, we will see later that a rotation matrix
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
> has complex eigenvalues $\cos \theta \pm i \sin \theta$.
>
> From ($\rho\rho$), we have
> $$\rho_{\phi + \theta}\rho_\phi = M_\theta,$$
> which shows that every rotation by $\theta$ can be written as the composition of two reflections whose axes of reflection correspond to lines making angles $\phi/2$ and $\phi/2 + \theta/2$ with respect to the $x$-axis, so the two axes of reflection make an angle $\theta/2$.
>
> Geometrically, $\mathbf{O}(2)$ is the disjoint union of two circles $S^1$.

> **Example 2.5.** Consider the set $\mathbf{SE}(2)$, of maps, $T_u \circ R_\theta$, obtained by composing a rotation and a translation.
>
> Given two such maps $T_u \circ R_\theta$ and $T_v \circ R_\phi$, we have
> $$\begin{aligned} (T_v \circ R_\phi)((T_u \circ R_\theta)(x)) &= (T_v \circ R_\phi)(R_\theta(x) + u) \\ &= R_\phi(R_\theta(x)) + R_\phi(u) + v \\ &= R_{\phi + \theta}(x) + R_\phi(u) + v, \end{aligned}$$
> so $(T_v \circ R_\phi) \circ (T_u \circ R_\theta)$ also belongs to $\mathbf{SE}(2)$.
>
> If we denote $T_u \circ R_\theta$ as $(u, R_\theta)$, we obtain a multiplication operation $\cdot : \mathbf{SE}(2) \times \mathbf{SE}(2) \to \mathbf{SE}(2)$ on the set $\mathbf{SE}(2)$ given by
> $$(v, R_\phi) \cdot (u, R_\theta) = (v + R_\phi(u), R_{\phi + \theta}).$$
> Observe the action of $R_\phi$ on $u$. It turns out that $\mathbf{SE}(2)$ is a semidirect product of $\mathbb{R}^2$ and $\mathbf{SO}(2)$.
>
> Note that the elements of $\mathbf{SE}(2)$ are transformations from $\mathbb{R}^2$ to $\mathbb{R}^2$, not matrices. A matrix representation is possible using $3 \times 3$-matrices; see Section 24.7.
>
> Translations are of the form $(u, R_0)$ (no rotation) and rotations are of the form $(0_2, R_\theta)$ (no translation). The identity element is $(0_2, R_0)$, and the inverse of $(u, R_\theta)$ is $(-R_{-\theta}(u), R_{-\theta})$. We can check that Conditions G1, G2, G3 (see Definition 2.1) hold, so $\mathbf{SE}(2)$ with the above multiplication is a group.
>
> The group $\mathbf{SE}(2)$ is not commutative. Consider the action of $R_\theta \circ T_{(1,0)}$ and the action of $T_{(1,0)} \circ R_\theta$ on the origin.
> <!-- PAGE 30 -->
> The maps in $\mathbf{SE}(2)$ are affine, and not linear, unless $u = 0$. Geometrically, $\mathbf{SE}(2)$ is the cylinder $S^1 \times \mathbb{R}^2$. It is not a compact space.
>
> The same construction can be done with pairs $(u, S)$, where $S \in \mathbf{O}(2)$ instead of $\mathbf{SO}(2)$. We obtain the group $\mathbf{E}(2)$ ($\mathbf{E}$ for Euclidean) of rigid motions of the plane ($\mathbb{R}^2$).
>
> A map of the form $T_u \circ \rho_\phi$ is called an indirect motion. Technically, in the above expression, we should use the linear transformation from $\mathbb{R}^2$ to itself defined by the matrix $\rho_\phi$.
>
> It can be shown that $\mathbf{E}(2)$ consists exactly of all functions $f : \mathbb{R}^2 \to \mathbb{R}^2$ that preserve the Euclidean distance. See Proposition 12.13 (not so easy to prove!).
>
> The matrices in $\mathbf{SO}(2)$ and $\mathbf{O}(2)$ have the property that
> $$SS^\top = S^\top S = I_2,$$
> where $S^\top$ is the transpose of $S$ (swap rows and columns). Such matrices are called orthogonal matrices.
>
> To generalize rotations and reflections to $\mathbb{R}^n$ with $n \ge 3$, we need to consider orthogonal matrices. For $n = 3$, this has been investigated extensively (Euler angles, quaternions, exponential representation, ...).

We are now ready for the formal definition of a group.

> **Definition 2.1.** A *group* is a set $G$ equipped with a binary operation $\cdot : G \times G \to G$ that associates an element $a \cdot b \in G$ to every pair of elements $a, b \in G$, and having the following properties: $\cdot$ is associative, has an identity element $e \in G$, and every element in $G$ is invertible (w.r.t. $\cdot$). More explicitly, this means that the following equations hold for all $a, b, c \in G$:
> - **(G1)** $a \cdot (b \cdot c) = (a \cdot b) \cdot c$. *(associativity)*;
> - **(G2)** $a \cdot e = e \cdot a = a$. *(identity)*;
> - **(G3)** For every $a \in G$, there is some $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$. *(inverse)*.
>
> A group $G$ is *abelian* (or *commutative*) if
> - **(Ab)** $a \cdot b = b \cdot a$ for all $a, b \in G$.

A set $M$ together with an operation $\cdot : M \times M \to M$ and an element $e$ satisfying only Conditions (G1) and (G2) is called a *monoid*. For example, the set $\mathbb{N} = \{0, 1, \dots, n, \dots\}$ of natural numbers is a (commutative) monoid under addition. However, it is not a group.

Some examples of groups are given below.

<!-- PAGE 31 -->

> **Example 2.6.**
> 1. The set $\mathbb{Z} = \{\dots, -n, \dots, -1, 0, 1, \dots, n, \dots\}$ of integers is an abelian group under addition, with identity element $0$. However, $\mathbb{Z}^* = \mathbb{Z} - \{0\}$ is not a group under multiplication.
> 2. The set $\mathbb{Q}$ of rational numbers (fractions $p/q$ with $p, q \in \mathbb{Z}$ and $q \neq 0$) is an abelian group under addition, with identity element $0$. The set $\mathbb{Q}^* = \mathbb{Q} - \{0\}$ is also an abelian group under multiplication, with identity element $1$.
> 3. Given any nonempty set $S$, the set of bijections $f : S \to S$, also called *permutations* of $S$, is a group under function composition (i.e., the multiplication of $f$ and $g$ is the composition $g \circ f$), with identity element the identity function $\mathrm{id}_S$. This group is not abelian as soon as $S$ has more than two elements. The permutation group of the set $S = \{1, \dots, n\}$ is often denoted $\mathfrak{S}_n$ and called the *symmetric group* on $n$ elements.
> 4. For any positive integer $p \in \mathbb{N}$, define a relation on $\mathbb{Z}$, denoted $m \equiv n \pmod{p}$, as follows:
>    $$m \equiv n \pmod{p} \quad \text{iff} \quad m - n = kp \quad \text{for some } k \in \mathbb{Z}.$$
>    The reader will easily check that this is an equivalence relation, and, moreover, it is compatible with respect to addition and multiplication, which means that if $m_1 \equiv n_1 \pmod{p}$ and $m_2 \equiv n_2 \pmod{p}$, then $m_1 + m_2 \equiv n_1 + n_2 \pmod{p}$ and $m_1 m_2 \equiv n_1 n_2 \pmod{p}$. Consequently, we can define an addition operation and a multiplication operation on the set of equivalence classes ($\bmod\; p$):
>    $$[m] + [n] = [m + n]$$
>    and
>    $$[m] \cdot [n] = [mn].$$
>    The reader will easily check that addition of residue classes ($\bmod\; p$) induces an abelian group structure with $[0]$ as zero. This group is denoted $\mathbb{Z}/p\mathbb{Z}$.
> 5. The set $\mathbb{R}[X]$ of all polynomials in one variable $X$ with real coefficients,
>    $$P(X) = a_0 X^n + a_1 X^{n-1} + \dots + a_{n-1}X + a_n,$$
>    (with $a_i \in \mathbb{R}$), is an abelian group under addition of polynomials. The identity element is the zero polynomial.
> 6. The set of $n \times n$ invertible matrices with real (or complex) coefficients is a group under matrix multiplication, with identity element the identity matrix $I_n$. This group is called the *general linear group* and is usually denoted by $\mathbf{GL}(n, \mathbb{R})$ (or $\mathbf{GL}(n, \mathbb{C})$).
> 7. The set of $n \times n$ invertible matrices $A$ with real (or complex) coefficients such that $\det(A) = 1$ is a group under matrix multiplication, with identity element the identity matrix $I_n$. This group is called the *special linear group* and is usually denoted by $\mathbf{SL}(n, \mathbb{R})$ (or $\mathbf{SL}(n, \mathbb{C})$).
> <!-- PAGE 32 -->
> 8. The set of $n \times n$ matrices $Q$ with real coefficients such that
>    $$Q Q^\top = Q^\top Q = I_n$$
>    is a group under matrix multiplication, with identity element the identity matrix $I_n$; we have $Q^{-1} = Q^\top$. This group is called the *orthogonal group* and is usually denoted by $\mathbf{O}(n)$.
> 9. The set of $n \times n$ invertible matrices $Q$ with real coefficients such that
>    $$Q Q^\top = Q^\top Q = I_n \quad \text{and} \quad \det(Q) = 1$$
>    is a group under matrix multiplication, with identity element the identity matrix $I_n$; as in (6), we have $Q^{-1} = Q^\top$. This group is called the *special orthogonal group* or *rotation group* and is usually denoted by $\mathbf{SO}(n)$.
>
> The groups in (6)–(9) are nonabelian for $n \ge 2$, except for $\mathbf{SO}(2)$ which is abelian (but $\mathbf{O}(2)$ is not abelian).

It is customary to denote the operation of an abelian group $G$ by $+$, in which case the inverse $a^{-1}$ of an element $a \in G$ is denoted by $-a$.

The identity element of a group is unique. In fact, we can prove a more general fact:

> **Proposition 2.1.** For any binary operation $\cdot : M \times M \to M$, if $e' \in M$ is a left identity and if $e'' \in M$ is a right identity, which means that
> $$e' \cdot a = a \quad \text{for all } a \in M \tag{G2l}$$
> and
> $$a \cdot e'' = a \quad \text{for all } a \in M, \tag{G2r}$$
> then $e' = e''$.

*Proof.* If we let $a = e''$ in equation (G2l), we get
$$e' \cdot e'' = e'',$$
and if we let $a = e'$ in equation (G2r), we get
$$e' \cdot e'' = e',$$
and thus
$$e' = e' \cdot e'' = e'',$$
as claimed. $\square$

<!-- PAGE 33 -->

Proposition 2.1 implies that the identity element of a monoid is unique, and since every group is a monoid, the identity element of a group is unique. Furthermore, every element in a group has a unique inverse. This is a consequence of a slightly more general fact:

> **Proposition 2.2.** In a monoid $M$ with identity element $e$, if some element $a \in M$ has some left inverse $a' \in M$ and some right inverse $a'' \in M$, which means that
> $$a' \cdot a = e \tag{G3l}$$
> and
> $$a \cdot a'' = e, \tag{G3r}$$
> then $a' = a''$.

*Proof.* Using (G3l) and the fact that $e$ is an identity element, we have
$$(a' \cdot a) \cdot a'' = e \cdot a'' = a''.$$
Similarly, using (G3r) and the fact that $e$ is an identity element, we have
$$a' \cdot (a \cdot a'') = a' \cdot e = a'.$$
However, since $M$ is a monoid, the operation $\cdot$ is associative, so
$$a' = a' \cdot (a \cdot a'') = (a' \cdot a) \cdot a'' = a'',$$
as claimed. $\square$

**Remark:** Axioms (G2) and (G3) can be weakened a bit by requiring only (G2r) (the existence of a right identity) and (G3r) (the existence of a right inverse for every element) (or (G2l) and (G3l)). It is a good exercise to prove that the group axioms (G2) and (G3) follow from (G2r) and (G3r).

Another important property about inverse elements in monoids is stated below.

> **Proposition 2.3.** In a monoid $M$ with identity element $e$, if $a$ and $b$ are invertible elements of $M$, where $a^{-1}$ is the inverse of $a$ and $b^{-1}$ is the inverse of $b$, then $ab$ is invertible and its inverse is given by $(ab)^{-1} = b^{-1}a^{-1}$.

*Proof.* Using associativity and the fact that $e$ is the identity element we have
$$\begin{aligned}
(ab)(b^{-1}a^{-1}) &= a(b(b^{-1}a^{-1})) && \text{associativity} \\
&= a((bb^{-1})a^{-1}) && \text{associativity} \\
&= a(ea^{-1}) && b^{-1} \text{ is the inverse of } b \\
&= aa^{-1} && e \text{ is the identity element} \\
&= e. && a^{-1} \text{ is the inverse of } a.
\end{aligned}$$
<!-- PAGE 34 -->
We also have
$$\begin{aligned}
(b^{-1}a^{-1})(ab) &= b^{-1}(a^{-1}(ab)) && \text{associativity} \\
&= b^{-1}((a^{-1}a)b) && \text{associativity} \\
&= b^{-1}(eb) && a^{-1} \text{ is the inverse of } a \\
&= b^{-1}b && e \text{ is the identity element} \\
&= e. && b^{-1} \text{ is the inverse of } b.
\end{aligned}$$
Therefore $b^{-1}a^{-1}$ is the inverse of $ab$. $\square$

Observe that the inverse of $ba$ is $a^{-1}b^{-1}$. Proposition 2.3 implies that the set of invertible elements of a monoid $M$ is a group, also with identity element $e$.

> **Definition 2.2.** If a group $G$ has a finite number $n$ of elements, we say that $G$ is a group of *order* $n$. If $G$ is infinite, we say that $G$ has *infinite order*. The order of a group is usually denoted by $|G|$ (if $G$ is finite).

Given a group $G$, for any two subsets $R, S \subseteq G$, we let
$$RS = \{r \cdot s \mid r \in R, s \in S\}.$$
In particular, for any $g \in G$, if $R = \{g\}$, we write
$$gS = \{g \cdot s \mid s \in S\},$$
and similarly, if $S = \{g\}$, we write
$$Rg = \{r \cdot g \mid r \in R\}.$$
From now on, we will drop the multiplication sign and write $g_1 g_2$ for $g_1 \cdot g_2$.

> **Definition 2.3.** Let $G$ be a group. For any $g \in G$, define $L_g$, the *left translation by $g$*, by $L_g(a) = ga$, for all $a \in G$, and $R_g$, the *right translation by $g$*, by $R_g(a) = ag$, for all $a \in G$.

The following simple fact is often used.

> **Proposition 2.4.** Given a group $G$, the translations $L_g$ and $R_g$ are bijections.

*Proof.* We show this for $L_g$, the proof for $R_g$ being similar.
If $L_g(a) = L_g(b)$, then $ga = gb$, and multiplying on the left by $g^{-1}$, we get $a = b$, so $L_g$ is injective. For any $b \in G$, we have $L_g(g^{-1}b) = gg^{-1}b = b$, so $L_g$ is surjective. Therefore, $L_g$ is bijective. $\square$

> **Definition 2.4.** Given a group $G$, a subset $H$ of $G$ is a *subgroup* of $G$ iff
> 1. The identity element $e$ of $G$ also belongs to $H$ ($e \in H$);
> <!-- PAGE 35 -->
> 2. For all $h_1, h_2 \in H$, we have $h_1 h_2 \in H$;
> 3. For all $h \in H$, we have $h^{-1} \in H$.

The proof of the following proposition is left as an exercise.

> **Proposition 2.5.** Given a group $G$, a subset $H \subseteq G$ is a subgroup of $G$ iff $H$ is nonempty and whenever $h_1, h_2 \in H$, then $h_1 h_2^{-1} \in H$.

If the group $G$ is finite, then the following criterion can be used.

> **Proposition 2.6.** Given a finite group $G$, a subset $H \subseteq G$ is a subgroup of $G$ iff
> 1. $e \in H$;
> 2. $H$ is closed under multiplication.

*Proof.* We just have to prove that Condition (3) of Definition 2.4 holds. For any $a \in H$, since the left translation $L_a$ is bijective, its restriction to $H$ is injective, and since $H$ is finite, it is also bijective. Since $e \in H$, there is a unique $b \in H$ such that $L_a(b) = ab = e$. However, if $a^{-1}$ is the inverse of $a$ in $G$, we also have $L_a(a^{-1}) = aa^{-1} = e$, and by injectivity of $L_a$, we have $a^{-1} = b \in H$. $\square$

> **Example 2.7.**
> 1. For any integer $n \in \mathbb{Z}$, the set
>    $$n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}$$
>    is a subgroup of the group $\mathbb{Z}$.
> 2. The set of matrices
>    $$\mathbf{GL}^+(n, \mathbb{R}) = \{A \in \mathbf{GL}(n, \mathbb{R}) \mid \det(A) > 0\}$$
>    is a subgroup of the group $\mathbf{GL}(n, \mathbb{R})$.
> 3. The group $\mathbf{SL}(n, \mathbb{R})$ is a subgroup of the group $\mathbf{GL}(n, \mathbb{R})$.
> 4. The group $\mathbf{O}(n)$ is a subgroup of the group $\mathbf{GL}(n, \mathbb{R})$.
> 5. The group $\mathbf{SO}(n)$ is a subgroup of the group $\mathbf{O}(n)$, and a subgroup of the group $\mathbf{SL}(n, \mathbb{R})$.
> <!-- PAGE 36 -->
> 6. It is not hard to show that every $2 \times 2$ rotation matrix $R \in \mathbf{SO}(2)$ can be written as
>    $$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}, \quad \text{with } 0 \le \theta < 2\pi.$$
>    Then $\mathbf{SO}(2)$ can be considered as a subgroup of $\mathbf{SO}(3)$ by viewing the matrix
>    $$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
>    as the matrix
>    $$Q = \begin{pmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
> 7. The set of $2 \times 2$ upper-triangular matrices of the form
>    $$\begin{pmatrix} a & b \\ 0 & c \end{pmatrix}, \quad a, b, c \in \mathbb{R},\; a, c \neq 0$$
>    is a subgroup of the group $\mathbf{GL}(2, \mathbb{R})$.
> 8. The set $V$ consisting of the four matrices
>    $$\begin{pmatrix} \pm 1 & 0 \\ 0 & \pm 1 \end{pmatrix}$$
>    is a subgroup of the group $\mathbf{GL}(2, \mathbb{R})$ called the *Klein four-group*.

> **Definition 2.5.** If $H$ is a subgroup of $G$ and $g \in G$ is any element, the sets of the form $gH$ are called *left cosets* of $H$ in $G$ and the sets of the form $Hg$ are called *right cosets* of $H$ in $G$. The left cosets (resp. right cosets) of $H$ induce an equivalence relation $\sim$ defined as follows: For all $g_1, g_2 \in G$,
> $$g_1 \sim g_2 \quad \text{iff} \quad g_1 H = g_2 H$$
> (resp. $g_1 \sim g_2$ iff $H g_1 = H g_2$). Obviously, $\sim$ is an equivalence relation.

Now, we claim the following fact:

> **Proposition 2.7.** Given a group $G$ and any subgroup $H$ of $G$, we have $g_1 H = g_2 H$ iff $g_2^{-1} g_1 H = H$ iff $g_2^{-1} g_1 \in H$, for all $g_1, g_2 \in G$.

*Proof.* If we apply the bijection $L_{g_2^{-1}}$ to both $g_1 H$ and $g_2 H$ we get $L_{g_2^{-1}}(g_1 H) = g_2^{-1} g_1 H$ and $L_{g_2^{-1}}(g_2 H) = H$, so $g_1 H = g_2 H$ iff $g_2^{-1} g_1 H = H$. If $g_2^{-1} g_1 H = H$, since $1 \in H$, we get $g_2^{-1} g_1 \in H$. Conversely, if $g_2^{-1} g_1 \in H$, since $H$ is a group, the left translation $L_{g_2^{-1} g_1}$ is a bijection of $H$, so $g_2^{-1} g_1 H = H$. Thus, $g_2^{-1} g_1 H = H$ iff $g_2^{-1} g_1 \in H$. $\square$

<!-- PAGE 37 -->

It follows that the equivalence class of an element $g \in G$ is the coset $gH$ (resp. $Hg$). Since $L_g$ is a bijection between $H$ and $gH$, the cosets $gH$ all have the same cardinality. The map $L_{g^{-1}} \circ R_g$ is a bijection between the left coset $gH$ and the right coset $Hg$, so they also have the same cardinality. Since the distinct cosets $gH$ form a partition of $G$, we obtain the following fact:

> **Proposition 2.8.** *(Lagrange)* For any finite group $G$ and any subgroup $H$ of $G$, the order $h$ of $H$ divides the order $n$ of $G$.

> **Definition 2.6.** Given a finite group $G$ and a subgroup $H$ of $G$, if $n = |G|$ and $h = |H|$, then the ratio $n/h$ is denoted by $(G : H)$ and is called the *index of $H$ in $G$*.

The index $(G : H)$ is the number of left (and right) cosets of $H$ in $G$. Proposition 2.8 can be stated as
$$|G| = (G : H)|H|.$$
The set of left cosets of $H$ in $G$ (which, in general, is not a group) is denoted $G/H$. The "points" of $G/H$ are obtained by "collapsing" all the elements in a coset into a single element.

> **Example 2.8.**
> 1. Let $n$ be any positive integer, and consider the subgroup $n\mathbb{Z}$ of $\mathbb{Z}$ (under addition). The coset of any integer $m \in \mathbb{Z}$ is
>    $$m + n\mathbb{Z} = \{m + nk \mid k \in \mathbb{Z}\}.$$
>    In particular, the coset of $0$ is the set $n\mathbb{Z}$. By dividing $m$ by $n$, we have $m = nq + r$ for some unique $r$ such that $0 \le r \le n - 1$. But then we see that $r$ is the smallest nonnegative element of the coset $m + n\mathbb{Z}$. This implies that there is a bijection between the cosets of the subgroup $n\mathbb{Z}$ of $\mathbb{Z}$ and the set of residues $\{0, 1, \dots, n - 1\}$ modulo $n$, or equivalently a bijection with $\mathbb{Z}/n\mathbb{Z}$.
> 2. The cosets of $\mathbf{SL}(n, \mathbb{R})$ in $\mathbf{GL}(n, \mathbb{R})$ are the sets of matrices
>    $$A\mathbf{SL}(n, \mathbb{R}) = \{AB \mid B \in \mathbf{SL}(n, \mathbb{R})\}, \quad A \in \mathbf{GL}(n, \mathbb{R}).$$
>    Since $A$ is invertible, $\det(A) \neq 0$, and we can write $A = (\det(A))^{1/n}((\det(A))^{-1/n}A)$ if $\det(A) > 0$ and $A = (-\det(A))^{1/n}((-\det(A))^{-1/n}A)$ if $\det(A) < 0$. But we have $(\det(A))^{-1/n}A \in \mathbf{SL}(n, \mathbb{R})$ if $\det(A) > 0$ and $-(-\det(A))^{-1/n}A \in \mathbf{SL}(n, \mathbb{R})$ if $\det(A) < 0$, so the coset $A\mathbf{SL}(n, \mathbb{R})$ contains the matrix
>    $$\begin{aligned} (\det(A))^{1/n}I_n \quad &\text{if } \det(A) > 0, \\ -(-\det(A))^{1/n}I_n \quad &\text{if } \det(A) < 0. \end{aligned}$$
>    It follows that there is a bijection between the cosets of $\mathbf{SL}(n, \mathbb{R})$ in $\mathbf{GL}(n, \mathbb{R})$ and $\mathbb{R}^*$.
> <!-- PAGE 38 -->
> 3. The cosets of $\mathbf{SO}(n)$ in $\mathbf{GL}^+(n, \mathbb{R})$ are the sets of matrices
>    $$A\mathbf{SO}(n) = \{AQ \mid Q \in \mathbf{SO}(n)\}, \quad A \in \mathbf{GL}^+(n, \mathbb{R}).$$
>    It can be shown (using the polar form for matrices) that there is a bijection between the cosets of $\mathbf{SO}(n)$ in $\mathbf{GL}^+(n, \mathbb{R})$ and the set of $n \times n$ symmetric, positive, definite matrices; these are the symmetric matrices whose eigenvalues are strictly positive.
> 4. The cosets of $\mathbf{SO}(2)$ in $\mathbf{SO}(3)$ are the sets of matrices
>    $$Q\mathbf{SO}(2) = \{QR \mid R \in \mathbf{SO}(2)\}, \quad Q \in \mathbf{SO}(3).$$
>    The group $\mathbf{SO}(3)$ moves the points on the sphere $S^2$ in $\mathbb{R}^3$, namely for any $x \in S^2$,
>    $$x \mapsto Qx \quad \text{for any rotation } Q \in \mathbf{SO}(3).$$
>    Here,
>    $$S^2 = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + z^2 = 1\}.$$
>    Let $N = (0, 0, 1)$ be the north pole on the sphere $S^2$. Then it is not hard to show that $\mathbf{SO}(2)$ is precisely the subgroup of $\mathbf{SO}(3)$ that leaves $N$ fixed. As a consequence, all rotations $QR$ in the coset $Q\mathbf{SO}(2)$ map $N$ to the same point $QN \in S^2$, and it can be shown that there is a bijection between the cosets of $\mathbf{SO}(2)$ in $\mathbf{SO}(3)$ and the points on $S^2$. The surjectivity of this map has to do with the fact that the action of $\mathbf{SO}(3)$ on $S^2$ is transitive, which means that for any point $x \in S^2$, there is some rotation $Q \in \mathbf{SO}(3)$ such that $QN = x$.

It is tempting to define a multiplication operation on left cosets (or right cosets) by setting
$$(g_1 H)(g_2 H) = (g_1 g_2)H,$$
but this operation is not well defined in general, unless the subgroup $H$ possesses a special property. In Example 2.8, it is possible to define multiplication of cosets in (1), but it is not possible in (2) and (3).

The property of the subgroup $H$ that allows defining a multiplication operation on left cosets is typical of the kernels of group homomorphisms, so we are led to the following definition.

> **Definition 2.7.** Given any two groups $G$ and $G'$, a function $\phi : G \to G'$ is a *homomorphism* iff
> $$\phi(g_1 g_2) = \phi(g_1)\phi(g_2), \quad \text{for all } g_1, g_2 \in G.$$

Taking $g_1 = g_2 = e$ (in $G$), we see that
$$\phi(e) = e',$$
and taking $g_1 = g$ and $g_2 = g^{-1}$, we see that
$$\phi(g^{-1}) = (\phi(g))^{-1}.$$

<!-- PAGE 39 -->

> **Example 2.9.**
> 1. The map $\phi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ given by $\phi(m) = m \bmod n$ for all $m \in \mathbb{Z}$ is a homomorphism.
> 2. The map $\det : \mathbf{GL}(n, \mathbb{R}) \to \mathbb{R}^*$ is a homomorphism because $\det(AB) = \det(A)\det(B)$ for any two matrices $A, B$. Similarly, the map $\det : \mathbf{O}(n) \to \mathbb{R}^*$ is a homomorphism.

If $\phi : G \to G'$ and $\psi : G' \to G''$ are group homomorphisms, then $\psi \circ \phi : G \to G''$ is also a homomorphism. If $\phi : G \to G'$ is a homomorphism of groups, and if $H \subseteq G$, $H' \subseteq G'$ are two subgroups, then it is easily checked that
$$\operatorname{Im} \phi = \phi(H) = \{\phi(g) \mid g \in H\}$$
is a subgroup of $G'$ and
$$\phi^{-1}(H') = \{g \in G \mid \phi(g) \in H'\}$$
is a subgroup of $G$. In particular, when $H' = \{e'\}$, we obtain the kernel, $\operatorname{Ker} \phi$, of $\phi$.

> **Definition 2.8.** If $\phi : G \to G'$ is a homomorphism of groups, and if $H \subseteq G$ is a subgroup of $G$, then the subgroup of $G'$,
> $$\operatorname{Im} \phi = \phi(H) = \{\phi(g) \mid g \in H\},$$
> is called the *image of $H$ by $\phi$*, and the subgroup of $G$,
> $$\operatorname{Ker} \phi = \{g \in G \mid \phi(g) = e'\},$$
> is called the *kernel of $\phi$*.

> **Example 2.10.**
> 1. The kernel of the homomorphism $\phi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ from Example 2.9 is $n\mathbb{Z}$.
> 2. The kernel of the homomorphism $\det : \mathbf{GL}(n, \mathbb{R}) \to \mathbb{R}^*$ is $\mathbf{SL}(n, \mathbb{R})$. Similarly, the kernel of the homomorphism $\det : \mathbf{O}(n) \to \mathbb{R}^*$ is $\mathbf{SO}(n)$.

The following characterization of the injectivity of a group homomorphism is used all the time.

> **Proposition 2.9.** If $\phi : G \to G'$ is a homomorphism of groups, then $\phi : G \to G'$ is injective iff $\operatorname{Ker} \phi = \{e\}$. (We also write $\operatorname{Ker} \phi = (0)$.)

*Proof.* Assume $\phi$ is injective. Since $\phi(e) = e'$, if $\phi(g) = e'$, then $\phi(g) = \phi(e)$, and by injectivity of $\phi$ we must have $g = e$, so $\operatorname{Ker} \phi = \{e\}$.

Conversely, assume that $\operatorname{Ker} \phi = \{e\}$. If $\phi(g_1) = \phi(g_2)$, then by multiplication on the left by $(\phi(g_1))^{-1}$ we get
$$e' = (\phi(g_1))^{-1}\phi(g_1) = (\phi(g_1))^{-1}\phi(g_2),$$
<!-- PAGE 40 -->
and since $\phi$ is a homomorphism $(\phi(g_1))^{-1} = \phi(g_1^{-1})$, so
$$e' = (\phi(g_1))^{-1}\phi(g_2) = \phi(g_1^{-1})\phi(g_2) = \phi(g_1^{-1}g_2).$$
This shows that $g_1^{-1}g_2 \in \operatorname{Ker} \phi$, but since $\operatorname{Ker} \phi = \{e\}$ we have $g_1^{-1}g_2 = e$, and thus $g_2 = g_1$, proving that $\phi$ is injective. $\square$

The maps $g \mapsto L_g$ (where $L_g$ is left translation by $g$) and $g \mapsto R_g$ (where $R_g$ is right translation by $g$) are injective homomorphisms of $G$ into the group of bijections of $G$ (because $L_{g_1 g_2} = L_{g_1} \circ L_{g_2}$ and $R_{g_1 g_2} = R_{g_2} \circ R_{g_1}$, and the kernels of these homomorphisms are $\{e\}$).

> **Definition 2.9.** We say that a group homomorphism $\phi : G \to G'$ is an *isomorphism* if there is a homomorphism $\psi : G' \to G$, so that
> $$\psi \circ \phi = \mathrm{id}_G \quad \text{and} \quad \phi \circ \psi = \mathrm{id}_{G'}. \tag{$\dagger$}$$
> If $\phi$ is an isomorphism we say that the groups $G$ and $G'$ are *isomorphic*. When $G' = G$, a group isomorphism is called an *automorphism*.

The reasoning used in the proof of Proposition 2.2 shows that if a group homomorphism $\phi : G \to G'$ is an isomorphism, then the homomorphism $\psi : G' \to G$ satisfying Condition ($\dagger$) is unique. This homomorphism is denoted $\phi^{-1}$.

Suppose $\phi : G \to G'$ is a bijective homomorphism, and let $\phi^{-1}$ be the inverse of $\phi$ (as a function). Then for all $a, b \in G'$, we have
$$\phi(\phi^{-1}(a)\phi^{-1}(b)) = \phi(\phi^{-1}(a))\phi(\phi^{-1}(b)) = ab,$$
and so
$$\phi^{-1}(ab) = \phi^{-1}(a)\phi^{-1}(b),$$
which proves that $\phi^{-1}$ is a homomorphism. Therefore, we proved the following fact.

> **Proposition 2.10.** A bijective group homomorphism $\phi : G \to G'$ is an isomorphism.

Observe that the property
$$gH = Hg, \quad \text{for all } g \in G \tag{$*$}$$
is equivalent by multiplication on the right by $g^{-1}$ to
$$gHg^{-1} = H, \quad \text{for all } g \in G,$$
and the above is equivalent to
$$gHg^{-1} \subseteq H, \quad \text{for all } g \in G. \tag{$**$}$$
This is because $gHg^{-1} \subseteq H$ implies $H \subseteq g^{-1}Hg$, and this for all $g \in G$.

<!-- PAGE 41 -->

> **Proposition 2.11.** Let $\phi : G \to G'$ be a group homomorphism. Then $H = \operatorname{Ker} \phi$ satisfies Property ($**$), and thus Property ($*$).

*Proof.* We have
$$\phi(ghg^{-1}) = \phi(g)\phi(h)\phi(g^{-1}) = \phi(g)e'\phi(g)^{-1} = \phi(g)\phi(g)^{-1} = e',$$
for all $h \in H = \operatorname{Ker} \phi$ and all $g \in G$. Thus, by definition of $H = \operatorname{Ker} \phi$, we have $gHg^{-1} \subseteq H$. $\square$

> **Definition 2.10.** For any group $G$, a subgroup $N$ of $G$ is a *normal subgroup* of $G$ iff
> $$gNg^{-1} = N, \quad \text{for all } g \in G.$$
> This is denoted by $N \triangleleft G$.

Proposition 2.11 shows that the kernel $\operatorname{Ker} \phi$ of a homomorphism $\phi : G \to G'$ is a normal subgroup of $G$.

Observe that if $G$ is abelian, then every subgroup of $G$ is normal.

Consider Example 2.7. Let $R \in \mathbf{SO}(2)$ and $A \in \mathbf{SL}(2, \mathbb{R})$ be the matrices
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
Then
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$
and we have
$$ARA^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 1 & -1 \end{pmatrix},$$
and clearly $ARA^{-1} \notin \mathbf{SO}(2)$. Therefore $\mathbf{SO}(2)$ is not a normal subgroup of $\mathbf{SL}(2, \mathbb{R})$. The same counter-example shows that $\mathbf{O}(2)$ is not a normal subgroup of $\mathbf{GL}(2, \mathbb{R})$.

Let $R \in \mathbf{SO}(2)$ and $Q \in \mathbf{SO}(3)$ be the matrices
$$R = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad Q = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}.$$
Then
$$Q^{-1} = Q^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$
<!-- PAGE 42 -->
and we have
$$QRQ^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$
$$= \begin{pmatrix} 0 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}.$$
Observe that $QRQ^{-1} \notin \mathbf{SO}(2)$, so $\mathbf{SO}(2)$ is not a normal subgroup of $\mathbf{SO}(3)$.

Let $T$ and $A \in \mathbf{GL}(2, \mathbb{R})$ be the following matrices
$$T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
We have
$$A^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = A,$$
and
$$ATA^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.$$
The matrix $T$ is upper triangular, but $ATA^{-1}$ is not, so the group of $2 \times 2$ upper triangular matrices is not a normal subgroup of $\mathbf{GL}(2, \mathbb{R})$.

Let $Q \in V$ and $A \in \mathbf{GL}(2, \mathbb{R})$ be the following matrices
$$Q = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
We have
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$
and
$$AQA^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 0 & -1 \end{pmatrix}.$$
Clearly $AQA^{-1} \notin V$, which shows that the Klein four-group is not a normal subgroup of $\mathbf{GL}(2, \mathbb{R})$.

The reader should check that the subgroups $n\mathbb{Z}$, $\mathbf{GL}^+(n, \mathbb{R})$, $\mathbf{SL}(n, \mathbb{R})$, and $\mathbf{SO}(n, \mathbb{R})$ as a subgroup of $\mathbf{O}(n, \mathbb{R})$, are normal subgroups.

If $N$ is a normal subgroup of $G$, the equivalence relation $\sim$ induced by left cosets (see Definition 2.5) is the same as the equivalence induced by right cosets. Furthermore, this equivalence relation is a *congruence*, which means that: For all $g_1, g_2, g'_1, g'_2 \in G$,
<!-- PAGE 43 -->
1. If $g_1 N = g'_1 N$ and $g_2 N = g'_2 N$, then $g_1 g_2 N = g'_1 g'_2 N$, and
2. If $g_1 N = g_2 N$, then $g_1^{-1} N = g_2^{-1} N$.

As a consequence, we can define a group structure on the set $G/{\sim}$ of equivalence classes modulo $\sim$, by setting
$$(g_1 N)(g_2 N) = (g_1 g_2)N.$$

> **Definition 2.11.** Let $G$ be a group and $N$ be a normal subgroup of $G$. The group obtained by defining the multiplication of (left) cosets by
> $$(g_1 N)(g_2 N) = (g_1 g_2)N, \quad g_1, g_2 \in G$$
> is denoted $G/N$, and called the *quotient of $G$ by $N$*. The equivalence class $gN$ of an element $g \in G$ is also denoted $\overline{g}$ (or $[g]$). The map $\pi : G \to G/N$ given by
> $$\pi(g) = \overline{g} = gN$$
> is a group homomorphism called the *canonical projection*.

Since the kernel of a homomorphism is a normal subgroup, we obtain the following very useful result.

> **Proposition 2.12.** Given a homomorphism of groups $\phi : G \to G'$, the groups $G/\operatorname{Ker} \phi$ and $\operatorname{Im} \phi = \phi(G)$ are isomorphic.

*Proof.* Since $\phi$ is surjective onto its image, we may assume that $\phi$ is surjective, so that $G' = \operatorname{Im} \phi$. We define a map $\overline{\phi} : G/\operatorname{Ker} \phi \to G'$ as follows:
$$\overline{\phi}(\overline{g}) = \phi(g), \quad g \in G.$$
We need to check that the definition of this map does not depend on the representative chosen in the coset $\overline{g} = g\operatorname{Ker} \phi$, and that it is a homomorphism. If $g'$ is another element in the coset $g\operatorname{Ker} \phi$, which means that $g' = gh$ for some $h \in \operatorname{Ker} \phi$, then
$$\phi(g') = \phi(gh) = \phi(g)\phi(h) = \phi(g)e' = \phi(g),$$
since $\phi(h) = e'$ as $h \in \operatorname{Ker} \phi$. This shows that
$$\overline{\phi}(\overline{g'}) = \phi(g') = \phi(g) = \overline{\phi}(\overline{g}),$$
so the map $\overline{\phi}$ is well defined. It is a homomorphism because
$$\begin{aligned}
\overline{\phi}(\overline{g}\,\overline{g'}) &= \overline{\phi}(\overline{gg'}) \\
&= \phi(gg') \\
&= \phi(g)\phi(g') \\
&= \overline{\phi}(\overline{g})\overline{\phi}(\overline{g'}).
\end{aligned}$$
The map $\overline{\phi}$ is injective because $\overline{\phi}(\overline{g}) = e'$ iff $\phi(g) = e'$ iff $g \in \operatorname{Ker} \phi$, iff $\overline{g} = \overline{e}$. The map $\overline{\phi}$ is surjective because $\phi$ is surjective. Therefore $\overline{\phi}$ is a bijective homomorphism, and thus an isomorphism, as claimed. $\square$

<!-- PAGE 44 -->

Proposition 2.12 is called the *first isomorphism theorem*.

A useful way to construct groups is the direct product construction.

> **Definition 2.12.** Given two groups $G$ and $H$, we let $G \times H$ be the Cartesian product of the sets $G$ and $H$ with the multiplication operation $\cdot$ given by
> $$(g_1, h_1) \cdot (g_2, h_2) = (g_1 g_2, h_1 h_2).$$
> It is immediately verified that $G \times H$ is a group called the *direct product* of $G$ and $H$.

Similarly, given any $n$ groups $G_1, \dots, G_n$, we can define the direct product $G_1 \times \dots \times G_n$ in a similar way.

If $G$ is an abelian group and $H_1, \dots, H_n$ are subgroups of $G$, the situation is simpler. Consider the map
$$a : H_1 \times \dots \times H_n \to G$$
given by
$$a(h_1, \dots, h_n) = h_1 + \dots + h_n,$$
using $+$ for the operation of the group $G$. It is easy to verify that $a$ is a group homomorphism, so its image is a subgroup of $G$ denoted by $H_1 + \dots + H_n$, and called the *sum of the groups $H_i$*. The following proposition will be needed.

> **Proposition 2.13.** Given an abelian group $G$, if $H_1$ and $H_2$ are any subgroups of $G$ such that $H_1 \cap H_2 = \{0\}$, then the map $a$ is an isomorphism
> $$a : H_1 \times H_2 \to H_1 + H_2.$$

*Proof.* The map is surjective by definition, so we just have to check that it is injective. For this, we show that $\operatorname{Ker} a = \{(0, 0)\}$. We have $a(a_1, a_2) = 0$ iff $a_1 + a_2 = 0$ iff $a_1 = -a_2$. Since $a_1 \in H_1$ and $a_2 \in H_2$, we see that $a_1, a_2 \in H_1 \cap H_2 = \{0\}$, so $a_1 = a_2 = 0$, which proves that $\operatorname{Ker} a = \{(0, 0)\}$. $\square$

Under the conditions of Proposition 2.13, namely $H_1 \cap H_2 = \{0\}$, the group $H_1 + H_2$ is called the *direct sum* of $H_1$ and $H_2$; it is denoted by $H_1 \oplus H_2$, and we have an isomorphism $H_1 \times H_2 \cong H_1 \oplus H_2$.
