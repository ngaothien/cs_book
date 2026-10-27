# Existence and Construction of Orthonormal Bases


<!-- PAGE 471 -->
Given two Euclidean spaces $E$ and $F$, where the inner product on $E$ is denoted by $\langle$ -, $-\rangle_{1}$ and the inner product on $F$ is denoted by $\langle$ -, $-\rangle_{2}$ , given any linear map $f$ : $E \to F$, it is immediately verified that the proof of Proposition 12.8 can be adapted to show that there is a unique linear map $f^{*}$ : $F \to E$ such that
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1}$$
for all $u \in E$ and all $v \in F$. The linear map $f^{*}$ is also called the adjoint of $f$. The following properties immediately follow from the definition of the adjoint map:
$(1)$ For any linear map $f$ : $E \to F$, we have
$$f^{**} = f.$$
$(2)$ For any two linear maps $f, g: E \to F$ and any scalar $\lambda  \in \mathbb{R}$:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}= \lambda f^{*} .$$
$(3)$ If $E, F, G$ are Euclidean spaces with respective inner products $\langle$ -, $-\rangle_{1} , \langle$ -, $-\rangle_{2}$ , and $\langle$ -, $-\rangle_{3}$ , and if $f$ : $E \to F$ and $g: F \to G$ are two linear maps, then
$$(g \circ f)^{*}= f^{*} \circ g^{*}.$$
Remark: Given any basis for $E$ and any basis for $F$, it is possible to characterize the matrix of the adjoint $f^{*}$ of $f$ in terms of the matrix of $f$ and the Gram matrices defining the inner products; see Problem 12.5. We will do so with respect to orthonormal bases in Proposition 12.14(2). Also, since inner products are symmetric, the adjoint $f^{*}$ of $f$ is also characterized by
$$f(u) \cdot  v = u \cdot  f^{*} (v),$$
for all $u, v \in E$.

## 12.4 Existence and Construction of Orthonormal

$$Bases$$
We can also use Theorem 12.6 to show that any Euclidean space of finite dimension has an orthonormal basis.

> **Proposition 12.9.** Given any nontrivial Euclidean space $E$ of finite dimension $n \ge 1$, there is an orthonormal basis $(u_{1}, \dots  , u_{n})$ for $E$.

<!-- PAGE 472 -->

*Proof.* We proceed by induction on $n$. When $n = 1$, take any nonnull vector $v \in E$, which exists since we assumed $E$ nontrivial, and let
$$u = \frac{v}{\|v\|} .$$
If $n \ge 2$, again take any nonnull vector $v \in E$, and let
$$u_{1} = \frac{v}{\|v\|} .$$
Consider the linear form $\phi_{u1}$  associated with $u_{1}$. Since $u_{1} \neq  0$, by Theorem 12.6, the linear form $\phi_{u1}$  is nonnull, and its kernel is a hyperplane $H$. Since $\phi_{u1} (w) = 0$ iff $u_{1} \cdot  w = 0$, the hyperplane $H$ is the orthogonal complement of ${u_{1}}$. Furthermore, since $u_{1}$ ̸ $= 0$ and the inner product is positive definite, $u_{1} \cdot  u_{1}$ ̸ $= 0$, and thus, $u_{1} \in / H$, which implies that $E = H \oplus \mathbb{R} u_{1}$. However, since $E$ is of finite dimension $n$, the hyperplane $H$ has dimension n-1, and by the induction hypothesis, we can find an orthonormal basis $(u_{2}, \dots  , u_{n})$ for $H$. Now because $H$ and the one dimensional space $\mathbb{R} u_{1}$ are orthogonal and $E = H \oplus \mathbb{R} u_{1}$, it is clear that $(u_{1}, \dots  , u_{n})$ is an orthonormal basis for $E$. As a consequence of Proposition 12.9, given any Euclidean space of finite dimension $n$, if $(e_{1}, \dots  , e_{n})$ is an orthonormal basis for $E$, then for any two vectors $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$ and $v = v_{1}e_{1} + \cdots  + v_{n}e_{n}$, the inner product $u \cdot  v$ is expressed as
$$u \cdot  v = (u_{1}e_{1} + \cdots  + u_{n}e_{n}) \cdot  (v_{1}e_{1} + \cdots  + v_{n}e_{n}) = \sum_{i=1}^{n}  u_{i}v_{i},$$
and the norm $\|u\|$ as
$$1/2$$
$$\|u\|= \|u_{1}e_{1} + \cdots  + u_{n}e_{n}\|= \begin{pmatrix} u_{i}^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
The fact that a Euclidean space always has an orthonormal basis implies that any Gram matrix $G$ can be written as
$$G = Q^{\top}Q,$$
for some invertible matrix $Q$. Indeed, we know that in a change of basis matrix, a Gram matrix $G$ becomes G' $= P^{\top}GP$. If the basis corresponding to G' is orthonormal, then G' $=$ I, so $G = (P^{-1} )^{\top}P^{-1}$ . There is a more constructive way of proving Proposition 12.9, using a procedure known as the Gram–Schmidt orthonormalization procedure. Among other things, the Gram–Schmidt orthonormalization procedure yields the QR-decomposition for matrices, an important tool in numerical methods.

<!-- PAGE 473 -->

> **Proposition 12.10.** Given any nontrivial Euclidean space $E$ of finite dimension $n \ge 1$, from any basis $(e_{1}, \dots  , e_{n})$ for $E$ we can construct an orthonormal basis $(u_{1}, \dots  , u_{n})$ for $E$, with the property that for every $k, 1 \le k \le n$, the families $(e_{1}, \dots  , e_{k})$ and $(u_{1}, \dots  , u_{k})$ generate the same subspace.

*Proof.* We proceed by induction on $n$. For $n = 1$, let
$$u_{1} = \frac{e_{1}}{\|e_{1}\|} .$$
For $n \ge 2$, we also let
$$u_{1} = \frac{e_{1}}{\|e_{1}\|} ,$$
and assuming that $(u_{1}, \dots  , u_{k})$ is an orthonormal system that generates the same subspace as $(e_{1}, \dots  , e_{k})$, for every $k$ with $1 \le k < n$, we note that the vector
$$u_{k+1}' = e_{k+1} - \sum_{i=1}^{k}  (e_{k+1} \cdot  u_{i}) u_{i}$$
is nonnull, since otherwise, because $(u_{1}, \dots  , u_{k})$ and $(e_{1}, \dots  , e_{k})$ generate the same subspace, $(e_{1}, \dots  , e_{k+1})$ would be linearly dependent, which is absurd, since $(e_{1}, \dots , e_{n})$ is a basis. Thus, the norm of the vector $u_{k+1}'$ being nonzero, we use the following construction of the vectors $u_{k}$ and $u_{k}'$:
$$u_{1}' = e_{1},u_{1} = \frac{u_{1}'}{\|u_{1}'\|} ,$$
and for the inductive step
$$u_{k+1}' = e_{k+1} - \sum_{i=1}^{k}  (e_{k+1} \cdot  u_{i}) u_{i},u_{k+1} = \frac{u_{k+1}'}{\|u_{k+1}'\|} ,$$
where $1 \le k \le n$ - $1$. It is clear that $\|u_{k+1}\| = 1$, and since $(u_{1}, \dots  , u_{k})$ is an orthonormal system, we have
$$u_{k+1}' \cdot  u_{i} = e_{k+1} \cdot  u_{i} -(e_{k+1} \cdot  u_{i})u_{i} \cdot  u_{i} = e_{k+1} \cdot  u_{i} -e_{k+1} \cdot  u_{i} = 0,$$
for all $i$ with $1 \le i \le k$. This shows that the family $(u_{1}, \dots  , u_{k+1})$ is orthonormal, and since $(u_{1}, \dots  , u_{k})$ and $(e_{1}, \dots  , e_{k})$ generates the same subspace, it is clear from the definition of $u_{k+1}$ that $(u_{1}, \dots  , u_{k+1})$ and $(e_{1}, \dots  , e_{k+1})$ generate the same subspace. This completes the induction step and the proof of the proposition. Note that $u_{k+1}'$ is obtained by subtracting from $e_{k+1}$ the projection of $e_{k+1}$ itself onto the orthonormal vectors $u_{1}, \dots  , u_{k}$ that have already been computed. Then $u_{k+1}'$ is normalized.

<!-- PAGE 474 -->
$$\mathbb{R}^{3}$$

> **Example 12.9.** For a specific example of this procedure, let $E =$ with the standard Euclidean norm. Take the basis
$$e_{1} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} e_{2} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} e_{3} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} .$$
Then
$$u_{1} = 1/\sqrt{3} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} ,$$
and
$$u_{2}' = e_{2} -(e_{2} \cdot  u_{1})u_{1} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} -2/3 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 1/3 \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} .$$
This implies that
$$u_{2} = 1/\sqrt{6} \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} ,$$
and that
$$u_{3}' = e_{3} -(e_{3} \cdot  u_{1})u_{1} -(e_{3} \cdot  u_{2})u_{2} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} -2/3 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + 1/6 \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} = 1/2 \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} .$$
$$-$$
To complete the orthonormal basis, normalize $u_{3}'$ to obtain
$$u_{3} = 1/\sqrt{2} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} .$$
$$-$$
An illustration of this example is provided by Figure 12.4.
Remarks:
$(1)$ The QR-decomposition can now be obtained very easily, but we postpone this until Section 12.8.
$(2)$ The proof of Proposition 12.10 also works for a countably infinite basis for $E$, producing a countably infinite orthonormal basis.

<!-- PAGE 475 -->
$$u^{‘2}$$
$$e$$
$$2$$
$$u$$
$$\overline{1}$$
$$udirection$$
$$udirection1$$
$$2$$
$$eu_{3}^{‘}$$
$$3$$

![Figure 12.4](../../assets/ch12/fig_12_4.png)

**Figure 12.4:** The top figure shows the construction of the blue $u_{2}'$ as perpendicular to the orthogonal projection of $e_{2}$ onto $u_{1}$, while the bottom figure shows the construction of the green $u_{3}'$ as normal to the plane determined by $u_{1}$ and $u_{2}$. It should also be said that the Gram–Schmidt orthonormalization procedure that we have presented is not very stable numerically, and instead, one should use the modified Gram– Schmidt method. To compute $u_{k+1}'$, instead of projecting $e_{k+1}$ onto $u_{1}, \dots  , u_{k}$ in a single step, it is better to perform $k$ projections. We compute $u_{1}^{k+1}, u_{2}^{k+1}, \dots  , u_{k}^{k+1}$ as follows:
$$u_{1}^{k+1}= e_{k+1} -(e_{k+1} \cdot  u_{1}) u_{1},$$
$$u_{i+1}^{k+1} = u_{i}^{k+1}-(u_{i}^{k+1}\cdot  u_{i+1}) u_{i+1},$$
where $1 \le i \le k$ - $1$. It is easily shown that $u_{k+1}' = u_{k}^{k+1}$.

> **Example 12.10.** Let us apply the modified Gram–Schmidt method to the $(e_{1}, e_{2}, e_{3})$ basis of Example 12.9. The only change is the computation of $u_{3}'$. For the modified Gram–Schmidt procedure, we first calculate
$$u_{1}^{3} = e_{3} -(e_{3} \cdot  u_{1})u_{1} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} -2/3 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 1/3 \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} .$$
$$-$$
Then
$$u_{2}^{3} = u_{1}^{3} -(u_{1}^{3} \cdot  u_{2})u_{2} = 1/3 \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} + 1/6 \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} = 1/2 \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} ,$$
$$--$$
and observe that $u_{2}^{3} = u_{3}'$. See Figure 12.5.

<!-- PAGE 476 -->
$$udirection$$
$$udirection1$$
$$2$$
$$\overline{u}\overline{3}$$
$$e1$$
$$3$$
$$udirection$$
$$udirection1$$
$$2$$
$$u33$$
$$1u$$
$$2$$

![Figure 12.5](../../assets/ch12/fig_12_5.png)

**Figure 12.5:** The top figure shows the construction of the blue $u_{1}^{3}$ as perpendicular to the orthogonal projection of $e_{3}$ onto $u_{1}$, while the bottom figure shows the construction of the sky blue $u_{2}^{3}$ as perpendicular to the orthogonal projection of $u_{1}^{3}$ onto $u_{2}$. The following Matlab program implements the modified Gram–Schmidt procedure. function $q =$ gramschmidt4(e) $n =$ size(e,1); for $i =$ 1:n q(:,i) $=$ e(:,i); for $j =$ 1:i-1
$$r = q(:,j)’*q(:,i);$$
$$q(:,i) = q(:,i) - r*q(:,j);$$
end $r =$ sqrt(q(:,i)’*q(:,i)); q(:,i) $= q(:,i)/r$; end end If we apply the above function to the matrix
$$\begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} ,$$

<!-- PAGE 477 -->
the ouput is the matrix
$$\begin{pmatrix} 0.5774 & 0.4082 & 0.7071 \\ 0.5774 & -0.8165 & -0.0000 \\ 0.5774 & 0.4082 & 0.7071 \end{pmatrix} ,$$
$$-$$
which matches the result of Example 12.9.

> **Example 12.11.** If we consider polynomials and the inner product
$$\langle f, g\rangle = \int_{-}^{}  1f(t)g(t)dt,$$
$$1$$
applying the Gram–Schmidt orthonormalization procedure to the polynomials
$$1, x, x^{2}, \dots  , x^{n}, \dots  ,$$
which form a basis of the polynomials in one variable with real coefficients, we get a family of orthonormal polynomials $Q_{n}(x)$ related to the Legendre polynomials. The Legendre polynomials $P_{n}(x)$ have many nice properties. They are orthogonal, but their norm is not always $1$. The Legendre polynomials $P_{n}(x)$ can be defined as follows. Letting $f_{n}$ be the function
$$f_{n}(x) = (x^{2}-1)^{n},$$
we define $P_{n}(x)$ as follows:
$$P_{0}(x) = 1,andP_{n}(x) = \frac{1}{2^{n}n!} f_{n}^{(n)} (x),$$
where $f_{n}^{(n)}$ is the nth derivative of $f_{n}$. They can also be defined inductively as follows:
$$P_{0}(x) = 1,$$
$$P_{1}(x) = x,$$
$$P_{n+1}(x) = \frac{2n + 1}{n + 1} xP_{n}(x) - \frac{n}{n + 1} P_{n-1}(x).$$
Here is an explicit summation for $P_{n}(x)$:
$$P_{n}(x) = \frac{1}{2^{n}} \sum_{k=0}^{⌊n/2⌋}  (-1)^{k} \begin{pmatrix} n \\ k \end{pmatrix} \begin{pmatrix} 2n -2k \\ n \end{pmatrix} x^{n-2k}.$$
The polynomials $Q_{n}$ are related to the Legendre polynomials $P_{n}$ as follows:
$$r$$
$$Q_{n}(x) = \frac{\overline{2}\overline{n}\overline{+ 1}}{2} P_{n}(x).$$

<!-- PAGE 478 -->

> **Example 12.12.** Consider polynomials over $[-1, 1]$, with the symmetric bilinear form
$$\langle f, g\rangle = \int_{-}^{}  1\sqrt \frac{1}{1 -t^{2}} f(t)g(t)dt.$$
$$1$$
We leave it as an exercise to prove that the above defines an inner product. It can be shown that the polynomials $T_{n}(x)$ given by
$$T_{n}(x) = \cos(n arccos x),n \ge 0,$$
(equivalently, with $x =$ cos $\theta$ , we have $T_{n}(cos \theta$ ) $= cos(n\theta$ )) are orthogonal with respect to the above inner product. These polynomials are the Chebyshev polynomials. Their norm is not equal to $1$. Instead, we have
$$(\pi$$
$$if n > 0,$$
$$\langle T_{n}, T_{n}\rangle =\overline{2}$$
$$\pi if n = 0.$$
Using the identity (cos $\theta  + i$ sin $\theta )^{n} =$ cos $n\theta  + i$ sin $n\theta$  and the binomial formula, we obtain the following expression for $T_{n}(x)$:
$$T_{n}(x) = \sum_{k=0}^{⌊n/2⌋}  \begin{pmatrix} n \\ 2k \end{pmatrix} (x^{2}-1)^{k}x^{n-2k}.$$
The Chebyshev polynomials are defined inductively as follows:
$$T_{0}(x) = 1$$
$$T_{1}(x) = x$$
$$T_{n+1}(x) = 2xT_{n}(x) -T_{n-1}(x),n \ge 1.$$
Using these recurrence equations, we can show that
$$-\overline{-}\overline{-}$$
$$T_{n}(x) = \frac{(x\sqrt{x}^{2}\overline{1)}^{n}+ (x +\sqrt{x}^{2}\overline{1)}^{n}}{2} .$$
The polynomial $T_{n}$ has $n$ distinct roots in the interval $[-1, 1]$. The Chebyshev polynomials play an important role in approximation theory. They are used as an approximation to a best polynomial approximation of a continuous function under the sup-norm $(\infty$ -norm). The inner products of the last two examples are special cases of an inner product of the form
$$\langle f, g\rangle = \int_{-}^{}  1W(t)f(t)g(t)dt,$$
$$1$$
where W(t) is a weight function. If $W$ is a continuous function such that W(x) $> 0$ on $(-1, 1)$, then the above bilinear form is indeed positive definite. Families of orthogonal
