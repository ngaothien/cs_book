# Alternating Multilinear Maps


<!-- PAGE 223 -->
and
$${j_{1}, \dots  , j_{q}, \dots  j_{k}},$$
where $i_{p} = i$ and $j_{q} = j$, since
$$\tau (\pi (\pi^{-1} (i_{p}))) = \tau (i_{p}) = \tau (i) = j = j_{q}$$
and
$$\tau (\pi (\pi^{-1} (j_{q}))) = \tau (j_{q}) = \tau (j) = i = i_{p},$$
we see that the classes $J_{l}$ and $J_{m}$ merge into a single class, and thus, the number of classes associated with $\tau  \circ \pi$  is $r$ - $1$, and $\epsilon (\tau  \circ \pi$ ) $= (-1)^{n-r+1} = -(-1)^{n-r} = -\epsilon (\pi$ ). Now, let $\pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$  be any product of transpositions. By the first part of the proposition, we have
$$\epsilon (\pi ) = (-1)^{m-1}\epsilon (\tau_{1} ) = (-1)^{m-1}(-1) = (-1)^{m},$$
since $\epsilon (\tau_{1}$ ) $= -1$ for a transposition.
Remark: When $\pi  = id_{n}$ is the identity permutation, since we agreed that the composition of $0$ transpositions is the identity, it it still correct that $(-1)^{0} = \epsilon$ (id) $= +1$. From the proposition, it is immediate that $\epsilon (\pi' \circ \pi$ ) $= \epsilon (\pi' )\epsilon (\pi$ ). In particular, since $\pi^{-1} \circ \pi  = id_{n}$, we get $\epsilon (\pi^{-1}$ ) $= \epsilon (\pi$ ). We can now proceed with the definition of determinants.

## 7.2 Alternating Multilinear Maps

First we define multilinear maps, symmetric multilinear maps, and alternating multilinear maps.
Remark: Most of the definitions and results presented in this section also hold when $K$ is a commutative ring and when we consider modules over $K$ (free modules, when bases are needed). Let $E_{1}, \dots  , E_{n}$, and $F$, be vector spaces over a field $K$, where $n \ge 1$.

> **Definition 7.3.** A function $f$ : $E_{1} \times  \dots  \times  E_{n} \to F$ is a multilinear map (or an $n$-linear map) if it is linear in each argument, holding the others fixed. More explicitly, for every $i, 1 \le i \le n$, for all $x_{1} \in E_{1}, \dots , x_{i-1} \in E_{i-1}, x_{i+1} \in E_{i+1}, \dots , x_{n} \in E_{n}$, for all $x, y \in E_{i}$, for all $\lambda  \in K$,
$$f(x_{1}, \dots  , x_{i-1}, x + y, x_{i+1}, \dots  , x_{n}) = f(x_{1}, \dots  , x_{i-1}, x, x_{i+1}, \dots  , x_{n})$$
$$+ f(x_{1}, \dots  , x_{i-1}, y, x_{i+1}, \dots  , x_{n}),$$
$$f(x_{1}, \dots  , x_{i-1}, \lambda x, x_{i+1}, \dots  , x_{n}) = \lambda f(x_{1}, \dots  , x_{i-1}, x, x_{i+1}, \dots  , x_{n}).$$

<!-- PAGE 224 -->
When $F = K$, we call $f$ an $n$-linear form (or multilinear form). If $n \ge 2$ and $E_{1} = E_{2} = \dots  = E_{n}$, an $n$-linear map $f$ : $E \times  \dots  \times  E \to F$ is called symmetric, if $f(x_{1}, \dots  , x_{n}) = f(x_{\pi(1)}, \dots  , x_{\pi(n)})$ for every permutation $\pi$  on ${1, \dots  , n}$. An $n$-linear map $f$ : $E\times \dots \times E \to F$ is called alternating, if $f(x_{1}, \dots  , x_{n}) = 0$ whenever $x_{i} = x_{i+1}$ for some $i, 1 \le i \le n$ - $1$ (in other words, when two adjacent arguments are equal). It does no harm to agree that when $n = 1$, a linear map is considered to be both symmetric and alternating, and we will do so. When $n = 2$, a 2-linear map $f$ : $E_{1} \times  E_{2} \to F$ is called a bilinear map. We have already seen several examples of bilinear maps. Multiplication $\cdot$ : $K \times  K \to K$ is a bilinear map, treating $K$ as a vector space over itself. The operation $\langle$ -, $-\rangle$ : $E^{*} \times  E \to K$ applying a linear form to a vector is a bilinear map. Symmetric bilinear maps (and multilinear maps) play an important role in geometry (inner products, quadratic forms) and in differential calculus (partial derivatives). A bilinear map is symmetric if f(u, $v) =$ f(v, $u)$, for all $u, v \in E$. Alternating multilinear maps satisfy the following simple but crucial properties.

> **Proposition 7.3.** Let $f$ : $E \times  \dots  \times  E \to F$ be an $n$-linear alternating map, with $n \ge 2$. The following properties hold: $(1)$
$$f(\dots  , x_{i}, x_{i+1}, \dots ) = -f(\dots  , x_{i+1}, x_{i}, \dots )$$
$(2)$
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = 0,$$
where $x_{i} = x_{j}$, and $1 \le i < j \le n. (3)$
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = -f(\dots  , x_{j}, \dots  , x_{i}, \dots ),$$
where $1 \le i < j \le n. (4)$
$$f(\dots  , x_{i}, \dots ) = f(\dots  , x_{i} + \lambda x_{j}, \dots ),$$
for any $\lambda  \in K$, and where $i \neq  j$.

*Proof.* $(1)$ By multilinearity applied twice, we have
$$f(\dots  , x_{i} + x_{i+1}, x_{i} + x_{i+1}, \dots ) = f(\dots  , x_{i}, x_{i}, \dots ) + f(\dots  , x_{i}, x_{i+1}, \dots )$$
$$+ f(\dots  , x_{i+1}, x_{i}, \dots ) + f(\dots  , x_{i+1}, x_{i+1}, \dots ),$$
and since $f$ is alternating, this yields
$$0 = f(\dots  , x_{i}, x_{i+1}, \dots ) + f(\dots  , x_{i+1}, x_{i}, \dots ),$$

<!-- PAGE 225 -->
that is, $f(\dots  , x_{i}, x_{i+1}, \dots$ ) $= -f(\dots  , x_{i+1}, x_{i}, \dots$ ).
$(2)$ If $x_{i} = x_{j}$ and $i$ and $j$ are not adjacent, we can interchange $x_{i}$ and $x_{i+1}$, and then $x_{i}$ and $x_{i+2}$, etc, until $x_{i}$ and $x_{j}$ become adjacent. By $(1)$,
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = \epsilon f(\dots  , x_{i}, x_{j}, \dots ),$$
where $\epsilon  = +1$ or $-1$, but $f(\dots  , x_{i}, x_{j}, \dots$ ) $= 0$, since $x_{i} = x_{j}$, and $(2)$ holds.
$(3)$ follows from $(2)$ as in $(1). (4)$ is an immediate consequence of $(2)$. Proposition 7.3 will now be used to show a fundamental property of alternating multilinear maps. First we need to extend the matrix notation a little bit. Let $E$ be a vector space over $K$. Given an $n \times  n$ matrix $A = (a_{i j})$ over $K$, we can define a map L(A): $E^{n} \to E^{n}$ as follows:
$$L(A)_{1}(u) = a_{1 1}u_{1} + \cdots  + a_{1n}u_{n},$$
$$\dots$$
$$L(A)_{n}(u) = a_{n1}u_{1} + \cdots  + a_{n n}u_{n},$$
for all $u_{1}, \dots  , u_{n} \in E$ and with $u = (u_{1}, \dots  , u_{n})$. It is immediately verified that L(A) is linear. Then given two $n\times n$ matrices $A = (a_{i j})$ and $B = (b_{i j})$, by repeating the calculations establishing the product of matrices (just before Definition 3.12), we can show that
$$L(AB) = L(A) \circ L(B).$$
It is then convenient to use the matrix notation to describe the effect of the linear map L(A), as
$$\begin{pmatrix} L(A)_{1}(u) \\ L(A)_{2}(u) \\ \vdots \\ L(A)_{n}(u) \end{pmatrix} = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} .$$

> **Lemma 7.4.** Let $f$ : $E \times  \dots  \times  E \to F$ be an $n$-linear alternating map. Let $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$ be two families of $n$ vectors, such that,
$$v_{1} = a_{1 1}u_{1} + \cdots  + a_{n1}u_{n},$$
$$\dots$$
$$v_{n} = a_{1n}u_{1} + \cdots  + a_{n n}u_{n}.$$
Equivalently, letting
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$

<!-- PAGE 226 -->
assume that we have
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = A^{\top} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} .$$
Then,
$$f(v_{1}, \dots  , v_{n}) = \begin{pmatrix} \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n} \\ \pi \end{pmatrix} \sum_{\in Sn}  f(u_{1}, \dots  , u_{n}),$$
where the sum ranges over all permutations $\pi$  on ${1, \dots  , n}$.

*Proof.* Expanding $f(v_{1}, \dots  , v_{n})$ by multilinearity, we get a sum of terms of the form
$$a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{\pi(1)}, \dots  , u_{\pi(n)}),$$
for all possible functions $\pi$ : ${1, \dots  , n} \to {1, \dots  , n}$. However, because $f$ is alternating, only the terms for which $\pi$  is a permutation are nonzero. By Proposition 7.1, every permutation $\pi$  is a product of transpositions, and by Proposition 7.2, the parity $\epsilon (\pi$ ) of the number of transpositions only depends on $\pi$ . Then applying Proposition 7.3 $(3)$ to each transposition in $\pi$ , we get
$$a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{\pi(1)}, \dots  , u_{\pi(n)}) = \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{1}, \dots  , u_{n}).$$
Thus, we get the expression of the lemma. For the case of $n = 2$, the proof details of Lemma 7.4 become
$$f(v_{1}, v_{2}) = f(a_{11}u_{1} + a_{21}u_{2}, a_{12}u_{1} + a_{22}u_{2})$$
$$= f(a_{11}u_{1} + a_{21}u_{2}, a_{12}u_{1}) + f(a_{11}u_{1} + a_{21}u_{2}, a_{22}u_{2})$$
$$= f(a_{11}u_{1}, a_{12}u_{1}) + f(a_{21}u_{2}, a_{12}u_{1}) + f(a_{11}u_{1}, a_{22}u_{2}) + f(a_{21}u_{2}, a_{22}u_{2})$$
$$= a_{11}a_{12}f(u_{1}, u_{1}) + a_{21}a_{12}f(u_{2}, u_{1}) + a_{11}a_{22}f(u_{1}, u_{2}) + a_{21}a_{22}f(u_{2}, u_{2})$$
$$= a_{21}a_{12}f(u_{2}, u_{1})a_{11}a_{22}f(u_{1}, u_{2})$$
$$= (a_{11}a_{22} -a_{12}a_{22}) f(u_{1}, u_{2}).$$
Hopefully the reader will recognize the quantity $a_{11}a_{22} -a_{12}a_{22}$. It is the determinant of the $2 \times  2$ matrix
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} .$$
This is no accident. The quantity
$$\det(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}$$
