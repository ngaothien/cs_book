# Linear Forms and the Dual Space


<!-- PAGE 112 -->
Proposition 3.25 shows that we can define addition and multiplication by a scalar on the set $E/M$ of equivalence classes of the equivalence relation $\equiv_{M}$ .

> **Definition 3.25.** Given any vector space $E$ and any subspace $M$ of $E$, we define the following operations of addition and multiplication by a scalar on the set $E/M$ of equivalence classes of the equivalence relation $\equiv_{M}$  as follows: for any two equivalence classes $[u], [v] \in E/M$, we have
$$[u] + [v] = [u + v],$$
$$\lambda [u] = [\lambda u].$$
By Proposition 3.25, the above operations do not depend on the specific choice of representatives in the equivalence classes $[u], [v] \in E/M$. It is also immediate to verify that $E/M$ is a vector space. The function $\pi$ : $E \to E/F$, defined such that $\pi (u) = [u]$ for every $u \in E$, is a surjective linear map called the natural projection of $E$ onto $E/F$. The vector space $E/M$ is called the quotient space of $E$ by the subspace $M$. Given any linear map $f$ : $E \to F$, we know that Ker $f$ is a subspace of $E$, and it is immediately verified that Im $f$ is isomorphic to the quotient space $E/Ker f$.

## 3.9 Linear Forms and the Dual Space

We already observed that the field $K$ itself $(K =\mathbb{R}$ or $K =\mathbb{C})$ is a vector space (over itself). The vector space Hom(E, $K)$ of linear maps from $E$ to the field $K$, the linear forms, plays a particular role. In this section, we only define linear forms and show that every finite-dimensional vector space has a dual basis. A more advanced presentation of dual spaces and duality is given in Chapter $11$.

> **Definition 3.26.** Given a vector space $E$, the vector space Hom(E, $K)$ of linear maps from $E$ to the field $K$ is called the dual space (or dual) of $E$. The space Hom(E, $K)$ is also denoted by $E^{*}$, and the linear maps in $E^{*}$ are called the linear forms, or covectors. The dual space $E^{**}$ of the space $E^{*}$ is called the bidual of $E$. As a matter of notation, linear forms $f$ : $E \to K$ will also be denoted by starred symbol, such as $u^{*}, x^{*}$, etc. If $E$ is a vector space of finite dimension $n$ and $(u_{1}, \dots  , u_{n})$ is a basis of $E$, for any linear form $f^{*} \in E^{*}$, for every $x = x_{1}u_{1} + \cdots  + x_{n}u_{n} \in E$, by linearity we have
$$f^{*} (x) = f^{*} (u_{1})x_{1} + \cdots  + f^{*} (u_{n})x_{n}$$
$$= \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n},$$
with $\lambda_{i}  = f^{*} (u_{i}) \in K$ for every $i, 1 \le i \le n$. Thus, with respect to the basis $(u_{1}, \dots  , u_{n})$, the linear form $f^{*}$ is represented by the row vector
$$(\lambda_{1}  \cdots  \lambda_{n} ),$$

<!-- PAGE 113 -->
we have
$$f^{*} (x) = \begin{pmatrix} \lambda_{1} & \cdots & \lambda_{n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} ,$$
a linear combination of the coordinates of $x$, and we can view the linear form $f^{*}$ as a linear equation. If we decide to use a column vector of coefficients
$$c = \begin{pmatrix} c_{1} \\ \vdots \\ c_{n} \end{pmatrix}$$
instead of a row vector, then the linear form $f^{*}$ is defined by
$$f^{*} (x) = c^{\top}x.$$
The above notation is often used in machine learning.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Example 3.7.** Given any differentiable function $f$ : $\to$ , by definition, for any $x \in$ ,
$$\mathbb{R}^{n} \mathbb{R}$$
the total derivative $df_{x}$ of $f$ at $x$ is the linear form $df_{x}$ : $\to$  defined so that for all $u = (u_{1}, \dots  , u_{n}) \in \mathbb{R}^{n}$,
$$df_{x}(u) = \begin{pmatrix} \partial f \\ \partial f \\ (x) & \cdots & (x) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = \sum_{i=1}^{n}  \frac{\partial f}{\partial x_{i}} (x) u_{i}.$$

> **Example 3.8.** Let $\mathcal{C}([0, 1])$ be the vector space of continuous functions $f$ : $[0, 1] \to \mathbb{R}$. The map $\mathcal{I}$ : $\mathcal{C}([0, 1]) \to \mathbb{R}$ given by
$$\mathcal{I}(f) = \int_{0}^{}  1f(x)dxfor any f \in C([0, 1])$$
is a linear form (integration).

> **Example 3.9.** Consider the vector space $M_{n}(\mathbb{R})$ of real $n\times n$ matrices. Let tr: $M_{n}(\mathbb{R}) \to \mathbb{R}$ be the function given by
$$\mathrm{tr}(A) = a_{11} + a_{22} + \cdots  + a_{nn},$$
called the trace of $A$. It is a linear form. Let $s: M_{n}(\mathbb{R}) \to \mathbb{R}$ be the function given by
$$s(A) = \sum_{i,j=1}^{n}  a_{ij},$$
where $A = (a_{ij})$. It is immediately verified that $s$ is a linear form.

<!-- PAGE 114 -->
Given a vector space $E$ and any basis $(u_{i})_{i\in I}$ for $E$, we can associate to each $u_{i}$ a linear form $u_{i}^{*} \in E^{*}$, and the $u_{i}^{*}$ have some remarkable properties.

> **Definition 3.27.** Given a vector space $E$ and any basis $(u_{i})_{i\in I}$ for $E$, by Proposition 3.20, for every $i \in$ I, there is a unique linear form $u_{i}^{*}$ such that
$$1if i = j$$
$$u_{i}^{*} (u_{j}) =$$
$$0if i \neq  j,$$
for every $j \in$ I. The linear form $u_{i}^{*}$ is called the coordinate form of index $i$ w.r.t. the basis $(u_{i})_{i\in I}$.
Remark: Given an index set $I$, authors often define the so called “Kronecker symbol” $\delta_{i j}$ such that
$$1if i = j$$
$$\delta_{i j}  =$$
$$0if i \neq  j,$$
for all $i, j \in$ I. Then, $u_{i}^{*} (u_{j}) = \delta_{i j}$ . The reason for the terminology coordinate form is as follows: If $E$ has finite dimension and if $(u_{1}, \dots  , u_{n})$ is a basis of $E$, for any vector
$$v = \lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n},$$
we have
$$u_{i}^{*} (v) = u_{i}^{*} (\lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n})$$
$$= \lambda_{1} u_{i}^{*} (u_{1}) + \cdots  + \lambda_{i} u_{i}^{*} (u_{i}) + \cdots  + \lambda_{n} u_{i}^{*} (u_{n})$$
$$= \lambda_{i} ,$$
since $u_{i}^{*} (u_{j}) = \delta_{i j}$ . Therefore, $u_{i}^{*}$ is the linear function that returns the ith coordinate of a vector expressed over the basis $(u_{1}, \dots  , u_{n})$. The following theorem shows that in finite-dimension, every basis $(u_{1}, \dots  , u_{n})$ of a vector space $E$ yields a basis $(u_{1}^{*}, \dots  , u_{n}^{*})$ of the dual space $E^{*}$, called a dual basis.

> **Theorem 3.26.** (Existence of dual bases) Let $E$ be a vector space of dimension $n$ over the field $K$. The following properties hold: For every basis $(u_{1}, \dots  , u_{n})$ of $E$, the family of coordinate forms $(u_{1}^{*}, \dots  , u_{n}^{*})$ is a basis of $E^{*}$ (called the dual basis of $(u_{1}, \dots  , u_{n}))$.

*Proof.* (a) If $v^{*} \in E^{*}$ is any linear form, consider the linear form
$$f^{*} = v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*}.$$
Observe that because $u_{i}^{*} (u_{j}) = \delta_{i j}$ ,
$$f^{*} (u_{i}) = (v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*})(u_{i})$$
$$= v^{*}(u_{1})u_{1}^{*}(u_{i}) + \cdots  + v^{*}(u_{i})u_{i}^{*} (u_{i}) + \cdots  + v^{*}(u_{n})u_{n}^{*}(u_{i})$$
$$= v^{*}(u_{i}),$$

<!-- PAGE 115 -->
and so $f^{*}$ and $v^{*}$ agree on the basis $(u_{1}, \dots  , u_{n})$, which implies that
$$v^{*}= f^{*} = v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*}.$$
Therefore, $(u_{1}^{*}, \dots  , u_{n}^{*})$ spans $E^{*}$. We claim that the covectors $u_{1}^{*}, \dots  , u_{n}^{*}$ are linearly independent. If not, we have a nontrivial linear dependence
$$\lambda_{1} u_{1}^{*} + \cdots  + \lambda_{n} u_{n}^{*} = 0^{*},$$
where $0^{*}$ denotes the linear form such that $0^{*}(v) = 0$ for all $v \in E$ (with $0 \in K)$, and if we apply the above linear form to each $u_{i}$, we have
$$(\lambda_{1} u_{1}^{*} + \cdots  + \lambda_{n} u_{n}^{*})(u_{i}) = \lambda_{1} u_{1}^{*}(u_{i}) + \cdots  + \lambda_{i} u_{i}^{*} (u_{i}) + \cdots  + \lambda_{n} u_{n}^{*}(u_{i}) = \lambda_{i}  = 0,$$
proving that $u_{1}^{*}, \dots  , u_{n}^{*}$ are indeed linearly independent. Therefore, $(u_{1}^{*}, \dots  , u_{n}^{*})$ is a basis of $E^{*}$. In particular, Theorem 3.26 shows a finite-dimensional vector space and its dual $E^{*}$ have the me dimension.

> **Example 3.10.** Consider the vector $space\mathbb{R}[X]_{n}$ of polynomials in the variable $X$ of degree at most $n$ with real coefficients. We know that it has the basis $(1, X, X^{2}, \dots  , X^{n})$. If we write $e_{i} = X^{i}$, the dual basis vectors $e_{i}^{*}$ are the linear forms defined on polynomials which are uniquely defined by the equations
$$e_{i}^{*} (e_{j}) = e_{i}^{*} (X^{j}) = \delta_{ij} .$$
We can identify explicitly the linear forms $e_{i}^{*}$ . Indeed, for any $i$ such that $0 \le i \le n$, if $D^{(i)}$ is the linear form defined by $D^{(i)} = D \circ \cdots  \circ D$ , where $D$ is the differentiation operator
$$|{z}$$
$$i$$
on polynomials, in other words, for any polynomial $P \in \mathbb{R}[X]_{n}, D^{(i)}P$ is the result of differentiating $P i$ times (with $D^{(0)} =$ id), then $e_{i}^{*}$ given by
$$e_{i}^{*} (P) = \frac{1}{i!} (D^{(i)}P)(0)$$
does the job, since
$$i!X^{j-i},if j > i$$
$$$$
$$$$
$$D^{(i)}X^{j}=i!,if j = i$$
$$0,if j < i,$$
$$$$
so when we evaluate $D^{(i)}X^{j}$ at $0$, we get $\delta_{ij}$ . We explained just after Definition 3.26 that if the space $E$ is finite-dimensional and has a finite basis $(u_{1}, \dots  , u_{n})$, then a linear form $f^{*}$ : $E \to K$ is represented by the row vector of coefficients
$$\begin{pmatrix} f^{*}(u_{1}) & \cdots & f^{*}(u_{n}) \end{pmatrix} .(1)$$
