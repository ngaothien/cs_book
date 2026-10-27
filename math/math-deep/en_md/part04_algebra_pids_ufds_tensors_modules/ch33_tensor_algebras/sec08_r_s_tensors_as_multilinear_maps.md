# (r,s)-Tensors as Multilinear Maps


<!-- PAGE 1205 -->
33.8 $(r$, s)-Tensors as Multilinear Maps As we just observed, Proposition 33.25 allows us to view the space of $(r$, s)-tensors $T^{r,s} (V$ ) as the space of multilinear maps
$$T : (V^{*})^{r}\times  V^{s}\to K,$$
a point of view that turns out to be technically very fruitful in differential geometry.

> **Definition 33.16.** The space $Hom((V^{*})^{r}, V^{s}; K)$ of multilinear maps $T$ : $(V^{*})^{r} \times  V^{s} \to K$ is denoted $\mathcal{T}^{r,s} (V$ ). For example, Dieudonn´e $[51]$, O’Neill $[137]$ and Sakai $[147]$ use this definition. Proposition 33.25 shows that the map $\mu^{r,s}$ : $T^{r,s}(V$ ) $\to T^{r,s}(V$ ) is an isomorphism. For this reason, the
$$\mathcal{T}^{r,s} \mathcal{T}^{0,1}  \mathcal{T}^{1,0}  \sim$$
elements of $(V$ ) are also called tensors. Note that $(V$ ) is $V^{*}$, and $(V$ ) is $V^{**} = V$ , using the canonical isomorphic $u \mapsto eval_{u}$.
Remark: The tensor spaces, $T^{r,s} (V$ ) $(resp,\mathcal{T}^{r,s} (V$ )) are also denoted $T_{s}^{r}  (V$ ) (resp. $\mathcal{T}_{s}^{r}  (V$ )). A tensor $\alpha  \in T^{r,s} (V$ ) is said to be contravariant in the first $r$ arguments and covariant in the last $s$ arguments. This terminology refers to the way tensors behave under coordinate changes. Given a basis $(e_{1}, \dots  , e_{n})$ of $V$ , if $(e_{1}^{*}, \dots  , e_{n}^{*})$ denotes the dual basis, then the tensors
$$e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}$$
form a basis of $T^{r,s} (V$ ), so every tensor $\alpha  \in T^{r,s} (V$ ) is given by an expression of the form
$$\alpha  = \sum_{i1,...,ir}  a_{j1...js}^{i1...ir}e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}.$$
$$j1,...,js$$
Using the isomorphism $\mu^{r,s}$ , the multilinear maps
$$\mu^{r,s} (e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*})$$
form a basis of $\mathcal{T}^{r,s} (V$ ), so every tensor $T \in T^{r,s} (V$ ) can be uniquely written as
$$T = \sum_{i1,...,ir}  a_{j1...js}^{i1...ir}\mu^{r,s} (e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}).$$
$$j1,...,js$$
Since $e_{j}^{*}(e_{i}) = \delta_{ij}$ , observe that
$$T(e_{i1}^{*}, \dots  , e_{ir}^{*}, e_{j1}, \dots  , e_{js}) = a_{j1...js}^{i1...ir}.$$
It is customary to drop $\mu^{r,s}$ and view
$$e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}$$

<!-- PAGE 1206 -->
as the corresponding multilinear map in $\mathcal{T}^{r,s} (V$ ). To simplify notation, we often write $\mu$ instead of $\mu^{r,s}$ . At first, the practice of dropping $\mu$  can be quite confusing, but one finds rather quickly that using the space $\mathcal{T}^{r,s} (V$ ) instead of the space $T^{r,s} (V$ ) is more convenient to deal with tensor fields. The tradition in classical tensor notation is to use lower indices on vectors and upper indices on linear forms, and in accordance to Einstein summation convention (or Einstein notation), the position of the indices on the coefficients is reversed. Einstein summation convention (already encountered in Section 33.1) is to assume that a summation is performed for all values of every index that appears simultaneously once as an upper index and once as a lower index. According to this convention, the linear form $e_{i}^{*}$ dual to the basis vector $e_{i}$ is denoted by $e^{i}$, and (suppressing the map $\mu^{r,s}$ ), a tensor $\alpha  \in T^{r,s} (V$ ) is written
$$\alpha  = a_{j1...js}^{i1...ir}e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e^{js}.$$
An older view of tensors is that they are multidimensional arrays of coefficients,
$$\begin{pmatrix} a_{j1...js}^{i1...ir} \\ (see \end{pmatrix} ,$$
subject to the rules for changes of bases  Proposition 33.29). From now on until Section 33.10 we will use the Einstein summation convention. It does reduce considerably the number of summation signs.

> **Proposition 33.26.** The $space\mathcal{T}^{1,1} (V$ ) is isomorphic to the space Hom(V, $V$ ) of linear maps from $V$ to itself.

*Proof.* Indeed, if $T \in T^{1,1} (V$ ), we obtain the linear map $f$ : $V \to V$ defined such that for every $u \in V$ ,
$$\theta (f(u)) = T(\theta , u),\theta  \in V^{*} .$$
If we pick a basis $(e_{1}, \dots  , e_{n})$ in $V$ and if $T$ is expressed as
$$T = a_{j}^{i}e_{i} \otimes e^{j},$$
then for any basis vector $e_{j}$, the linear form T(-, $e_{j})$ on $V^{*}$ is the $(1$, 0)-tensor $\mu (a_{j}^{i}e_{i})$, namely, evaluation of a linear form in $V^{*}$ at $a_{j}^{i}e_{i} \in V$ . Thus the $(1$, 1)-tensor $T$ defines the linear map $f$ : $V \to V$ given by
$$f(e_{j}) = a_{j}^{i}e_{i},$$
and we see that the matrix representing $f$ over the basis $(e_{1}, \dots  , e_{n})$ is $(a_{j}^{i})$. Note the double interpretation of $a_{j}^{i}e_{i}$. We can view it as a vector in $V$ (a linear combination of the vectors $e_{i}$ in $V$ ), or as a (multi)linear map in $\mathcal{T}^{1,0} (V$ ), where this time, $e_{i}$ is really $\mu (e_{i})$, namely the linear form $v \mapsto v(e_{i})$, with $v \in V^{*}$ . For any vector $u = u^{j}e_{j} \in V$ , we have
$$f(u) = f(u^{j}e_{j}) = u^{j}f(e_{j}) = u^{j}a_{j}^{i}e_{i} = a_{j}^{i}u^{j}e_{i} \in V,$$
so the ith coordinate $f(u)^{i}$ of f(u) is given by $f(u)^{i} = a_{j}^{i}u^{j}$, confirming that $(a_{j}^{i})$ is the matrix representing $f$.

<!-- PAGE 1207 -->
 Note that in the above computation, the $(1$, 1)-tensor $(a_{j}^{i})$ denotes a matrix $A$ where the upper index $i$ is the row index and the lower index $j$ is the column index, because we implicitly assumed that the coordinates $u^{j}$ of the vector $u$ constitute a column vector and that f(u) is also represented by a column vector, so that $f(u)^{i} = a_{j}^{i}u^{j}$ is the product
$$f(u)^{i} = \begin{pmatrix} a_{1}^{i} & \cdots & a_{j}^{i} & \cdots & a_{n}^{i} \end{pmatrix} \begin{pmatrix} u^{1} \\ \vdots \\ u^{j} \\ \vdots \\ u^{n} \end{pmatrix}$$
of the ith row of the matrix $A$ by the column vector whose jth entry is $u^{j}$. The equation $f(e_{j}) = a_{j}^{i}e_{i}$ can be symbolically written as
$$f(e_{j}) = \begin{pmatrix} e_{1} & \cdots & e_{i} & \cdots & e_{n} \end{pmatrix} \begin{pmatrix} a_{j}^{1} \\ \vdots \\ a_{j}^{i} \\ \vdots \\ a_{j}^{n} \end{pmatrix} ,$$
where the column vector above is the jth column of the matrix $A$. To recap,
$$\begin{pmatrix} f(u)^{1} \\ \vdots \\ f(u)^{n} \end{pmatrix} = A \begin{pmatrix} u^{1} \\ \vdots \\ u^{n} \end{pmatrix} , \begin{pmatrix} f(e_{1}) & \cdots & f(e_{n}) \end{pmatrix} = \begin{pmatrix} e_{1} & \cdots & e_{n} \end{pmatrix} A.$$
A dual interpretation of the $(1$, 1)-tensor $(a_{j}^{i})$ consists in viewing the coordinates $u^{j}$ of the vector $u$ as forming a row vector, in which case f(u) is also represented by a row vector, so that $f(u)^{i} = a_{j}^{i}u^{j}$ is the product
$$f(u)^{i} = \begin{pmatrix} u^{1} & \cdots & u^{j} & \cdots & u^{n} \end{pmatrix} \begin{pmatrix} a_{1}^{i} \\ \vdots \\ a_{j}^{i} \\ \vdots \\ a_{n}^{i} \end{pmatrix} ,$$
where the column vector above is the transpose of the ith row of $A$, which means that the matrix involved is the transpose $A^{\top}$ of the matrix $A$. In this point of view, the equation $f(e_{j}) = a_{j}^{i}e_{i}$ can be symbolically written as
$$f(e_{j}) = \begin{pmatrix} a_{j}^{1} & \cdots & a_{j}^{i} & \cdots & a_{j}^{n} \end{pmatrix} \begin{pmatrix} e_{1} \\ \vdots \\ e_{i} \\ \vdots \\ e_{n} \end{pmatrix} ,$$

<!-- PAGE 1208 -->
where the row vector above is the transpose of the jth column of the matrix $A$. Again, the matrix involved is the transpose $A^{\top}$ of $A$. To recap,
$$\begin{pmatrix} f(u)^{1} & \cdots & f(u)^{n} \end{pmatrix} = \begin{pmatrix} u^{1} & \cdots & u^{n} \end{pmatrix} A^{\top}, \begin{pmatrix} f(e_{1}) \\ \vdots \\ f(e_{n}) \end{pmatrix} = A^{\top} \begin{pmatrix} e_{1} \\ \vdots \\ e_{n} \end{pmatrix} .$$
Thus, in the dual interpretation, given a $(1, 1)$ tensor $(a_{j}^{i})$, it makes sense to view the lower index $j$ as the row index and the upper index $i$ as the column index. We usually swap $i$ and $j$ so that the expression $(a_{i}^{j})$ denotes a matrix where the lower index $i$ is the row index and the upper index $j$ is the column index. With this convention, the matrix $A^{\top}$ above becomes the matrix $A$, since
$$f(e_{i}) = \begin{pmatrix} a_{i}^{1} & \cdots & a_{i}^{j} & \cdots & a_{i}^{n} \end{pmatrix} \begin{pmatrix} e_{1} \\ \vdots \\ e_{j} \\ \vdots \\ e_{n} \end{pmatrix} = a_{i}^{j}e_{j}.$$
The dual interpretation is used below in Proposition 33.29. Proposition 33.26 generalizes to $(1$, s)-tensors as follows.

> **Proposition 33.27.** The $space\mathcal{T}^{1,s} (V$ ) is isomorphic to the space $Hom(V^{s}$ ; $V$ ) of multilinear maps from $V^{s}$ to $V$ .

*Proof.* Indeed, if $T \in T^{1,s}(V$ ), we obtain the multilinear map $f$ : $V^{s} \to V$ defined such that all $u_{1}, \dots  , u_{s} \in V$ ,
$$\theta (f(u_{1}, \dots  , u_{s})) = T(\theta , u_{1}, \dots  , u_{s}),\theta  \in V^{*} .$$
If we pick a basis $(e_{1}, \dots  , e_{n})$ in $V$ and if $T$ is expressed as
$$T = a_{j1...js}^{i}e_{i} \otimes e^{j1}\otimes \cdots  \otimes e^{js},$$
then for any basis vectors $e_{j1}, \dots  , e_{js}$, the multilinear form T(-, $e_{j1}, \dots  , e_{js})$ on $V^{*}$ is the $(1$, 0)-tensor $\mu (a_{j1...js}^{i}e_{i})$, namely, evaluation of a linear form in $V^{*}$ at $a_{j1...js}^{i}e_{i} \in V$ . Thus the $(1$, s)-tensor $T$ defines the multilinear map $f$ : $V^{s} \to V$ given by
$$f(e_{j1}, \dots  , e_{js}) = a_{j1...js}^{i}e_{i}.$$
Conversely, a multilinear map $f$ : $V^{s} \to V$ yields the $(1$, s)-tensor $T \in T^{1,s}(V$ ) given by
$$T(\theta , u_{1}, \dots  , u_{s}) = \theta (f(u_{1}, \dots  , u_{s})),$$
for all $\theta  \in V^{*}$ and all $u_{1}, \dots  , u_{s} \in V$ .

<!-- PAGE 1209 -->
Using the isomorphism $\mu$ : $T^{r,s} (V$ ) $\to T^{r,s} (V$ ), it is not hard to show that the tensor product
$$\mathcal{T}^{r1,s1} (V ) \times  T^{r2,s2} (V ) \longrightarrow T^{r1+r2,s1+s2} (V )$$
is defined as follows.

> **Definition 33.17.** For two tensors $T_{1} \in T^{r1,s1} (V$ ) and $T_{2} \in T^{r2,s2} (V$ ), their tensor product $T_{1} \otimes T_{2}$ is the multilinear map in $\mathcal{T}^{r1+r2,s1+s2} (V$ ) defined as follows:
$$(T_{1} \otimes T_{2})(\omega^{1} , \dots  , \omega^{r1} , \theta^{1} , \dots  , \theta^{r2} , v_{1}, \dots  , v_{s1}, y_{1}, \dots  , y_{s2})$$
$$= T_{1}(\omega^{1} , \dots  , \omega^{r1} , v_{1}, \dots  , v_{s1})T_{2}(\theta^{1} , \dots  , \theta^{r2} , y_{1}, \dots  , y_{s2}),$$
$$\in   \le  \le  \in  \le  \le  \in   \le  \le  \in$$
for all $\omega^{i1} V^{*} (1 i_{1} r_{1}), v_{j1} V (1 j_{1} s_{1}), \theta^{i2} V^{*} (1 i_{2} r_{2}), y_{j2} V (1 \le j_{2} \le s_{2})$. We check immediately that if $T_{1} \in T^{r1,s1} (V$ ) and $T_{2} \in T^{r2,s2} (V$ ), then
$$\mu^{r1+r2,s1+s2} (T_{1} \otimes T_{2}) = \mu^{r1,s1} (T_{1}) \otimes \mu^{r2,s2} (T_{2}),$$
where the tensor product on the left is the tensor product on $T^{r1,s1} (V$ ) $\times  T^{r2,s2} (V$ ) from Definition 33.15, and the tensor product on the right is the tensor product on $\mathcal{T}^{r1,s1} (V$ ) $\times \mathcal{T}^{r2,s2} (V$ ) from Definition 33.17. If $V$ and $W$ are two vector spaces, for any linear map $\phi$ : $V \to W$, recall that the transpose $\phi^{\top}$ of $\phi$  is the linear map $\phi^{\top}$ : $W^{*} \to V^{*}$ given by
$$\phi^{\top} (\omega ) = \omega  \circ \phi ,\omega  \in W^{*} .$$
If $\phi$ : $V \to W$ is a linear isomorphism, it induces a linear map $\phi_{s}^{r}$  : $\mathcal{T}^{r,s} (V$ ) $\to T^{r,s} (W)$ defined as follows.

> **Definition 33.18.** Let $\phi$ : $V \to W$ be a linear isomorphism of finite-dimensional vector spaces. The map $\phi_{s}^{r}$  : $\mathcal{T}^{r,s} (V$ ) $\to T^{r,s} (W)$ is defined as follows. For every $T \in T^{r,s} (V$ ),
$$(\phi_{s}^{r} T)(\theta^{1} , \dots  , \theta^{r} , v_{1}, \dots  , v_{s}) = T(\phi^{\top} (\theta^{1} ), \dots  , \phi^{\top} (\theta^{r} ), \phi^{-1} (v_{1}), \dots  , \phi^{-1} (v_{s})),$$
for all $\theta^{1} , \dots  , \theta^{r} \in W^{*}$ and all $v_{1}, \dots  , v_{s} \in W$. Since $\phi^{-1}$ and $\phi^{\top}$ are linear, $\phi_{s}^{r} T$ is multilinear, thus in $\mathcal{T}^{r,s}(W)$. The following proposition is shown in Abraham and Marsden $[1]$ (Proposition 1.7.4).

> **Proposition 33.28.** Let $\phi$ : $E \to F$ and $\psi$ : $F \to G$ be two linear isomorphisms of finite-dimensional vector spaces. The following properties hold.
$(1) (\psi  \circ \phi )_{s}^{r} = \psi_{s}^{r}  \circ \phi_{s}^{r}$ .
$(2)$ If id: $E \to E$ is the identity, then $id_{s}^{r}$ : $\mathcal{T}^{r,s} (E) \to T^{r,s} (E)$ is also the identity.
$(3)$ The map $\phi_{s}^{r}$  : $\mathcal{T}^{r,s}(E) \to T^{r,s}(F)$ is a linear isomorphism and $(\phi_{s}^{r} )^{-1} = (\phi^{-1} )_{s}^{r}$.

<!-- PAGE 1210 -->
The next proposition gives formulae for the components of $\phi_{s}^{r} T$ in terms of the components of $T$ with respect to bases of $E$ and $F$. Let $(e_{1}, \dots  , e_{n})$ be a basis of $E, (f_{1}, \dots  , f_{n})$ be a basis of $F$, and let $(e^{1}, \dots  , e^{n})$ be the dual basis of $E^{*}$ and $(f^{1} , \dots  , f^{n}$ ) be the dual basis of $F^{*}$ . If $A = (a_{i}^{j})$ is the matrix representing $\phi$  in the dual interpretation given (in Einstein notation) by
$$\phi (e_{i}) = a_{i}^{j}f_{j},$$
namely,
$$\begin{pmatrix} \phi (e_{1}) \\ \vdots \\ \phi (e_{n}) \end{pmatrix} = A \begin{pmatrix} f_{1} \\ \vdots \\ f_{n} \end{pmatrix} ,$$
then it known that the matrix representing $\phi^{\top}$ (also in the dual interpretation) with respect to the dual bases $(f^{1} , \dots  , f^{n}$ ) and $(e^{1}, \dots  , e^{n})$ is the transpose $A^{\top}$ of the matrix $A$ (see Gallier and Quaintance $[76]$, Section 10.6). This means that
$$\phi^{\top} (f^{i} ) = a_{j}^{i}e^{j},$$
where transposition corresponds to the fact that the indices $i$ and $j$ are raised when passing from vectors to their dual. If $B = (b_{i}^{j})$ denotes the inverse of $A$, then we have
$$\phi^{-1} (f_{i}) = b_{i}^{j}e_{j}.$$
We easily obtain the following result.

> **Proposition 33.29.** Let $\phi$ : $E \to F$ be a linear isomorphism, $(e_{1}, \dots  , e_{n})$ be a basis of $E$, and $(f_{1}, \dots  , f_{n})$ be a basis of $F$. If $A = (a_{i}^{j})$ is the matrix representing $\phi$  in the dual interpretation as above and $B = (b_{i}^{j})$ is its inverse, for any $T \in T^{r,s} (E)$ with components with respect to the basis  $\otimes \cdots \otimes  \otimes  \cdots \otimes$ , the components of  with respect $t_{j...js}^{i1...ir}  e_{i1} e_{ir} e^{j1} e^{js}  \phi_{s}^{r} T to^{1}$ the basis $f_{i1'} \otimes \cdots  \otimes f_{i'r} \otimes f_{1}^{j'} \cdots  \otimes f^{js'}$  are given by
$$(t')_{j'...j'}^{i'1...i'r} = t_{j1...js}^{i1...ir}a_{i1}^{i'1} \cdots  a_{ir}^{i'r} \cdots  b_{j'}^{j1} \cdots  b_{j'}^{js}.$$
$$1s1s$$
Observe that the Einstein summation convention pays offin avoiding many summation
$$symbols ( \sum  ).$$
In the special case where $E = F$ and $\phi$  is the identity, we obtain a formula expressing how the components of a tensor change under a change of basis. This makes a connection with the old-fashion method for defining tensors. Another operation on general tensors, contraction, is useful in differential geometry.
