# Indexed Families; the Sum Notation i I ai


<!-- PAGE 72 -->
$8$. A very important example of vector space is the set of linear maps between two vector spaces to be defined in Section 11.1. Here is an example that will prepare us for the vector space of linear maps. Let $X$ be any nonempty set and let $E$ be a vector space. The set of all functions $f$ : $X \to E$ can be made into a vector space as follows: Given any two functions $f$ : $X \to E$ and $g: X \to E$, let $(f + g): X \to E$ be defined such that
$$(f + g)(x) = f(x) + g(x)$$
for all $x \in X$, and for every $\lambda  \in \mathbb{R}$, let $\lambda f$ : $X \to E$ be defined such that
$$(\lambda f)(x) = \lambda f(x)$$
for all $x \in X$. The axioms of a vector space are easily verified. Let $E$ be a vector space. We would like to define the important notions of linear combination and linear independence. Before defining these notions, we need to discuss a strategic choice which, depending how it is settled, may reduce or increase headaches in dealing with notions such as linear combinations and linear dependence (or independence). The issue has to do with using sets of vectors versus sequences of vectors.
$$3.3Indexed Families; the Sum Notation \sum  i\in I ai$$
Our experience tells us that it is preferable to use sequences of vectors; even better, indexed families of vectors. (We are not alone in having opted for sequences over sets, and we are in good company; for example, Artin $[7]$, Axler $[10]$, and Lang $[113]$ use sequences. Nevertheless, some prominent authors such as Lax $[117]$ use sets. We leave it to the reader to conduct a survey on this issue.) Given a set $A$, recall that a sequence is an ordered $n$-tuple $(a_{1}, \dots  , a_{n}) \in A^{n}$ of elements from $A$, for some natural number $n$. The elements of a sequence need not be distinct and the order is important. For example, $(a_{1}, a_{2}, a_{1})$ and $(a_{2}, a_{1}, a_{1})$ are two distinct sequences in $A^{3}$. Their underlying set is ${a_{1}, a_{2}}$. What we just defined are finite sequences, which can also be viewed as functions from ${1, 2, \dots  , n}$ to the set $A$; the ith element of the sequence $(a_{1}, \dots  , a_{n})$ is the image of $i$ under the function. This viewpoint is fruitful, because it allows us to define (countably) infinite sequences as functions $s: \mathbb{N} \to A$. But then, why limit ourselves to ordered sets such as ${1, \dots  , n}$ or $\mathbb{N}$ as index sets? The main role of the index set is to tag each element uniquely, and the order of the tags is not crucial, although convenient. Thus, it is natural to define the notion of indexed family.

<!-- PAGE 73 -->
$$A_{I}$$
$$I\in I$$

> **Definition 3.2.** Given a set $A$, an I-indexed family of elements of $A$, for short a family, is a function a: I $\to A$ where I is any set viewed as an index set. Since the function a is determined by its graph
$${(i, a(i)) | i \in I},$$
the family a can be viewed as the set of pairs $a = {(i$, a(i)) | $i \in I}$. For notational simplicity, we write $a_{i}$ instead of a(i), and denote the family $a = {(i$, a(i)) | $i \in I}$ by $(a_{i})_{i\in I}$. For example, if $I = {r, g, b, y}$ and $A =\mathbb{N}$, the set of pairs
$$a = {(r, 2), (g, 3), (b, 2), (y, 11)}$$
is an indexed family. The element $2$ appears twice in the family with the two distinct tags $r$ and $b$. When the indexed set $I$ is totally ordered, a family $(a_{i})_{i\in I}$ is often called an I-sequence. Interestingly, sets can be viewed as special cases of families. Indeed, a set $A$ can be viewed as the A-indexed family ${(a$, a) | $a \in I}$ corresponding to the identity function.
Remark: An indexed family should not be confused with a multiset. Given any set $A$, a multiset is a similar to a set, except that elements of $A$ may occur more than once. For example, if $A = {a, b, c, d}$, then ${a$, a, a, $b, c, c, d, d}$ is a multiset. Each element appears with a certain multiplicity, but the order of the elements does not matter. For example, a has multiplicity $3$. Formally, a multiset is a function $s: A \to \mathbb{N}$, or equivalently a set of pairs ${(a, i)$ | $a \in A}$. Thus, a multiset is an A-indexed family of elements from $\mathbb{N}$, but not $a \mathbb{N}-indexed$ family, since distinct elements may have the same multiplicity (such as $c$ an $d$ in the example above). An indexed family is a generalization of a sequence, but a multiset is a generalization of a set. We also need to take care of an annoying technicality, which is to define sums of the
$$form \sum_{i}  \in I a_{i}, where I is any finite index set and (a_{i})_{i\in I} is a family of elements in some set$$
A equiped with a binary operation $+: A \times  A \to A$ which is associative (Axiom (G1)) and commutative. This will come up when we define linear combinations. The issue is that the binary operation $+$ only tells us how to compute $a_{1} + a_{2}$ for two elements of $A$, but it does not tell us what is the sum of three of more elements. For example, how should $a_{1} + a_{2} + a_{3}$ be defined? What we have to do is to define $a_{1}+a_{2}+a_{3}$ by using a sequence of steps each involving two elements, and there are two possible ways to do this: $a_{1} +(a_{2} +a_{3})$ and $(a_{1} +a_{2})+a_{3}$. If our operation $+$ is not associative, these are different values. If it associative, then $a_{1}+(a_{2}+a_{3}) = (a_{1} + a_{2}) + a_{3}$, but then there are still six possible permutations of the indices $1, 2, 3$, and if $+$ is not commutative, these values are generally different. If our operation is commutative, then all six permutations have the same value. Thus, if $+$ is associative and commutative,
$$it seems intuitively clear that a sum of the form \sum_{i}  \in I a_{i} does not depend on the order of the$$
operations used to compute it.

<!-- PAGE 74 -->
This is indeed the case, but a rigorous proof requires induction, and such a proof is surprisingly involved. Readers may accept without proof the fact that sums of the form
$$\sum_{i}  a_{i} are indeed well defined, and jump directly to Definition 3.3. For those who want to$$
$see^{\in I}$ the gory details, here we go.
$$First, we define sums \sum_{i}  a_{i}, where I is a finite sequence of distinct natural numbers,$$
say $I = (i_{1}, \dots  , i_{m})$. If $I = (^{\in I}i_{1}, \dots  , i_{m})$ with $m \ge 2$, we denote the sequence $(i_{2}, \dots  , i_{m})$ by I $-{i_{1}}$. We proceed by induction on the size $m$ of I. Let
$$\sum_{i\in I}  a_{i} = a_{i1},if m = 1,$$
$$\sum_{i\in I}  a_{i} = a_{i1} + \begin{pmatrix} a_{i} \\ i & } \end{pmatrix} \sum_{\in I-{i1}  ,if m > 1.$$
For example, if $I = (1, 2, 3, 4)$, we have
$$\sum_{i\in I}  a_{i} = a_{1} + (a_{2} + (a_{3} + a_{4})).$$
If the operation $+$ is not associative, the grouping of the terms matters. For instance, in general
$$a_{1} + (a_{2} + (a_{3} + a_{4})) \neq  (a + a_{2}) + (a_{3} + a_{4}).$$
$$However, if the operation + is associative, the sum \sum_{i}^{1}  \in I a_{i} should not depend on the grouping$$
of the elements in I, as long as their order is preserved. For example, if $I = (1, 2, 3, 4, 5), J_{1} = (1, 2)$, and $J_{2} = (3, 4, 5)$, we expect that
$$\sum_{i\in I}  a_{i} = \begin{pmatrix} a_{j} \end{pmatrix} \sum_{j\in J1}  + \begin{pmatrix} a_{j} \end{pmatrix} \sum_{j\in J2}  .$$
This indeed the case, as we have the following proposition.

> **Proposition 3.2.** Given any nonempty set $A$ equipped with an associative binary operation $+: A \times  A \to A$, for any nonempty finite sequence I of distinct natural numbers and for any partition of I into $p$ nonempty sequences $I_{k1}, \dots  , I_{kp}$, for some nonempty sequence $K = (k_{1}, \dots  , k_{p})$ of distinct natural numbers such that $k_{i} < k_{j}$ implies that $\alpha  < \beta$  for all $\alpha  \in I_{ki}$ and all $\beta  \in I_{kj}$, for every sequence $(a_{i})_{i\in I}$ of elements in $A$, we have
$$\sum_{\alpha\in I}  a_{\alpha} = \sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik}  .$$

*Proof.* We proceed by induction on the size $n$ of I. If $n = 1$, then we must have $p = 1$ and $I_{k1} =$ I, so the proposition holds trivially.

<!-- PAGE 75 -->
$$A_{I}$$
$$I\in I$$
Next, assume $n > 1$. If $p = 1$, then $I_{k1} =$ I and the formula is trivial, so assume that $p \ge 2$ and write $J = (k_{2}, \dots  , k_{p})$. There are two cases. Case $1$. The sequence $I_{k1}$ has a single element, say $\beta$ , which is the first element of I. In this case, write $C$ for the sequence obtained from I by deleting its first element $\beta$ . By definition,
$$\sum_{\alpha\in I}  a_{\alpha} = a_{\beta} + \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in C}  ,$$
$$and \sum_{\alpha\in Ik}  \sum_{j\in J}  \sum_{\alpha\in Ij}$$
$$\sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} = a_{\beta} + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Since |C| $= n$ - $1$, by the induction hypothesis, we have
$$\begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in C}  = \sum_{j\in J}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ij}  ,$$
which yields our identity. Case $2$. The sequence $I_{k1}$ has at least two elements. In this case, let $\beta$  be the first element of I (and thus of $I_{k1})$, let I' be the sequence obtained from I by deleting its first element $\beta$ , let $I_{k1}'$ be the sequence obtained from $I_{k1}$ by deleting its first element $\beta$ , and let $I_{ki}' = I_{ki}$ for $i = 2, \dots  , p$. Recall that $J = (k_{2}, \dots  , k_{p})$ and $K = (k_{1}, \dots  , k_{p})$. The sequence I' has $n$ - $1$ elements, so by the induction hypothesis applied to I' and the I' , we get
$$\sum_{\alpha\in I'}  a_{\alpha} = \sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik'}  = \begin{pmatrix} a_{\alpha} \\ \alpha \end{pmatrix} \sum_{\in Ik'1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}^{ki}  .$$
If we add the lefthand side to $a_{\beta}$, by definition we get
$$\sum_{\alpha\in I}  a_{\alpha}.$$
If we add the righthand side to $a_{\beta}$, using associativity and the definition of an indexed sum, we get
$$a_{\beta} + \begin{pmatrix}  \\ a_{\alpha} \\ \alpha \end{pmatrix} \begin{pmatrix}  &  \\ + & a_{\alpha} \end{pmatrix} \sum_{\in Ik'1}  \begin{pmatrix}\end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}  = \begin{pmatrix}  \\ a_{\beta} + & a_{\alpha} \\ \alpha \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in Ik'1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}$$
$$= \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\in Ik1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}$$
$$= \sum_{k\in K}^{\alpha}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik}  ,$$
as claimed.

<!-- PAGE 76 -->
$$If I = (1, \dots  , n), we also write \sum_{=1ii}  n a_{i} instead of \sum_{i}  a_{i}. Since + is associative, Propo-$$
$$sition 3.2 shows that the sum \sum_{1i}  n a^{=1} is independent of^{\in I} the grouping of its elements, which$$
justifies the use the notation $a  + \cdots  + a_{n}$ (without any parentheses). If we also assume that our associative binary operation on $A$ is commutative, then we
$$can show that the sum \sum_{i}  \in I a_{i} does not depend on the ordering of the index set I.$$

> **Proposition 3.3.** Given any nonempty set $A$ equipped with an associative and commutative binary operation $+: A \times  A \to A$, for any two nonempty finite sequences I and $J$ of distinct natural numbers such that $J$ is a permutation of I (in other words, the underlying sets of I and $J$ are identical), for every sequence $(a_{i})_{i\in I}$ of elements in $A$, we have
$$\sum_{\alpha\in I}  a_{\alpha} = \sum_{\alpha\in J}  a_{\alpha}.$$

*Proof.* We proceed by induction on the number $p$ of elements in I. If $p = 1$, we have $I = J$ and the proposition holds trivially. If $p > 1$, to simplify notation, assume that $I = (1, \dots  , p)$ and that $J$ is a permutation $(i_{1}, \dots  , i_{p})$ of I. First, assume that $2 \le i_{1} \le$ p-1, let J' be the sequence obtained from $J$ by deleting $i_{1}$, I' be the sequence obtained from I by deleting $i_{1}$, and let $P = (1, 2, \dots  , i_{1}-1)$ and $Q = (i_{1} +1, \dots$  , p-1, $p)$. Observe that the sequence I' is the concatenation of the sequences $P$ and $Q$. By the induction hypothesis applied to J' and I', and then by Proposition 3.2 applied to I' and its partition $(P, Q)$, we have
$$\sum_{\alpha\in J'}  a_{\alpha} = \sum_{\alpha\in I'}  a_{\alpha} = \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  .$$
If we add the lefthand side to $a_{i1}$, by definition we get
$$\sum_{\alpha\in J}  a_{\alpha}.$$
If we add the righthand side to $a_{i1}$, we get
$$a_{i1} + \begin{pmatrix}  \\ a_{i} \end{pmatrix} \begin{pmatrix}  \\ + & a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  \begin{pmatrix}\end{pmatrix} \sum_{i=i1+1}^{p}  .$$
Using associativity, we get
$$a_{i1} + \begin{pmatrix}  \\ a_{i} \end{pmatrix} \begin{pmatrix}  \\ + & a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  \begin{pmatrix}\end{pmatrix} \sum_{i=i1+1}^{p}  = \begin{pmatrix}  \\ a_{i1}+ & a_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  ,$$

<!-- PAGE 77 -->
$$A_{I}$$
$$I\in I$$
then using associativity and commutativity several times (more rigorously, using induction on $i_{1}$ - $1)$, we get
$$\begin{pmatrix}  \\ a_{i1}+ & a_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  = \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  + a_{i1} + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}$$
$$= \sum_{i=1}^{p}  a_{i},$$
as claimed. The cases where $i_{1} = 1$ or $i_{1} = p$ are treated similarly, but in a simpler manner since either $P =$ () or $Q =$ () (where () denotes the empty sequence).
$$Having done all this, we can now make sense of sums of the form \sum_{i}  a_{i}, for any finite$$
indexed set $I$ and any family $a = (a_{i})_{i\in I}$ of elements in $A$, where $A$ is $a^{\in I}$ set equipped with a binary operation $+$ which is associative and commutative. Indeed, since I is finite, it is in bijection with the set ${1, \dots  , n}$ for some $n \in \mathbb{N}$, and any total ordering ⪯ on I corresponds to a permutation $I_{⪯}$ of ${1, \dots  , n}$ (where we identify a
$$permutation with its image). For any total ordering ⪯on I, we define \sum_{i}  \in I,⪯a_{i} as$$
$$\sum_{i\in I,⪯}  a_{i} = \sum_{j\in I⪯}  a_{j}.$$
Then for any other total ordering ⪯' on I, we have
$$\sum_{i\in I,⪯'}  a_{i} = \sum_{j\in I⪯'}  a_{j},$$
and since $I_{⪯}$ and $I_{⪯'}$ are different permutations of ${1, \dots  , n}$, by Proposition 3.3, we have
$$\sum_{j\in I⪯}  a_{j} = \sum_{j\in I⪯'}  a_{j}.$$
$$Therefore, the sum \sum_{i}  \in a_{i} does not depend on the total ordering on I. We define the sum$$
$$\sum_{i}  \in I a_{i} as the common^{I,⪯} value \sum_{i}  \in I,⪯a_{i} for all total orderings ⪯of I.$$
Here are some examples with $A =\mathbb{R}$:
$$\sqrt\sqrt\sqrt$$
$$1. If I = {1, 2, 3}, a = {(1, 2), (2, -3), (3,\overline{2)}}, then \sum_{i}  \in I a_{i} = 2 -3 +\overline{2 =} -1 +\overline{2.}$$
$$\sqrt\sqrt\sqrt$$
$$2. If I = {2, 5, 7}, a = {(2, 2), (5, -3), (7,\overline{2)}}, then \sum_{i}  \in I a_{i} = 2 -3 +\overline{2 =} -1 +\overline{2.}$$
$$3. If I = {r, g, b}, a = {(r, 2), (g, -3), (b, 1)}, then \sum_{i}  \in I a_{i} = 2 -3 + 1 = 0.$$
