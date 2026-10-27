# Permutations, Signature of a Permutation


<!-- PAGE 219 -->
Chapter $7$ Determinants In this chapter all vector spaces are defined over an arbitrary field $K$. For the sake of concreteness, the reader may safely assume that $K =\mathbb{R}$.

## 7.1 Permutations, Signature of a Permutation

This chapter contains a review of determinants and their use in linear algebra. We begin with permutations and the signature of a permutation. Next, we define multilinear maps and alternating multilinear maps. Determinants are introduced as alternating multilinear maps taking the value $1$ on the unit matrix (following Emil Artin). It is then shown how to compute a determinant using the Laplace expansion formula, and the connection with the usual definition is made. It is shown how determinants can be used to invert matrices and to solve (at least in theory!) systems of linear equations (the Cramer formulae). The determinant of a linear map is defined. We conclude by defining the characteristic polynomial of a matrix (and of a linear map) and by proving the celebrated Cayley-Hamilton theorem which states that every matrix is a “zero” of its characteristic polynomial (we give two proofs; one computational, the other one more conceptual). Determinants can be defined in several ways. For example, determinants can be defined in a fancy way in terms of the exterior algebra (or alternating algebra) of a vector space. We will follow a more algorithmic approach due to Emil Artin. No matter which approach is followed, we need a few preliminaries about permutations on a finite set. We need to show that every permutation on $n$ elements is a product of transpositions, and that the parity of the number of transpositions involved is an invariant of the permutation. Let $[n] = {1, 2 \dots  , n}$, where $n \in \mathbb{N}$, and $n > 0$.

> **Definition 7.1.** A permutation on $n$ elements is a bijection $\pi$ : $[n] \to [n]$. When $n = 1$, the only function from $[1]$ to $[1]$ is the constant map: $1 \mapsto 1$. Thus, we will assume that $n \ge 2$. A transposition is a permutation $\tau$  : $[n] \to [n]$ such that, for some $i < j$ (with $1 \le i < j \le n), \tau (i) = j, \tau (j) = i$, and $\tau (k) = k$, for all $k \in [n] -{i, j}$. In other words, a transposition exchanges two distinct elements $i, j \in [n]$. A cyclic permutation of order $k$ (or $k$-cycle) is a
$$219$$

<!-- PAGE 220 -->
permutation $\sigma$ : $[n] \to [n]$ such that, for some sequence $(i_{1}, i_{2}, \dots  , i_{k})$ of distinct elements of $[n]$ with $2 \le k \le n$,
$$\sigma (i_{1}) = i_{2}, \sigma (i_{2}) = i_{3}, \dots  , \sigma (i_{k-1}) = i_{k}, \sigma (i_{k}) = i_{1},$$
and $\sigma (j) = j$, for $j \in [n]-{i_{1}, \dots  , i_{k}}$. The set ${i_{1}, \dots  , i_{k}}$ is called the domain of the cyclic permutation, and the cyclic permutation is usually denoted by $(i_{1} i_{2} \dots  i_{k})$. If $\tau$  is a transposition, clearly, $\tau  \circ \tau  =$ id. Also, a cyclic permutation of order $2$ is a transposition, and for a cyclic permutation $\sigma$  of order $k$, we have $\sigma^{k} =$ id. Clearly, the composition of two permutations is a permutation and every permutation has an inverse which is also a permutation. Therefore, the set of permutations on $[n]$ is a group often denoted $\mathfrak{S}_{n}$. It is easy to show by induction that the group $\mathfrak{S}_{n}$ has $n$! elements. We will also use the terminology product of permutations (or transpositions), as a synonym for composition of permutations. A permutation $\sigma$  on $n$ elements, say $\sigma (i) = k_{i}$ for $i = 1, \dots  , n$, can be represented in functional notation by the $2 \times  n$ array
$$\begin{pmatrix} 1 \\ \cdots & i & \cdots & n \\ k_{1} & \cdots & k_{i} & \cdots & k_{n} \end{pmatrix}$$
known as Cauchy two-line notation. For example, we have the permutation $\sigma$  denoted by
$$\begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 2 & 4 & 3 & 6 & 5 & 1 \end{pmatrix} .$$
A more concise notation often used in computer science and in combinatorics is to represent a permutation by its image, namely by the sequence
$$\sigma (1) \sigma (2) \cdots  \sigma (n)$$
written as a row vector without commas separating the entries. The above is known as the one-line notation. For example, in the one-line notation, our previous permutation $\sigma$  is represented by
$$2 4 3 6 5 1.$$
The reason for not enclosing the above sequence within parentheses is avoid confusion with the notation for cycles, for which is it customary to include parentheses. The following proposition shows the importance of cyclic permutations and transpositions.

> **Proposition 7.1.** For every $n \ge 2$, for every permutation $\pi$ : $[n] \to [n]$, there is a partition of $[n]$ into $r$ subsets called the orbits of $\pi$ , with $1 \le r \le n$, where each set $J$ in this partition is either a singleton ${i}$, or it is of the form
$$J = {i, \pi (i), \pi^{2} (i), \dots  , \pi^{ri-1} (i)},$$

<!-- PAGE 221 -->
where $r_{i}$ is the smallest integer, such that, $\pi^{ri} (i) = i$ and $2 \le r_{i} \le n$. If $\pi$  is not the identity, then it can be written in a unique way (up to the order) as a composition $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$ of cyclic permutations with disjoint domains, where $s$ is the number of orbits with at least two elements. Every permutation $\pi$ : $[n] \to [n]$ can be written as a nonempty composition of transpositions.

*Proof.* Consider the relation $R_{\pi}$ defined on $[n]$ as follows: $iR_{\pi}j$ iff there is some $k \ge 1$ such that $j = \pi^{k} (i)$. We claim that $R_{\pi}$ is an equivalence relation. Transitivity is obvious. We claim that for every $i \in [n]$, there is some least $r (1 \le r \le n)$ such that $\pi^{r} (i) = i$. Indeed, consider the following sequence of $n + 1$ elements:
$$\langle i, \pi (i), \pi^{2} (i), \dots  , \pi^{n} (i)\rangle .$$
Since $[n]$ only has $n$ distinct elements, there are some $h, k$ with $0 \le h < k \le n$ such that
$$\pi^{h} (i) = \pi^{k} (i),$$
and since $\pi$  is a bijection, this implies $\pi^{k-h} (i) = i$, where $0 \le k$ - $h \le n$. Thus, we proved that there is some integer $m \ge 1$ such that $\pi^{m} (i) = i$, so there is such a smallest integer $r$. Consequently, $R_{\pi}$ is reflexive. It is symmetric, since if $j = \pi^{k} (i)$, letting $r$ be the least $r \ge 1$ such that $\pi^{r} (i) = i$, then
$$i = \pi^{kr} (i) = \pi^{k(r-1)} (\pi^{k} (i)) = \pi^{k(r-1)} (j).$$
Now, for every $i \in [n]$, the equivalence class (orbit) of $i$ is a subset of $[n]$, either the singleton ${i}$ or a set of the form
$$J = {i, \pi (i), \pi^{2} (i), \dots  , \pi^{ri-1} (i)},$$
where $r_{i}$ is the smallest integer such that $\pi^{ri} (i) = i$ and $2 \le r_{i} \le n$, and in the second case, the restriction of $\pi$  to $J$ induces a cyclic permutation $\sigma_{i}$ , and $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$ , where $s$ is the number of equivalence classes having at least two elements. For the second part of the proposition, we proceed by induction on $n$. If $n = 2$, there are exactly two permutations on $[2]$, the transposition $\tau$  exchanging $1$ and $2$, and the identity. However, $id_{2} = \tau^{2}$  . Now, let $n \ge 3$. If $\pi (n) = n$, since by the induction hypothesis, the restriction of $\pi$  to $[n$ - $1]$ can be written as a product of transpositions, $\pi$  itself can be written as a product of transpositions. If $\pi (n) = k \neq  n$, letting $\tau$  be the transposition such that $\tau (n) = k$ and $\tau (k) = n$, it is clear that $\tau  \circ \pi$  leaves $n$ invariant, and by the induction hypothesis, we have $\tau  \circ \pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$  for some transpositions, and thus
$$\pi  = \tau  \circ \tau_{m}  \circ \dots  \circ \tau_{1} ,$$
a product of transpositions (since $\tau  \circ \tau  = id_{n})$.

<!-- PAGE 222 -->
Remark: When $\pi  = id_{n}$ is the identity permutation, we can agree that the composition of $0$ transpositions is the identity. The second part of Proposition 7.1 shows that the transpositions generate the group of permutations $\mathfrak{S}_{n}$. In writing a permutation $\pi$  as a composition $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$  of cyclic permutations, it is clear that the order of the $\sigma_{i}$  does not matter, since their domains are disjoint. Given a permutation written as a product of transpositions, we now show that the parity of the number of transpositions is an invariant.

> **Definition 7.2.** For every $n \ge 2$, since every permutation $\pi$ : $[n] \to [n]$ defines a partition of $r$ subsets over which $\pi$  acts either as the identity or as a cyclic permutation, let $\epsilon (\pi$ ), called the signature of $\pi$ , be defined by $\epsilon (\pi$ ) $= (-1)^{n-r}$, where $r$ is the number of sets in the partition. If $\tau$  is a transposition exchanging $i$ and $j$, it is clear that the partition associated with $\tau$  consists of $n$ - $1$ equivalence classes, the set ${i, j}$, and the $n$ - $2$ singleton sets ${k}$, for $k \in [n] -{i, j}$, and thus, $\epsilon (\tau$ ) $= (-1)^{n-(n-1)} = (-1)^{1} = -1$.

> **Proposition 7.2.** For every $n \ge 2$, for every permutation $\pi$ : $[n] \to [n]$, for every transposition $\tau$ , we have
$$\epsilon (\tau  \circ \pi ) = -\epsilon (\pi ).$$
Consequently, for every product of transpositions such that $\pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$ , we have
$$\epsilon (\pi ) = (-1)^{m},$$
which shows that the parity of the number of transpositions is an invariant.

*Proof.* Assume that $\tau (i) = j$ and $\tau (j) = i$, where $i < j$. There are two cases, depending whether $i$ and $j$ are in the same equivalence class $J_{l}$ of $R_{\pi}$, or if they are in distinct equivalence classes. If $i$ and $j$ are in the same class $J_{l}$, then if
$$J_{l} = {i_{1}, \dots  , i_{p}, \dots  i_{q}, \dots  i_{k}},$$
where $i_{p} = i$ and $i_{q} = j$, since
$$\tau (\pi (\pi^{-1} (i_{p}))) = \tau (i_{p}) = \tau (i) = j = i_{q}$$
and
$$\tau (\pi (i_{q-1})) = \tau (i_{q}) = \tau (j) = i = i_{p},$$
it is clear that $J_{l}$ splits into two subsets, one of which is ${i_{p}, \dots  , i_{q-1}}$, and thus, the number of classes associated with $\tau  \circ \pi$  is $r + 1$, and $\epsilon (\tau  \circ \pi$ ) $= (-1)^{n-r-1} = -(-1)^{n-r} = -\epsilon (\pi$ ). If $i$ and $j$ are in distinct equivalence classes $J_{l}$ and $J_{m}$, say
$${i_{1}, \dots  , i_{p}, \dots  i_{h}}$$
