# The Chinese Remainder Theorem


<!-- PAGE 1147 -->
for some $p \in A$ that is not a unit. Moreover, by Proposition 32.1, the element $p$ is irreducible. Define
$$\mathfrak{B} = {a \in A | pa \in \mathfrak{A}}.$$
Clearly, $\mathfrak{A} = p\mathfrak{B}, \mathfrak{B} \neq  (0), \mathfrak{A} \subseteq \mathfrak{B}$, and $\mathfrak{B}$ is a proper ideal. We claim that $\mathfrak{A} \neq \mathfrak{B}$. Indeed, if $\mathfrak{A} = \mathfrak{B}$ were true, then we would have $\mathfrak{A} = p\mathfrak{B} = \mathfrak{B}$, but this is impossible since $p$ is irreducible, $A$ is a UFD, and $\mathfrak{B} \neq  (0)$ (we get $\mathfrak{B} = p^{m}\mathfrak{B}$ for all $m$, and every element of $\mathfrak{B}$ would be a multiple of $p^{m}$ for arbitrarily large $m$, contradicting the fact that $A$ is a UFD). Thus, we have $\mathfrak{A} \subset \mathfrak{B}$, and since $\mathfrak{A}$ is a maximal element of $\mathcal{F}$, we must have $\mathfrak{B} \in F/$ . However, $\mathfrak{B} \in F/$  means that $\mathfrak{B}$ is a principal ideal, and thus, $\mathfrak{A} = p\mathfrak{B}$ is also a principal ideal, a contradiction. Observe that the above proof shows that Proposition 32.13 also holds under the assumption that every prime ideal is principal.

## 32.2 The Chinese Remainder Theorem

In this section, which is a bit of an interlude, we prove a basic result about quotients of commutative rings by products of ideals that are pairwise relatively prime. This result has applications in number theory and in the structure theorem for finitely generated modules over a PID, which will be presented later.

> **Definition 32.3.** Given two ideals $\mathfrak{a}$ and $\mathfrak{b}$ of a ring $A$, we define the ideal $\mathfrak{ab}$ as the set of all finite sums of the form
$$a_{1}b_{1} + \cdots  + a_{k}b_{k},a_{i} \in \mathfrak{a}, b_{i} \in \mathfrak{b}.$$
More generally, if $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ are $n \ge 2$ ideals of $A$, the ideal $\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$ is the set of finite sums
$$\sum_{j}  k=1 a_{1}^{j} \cdots  a_{n}^{j}, where a_{i}^{j} \in \mathfrak{a}_{i} for i = 1, \dots  , n and j = 1, \dots  , k.$$
The reader should check $that\mathfrak{ab} and\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$ are indeed ideals. Observe $that\mathfrak{ab} \subseteq \mathfrak{a}$ and $\mathfrak{ab} \subseteq \mathfrak{b}$, so that
$$\mathfrak{ab} \subseteq \mathfrak{a} \cap \mathfrak{b}.$$
In general equality does not hold. However we have the following result.

> **Proposition 32.14.** Given a ring $A$ and two ideals $\mathfrak{a}$ and $\mathfrak{b}$ in $A$, if
$$\mathfrak{a} +\mathfrak{b} = A,$$
then we have
$$\mathfrak{ab} =\mathfrak{a} \cap \mathfrak{b}.$$

<!-- PAGE 1148 -->

*Proof.* If $\mathfrak{a} +\mathfrak{b} = A$, there is some $a \in \mathfrak{a}$ and some $b \in \mathfrak{b}$ such that
$$a + b = 1,$$
so for every $x \in \mathfrak{a} \cap \mathfrak{b}$, we have
$$x = xa + xb,$$
which shows that $x \in \mathfrak{ab}$.

> **Definition 32.4.** Given a ring $A$, two $ideals\mathfrak{a} and\mathfrak{b}$ of $A$ that satisfy the $condition\mathfrak{a}+\mathfrak{b} = A$ are said to be coprime or comaximal. We define the homomorphism $\phi$ : $A \to A/\mathfrak{a} \times  A/\mathfrak{b}$ by
$$\phi (x) = (\overline{x}_{a}\overline{, x}_{b}),$$
$where\overline{x}_{a}$ is the equivalence class of $x modulo\mathfrak{a}$ (resp. $\overline{x}_{b}$ is the equivalence class of $x$ modulo $\mathfrak{b})$. Recall that the ideal $\mathfrak{a}$ defines the equivalence relation $\equiv_{a}$  on $A$ given by
$$x \equiv_{a}  yiffx -y \in \mathfrak{a},$$
and that $A/\mathfrak{a}$ is the quotient ring of equivalence classes $\overline{x}_{a}$, where $x \in A$, and similarly for $A/\mathfrak{b}$. Sometimes, we also write $x \equiv y$ (mod $\mathfrak{a})$ for $x \equiv_{a}  y$. Clearly, the kernel of the homomorphism $\phi$  is $\mathfrak{a} \cap \mathfrak{b}$. If we assume that $\mathfrak{a} +\mathfrak{b} = A$, then Ker $(\phi$ ) $=\mathfrak{a} \cap \mathfrak{b} =\mathfrak{ab}$, and because $\phi$  has a constant value on the equivalence classes modulo $\mathfrak{ab}$, the map $\phi$  induces a quotient homomorphism
$$\theta : A/\mathfrak{ab} \to A/\mathfrak{a} \times  A/\mathfrak{b}$$
given by $\theta (\overline{x}) = \phi (x)$, as illustrated in the following diagram:
$$A\overline{J} A/\mathfrak{ab}$$
$$\overline{J}^{\pi}\overline{J}$$
$$\overline{J} J$$
$$JJ$$
$$JJ\theta$$
$$\phi JJ$$
$$%$$
$$A/\mathfrak{a} \times  A/\mathfrak{b}.$$
Because Ker $(\phi$ ) $=\mathfrak{ab}$, the homomorphism $\theta$  is injective. The Chinese remainder theorem says that $\theta$  is an isomorphism.

> **Theorem 32.15.** Given a commutative ring $A$, let $\mathfrak{a}$ and $\mathfrak{b}$ be any two ideals of $A$ such that $\mathfrak{a} +\mathfrak{b} = A$. Then the homomorphism $\theta$ : $A/\mathfrak{ab} \to A/\mathfrak{a} \times  A/\mathfrak{b}$ is an isomorphism.

*Proof.* We already showed that $\theta$  is injective, so we need to prove that $\theta$  is surjective. Given any $\overline{y} \in A/\mathfrak{a}$ and any $\overline{z} \in A/\mathfrak{b}$, first we need to prove that for any choice of a representative

<!-- PAGE 1149 -->
$y$ in the equivalence $class\overline{y}$ and of a representative $z$ in the equivalence $class\overline{z}$, there is some $x \in A$ such that
$$x \equiv y(\mathrm{mod} \mathfrak{a})$$
$$x \equiv z(\mathrm{mod} \mathfrak{b}).$$
Then we also need to show that if x' is a solution obtained for another choice of a representative y' in the equivalence $class\overline{y}$ and a representative z' in the equivalence $class\overline{z}$, we have x' $\equiv_{ab}  x$. Since $\mathfrak{a} +\mathfrak{b} = A$, there exist some $a \in \mathfrak{a}$ and some $b \in \mathfrak{b}$ such that
$$a + b = 1.$$
If we let
$$x = az + by,$$
since $a \in \mathfrak{a}$ we have
$$x = az + by \equiv_{a}  by \equiv_{a}  (1 -a)y \equiv_{a}  y -ay \equiv_{a}  y,$$
and similarly since $b \in \mathfrak{b}$
$$x = az + by \equiv_{b}  az \equiv_{b}  (1 -b)z \equiv_{b}  z -bz \equiv_{b}  z,$$
which shows that $x =$ az $+$ by works. For another choice of elements a' $\in \mathfrak{a}$ and b' $\in \mathfrak{b}$ such that a' $+$ b' $= 1$ and of a representative y' in the equivalence class $\overline{y}$ and a representative z' in the equivalence class $\overline{z}$, we need to show x' $\equiv_{ab}  x$ so that $\theta (\overline{x}) = \phi (x)$ is well defined. The above computation shows that x' $=$ a'z' $+$ b'y' is a solution of the system
$$x'\equiv y'(\mathrm{mod} \mathfrak{a})$$
$$x'\equiv z'(\mathrm{mod} \mathfrak{b}).$$
Since we also have
$$x \equiv y(\mathrm{mod} \mathfrak{a})$$
$$x \equiv z(\mathrm{mod} \mathfrak{b}),$$
y' $\equiv_{a}  y$, and z' $\equiv_{b}  z$, we obtain
$$x'-x \equiv y'-y \equiv 0(\mathrm{mod} \mathfrak{a})$$
$$x'-x \equiv z'-z \equiv 0(\mathrm{mod} \mathfrak{b}),$$
thus x' - $x \in \mathfrak{a} \cap \mathfrak{b} =\mathfrak{ab}$, namely x' $\equiv_{ab}  x$.

<!-- PAGE 1150 -->
Theorem 32.15 can be generalized to any (finite) number of ideals.

> **Theorem 32.16.** (Chinese remainder theorem) Given a commutative ring $A$, let $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ be any $n \ge 2$ ideals of $A$ such that $\mathfrak{a}_{i} +\mathfrak{a}_{j} = A$ for all i̸ $= j$. Then the homomorphism $\theta$ : $A/\mathfrak{a}_{1} \cdots \mathfrak{a}_{n} \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ is an isomorphism.

*Proof.* The map $\theta$ : $A/\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ is induced by the homomorphism $\phi$ : $A \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ given by
$$\phi (x) = (\overline{x}_{a1}\overline{, \dots  , x}_{an})$$
as illustrated below:
$$A\overline{O} A/\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n}$$
$$\overline{O}\overline{O}^{\pi}$$
$$\overline{O}\overline{O}$$
$$OO$$
$$OO$$
$$OO\theta$$
$$\phi OO$$
$$O'$$
$$A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}.$$
Clearly, Ker $(\phi$ ) $=\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n}$, so $\theta$  is well-defined and injective. We need to prove that
$$\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$$
and that $\theta$  is surjective. We proceed by induction. The case $n = 2$ is Theorem 32.15. By induction, assume that
$$\mathfrak{a}_{2} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}.$$
We claim that
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A.$$
Indeed, since $\mathfrak{a}_{1} +\mathfrak{a}_{i} = A$ for $i = 2, \dots  , n$, there exist some $a_{i} \in \mathfrak{a}_{1}$ and some $b_{i} \in \mathfrak{a}_{i}$ such that
$$a_{i} + b_{i} = 1,i = 2, \dots  , n,$$
and by multiplying these equations, we get
$$(a_{2} + b_{2}) \cdots  (a_{n} + b_{n}) = 1,$$
and so
$$a + b_{2} \cdots  b_{n} = 1,$$
where a is a sum of terms each containing some $a_{j}$ as a factor, so $a \in \mathfrak{a}_{1}$ and $b_{2} \cdots  b_{n} \in \mathfrak{a}_{2} \cdots \mathfrak{a}_{n}$, which shows that
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A,(*)$$
as claimed. It follows that
$$\mathfrak{a}_{1} \cap \mathfrak{a}_{2} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cap (\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}) =\mathfrak{a}_{1}\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}.$$

<!-- PAGE 1151 -->
Let us now prove that $\theta$  is surjective by induction. The case $n = 2$ is Theorem 32.15. If $n \ge 3$, given any $\overline{x}_{i} \in A/\mathfrak{a}_{i}$ for $i = 1, \dots  , n$, first we need to prove that for any choice $x_{i}$ of a representative in the equivalence class $\overline{x}_{i}$, there is some $x \in A$ such that
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n$$
Then we need to prove that if x' is any other solution obtained using other representatives
$$-$$
$x_{i}'$ in the classes $\overline{x}_{i}$, then x' $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$. First, applying Theorem 32.15 to $\mathfrak{a}_{1}$ and $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}$, we can find $y_{1} \in A$ such that
$$y_{1} \equiv 1(\mathrm{mod} \mathfrak{a}_{1})$$
$$y_{1} \equiv 0(\mathrm{mod} \mathfrak{a}_{2} \cdots \mathfrak{a}_{n}).$$
By the induction hypothesis, we can find $y_{2}, \dots  , y_{n} \in A$ such that for all $i, j$ with $2 \le i, j \le n$,
$$y_{i} \equiv 1(\mathrm{mod} \mathfrak{a}_{i})$$
$$y_{i} \equiv 0(\mathrm{mod} \mathfrak{a}_{j}),j \neq  i.$$
Observe that $y_{i} \equiv 0$ (mod $\mathfrak{a}_{j})$ for all $j \neq  i$ with $2 \le i, j \le n$ is equivalent to
$$y_{j} \equiv 0(\mathrm{mod} \mathfrak{a}_{i})for all j \neq  i with 2 \le i, j \le n.$$
We claim that
$$x = x_{1}y_{1} + x_{2}y_{2} + \cdots  + x_{n}y_{n}$$
works. Indeed, for $i = 2, \dots  , n$ and every term $x_{j}y_{j}$ with $j \neq  i$ and $2 \le j \le n$ in the sum $x_{2}y_{2} + \cdots  + x_{i}y_{i} + \cdots  + x_{n}y_{n}$, we have $x_{j}y_{j} \equiv 0$ (mod $\mathfrak{a}_{i})$ since $y_{j} \equiv 0$ (mod $\mathfrak{a}_{i})$ for all $j \neq  i$ with $2 \le i, j \le n$, and $x_{i}y_{i} \equiv x_{i}$ (mod $\mathfrak{a}_{i})$ since $y_{i} \equiv 1$ (mod $\mathfrak{a}_{i})$, so we get
$$x \equiv x_{1}y_{1} + x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n.(**)$$
Since $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} \subseteq \mathfrak{a}_{i}$ for $i = 2, \dots  , n$ and $y_{1} \equiv 0$ (mod $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n})$, we have
$$x_{1}y_{1} \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n$$
and equation (**) reduces to
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n.$$
For $i = 1$, we get
$$x \equiv x_{1}(\mathrm{mod} \mathfrak{a}_{1}),$$
therefore
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
We still to prove that if x' is any other solution obtained using other solutions $y_{i}'$ and
$$-$$
other representatives $x_{i}'$ in the classes $\overline{x}_{i}$, then x' $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$.

<!-- PAGE 1152 -->
But another solution x' $= x_{1}'y_{1}' + x_{2}'y_{2}' + \cdots  + x_{n}'y_{n}'$ satisfies the system of equations
$$x'\equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
and since $x_{i}' \equiv_{ai}  x_{i}$ and
$$x \equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
we obtain
$$x'-x \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
so x' - $x \in \mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$, as desired. Another proof uses the equation
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A$$
proven earlier, which also holds for any $i$, namely
$$\mathfrak{a}_{i} + \prod_{=1,j\neq}^{n}  \mathfrak{a}_{j} = A,1 \le i \le n.$$
$$ji$$
$$Pick any a_{i} \in \mathfrak{a}_{i} and any b_{i} \in \prod_{j}  n=1,j\neq i \mathfrak{a}_{j} such that a_{i} + b_{i} = 1, 1 \le i \le n. We claim that$$
$$x = b_{1}x_{1} + \cdots  + b_{n}x_{n}$$
satisfies the system of equations
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
This is because for each $i$ with $1 \le i \le n$,
$$x = b_{1}x_{1} + \cdots  + b_{i}x_{i} + \cdots  + b_{n}x_{n} = b_{1}x_{1} + \cdots  + (1 -a_{i})x_{i} + \cdots  + b_{n}x_{n}$$
$$= x_{i} + b_{1}x_{1} + \cdots  + b_{i-1}x_{i-1} -a_{i}x_{i} + b_{i+1}x_{i+1} + \cdots  + b_{n}x_{n},$$
$$but b_{k} \in \prod_{j}  n=1,j\neq k \mathfrak{a}_{j} for all k, \prod_{j}  n=1,j\neq k \mathfrak{a}_{j} \subseteq \mathfrak{a}_{i} if k \neq  i, and a_{i} \in \mathfrak{a}_{i}, so$$
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
$n$
$$If x'= b_{1}'x_{1}' + \cdots  + b_{i}'x_{i}' + \cdots  + b_{n}'x_{n}' for another choice of a_{i}' \in \mathfrak{a}_{i}, b_{i}' \in \prod_{j}  =1,j\neq i \mathfrak{a}_{j}, and x_{i}' in$$
the equivalence class $\overline{x}_{i}$, we have the equations
$$x'\equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
and since $x_{i}' \equiv x_{i}$ (mod $\mathfrak{a}_{i})$ for $i = 1, \dots  , n$, we deduce that
$$x'-x \equiv x_{i}' -x_{i} \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
so as before, x' - $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$, as desired.

<!-- PAGE 1153 -->
The classical version of the Chinese remainder theorem is the case where $A = \mathbb{Z}$ and where the ideals $\mathfrak{a}_{i}$ are defined by $n$ pairwise relatively prime integers $m_{1}, \dots  , m_{n}$. By the Bezout identity, since $m_{i}$ and $m_{j}$ are relatively prime whenever i̸ $= j$, there exist some $u_{i}, u_{j} \in \mathbb{Z}$ such that $u_{i}m_{i} + u_{j}m_{j} = 1$, and so $m_{i}\mathbb{Z} + m_{j}\mathbb{Z} = \mathbb{Z}$. In this case, we get an isomorphism
$$\mathbb{Z}/(m_{1} \cdots  m_{n})\mathbb{Z} \approx \prod_{i=1}^{n}  \mathbb{Z}/m_{i}\mathbb{Z}.$$
In particular, if $m$ is an integer greater than $1$ and
$$m = \prod_{i}  p_{i}^{ri}$$
is its factorization into prime factors, then
$$\mathbb{Z}/m\mathbb{Z} \approx \prod_{i}  \mathbb{Z}/p_{i}^{ri} \mathbb{Z}.$$
In the previous situation where the integers $m_{1}, \dots  , m_{n}$ are pairwise relatively prime, if we write $m = m_{1} \cdots  m_{n}$ and $m_{i}' = m/m_{i}$ for $i = 1 \dots  , n$, then $m_{i}$ and $m_{i}'$ are relatively prime, and so $m_{i}'$ has an inverse modulo $m_{i}$. If $t_{i}$ is such an inverse, so that
$$m_{i}'t_{i} \equiv 1(\mathrm{mod} m_{i}),$$
then it is not hard to show that for any $a_{1}, \dots  , a_{n} \in \mathbb{Z}$,
$$x = a_{1}t_{1}m_{1}' + \cdots  + a_{n}t_{n}m_{n}'$$
satisfies the congruences
$$x \equiv a_{i}(\mathrm{mod} m_{i}),i = 1, \dots  , n.$$
Theorem 32.16 can be used to characterize rings isomorphic to finite products of quotient rings. Such rings play a role in the structure theorem for torsion modules over a PID.

> **Definition 32.5.** Given $n$ rings $A_{1}, \dots  , A_{n} (n \ge 2)$, recall that the product ring $A = A_{1} \times  \cdots  \times  A_{n}$ is the ring in which addition and multiplication are defined componenwise. That is,
$$(a_{1}, \dots  , a_{n}) + (b_{1}, \dots  , b_{n}) = (a_{1} + b_{1}, \dots  , a_{n} + b_{n})$$
$$(a_{1}, \dots  , a_{n}) \cdot  (b_{1}, \dots  , b_{n}) = (a_{1}b_{1}, \dots  , a_{n}b_{n}).$$
The additive identity is $0_{A} = (0, \dots  , 0)$ and the multiplicative identity is $1_{A} = (1, \dots  , 1)$. For $i = 1, \dots  , n$, we can define the element $e_{i} \in A$ as follows:
$$e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0),$$
where the $1$ occurs in position $i$.

<!-- PAGE 1154 -->
Observe that the following properties hold for all $i, j = 1, \dots  , n$:
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A}.$$
Also, for any element $a = (a_{1}, \dots  , a_{n}) \in A$, we have
$$e_{i}a = (0, \dots  , 0, a_{i}, 0, \dots  , 0) = pr_{i}(a),$$
where $pr_{i}$ is the projection of $A$ onto $A_{i}$. As a consequence
$$\mathrm{Ker} (pr_{i}) = (1_{A} -e_{i})A.$$

> **Definition 32.6.** Given a commutative ring $A$, a direct decomposition of $A$ is a sequence $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n}) (n \ge 2)$ of ideals in $A$ such that there is an isomorphism $A \approx A/\mathfrak{b}_{1} \times \cdots \times A/\mathfrak{b}_{n}$. The following theorem gives useful conditions characterizing direct decompositions of a ring.

> **Theorem 32.17.** Let $A$ be a commutative ring and let $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ be a sequence of ideals in $A (n \ge 2)$. The following conditions are equivalent:
(a) The sequence $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ is a direct decomposition of $A$.
$(b)$ There exist some nonzero elements $e_{1}, \dots  , e_{n}$ of $A$ such that
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A},$$
and $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$, for $i, j = 1, \dots  , n$.
$(c)$ We have $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ for all $i \neq  j$, and $\mathfrak{b}_{1} \cdots \mathfrak{b}_{n} = (0)$.
$(d)$ We have $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ for all $i \neq  j$, and $\mathfrak{b}_{1} \cap \cdots  \cap \mathfrak{b}_{n} = (0)$.

*Proof.* Assume (a). Since we have an isomorphism $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$, we may identify $A$ with $A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$, and $\mathfrak{b}_{i}$ with Ker $(pr_{i})$. Then, $e_{1}, \dots  , e_{n}$ are the elements defined just before Definition 32.6. As noted, $\mathfrak{b}_{i} =$ Ker $(pr_{i}) = (1_{A}$ - $e_{i})A$. This proves $(b)$. Assume $(b)$. Since $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$ and $A$ is a ring with unit $1_{A}$, we have $1_{A}$ - $e_{i} \in \mathfrak{b}_{i}$ for $i = 1, \dots  , n$. For all $i \neq  j$, we also have $e_{i}(1_{A}$ - $e_{j}) = e_{i}$ - $e_{i}e_{j} = e_{i}$, so (because $\mathfrak{b}_{j}$ is an

<!-- PAGE 1155 -->
ideal), $e_{i} \in \mathfrak{b}_{j}$, and thus, $1_{A} = 1_{A}$ - $e_{i} + e_{i} \in \mathfrak{b}_{i} +\mathfrak{b}_{j}$, which shows that $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ for all $i \neq  j$. Furthermore, for any $x_{i} \in A$, with $1 \le i \le n$, since $e_{i}e_{j} = 0$ for all $i \neq  j$, we have
$$\prod_{i=1}^{n}  x_{i}(1_{A} -e_{i}) = \begin{pmatrix} x_{i} \end{pmatrix} \prod_{i=1}^{n}  \prod_{i=1}^{n}  (1_{A} -e_{i})$$
$$= \begin{pmatrix} x_{i} \end{pmatrix} \prod_{i=1}^{n}  (1_{A} - \sum_{i=1}^{n}  e_{i})$$
$$= 0,$$
which proves that $\mathfrak{b}_{1} \cdots \mathfrak{b}_{n} = (0)$. Thus, $(c)$ holds. The equivalence of $(c)$ and $(d)$ follows from the proof of Theorem 32.16. The fact that $(c)$ implies (a) is an immediate consequence of Theorem 32.16. Here is example of Theorem 32.17.

> **Example 32.2.** Take the commutative ring of residue classes mod $30$, namely
$$A :=\mathbb{Z}/30\mathbb{Z} = {\overline{i}}_{i=0}^{29}.$$
Let
$$\mathfrak{b}_{1} = 2\mathbb{Z}/30\mathbb{Z} := {2\overline{i}}_{i=0}^{14}$$
$$\mathfrak{b}_{2} = 3\mathbb{Z}/30\mathbb{Z} := {3\overline{i}}_{i=0}^{9}$$
$$\mathfrak{b}_{3} = 5\mathbb{Z}/30\mathbb{Z} := {5\overline{i}}_{i=0}^{5}.$$
Each $\mathfrak{b}_{i}$ is an ideal in $\mathbb{Z}/30\mathbb{Z}$. Furthermore
$$\mathbb{Z}/30\mathbb{Z} = (\mathbb{Z}/30\mathbb{Z})/(2\mathbb{Z}/30\mathbb{Z}) \times  (\mathbb{Z}/30\mathbb{Z})/(3\mathbb{Z}/30\mathbb{Z}) \times  (\mathbb{Z}/30\mathbb{Z})/(5\mathbb{Z}/30\mathbb{Z}),$$
where
$$e_{1} = (1, 0, 0) \to \overline{15},e_{2} = (0, 1, 0) \to \overline{10},e_{3} = (0, 0, 1) \to \overline{6},$$
since
$$\overline{15}^{2}\overline{= 15},\overline{10}^{2}\overline{= 10},\overline{6}^{2}\overline{= 6}$$
$$\overline{15 10 = 15 6 = 10 6 = 0},\overline{15 + 10 + 6 = 1}.$$
Observe that $\overline{15}$ corresponds to $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/(2\mathbb{Z}/30\mathbb{Z}), \overline{10}$ corresponds to $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/ (3\mathbb{Z}/30\mathbb{Z})$, while $\overline{6}$ corresponds to $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/(5\mathbb{Z}/30\mathbb{Z})$. The following structure theorem for commutative rings isomorphic to a product ring is also very useful. See Bourbaki $[26]$ Chapter I, Section 8(10) and Lafon $[112]$, Chapter II, Section 3(1).

<!-- PAGE 1156 -->

> **Proposition 32.18.** Let $A_{1}, \dots  , A_{n} (n \ge 2)$ and $A$ be commutative rings (with identity) and assume that we have an isomorphism $\theta$ : $A \to A_{1} \times  \cdots  \times  A_{n}$. Write $0_{n} = (0, \dots  , 0)$, and for $i = 1, \dots  , n$, define the element $e_{i} \in A_{1} \times  \cdots  \times  A_{n}$ as
$$e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0),$$
where the $1$ occurs in position $i$. Then let $e_{i} = \theta^{-1} (e_{i}) and\mathfrak{a}_{i} = e_{i}A = \theta^{-1} (e_{i}(A_{1}\times \cdots \times A_{n}))$, for $i = 1, \dots  , n$. The following properties hold.
$(1)$ The elements $e_{i} \in A$ are nonzero idempotents such that for all $i, j = 1, \dots  , n$,
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A}.$$
$(2) \mathfrak{a}_{i} = e_{i}A$ is a nonzero ideal for $i = 1, \dots  , n$. The ring $\mathfrak{a}_{i}$ has the identity $e_{i}$ and is isomorphic to $A_{i}$ for $i = 1, \dots  , n$.
$(3)$ The ring $A$ is the direct sum $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$.
$(4)$ For every ideal $\mathfrak{b}$ in $R$, we have $\mathfrak{b} = \mathfrak{b} \cap \mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{b} \cap \mathfrak{a}_{n} = e_{1}\mathfrak{b} \oplus \cdots  \oplus e_{n}\mathfrak{b}$ and $\mathfrak{b} \cap \mathfrak{a}_{i} = e_{i}\mathfrak{b}$ is an ideal for $i = 1, \dots  , n$.
$(5)$ Let $A$ be a commutative ring with identity and assume that there exist $n \ge 2$ nonzero elements $e_{i} \in A$ satisfying the properties in $(1)$. Then each $\mathfrak{a}_{i} = e_{i}A$ is a nonzero ideal in $A$ and a ring with identity $e_{i}$ for $i = 1, \dots  , n$, and the ring $A$ is the direct sum $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$. There is an isomorphism $\theta$ : $A \to \mathfrak{a}_{1} \times  \cdots  \times \mathfrak{a}_{n}$. Sketch of proof. The properties in $(1)$ hold because they are easily checked for the $e_{i}$ in $A_{1} \times  \cdots  \times  A_{n}$, and tranferred back to $A$ using the inverse isomorphism $\theta^{-1}$ . For example, in $A_{1} \times  \cdots  \times  A_{n}$, we have $e_{i}e_{j} = 0_{n}$ if $i \neq  j$, and
$$e_{i}e_{j} = \theta^{-1} (\theta (e_{i}e_{j})) = \theta^{-1} (\theta (e_{i})\theta (e_{j})) = \theta^{-1} (e_{i}e_{j}) = \theta^{-1} (0_{n}) = 0.$$
To prove $(2)$, we observe that $e_{i}(A_{1} \times  \cdots  \times  A_{n}) = {(0, \dots  , a_{1}, \dots  , 0)$ | $a_{i} \in A_{i}}$ is an ideal in $A_{1} \times  \cdots  \times  A_{n}$ and ring homomorphisms map ideals to ideals. By definition, $e_{i}$ is the identity of $\mathfrak{a}_{i} = e_{i}A$, and since $A_{i}$ is isomorphic to ${(0, \dots  , a_{i}, \dots  , 0)$ | $a_{i} \in A_{i}}$ by the map $a_{i} \mapsto (0, \dots  , a_{i}, \dots  , 0)$ and $\theta^{-1}$ is an isomorphism between ${(0, \dots  , a_{i}, \dots  , 0)$ | $a_{i} \in A_{i}}$ and $\mathfrak{a}_{i}$, by composition we have an isomorphism between $A_{i}$ and $\mathfrak{a}_{i}$.
$(3)$ From $(1)$, since $e_{1} + \cdots  + e_{n} = 1_{A}$, for all $a \in A$, we have $a = e_{1}a + \cdots  + e_{n}a$, with $e_{i}a \in \mathfrak{a}_{i}$, so $A =\mathfrak{a}_{1} + \cdots  +\mathfrak{a}_{n}$.
$$If a \in \mathfrak{a}_{i} \cap \bigoplus_{kj}  \mathfrak{a}_{j} then a = e_{i}\alpha_{i}  = \sum  j\neq i e_{j}\alpha_{j}  with \alpha_{i} , \alpha_{j}  \in A, and since e_{i}e_{j} = 0 for all$$
$i \neq  j$ and $e_{k}e  =^{\neq i} e_{k}$ for all $k$ (by $(1))$,
$$e_{i}a = e \sum_{ij\neq i}  e_{j}\alpha_{j}  = \sum_{j\neq i}  e_{i}e_{j}\alpha_{j}  = 0,$$
