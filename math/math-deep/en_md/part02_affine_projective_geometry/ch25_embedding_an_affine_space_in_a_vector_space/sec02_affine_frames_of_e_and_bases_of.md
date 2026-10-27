# Affine Frames of E and Bases of


<!-- PAGE 860 -->
$$Proposition 25.2. Given any affine space \begin{pmatrix} \longrightarrow \\ E,E \\ family \end{pmatrix} , for any family (a_{i} )_{i\in I}\longrightarrow  of points in E,$$
any family $(\lambda_{i} )_{i\in I}$ of scalars in $\mathbb{R}$, and any  $(v_{j})_{j\in J}$ of vectors in $E$ , with I $\cap J = \emptyset$ , the following properties hold:
$$(1) If \sum_{i}  \in I \lambda_{i}  = 0, then$$
$$----\longrightarrow$$
$$\sum_{i\in I}  \langle a_{i}, \lambda_{i} \rangle +b \sum_{j\in J}  v_{j} = \sum_{i\in I}  \lambda_{i} a_{i} + \sum_{j\in J}  v_{j},$$
where
$$----\longrightarrow$$
$$\sum_{i\in I}  \lambda_{i} a_{i} = \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}$$
for any $b \in E$, which, by Proposition 24.1, is a vector independent of $b$, or
$$(2) If \sum_{i}  \in I \lambda_{i}  \neq  0, then$$
$$\sum_{i\in I}  \langle a_{i}, \lambda_{i} \rangle + \sum_{j\in J}  v_{j} =* \sum_{i\in I}  \frac{\lambda_{i}}{\lambda_{i}} a_{i} + \sum_{j\in J}  \frac{v_{j}}{\lambda_{i}} , \sum_{i\in I}  \lambda_{i} +.$$
$$b \sum_{i}  \in I \sum_{i}  \in I$$

*Proof.* By induction on the size of I and the size of $J$. The above formulae show that we have some kind of extended barycentric calculus. Operations on weighted points and vectors were introduced by $H$. Grassmann, in his book published in $1844$! This calculus will be helpful in dealing with rational curves.

## 25.2 Affine Frames of E and Bases of E

$$b$$
There is also a nice relationship between affine frames in and bases of $E$, stated in
$$the following proposition. \begin{pmatrix} \longrightarrow \\ E,E \end{pmatrix} b$$
$$-\longrightarrow$$
$$Proposition-\longrightarrow  25.3. Given -\longrightarrow any affine -\longrightarrow  space \begin{pmatrix} \longrightarrow \\ E,E \\ isa \end{pmatrix} , for any affine frame (a_{0}, (a_{0}a_{1}, \dots ,$$
$a_{0}a_{m}))$ for $E$, the family $(a_{0}a_{1}, \dots  ,a_{0}a_{m}, a_{0})$   basis for $E$, and for any affine frame
$$b$$
$(a_{0}, \dots  , a_{m})$ for $E$, the family $(a_{0}, \dots  , a_{m})$ is a basis for $E$. Furthermore, given any element
$$b$$
$\langle x, \lambda \rangle \in E$, if
$$b$$
$$-\longrightarrow -\longrightarrow$$
$$x = a_{0} + x_{1}a_{0}a_{1} + \cdots  + x_{m}a_{0}a_{m}$$
$$-\longrightarrow  -\longrightarrow$$
over the affine frame $(a_{0}, (a_{0}a_{1}, \dots  ,a_{0}a_{m}))$ in $E$, then the coordinates of $\langle x, \lambda \rangle$ over the basis $-\longrightarrow  -\longrightarrow (a_{0}a_{1}, \dots  ,a_{0}a_{m}, a_{0})$ in $E$ are
$$b$$
$$(\lambda x_{1}, \dots  , \lambda x_{m}, \lambda ).$$
$$\longrightarrow$$
For any vector $v \in E$ , if
$$-\longrightarrow -\longrightarrow$$
$$v = v_{1}a_{0}a_{1} + \cdots  + v_{m}a_{0}a_{m}$$

<!-- PAGE 861 -->
$$-\longrightarrow  -\longrightarrow  \longrightarrow -\longrightarrow  -\longrightarrow$$
over the basis $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ in $E$ , then over the basis $(a_{0}a_{1}, \dots  ,a_{0}a_{m}, a_{0})$ in $E$, the
$$b$$
coordinates of $v$ are
$$(v_{1}, \dots  , v_{m}, 0).$$
For any element $\langle a, \lambda \rangle$ , where $\lambda$ ̸ $= 0$, if the barycentric coordinates of a w.r.t. the affine basis $(a_{0}, \dots  , a_{m})$ in $E$ are $(\lambda_{0} , \dots  , \lambda_{m}$ ) with $\lambda_{0}  +\cdots +\lambda_{m}  = 1$, then the coordinates of $\langle a, \lambda \rangle$ w.r.t. the basis $(a_{0}, \dots  , a_{m})$ in $E$ are
$$b$$
$$(\lambda \lambda_{0} , \dots  , \lambda \lambda_{m} ).$$
$$\longrightarrow$$
If a vector $v \in E$ is expressed as
$$-\longrightarrow -\longrightarrow$$
$$v = v_{1}a_{0}a_{1} + \cdots  + v_{m}a_{0}a_{m} = -(v_{1} + \cdots  + v_{m})a_{0} + v_{1}a_{1} + \cdots  + v_{m}a_{m},$$
with respect to the affine basis $(a_{0}, \dots  , a_{m})$ in $E$, then its coordinates w.r.t. the basis $(a_{0}, \dots  , a_{m})$ in $E$ are
$$b$$
$$(-(v_{1} + \cdots  + v_{m}), v_{1}, \dots  , v_{m}).$$

*Proof.* We sketch parts of the proof, leaving the details as an exercise. Figure 25.2 shows
$$-\longrightarrow  -\longrightarrow$$
the basis $(a_{0}a_{1},a_{0}a_{2}, a_{0})$ corresponding to the affine frame $(a_{0}, a_{1}, a_{2})$ in $E$.
$$x,\lambda =(\lambda x,\lambda x, \lambda )$$
$$12$$
$$aaa$$
$$020$$
$$ax = a + x \overline{a}\overline{a} + x \overline{a}\overline{a} x = x,1$$
$$10101202$$
$$EE$$
$$\Omega \overline{a}\overline{a}$$
$$\overline{a}\overline{a} 02$$
$$01$$
$$Figure 25.2: The affine frame (a_{0}, a_{1}, a_{2}) of E and the basis inE.$$
$$b$$
If we assume that we have a nontrivial linear combination
$$-\longrightarrow -\longrightarrow$$
$$\lambda_{1} a_{0}a_{1}+ \cdots + \lambda_{m} a_{0}a_{m}+ \mu a_{0} = 0,$$
$$b bb$$
if $\mu  \neq  0$, then we have
$$-\longrightarrow -\longrightarrow -\longrightarrow -\longrightarrow$$
$$\lambda_{1} a_{0}a_{1}+ \cdots + \lambda_{m} a_{0}a_{m}+ \mu a_{0} = \langle a_{0} + \mu^{-1} \lambda_{1} a_{0}a_{1} + \cdots  + \mu^{-1} \lambda_{m} a_{0}a_{m}, \mu \rangle ,$$
$$b bb$$

<!-- PAGE 862 -->
$$-\longrightarrow  -\longrightarrow  \longrightarrow$$
which is never null, and thus, $\mu  = 0$, but since $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ is a basis of $E$ , we must also have $\lambda_{i}  = 0$ for all $i, 1 \le i \le m$. Given any element $\langle x, \lambda \rangle \in E$, if
$$b$$
$$-\longrightarrow -\longrightarrow$$
$$x = a_{0} + x_{1}a_{0}a_{1} + \cdots  + x_{m}a_{0}a_{m}$$
$$-\longrightarrow  -\longrightarrow$$
over the affine frame $(a_{0}, (a_{0}a_{1}, \dots  ,a_{0}a_{m}))$ in $E$, in view of the definition of $+$ , we have
$$b$$
$$-\longrightarrow -\longrightarrow$$
$$\langle x, \lambda \rangle =\langle a_{0} + x_{1}a_{0}a_{1} + \cdots  + x_{m}a_{0}a_{m}, \lambda \rangle$$
$$-\longrightarrow -\longrightarrow$$
$$=\langle a_{0}, \lambda \rangle + \lambda x_{1}a_{0}a_{1}+ \cdots + \lambda x_{m}a_{0}a_{m},$$
$$bb b$$
$$-\longrightarrow  -\longrightarrow$$
which shows that over the basis $(a_{0}a_{1}, \dots  ,a_{0}a_{m}, a_{0})$ in $E$, the coordinates of $\langle x, \lambda \rangle$ are
$$b$$
$$(\lambda x_{1}, \dots  , \lambda x_{m}, \lambda ).$$
$$-\longrightarrow  -\longrightarrow$$
If $(x_{1}, \dots  , x_{m})$ are the coordinates of $x$ w.r.t. the affine frame $(a_{0}, (a_{0}a_{1}, \dots  ,a_{0}a_{m}))$ in $E$, then $(x_{1}, \dots  , x_{m}, 1)$ are the coordinates of $x$ in $E$, i.e., the last coordinate is $1$, and if
$$b \longrightarrow$$
$$-\longrightarrow  -\longrightarrow$$
$u$ has coordinates $(u_{1}, \dots  , u_{m})$ with respect to the basis $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ in $E$ , then $u$ has coordinates $(u_{1}, \dots  , u_{m}, 0)$ in $E$, i.e., the last coordinate is $0$. Figure 25.3 shows the affine
$$b$$
frame $(a_{0}, a_{1}, a_{2})$ in $E$ viewed as a basis in $E$.
$$b$$
$$x,\lambda =(\lambda \lambda ,\lambda \lambda  1, \lambda \lambda )$$
$$02$$
$$aaa$$
$$020a$$
$$2$$
$$ax = \lambda a+\lambda a+\lambda aax,1$$
$$12 2x =$$
$$00111$$
$$EE$$
$$\Omega$$
$$\Omega$$
$$Figure 25.3: The basis (a_{0}, a_{1}, a_{2}) inE.$$
$$b$$
