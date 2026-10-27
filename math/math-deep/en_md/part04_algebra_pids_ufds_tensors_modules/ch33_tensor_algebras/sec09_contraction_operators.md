# Contraction Operators


<!-- PAGE 1211 -->

## 33.9 Contraction Operators


> **Definition 33.19.** For all $r, s \ge 1$, the contraction $c_{i,j}$ : $T^{r,s} (V$ ) $\to T^{r-1,s-1} (V$ ), with $1 \le i \le r$ and $1 \le j \le s$, is the linear map defined on generators by $c_{i,j}(u_{1} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{s}$ )
$$= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s} ,$$
$$c$$
$$b$$
$u_{i} \in V , \omega^{j} \in V^{*}$, where the hat over an argument means that it should be omitted. Note that since $T^{r,s}(V$ ) is the tensor product $T^{r,s}(V$ ) $= V^{\otimes r} \otimes (V^{*})^{\otimes s}$, the map $c_{i,j}$ is the unique linear extension of the multilinear map from $V^{r} \times  (V^{*})^{s}$ to $V^{\otimes r} \otimes (V^{*})^{\otimes s}$ given by $c_{i,j}(u_{1}, \dots  , u_{r}, \omega^{1} , \dots  , \omega^{s}$ ) $= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s}$ .
$$c$$
$$b$$
Therefore this definition is intrinsic, that is, does not depend on any choice of basis.
Remark: Note that the notation $c_{i,j}$ is ambiguous, since technically we have an operator $c_{i,j}^{r,s}$ : $T^{r,s}(V$ ) $\to T^{r-1,s-1}(V$ ) for every pair $r, s \ge 1$, with $1 \le i \le r$ and $1 \le j \le s$, and $c_{i,j}^{s,r}$ ̸ $= c_{i,j}^{r',s'}$ if $(r$, s)̸ $=$ (r', s'), $1 \le i \le$ min(r, r') and $1 \le j \le$ min(s, s'). However it is customary to omit the superscripts $r$ and $s$ and rely on context to infer $r$ and $s$. The notation $c_{i,j}$ is also used by Gallot, Hulin, Lafontaine $[77]$, but Sakai $[147]$ uses $c_{j}^{i}$, and O’Neill $[137]$ uses $c_{i}^{j}$. Let us figure our what is $c_{1,1}$ : $T^{1,1} (V$ ) $\to \mathbb{R}$, that is $c_{1,1}$ : $V \otimes V^{*} \to \mathbb{R}$. If $(e_{1}, \dots  , e_{n})$ is a basis of $V$ and $(e^{1}, \dots  , e^{n})$ is the dual basis, by Proposition 33.12, every $h \in V \otimes V^{*}$ can be expressed as
$$h = a_{j}^{i} e_{i} \otimes e^{j}.$$
As
$$c_{1,1}(e_{i} \otimes e^{j}) = \delta_{i,j} ,$$
we get
$$c_{1,1}(h) = a_{i}^{i}.$$
Remark: By Proposition 33.25, $V \otimes V^{*}$ is isomorphic $to\mathcal{T}^{1,1} (V$ ), and by Proposition 33.26, $\mathcal{T}^{1,1} (V$ ) is isomorphic to Hom(V, $V$ ). Thus we can view $h \in V \otimes V^{*}$ as linear map. The matrix of $h$ over the basis $(e_{1}, \dots  , e_{n})$ is also $(a_{j}^{i})$, so tr(h) $= a_{i}^{i}$ is its trace. Since $c_{1,1}$ is defined independently of any basis, $c_{1,1}$ provides an intrinsic definition of the trace of a linear map $h \in$ Hom(V, $V$ ). The notion of contraction transfers to the space $\mathcal{T}^{r,s} (V$ ), but at first glance, we don’t have an intrinsic definition since it appears that we have to resort to bases. There is a way to circumvent this problem as explained in O’Neill $[137]$ (Chapter $2$, Lemma $6)$. The first step is to show that the contraction $c_{1,1}$ from $\mathcal{T}^{1,1} (V$ ) to $K$ is intrinsically defined.

<!-- PAGE 1212 -->

> **Proposition 33.30.** There is a unique linear map $c_{1,1}$ : $\mathcal{T}^{1,1} (V$ ) $\to K$ such that
$$c_{1,1}(\mu (u \otimes \theta )) = \theta (u),u \in V, \theta  \in V^{*} .$$

*Proof.* If we pick a basis $(e_{1}, \dots  , e_{n})$ of $V$ , we see immediately that for any $T \in T^{1,1} (V$ ) expressed as
$$T = t_{j}^{i} e_{i} \otimes e^{j},$$
(again, writing $e_{i} \otimes e^{j}$ instead of $\mu (e_{i} \otimes e^{j}))$, since $c_{1,1}(e_{i} \otimes e^{j}) = e^{j}(e_{i}) = \delta_{ij}$ , we must have
$$c_{1,1}(T) = t_{i}^{i}.$$
Given another basis $(f_{1}, \dots  , f_{n})$, if this basis is expressed in terms of the basis $(e_{1}, \dots  , e_{n})$ as
$$e_{i} = a_{i}^{j}f_{j},$$
then by Proposition 33.29), we have
$$f^{i}= a_{j}^{i}e^{j},$$
so if $(b_{i}^{j})$ is the inverse of $(a_{i}^{j})$, we obtain
$$T = t_{j}^{i}a_{i}^{k} b_{l}^{j} f_{k} \otimes f^{l},$$
and thus the contracted tensor over the new bases is given by
$$c_{1,1}'(T) = t_{j}^{i}a_{i}^{k} b_{k}^{j}.$$
But $(b_{i}^{j})$ is the inverse of $(a_{i}^{j})$, so $a_{i}^{k} b_{k}^{j} = \delta_{ij}$ , which implies by Proposition 33.29 that
$$c_{1,1}'(T) = t_{i}^{i} = c_{1,1}(T).$$
Therefore, $c_{1,1}(T)$ is independent of the choice of basis. In the general case, we have the following result.

> **Proposition 33.31.** There is a unique linear map $c_{i,j}$ : $\mathcal{T}^{r,s} (V$ ) $\to T^{r-1,s-1} (V$ ), with $1 \le i \le r$ and $1 \le j \le s$, such that (omitting the map $\mu$ ) $c_{i,j}(u_{1} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{s}$ )
$$= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s} ,$$
$$c$$
$$b$$
$u_{i} \in V , \omega^{j} \in V^{*}$.

<!-- PAGE 1213 -->

*Proof.* If we pick a basis $(e_{1} \dots  , e_{n})$ in $V$ , using the Einstein summation convention, (omitting the map $\mu$ ), for any $\alpha  \in T^{r,s} (V$ ), we can write
$$\alpha  = a_{j1...js}^{i1...ir} e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e^{js},$$
and since $e^{j}(e_{i}) = \delta_{ij}$ , we must have
$$c_{k,l}(\alpha ) = a_{j1...jl-1mjl+1...js}^{i1...ik-1mik+1...ir} e_{i1} \otimes \cdots  \otimes e_{ik} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e_{l}^{j}\otimes \cdots  \otimes e^{js},$$
$$c$$
$$c$$
where the repeated index $m$ appears as a superscript in position $k$ and as a subscript in position $l$, so according to the Einstein summation convention,
$$a_{j1...jl-1mjl+1...,js}^{i1...ik-1mik+1...ir}$$
denotes the sum
$$\sum_{m=1}^{n}  a_{j1...jl-1mjl+1...js}^{i1...ik-1mik+1...ir} .$$
Given another basis $(f_{1}, \dots  , f_{n})$, if this basis is expressed in terms of the basis $(e_{1}, \dots  , e_{n})$ as
$$e_{i} = a_{i}^{j}f_{j},$$
then by Proposition 33.29, we have
$$\alpha  = t_{j1...js}^{i1...ir}a_{i1}^{i'1} \cdots  a_{ir}^{i'r} \cdots  b_{j'}^{j1} \cdots  b_{j'}^{js} f_{i1'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f^{js'} .$$
$$1s$$
Consequently, contracting on the pair of indices $(i_{k}', j_{l}')$, the contracted tensor over the new bases is given by
$$c_{k,l}'(\alpha ) = t_{j1...m...js}^{i1...m...ir}a_{i1}^{i'1} \cdots a_{ik}^{m} \cdots  a_{ir}^{i'r} b_{j'}^{j1} \cdots  cb_{m}^{jl} \cdots  b_{j'}^{js}$$
$$c$$
$$1s$$
$$f_{i1'} \otimes \cdots  \otimes f_{ik'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f_{l}^{j'}  \otimes \cdots  \otimes f^{js'} .$$
$$cc$$
Since $(b_{i}^{j})$ is the inverse of $(a_{i}^{j})$, we have $a_{ik}^{m}b_{m}^{jl} = \delta_{ikjl}$ , which implies that
$$c_{k,l}'(\alpha ) = t_{j1...m...js}^{i1...m...ir}a_{i1}^{i'1} \cdots a_{ik}^{m} \cdots  a_{ir}^{i'r} b_{j'}^{j1} \cdots  cb_{m}^{jl} \cdots  b_{j'}^{js}$$
$$c$$
$$1s$$
$$f_{i1'} \otimes \cdots  \otimes f_{ik'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f_{l}^{j'}  \otimes \cdots  \otimes f^{js'}$$
$$cc$$
$$= t_{j1...m...js}^{i1...m...ir} e_{i1} \otimes \cdots  \otimes e_{ik} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e_{l}^{j}\otimes \cdots  \otimes e^{js}$$
$$c$$
$$c$$
$$= c_{k,l}(\alpha ).$$
Therefore, the definition of $c_{k,l}$ is intrinsic; it does not depend on the choice of basis. We now turn to symmetric tensors.
