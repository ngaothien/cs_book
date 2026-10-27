# Polynomials


<!-- PAGE 1068 -->
$M$ such that M(i) $= k_{i}$ for every $i, 1 \le i \le n$, is denoted by $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, or more simply, by $(k_{1}, \dots  , k_{n})$, and $deg(k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n) = k_{1} + \cdots  + k_{n}$ is the size or degree of $M$. The set of all multisets over I is denoted by $\mathbb{N}^{(I)}$, and when $I = {1, \dots  , n}$, by $\mathbb{N}^{(n)}$. Intuitively, the order of the elements of a multiset is irrelevant, but the multiplicity of each element is relevant, contrary to sets. Every $i \in$ I is identified with the multiset $M_{i}$ such
$$\mathbb{N}^{(1)}$$
that $M_{i}(i) = 1$ and $M_{i}(j) = 0$ for $j \neq  i$. When $I = {1}$, the set of multisets $k \cdot  1$ can be identified with $\mathbb{N}$ and ${1}^{*}$. We will denote $k \cdot  1$ simply by $k$.
$$\mathbb{N}^{(n)}$$
 However, beware that when $n \ge 2$, the set of multisets cannot be identified with the set of strings in ${1, \dots  , n}^{*}$, because multiset union is commutative, but concatenation of strings in ${1, \dots  , n}^{*}$ is not commutative when $n \ge 2$. This is because in a multiset $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, the order is irrelevant, whereas in a string, the order is relevant. For example, $2 \cdot  1 + 3 \cdot  2 = 3 \cdot  2 + 2 \cdot  1$, but $11222 \neq  22211$, as strings over ${1, 2}$.
$$\mathbb{N}^{(n)}  \mathbb{N}^{n}$$
Nevertherless, and the set of ordered $n$-tuples under component-wise addition are isomorphic under the map
$$k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n \mapsto (k_{1}, \dots  , k_{n}).$$
Thus, since the notation $(k_{1}, \dots  , k_{n})$ is less cumbersome that $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, it will be preferred. We just have to remember that the order of the $k_{i}$ is really irrelevant.
$$\mathbb{N}^{(I)}  \mathbb{N}^{I}$$
 But when I is infinite, beware that and the set of ordered $I$-tuples are not isomorphic. We are now ready to define polynomials.

## 30.2 Polynomials

We begin with polynomials in one variable.

> **Definition 30.2.** Given a ring $A$, we define the set $\mathcal{P}_{A}(1)$ of polynomials over $A$ in one variable as the set of functions $P$ : $\mathbb{N} \to A$ such that P(k) $\neq  0$ for finitely many $k \in \mathbb{N}$. The polynomial such that P(k) $= 0$ for all $k \in \mathbb{N}$ is the null (or zero) polynomial and it is denoted by $0$. We define addition of polynomials, multiplication by a scalar, and multiplication of polynomials, as follows: Given any three polynomials $P, Q, R \in P_{A}(1)$, letting $a_{k} =$ P(k), $b_{k} =$ Q(k), and $c_{k} =$ R(k), for every $k \in \mathbb{N}$, we define $R = P + Q$ such that
$$c_{k} = a_{k} + b_{k},$$
$R = \lambda P$ such that
$$c_{k} = \lambda a_{k},$$
where $\lambda  \in A$,

<!-- PAGE 1069 -->
and $R = PQ$ such that
$$c_{k} = \sum_{i+j=k}  a_{i}b_{j}.$$
We define the polynomial $e_{k}$ such that $e_{k}(k) = 1$ and $e_{k}(i) = 0$ for $i \neq  k$. We also denote $e_{0}$ by $1$ when $k = 0$. Given a polynomial $P$, the $a_{k} =$ P(k) $\in A$ are called the coefficients of $P$. If $P$ is not the null polynomial, there is a greatest $n \ge 0$ such that $a_{n} \neq  0$ (and thus, $a_{k} = 0$ for all $k > n)$ called the degree of $P$ and denoted by deg(P). Then, $P$ is written uniquely as
$$P = a_{0}e_{0} + a_{1}e_{1} + \cdots  + a_{n}e_{n}.$$
When $P$ is the null polynomial, we let deg(P) $= -\infty$ . There is an injection of $A into\mathcal{P}_{A}(1)$ given by the map $a \mapsto$ a1 (recall that $1$ denotes $e_{0})$. There is also an injection of $\mathbb{N}$ into $\mathcal{P}_{A}(1)$ given by the map $k \mapsto e_{k}$. Observe that $e_{k} = e_{1}^{k}$ (with $e_{1}^{0} = e_{0} = 1)$. In order to alleviate the notation, we often denote $e_{1}$ by $X$, and we call $X$ a variable (or indeterminate). Then, $e_{k} = e_{1}^{k}$ is denoted by $X^{k}$. Adopting this notation, given a nonnull polynomial $P$ of degree $n$, if P(k) $= a_{k}, P$ is denoted by
$$P = a_{0} + a_{1}X + \cdots  + a_{n}X^{n},$$
or by
$$P = a_{n}X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{0},$$
if this is more convenient (the order of the terms does not matter anyway). Sometimes, it will also be convenient to write a polynomial as
$$P = a_{0}X^{n}+ a_{1}X^{n-1}+ \cdots  + a_{n}.$$
The set $\mathcal{P}_{A}(1)$ is also denoted by A[X] and a polynomial $P$ may be denoted by P(X). In denoting polynomials, we will use both upper-case and lower-case letters, usually, $P, Q, R, S, p, q, r, s$, but also $f, g, h$, etc., if needed (as long as no ambiguities arise). Given a nonnull polynomial $P$ of degree $n$, the nonnull coefficient $a_{n}$ is called the leading coefficient of $P$. The coefficient $a_{0}$ is called the constant term of $P$. A polynomial of the form $a_{k}X^{k}$ is called a monomial. We say that $a_{k}X^{k}$ occurs in $P$ if $a_{k}$ ̸ $= 0$. A nonzero polynomial $P$ of degree $n$ is called a monic polynomial (or unitary polynomial, or monic) if $a_{n} = 1$, where $a_{n}$ is its leading coefficient, and such a polynomial can be written as
$$P = X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{0}orP = X^{n}+ a_{1}X^{n-1}+ \cdots  + a_{n}.$$
 The choice of the variable $X$ to denote $e_{1}$ is standard practice, but there is nothing special about $X$. We could have chosen $Y , Z$, or any other symbol, as long as no ambiguities arise.

<!-- PAGE 1070 -->
Formally, the definition of $\mathcal{P}_{A}(1)$ has nothing to do with $X$. The reason for using $X$ is simply convenience. Indeed, it is more convenient to write a polynomial as $P = a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$ rather than as $P = a_{0}e_{0} + a_{1}e_{1} + \cdots  + a_{n}e_{n}$. We have the following simple but crucial proposition.

> **Proposition 30.1.** Given two nonnull polynomials P(X) $= a_{0}+a_{1}X +\cdots +a_{m}X^{m}$ of degree $m$ and Q(X) $= b_{0} + b_{1}X + \cdots  + b_{n}X^{n}$ of degree $n$, if either $a_{m}$ or $b_{n}$ is not a zero divisor, then $a_{m}b_{n} \neq  0$, and thus, PQ $\neq  0$ and
$$deg(PQ) = deg(P) + deg(Q).$$
In particular, if $A$ is an integral domain, then A[X] is an integral domain.

*Proof.* Since the coefficient of $X^{m+n}$ in PQ is $a_{m}b_{n}$, and since we assumed that either $a_{m}$ or $a_{n}$ is not a zero divisor, we have $a_{m}b_{n} \neq  0$, and thus, PQ $\neq  0$ and
$$deg(PQ) = deg(P) + deg(Q).$$
Then, it is obvious that A[X] is an integral domain. It is easily verified that A[X] is a commutative ring, with multiplicative identity $1X^{0} = 1$. It is also easily verified that A[X] satisfies all the conditions of Definition 3.1, but A[X] is not a vector space, since $A$ is not necessarily a field. A structure satisfying the axioms of Definition 3.1 when $K$ is a ring (and not necessarily a field) is called a module. Modules fail to have some of the nice properties that vector spaces have, and thus, they are harder to study. For example, there are modules that do not have a basis. We postpone the study of modules until Chapter $35$. However, when the ring $A$ is a field, A[X] is a vector space. But even when $A$ is just a ring, the family of polynomials $(X^{k})_{k\in N}$ is a basis of A[X], since every polynomial P(X) can be written in a unique way as P(X) $= a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$ (with P(X) $= 0$ when P(X) is the null polynomial). Thus, A[X] is a free module. Next, we want to define the notion of evaluating a polynomial P(X) at some $\alpha  \in A$. For this, we need a proposition.

> **Proposition 30.2.** Let $A, B$ be two rings and let $h: A \to B$ be a ring homomorphism. For any $\beta  \in B$, there is a unique ring homomorphism $\phi$ : A[X] $\to B$ extending $h$ such that $\phi (X) = \beta$ , as in the following diagram (where we denote by $h+\beta$  the map $h+\beta$  : $A\cup {X} \to B$ such that $(h + \beta )(a) =$ h(a) for all $a \in A$ and $(h + \beta )(X) = \beta$ ):
$$A \cup {X}\iota A[X]$$
$$LL$$
$$LL$$
$$LL$$
$$LL$$
$$h+\beta LL^{\phi}$$
$$%$$
$$B$$

<!-- PAGE 1071 -->

*Proof.* Let $\phi (0) = 0$, and for every nonull polynomial P(X) $= a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$, let
$$\phi (P(X)) = h(a_{0}) + h(a_{1})\beta  + \cdots  + h(a_{n})\beta^{n} .$$
It is easily verified that $\phi$  is the unique homomorphism $\phi$ : A[X] $\to B$ extending $h$ such that $\phi (X) = \beta$ . Taking $A = B$ in Proposition 30.2 and $h: A \to A$ the identity, for every $\beta  \in A$, there is a unique homomorphism $\phi_{\beta}$  : A[X] $\to A$ such that $\phi_{\beta} (X) = \beta$ , and for every polynomial P(X), we write $\phi_{\beta}$ (P(X)) as $P(\beta$ ) and we call $P(\beta$ ) the value of P(X) at $X = \beta$ . Thus, we can define a function $P_{A}$ : $A \to A$ such that $P_{A}(\beta$ ) $= P(\beta$ ), for all $\beta  \in A$. This function is called the polynomial function induced by $P$. More generally, $P_{B}$ can be defined for any (commutative) ring $B$ such that $A \subseteq B$. In general, it is possible that $P_{A} = Q_{A}$ for distinct polynomials $P, Q$. We will see shortly conditions for which the map $P \mapsto P_{A}$ is injective. In particular, this is true for $A = \mathbb{R}$ (in general, any infinite integral domain). We now define polynomials in $n$ variables.

> **Definition 30.3.** Given $n \ge 1$ and a ring $A$, the set $\mathcal{P}_{A}(n)$ of polynomials over $A$ in $n$
$$\mathbb{N}^{(n)}$$
variables is the set of functions $P$ : $\to A$ such that $P(k_{1}, \dots  , k_{n}) \neq  0$ for finitely many $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$. The polynomial such that $P(k_{1}, \dots  , k_{n}) = 0$ for all $(k_{1}, \dots  , k_{n})$ is the null (or zero) polynomial and it is denoted by $0$. We define addition of polynomials, multiplication by a scalar, and multiplication of polynomials, as follows: Given any three polynomials $P, Q, R \in P_{A}(n)$, letting $a_{(k1,...,kn)} = P(k_{1}, \dots  , k_{n}), b_{(k1,...,kn)} = Q(k_{1}, \dots  , k_{n}), c_{(k1,...,kn)} = R(k_{1}, \dots  , k_{n})$, for every $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, we define $R = P + Q$ such that
$$c_{(k1,...,kn)} = a_{(k1,...,kn)} + b_{(k1,...,kn)},$$
$R = \lambda P$, where $\lambda  \in A$, such that
$$c_{(k1,...,kn)} = \lambda a_{(k1,...,kn)},$$
and $R = PQ$, such that
$$c_{(k1,...,kn)} = \sum_{1,...,jn}  a_{(i1,...,in)}b_{(j1,...,jn)}.$$
$$(i1,...,in)+(j)=(k1,...,kn)$$
For every $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, we let $e_{(k1,...,kn)}$ be the polynomial such that
$$e_{(k1,...,kn)}(k_{1}, \dots  , k_{n}) = 1ande_{(k1,...,kn)}(h_{1}, \dots  , h_{n}) = 0,$$
for $(h_{1}, \dots  , h_{n})̸ = (k_{1}, \dots  , k_{n})$. We also denote $e_{(0,...,0)}$ by $1$. Given a polynomial $P$, the $a_{(k1,...,kn)} = P(k_{1}, \dots  , k_{n}) \in A$, are called the coefficients of $P$. If $P$ is not the null polynomial, there is a greatest $d \ge 0$ such that $a_{(k1,...,kn)} = 0$ for some $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, with $d =$
$$̸$$
$k_{1} + \cdots  + k_{n}$, called the total degree of $P$ and denoted by deg(P). Then, $P$ is written uniquely as
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}e_{(k1,...,kn)}.$$
$$(k\mathbb{N}(n)$$
$$1$$
When $P$ is the null polynomial, we let deg(P) $= -\infty$ .

<!-- PAGE 1072 -->
There is an injection of $A into\mathcal{P}_{A}(n)$ given by the map $a \mapsto$ a1 (where $1$ denotes $e_{(0,...,0)})$.
$$\mathbb{N}^{(n)}$$
There is also an injection of $into\mathcal{P}_{A}(n)$ given by the map $(h_{1}, \dots  , h_{n}) \mapsto e_{(h1,...,hn)}$. Note that $e_{(h1,...,hn)}e_{(k1,...,kn)} = e_{(h1+k1,...,hn+kn)}$. In order to alleviate the notation, let $X_{1}, \dots  , X_{n}$ be $n$ distinct variables and denote $e_{(0,...,0,1,0...,0)}$, where $1$ occurs in the position $i$, by $X_{i}$ (where $1 \le i \le n)$. With this convention, in view of $e_{(h1,...,hn)}e_{(k1,...,kn)} = e_{(h1+k1,...,hn+kn)}$, the polynomial $e_{(k1,...,kn)}$ is denoted by $X_{1}^{k1} \cdots  X_{n}^{kn}$ (with $e_{(0,...,0)} = X_{1}^{0} \cdots  X_{n}^{0} = 1)$ and it is called a primitive monomial. Then, $P$ is also written as
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} .$$
$$(k\mathbb{N}(n)$$
$$1$$
We also denote $\mathcal{P}_{A}(n)$ by $A[X_{1}, \dots  , X_{n}]$. A polynomial $P \in A[X_{1}, \dots  , X_{n}]$ is also denoted by $P(X_{1}, \dots  , X_{n})$. As in the case $n = 1$, there is nothing special about the choice of $X_{1}, \dots  , X_{n}$ as variables (or indeterminates). It is just a convenience. After all, the construction $of\mathcal{P}_{A}(n)$ has nothing to do with $X_{1}, \dots  , X_{n}$. Given a nonnull polynomial $P$ of degree $d$, the nonnull coefficients $a_{(k1,...,kn)}$ ̸ $= 0$ such that $d = k_{1} + \cdots  + k_{n}$ are called the leading coefficients of $P$. A polynomial of the form $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ is called a monomial. Note that $deg(a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ ) $= k_{1}+\cdots +k_{n}$. Given a polynomial
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} ,$$
$$(k\mathbb{N}(n)$$
$$1$$
a monomial $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ occurs in the polynomial $P$ if $a_{(k1,...,kn)} \neq  0$. A polynomial
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$$
$$(k\mathbb{N}(n)$$
$$1$$
is homogeneous of degree $d$ if
$$deg(X_{1}^{k1} \cdots  X_{n}^{kn} ) = d,$$
for every monomial $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ occurring in $P$. If $P$ is a polynomial of total degree $d$, it is clear that $P$ can be written uniquely as
$$P = P^{(0)}+ P^{(1)}+ \cdots  + P^{(d)},$$
where $P^{(i)}$ is the sum of all monomials of degree $i$ occurring in $P$, where $0 \le i \le d$. It is easily verified that $A[X_{1}, \dots  , X_{n}]$ is a commutative ring, with multiplicative identity $1X_{1}^{0} \cdots  X_{n}^{0} = 1$. It is also easily verified that A[X] is a module. When $A$ is a field, A[X] is a vector space. Even when $A$ is just a ring, the family of polynomials
$$(X_{1}^{k1} \cdots  X_{n}^{kn} )_{(k1,...,kn)\in N(n)}$$

<!-- PAGE 1073 -->
is a basis of $A[X_{1}, \dots  , X_{n}]$, since every polynomial $P(X_{1}, \dots  , X_{n})$ can be written in a unique way as
$$P(X_{1}, \dots  , X_{n}) = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} .$$
$$(k\mathbb{N}(n)$$
$$1$$
Thus, $A[X_{1}, \dots  , X_{n}]$ is a free module.
Remark: The construction of Definition 30.3 can be immediately extended to an arbitrary set $I$, and not just $I = {1, \dots  , n}$. It can also be applied to monoids more general $that\mathbb{N}^{(I)}$. Proposition 30.2 is generalized as follows.

> **Proposition 30.3.** Let $A, B$ be two rings and let $h: A \to B$ be a ring homomorphism. For any $\beta  = (\beta_{1} , \dots  , \beta_{n}$ ) $\in B^{n}$, there is a unique ring homomorphism $\phi$ : $A[X_{1}, \dots  , X_{n}] \to B$ extending $h$ such that $\phi (X_{i}) = \beta_{i} , 1 \le i \le n$, as in the following diagram (where we denote by $h + \beta$  the map $h + \beta$  : $A \cup {X_{1}, \dots  , X_{n}} \to B$ such that $(h + \beta )(a) =$ h(a) for all $a \in A$ and $(h + \beta )(X_{i}) = \beta_{i} , 1 \le i \le n)$:
$$A \cup {X_{1}, \dots  , X_{n}}\iota A[X_{1}, \dots  , X_{n}]$$
$$TTT$$
$$TTT$$
$$TTT$$
$$TT\phi$$
$$TTT$$
$$h+\beta TTT$$
$$)$$
$$B$$

*Proof.* Let $\phi (0) = 0$, and for every nonull polynomial
$$P(X_{1}, \dots  , X_{n}) = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} ,$$
$$(k\mathbb{N}(n)$$
$$1$$
let
$$\phi (P(X_{1}, \dots  , X_{n})) = \sum  h(a_{(k1,...,kn)})\beta_{1}^{k1}  \cdots  \beta_{n}^{kn}  .$$
It is easily verified that $\phi$  is the unique homomorphism $\phi$ : $A[X_{1}, \dots  , X_{n}] \to B$ extending $h$ such that $\phi (X_{i}) = \beta_{i}$ . Taking $A = B$ in Proposition 30.3 and $h: A \to A$ the identity, for every $\beta_{1} , \dots  , \beta_{n}  \in A$, there is a unique homomorphism $\phi$ : $A[X_{1}, \dots  , X_{n}] \to A$ such that $\phi (X_{i}) = \beta_{i}$ , and for every polynomial $P(X_{1}, \dots  , X_{n})$, we write $\phi (P(X_{1}, \dots  , X_{n}))$ as $P(\beta_{1} , \dots  , \beta_{n}$ ) and we call $P(\beta_{1} , \dots  , \beta_{n}$ ) the value of $P(X_{1}, \dots  , X_{n})$ at $X_{1} = \beta_{1} , \dots  , X_{n} = \beta_{n}$ . Thus, we can define a function $P_{A}$ : $A^{n} \to A$ such that $P_{A}(\beta_{1} , \dots  , \beta_{n}$ ) $= P(\beta_{1} , \dots  , \beta_{n}$ ), for all $\beta_{1} , \dots  , \beta_{n}  \in A$. This function is called the polynomial function induced by $P$. More generally, $P_{B}$ can be defined for any (commutative) ring $B$ such that $A \subseteq B$. As in the case of a single variable, it is possible that $P_{A} = Q_{A}$ for distinct polynomials $P, Q$. We will see shortly that the map $P \mapsto P_{A}$ is injective when $A = \mathbb{R}$ (in general, any infinite integral domain).
