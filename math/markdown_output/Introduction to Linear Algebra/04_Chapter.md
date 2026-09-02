# **Chapter 4**

# **Orthogonality**

# **4.1 Orthogonality of the Four Subspaces**

**<sup>1</sup>**Orthogonal vectors have v <sup>T</sup>w = 0. Then llvll<sup>2</sup>+ llwll<sup>2</sup>= llv + wll<sup>2</sup>= llv - wll<sup>2</sup> . 2 Subspaces V and W are orthogonal when v <sup>T</sup>w <sup>=</sup> 0 for every v in V and every win W. **<sup>3</sup>**The row space of *A* is orthogonal to the nullspace. The column space is orthogonal to N(A T ). 4 One pair of dimensions adds to *r* + ( *n* - r) = *n.* The other pair has *r* + ( *m* - r) = *m.* S Row space and nullspace are orthogonal *complements:* Every *x* in R <sup>n</sup>splits into Xrow + Xnull· 6 Suppose a space *S* has dimension *d.* Then every basis for *S* consists of *d* vectors. 7 If d vectors in Sare independent, they span *S.* If d vectors span *S,* they are independent.

Two vectors are orthogonal when their dot product is zero: *v* · *w* = *v* T *w* = 0. This chapter moves to **orthogonal subspaces** and **orthogonal bases** and **orthogonal matrices.** The vectors in two subspaces, and the vectors in a basis, and the column vectors in Q, all pairs will be orthogonal. Think of a <sup>2</sup>+ b <sup>2</sup>= c2 for a *right triangle* with sides *v* and *w.*

**Orthogonal vectors** and llvll

<sup>2</sup>+ llwll<sup>2</sup>= llv + wll<sup>2</sup>

The right side is ( v + w) T ( v + w). This equals v T v + w T w when v T w = w T v = 0.

Subspaces entered Chapter 3 to throw light on *Ax* = *b.* Right away we needed the column space and the nulls pace. Then the light turned onto *<sup>A</sup> <sup>T</sup> ,* uncovering two more subspaces. Those four fundamental subspaces reveal what a matrix really does.

A matrix multiplies a vector: *A times x.* At the first level this is only numbers. At the second level *Ax* is a combination of column vectors. The third level shows subspaces. But I don't think you have seen the whole picture until you study Figure 4.2.

The subspaces fit together to show the hidden reality of *A* times *x.* The 90° angles between subspaces are new-and we can say now what those right angles mean.

*The row space is perpendicular to the nullspace.* Every row of *A* is perpendicular to every solution of *Ax* = 0. That gives the 90° angle on the left side of the figure. This perpendicularity of subspaces is Part 2 of the Fundamental Theorem of Linear Algebra.

*The column space is perpendicular to the nullspace of AT.* When *b* is outside the column space-when we want to solve *Ax* = band can't do it-then this nullspace of *A <sup>T</sup>*comes into its own. It contains the error *e* = *b* - *Ax* in the "least-squares" solution. Least squares is the key application of linear algebra in this chapter.

Part 1 of the Fundamental Theorem gave the dimensions of the subspaces. The row and column spaces have the same dimension *r* (they are drawn the same size). The two nullspaces have the remaining dimensions *n* - *r* and *m* - *r.* Now we will show that *the row space and nullspace are orthogonal subspaces inside Rn.*

**DEFINITION** Two subspaces *V* and *W* of a vector space are *orthogonal* if every vector v in V is perpendicular to every vector *w* in W:

**Orthogonal subspaces**                      
$$v^T w = 0$$
                      *for all  $v$  in  $V$  and all  $w$  in  $W$ .*

**Example 1** The floor of your room (extended to infinity) is a subspace *V.* The line where two walls meet is a subspace *W* (one-dimensional). Those subspaces are orthogonal. Every vector up the meeting line of the walls is perpendicular to every vector in the floor.

**Example 2** Two walls look perpendicular but those two subspaces are not orthogonal! The meeting line is in both V and W -and this line is not perpendicular to itself. Two planes (dimensions 2 and 2 in R<sup>3</sup> ) cannot be orthogonal subspaces.

When a vector is in two orthogonal subspaces, it *must* be zero. It is perpendicular to itself. It is *v* and it is *w,* so *v T v* = 0. This has to be the zero vector.

*V* <sup>I</sup>

I

*w* 

orthogonal plane *V* and line *W* 

*V* 

non-orthogonal planes

Figure 4.1: Orthogonality is impossible when dim *V* +dim *W* >dim (whole space).

The crucial examples for linear algebra come from the four fundamental subspaces. Zero is the only point where the nullspace meets the row space. More than that, the **nullspace and row space of** *A* **meet at 90° .** This key fact comes directly from *Ax* = **0:** 

Every vector *x* in the nullspace is perpendicular to every row of *A,* because *Ax* = **0.**  *The nullspace N(A) and the row space* C(A<sup>T</sup> ) *are orthogonal subspaces of R<sup>n</sup> .* 

To see why xis perpendicular to the rows, look at *Ax* = **0.** Each row multiplies x:

$$Ax = \begin{bmatrix} \text{row 1} \\ \vdots \\ \text{row } m \end{bmatrix} \begin{bmatrix} x \end{bmatrix} = \begin{bmatrix} 0 \\ \vdots \\ 0 \end{bmatrix} \quad (1)$$
←  $(\text{row 1}) \cdot x$  is zero  
←  $(\text{row } m) \cdot x$  is zero

The first equation says that row 1 is perpendicular to *x.* The last equation says that row mis perpendicular to *x. Every row has a zero dot product with x.* Then xis also perpendicular to every *combination* of the rows. The whole row space C(A<sup>T</sup> ) is orthogonal to *N(A).* 

Here is a second proof of that orthogonality for readers who like matrix shorthand. The vectors in the row space are combinations A<sup>T</sup>*y* of the rows. Take the dot product of A<sup>T</sup>*y* with any *x* in the nullspace. *These vectors are perpendicular:* 

Of 
$$A^T y$$
 with any  $x$  in the nullspace. *These vectors are perpendicular:*

| Nullspace orthogonal to row space | $x^T(A^T y) = (Ax)^T y = 0^T y = 0$ . | (2) |
|-----------------------------------|---------------------------------------|-----|
|-----------------------------------|---------------------------------------|-----|

We like the first proof. You can see those rows of *A* multiplying x to produce zeros in equation (1). The second proof shows why *A* and A<sup>T</sup>are both in the Fundamental Theorem.

**Example 3** The rows of *A* are perpendicular to x = ( 1, 1, -1) in the nullspace :

| $Ax = \begin{bmatrix} 1 & 3 & 4 \\ 5 & 2 & 7 \\ -1 & -1 & -1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$ | gives the dot products | $1 + 3 - 4 = 0$ $5 + 2 - 7 = 0$ |
|-------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------|
|-------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------|

Now we tum to the other two subspaces. In this example, the column space is all of R <sup>2</sup> . The nullspace of A<sup>T</sup>is only the zero vector (orthogonal to every vector). The column space of *A* and the nullspace of A<sup>T</sup>are always orthogonal subspaces.

Every vector *y* in the nullspace of A<sup>T</sup>is perpendicular to every column of *A. The left nullspace* N(A<sup>T</sup> ) *and the column space C(A) are orthogonal in* R<sup>m</sup> .

*Apply the original proof to* A<sup>T</sup>. The nullspace of A<sup>T</sup>is orthogonal to the row space of A<sup>T</sup>-and the row space of A<sup>T</sup>is the column space of *A.* Q .E.D.

For a visual proof, look at A<sup>T</sup>*y* = 0. Each column of *A* multiplies *y* to give 0:

$$C(A) \perp N(A^T) \quad A^T \mathbf{y} = \begin{bmatrix} (\text{column } 1)^T \\ \vdots \\ (\text{column } n)^T \end{bmatrix} \begin{bmatrix} \mathbf{y} \end{bmatrix} = \begin{bmatrix} 0 \\ \vdots \\ 0 \end{bmatrix}. \quad (3)$$

The dot product of *y* with every column of *A* is zero. Then *y* in the left nullspace is perpendicular to each column of A-and to the whole column space.

![](images/_page_206_Diagram_2.jpeg)

Figure 4.2: Two pairs of orthogonal subspaces. The dimensions add to *n* and add to *m.* **This is the Big Picture-two** subspaces in *R<sup>n</sup>*and two subspaces in Rm.

# **Orthogonal Complements**

*Important* The fundamental subspaces are more than just orthogonal (in pairs). Their dimensions are also right. Two lines could be perpendicular in **R**<sup>3</sup> , **but those lines** *could not be* **the row space and nullspace of a 3 by 3 matrix.** The lines have dimensions 1 and 1, adding to 2. But the correct dimensions rand *n* - *r* must add *ton=* 3.

The fundamental subspaces of a 3 by 3 matrix have dimensions 2 and 1, or 3 and 0. Those pairs of subspaces are not only orthogonal, they are *orthogonal complements.*

**DEFINITION** The *orthogonal complement* of a subspace *V* contains *every* vector that is perpendicular to V. This orthogonal subspace is denoted by VJ.. (pronounced "V perp").

By this definition, the nullspace is the orthogonal complement of the row space. *Every x* that is perpendicular to the rows satisfies *Ax* = 0, and lies in the nullspace.

The reverse is also true. *If v is orthogonal to the nullspace, it must be in the row space.* Otherwise we could add this *v* as an extra row of the matrix, without changing its nullspace. The row space would grow, which breaks the law *r* + ( *n* - *r)* = *n.* We conclude that the nullspace complement N(A)J.. is exactly the row space C(AT).

In the same way, the left nullspace and column space are orthogonal in Rm, and they are orthogonal complements. Their dimensions *r* and *m* - *r* add to the full dimension *m.*

## *Fundamental Theorem of Linear Algebra,* **Part 2**

*N(A) is the orthogonal complement of the row space C(A<sup>T</sup>)* **(in** *R ). N(A<sup>T</sup> ) is the orthogonal complement of the column space C(A)* **(in** *R <sup>m</sup>).* 

Part 1 gave the dimensions of the subspaces. Part 2 gives the 90° angles between them. The point of "complements" is that every *x* can be split into a *row space component Xr*  and a *nullspace component Xn.* When *A* multiplies *x* = *Xr* + *Xn,* Figure 4.3 shows what happens to *Ax= Axr*<sup>+</sup>*Ax<sup>n</sup> :* 

The nullspace component goes to zero: *Axn* = 0.

The row space component goes to the column space: *Axr* = *Ax.* 

Every vector goes to the column space! Multiplying by *A* cannot do anything else. More than that: *Every vector b in the column space comes from one and only one vector Xr in the row space.* Proof: If *Axr* = *Ax�,* the difference *Xr* - *x�* is in the nullspace. It is also in the row space, where *Xr* and *x�* came from. This difference must be the zero vector, because the nullspace and row space are perpendicular. Therefore *Xr* = *x�.* 

There is an *r* by *r* invertible matrix hiding inside *A,* if we throw away the two nullspaces. *From the row space to the column space, A is invertible.* The "pseudo inverse" will invert that part of *A* in Section 7.4.

**Example 4** Every matrix of rank *r* has an *r* by *r* invertible submatrix:

| $A = \begin{bmatrix} 3 & 0 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ | contains the submatrix | $\begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------|
|-------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------|

The other eleven zeros are responsible for the nullspaces. The rank of *B* is also *r* = 2:

| $B = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 2 & 4 & 5 & 6 \\ 1 & 2 & 4 & 5 & 6 \\ 1 & 2 & 4 & 5 & 6 \end{bmatrix}$ | contains $\begin{bmatrix} 1 & 3 \\ 1 & 4 \end{bmatrix}$ | in the pivot rows and columns. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|--------------------------------|
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|--------------------------------|

Every matrix can be diagonalized, when we choose the right bases for *R<sup>n</sup>*and Rm. This *Singular Value Decomposition* has become extremely important in applications.

Let me repeat one clear fact. A row of *A* can't be in the nullspace of *A* (except for a zero row). The only vector in two orthogonal subspaces is the zero vector.

If **a vector** *v* **is orthogonal to itself then** *v* **is the zero vector.**

![](images/_page_208_Diagram_2.jpeg)

Figure 4.3: This update of Figure 4.2 shows the true action of *A* on x Row space vector *Xr* to column space, nullspace vector *Xn* to zero. *Xr* + *Xn-*

# **Drawing the Big Picture**

I don't know the best way to draw the four subspaces in Figures 4.2 and 4.3. This big picture has to show the orthogonality of those subspaces. I can see a possible way to do it when a line meets a plane-maybe Figure 4.4 also shows that those spaces are infinite, more clearly than the rectangles in Figure 4.3. But how do I draw a pair of two-dimensional subspaces in R **4,** to show they are orthogonal to each other? Good ideas are welcome.

![](images/_page_208_Diagram_6.jpeg)

Figure 4.4: Row space of *A* = plane. Nullspace = orthogonal line. Dimensions 2 + 1 = 3.

### **Combining Bases from Subspaces**

What follows are some valuable facts about bases. They were saved until now-when we are ready to use them. After a week you have a clearer sense of what a basis is *(linearly independent* vectors that *span the space).* Normally we have to check both properties. When the count is right, one property implies the other :

Any n independent vectors in *Rn* must span *R<sup>n</sup> .* So they are a basis. Any *n* vectors that span *Rn* must be independent. So they are a basis.

Starting with the correct number of vectors, one property of a basis produces the other. This is true in any vector space, but we care most about *R<sup>n</sup> .* When the vectors go into the columns of an *n* by *n square* matrix *A,* here are the same two facts:

If the n columns of A are independent, they span *R<sup>n</sup> .* So Ax = *<sup>b</sup>*is solvable. If the *n* columns span R , they are independent. So Ax = *<sup>b</sup>*has only one solution.

Uniqueness implies existence and existence implies uniqueness. *Then A is invertible.* If there are no free variables, the solution x is unique. There must be n pivot columns. Then back substitution solves Ax = *b* (the solution exists).

Starting in the opposite direction, suppose that Ax = *b* can be solved for every *<sup>b</sup> (existence of solutions).* Then elimination produced no zero rows. There are *n* pivots and no free variables. The nullspace contains only *x* = 0 *(uniqueness* of solutions).

With bases for the row space and the nulls pace, we have *r* + ( *n* - *r)* = *<sup>n</sup>*vectors. This is the right number. Those n vectors are independent. 2 *Therefore they span Rn.*

Each xis the sum Xr + <sup>X</sup>n of a row space vector Xr and a nullspace vector X<sup>n</sup> ,

The splitting in Figure 4.3 shows the key point of orthogonal complements-the dimensions add to n and all vectors are fully accounted for.

**Example 5** For 
$$A = \begin{bmatrix} 2 & 2 \\ 3 & 6 \end{bmatrix}$$
 split  $x = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$  into  $x_r + x_n = \begin{bmatrix} 2 \\ 4 \end{bmatrix} + \begin{bmatrix} 2 \\ -1 \end{bmatrix}$ .

The vector (2, 4) is in the row space. The orthogonal vector (2, -1) is in the nullspace. The next section will compute this splitting for any *A* and x, by a projection.

If a combination of all n vectors gives xr + xn = 0, then xr = -xn is in both subspaces. So Xr = xn = 0. All coefficients of the row space basis and of the nullspace basis must be zero. This proves independence of the n vectors together.

#### **• REVIEW OF THE KEY IDEAS •**

- 1. Subspaces *V* and Ware orthogonal if every *v* in Vis orthogonal to every *win W.*
- **2.** *V* and *W* are "orthogonal complements" if *W* contains **all** vectors perpendicular to *V* (and vice versa). Inside *R<sup>n</sup> ,* the dimensions of complements *V* and *W* add *ton.*
- **3.** The nullspace *N(A)* and the row space *C(A<sup>T</sup> )* are orthogonal complements, with dimensions *(n* - *r)* + *r* = *n.* Similarly *N(A<sup>T</sup> )* and *C(A)* are orthogonal complements with (m - *r)* + *r* = *m.*
- **4.** Any *n* independent vectors in R <sup>n</sup>span **<sup>R</sup> <sup>n</sup> .** Any *n* spanning vectors are independent.

#### **• WORKED EXAMPLES •**

**4.1 A** Suppose *S* is a six-dimensional subspace of nine-dimensional space **R** <sup>9</sup> .

- (a) What are the possible dimensions of subspaces orthogonal to S?
- (b) What are the possible dimensions of the orthogonal complement S J\_ of S? ( c) What is the smallest possible size of a matrix A that has row space S?
- (d) What is the smallest possible size of a matrix B that has nullspace S J\_ ?

#### **Solution**

- (a) If Sis six-dimensional in R<sup>9</sup> , subspaces orthogonal to Scan have dimensions 0, 1, 2, 3.
- (b) The complement S J\_ is the largest orthogonal subspace, with dimension 3.
- (c) The smallest matrix *A* is 6 by 9 (its six rows will be a basis for S).
- (d) This is the same as question (c) !

If a new row 7 of *B* is a combination of the six rows of *A,* then *B* has the same row space as *A.* It also has the same nullspace. The special solutions s 1, s2, s3to *Ax* = 0. will be the same for *Bx* = 0. Elimination will change row 7 of *B* to all zeros.

- **4.1 B** The equation *x 3y 4z* = 0 describes a plane Pin **R<sup>3</sup>**(actually a subspace).
  - (a) The plane Pis the nullspace *N(A)* of what 1 by 3 matrix *A? Ans: A=* [1 -3 -4].
  - (b) Find a basis s 1, s2of special solutions of *x 3y 4z* = 0 (these would be the columns of the nullspace matrix N). *Answer:* s1<sup>=</sup>(3, 1, 0) and s2<sup>=</sup>(4, 0, 1).
  - (c) Find a basis for the line PJ\_ that is perpendicular to *P. Answer:* (1, -3, -4)!

# **Problem Set 4.1**

**Questions 1-12 grow out of Figures 4.2 and 4.3 with four subspaces.** 

- 1 Construct any 2 by 3 matrix of rank one. Copy Figure 4.2 and put one vector in each subspace (and put two in the nullspace). Which vectors are orthogonal? 2 Redraw Figure 4.3 for a 3 by 2 matrix of rank *r* = 2. Which subspace is *<sup>Z</sup>* (zero vector only)? The nullspace part of any vector *x* in R**2** is *Xn* = \_\_ . **<sup>3</sup>**Construct a matrix with the required property or say why that is impossible:
  - (a) Column space contains [ \_ !] and [-!], nullspace contains [ ½]
  - (b) Row space contains [ \_ !] and [-!] , nullspace contains [ ½] ( c) *Ax* = [½ ] has a solution and *A<sup>T</sup>*[ g] = [g]
- (d) Every row is orthogonal to every column *(A* is not the zero matrix) ( e) Columns add up to a column of zeros, rows add to a row of 1 's. 4 If *AB* = 0 then the columns of *B* are in the of *A.* The rows of *A* are in the \_\_ of *B.* With *AB=* 0, why can't *A* and *B* be 3 by 3 matrices of rank 2? **<sup>5</sup>**(a) IfAx=bhas asolution andATy=O,is(yTx=O)or(yTb=O)?
- (b) If *A<sup>T</sup> y=* (1, 1, 1) has a solution and *Ax=* **0,** then \_\_ . **<sup>6</sup>**This system of equations *Ax* = *b* has *no solution* (they lead to O = 1):

| $x + 2y + 2z$  | $=$ | 5 |
|----------------|-----|---|
| $2x + 2y + 3z$ | $=$ | 5 |
| $3x + 4y + 5z$ | $=$ | 9 |

Find numbers YI, Y2, y3 to multiply the equations so they add to O = 1. You have found a vector yin which subspace? Its dot product *y<sup>T</sup> <sup>b</sup>*is 1, so no solution *x.* 

**<sup>7</sup>**Every system with no solution is like the one in Problem 6. There are numbers YI, ... , Ym that multiply the m equations so they add up to O = 1. This is called **Fredholm's Alternative:** 

**Exactly one of these problems has a solution** 

| $Ax = b$ | OR | $A^T y = 0$ | with | $y^T b = 1$ . |
|----------|----|-------------|------|---------------|
|          |    |             |      |               |

If *b* is not in the column space of *A,* it is not orthogonal to the nullspace of *A<sup>T</sup> .*  Multiply the equations *XI* - x2 = 1 and x2 - *<sup>x</sup>3*= 1 and *XI* - *<sup>x</sup>3*= 1 by numbers YI, Yz, y3 chosen so that the equations add up to O = 1.

8 In Figure 4.3, how do we know that  $Ax_r$  is equal to  $Ax$ ? How do we know that this vector is in the column space? If  $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$  and  $x = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$  what is  $x_r$ ?

9 If  $A^T Ax = 0$  then  $Ax = 0$ . Reason:  $Ax$  is in the nullspace of  $A^T$  and also in the \_\_\_\_\_ of  $A$  and those spaces are \_\_\_\_\_. Conclusion:  $A^T A$  has the same nullspace as  $A$ . This key fact is repeated in the next section.

10 Suppose  $A$  is a symmetric matrix ( $A^T = A$ ).

1. Why is its column space perpendicular to its nullspace?
2. If  $Ax = 0$  and  $Az = 5z$ , which subspaces contain these “eigenvectors”  $x$  and  $z$ ? **Symmetric matrices have perpendicular eigenvectors**  $x^T z = 0$ .

11 (Recommended) Draw Figure 4.2 to show each subspace correctly for

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} 1 & 0 \\ 3 & 0 \end{bmatrix}.$$

12 Find the pieces  $x_r$  and  $x_n$  and draw Figure 4.3 properly if

$$A = \begin{bmatrix} 1 & -1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \quad \text{and} \quad x = \begin{bmatrix} 2 \\ 0 \end{bmatrix}.$$

**Questions 13–23 are about orthogonal subspaces.**

13 Put bases for the subspaces  $V$  and  $W$  into the columns of matrices  $V$  and  $W$ . Explain why the test for orthogonal subspaces can be written  $V^T W = 0$  zero matrix. This matches  $v^T w = 0$  for orthogonal vectors.

14 The floor  $V$  and the wall  $W$  are not orthogonal subspaces, because they share a nonzero vector (along the line where they meet). No planes  $V$  and  $W$  in  $\mathbb{R}^3$  can be orthogonal! Find a vector in the column spaces of both matrices:

$$A = \begin{bmatrix} 1 & 2 \\ 1 & 3 \\ 1 & 2 \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} 5 & 4 \\ 6 & 3 \\ 5 & 1 \end{bmatrix}$$

This will be a vector  $Ax$  and also  $B\hat{x}$ . Think 3 by 4 with the matrix  $[A \ B]$ .

15 Extend Problem 14 to a  $p$ -dimensional subspace  $V$  and a  $q$ -dimensional subspace  $W$  of  $\mathbb{R}^n$ . What inequality on  $p + q$  guarantees that  $V$  intersects  $W$  in a nonzero vector? These subspaces cannot be orthogonal.

16 Prove that every  $y$  in  $N(A^T)$  is perpendicular to every  $Ax$  in the column space, using the matrix shorthand of equation (2). Start from  $A^T y = 0$ .

11 If S is the subspace of R3 containing only the zero vector, what is S1\_ ? If S is spanned by (1, 1, 1), what is S1\_ ? If Sis spanned by (1, 1, 1) and (1, 1, -1), what is a basis for S1\_ ? 18 Suppose Sonly contains two vectors (1, 5, 1) and (2, 2, 2) (not a subspace). Then S1 is the nullspace of the matrix A = \_\_ . S1\_ is a subspace even if S is not. 19 Suppose Lis a one-dimensional subspace (a line) in R . Its orthogonal complement L 1\_ is the \_\_ perpendicular to L. Then (L1\_ ) 1\_ is a \_\_ perpendicular to L 1- \_ In fact ( L 1-) 1- is the same as \_\_ . 20 Suppose *V* is the whole space R <sup>4</sup> . Then *V*1 contains only the vector \_\_ . Then (V1\_ )1\_ is \_\_ . So (V1- ) 1\_ is the same as \_\_ . 21 Suppose Sis spanned by the vectors (1, 2, 2, 3) and (1, 3, 3, 2). Find two vectors that span S1\_ . This is the same as solving Ax **=** 0 for which A? 22 If P is the plane of vectors in R 4 satisfying x1 <sup>+</sup>x2 <sup>+</sup>x3 <sup>+</sup>x*4*<sup>=</sup>0, write a basis for p .l. Construct a matrix that has P as its nullspace. 23 If a subspace Sis contained in a subspace V, prove that S.l contains V.l .

## Questions 24-30 are about perpendicular columns and rows.

- 24 Suppose an n by n matrix is invertible: AA-*<sup>1</sup>*=I. Then the first column of A-1 is orthogonal to the space spanned by which rows of A? 25 Find A <sup>T</sup>A if the columns of A are unit vectors, all mutually perpendicular. 26 Construct a 3 by 3 matrix *A* with no zero entries whose columns are mutually perpendicular. Compute A <sup>T</sup>A. Why is it a diagonal matrix? 27 The lines 3x <sup>+</sup>*y* <sup>=</sup>b1 and 6x + 2y = b2 are \_\_ . They are the same line if \_\_ . In that case ( b1, b2) is perpendicular to the vector \_\_ . The nullspace of the matrix is the line 3x <sup>+</sup>*y* = \_\_ . One particular vector in that nullspace is \_\_ . 28 Why is each of these statements false?
  - (a) (1, 1, 1) is perpendicular to (1, 1, -2) so the planes x <sup>+</sup>*y* <sup>+</sup>z = 0 and x <sup>+</sup>*y* 2z **=** 0 are orthogonal subspaces.
  - (b) The subspace spanned by (1, 1, 0, 0, 0) and (0, 0, 0, 1, 1) is the orthogonal complement of the subspace spanned by (1, -1, 0, 0, 0) and (2, -2, 3, 4, -4).
- (c) Two subspaces that meet only in the zero vector are orthogonal. 29 Find a matrix with v **=** (l, 2, 3) in the row space and column space. Find another matrix with v in the nullspace and column space. Which pairs of subspaces can v notbe in?

# **Challenge Problems**

- 30 Suppose *A* is 3 by 4 and *B* is 4 by 5 and *AB* = 0. So *N(A)* contains *C(B).*  Prove from the dimensions of *N(A)* and *C(B)* that rank(A) + rank(B) S:: 4. 31 The command *N* = null(A) will produce a basis for the nullspace of *A.* Then the command *B* = null(N') will produce a basis for the \_\_ of *A.*  32 Suppose I give you four nonzero vectors *r, n, c, l* in R .
  - (a) What are the conditions for those to be bases for the four fundamental subspaces *C(A<sup>T</sup>), N(A), C(A), N(A<sup>T</sup>)* of a 2 by 2 matrix?
  - (b) What is one possible matrix *A?*
  - (a) What are the conditions for those pairs to be bases for the four fundamental subspaces of a 4 by 4 matrix?
  - (b) What is one possible matrix *A?*

# **4.2 Projections**

1 The projection of a vector *b* onto the line through *a* is the closest point *p* = *a( a <sup>T</sup> b/ a* Ta). The error *e* = *b* -pis perpendicular to a: Right triangle *b p e* has I IPI l <sup>2</sup>+ I lei l = I Jbl l <sup>2</sup> . The **projection** of *b* onto a subspace Sis the closest vector pin *S; b* -pis orthogonal to *S. A<sup>T</sup>A*is invertible (and symmetric) only if *A* has independent columns: *N(A<sup>T</sup>A)= N(A).* Then the projection of *b* onto the column space of *A* is the vector *p* = *A(A<sup>T</sup>*A)-<sup>1</sup>*A<sup>T</sup> b.* The **projection matrix** onto *C(A)* is IP= *A(A<sup>T</sup>*A)-<sup>1</sup>*A<sup>T</sup> .* I It hasp= *Pb* and P<sup>2</sup>*=P* = *<sup>p</sup><sup>T</sup> \_*

May we start this section with two questions? (In addition to that one.) The first question aims to show that projections are easy to visualize. The second question is about "projection matrices"-symmetric matrices with P2 = *P. The projection of bis Pb.*

1 What are the projections of *b* = (2, 3, 4) onto the z axis and the *xy* plane? 2 What matrices A and P2 produce those projections onto a line and a plane?

When *b* is projected onto a line, *its projection pis the part of b along that line.* If *b* is projected onto a plane, *p* is the part in that plane. *The projection pis Pb.* The projection matrix *P* multiplies *b* to give *p.* This section finds *p* and also *P.*

The projection onto the z axis we call p<sup>1</sup> . The second projection drops straight down to the *xy* plane. The picture in your mind should be Figure 4.5. Start with *b* = (2, 3, 4). The projection across gives p1 = (0, 0, 4). The projection down gives p2 = (2, 3, 0). Those are the parts of *b* along the z axis and in the *xy* plane.

The projection matrices A and P2 are 3 by 3. They multiply *b* with 3 components to produce *p* with 3 components. Projection onto a line comes from a rank one matrix. Projection onto a plane comes from a rank two matrix:

| <b>Projection matrix</b> | $P_1 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | Onto the $xy$ plane: | $P_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ |
|--------------------------|---------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|
|--------------------------|---------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|

A picks out the z component of every vector. P2 picks out the x and y components. To find the projections p1 and p2 of *b,* multiply *b* by A and P2 (small p for the vector, capital *P* for the matrix that produces it):

| $p_1 = P_1 b =$ | $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ | $= \begin{bmatrix} 0 \\ 0 \\ z \end{bmatrix}$ | $p_2 = P_2 b =$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ | $= \begin{bmatrix} x \\ y \\ 0 \end{bmatrix}$ |
|-----------------|---------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------|-----------------|---------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------|
|                 |                                                                     |                                             |                                               |                 |                                                                     |                                             |                                               |

In this case the projections  $p_1$  and  $p_2$  are perpendicular. The  $xy$  plane and the  $z$  axis are **orthogonal subspaces**, like the floor of a room and the line between two walls.

![](images/_page_216_Picture_16.jpeg)

Figure 4.5: The projections  $p_1 = P_1 b$  and  $p_2 = P_2 b$  onto the  $z$  axis and the  $xy$  plane.

More than just orthogonal, the line and plane are orthogonal **complements**. Their dimensions add to  $1 + 2 = 3$ . Every vector  $b$  in the whole space is the sum of its parts in the two subspaces. The projections  $p_1$  and  $p_2$  are exactly those two parts of  $b$ :

The vectors give  $p_1 + p_2 = b$ . The matrices give  $P_1 + P_2 = I$ . (1)

This is perfect. Our goal is reached—for this example. We have the same goal for any line and any plane and any  $n$ -dimensional subspace. The object is to find the part  $p$  in each subspace, and the projection matrix  $P$  that produces that part  $p = Pb$ . Every subspace of  $\mathbf{R}^m$  has its own  $m$  by  $m$  projection matrix. To compute  $P$ , we absolutely need a good description of the subspace that it projects onto.

The best description of a subspace is a basis. We put the basis vectors into the columns of  $A$ . **Now we are projecting onto the column space of  $A$ !** Certainly the  $z$  axis is the column space of the 3 by 1 matrix  $A_1$ . The  $xy$  plane is the column space of  $A_2$ . That plane is *also* the column space of  $A_3$  (a subspace has many bases). So  $p_2 = p_3$  and  $P_2 = P_3$ .

$$A_1 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \quad \text{and} \quad A_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \quad \text{and} \quad A_3 = \begin{bmatrix} 1 & 2 \\ 2 & 3 \\ 0 & 0 \end{bmatrix}.$$

Our problem is **to project any  $b$  onto the column space of any  $m$  by  $n$  matrix**. Start with a line (dimension  $n = 1$ ). The matrix  $A$  will have only one column. Call it  $a$ .

### Projection Onto a Line

A line goes through the origin in the direction of  $a = (a_1, \dots, a_m)$ . Along that line, we want the point  $p$  closest to  $b = (b_1, \dots, b_m)$ . The key to projection is orthogonality: **The line from  $b$  to  $p$  is perpendicular to the vector  $a$ .** This is the dotted line marked  $e = b - p$  for the error on the left side of Figure 4.6. We now compute  $p$  by algebra.

The projection *p* will be some multiple of *a.* Call it *p* = *xa* = *"x* hat" times *a.*  Computing this number *x* will give the vector *p.* Then from the formula for *p,* we will read off the projection matrix *P.* These three steps will lead to all projection matrices: **find** *x,* **then find the vector** p, **then find the matrix** *P.*

The dotted line *b* - p is the "error" *e* = *b* - *xa.* It is perpendicular to a-this will determine *x.* Use the fact that *b-xa* is **perpendicular to** *<sup>a</sup>*when their dot product is zero:

| Projecting $b$ onto $a$ with error $e = b - \hat{x}a$ |    | $\hat{x} = \frac{a \cdot b}{a \cdot a} = \frac{a^T b}{a^T a}$ | (2) |
|-------------------------------------------------------|----|---------------------------------------------------------------|-----|
| $a \cdot (b - \hat{x}a) = 0$                          | or | $a \cdot b - \hat{x}a \cdot a = 0$                            |     |

The multiplication *a <sup>T</sup> b* is the same as *a* · *b.* Using the transpose is better, because it applies also to matrices. Our formula *x* = *a <sup>T</sup> b/ a <sup>T</sup> a* gives the projection p = *xa.* 

![](images/_page_217_Figure_6.jpeg)

Figure 4.6: The projection *p* of *b* onto a line and onto *S* = column space of *A.*

*� aTb* **The projection of** *b* **onto the line through** *a* **is the vector** p = *xa* = -- *a. a<sup>T</sup> a* 

Special case 1: If *b* = *a* then *x* = l. The projection of *a* onto *a* is itself. *Pa= a.* 

Special case 2: If bis perpendicular to *a* then *a <sup>T</sup> b* = 0. The projection is p = 0.

**Example 1** Project 
$$b = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$
 onto  $a = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$  to find  $p = \hat{x}a$  in Figure 4.6.

**Solution** The number *x* is the ratio of *a <sup>T</sup> b* = 5 to *a <sup>T</sup> a* = 9. So the projection is p = � *a.* 

The error vector between *b* and *p* is *e* = *b* - *p.* Those vectors *p* and *e* will add to b=(l,1,1):

$$p = \frac{5}{9}a = \left(\frac{5}{9}, \frac{10}{9}, \frac{10}{9}\right) \quad \text{and} \quad e = b - p = \left(\frac{4}{9}, -\frac{1}{9}, -\frac{1}{9}\right).$$

The error *e* should be perpendicular to *a=* (1, 2, 2) and it is: *e <sup>T</sup> a=* ½ - � - � = 0.

Look at the right triangle of *b, p,* and *e.* The vector *b* is split into two parts-its component along the line is *p,* its perpendicular part is *e.* Those two sides *p* and *e*  have length I IPI I = JJbJJ cos *<sup>0</sup>*and I Jel I = llbl l sin *0.* Trigonometry matches the dot product:

$$p = \frac{a^T b}{a^T a} \quad \text{has length} \quad \|p\| = \frac{\|a\| \|b\| \cos \theta}{\|a\|^2} \|a\| = \|b\| \cos \theta. \quad (3)$$

The dot product is a lot simpler than getting involved with cos *0* and the length of *b.*  The example has square roots in *cos0* = 5/3/3 and JJbll = /3. There are no square roots in the projection *p* = *5a/9.* The good way to 5/9 is *a <sup>T</sup> b/ a <sup>T</sup> a.*

Now comes the *projection matrix.* In the formula for *p,* what matrix is multiplying *b?*  You can see the matrix better if the number xis on the right side of a:

**Projection matrix** 
$$P = a\hat{x} = a \frac{a^T b}{a^T a} = Pb$$
 when the matrix is  $P = \frac{aa^T}{a^T a}$ .

*P* is a column times a row! The column is *a,* the row is *a* T. Then divide by the number *a <sup>T</sup> a.* The projection matrix *P* is *m* by *m,* but *its rank is one.* We are projecting onto a one-dimensional subspace, the line through *a. That line is the column space of P.* 

<sup>T</sup>**Example 2** Find the projection matrix *P* = :� *a*  onto the line through *a* = [ �] .

**Solution** Multiply column *a* times row *a* T and divide by *a <sup>T</sup> a* = 9:

| Projection matrix | $P = \frac{aa^T}{a^T a} = \frac{1}{9} \begin{bmatrix} 1 \\ 2 \\ 2 \\ a \end{bmatrix}$ | $\begin{bmatrix} 1 \\ 1 & 2 & 2 \end{bmatrix} = \frac{1}{9} \begin{bmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{bmatrix}$ |
|-------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|                   |                                                                                       |                                                                                                                                |

This matrix projects *any* vector *b* onto *a.* Checkp = *Pb* for *b* = (1, 1, 1) in Example 1:

| $p = Pb = \frac{1}{9} \begin{bmatrix} 5 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \frac{1}{9} \begin{bmatrix} 5 \\ 10 \\ 10 \end{bmatrix}$ | which is correct. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|

If the vector *a* is doubled, the matrix *P* stays the same! It still projects onto the same line. If the matrix is squared, *P<sup>2</sup>*equals *P. Projecting a second time doesn't change anything,*  so P**<sup>2</sup>**=*P.* The diagonal entries of *P* add up to½ (1 4 + 4) + 1. =

The matrix *I* -*P* should be a projection too. It produces the other side *e* of the trianglethe perpendicular part of *b.* Note that *(I* - *P)b* equals *b- p* which is *e* in the left nullspace.

*When P projects onto one subspace, I - P projects onto the perpendicular subspace.*  Here *I* - *P* projects onto the plane perpendicular to *a.* 

Now we move beyond projection onto a line. Projecting onto an n-dimensional subspace of Rm takes more effort. The crucial formulas will be collected in equations (5)-(6)-(7). Basically you need to remember those three equations.

### **Projection Onto a Subspace**

Start with *n* vectors a1, ... , *an* in Rm. Assume that these *a's* are linearly independent.

*Problem: Find the combination p* =x<sup>1</sup> a1+ · · · + *Xnan closest to a given vector b.*  We are projecting each bin Rm onto the subspace spanned by the *a's.* 

With *n* = l (one vector a1) this is projection onto a line. The line is the column space of *A,* which has just one column. In general the matrix *A* has *n* columns a1, ... , *an.* 

The combinations in Rm are the vectors *Ax* in the column space. We are looking for the particular combination *p* = *Ax (the projection)* that is closest to *b.* The hat over *x*  indicates the *best* choice *x,* to give the closest vector in the column space. That choice is *x* = *a <sup>T</sup> b/ a <sup>T</sup> a* when *n* = l. For *n* > l, the best *x* = (x1, ... , *xn)* is to be found now.

We compute projections onto n-dimensional subspaces in three steps as before: *Find the vector x, find the projection p* = *Ax, find the projection matrix P.* 

The key is in the geometry! The dotted line in Figure 4.6 goes from *b* to the nearest point *Ax* in the subspace. *This error vector b* - *Ax is perpendicular to the subspace.*  The error *b* - *Ax* makes a right angle with all the vectors a<sup>1</sup> , ... , *an* in the base. The n right angles give the n equations for x:

$$\begin{aligned} a_1^T(\mathbf{b} - A\hat{\mathbf{x}}) &= 0 \\ \vdots & \qquad \text{or} \\ a_n^T(\mathbf{b} - A\hat{\mathbf{x}}) &= 0 \end{aligned}$$

The matrix with those rows *a;* is *AT.* The *n* equations are exactly *A <sup>T</sup>(b* - *Ax)* = 0.

Rewrite *A <sup>T</sup>(b* - *Ax)* = O in its famous form *A <sup>T</sup>Ax* = *A T b.* This is the equation for *x,* and the coefficient matrix is *A<sup>T</sup>A.* Now we can find *x* and *p* and *P,* in that order.

The combination *p* = <sup>x</sup>1a1+ · · · + xnan = Ax that is closest to b comes from x:

| <b>Find <math display="block">\hat{x}(n \times 1)</math></b> | $A^T(b - A\hat{x}) = 0$ | or | $A^T A\hat{x} = A^T b$ | (5) |
|--------------------------------------------------------------|-------------------------|----|------------------------|-----|
|--------------------------------------------------------------|-------------------------|----|------------------------|-----|

This symmetric matrix A <sup>T</sup>A is *n* by *n.* It is invertible if the a's are independent. The solution is x = (AT A)-1 ATb. The *projection* of *b* onto the subspace is p:

| <b>Find <math display="block">p(m \times 1)</math></b> | $p = A\hat{x} = A(A^T A)^{-1} A^T b$ | (6) |
|--------------------------------------------------------|--------------------------------------|-----|
|--------------------------------------------------------|--------------------------------------|-----|

The next formula picks out the *projection matrix* that is multiplying bin (6):

| Find $P(m \times m)$ | $P = A(A^T A)^{-1} A^T$ | (7) |
|----------------------|-------------------------|-----|
|                      |                         |     |

Compare with projection onto a line, when A has only one column : AT A is a Ta.

| For $n = 1$ | $\widehat{x} = \frac{a^T b}{a^T a}$ | and | $p = a \frac{a^T b}{a^T a}$ | and | $P = \frac{aa^T}{a^T a}$ |
|-------------|-------------------------------------|-----|-----------------------------|-----|--------------------------|
| <hr/>       |                                     |     |                             |     |                          |

Those formulas are identical with (5) and (6) and (7). The number a Ta becomes the matrix AT A. When it is a number, we divide by it. When it is a matrix, we invert it. The new formulas contain (AT A)-1 instead of l/aTa. The linear independence of the columns a1, ... , an will guarantee that this inverse matrix exists.

The key step was A<sup>T</sup> (b - Ax) = 0. We used geometry (e is orthogonal to each *a). Linear algebra gives this "normal equation" too,* in a very quick and beautiful way :

- 1. Our subspace is the column space of *A.*
- 2. The error vector *b*  Ax is perpendicular to that column space.
- 3. Therefore *b*  Ax is in the nulls pace of A<sup>T</sup> ! This means AT ( *b*  Ax) <sup>=</sup>0.

The left nullspace is important in projections. That nullspace of AT contains the error vector *e* = *b-*Ax. The vector bis being split into the projection *p* and the error *e* = *b-p.* Projection produces a right triangle with sides *p, e,* and *b.*

**Example 3** If 
$$A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$$
 and  $b = \begin{bmatrix} 6 \\ 0 \end{bmatrix}$  find  $\hat{x}$  and  $p$  and  $P$ .

**Solution** Compute the square matrix AT A and also the vector ATb:

| $A^{\text{T}}A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 3 & 3 \\ 3 & 3 \end{bmatrix}$ | and $A^{\text{T}}\mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 2 \end{bmatrix}$ | $\begin{bmatrix} 6 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 6 \\ 0 \\ 0 \end{bmatrix}$ |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|

Now solve the normal equation  $A^T A \hat{x} = A^T b$  to find  $\hat{x}$ :

$$\begin{bmatrix} 3 & 3 \\ 3 & 5 \end{bmatrix} \begin{bmatrix} \hat{x}_1 \\ \hat{x}_2 \end{bmatrix} = \begin{bmatrix} 6 \\ 0 \end{bmatrix} \quad \text{gives} \quad \hat{x} = \begin{bmatrix} \hat{x}_1 \\ \hat{x}_2 \end{bmatrix} = \begin{bmatrix} 5 \\ -3 \end{bmatrix}. \quad (8)$$

The combination  $p = A \hat{x}$  is the projection of  $b$  onto the column space of  $A$ :

$$p = 5 \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - 3 \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \\ -1 \end{bmatrix}. \quad \text{The error is} \quad e = b - p = \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}. \quad (9)$$

Two checks on the calculation. First, the error  $e = (1, -2, 1)$  is perpendicular to both columns  $(1, 1, 1)$  and  $(0, 1, 2)$ . Second, the matrix  $P$  times  $b = (6, 0, 0)$  correctly gives  $p = (5, 2, -1)$ . That solves the problem for one particular  $b$ , as soon as we find  $P$ .

The projection matrix is  $P = A(A^T A)^{-1} A^T$ . The determinant of  $A^T A$  is  $15 - 9 = 6$ ; then  $(A^T A)^{-1}$  is easy. Multiply  $A$  times  $(A^T A)^{-1}$  times  $A^T$  to reach  $P$ :

$$(A^T A)^{-1} = \frac{1}{6} \begin{bmatrix} 5 & -3 \\ -3 & 3 \end{bmatrix} \quad \text{and} \quad P = \frac{1}{6} \begin{bmatrix} 5 & 2 & -1 \\ 2 & 2 & 2 \\ -1 & 2 & 5 \end{bmatrix}. \quad (10)$$

We must have  $P^2 = P$ , because a second projection doesn't change the first projection.

**Warning** The matrix  $P = A(A^T A)^{-1} A^T$  is deceptive. You might try to split  $(A^T A)^{-1}$  into  $A^{-1}$  times  $(A^T)^{-1}$ . If you make that mistake, and substitute it into  $P$ , you will find  $P = AA^{-1}(A^T)^{-1} A^T$ . Apparently everything cancels. This looks like  $P = I$ , the identity matrix. We want to say why this is wrong.

**The matrix  $A$  is rectangular. It has no inverse matrix.** We cannot split  $(A^T A)^{-1}$  into  $A^{-1}$  times  $(A^T)^{-1}$  because there is no  $A^{-1}$  in the first place.

In our experience, a problem that involves a rectangular matrix almost always leads to  $A^T A$ . When  $A$  has independent columns,  $A^T A$  is invertible. This fact is so crucial that we state it clearly and give a proof.

 **$A^T A$  is invertible if and only if  $A$  has linearly independent columns.**

**Proof**  $A^T A$  is a square matrix ( $n$  by  $n$ ). For every matrix  $A$ , we will now show that  $A^T A$  has the same nullspace as  $A$ . When the columns of  $A$  are linearly independent, its nullspace contains only the zero vector. Then  $A^T A$ , with this same nullspace, is invertible.

Let  $A$  be any matrix. If  $x$  is in its nullspace, then  $Ax = 0$ . Multiplying by  $A^T$  gives  $A^T Ax = 0$ . So  $x$  is also in the nullspace of  $A^T A$ .

Now start with the nullspace of  $A^T A$ . **From**  $A^T Ax = 0$  we must prove  $Ax = 0$ . We can't multiply by  $(A^T)^{-1}$ , which generally doesn't exist. Just multiply by  $x^T$ :

$$(x^T) A^T Ax = 0 \quad \text{or} \quad (Ax)^T (Ax) = 0 \quad \text{or} \quad \|Ax\|^2 = 0. \quad (11)$$

We have shown: If  $A^T Ax = 0$  then  $Ax$  has length zero. Therefore  $Ax = 0$ . Every vector  $x$  in one nullspace is in the other nullspace. If  $A^T A$  has dependent columns, so has  $A$ . If  $A^T A$  has independent columns, so has  $A$ . This is the good case:  $A^T A$  is invertible.

### *When A has independent columns, AT A is square, symmetric, and invertible.*

To repeat for emphasis: *AT A* is *(n* by m) times (m by *n).* Then *AT A* is square *(n* by *n).* It is symmetric, because its transpose is *(AT A)* <sup>T</sup>= *AT (A<sup>T</sup> )* <sup>T</sup>which equals *AT A.* We just proved that *AT A* is invertible-provided *A* has independent columns. Watch the difference between dependent and independent columns:

$$\begin{bmatrix} A^T & A \\ \begin{bmatrix} 1 & 2 \\ 2 & 0 \end{bmatrix} & \begin{bmatrix} 1 & 2 \\ 1 & 2 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 4 & 8 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} A^T & A \\ \begin{bmatrix} 1 & 2 \\ 2 & 0 \end{bmatrix} & \begin{bmatrix} 1 & 2 \\ 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 4 & 9 \end{bmatrix} \end{bmatrix}$$

**Very brief summary** To find the projectionp = :i\a1 + · · · *+xnan,* solve *AT Ax= A <sup>T</sup> b.*  This gives *x.* The projection is *p* = *Ax* and the error is *e* = *b* - *p* = *b* - *Ax.* The projection matrix *P* = *A(A<sup>T</sup>*A)-1 *A<sup>T</sup>*gives *p* = *Pb.* 

**This matrix satisfies P**<sup>2</sup>=*P. The distance from b to the subspace C(A) is llell-*

#### **• REVIEW OF THE KEY IDEAS •**

- 1. The projection of *b* onto the line through *a* is *p* = *ax* = *a( a <sup>T</sup> b/ a Ta).*
- **2.** The rank one projection matrix *P* = *aa* T / *a <sup>T</sup> a* multiplies *b* to produce *p.*
- **3.** Projecting *b* onto a subspace leaves *e* = *b p* perpendicular to the subspace.
- **4.** When *A* has full rank n, the equation *AT Ax= A<sup>T</sup> b* leads to *x* and *p* = *Ax.*
- **5.** The projection matrix *P* = *A(A<sup>T</sup>*A)-<sup>1</sup>*A<sup>T</sup>*has *p <sup>T</sup>*= *P* and P2 = *P* and *Pb= p.*

#### **• WORKED EXAMPLES •**

**4.2 A** Project the vector *b* = (3, 4, 4) onto the line through *a* = (2, 2, 1) and then onto the plane that also contains *a\** = (1, 0, 0). Check that the first error vector *b* - *p* is perpendicular to *a,* and the second error vector *e\** = *b* - *p\** is also perpendicular to *a\*.* 

Find the 3 by 3 projection matrix *P* onto that plane of *a* and *a\*.* Find a vector whose *projection onto the plane is the zero vector.* Why is it exactly the error *e\** ?

**Solution** The projection of *b* = (3, 4, 4) onto the line through *a=* (2, 2, 1) is *p* = *2a:*

Onto a line 
$$p = \frac{a^T b}{a^T a} a = \frac{18}{9}(2, 2, 1) = (4, 4, 2) = 2a.$$

The error vector *e* = *b* -*p* = (-l, 0, 2) is perpendicular to *a=* (2, 2, 1). *Sop* is correct.

The plane of *a=* (2, 2, 1) and *a\*=* (1, 0, 0) is the column space of *A=* [a a\*]:

$$A = \begin{bmatrix} 2 & 1 \\ 2 & 0 \\ 1 & 0 \end{bmatrix}, \quad A^T A = \begin{bmatrix} 9 & 2 \\ 2 & 1 \end{bmatrix}, \quad (A^T A)^{-1} = \frac{1}{5} \begin{bmatrix} 1 & -2 \\ -2 & 9 \end{bmatrix}, \quad P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & .8 & .4 \\ 0 & .4 & .2 \end{bmatrix}.$$

Now *p\** = *Pb=* (3, 4.8, 2.4). The error *e\** = *b* - *p\** = (0, -.8, 1.6) is perpendicular to *a* and *a\*.* This *e\** is in the nullspace of *P* and *its projection is zero!* Note P2 = *P* = *p T\_*

**4.2 B** Suppose your pulse is measured at *x* = 70 beats per minute, then at *x* = 80, then at *x* = 120. Those three equations *Ax* = *b* in one unknown have *A<sup>T</sup>*= [1 1 1] and *b* = (70, 80,120). *The best xis the* \_\_ *of* 70, 80,120. Use calculus and projection:

- 1. Minimize *E* = *(x*  70)2 + *(x*  80)2 + *(x*  <sup>12</sup>0)2 by solving *dE/dx* = 0.
- 2. Project *b* = (70, 80,120) onto *a=* (l, 1, 1) to find *x* = *a <sup>T</sup>bja<sup>T</sup>a.*

**Solution** The closest horizontal line to the heights 70, 80, 120 is the *average x* = 90:

$$\frac{dE}{dx} = 2(x - 70) + 2(x - 80) + 2(x - 120) = 0 \quad \text{gives} \quad \hat{x} = \frac{70 + 80 + 120}{3} = 90.$$

| Also by projection : | $\hat{x} = \frac{a^T b}{a^T a} = \frac{(1, 1, 1)^T (70, 80, 120)}{(1, 1, 1)^T (1, 1, 1)} = \frac{70 + 80 + 120}{3} = 90.$ |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|
|----------------------|---------------------------------------------------------------------------------------------------------------------------|

In *recursive* least squares, a fourth measurement 130 changes the average Xold = 90 to *Xnew* = 100. Verify the *update formula Xnew* = Xold + ¾(130 - <sup>x</sup>01d)- When a new measurement arrives, we don't have to average all the old measurements again!

#### **Problem Set 4.2**

**Questions 1-9 ask for projections** *p* **onto lines. Also errors** *e* = *b* - *p* **and matrices** *P.*

1 Project the vector b onto the line through *a.* Check that *e* is perpendicular to *a:*

| (a) | $b = \begin{bmatrix} 1 \\ 2 \\ 2 \\ 2 \end{bmatrix}$ | and | $a = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}$ | (b) | $b = \begin{bmatrix} 1 \\ 3 \\ 3 \\ 1 \end{bmatrix}$ | and | $a = \begin{bmatrix} -1 \\ -3 \\ -1 \\ -1 \end{bmatrix}$ |
|-----|------------------------------------------------------|-----|------------------------------------------------------|-----|------------------------------------------------------|-----|----------------------------------------------------------|
|-----|------------------------------------------------------|-----|------------------------------------------------------|-----|------------------------------------------------------|-----|----------------------------------------------------------|

2 *Draw* the projection of *b* onto *a* and also compute it from *p* **=** xa:

| $a$ | $b = \begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix}$ | and | $a = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ | (b) | $b = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ | and | $a = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ |
|-----|----------------------------------------------------------------|-----|--------------------------------------------|-----|--------------------------------------------|-----|---------------------------------------------|
|-----|----------------------------------------------------------------|-----|--------------------------------------------|-----|--------------------------------------------|-----|---------------------------------------------|

3 In Problem 1, find the projection matrix P = aaTjaTa onto the line through each vector a. Verify in both cases that P*<sup>2</sup>*<sup>=</sup> P. Multiply Pb in each case to compute the projection *p.* 4 Construct the projection matrices A and P2 onto the lines through the a's in Problem 2. Is it true that (A + P<sup>2</sup> ) <sup>2</sup>**=** A + *P<sup>2</sup> ?* This *would* be true if *AP2***=** 0. 5 Compute the projection matrices *aa* T / *a* Ta onto the lines through a1 = ( -1, 2, 2) and a*2* **=** (2, 2, -1). Multiply those projection matrices and explain why their product AA is what it is. 6 Project b **=** (1, 0, 0) onto the lines through a1 and a*2* in Problem 5 and also onto a3 **=** (2, -1, 2). Add up the three projections p1 + *p2*<sup>+</sup>p3. 7 Continuing Problems 5-6, find the projection matrix P3 onto a*3*<sup>=</sup> (2, -1, 2). Verify that **A** + P2 + P*3* **=** I. This is because the basis a1, *a2, <sup>a</sup>3*is orthogonal!

*a3* = [-�] **[-1]** 2 a*1* = <sup>2</sup>

*a, <sup>=</sup>*[ j]

Questions 5-6-7: orthogonal

![](images/_page_224_Diagram_5.jpeg)

Questions 8-9-10: not orthogonal

8 Project the vector *<sup>b</sup>* <sup>=</sup>(1, 1) onto the lines through a1 = (1, 0) and *a2*<sup>=</sup>(1, 2). Draw the projections p1 and p*2* and add p1 + p*<sup>2</sup> .* The projections do not add to *<sup>b</sup>* because the *a's* are not orthogonal. 9 In Problem 8, the projection of *b* onto the *plane* of a1 and *a2*will equal *b.* Find P=A(ATA)-*1*A<sup>T</sup> forA= [a1 a2] **=** [H] **=** invertible matrix. 10 Project a1 = (1, 0) onto a2 <sup>=</sup> (1, 2). Then project the result back onto a1. Draw these projections and multiply the projection matrices AP2: Is this a projection?

#### Questions 11-20 ask for projections, and projection matrices, onto subspaces.

11 Project b onto the column space of A by solving A<sup>T</sup>Ax= A <sup>T</sup>b and *p* = Ax:

| (a) | $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$ | and | $b = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$ | (b) | $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$ | and | $b = \begin{bmatrix} 4 \\ 4 \\ 6 \end{bmatrix}$ |
|-----|-------------------------------------------------------------|-----|-------------------------------------------------|-----|-------------------------------------------------------------|-----|-------------------------------------------------|
|-----|-------------------------------------------------------------|-----|-------------------------------------------------|-----|-------------------------------------------------------------|-----|-------------------------------------------------|

Find e = *b* - *p.* It should be perpendicular to the columns of A.

- 12 Compute the projection matrices A and P2 onto the column spaces in Problem 11. Verify that Ab gives the first projection p1. Also verify *P}* = P2. 13 (Quick and Recommended) Suppose A is the 4 by 4 identity matrix with its last column removed. *A* is 4 by 3. Project *b* = (1, 2, 3, 4) onto the column space of A. What shape is the projection matrix *P* and what is *P?*  14 Suppose *b* equals 2 times the first column of *A.* What is the projection of *b* onto the column space of *A?* Is *P* = *I* for sure in this case? Compute *p* and *P* when *b* = (0, 2, 4) and the columns of *A* are (0, 1, 2) and (1, 2, 0). 15 If A is doubled, then P = 2A(4A<sup>T</sup>A)-<sup>1</sup> 2A<sup>T</sup> \_ This is the same as A(A<sup>T</sup>A)-*<sup>1</sup>*A<sup>T</sup>. The column space of 2A is the same as \_\_ . Is *x* the same for A and 2A? 16 What linear combination of (1, 2, -1) and (1, 0, 1) is closest to *b* = (2, 1, 1 )? 17 *(Important)* If P<sup>2</sup>= *P* show that *(I* - P)<sup>2</sup>= *I* - *P.* When *P* projects onto the column space of *A, I* - *P* projects onto the \_\_ . 18 (a) If Pis the 2 by 2 projection matrix onto the line through (1, 1), then *I* - Pis the projection matrix onto \_\_ .
- (b) If Pis the 3 by 3 projection matrix onto the line through (1, 1, 1), then *I P* is the projection matrix onto \_\_ . 19 To find the projection matrix onto the plane *x* - *y* - 2z = 0, choose two vectors in that plane and make them the columns of A. The plane will be the column space of A! Then compute P = A(A<sup>T</sup>A)-<sup>1</sup>A<sup>T</sup>. 20 To find the projection matrix *P* onto the same plane *x* - *y* - 2z = 0, write down a vector e that is perpendicular to that plane. Compute the projection *Q* = ee T / e Te and then *P* = *I* - *Q.*

### Questions21-26show that projection matrices satisfy *P<sup>2</sup>*= *P* and p<sup>T</sup>= *P.*

21 Multiply the matrix P A(A<sup>T</sup>A)-<sup>1</sup>A<sup>T</sup>by itself. Cancel to prove that P<sup>2</sup>= P. Explain why *P(Pb)* always equals *Pb:* The vector *Pb* is in the column space of *A*  so its projection onto that column space is \_\_ . 22 Prove that P = A(A<sup>T</sup>A)-<sup>1</sup>A<sup>T</sup>is symmetric by computing p<sup>T</sup> \_ Remember that the inverse of a symmetric matrix is symmetric.

23 If *A* is square and invertible, the warning against splitting ( *AT A)* - <sup>1</sup>does not apply. It is true that *AA* -l *(AT* )-<sup>1</sup>*A<sup>T</sup>***=***I. When A is invertible, why is P* **=** *I? What is the error e?* 24 The nullspace of *AT* is \_\_ to the column space *C(A).* So if *A T b* **=** 0, the projection of *b* onto *C(A)* should be *p***= \_\_ .** Check that *P* **=** *A(AT* A)-<sup>1</sup>*A<sup>T</sup>* gives this answer. 25 The projection matrix *P* onto an n-dimensional subspace of R <sup>m</sup>has rank r **=** n. *Reason:* The projections *Pb* fill the subspace *S.* So Sis the \_\_ of*P.*  26 If an m by m matrix has A<sup>2</sup>**=** *A*and its rank ism, prove that *A= I.* 27 The important fact that ends the section is this: *If A<sup>T</sup>Ax* = 0 *then Ax* = 0. *New Proof:* The vector *Ax* is in the nullspace of \_\_ . *Ax* is always in the column space of \_\_ . To be in both of those perpendicular spaces, *Ax* must be zero. 28 Use *p <sup>T</sup>***=***P* and P <sup>2</sup>**=***P* to prove that the length squared of column 2 always equals the diagonal entry A2. This number is � **<sup>=</sup>**<sup>3</sup> � <sup>+</sup><sup>3</sup> � <sup>+</sup><sup>3</sup> � for

$$P = \frac{1}{6} \begin{bmatrix} 5 & 2 & -1 \\ 2 & 2 & 2 \\ -1 & 2 & 5 \end{bmatrix}$$

29 If *B* has rank m (full row rank, independent rows) show that *BE<sup>T</sup>*is invertible.

### **Challenge Problems**

30 (a) Find the projection matrix Pc onto the column space of A (after looking closely at the matrix!)

$$A = \begin{bmatrix} 3 & 6 & 6 \\ 4 & 8 & 8 \end{bmatrix}$$

- (b) Find the 3 by 3 projection matrix *PR* onto the row space of *A.* Multiply *B* **<sup>=</sup>** *P0APR.* Your answer *B* should be a little surprising-can you explain it? 31 In Rm, suppose I give you *b* and also a combination *p* of a1, ... , *a<sup>n</sup> .* How would you test to see if pis the projection of b onto the subspace spanned by the *a's?*  32 Suppose Pi is the projection matrix onto the I-dimensional subspace spanned by the first column of *A.* Suppose *P2* is the projection matrix onto the 2-dimensional column space of *A.* After thinking a little, compute the product P2Pi.

$$A = \begin{bmatrix} 1 & 0 \\ 2 & 1 \\ 0 & 1 \end{bmatrix}.$$

33 Suppose you know the average XoJd of b1, b2, ... , b999. When b1000 arrives, check that the new average is a combination of XoJd and the mismatch b1000 - Xold:

$$\hat{\mathbf{x}}_{\text{new}} = \frac{b_1 + \dots + b_{1000}}{1000} = \frac{b_1 + \dots + b_{999}}{999} + \frac{1}{1000} \left( b_{1000} - \frac{b_1 + \dots + b_{999}}{999} \right).$$

This is a "Kalman fi.Uer" Xnew = Xold + iloo (b1000 - XoJd) with gain matrix 1<sup>0</sup> 1 00 . The last page of the book extends the Kalman filter to matrix updates.

34 (2017) Suppose Pi and P2 are projection matrices (Pl= Pi= P?). Prove this fact: Pi P2 is a projection matrix if and only if Pi P2 = P2 A.

# **4.3 Least Squares Approximations**

**<sup>1</sup>**Solving I AT Ax = AT b I gives the projection *p* = Ax of b onto the column space of A. **<sup>2</sup>**When Ax = b has no solution, xis the "least -squares solution": I lb - Axl <sup>1</sup> <sup>2</sup>= minimum. **<sup>3</sup>**Setting partial derivatives of E <sup>=</sup><sup>I</sup>!Ax - bl <sup>1</sup> <sup>2</sup>to zero ( *gf* <sup>=</sup>0) also produces AT Ax <sup>=</sup> A<sup>T</sup> b. 4 To fit points ( t1, b1 ), ... , (tm, bm) by a straight line, A has columns (1, ... , 1) and (t1, ... , tm)- <sup>A</sup>TA [ m � *ti* ] A<sup>T</sup> <sup>b</sup> . [ � *bi*  S ] In that case is the 2 by 2 matrix � *ti* � tr and 1s the vector � *tibi*  .

It often happens that Ax = *<sup>b</sup>*has no solution. The usual reason is: *too many equations.*  The matrix *A* has more rows than columns. There are more equations than unknowns (mis greater than n). Then columns span a small part of m-dimensional space. Unless all measurements are perfect, *b* is outside that column space of A. Elimination reaches an impossible equation and stops. But we can't stop just because measurements include noise!

To repeat: We cannot always get the error e = *b* - Ax down to zero. When e is zero, x is an exact solution to Ax = *b. When the length of e is as small as possible,* x *is a least squares solution.* Our goal in this section is to compute *x* and use it. These are real problems and they need an answer.

The previous section emphasized *p* (the projection). This section emphasizes x (the least squares solution). They are connected by *<sup>p</sup>*= Ax. The fundamental equation is still AT Ax= A<sup>T</sup> b. Here is a short unofficial way to reach this *"normal equation":* 

**When** Ax= b **has no solution, multiply by** A<sup>T</sup>**and solve** A <sup>T</sup>Ax= A Tb.

**Example 1** A crucial application of least squares is fitting a straight line to m points. Start with three points: *Find the closest line to the points* (0, 6), (1, 0), *and* (2, 0).

No straight line *<sup>b</sup>* <sup>=</sup>*C* + *Dt* goes through those three points. We are asking for two numbers *C* and *D* that satisfy three equations: n = 2 and m = 3. Here are the three equations at *t* = 0, l, 2 to match the given values b = 6, 0, 0:

*t=O*  **t=l t=2**  The first point is on the line b <sup>=</sup>C +*Dt* if The second point is on the line b = C + *Dt* if The third point is on the line b <sup>=</sup>C +*Dt* if C+D·0=6 C+D·l=0 C+D·2 = 0. This 3 by 2 system has *no solution: b* <sup>=</sup> (6, 0, 0) is not a combination of the columns (1, 1, 1) and (0, 1, 2). Read off *A,* x, and *b* from those equations:

| $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}$ | $\mathbf{x} = \begin{bmatrix} C \\ D \end{bmatrix}$ | $\mathbf{b} = \begin{bmatrix} 6 \\ 0 \\ 0 \end{bmatrix}$ | $A\mathbf{x} = \mathbf{b}$ is <i>not</i> solvable. |
|-------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|----------------------------------------------------|
|-------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|----------------------------------------------------|

The same numbers were in Example 3 in the last section. We computed *x* = (5, -3). **Those numbers are the best** *C* **and** *D,* **so** 5 - 3t **will be the best line for the 3 points.** We must connect projections to least squares, by explaining why A <sup>T</sup>Ax= A Tb.

In practical problems, there could easily be m = 100 points instead of m = 3. They don't exactly match any straight line C + Dt. Our numbers 6, 0, 0 exaggerate the error so you can see e1, e<sup>2</sup> , and e3 in Figure 4.6.

# **Minimizing the Error**

How do we make the error *e* = *b* -*Ax* as small as possible? This is an important question with a beautiful answer. The best *x* (called x) can be found by geometry (the error *e* meets the column space of A at 90° ) and by algebra : AT Ax <sup>=</sup> A <sup>T</sup>b. Calculus gives the same x: the derivative of the error I *!Ax* - bl 1 <sup>2</sup>is zero at *x.*

**By geometry** Every *Ax* lies in the plane of the columns (1, 1, 1) and (0, 1, 2). In that plane, we look for the point closest to *b. The nearest point is the projection p.* 

The best choice for Ax is *p.* The smallest possible error is *e* = b - *p,* perpendicular to the columns. *The three points at heights* (p1, p2, p3) *do lie on a line,* because *p* is in the column space of *A.* In fitting a straight line, xis the best choice for ( *C, D).*

**By algebra** Every vector *b* splits into two parts. The part in the column space is *p.*  The perpendicular part is *e.* There is an equation we cannot solve *(Ax* = *b).* There is an equation Ax= *p* we can and do solve (by removing *e* and solving A <sup>T</sup>Ax= A<sup>T</sup> b) :

| $Ax = b = p + e$ | is impossible | $A\hat{x} = p$ | is solvable | $\hat{x}$ | is $(A^T A)^{-1} A^T b$ . (1) |
|------------------|---------------|----------------|-------------|-----------|-------------------------------|
|                  |               |                |             |           |                               |

The solution to Ax = *p* leaves the least possible error (which is e):

| Squared length for any $x$ | $\ Ax - b\ ^2 = \ Ax - p\ ^2 + \ e\ ^2$ | (2) |
|----------------------------|-----------------------------------------|-----|
|                            |                                         |     |

This is the law c <sup>2</sup>= a <sup>2</sup>+ b <sup>2</sup>for a right triangle. The vector *Ax* - pin the column space is perpendicular to *e* in the left nullspace. We reduce *Ax* - *p* to **zero** by choosing *x* = *x.* That leaves the smallest possible error *e* = ( e1, e2, e3) which we can't reduce.

Notice what "smallest" means. The *squared length* of *Ax* -*b* is minimized:

### *The least squares solution x makes E* = 11 *Ax* - *b* 11 <sup>2</sup>*as small as possible.*

Figure 4.6a shows the closest line. It misses by distances e1, e2, e3 = 1, -2, 1. *Those are vertical distances.* The least squares line minimizes *E* <sup>=</sup> ei + *e�* + e�.

Figure 4.6b shows the same problem in 3-dimensional space (b *p e* space). The vector *b* is not in the column space of *A.* That is why we could not solve Ax = *b.* No line goes through the three points. The smallest possible error is the perpendicular vector *e.* This is *e* = b - Ax, the vector of errors (1, -2, 1) in the three equations. Those are the distances from the best line. Behind both figures is the fundamental equation A<sup>T</sup>Ax = A<sup>T</sup>*b.*

![](images/_page_230_Figure_3.jpeg)

Figure 4.6: **Best line and projection: Two pictures, same problem.** The line has heights *p* <sup>=</sup>(5, 2, -1) with errors *e* = (1, -2, 1). The equations A<sup>T</sup>Ax= A<sup>T</sup>b give x = (5, -3). Same answer! The best line is *b* = 5 - *3t* and the closest point is *p* = 5a1 - 3a2.

Notice that the errors 1, -2, 1 add to zero. *Reason:* The error *e* = (e1, e2, e3) is perpendicular to the first column (1, 1, 1) in *A.* The dot product gives e1 + e2 + e3 = 0.

**By calculus** Most functions are minimized by calculus! The graph bottoms out and the derivative in every direction is zero. Here the error function *E* to be minimized is a *sum of squares* **ei** + *e�* + *e�* (the square of the error in each equation):

$$E = \|Ax - b\|^2 = (C + D \cdot 0 - 6)^2 + (C + D \cdot 1)^2 + (C + D \cdot 2)^2. \quad (3)$$

The unknowns are *C* and *D.* With two unknowns there are *two derivatives-both* zero at the minimum. They are "partial derivatives" because *8 E* / *fJC* treats *D* as constant and *8E/8D* treats *C* as constant:

| $\partial E/\partial C = 2(C + D \cdot 0 - 6)$ | $+2(C + D \cdot 1)$ | $+2(C + D \cdot 2)$ | $= 0$ |
|------------------------------------------------|---------------------|---------------------|-------|
|                                                |                     |                     |       |

$$\partial E/\partial D = 2(C + D \cdot 0 - 6)(\mathbf{0}) + 2(C + D \cdot 1)(\mathbf{1}) + 2(C + D \cdot 2)(\mathbf{2}) = 0.$$

*8 E* / *8 D* contains the extra factors O, 1, 2 from the chain rule. (The last derivative from *(C* + 2D)<sup>2</sup>was 2 times *C* + 2D times that extra 2.) Those factors are just 1, 1, 1 in *8E/8C.* 

It is no accident that those factors 1, 1, 1 and 0, 1, 2 in the derivatives of I I Ax - bl 1 2 are the columns of *A.* Now cancel 2 from every term and collect all C's and all D's:

| The $C$ derivative is zero: | $3C + 3D = 6$ | This matrix | $\begin{bmatrix} 3 & 3 \\ 3 & 3 \end{bmatrix}$ | is $A^T A$ | (4) |
|-----------------------------|---------------|-------------|------------------------------------------------|------------|-----|
| The $D$ derivative is zero: | $3C + 5D = 0$ |             |                                                |            |     |

*These equations are identical with* AT Ax = AT b. The best *C* and *D* are the components of x. The equations from calculus are the same as the "normal equations" from linear algebra. These are the key equations of least squares:

#### *The partial derivatives of* II Ax - bll<sup>2</sup>*are zero when* A <sup>T</sup>Ax = A Tb.

The solution is C = 5 and D = -3. Therefore b = 5 - 3t is the best line-it comes closest to the three points. At *t* = 0, 1, 2 this line goes through *p* = 5, 2, -1. It could not go through *b* = 6, 0, 0. The errors are 1, -2, 1. This is the vector el

# **The Big Picture for Least Squares**

The key figure of this book shows the four subspaces and the true action of a matrix. The vector x on the left side of Figure 4.3 went to b = Ax on the right side. In that figure x was split into *Xr* + *Xn.* There were *many* solutions to Ax = *b.* 

In this section the situation is just the opposite. There are *no* solutions to Ax <sup>=</sup>b. *Instead of splitting up x we are splitting up b* = *p* + *e.* Figure 4.7 shows the big picture for least squares. Instead of Ax = b we solve Ax = p. The error *e* = b-p is unavoidable.

![](images/_page_231_Diagram_12.jpeg)

Figure 4.7: The projection *p* =Ax is closest to *b,* so x minimizes E = llb - Axll <sup>2</sup> .

Notice how the nullspace *N(A)* is very small-just one point. With independent columns, the only solution to Ax = 0 is x = 0. Then AT A is invertible. The equation A <sup>T</sup>Ax = A<sup>T</sup>*b*fully determines the best vector x. The error has A<sup>T</sup>*e* = 0.

Chapter 7 will have the complete picture-all four subspaces included. Every x splits into Xr + Xn, and every b splits into p + e. The best solution is *x* = Xr in the row space. We can't help *e* and we don't want Xn from the nullspace-this leaves Ax = *p.* 

## **Fitting a Straight Line**

Fitting a line is the clearest application of least squares. It starts with *m* > 2 points, hopefully near a straight line. At times t1, ... , *tm* those *m* points are at heights b1, ... , *bm.* The best line *C* + *Dt* misses the points by vertical distances e1, ... , *em.*  No line is perfect, and the least squares line minimizes E = er+···+ *e;,...*

The first example in this section had three points in Figure 4.6. Now we allow *m* points (and *m* can be large). The two components of *x* are still C and D.

A line goes through them points when we exactly solve *Ax* = *b.* Generally we can't do it. Two unknowns *C* and *D* determine a line, so *A* has only *n* = 2 columns. To fit the *m* points, we are trying to solve *m* equations (and we only have two unknowns!).

$$Ax = b \quad \text{is} \quad \begin{aligned} & C + Dt_1 = b_1 \\ & C + Dt_2 = b_2 \\ & \vdots \\ & C + Dt_m = b_m \end{aligned} \quad \text{with} \quad A = \begin{bmatrix} 1 & t_1 \\ 1 & t_2 \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix}. \quad (5)$$

The column space is so thin that almost certainly b is outside of it. When b happens to lie in the column space, the points happen to lie on a line. In that case b = p. Then *Ax* = <sup>b</sup> is solvable and the errors are *e* = (0, ... , 0).

*The closest line C* + Dt *has heights* p1, ... , *Prn with errors e* 1, ••• , *ern. Solve* AT Ax= A <sup>T</sup> b *for* x = (C, D). *The errors are* ei = bi - *C* - Dti.

Fitting points by a straight line is so important that we give the two equations AT Ax = A<sup>T</sup> b, once and for all. The two columns of A are independent (unless all times ti are the same). So we turn to least squares and solve AT Ax= A<sup>T</sup> b.

| Dot-product matrix | $A^T A = \begin{bmatrix} 1 & \cdots & 1 \\ t_1 & \cdots & t_m \end{bmatrix}$ | $\begin{bmatrix} 1 & t_1 \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix}$ | $= \begin{bmatrix} m & \sum t_i \\ \sum t_i & \sum t_i^2 \end{bmatrix}$ | (6) |
|--------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------|-----|
|--------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------|-----|

On the right side of the normal equation is the 2 by 1 vector AT b:

$$A^T \mathbf{b} = \begin{bmatrix} 1 & \cdots & 1 \\ t_1 & \cdots & t_m \end{bmatrix} \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} = \begin{bmatrix} \sum b_i \\ \sum t_i b_i \end{bmatrix}. \quad (7)$$

The line C + Dt minimizes d + · · · + e;,, = IIAx - bll <sup>2</sup>when <sup>A</sup> <sup>T</sup>Ax= A <sup>T</sup>b:

$$A^T A \hat{\mathbf{x}} = A^T \mathbf{b} \quad \left[ \begin{array}{cc} m & \Sigma t_i \\ \Sigma t_i & \Sigma t_i^2 \end{array} \right] \begin{bmatrix} C \\ D \end{bmatrix} = \begin{bmatrix} \Sigma b_i \\ \Sigma t_i b_i \end{bmatrix}. \quad (8)$$

The vertical errors at the *m* points on the line are the components of *e* = *b* - *p.* This error vector (the *residual) b* - Ax is perpendicular to the columns of A (geometry). The error is in the nullspace of <sup>A</sup> <sup>T</sup>(linear algebra). The best x = *(C, D)* minimizes the total error *E,* the sum of squares (calculus):

$$E(\mathbf{x}) = \|A\mathbf{x} - \mathbf{b}\|^2 = (C + Dt_1 - b_1)^2 + \dots + (C + Dt_m - b_m)^2.$$

Calculus sets the derivatives 8E/8C and 8E/8D to zero, and produces A <sup>T</sup>Ax= A Tb.

Other least squares problems have more than two unknowns. Fitting by the best parabola has n = 3 coefficients C, D, E (see below). In general we are fitting m data points by *n* parameters x1, ... , *Xn.* The matrix *A* has *n* columns and *n* < *m.* The derivatives of II Ax - bll <sup>2</sup>give *then* equations <sup>A</sup> <sup>T</sup>Ax= A <sup>T</sup>b. **The derivative of a square is linear.** This is why the method of least squares is so popular.

**Example 2** *A* has *orthogonal columns* when the measurement times ti add to zero.

Suppose *b* = 1, 2, 4 at times *t* = -2, 0, 2. *Those times add to zero.* The columns of *A* have *zero dot product:* (1, 1, 1) is orthogonal to (-2, 0, 2):

| $C + D(-2) = 1$ |    |        | $\begin{bmatrix} 1 & -2 \\ 1 & 0 \\ 1 & 2 \end{bmatrix}$ | $\begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix}$ |
|-----------------|----|--------|----------------------------------------------------------|---------------------------------------------|
| $C + D(0) = 2$  | or | $Ax =$ |                                                          |                                             |
| $C + D(2) = 4$  |    |        |                                                          |                                             |

When the columns of *A* are orthogonal, <sup>A</sup> <sup>T</sup>*A* will be a diagonal matrix:

$$A^T A \widehat{x} = A^T b \quad \text{is} \quad \begin{bmatrix} 3 & 0 \\ 0 & 8 \end{bmatrix} \begin{bmatrix} C \\ D \end{bmatrix} = \begin{bmatrix} 7 \\ 6 \end{bmatrix}. \quad (9)$$

*Main point:* Since <sup>A</sup> <sup>T</sup>*A is diagonal,* we can solve separately for *C* = f and *D* = i. The zeros in <sup>A</sup> <sup>T</sup>*A* are dot products of perpendicular columns in *A.* The diagonal matrix <sup>A</sup> <sup>T</sup>*A,* with entries *m* = 3 and tr + t� + t� = 8, is virtually as good as the identity matrix.

Orthogonal columns are so helpful that it is worth *shifting the times by subtracting the average time t* = ( ti + · · · + tm) / *m.* If the original times were 1, 3, 5 then their average is *t* = 3. The shifted times *T* = t - *t* = t - 3 add up to zero!

| $T_1 = 1 - 3 = -2$ | $A_{\text{new}} = \begin{bmatrix} 1 & T_1 \\ 1 & T_2 \\ 1 & T_3 \end{bmatrix}$ | $A_{\text{new}}^T A_{\text{new}} = \begin{bmatrix} 3 & 0 \\ 0 & 8 \end{bmatrix}$ |
|--------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| $T_2 = 3 - 3 = 0$  |                                                                                |                                                                                  |
| $T_3 = 5 - 3 = 2$  |                                                                                |                                                                                  |

Now *C* and *D* come from the easy equation (9). Then the best straight line uses *C* + *DT* which is C + D(t - t) = C + D(t - 3). Problem 30 even gives a formula for C and D.

That was a perfect example of the "Gram-Schmidt idea" coming in the next section: *Make the columns orthogonal in advance.* Then AJewAnew is diagonal and Xnew is easy.

# **Dependent Columns in** *A:* **What is** *x?*

From the start, this chapter has assumed independent columns in A. Then AT A is invertible. Then A<sup>T</sup>Ax= A<sup>T</sup>b produces the least squares solution to Ax= *b.*

$$\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = b$$

$$Ax = b$$

$$\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \hat{x}_1 \\ \hat{x}_2 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix} = p$$

$$A\hat{x} = p$$

$$Ax = b$$

$$\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = b$$

Which *x* is best if *A* has *dependent columns?* Here is a specific example.

The measurements b1 = 3 and b2 = 1 are at the same time *T* ! A straight line *C* + *Dt* cannot go through both points. I think we are right to project *b* = (3, 1) *top* = (2, 2) in the column space of *A.* That changes the equation Ax = *b* to the equation Ax = *p.* An equation with no solution has become an equation with infinitely many solutions. The problem is that *A* has dependent columns and ( 1, -1) is in its nulls pace.

Which solution *x* should we choose? All the dashed lines in the figure have the same two errors 1 and -1 at time *T.* Those errors ( 1, -1) = *e* = *b* -*p* are as small as possible. But this doesn't tell us which dashed line is best.

My instinct is to go for the horizontal line at height 2. If the equation for the best line is *b* = *C* + *Dt,* then my choice will have <sup>x</sup> <sup>1</sup>= *C* = 2 and <sup>x</sup>2= *D* = 0. But what if the line had been written as *b* = *ct* + *d?* This is equally correct (just reversing *C* and D). Now the horizontal line has <sup>x</sup> <sup>1</sup>= c = 0 and <sup>x</sup>2= *d* = 2. I don't see any way out.

In Section 7.4, the *"pseudoinverse" of* A will choose the **shortest solution to** Ax = p. Here, that shortest solution will be x<sup>+</sup>= (1, 1). This is the particular solution in the row space of *A,* and x<sup>+</sup>has length v'2. (Both solutions x = (2, 0) and (0, 2) have length 2.) We are arbitrarily choosing the nullspace component of the solution x<sup>+</sup>to be zero.

When *A* has independent columns, the nullspace only contains the zero vector and the pseudoinverse is our usual left inverse L = (A<sup>T</sup>A)-1 A<sup>T</sup>. When I write it that way, the pseudoinverse sounds like the best way to choose *x.* 

*Comment* MATLAB experiments with singular matrices produced either **Inf** or **NaN** (Not a Number) or 10<sup>16</sup>(a bad number). There is a warning in every case! I believe that **Inf** and **NaN** and 10<sup>16</sup>come from the possibilities Ox = b and Ox = 0 and 10-<sup>16</sup>x = 1.

Those are three small examples of three big difficulties: singular with no solution, singular with many solutions, and very very close to singular.

### **Fitting by a Parabola**

If we throw a ball, it would be crazy to fit the path by a straight line. A parabola *b* = *C* + *Dt* + *Et2* allows the ball to go up and come down again *(bis* the height at time t). The actual path is not a perfect parabola, but the whole theory of projectiles starts with that approximation.

When Galileo dropped a stone from the Leaning Tower of Pisa, it accelerated. The distance contains a quadratic term ½gt<sup>2</sup> . (Galileo's point was that the stone's mass is not involved.) Without that t <sup>2</sup>term we could never send a satellite into its orbit. But even with a nonlinear function like t , the unknowns *C, D, E* still appear linearly! Fitting points by the best parabola is still a problem in linear algebra.

**Problem** Fit heights b1, ... , *bm* at times t1, ... , *tm* by a parabola *C* + *Dt* + *Et<sup>2</sup> •* 

**Solution** With *m* > 3 points, the *m* equations for an exact fit are generally unsolvable:

$$\begin{aligned} C + Dt_1 + Et_1^2 &= b_1 \\ \vdots & \\ C + Dt_m + Et_m^2 &= b_m \end{aligned} \quad \text{is } A\mathbf{x} = \mathbf{b} \text{ with } m \text{ by 3 matrix} \quad A = \begin{bmatrix} 1 & t_1 & t_1^2 \\ \vdots & \vdots & \vdots \\ 1 & t_m & t_m^2 \end{bmatrix}. \quad (10)$$

**Least squares** The closest parabola *C* + *Dt* + *Et2* chooses x = ( *C, D, E)* to satisfy the three normal equations A <sup>T</sup>Ax = A<sup>T</sup> b.

May I ask you to convert this to a problem of projection? The column space of *A* has dimension \_\_ . The projection of b is *p* = Ax, which combines the three columns using the coefficients *C, D, E.* The error at the first data point is e <sup>1</sup>= b<sup>1</sup>- *C* - *Dti* - *Etr.* The total squared error is er + \_\_ . If you prefer to minimize by calculus, take the partial derivatives of *E* with respect to \_\_ , \_\_ , \_\_ . These three derivatives will be zero when x = ( C, D, E) solves the 3 by 3 system of equations AT Ax = AT b.

Section 10.5 has more least squares applications. The big one is Fourier seriesapproximating functions instead of vectors. The function to be minimized changes from a sum of squared errors er + ... + *e�* to an integral of the squared error.

**Example 3** For a parabola *b* = *C* + *Dt* + *Et2* to go through the three heights *b* = 6, 0, 0 when *t* = 0, 1, 2, the equations for *C, D, E* are

$$\begin{aligned} C + D \cdot 0 + E \cdot 0^2 &= 6 \\ C + D \cdot 1 + E \cdot 1^2 &= 0 \\ C + D \cdot 2 + E \cdot 2^2 &= 0. \end{aligned} \tag{11}$$

This is *Ax* = *b.* We can solve it exactly. Three data points give three equations and a square matrix. The solution is *x* = *(C, D, E)* = (6, -9, 3). The parabola through the three points in Figure 4.8a is *b* = 6 - 9t + 3t**<sup>2</sup> .** 

What does this mean for projection? The matrix has three columns, which span the whole space R **.** The projection matrix is the identity. The projection of *b* is *b.* The error is zero. We didn't need A <sup>T</sup>Ax = A<sup>T</sup> b, because we solved Ax = *b.* Of course we could multiply by A<sup>T</sup>, but there is no reason to do it.

Figure 4.8 also shows a fourth point *b4* at time *<sup>t</sup>4.* If that falls on the parabola, the new Ax = *b* (four equations) is still solvable. When the fourth point is not on the parabola, we tum to A <sup>T</sup>Ax = A<sup>T</sup> b. Will the least squares parabola stay the same, with all the error at the fourth point? Not likely!

Least squares balances the four errors to get three equations for *C, D, E.* 

![](images/_page_236_Figure_5.jpeg)

Figure 4.8: An exact fit of the parabola at *t* = 0, 1, 2 means that p = b and *e* = 0. The fourth point @ off the parabola makes *m* > *n* and we need least squares: project *b* on *C (A).* The figure on the right shows b-not a combination of the three columns of *A.* 

#### **• REVIEW OF THE KEY IDEAS •**

- 1. The least squares solution x minimizes 11 Ax b 112 = x <sup>T</sup> A <sup>T</sup>Ax - 2x <sup>T</sup> A <sup>T</sup>*b* + *b* <sup>T</sup>
  - b. This is *E,* the sum of squares of the errors in the *m* equations ( *m* > *n).*
- 2. The best x comes from the normal equations A <sup>T</sup>Ax = A <sup>T</sup>*b.* E is a minimum.
- 3. To fit *m* points by a line *b* = *C* + *Dt,* the normal equations give *C* and *D.*
- 4. The heights of the best line are p = (p1, ... , *Pm).* The vertical distances to the data points are the errors e = (e1, ... , em), A key equation is A <sup>T</sup> e = 0.
- 5. If we try to fit *m* points by a combination of *n* < *m* functions, the *m* equations Ax = b are generally unsolvable. Then equations A <sup>T</sup>Ax = A<sup>T</sup> b give the least squares solution-the combination with smallest MSE (mean square error).

#### **• WORKED EXAMPLES •**

**4.3 A** Start with nine measurements b1 to *<sup>b</sup><sup>9</sup> , all zero,* at times t = 1, ... , 9. The tenth measurement b10 = 40 is an outlier. Find the **best horizontal line** y = *C* to fit the ten points (1, 0), (2, 0), ... , (9, 0), (10, 40) using three options for the error E:

(1) Least *squares* E2 = ef + · · · + ef0(then the normal equation for *C* is linear) **(2)** Least *maximum* error *<sup>E</sup>00* = lemaxl **(3)** Least *sum* of errors E1 = le1I + · · · + le1ol-

**Solution** (1) The least squares fit to 0, 0, ... , 0, 40 by a horizontal line is *C* <sup>=</sup>4:

| $A = \text{column of } 1^{\text{th}}$ | $A^T A = 10$ | $A^T b = \text{sum of } b_i = 40.$ | $\text{So } 10 C = 40.$ |
|---------------------------------------|--------------|------------------------------------|-------------------------|
|---------------------------------------|--------------|------------------------------------|-------------------------|

(2) The least maximum error requires *C* <sup>=</sup>20, halfway between O and 40.

(3) The least sum requires *C* <sup>=</sup>0 (!!).The sum of errors 9ICI + 140 - Cl would increase if *C* moves up from zero.

The least sum comes from the *median* measurement (the median of 0, ... , 0, 40 is zero). Many statisticians feel that the least squares solution is too heavily influenced by outliers like b1o = 40, and they prefer least sum. But the equations become *nonlinear.* 

Now find the least squares line *C* + *Dt* through those ten points (1, 0) to (10, 40):

$$A^T A = \begin{bmatrix} 10 & \sum t_i^2 \\ \sum t_i & \sum t_i^2 \end{bmatrix} = \begin{bmatrix} 10 & 55 \\ 55 & 385 \end{bmatrix} \quad A^T \mathbf{b} = \begin{bmatrix} \sum b_i \\ \sum t_i b_i \end{bmatrix} = \begin{bmatrix} 40 \\ 400 \end{bmatrix}$$

Those come from equation (8). Then *A<sup>T</sup>Ax= A<sup>T</sup> b* gives *C* = -8 and *D* = 24/11.

What happens to *C* and *D* if you multiply b = (0, 0, ... , 40) by 3 and then add 30 to get bnew = (30, 30, ... , 150)? Linearity allows us to rescale *b.* Multiplying *b* by 3 will multiply *C* and *D* by 3. Adding 30 to all *bi*will add 30 to *C.* 

**4.3 B** Find the parabola *C* + *Dt* + *Et<sup>2</sup>*that comes closest (least squares error) to the values b = (0, 0, 1, 0, 0) at the times *t* = -2, -1, 0, 1, 2. First write down the five equations *Ax* = bin three unknowns *x* = ( *C, D, E)* for a parabola to go through the five points. No solution because no such parabola exists. Solve *A<sup>T</sup>Ax* = *A<sup>T</sup>b.*

I would predict *D* = 0. Why should the best parabola be symmetric around *t* = O? In *A<sup>T</sup>Ax* = *A<sup>T</sup>b,* equation 2 for *D* should uncouple from equations 1 and 3.

**Solution** The five equations *Ax* = *b* have a rectangular *Vandermonde matrix* A:

$$\begin{array}{lll} C + D & (-2)^2 = 0 & A = \begin{bmatrix} 1 & -2 & 4 \\ C + D & (-1)^2 = 0 & \\ C + D & (0)^2 = 1 & \\ C + D & (1)^2 = 0 & \\ C + D & (2)^2 = 0 & \end{bmatrix} \\ C + D & (-1)^2 = 0 & A = \begin{bmatrix} 5 & 0 & 10 \\ 0 & 10 & 0 \\ 10 & 0 & 34 \end{bmatrix} \end{array}$$

Those zeros in *A<sup>T</sup>A* mean that column 2 of *A* is orthogonal to columns 1 and 3. We see this directly in *A* (the times -2, -1, 0, 1, 2 are symmetric). The best *C, D, E* in the parabola *C* + *Dt* + *Et<sup>2</sup>*come from *A<sup>T</sup>Ax= A<sup>T</sup> b,* and Dis uncoupled from *C* and E:

| $\begin{bmatrix} 5 & 0 & 10 & 0 \\ 0 & 10 & 0 & 0 \\ 10 & 0 & 34 & 0 \end{bmatrix} \begin{bmatrix} C \\ D \\ E \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ | leads to | $C = 34/70$          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------|
|                                                                                                                                                                           |          | $D = 0$ as predicted |
|                                                                                                                                                                           |          | $E = -10/70$         |

### **Problem Set 4.3**

**Problems 1-11 use four data points** *<sup>b</sup>*= (0, 8, 8, 20) **to bring out the key ideas.**

![](images/_page_238_Figure_6.jpeg)

![](images/_page_238_Diagram_7.jpeg)

Figure 4.9: **Problems 1-11:** The closest line *C* + *Dt* matches *Ca1*<sup>+</sup>*Da2* in **<sup>R</sup> 4**

1 With b = 0, 8, 8, 20 at *t* = 0, 1, 3, 4, set up and solve the normal equations *A<sup>T</sup>Ax* = *A<sup>T</sup> b.* For the best straight line in Figure 4.9a, find its four heights *Pi* and four errors *ei.* What is the minimum value *E* = ei + *e�* + *e�* + *e�?*  **<sup>2</sup>**(Line *C* + *Dt* does go through p's) With *b* = 0, 8, 8, 20 at times *t* = 0, 1, 3, 4, write down the four equations Ax = *b* (unsolvable). Change the measurements to *<sup>p</sup>*= 1, 5, 13, 17 and find an exact solution to *Ax* = *p.*  **<sup>3</sup>**Check that *e* = *b* - *<sup>p</sup>*= ( -1, 3, -5, 3) is perpendicular to both columns of the same matrix *A.* What is the shortest distance llell from *b* to the column space of *A?*  4 (By calculus) Write down E = II Ax - bll <sup>2</sup>as a sum of four squares-the last one is (C + *4D -* 20)<sup>2</sup> . Find the derivative equations *8E/8C* = 0 and *8E/8D* = 0. Divide by 2 to obtain the normal equations *A <sup>T</sup>Ax= A <sup>T</sup>b.*  **<sup>5</sup>**Find the height *C* of the best *horizantal line* to fit *b* = (0, 8, 8, 20). An exact fit would solve the unsolvable equations *C* = 0, *C* = 8, *C* = 8, *C* = 20. Find the 4 by 1 matrix *A* in these equations and solve *A<sup>T</sup>Ax* = *A<sup>T</sup> b.* Draw the horizontal line at height x = *C* and the four errors in e.

- 6 Project *b* = (0, 8, 8, 20) onto the line through *a* = (1, 1, 1, 1). Find x = *a Tb/ a Ta*  and the projection *p* = *xa.* Check that *e* = b - *p* is perpendicular to *a,* and find the shortest distance llell from b to the line through *a.* 7 Find the closest line *b* = *Dt, through the origin,* to the same four points. An exact fit would solve *D* · 0 = 0, *D* · l = 8, *D* · 3 = 8, *D* · 4 = 20. Find the 4 by 1 matrix and solve *A<sup>T</sup>Ax= A<sup>T</sup>b.* Redraw Figure 4.9a showing the best line *b* = *Dt* and the e's. 8 Project *b* = (0, 8, 8, 20) onto the line through *a* = (0, 1, 3, 4). Find x = *D* and *p* <sup>=</sup>*xa.* The best *C* in Problems 5-6 and the best Din Problems 7-8 do *not* agree with the best (C, *D)* in Problems 1-4. That is because (1, 1, 1, 1) and (0, 1, 3, 4) are \_\_ perpendicular. 9 For the closest parabola *b* = *C* + *Dt* + *Et<sup>2</sup>*to the same four points, write down the unsolvable equations *Ax* = *b* in three unknowns *x* = ( *C, D, E).* Set up the three normal equations *A <sup>T</sup>Ax* = *A <sup>T</sup>b* (solution not required). In Figure 4.9a you are now fitting a parabola to 4 points-what is happening in Figure 4.9b? 10 For the closest cubic *b* = *C* + *Dt* + *Et<sup>2</sup>*+*Ft3* to the same four points, write down the four equations *Ax* = *b.* Solve them by elimination. In Figure 4.9a this cubic now goes exactly through the points. What are *p* and *e?*  11 The average of the four times is *t* = ¼(O + 1 + 3 + 4) = 2. The average of the four *b's* is b = ¼(O + 8 + 8 + 20) = 9.
  - (a) Verify that the best line goes through the center point (t, b) <sup>=</sup>(2, 9).
  - (b) Explain why *C* + *Dt* = b comes from the first equation in *A<sup>T</sup>Ax* = *A<sup>T</sup>b.*

#### **Questions 12-16 introduce basic ideas of statistics-the foundation for least squares.**

- 12 (Recommended) This problem projects b = ( b1, ... , bm) onto the line through *a* = (1, ... , 1). We solve m equations *ax=* bin 1 unknown (by least squares).
  - (a) Solve *a <sup>T</sup> ax= a <sup>T</sup>b* to show that xis the *mean* (the average) of the *b's.*
  - (b) Find *e* = *b ax* and the *variance* llell<sup>2</sup>and the *standard deviation* llell-
- (c) The horizontal line b = 3 is closest to b = (1, 2, 6). Check that *p* = (3, 3, 3) is perpendicular to *e* and find the 3 by 3 projection matrix *P.* 13 First assumption behind least squares: *Ax* = *b- (noise e with mean zero).* Multiply the error vectors *e* = *b* - *Ax* by *(A<sup>T</sup>A)-<sup>1</sup>A<sup>T</sup>*to get *x* - *x* on the right. The estimation errors *<sup>x</sup>*- *x* also average to zero. The estimate *x* is *unbiased.*  14 Second assumption behind least squares: Them errors *ei* are independent with variance a 2 , so the average of *(b* - *Ax )(b* - *Ax* ) <sup>T</sup>is a <sup>2</sup>*I.* Multiply on the left by *(A<sup>T</sup>*A)-<sup>1</sup>*A<sup>T</sup>*and on the right by *A(A<sup>T</sup>*A)-<sup>1</sup>to show that the average matrix *(x* - *x) (x* - *x)* <sup>T</sup>is *a <sup>2</sup>*( *A<sup>T</sup>A* )-<sup>1</sup> . This is the *covariance matrix* Win Section 10.2.

15 A doctor takes 4 readings of your heart rate. The best solution to *x* **=** b1, ... , *x* **=** *b4*  is the average x of b1, ... , *b4.* The matrix *A* is a column of 1 's. Problem 14 gives the expected error (x - x)2 as 0" 2(AT A)- 1 **= \_\_ .** *By averaging, the vmiance drops from* 0" <sup>2</sup>*to* 0" <sup>2</sup>/ 4. 16 If you know the average x*9* of 9 numbers b1, ... , *b<sup>9</sup> ,* how can you quickly find the average x*10* with one more number b10 ? The idea of *recursive* least squares is to avoid adding 10 numbers. What number multiplies *<sup>x</sup>9* in computing *<sup>x</sup>10*?

$$\widehat{x}_{10} = \frac{1}{10}b_{10} + \dots - \widehat{x}_9 = \frac{1}{10}(b_1 + \dots + b_{10})$$
 as in Worked Example 4.2 C.

Questions 17-24 give more practice with x and *p* and *e.*

17 Write down three equations for the line *b* **=** *C* + *Dt* to go through *b* **=** 7 at *t* **=** -1, *b* **=** 7 at *t* **=** l, and *b* **=** 21 at *t* **=** 2. Find the least squares solution x **=** (C, *D)* and draw the closest line. 18 Find the projection *p* **=** *Ax* in Problem 17. This gives the three heights of the closest line. Show that the error vector ise **=** (2, -6, 4). Why is *Pe=* O? 19 Suppose the measurements at *<sup>t</sup>*= -1, 1, 2 are the errors 2, -6, 4 in Problem 18. Compute *x* and the closest line to these new measurements. Explain the answer: *b* <sup>=</sup>(2, -6, 4) is perpendicular to \_\_ sothe projection is *p* <sup>=</sup>0. 20 Suppose the measurements at *t* = -1, 1, 2 are b = ( 5, 13, 17). Compute *x* and the closest line and *e.* The error is *e* **<sup>=</sup>**0 because this b is 21 Which of the four subspaces contains the error vector *e?* Which contains *p?* Which contains *x?* What is the nullspace of *A?* 22 Find the best line *C* + *Dt* to fit *b* <sup>=</sup>4, 2, -1, 0, 0 at times *t* <sup>=</sup>-2, -1, 0, 1, 2. 23 Is the error vector *e* orthogonal to *b* or *pore* or *x?* Show that llell <sup>2</sup>equals *<sup>e</sup> <sup>T</sup> b* which equals *b T b* - *p <sup>T</sup> b.* This is the smallest total error *E.* 24 The partial derivatives of 11Axll <sup>2</sup>with respect to x1, ... , *Xn* fill the vector 2A<sup>T</sup>*Ax.* The derivatives of 2b <sup>T</sup>*Ax* fill the vector *2A<sup>T</sup> b.* So the derivatives of IIAx - bll <sup>2</sup>are zero when

### **Challenge Problems**

25 *What condition on* ( t1, b1), ( t<sup>2</sup> , b2), ( t3, b3) *puts those three points onto a straight line?* A column space answer is: (b<sup>1</sup> , b<sup>2</sup> , b<sup>3</sup> ) must be a combination of (1, 1, 1) and ( t1, t2, t3). Try to reach a specific equation connecting the t's and *b's.* I should have thought of this question sooner!

26 Find the *plane* that gives the best fit to the 4 values *b* = (0, 1, 3, 4) at the corners (1, 0) and (0, 1) and (-1, 0) and (0, -1) of a square. The equations *C* + *Dx+ Ey* <sup>=</sup> *b* at those 4 points are *Ax* = *b* with 3 unknowns *x* = ( *C, D, E).* What is *A?*  At the center (0, 0) of the square, show that *C* + *Dx* + *Ey* = average of the b's. 27 (Distance between lines) The points *P* = *(x, x, x)* and *Q* = *(y, 3y,* -1) are on two lines in space that don't meet. Choose x and y to minimize the squared distance 11 P - Q 11 <sup>2</sup> . The line connecting the closest P and Q is perpendicular to \_\_ . 28 Suppose the columns of *A* are not independent. How could you find a matrix *B* so that *P* = *B* ( *B<sup>T</sup>B* )-1 *B <sup>T</sup>*does give the projection onto the column space of *A?* (The usual formula will fail when *A<sup>T</sup>A* is not invertible.) 29 Usually there will be exactly one hyperplane in *R <sup>n</sup>*that contains the n given points *<sup>x</sup>*= 0, a**1, ... ,** *an-l·* (Example for n = 3: There will be one plane containing 0, a1, a*2*unless \_\_ .) What is the test to have exactly one plane in *R n ?*  30 Example 2 shifted the times *ti* to make them add to zero. We subtracted away the average time *t* = (t1+ · · · + *tm)/m* to get *<sup>T</sup>i<sup>=</sup>ti* - *t.* Those *Ti* add to zero. With the columns (1, ... , 1) and (T1, ... , *Tm)* now orthogonal, *A<sup>T</sup>A* is diagonal. Its entries are *m* and *T'f* + · · · + *T�.* Show that the best *C* and *D* have direct formulas:

$$T \text{ is } t - \hat{t} \quad C = \frac{b_1 + \dots + b_m}{m} \quad \text{and} \quad D = \frac{b_1 T_1 + \dots + b_m T_m}{T_1^2 + \dots + T_m^2}.$$

*The best line is C* + *DT or C* + *D* ( *t* - *t).* The time shift that makes *A<sup>T</sup>A* diagonal is an example of the Gram-Schmidt process: *orthogonalize the columns of A in advance.* 

# **4.4 Orthonormal Bases and Gram-Schmidt**

1 Th 1 h l . f T { <sup>0</sup> 1 £ f o <sup>r</sup>i\_ # J\_ }· Then I *Q<sup>T</sup>Q*- e co umns q1, ... , *<sup>q</sup>n* are ort onorma 1 <sup>q</sup> - *I.* I <sup>i</sup> % = or . . i = J 2 If *Q* is also square, then *QQ<sup>T</sup>*=*<sup>I</sup>*and I *<sup>Q</sup><sup>T</sup>*=Q- 1 I- *<sup>Q</sup>*is an "orthogonal matrix". 3 The least squares solution to *Qx* = bis *<sup>x</sup>*= *QTb.* Projection of b: *<sup>p</sup>*= *QQTb* = *Pb.*  **<sup>4</sup>**The **Gram-Schmidt** process takes independent ai to orthonormal q<sup>i</sup> . Start with q**1** =ai/ I la1II-5 qi is (ai - projection pi)/ llai -pill; projection Pi<sup>=</sup>(a'fq<sup>1</sup> )q1+ · · · + (a'fqi\_<sup>1</sup> )qi-l· 6 Each ai will be a combination of q1 to q<sup>i</sup> . Then *<sup>A</sup>*= *QR:* orthogonal *Q* and triangular *R.*

This section has two goals, **why** and **how.** The first is to see why orthogonality is good. Dot products are zero, so A <sup>T</sup>A will be diagonal. It becomes so easy to find x and p = Ax. *The second goal is to construct orthogonal vectors.* You will see how Gram-Schmidt chooses combinations of the original basis vectors to produce right angles. Those original vectors are the columns of *A,* probably *not* orthogonal. *The orthonormal basis vectors will be the columns of a new matrix Q.* 

From Chapter 3, a basis consists of independent vectors that span the space. The basis vectors could meet at any angle (except 0 ° and 180 ° ). But every time we visualize axes, they are perpendicular. *In our imagination, the coordinate axes are practically always orthogonal.* This simplifies the picture and it greatly simplifies the computations.

The vectors q1 , ... , qn are *orthogonal* when their dot products qi · % are zero. More exactly *q'f* % = 0 whenever i # j. With one more step-just *divide each vector by its length-the* vectors become *orthogonal unit vectors.* Their lengths are all 1 (normal). Then the basis is called *orthonormal.*

**DEFINITION** The vectors q1 , ... , *qn* are *orthonormal* if

$$q_i^\top q_j = \begin{cases} 0 & \text{when } i \neq j & (\text{orthogonal vectors}) \\ 1 & \text{when } i = j & (\text{unit vectors: } \|q_i\| = 1) \end{cases}$$

A matrix with orthonormal columns is assigned the special letter *Q.* 

*The matrix* Q *is easy to work with because* QT Q = I. This repeats in matrix language that the columns q<sup>1</sup> , ... , *qn* are orthonormal. *Q* is not required to be square.

*A matrix Q with orthonormal columns satisfies*  QTQ =I:

$$Q^T Q = \begin{bmatrix} -q_1^T - \\ -q_2^T - \\ -q_n^T - \end{bmatrix} \begin{bmatrix} | & | & | \\ q_1 & q_2 & q_n \end{bmatrix} = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix} = I. \quad (1)$$

When row i of Q<sup>T</sup>multiplies column j of Q, the dot product is *q;* q<sup>j</sup> . Off the diagonal ( i -=/- *j)* that dot product is zero by orthogonality. On the diagonal ( i = *j)* the unit vectors give q; qi= llq<sup>i</sup> ll <sup>2</sup>= 1. Often *Q* is rectangular (m > *n).* Sometimes *m* = *n.*

*When Q is square, Q <sup>T</sup>Q* = *I means that Q <sup>T</sup>= Q-***<sup>1</sup> .-** *transpose= inverse.*

If the columns are only orthogonal (not unit vectors) , dot products still give a diagonal matrix (not the identity matrix). This diagonal matrix is almost as good as *I.* The important thing is orthogonality-then it is easy to produce unit vectors.

*To repeat: QT Q* = *I* even when *Q* is rectangular. In that case *QT* is only an inverse from the left. For square matrices we also have *QQ<sup>T</sup>*=*I,* so *QT* is the two-sided inverse of *Q.* The rows of a square Qare orthonormal like the columns. *The inverse is the transpose.* In this square case we call *Q* an *orthogonal matrix. <sup>1</sup>*

Here are three examples of orthogonal matrices-rotation and permutation and reflection. The quickest test is to check *QTQ* = *I.*

**Example 1 (Rotation)** *<sup>Q</sup>*rotates every vector in the plane by the angle 0:

$$Q = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \text{ and } Q^T = Q^{-1} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}.$$

The columns of *Q* are orthogonal (take their dot product). They are unit vectors because <sup>s</sup>in2 0 + co<sup>s</sup> <sup>2</sup>0 = 1. Those columns give an *orthonormal basis* for the plane R **.** 

The standard basis vectors i and j are rotated through *0* (see Figure 4.10a). Q-<sup>1</sup>rotates vectors back through *-0.* It agrees with Q<sup>T</sup> , because the cosine of *-0* equals the cosine of *0,* and sin(-0) = - <sup>s</sup>in *0.* We have *QTQ* = *I* and *QQ<sup>T</sup>*=*I.*

**Example 2 (Permutation)** These matrices change the order to *(y, z, x)* and *(y,* x):

$$\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} y \\ z \\ x \end{bmatrix} \quad \text{and} \quad \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} y \\ x \end{bmatrix}.$$

All columns of these Q's are unit vectors (their lengths are obviously 1). They are also orthogonal (the 1 's appear in different places). *The inverse of a permutation matrix* is *its transpose: Q-1* = *QT.* The inverse puts the components back into their original order:

<sup>1 &</sup>quot;Orthonormal matrix" would have been a better name for *Q,* but it's not used. Any matrix with orthonormal columns has the letter *Q.* But we only call it an **orthogonal matrix** when it is square.

| Inverse = transpose: | $\begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ | $\begin{bmatrix} y \\ z \\ x \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ | and | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} y \\ x \end{bmatrix} = \begin{bmatrix} x \\ y \end{bmatrix}$ |
|----------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------|
|----------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------|

#### *Every permutation matrix is an orthogonal matrix.*

**Example 3 (Reflection)** If u is any unit vector, set Q = *I* -2uu T. Notice that uu Tis a matrix while u <sup>T</sup> u is the number llull2 = 1. Then QT and Q-1 both equal Q:

| $Q^T = I - 2uu^T = Q$ | and | $Q^T Q = I - 4uu^T + 4uu^T uu^T = I$ | (2) |
|-----------------------|-----|--------------------------------------|-----|
|                       |     |                                      |     |

Reflection matrices *I* -2uu T are symmetric and also orthogonal. If you square them, you get the identity matrix: Q2 = QT Q = I. Reflecting twice through a mirror brings back the original, like ( -1 ) <sup>2</sup>= 1. Notice u <sup>T</sup> u = l inside 4uu T uu T in equation (2).

*j <sup>0</sup>*<sup>s</sup>m<sup>0</sup> *Qi= j u*  Reflect ,' )" mirror Qj = [-:�::] �i <sup>=</sup> [ c?s0 ] Rotate by *<sup>0</sup> <sup>0</sup>*. <sup>I</sup>uto-u ----- Qj = i

Figure 4.10: Rotation by 
$$Q = \begin{bmatrix} C & -s \\ 0 & C \end{bmatrix}$$
 and reflection across  $45^\circ$  by  $Q = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ .

As example choose the direction u = (-l/ v12, 1/ v12). Compute 2uu T (column times row) and subtract from *I* to get the reflection matrix Qin the direction of *u:*

| Reflection | $Q = I - 2 \begin{bmatrix} .5 & -.5 \\ -.5 & .5 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ | and | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} y \\ x \end{bmatrix}$ |
|------------|---------------------------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------|
|            |                                                                                                               |     |                                                                                                                            |

When *(x,* y) goes to *(y,* x), a vector like (3, 3) doesn't move. It is on the mirror line.

Rotations preserve the length of every vector. So do reflections. So do permutations. So does multiplication by any orthogonal matrix *Q-lengths and angles don't change.*

**Proof** 11Qxll2 equals llxll2 because (Qx)<sup>T</sup> (Qx) = xTQTQx = xTJx = x<sup>T</sup> x.

# *If Q has orthonormal columns* ( Q<sup>T</sup>*Q* = *I), it leaves lengths unchanged:*

| Same length for $Qx$ | $\ Qx\  = \ x\ $ for every vector $x$ . | (3) |
|----------------------|-----------------------------------------|-----|
|                      |                                         |     |

$$Q$$
 also preserves dot products:  $(Qx)^T(Qy) = x^TQ^TQy = x^Ty$ . Just use  $Q^TQ = I$ .

# **Projections Using Orthonormal Bases:** Q **Replaces** A

Orthogonal matrices are excellent for computations-numbers can never grow too large when lengths of vectors are fixed. Stable computer codes use *Q's* as much as possible.

For projections onto subspaces, all formulas involve *A <sup>T</sup>A.* The entries of *A <sup>T</sup>A* are the dot products *a; a*1 of the basis vectors a1, ... , *an.* 

**Suppose the basis vectors are actually orthonormal.** *Thea's* become the *q's.* Then *A <sup>T</sup>A simplifies to QTQ* = *I.* Look at the improvements in *x* and *p* and *P.* Instead of *QT Q* we print a blank for the identity matrix:

| — | $\hat{x} = Q^T b$ | and | $p = Q \hat{x}$ | and | $P = Q - \underline{Q}^T$ . | (4) |
|---|-------------------|-----|-----------------|-----|-----------------------------|-----|
|---|-------------------|-----|-----------------|-----|-----------------------------|-----|

### *The least squares solution of Qx* = *bis <sup>x</sup>*= *Q<sup>T</sup> b. The projection matrix is QQ<sup>T</sup> .*

There are no matrices to invert. This is the point of an orthonormal basis. The best *x* = *Q<sup>T</sup> b* just has dot products of q**<sup>1</sup> , ...** *,qn*with *b.* We have !-dimensional projections! The "coupling matrix" or "correlation matrix" *A <sup>T</sup>A* is now *QTQ* = *I.* There is no coupling. When *A* is *Q,* with orthonormal columns, here is *p* = *Qx* = *QQ<sup>T</sup> b:* 

$$p = \begin{bmatrix} | & & | \\ q_1 & \cdots & q_n \\ | & & | \end{bmatrix} \begin{bmatrix} q_1^T b \\ \vdots \\ q_n^T b \end{bmatrix} = q_1(q_1^T b) + \cdots + q_n(q_n^T b). \quad (5)$$

**Important case:** When *Q* is square and *m* = *n,* the subspace is the whole space. Then *QT* = Q-1 and *x* = *Q<sup>T</sup> b* is the same as x = *Q-1b.* The solution is exact! The projection of *b* onto the whole space is *b* itself. In this case *p* = band *P* = *QQT* = *I.*

You may think that projection onto the whole space is not worth mentioning. But when *<sup>p</sup>*= *b,* our formula assembles *b* out of its 1-dimensional projections. If q**<sup>1</sup> ,** ... , *qn*is an orthonormal basis for the whole space, then *Q* is square. Every b = *QQ<sup>T</sup> b is the sum of its components along the* q's:

$$b = q_1(q_1^T b) + q_2(q_2^T b) + \cdots + q_n(q_n^T b). \quad (6)$$

**Transforms** *QQT* = *I* is the foundation of Fourier series and all the great "transforms" of applied mathematics. They break vectors *b* or functions *f* ( *x)* into perpendicular pieces. Then by adding the pieces in (6), the inverse transform puts *band f(x)* back together.

**Example 4** The columns of this orthogonal Qare orthonormal vectors q<sup>1</sup> , q<sup>2</sup> , q3 :

| $m = n = 3$ | $Q = \frac{1}{3} \begin{bmatrix} -1 & 2 & 2 \\ 2 & -1 & 2 \\ 2 & 2 & -1 \end{bmatrix}$ | has | $Q^T Q = Q Q^T = I$ . |
|-------------|----------------------------------------------------------------------------------------|-----|-----------------------|
|-------------|----------------------------------------------------------------------------------------|-----|-----------------------|

The separate projections of *b* = (0, 0, 1) onto q1 and q2 and <1:3 are p1 and p2 and *p<sup>3</sup>*

| $q_1(q_1^T b) = \frac{2}{3} q_1$ | and | $q_2(q_2^T b) = \frac{2}{3} q_2$ | and | $q_3(q_3^T b) = -\frac{1}{3} q_3$ |
|----------------------------------|-----|----------------------------------|-----|-----------------------------------|
|                                  |     |                                  |     |                                   |

The sum of the first two is the projection of *b* onto the *plane* of q1 and q<sup>2</sup> . The sum of all three is the projection of *b* onto the *whole* space-which is p1<sup>+</sup>p2<sup>+</sup>*p3*= *b* itself:

| <b>Reconstruct <math display="block">b</math></b> | $\frac{2}{3}q_1 + \frac{2}{3}q_2 - \frac{1}{3}q_3 = \frac{1}{9}$ | $\begin{bmatrix} -2 + 4 - 2 \\ 4 - 2 - 2 \\ 4 + 4 + 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = b.$ |
|---------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| $b = p_1 + p_2 + p_3$                             |                                                                  |                                                                                                                       |

#### **The Gram-Schmidt Process**

The point of this section is that "orthogonal is good". Projections and least squares always involve **A <sup>T</sup>***A.* When this matrix becomes **Q <sup>T</sup>Q** = *I,* the inverse is no problem. The one-dimensional projections are uncoupled. The best *x* is **Q T b** (just *n* separate dot products). For this to be true, we had to say *"If* the vectors are orthonormal". *Now we explain the "Gram-Schmidt way" to create orthonormal vectors.* 

Start with three independent vectors *a, b,* c. We intend to construct three orthogonal vectors *A, B, C.* Then (at the end may be easiest) we divide *A, B, C* by their lengths. That produces three orthonormal vectors q1<sup>=</sup>A/IIAII, q2<sup>=</sup>B/IIBII, *q3*<sup>=</sup>*C* /IICII-

**Gram-Schmidt** Begin by choosing *<sup>A</sup>*=*a.* This first direction is accepted as it comes. The next direction *B* must be perpendicular to *A. Start with b and subtract its projection along A.* This leaves the perpendicular part, which is the orthogonal vector *B:*

| First Gram-Schmidt step | $B = b - \frac{A^T b}{A^T A} A.$ | (7) |
|-------------------------|----------------------------------|-----|
|-------------------------|----------------------------------|-----|

A and *B* are orthogonal in Figure 4.11. Multiply equation (7) by AT to verify that A<sup>T</sup>*B*= A<sup>T</sup>*b*- A<sup>T</sup>*b* = 0. This vector *B* is what we have called the error vector *e,* perpendicular to *A.* Notice that B in equation (7) is not zero (otherwise *a* and *b* would be dependent). The directions *A* and *B* are now set.

The third direction starts with c. This is not a combination of *A* and *B* (because *c* is not a combination of *a* and *b).* But most likely *c* is not perpendicular to *A* and *B.* So subtract off its components in those two directions to get a perpendicular direction *C:*

| Next Gram-Schmidt step | $C = c - \frac{A^T c}{A^T A} A - \frac{B^T c}{B^T B} B.$ | (8) |
|------------------------|----------------------------------------------------------|-----|
|------------------------|----------------------------------------------------------|-----|

This is the one and only idea of the Gram-Schmidt process. *Subtract from every new vector its projections in the directions already set.* That idea is repeated at every step.<sup>2</sup> If we had a fourth vector *d,* we would subtract three projections onto *A, B, C* to get *D.*

<sup>2</sup> 1 think Gram had the idea. I don't really know where Schmidt came in.

![](images/_page_247_Diagram_2.jpeg)

Figure 4.11: First project *b* onto the line through *a* and find the orthogonal *B* as *b* - *p.*  Then project c onto the *AB* plane and find *C* as *c* - *p.* Divide by IIAII, IIBII, IICII-

At the end, *or immediately when each one* is *found,* divide the orthogonal vectors *A, B, C, D* by their lengths. The resulting vectors q<sup>1</sup> , *q2,* q<sup>3</sup> , *q4*are orthonormal.

Example of Gram-Schmidt Suppose the independent non-orthogonal vectors *a, b,* c are

| $a = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$ | and | $b = \begin{bmatrix} 2 \\ 0 \\ -2 \end{bmatrix}$ | and | $c = \begin{bmatrix} 3 \\ -3 \\ 3 \end{bmatrix}$ |
|--------------------------------------------------|-----|--------------------------------------------------|-----|--------------------------------------------------|
|--------------------------------------------------|-----|--------------------------------------------------|-----|--------------------------------------------------|

Then A = *a* has A <sup>T</sup>A = 2 and A<sup>T</sup>*b* = 2. Subtract from *b* its projection p along A:

| First step | $B = b - \frac{A^T b}{A^T A} A = b - \frac{2}{2} A = \begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}$ |
|------------|--------------------------------------------------------------------------------------------------|
|------------|--------------------------------------------------------------------------------------------------|

Check: A <sup>T</sup>B = 0 as required. Now subtract the projections of c on A and B to get C:

| Next step | $C = c - \frac{A^T c}{A^T A} A - \frac{B^T c}{B^T B} B = c - \frac{6}{2} A + \frac{6}{6} B = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|

Check: *C* = (1, 1, 1) is perpendicular to both *A* and *B.* Finally convert *A, B, C* to unit vectors (length 1, orthonormal). The lengths of *A, B, C* are v'2 and v'6 and \/'3. Divide by those lengths, for an orthonormal basis:

$$q_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad \text{and} \quad q_2 = \frac{1}{\sqrt{6}} \begin{bmatrix} 1 \\ -2 \end{bmatrix} \quad \text{and} \quad q_3 = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}.$$

, q*<sup>2</sup> ,* q**3** contain square roots.

### The Factorization $A = QR$

We started with a matrix  $A$ , whose columns were  $a, b, c$ . We ended with a matrix  $Q$ , whose columns are  $q_1, q_2, q_3$ . How are those matrices related? Since the vectors  $a, b, c$  are combinations of the  $q$ 's (and vice versa), there must be a third matrix connecting  $A$  to  $Q$ . This third matrix is the triangular  $R$  in  $A = QR$ .

The first step was  $q_1 = a/\|a\|$  (other vectors not involved). The second step was equation (7), where  $b$  is a combination of  $A$  and  $B$ . At that stage  $C$  and  $q_3$  were not involved. This non-involvement of later vectors is the key point of Gram-Schmidt:

- • The vectors  $a$  and  $A$  and  $q_1$  are all along a single line.
- • The vectors  $a, b$  and  $A, B$  and  $q_1, q_2$  are all in the same plane.
- • The vectors  $a, b, c$  and  $A, B, C$  and  $q_1, q_2, q_3$  are in one subspace (dimension 3).

At every step  $a_1, \dots, a_k$  are combinations of  $q_1, \dots, q_k$ . Later  $q$ 's are not involved. The connecting matrix  $R$  is *triangular*, and we have  $A = QR$ :

$$\begin{bmatrix} a & b & c \end{bmatrix} = \begin{bmatrix} q_1 & q_2 & q_3 \end{bmatrix} \begin{bmatrix} q_1^T a & q_1^T b & q_1^T c \\ q_2^T b & q_2^T c \\ q_3^T c \end{bmatrix} \quad \text{or} \quad A = QR. \quad (9)$$

 $A = QR$  is Gram-Schmidt in a nutshell. Multiply by  $Q^T$  to recognize  $R = Q^T A$  above.

**(Gram-Schmidt)** From independent vectors  $a_1, \dots, a_n$ , Gram-Schmidt constructs orthonormal vectors  $q_1, \dots, q_n$ . The matrices with these columns satisfy  $A = QR$ . Then  $R = Q^T A$  is *upper triangular* because later  $q$ 's are orthogonal to earlier  $a$ 's.

Here are the original  $a$ 's and the final  $q$ 's from the example. The  $i, j$  entry of  $R = Q^T A$  is row  $i$  of  $Q^T$  times column  $j$  of  $A$ . The dot products  $q_i^T a_j$  go into  $R$ . **Then  $A = QR$ :**

$$A = \begin{bmatrix} 1 & 2 & 3 \\ -1 & 0 & -3 \\ 0 & -2 & 3 \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{6} & 1/\sqrt{3} \\ -1/\sqrt{2} & 1/\sqrt{6} & 1/\sqrt{3} \\ 0 & -2/\sqrt{6} & 1/\sqrt{3} \end{bmatrix} \begin{bmatrix} \sqrt{2} & \sqrt{2} & \sqrt{18} \\ 0 & \sqrt{6} & -\sqrt{6} \\ 0 & 0 & \sqrt{3} \end{bmatrix} = QR.$$

Look closely at  $Q$  and  $R$ . The lengths of  $A, B, C$  are  $\sqrt{2}, \sqrt{6}, \sqrt{3}$  on the diagonal of  $R$ . The columns of  $Q$  are orthonormal. Because of the square roots,  $QR$  might look harder than  $LU$ . Both factorizations are absolutely central to calculations in linear algebra.

Any  $m$  by  $n$  matrix  $A$  with independent columns can be factored into  $A = QR$ . The  $m$  by  $n$  matrix  $Q$  has orthonormal columns, and the square matrix  $R$  is upper triangular with positive diagonal. We must not forget why this is useful for least squares:  $A^T A = (QR)^T Q R = R^T Q^T Q R = R^T R$ . The least squares equation  $A^T A \hat{x} = A^T b$  simplifies to  $R^T R \hat{x} = R^T Q^T b$ . Then finally we reach  $R \hat{x} = Q^T b$ : good.

| Least squares | $R^T \hat{x} = R^T Q^b \mathbf{v}$ | or | $\hat{x} = Q^b \mathbf{v}$ | or | $\hat{x} = R^{-1} Q^b \mathbf{v}$ | (10) |
|---------------|------------------------------------|----|----------------------------|----|-----------------------------------|------|
|               |                                    |    |                            |    |                                   |      |

Instead of solving Ax = *b,* which is impossible, we solve *Rx* = Q<sup>T</sup> b by back substitution-which is very fast. The real cost is the mn 2 multiplications in the Gram-Schmidt process, which are needed to construct the orthogonal Q and the triangular R with A = QR.

Below is an informal code. It executes equations (11) for *j* = 1 then *j* = 2 and eventually *<sup>j</sup>*= n. The important lines 4-5 subtract from v = a, its projection onto each q<sup>i</sup> , i < *j.* The last line of that code normalizes v ( divides by r *jj* = 11 v 11) to get the unit vector *q* {

$$r_{kj} = \sum_{i=1}^m q_{ik} v_{ij} \quad \text{and} \quad v_{ij} = v_{ij} - q_{ik} r_{kj} \quad \text{and} \quad r_{jj} = \left( \sum_{i=1}^m v_{ij}^2 \right)^{1/2} \quad \text{and} \quad q_{ij} = \frac{v_{ij}}{r_{jj}}. \quad (11)$$

Starting from a, b, c = a1, a<sup>2</sup> , a3 this code will construct q<sup>1</sup> , then B, q<sup>2</sup> , then C, q<sup>3</sup> :

| $q_1 = a_1/\ a_1\ $          | $B = a_2 - (q_1^T a_2)q_1$ | $q_2 = B/\ B\ $ |
|------------------------------|----------------------------|-----------------|
| $C^* = a_3 - (q_1^T a_3)q_1$ | $C = C^* - (q_2^T C^*)q_2$ | $q_3 = C/\ C\ $ |

Equation (11) subtracts **one projection at a time** as in *C\** and *C.* That change is called *modified Gram-Schmidt.* This code is numerically more stable than equation (8) which subtracts all projections at once.

| for $j = 1:n$                | % <b>modified Gram-Schmidt</b>                             |
|------------------------------|------------------------------------------------------------|
| $v = A(:, j);$               | % $v$ begins as column $j$ of the original $A$             |
| for $i = 1:j-1$              | % columns $q_1$ to $q_{j-1}$ are already settled in $Q$    |
| $R(i, j) = Q(:, i)' * v;$    | % compute $R_{ij} = q_i^T a_j$ which is $q_i^T v$          |
| $v = v - R(i, j) * Q(:, i);$ | % <b>subtract the projection</b> ( $q_i^T v$ ) $q_i$       |
| end                          | % $v$ is now perpendicular to all of $q_1, \dots, q_{j-1}$ |
| $R(j, j) = \text{norm}(v);$  | % the diagonal entries $R_{jj}$ are lengths                |
| $Q(:, j) = v / R(j, j);$     | % divide $v$ by its length to get the next $q_j$           |
| end                          | % the "for $j = 1:n$ loop" produces all of the $q_j$       |

To recover column j of *A,* undo the last step and the middle steps of the code:

$$R(j, j)\mathbf{q}_j = (\mathbf{v} \text{ minus its projections}) = (\text{column } j \text{ of } A) - \sum_{i=1}^{j-1} R(i, j)\mathbf{q}_i. \quad (12)$$

*Confession* Good software like LAPACK, used in good systems like MATLAB and Julia and Python, will not use this Gram-Schmidt code. There is now a better way. "Householder reflections" act on *A* to produce the upper triangular *R.* This happens one column at a time in the same way that elimination produces the upper triangular U in LU.

Those reflection matrices *I* -*2uu* T will be described in Chapter 11 on numerical linear algebra. If *A* is tridiagonal we can simplify even more to use 2 by 2 rotations. The result is always *<sup>A</sup>*<sup>=</sup> *QR* and the MATLAB command to orthogonalize *A* is [Q, R] = qr(A). I believe that Gram-Schmidt is still the good process to understand, even if the reflections or rotations lead to a more perfect *Q.*

#### **• REVIEW OF THE KEY IDEAS •**

- 1. If the orthonormal vectors q<sup>1</sup> , ... , qn are the columns of *Q,* then q; q1<sup>=</sup>0 and *q; qi* = 1 translate into the matrix multiplication *Q<sup>T</sup>Q* = *I.*
- 2. If *Q* is square (an *orthogonal matrix)* then *Q<sup>T</sup> =* Q-<sup>1</sup> : *transpose= inverse.*
- 3. The length of *Qx* equals the length of x: IIQxll = llxll-
- 4. The projection onto the column space of *Q* spanned by the *q's* is *P* = *QQ<sup>T</sup>.*
- 5. If *Q* is square then *P* = *QQ<sup>T</sup>*=*I* and every *b* = q**1** (qlb) + · · · + q<sup>n</sup> (qJb).
- 6. Gram-Schmidt produces orthonormal vectors q<sup>1</sup> , q2 , q3from independent *a, b,* c. In matrix form this is the factorization *A= QR=* (orthogonal Q)(triangular *R).*

#### **• WORKED EXAMPLES •**

**4.4 A** Add two more columns with all entries 1 or -1, so the columns of this 4 by 4 "Hadamard matrix" are orthogonal. How do you turn *H4* into an *orthogonal matrix Q?*

The block matrix *<sup>H</sup>8* = [ ;: \_;:] is the next Hadamard matrix with 1 's and -1 's. What is the product Hl' H <sup>8</sup> ?

$$H_2 = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \quad H_4 = \begin{bmatrix} 1 & 1 & x & x \\ 1 & -1 & x & x \\ 1 & 1 & x & x \\ 1 & -1 & x & x \end{bmatrix} \quad \text{and} \quad Q_4 = \begin{bmatrix} x & x \\ x & x \\ x & x \\ x & x \end{bmatrix}$$

The projection of *b* = (6, 0, 0, 2) onto the first column of *<sup>H</sup>4* is p**1** = (2, 2, 2, 2). The projection onto the second column is p2= ( 1, -1, 1, -1). What is the projection p**1** <sup>2</sup>of *b* onto the 2-dimensional space spanned by the first two columns?

**Solution** *H4* can be built from H <sup>2</sup>just as *Hs* is built from H4:

$$H_4 = \begin{bmatrix} H_2 & H_2 \\ H_2 & -H_2 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{bmatrix} \text{ has orthogonal columns.}$$

Then *Q* = *H* /2 has orthonormal columns. Dividing by 2 gives unit vectors in *Q.* A 5 by 5 Hadamard matrix is impossible because the dot product of columns would have five 1 's and/or -1 's and could not add to zero. *<sup>H</sup>8* has orthogonal columns of length Js.

$$H_8^T H_8 = \begin{bmatrix} H^T & -H^T \\ H^T & -H^T \end{bmatrix} \begin{bmatrix} H & H \\ H & -H \end{bmatrix} = \begin{bmatrix} 2H^T H & 0 \\ 0 & 2H^T H \end{bmatrix} = \begin{bmatrix} 8I & 0 \\ 0 & 8I \end{bmatrix} \cdot Q_8 = \frac{H_8}{\sqrt{8}}$$

**4.4 B What is the key point of orthogonal columns?** Answer: A <sup>T</sup>A is diagonal and easy to invert. **We can project onto lines and just add.** The axes are orthogonal.

**Add** *p's* Projection p**<sup>1</sup> ,2** onto a plane equals p**1**<sup>+</sup>p**2** onto orthogonal lines.

### **Problem Set 4.4**

**Problems 1-12 are about orthogonal vectors and orthogonal matrices.** 

1 Are these pairs of vectors orthonormal or only orthogonal or only independent?

| (a) | $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} -1 \\ 1 \end{bmatrix}$ | (b) | $\begin{bmatrix} .6 \\ .8 \end{bmatrix}$ and $\begin{bmatrix} .4 \\ -.3 \end{bmatrix}$ | (c) | $\begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix}$ and $\begin{bmatrix} -\sin \theta \\ \cos \theta \end{bmatrix}$ |
|-----|------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------|
|     |                                                                                    |     |                                                                                        |     |                                                                                                                            |

Change the second vector when necessary to produce orthonormal vectors.

- **<sup>2</sup>**The vectors (2, 2, -1) and ( -1, 2, 2) are orthogonal. Divide them by their lengths to find orthonormal vectors q**1** and q<sup>2</sup> . Put those into the columns of Q and multiply Q <sup>T</sup>Q andQQ <sup>T</sup> \_ **<sup>3</sup>**(a) If A has three orthogonal columns each of length 4, what is A <sup>T</sup>A?
- (b) If A has three orthogonal columns of lengths 1, 2, 3, what is A <sup>T</sup>A? **<sup>4</sup>**Give an example of each of the following:
  - (a) A matrix Q that has orthonormal columns but QQ <sup>T</sup>=/- I.
  - (b) Two orthogonal vectors that are not linearly independent.
- (c) An orthonormal basis for R **,** including the vector q1 = (1, 1, 1)/v3. **<sup>5</sup>**Find two orthogonal vectors in the plane x + *y* + 2z = 0. Make them orthonormal. **<sup>6</sup>**If Q <sup>1</sup>and Q <sup>2</sup>are orthogonal matrices, show that their product Q <sup>1</sup>Q <sup>2</sup>is also an orthogonal matrix. (Use Q <sup>T</sup>Q = I.)

- 7 If Q has orthonormal columns, what is the least squares solution x to Qx = *b?* 8 If q1 and *q2*are orthonormal vectors in R. , what combination \_\_ q1 + \_\_ *q<sup>2</sup>* is closest to a given vector *b?* 9 (a) Compute *P* = QQT when q1 = (.8, .6, 0) and *<sup>q</sup>*2= (-.6, .8, 0). Verify that *p<sup>2</sup>=P.*
- (b) Prove that always (QQT) 2 = QQT by using QTQ = *I.* Then *P* = QQT is the projection matrix onto the column space of *Q.*  10 Orthonormal vectors are automatically linearly independent.
  - (a) Vector proof: When c<sup>1</sup> q1 +c2q2+c*<sup>3</sup> <sup>q</sup>3*= 0, what dot product leads to c1 = O? Similarly c2 = 0 and c3= 0. Thus the q's are independent.
- (b) Matrix proof: Show that Qx = 0 leads to x = 0. Since Q may be rectangular, you can use QT but not Q� 1 . 11 (a) Gram-Schmidt: Find orthonormal vectors q1 and q2 in the plane spanned by *a=* (1, 3, 4, 5, 7) and b = (-6, 6, 8, 0, 8).
- (b) Which vector in this plane is closest to ( 1, 0, 0, 0, 0)? 12 If a<sup>1</sup> , a2, a*3* is a basis for R <sup>3</sup> , any vector b can be written as or

| $b = x_1a_1 + x_2a_2 + x_3a_3$ | or | $\begin{bmatrix} a_1 & a_2 & a_3 \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = b$ |
|--------------------------------|----|-------------------------------------------------|-------------------------------------------------------|
|--------------------------------|----|-------------------------------------------------|-------------------------------------------------------|

- (a) Suppose the a's are orthonormal. Show that x1 = af b.
- (b) Suppose the a's are orthogonal. Show that x1 = afb/af a<sup>1</sup> .
- (c) If the a's are independent, x1 is the first component of \_\_ times *b.*

**Problems** 13-25 **are about the Gram-Schmidt process and** *A= QR.*

13 What multiple of a = [ i ] should be subtracted from *b* = [ 6] to make the result *<sup>B</sup>* orthogonal to *a?* Sketch a figure to show *a, b,* and *B.*  14 Complete the Gram-Schmidt process in Problem 13 by computing q1 = a/ llall and q2 = B/IIBII and factoring into *QR:*

$$\begin{bmatrix} 1 & 4 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} q_1 & q_2 \end{bmatrix} \begin{bmatrix} \| a \| & ? \\ 0 & \| B \| \end{bmatrix}$$

15 (a) Find orthonormal vectors  $q_1, q_2, q_3$  such that  $q_1, q_2$  span the column space of

$$A = \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ -2 & 4 \end{bmatrix}.$$

(b) Which of the four fundamental subspaces contains  $q_3$ ?

(c) Solve  $Ax = (1, 2, 7)$  by least squares.

16 What multiple of  $a = (4, 5, 2, 2)$  is closest to  $b = (1, 2, 0, 0)$ ? Find orthonormal vectors  $q_1$  and  $q_2$  in the plane of  $a$  and  $b$ .

17 Find the projection of  $b$  onto the line through  $a$ :

$$a = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \quad \text{and} \quad b = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \quad \text{and} \quad p = ? \quad \text{and} \quad e = b - p = ?$$

Compute the orthonormal vectors  $q_1 = a/\|a\|$  and  $q_2 = e/\|e\|$ .

18 (Recommended) Find orthogonal vectors  $A, B, C$  by Gram-Schmidt from  $a, b, c$ :

$$a = (1, -1, 0, 0) \quad b = (0, 1, -1, 0) \quad c = (0, 0, 1, -1).$$

 $A, B, C$  and  $a, b, c$  are bases for the vectors perpendicular to  $d = (1, 1, 1, 1)$ .

19 If  $A = QR$  then  $A^T A = R^T R =$  \_\_\_\_\_ triangular times \_\_\_\_\_ triangular. *Gram-Schmidt on A corresponds to elimination on  $A^T A$ .* The pivots for  $A^T A$  must be the squares of diagonal entries of  $R$ . Find  $Q$  and  $R$  by Gram-Schmidt for this  $A$ :

$$A = \begin{bmatrix} -1 & 1 \\ 2 & 1 \\ 2 & 4 \end{bmatrix} \quad \text{and} \quad A^T A = \begin{bmatrix} 9 & 9 \\ 9 & 18 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 9 & \\ & 9 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}.$$

20 True or false (give an example in either case):

(a)  $Q^{-1}$  is an orthogonal matrix when  $Q$  is an orthogonal matrix.

(b) If  $Q$  (3 by 2) has orthonormal columns then  $\|Qx\|$  always equals  $\|x\|$ .

21 Find an orthonormal basis for the column space of  $A$ :

$$A = \begin{bmatrix} 1 & -2 \\ 1 & 0 \\ 1 & 1 \\ 1 & 3 \end{bmatrix} \quad \text{and} \quad b = \begin{bmatrix} -4 \\ -3 \\ 3 \\ 0 \end{bmatrix}.$$

22 Find orthogonal vectors *A, B, C* by Gram-Schmidt from

| $a = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}$ | and | $b = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$ | and | $c = \begin{bmatrix} 1 \\ 0 \\ 4 \end{bmatrix}$ |
|-------------------------------------------------|-----|--------------------------------------------------|-----|-------------------------------------------------|
|-------------------------------------------------|-----|--------------------------------------------------|-----|-------------------------------------------------|

23 Find q<sup>1</sup> , q2 , *q3* ( orthonormal) as combinations of *a,* b, *c* (independent columns). Then write A as *QR:* 

$$A = \begin{bmatrix} 1 & 2 & 4 \\ 0 & 0 & 5 \\ 0 & 3 & 6 \end{bmatrix}$$

24 (a) Find a basis for the subspace Sin R <sup>4</sup>spanned by all solutions of

$$x_1 + x_2 + x_3 - x_4 = 0.$$

- (b) Find a basis for the orthogonal complement SJ\_ .
- (c) Find b1 in Sand b2 in SJ\_ so that b1<sup>+</sup>b2 = b = (1, 1, 1, 1).

25 **If** *ad* - *be>* 0, the entries in *A= QR* are

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \frac{\begin{bmatrix} a & -c \\ c & a \end{bmatrix} \begin{bmatrix} a^2 + c^2 & ab + cd \\ 0 & ad - bc \end{bmatrix}}{\sqrt{a^2 + c^2}}.$$

Write *A* = *QR* when *a, b,* c, *d* = 2, 1, 1, 1 and also 1, 1, 1, 1. Which entry of *R* becomes zero when the columns are dependent and Gram-Schmidt breaks down?

### Problems **26-29** use the *QR* code in equation (11). **It** executes Gram-Schmidt.

26 Show why *C* (found via *C\** in the steps after (11)) is equal to *C* in equation (8). 27 Equation (8) subtracts from cits components along *A* and *B.* Why not subtract the components along *a* and along b? 28 Where are the *mn2* multiplications in equation (11)? 29 Apply the MATLAB qr code to *a=* (2, 2, -1), *b* <sup>=</sup>(0, -3, 3), *c* <sup>=</sup>(1, 0, 0). What are the *q's?* 

#### Problems **30-35** involve orthogonal matrices **that** are special.

**<sup>30</sup>**The first four *wavelets* are in the columns of this wavelet matrix W:

$$W = \frac{1}{2} \begin{bmatrix} 1 & 1 & \sqrt{2} & 0 \\ 1 & 1 & -\sqrt{2} & 0 \\ 1 & -1 & 0 & \sqrt{2} \\ 1 & -1 & 0 & -\sqrt{2} \end{bmatrix}.$$

31 (a) Choose *c* so that *Q* is an orthogonal matrix:

$$Q = c \begin{bmatrix} 1 & -1 & -1 & -1 \\ -1 & 1 & -1 & 1 \\ -1 & -1 & 1 & -1 \\ -1 & -1 & -1 & 1 \end{bmatrix}.$$

Project *b* = (l, 1, 1, 1) onto the first column. Then project *b* onto the plane of the first two columns.

- 32 If *u* is a unit vector, then *Q* = *I 2uu* Tis a reflection matrix (Example 3). Find Q<sup>1</sup> from *u* = (0, 1) and Q2 from *u* = (0, v'J,/2, v'J,/2). Draw the reflections when Q<sup>1</sup> and Q2 multiply the vectors (1, 2) and (1, 1, 1). 33 Find all matrices that are both orthogonal and lower triangular. 34 *Q* = *I* - *2uu* T is a reflection matrix when *u* Tu = l. Two reflections give Q <sup>2</sup>= *I.* 
  - (a) Show that *Qu* <sup>=</sup>*-u.* The mirror is perpendicular to *u.*
  - (b) Find *Qv* when *u* T *<sup>v</sup>* <sup>=</sup>0. The mirror contains *v.* It reflects to itself.

## **Challenge Problems**

35 (MATLAB) Factor [ Q, R] = qr(A) for *A* = eye(4) - diag([ 1 1 1 ],-1). You are orthogonalizing the columns (1, -1, 0, 0) and (0, 1, -1, 0) and (0, 0, 1, -1) and (0, 0, 0, 1) of *A.* Can you scale the orthogonal columns of *Q* to get nice integer components? 36 If *A* ism by *n* with rank *n,* qr(A) produces a *square <sup>Q</sup>*and zeros below *R:* 

| The factors from MATLAB are $(m$ by $m)(m$ by $n)$ | $A = [Q_1 \quad Q_2] \begin{bmatrix} R \\ 0 \end{bmatrix}$ |
|----------------------------------------------------|------------------------------------------------------------|
|----------------------------------------------------|------------------------------------------------------------|

The *n* columns of Q1 are an orthonormal basis for which fundamental subspace? The *m-n* columns of Q2 are an orthonormal basis for which fundamental subspace?

37 We know that *P* <sup>=</sup> QQT is the projection onto the column space of Q(m by n). Now add another column *a* to produce *<sup>A</sup>* <sup>=</sup>[Q a]. Gram-Schmidt replaces *a* by what vector *q?* Start with *a,* subtract \_\_ , divide by \_\_ to find *q.*

