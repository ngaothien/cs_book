# **Chapter 8**

# **Linear Transformations**

# **8.1 The Idea of a Linear Transformation**

1 A **linear transformation** *<sup>T</sup>*takes vectors *v* to vectors *T( v* ). Linearity requires I *T(c <sup>v</sup>*+ *dw)* = *cT(v)* + *dT(w)* I Note T(O) = 0 so *T(v)* = *<sup>v</sup>*+ *u0* is not linear. 2 The input vectors *v* and outputs *T( v)* can be in R <sup>n</sup>or matrix space or function space. 3 If *A* ism by *n, T(x) =Axis* linear from the input space R <sup>n</sup>to the output space Rm. 4 The derivative T(f) = :: is linear. The integral T<sup>+</sup> (J) = 1<sup>x</sup> j(t) dt is its pseudoinverse. 5 The product *ST* of two linear transformations is still linear : I ( *ST)* ( *v)* = *S (T* ( *v))* .1

When a matrix *A* multiplies a vector *v,* it "transforms" *v* into another vector *Av. In goes v, out comes T( v)* = *Av.* A transformation *T* follows the same idea as a function. In goes a number *x,* out comes *f(x).* For one vector *v* or one number *x,* we multiply by the matrix or we evaluate the function. The deeper goal is to see all vectors *v* at once. We are transforming the whole space V when we multiply every v by *A.*

Start again with a matrix *A.* It transforms *v* to *Av.* It transforms *w* to *Aw.* Then we *know* what happens to *u* = *<sup>v</sup>*+ *w.* There is no doubt about *Au,* it has to equal *Av+ Aw.* Matrix multiplication *T( v)* = *Av* gives a *linear transformation:*

A *transformation <sup>T</sup>*assigns an output *T( v)* to each input vector *v* in V. The transformation is *linear* if it meets these requirements for all v and w:

| (a) $T(\mathbf{v} + \mathbf{w}) = T(\mathbf{v}) + T(\mathbf{w})$ | (b) $T(c\mathbf{v}) = cT(\mathbf{v})$ | for all c. |
|------------------------------------------------------------------|---------------------------------------|------------|
|                                                                  |                                       |            |

If the input is *v* = **0,** the output must be *T( v)* = **0.** We combine rules (a) and (b) into one:

**Linear transformation** *T(cv* + *dw) must equal cT(v)* + *dT(w).* 

Again I can test matrix multiplication for linearity: *A( cv* + *dw)* = *cAv* + *dAw* is *true.* 

A linear transformation is highly restricted. Suppose *T* adds *u0* to every vector. Then *T(v)* = *v* + *u0* and *T(w)* = *w* + *u0.* This isn't good, or at least *it isn't linear.*  Applying *T* to *v* + *w* produces *v* + *w* + *u0.* That is not the same as *T( v)* + *T( w* ):

| Shift is not linear | $v + w + u_0$ | is not | $T(v) + T(w) = (v + u_0) + (w + u_0)$ |
|---------------------|---------------|--------|---------------------------------------|
|---------------------|---------------|--------|---------------------------------------|

The exception is when *u0* = 0. The transformation reduces to *T( v)* = *v.* This is the *identity transformation* (nothing moves, as in multiplication by the identity matrix). That is certainly linear. In this case the input space Vis the same as the output space W.

The linear-plus-shift transformation *T( v)* = *Av* + *u0* is called *"affine".* Straight lines stay straight although *T* is not linear. Computer graphics works with affine transformations in Section 10.6, because we must be able to move images.

**Example 1** Choose a fixed vector *a* = ( 1, 3, 4), and let *T* ( *v)* be the dot product *a* · v:

The output is *T(v) =a· v* = v1<sup>+</sup>*3v2* + *4v3.* 

| The input is | $v = (v_1, v_2, v_3)$ . | The output is | $T(v) = \mathbf{a} \cdot \mathbf{v} = v_1 + 3v_2 + 4v_3$ . |
|--------------|-------------------------|---------------|------------------------------------------------------------|
|              |                         |               |                                                            |

*Dot products are linear.* The inputs v come from three-dimensional space, so V = R <sup>3</sup> . The outputs are just numbers, so the output space is W **=** R <sup>1</sup> . We are multiplying by the row matrix *A* = [ 1 3 4]. Then *T* ( *v)* = *Av.* 

You will get good at recognizing which transformations are linear. If the output involves squares or products or lengths, *vf* or v1 *v2* or llv II, then Tis not linear.

**Example 2** The length *T( v)* = llvll is not linear. Requirement (a) for linearity would be llv + wll = llvll + llwll- Requirement (b) would be llcvll = cllvll- Both are false!

*Not* (a): The sides of a triangle satisfy an *inequality* llv + wll ::; llvll + llwll-

*Not* (b): The length II -vii is llvll and not -llvll- For negative c, linearity fails.

**Example 3** (Rotation) *T* is the transformation that *rotates every vector by* 30° . The *"domain"* of Tis the *xy* plane (all input vectors *v).* The *"range"* of Tis also the *xy* plane ( all rotated vectors *T* ( *v)* ). We described *T* without a matrix: rotate the plane by 30° .

Is rotation linear? *Yes it is.* We can rotate two vectors and add the results. The sum of rotations *T( v)* + *T( w)* is the same as the rotation *T( v* + *w)* of the sum. **The whole plane is turning together, in this linear transformation.** 

# **Lines to Lines, Triangles to Triangles, Basis Tells All**

Figure 8.1 shows the line from *v tow* in the input space. It also shows the line from *T( v)* to *T( w)* in the output space. Linearity tells us: Every point on the input line goes onto the output line. And more than that: *Equally spaced points go to equally spaced points.* The middle point *u* = ½v + ½w goes to the middle point *T(u)* = *½T(v)* + *½T(w).* 

The second figure moves up a dimension. Now we have three corners *v1,* v2, *v3.*  Those inputs have three outputs *T(v1), T(v2), T(v3). The input triangle goes onto the output triangle.* Equally spaced points stay equally spaced (along the edges, and then between the edges). The middle point *u* = ½ ( *v1* <sup>+</sup>v2<sup>+</sup>*v3)* goes to the middle point *T(u)* = ½(T(v1) + *T(v2)* + *T(v3)).* 

![](images/_page_412_Diagram_5.jpeg)

Figure 8.1: Lines to lines, equal spacing to equal spacing, *u* = 0 to *T(u)* = 0.

*The rule of linearity extends to combinations of three vectors or n vectors:* 

| Linearity                                          | $u = c_1v_1 + c_2v_2 + \dots + c_nv_n$ | must transform to | (1) |
|----------------------------------------------------|----------------------------------------|-------------------|-----|
| $T(u) = c_1T(v_1) + c_2T(v_2) + \dots + c_nT(v_n)$ |                                        |                   |     |

The 2-vector rule starts the 3-vector proof: *T* ( *cu* + *dv* + *ew)* = *T (cu)* + *T* ( *dv* + *ew).*  Then linearity applies to both of those parts, to give *cT(u)* + *dT(v)* + *eT(w).* 

Then-vector rule (1) leads to the most important fact about linear transformations:

**Suppose you know** *T* ( *v)* **for all vectors** v1, ••• , *Vn* **in a basis Then you know** *T* ( u) **for every vector** *u* **in the space.**

You see the reason: Every *u* in the space is a combination of the basis vectors *Vj.*  Then linearity tells us that *T* ( *u)* is the same combination of the outputs *T* ( *v j).* 

**Example 4 The transformation** *T* **takes the derivative of the input:** *T( u)* = *du/ dx.*  How do you find the derivative of *u* = 6 - *4x* + 3x<sup>2</sup> ? You start with the derivatives of 1, *x,* and x • Those are the basis vectors. Their derivatives are 0, 1, and 2x. Then you use linearity for the derivative of any combination:

$$\frac{du}{dx} = 6 (\text{derivative of } 1) - 4 (\text{derivative of } x) + 3 (\text{derivative of } x^2) = -4 + 6x.$$

All of calculus depends on linearity! Precalculus finds a few key derivatives, for x <sup>n</sup>and sin *x* and cos *x* and e . Then linearity applies to all their combinations.

I would say that the only rule special to calculus is the *chain rule.* That produces the derivative of a chain of functions *f (g(x)* ).

**Nullspace** of *T(u)* = *du/dx.* For the nullspace we solve *T(u)* = 0. The derivative is zero when *u is a constant function.* So the one-dimensional nullspace is a line in function space-all multiples of the special solution *u* = 1.

**Column space** of *T* ( *u)* = *du/ dx.* In our example the input space contains all quadratics *a+ bx+* cx<sup>2</sup> . The outputs (the column space) are all linear functions *b* + 2cx. Notice that the **Counting Theorem** is still true : *r* + ( *n* - *r)* = *n.* 

dimension ( **column space)** +dimension ( **nullspace)** = 2+ 1 = **3** = dimension **(input space)**

*What is the matrix for d/ dx?* I can't leave derivatives without asking for a matrix. We have a linear transformation *T* = *d/ dx.* We know what *T* does to the basis functions:

| $v_1, v_2, v_3 = 1, x, x^2$ | $\frac{dv_1}{dx} = 0$ | $\frac{dv_2}{dx} = 1 = v_1$ | $\frac{dv_3}{dx} = 2x = 2v_2.$ | (2) |
|-----------------------------|-----------------------|-----------------------------|--------------------------------|-----|
|                             |                       |                             |                                |     |

The 3-dimensional input space V ( = quadratics) transforms to the 2-dimensional output space **W** (= linear functions). If v 1, v2, v*3* were vectors, I would know the matrix.

| $\mathbf{A} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix} = \text{matrix form of the derivative } T = \frac{d}{dx}.$ | (3) |
|-------------------------------------------------------------------------------------------------------------------------------|-----|
|-------------------------------------------------------------------------------------------------------------------------------|-----|

The linear transformation *du/ dx* is perfectly copied by the matrix multiplication *Au.*

| Input $u$       | Multiplication $Au = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$ | $\begin{bmatrix} a \\ b \\ c \end{bmatrix} = \begin{bmatrix} b \\ 2c \end{bmatrix}$ | Output $\frac{du}{dx} = b + 2cx$ . |
|-----------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------|
| $a + bx + cx^2$ |                                                                            |                                                                                     |                                    |

The connection from *T* to *A* (we will connect every transformation to a matrix) depended on choosing an input basis 1, *x,* x <sup>2</sup>and an output basis 1, *x.*

**Next we look at integrals. They give the pseudoinverse r<sup>+</sup>of the derivative!**  I can't write r- <sup>1</sup>and I can't say *"inverse of T"* when the derivative of 1 is 0.

# **Example 5 Integration** *T<sup>+</sup>***is also linear:** *fox* ( *D* + *Ex) dx* = *Dx* + ½ *Ex<sup>2</sup>*

The input basis is now 1, *x.* The output basis is 1, *x, x .* The matrix *A<sup>+</sup>*for *r<sup>+</sup>*is 3 by 2:

**Output** = **Integral of** *v r+(v)* = *Dx* + *½Ex<sup>2</sup>*

| Input $v$ | Multiplication $A^+v = \begin{bmatrix} 0 & 0 \\ 1 & 0 \\ 0 & \frac{1}{2} \end{bmatrix}$ | $\begin{bmatrix} D \\ E \end{bmatrix} = \begin{bmatrix} 0 \\ D \\ \frac{1}{2}E \end{bmatrix}$ | Output = Integral of $v$<br>$T^+(v) = Dx + \frac{1}{2}Ex^2$ |
|-----------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
|           |                                                                                         |                                                                                               |                                                             |

*The Fundamental Theorem of Calculus says that integration is the (pseudo )inverse of differentiation.* For linear algebra, the matrix *A<sup>+</sup>*is the (pseudo )inverse of the matrix A:

| $A^+A = \begin{bmatrix} 0 & 0 \\ 1 & 0 \\ 0 & \frac{1}{2} \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad \text{and} \quad AA^+ = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \quad (4)$ |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The derivative of a constant function is zero. That zero is on the diagonal of *A<sup>+</sup>A.* Calculus wouldn't be calculus without that 1-dimensional nullspace of *T* = *d/ dx.* 

### **Examples of Transformations (mostly linear)**

**Example 6** Project every 3-dimensional vector onto the horizontal plane z = 1. The vector *v* = ( *x, y, z)* is transformed to *T* ( *v)* = ( *x, y,* 1). This transformation is not linear. Why not? It doesn't even transform *v* = 0 into *T( v)* = 0.

**Example 7** Suppose *A* is an *invertible matrix.* Certainly *T( v* + *w)* = *Av* + *Aw* = *T* ( *v)* + *T* ( *w).* Another linear transformation is multiplication by *A* - 1 . This produces the *inverse transformation* r- <sup>1</sup> , which brings every vector *T* ( *v)* back to v:

$$T^{-1}(T(\mathbf{v})) = \mathbf{v}$$
 matches the matrix multiplication  $A^{-1}(A\mathbf{v}) = \mathbf{v}$ .

If *T(v)* = *Av* and *S(u)* = *Bu,* then the product *T(S(u))* matches the product *ABu.* 

We are reaching an unavoidable question. *Are all linear transformations from* V = *R<sup>n</sup> to* W = Rm *produced by matrices?* When a linear *T* is described as a "rotation" or "projection" or" ... ", is there always a matrix *A* hiding behind *T?* Is *T(v)* always *Av?* 

The answer is *yes!* This is an approach to linear algebra that doesn't start with matrices. We still end up with matrices-after *we choose an input basis and output basis.* 

**Note** Transformations have a language of their own. For a matrix, the column space contains all outputs *Av.* The nullspace contains all inputs for which *Av* = 0. Translate those words into *"range"* and *"kernel":* 

*Range of T* = set of *all outputs T* ( *v).* Range corresponds to column space.

*Kernel of T* = set of *all inputs for which T( v)* = 0. Kernel corresponds to nullspace.

The range is in the output space W. The kernel is in the input space V. When *T* is multiplication by a matrix, *T ( v)* = *Av,* range is column space and kernel is nulls pace.

#### **Linear Transformations of the Plane**

It is more interesting to *see* a transformation than to define it. When a 2 by 2 matrix *<sup>A</sup>* multiplies all vectors in R <sup>2</sup> , we can watch how it acts. Start with a "house" that has eleven endpoints. Those eleven vectors *v* are transformed into eleven vectors *Av.* Straight lines between *v's* become straight lines between the transformed vectors *Av.* (The transformation from house to house is linear!) Applying *A* to a standard house produces a new house-possibly stretched or rotated or otherwise unlivable.

This part of the book is visual, not theoretical. We will show four houses and the matrices that produce them. The columns of *H* are the eleven comers of the first house. (H is 2 by 12, so **plot2d** in Problem 25 will connect the **11th** comer to the first.) *A* multiplies the 11 points in the house matrix *H* to produce the comers *AH* of the other houses.

| House matrix | $H = \begin{bmatrix} -6 & -6 & -7 & 0 & 7 & 6 & 6 & -3 & -3 & 0 & -6 \\ -7 & 2 & 1 & 8 & 1 & 2 & -7 & -2 & -2 & -2 & -7 \end{bmatrix}$ |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
|              |                                                                                                                                        |

<sup>A</sup> <sup>=</sup> [� �]

<sup>A</sup> <sup>=</sup> [� �]

A = [

cos 35° sin 35°

-sin 35� cos 35°

A= 10.7 0.31 Lo.3 o.1J

Figure 8.2: Linear transformations of a house drawn by **plot2d(A** \* *H).*

#### **• REVIEW OF THE KEY IDEAS •**

- **1.** A transformation T takes each *v* in the input space to T( *v)* in the output space.
- **2.** Tis **linear** ifT(v + *w)* = *T(v)* + *T(w)* and *T(cv)* = *cT(v):* lines to lines.
- **3.** Combinations to combinations: *T* (c1 v1+ · · · *+cnvn)* = c1 *T( vi)+··· +en T( vn)-*
- **4.** *<sup>T</sup>*= *derivative* and r+ = *integral* are linear. So is *T(v)* = *Av* from *<sup>R</sup> <sup>n</sup>*to R m.

■ WORKED EXAMPLES ■**8.1 A** The elimination matrix  $\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$  gives a *shearing transformation* from  $(x, y)$  to  $T(x, y) = (x, x + y)$ . If the inputs fill a square, draw the transformed square.

**Solution** The points  $(1, 0)$  and  $(2, 0)$  on the  $x$  axis transform by  $T$  to  $(1, 1)$  and  $(2, 2)$  on the  $45^\circ$  line. Points on the  $y$  axis are *not moved*:  $T(0, y) = (0, y) = \text{eigenvectors with } \lambda = 1$ .

![](images/_page_416_Picture_20.jpeg)

**8.1 B** A **nonlinear transformation**  $T$  is invertible if every  $b$  in the output space comes from exactly one  $x$  in the input space:  $T(x) = b$  always has exactly one solution. Which of these transformations (on real numbers  $x$ ) is invertible and what is  $T^{-1}$ ? *None are linear, not even  $T_3$ .* When you solve  $T(x) = b$ , you are inverting  $T$ :

$$T_1(x) = x^2 \quad T_2(x) = x^3 \quad T_3(x) = x + 9 \quad T_4(x) = e^x \quad T_5(x) = \frac{1}{x} \text{ for nonzero } x \text{'s}$$

**Solution**  $T_1$  is not invertible:  $x^2 = 1$  has *two* solutions and  $x^2 = -1$  has *no* solution.  $T_4$  is not invertible because  $e^x = -1$  has no solution. (If the output space changes to *positive*  $b$ 's then the inverse of  $e^x = b$  is  $x = \ln b$ .)

Notice  $T_5^2 = \text{identity}$ . But  $T_3^2(x) = x + 18$ . What are  $T_2^2(x)$  and  $T_4^2(x)$ ?

 $T_2, T_3, T_5$  are invertible:  $x^3 = b$  and  $x + 9 = b$  and  $\frac{1}{x} = b$  have one solution  $x$ .

$$x = T_2^{-1}(b) = b^{1/3} \quad x = T_3^{-1}(b) = b - 9 \quad x = T_5^{-1}(b) = 1/b$$

## Problem Set 8.1

1. 1 A linear transformation must leave the zero vector fixed:  $T(0) = 0$ . Prove this from  $T(v + w) = T(v) + T(w)$  by choosing  $w = \underline{\hspace{2cm}}$  (and finish the proof). Prove it also from  $T(cv) = cT(v)$  by choosing  $c = \underline{\hspace{2cm}}$ .
2. 2 Requirement (b) gives  $T(cv) = cT(v)$  and also  $T(dw) = dT(w)$ . Then by addition, requirement (a) gives  $T(\underline{\hspace{2cm}}) = (\underline{\hspace{2cm}})$ . What is  $T(cv + dw + eu)$ ?
3. 3 Which of these transformations are not linear? The input is  $v = (v_1, v_2)$ :
   1. (a)  $T(v) = (v_2, v_1)$
   2. (b)  $T(v) = (v_1, v_1)$
   3. (c)  $T(v) = (0, v_1)$
   4. (d)  $T(v) = (0, 1)$
   5. (e)  $T(v) = v_1 - v_2$
   6. (f)  $T(v) = v_1 v_2$ .

- 4 If Sand Tare linear transformations, is *T(S(* v)) linear or quadratic?
  - (a) (Special case) If *S(v)* = *v* and *T(v)* = *v,* then *T(S(v))* = *v* or v 2?
- (b) (General case) *S(* V1 +v<sup>2</sup> ) = *S(* v1) + *S(* v<sup>2</sup> ) and *T(* V1 +v<sup>2</sup> ) = *T(* v1) + *T(* v<sup>2</sup> ) combine into *T(S(v1* + v<sup>2</sup> )) = T( \_\_ ) = \_\_ + \_\_ . 5 Suppose *T* ( v) = v except that *T* 0, ( v2) = ( 0, 0). Show that this transformation satisfies *T(cv)* = *cT(v)* but does not satisfy *T(v* + w) = *T(v)* + *T(w).*  6 Which of these transformations satisfy *T* ( *v* + w) = *T* ( v) + *T* ( *w)* and which satisfy *T(cv)* = *cT(v)?*
- (a) *T(v)* = v/llvll ( d) T (*v)* = largest component of *v.* 7 For these transformations ofV = R2 to W = R<sup>2</sup> , find *T(T(v)).* Show that when *<sup>T</sup>*( v) is linear, then also *T* ( *T* ( v)) is linear.
  - (a) *T(v)* = *-v* (b) *T(v)* = *v* + (l, 1)
  - (c) *T( v)* = 90° rotation= -v( <sup>2</sup> , v1)
- (d) *T(v)* =projection= ½(vi+ v<sup>2</sup> , v1 + v<sup>2</sup> )- 8 Find the range and kernel (like the column space and nulls pace) of T:
  - (a) T(v1,v<sup>2</sup> ) = (v1 -v<sup>2</sup> ,0)
  - (c) *T(v1,* v<sup>2</sup> ) = (0, 0)
- (b) T(v1,v<sup>2</sup> ,v3) = (v1,v<sup>2</sup> )
- (d) T(v1,v<sup>2</sup> ) = (v1,vi). **<sup>9</sup>**The "cyclic" transformation *T* is defined by *T(* v1, v<sup>2</sup> , v3) = ( v<sup>2</sup> , *v<sup>3</sup> ,* vi). What is *T(T(v))?* What is *T<sup>3</sup> (v)?* What is T<sup>100</sup> (v)? Apply Ta hundred times to *v.*  **<sup>10</sup>**A linear transformation from V to W has an *inverse* from W to V when the range is all of W and the kernel contains only *v* = **0.** Then *T( v)* = w has one solution *v* for each win W. Why are these T's not invertible?
  - (a) T(v1,v<sup>2</sup> ) = (v<sup>2</sup> ,v<sup>2</sup> )
  - (b) T(v1,v<sup>2</sup> ) = (v1,v<sup>2</sup> ,v1 +v<sup>2</sup> )
- (c) *T(v1,v2)* = v1 W=R<sup>2</sup> W=R<sup>3</sup> W=R<sup>1</sup> 11 If T( *v)* = Av and A is m by n, then Tis "multiplication by *A."* 
  - (a) What are the input and output spaces V and W?
  - (b) Why is range of *T* = column space of *A?* ( c) Why is kernel of *T* = null space of *A?*

- 12 Suppose a linear *T* transforms (1, 1) to (2, 2) and (2, 0) to (0, 0). Find *T(* v ):
  - (a) *<sup>V</sup>*= (2, 2) (b) v=(3,l) (c) *<sup>V</sup>*= (-l, 1) (d) *<sup>V</sup>*<sup>=</sup> *(a, b).*

Problems 13-19 may be harder. The input space V contains all 2 by 2 matrices *M.*

- 13 *<sup>M</sup>*is any 2 by 2 matrix and *A* = [ ½ z] . The transformation *T* is defined by *T* ( *M)* = *AM.* What rules of matrix multiplication show that *T* is linear? 14 Suppose *A* = [ ½ � ] . Show that the range of *T* is the whole matrix space V and the kernel is the zero matrix:
  - (1) If *AM=* 0 prove that *M* must be the zero matrix.
- (2) Find a solution to *AM= B* for any 2 by 2 matrix *B.* 15 Suppose *A* = [ ½ � ] . Show that the identity matrix *I* is not in the range of *T.* Find a nonzero matrix *M* such that *T(M)* = *AM* is zero. 16 Suppose *T* transposes every 2 by 2 matrix *M.* Try to find a matrix *A* which gives *AM* = *MT. Show that no matrix A will do it. To professors:* Is this a linear transformation that doesn't come from a matrix? The matrix should be 4 by 4! 17 The transformation *T* that transposes every 2 by 2 matrix is definitely linear. Which of these extra properties are true?
  - (a) T <sup>2</sup>= identity transformation.
  - (b) The kernel of *T* is the zero matrix. ( c) Every 2 by 2 matrix is in the range of *T.*
- (d) *T(M)* =-M is impossible. 18 Suppose *T(M)* = [6 8] [ M] [g �]- Find a matrix with *T(M) cf=* 0. Describe all matrices with *T(M)* = 0 (the kernel) and all output matrices *T(M)* (the range). 19 If *A* and Bare invertible and *T(M)* = *AM B,* find r- <sup>1</sup>(M) in the form ( )M( ). Questions 20-26 are about house transformations. The output is *T(H)* = *AH.* 20 How can you tell from the picture of *T* (house) that *A* is
  - (a) a diagonal matrix?
  - (b) a rank-one matrix?
- (c) a lower triangular matrix? 21 Draw a picture of *T* (house) for these matrices:

| $D = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$ | and | $A = \begin{bmatrix} .7 & .7 \\ .3 & .3 \end{bmatrix}$ | and | $U = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ |
|----------------------------------------------------|-----|--------------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|--------------------------------------------------------|-----|----------------------------------------------------|

- 22 What are the conditions on *A* = [ � �] to ensure that *T* (house) will
  - (a) sit straight up?
  - (b) expand the house by 3 in all directions?
- (c) rotate the house with no change in its shape? 23 Describe *T* (house) when *T(v)* = *-v* + (1, 0). This Tis "affine". 24 Change the house matrix *H* to add a chimney. **<sup>25</sup>**The standard house is drawn by plot2d(H). Circles from o and lines from -:

| $x = H(1, \cdot)'; y = H(2, \cdot)';$<br>$\text{axis}([-1010-1010]), \text{axis}('\text{square}')$<br>$\text{plot}(x, y, 'o', x, y, '-');$ |
|--------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------|

Test plot2d(A '\* H) and pfot2d(A *1* \* A \* H) with the matrices in Figure 8.1.

26 Without a computer sketch the houses *A* \* *H* for these matrices *A:*

| $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | and | $\begin{bmatrix} .5 & .5 \\ .5 & .5 \end{bmatrix}$ | and | $\begin{bmatrix} .5 & .5 \\ -.5 & .5 \end{bmatrix}$ | and | $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ |
|------------------------------------------------|-----|----------------------------------------------------|-----|-----------------------------------------------------|-----|------------------------------------------------|
|                                                |     |                                                    |     |                                                     |     |                                                |

- 27 This code creates a vector theta of 50 angles. It draws the unit circle and then it draws *T* (circle) = ellipse. *T* ( *v)* = *Av* takes circles **to** ellipses. A= [2 1 ;1 2] % You can change A theta= [0:2 \* pi/50:2 \* pi]; circle= [cos(theta); sin(theta)]; ellipse = A \* circle; axis([-4 4 -4 4]); axis('square') plot(circle(1,:), circle(2,:), ellipse(1,:), ellipse(2,:)) **<sup>28</sup>**Add two eyes and a smile to the circle in Problem 27. (If one eye is dark and the other is light, you can tell when the face is reflected across the *y* axis.) Multiply by matrices *A* to get new faces. 29 What conditions on det *<sup>A</sup>* <sup>=</sup>*ad* - *be* ensure that the output house *AH* will
  - (a) be squashed onto a line?
  - (b) keep its endpoints in clockwise order (not reflected)?
- (c) have the same area as the original house? **30**Why does every linear transformation *T* from R 2 to R 2 take squares to parallelograms? Rectangles also go to parallelograms (squashed if *T* is not invertible).

# **8.2 The Matrix of a Linear Transformation**

**1** We know all T(v) ifwe know T(v1), ... , T(v<sup>n</sup> ) for an input basis v1, ... , V<sup>n</sup> : use **linearity.**  2 Column j in the "matrix for *T"* comes from applying *T* to the input basis vector *v <sup>j</sup> .*  **3** Write T( Vj) = a *<sup>1</sup>* jw*1*+ · · · + a<sup>m</sup> jWm in the output basis of w's. Those aij go into column *j.*  **4** The matrix for T(x) =Axis A, if the input and output bases= columns of Inxn and Imxm· 5 When the bases change to v's and w's, the matrix for the same T changes from A to w-1 AV. 6 Best bases: *V* = *W* = eigenvectors and *V, W* = singular vectors give diagonal A and :B.

*The next pages assign a matrix A to every linear transformation T.* For ordinary column vectors, the input *v* is in **V** = *Rn* and the output *T* ( *v)* is in **W** = Rm. The matrix *A* for this transformation will be *m* by *n.* Our choice of bases in V and W will decide *A.* 

The standard basis vectors for *Rn* and Rm are the columns of *I.* That choice leads to a standard matrix. Then T(v) = Av in the normal way. But these spaces also have other bases, so *the same transformation T is represented by other matrices.* A main theme of linear algebra is to choose the bases that give the best matrix (a diagonal matrix) for *T.* 

All vector spaces **V** and **W** have bases. Each choice of those bases leads to a matrix for *T.* When the input basis is different from the output basis, the matrix for *T( v)* = *v* will not be the identity *I.* It will be the "change of basis matrix". Here is the key idea:

**Suppose we know** *T(* v) **for the input basis vectors v1 to** Vn. **Columns 1 ton of the matrix will contain those outputs** T(v1) **to** T(v<sup>n</sup> ) A **times** *c* = **matrix times vector = combination of those** n **columns. Acis thecorrect combination** c1T(v1) + · · · + cnT(v<sup>n</sup> ) = T(v).

**Reason** Every vis a unique combination c1v1+ · · · + CnVn of the basis vectors Vj. Since *T* is a linear transformation (here is the moment for linearity), *T( v)* must be **the same combination** c1T(v1) + · · · + cnT(v<sup>n</sup> ) **of the outputs** T(vj) **in the columns.** 

Our first example gives the matrix *A* for the standard basis vectors in R 2 and R 3 .

**Example 1** Suppose *T* transforms v1 = (1, 0) to *T( vi)* = (2, 3, 4). Suppose the second basis vectorv2 = (0,l)goes to T(v2) = (5,5,5). IfTis linearfromR<sup>2</sup> toR3 then its "standard matrix" is 3 by 2. Those outputs *T(* v1) and *T(* v2) go into the columns of A:

| $A = \begin{bmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{bmatrix}$ | $c_1 = 1$ and $c_2 = 1$ give $T(\mathbf{v}_1 + \mathbf{v}_2) = \begin{bmatrix} 2 & 5 \\ 3 & 5 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}$ |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Change of Basis

**Example 2** Suppose the input space  $\mathbf{V} = \mathbf{R}^2$  is also the output space  $\mathbf{W} = \mathbf{R}^2$ . Suppose that  $T(\mathbf{v}) = \mathbf{v}$  is the identity transformation. You might expect its matrix to be  $I$ , but that only happens when the input basis is the same as the output basis. I will choose different bases to see how the matrix is constructed.

For this special case  $T(\mathbf{v}) = \mathbf{v}$ , I will call the matrix  $B$  instead of  $A$ . We are just changing basis from the  $\mathbf{v}$ 's to the  $\mathbf{w}$ 's. Each  $\mathbf{v}$  is a combination of  $\mathbf{w}_1$  and  $\mathbf{w}_2$ .

$$\text{Input basis} \begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 3 & 8 \end{bmatrix} \quad \text{Output basis} \begin{bmatrix} \mathbf{w}_1 & \mathbf{w}_2 \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 1 & 2 \end{bmatrix} \quad \text{Change of basis} \begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 \end{bmatrix} = \begin{bmatrix} 1\mathbf{w}_1 + 1\mathbf{w}_2 \\ 2\mathbf{w}_1 + 3\mathbf{w}_2 \end{bmatrix}$$

Please notice! I wrote the input basis  $\mathbf{v}_1, \mathbf{v}_2$  in terms of the output basis  $\mathbf{w}_1, \mathbf{w}_2$ . That is because of our key rule. We apply the identity transformation  $T$  to each input basis vector:  $T(\mathbf{v}_1) = \mathbf{v}_1$  and  $T(\mathbf{v}_2) = \mathbf{v}_2$ . **Then we write those outputs  $\mathbf{v}_1$  and  $\mathbf{v}_2$  in the output basis  $\mathbf{w}_1$  and  $\mathbf{w}_2$ .** Those bold numbers 1, 1 and 2, 3 tell us column 1 and column 2 of the matrix  $B$  (the change of basis matrix):  $WB = V$  so  $B = W^{-1}V$ .

$$\text{Matrix } B \text{ for change of basis} \begin{bmatrix} \mathbf{w}_1 & \mathbf{w}_2 \end{bmatrix} \begin{bmatrix} \mathbf{B} \end{bmatrix} = \begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 \end{bmatrix} \text{ is } \begin{bmatrix} 3 & 0 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} \mathbf{1} & \mathbf{2} \\ \mathbf{1} & \mathbf{3} \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 3 & 8 \end{bmatrix}. \quad (1)$$

When the input basis is in the columns of a matrix  $\mathbf{V}$ , and the output basis is in the columns of  $\mathbf{W}$ , the change of basis matrix for  $T = I$  is  $\mathbf{B} = \mathbf{W}^{-1}\mathbf{V}$ .

**The key** I see a clear way to understand that rule  $B = W^{-1}V$ . Suppose the same vector  $\mathbf{u}$  is written in the input basis of  $\mathbf{v}$ 's and the output basis of  $\mathbf{w}$ 's. I will do that three ways:

$$\mathbf{u} = c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n \quad \text{is } \begin{bmatrix} \mathbf{v}_1 & \dots & \mathbf{v}_n \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} = \begin{bmatrix} \mathbf{w}_1 & \dots & \mathbf{w}_n \end{bmatrix} \begin{bmatrix} d_1 \\ \vdots \\ d_n \end{bmatrix} \quad \text{and } \mathbf{V}\mathbf{c} = \mathbf{W}\mathbf{d}.$$

The coefficients  $\mathbf{d}$  in the new basis of  $\mathbf{w}$ 's are  $\mathbf{d} = \mathbf{W}^{-1}\mathbf{V}\mathbf{c}$ . Then  $\mathbf{B}$  is  $\mathbf{W}^{-1}\mathbf{V}$ . (2)

This formula  $\mathbf{B} = \mathbf{W}^{-1}\mathbf{V}$  produces one of the world's greatest mysteries: When the standard basis  $\mathbf{V} = \mathbf{I}$  is changed to a different basis  $\mathbf{W}$ , the change of basis matrix is not  $\mathbf{W}$  but  $\mathbf{B} = \mathbf{W}^{-1}$ . Larger basis vectors have smaller coefficients!

$$\begin{bmatrix} x \\ y \end{bmatrix} \text{ in the standard basis has coefficients } \begin{bmatrix} \mathbf{w}_1 & \mathbf{w}_2 \end{bmatrix}^{-1} \begin{bmatrix} x \\ y \end{bmatrix} \text{ in the } \mathbf{w}_1, \mathbf{w}_2 \text{ basis.}$$

#### **Construction of the Matrix**

Now we construct a matrix for any linear transformation. Suppose T transforms the space V ( n-dimensional) to the space W ( m-dimensional). We choose a basis v1, ... , *Vn* for V and we choose a basis w1, ... , Wm for W. The matrix *A* will be *m* by *n.* To find the first column of *A,* apply *T* to the first basis vector Vi. The output *T* ( v1) is in W.

| $T(v_1)$ | <i>is a combination</i> | $a_{11}w_1 + \dots + a_{m1}w_m$ | <i>of the output basis for <math>W</math>.</i> |
|----------|-------------------------|---------------------------------|------------------------------------------------|
|          |                         |                                 |                                                |

*These numbers* an, ... ,a<sup>m</sup>1*go into the first column of A.* Transforming Vi to *T(v<sup>1</sup> )*  matches multiplying (1, 0, ... , 0) by *A.* It yields that first column of the matrix. When Tis the derivative and the first basis vector is 1, its derivative is *T(v1)* = 0. So for the derivative matrix below, the first column of *A* is all zero.

**Example 3** The input basis of v's is 1, *x,* x , *x .* The output basis of *w's* is 1, *x,* x . *dv*  Then *T* **takes the derivative:** *T( v)* = - and *A* "derivative matrix". dx

$$\text{If } \mathbf{v} = c_1 + c_2 x + c_3 x^2 + c_4 x^3 \\ \text{then } \frac{dv}{dx} = 1c_2 + 2c_3 x + 3c_4 x^2 \quad Ac = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \\ c_3 \\ c_4 \end{bmatrix} = \begin{bmatrix} 2c_2 \\ 2c_3 \\ 3c_4 \end{bmatrix}$$

**Key rule:** The jth column of *A* is found by applying *T* to the jth basis vector *v*1

| $T(\mathbf{v}_j) = \text{combination of output basis vectors} = a_{1j}\mathbf{v}_1 + \cdots + a_{mj}\mathbf{w}_m.$ | (3) |
|--------------------------------------------------------------------------------------------------------------------|-----|
|--------------------------------------------------------------------------------------------------------------------|-----|

These numbers aij go into *A. The matrix is constructed to get the basis vectors right. Then linearity gets all other vectors right.* Every *vis* a combination c1 v1+ · · · + *CnVn,*  and *T* ( *v)* is a combination of the *w* 's. When *A* multiplies the vector c = ( c1, . . . , *Cn)*  in the *v* combination, *Ac* produces the coefficients in the *T( v)* combination. This is because matrix multiplication (combining columns) is linear like *T.*

The matrix *A* tells us what *T* does. Every linear transformation from V to W can be converted to a matrix. This matrix depends on the bases.

**Example 4** For the integral r+ ( *v* ), the first basis function is again **1.** Its integral is the second basis function x. So the first column of the "integral matrix" A+ is (0, 1, 0, 0).

$$\text{The integral of } d_1 + d_2x + d_3x^2 \quad A^+ d = \begin{bmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & \frac{1}{2} & 0 \\ 0 & 0 & \frac{1}{3} \end{bmatrix} \begin{bmatrix} d_1 \\ d_2 \\ d_3 \end{bmatrix} = \begin{bmatrix} 0 \\ d_1 \\ \frac{1}{2}d_2 \\ \frac{1}{3}d_3 \end{bmatrix}$$

If you integrate a function and then differentiate, you get back to the start. So *AA<sup>+</sup>*= *I.* But if you differentiate before integrating, the constant term is lost. So *A<sup>+</sup>A*is not *I. The integral of the derivative of* l *is zero:* 

$$T^+T(1) = \text{integral of zero function} = 0.$$

This matches *A<sup>+</sup>A,* whose first column is all zero. The derivative T has a kernel (the constant functions). Its matrix *A* has a nullspace. Main idea again: *Av* copies *T( v* ).

The examples of the derivative and integral made three points. First, linear transformations *T* are everywhere-in calculus and differential equations and linear algebra. Second, spaces other than *<sup>R</sup>n* are important-we had functions in V and W. Third, **if we differentiate and then integrate, we can multiply their matrices** *A+ A.* 

#### **Matrix Products** *AB* **Match Transformations** *TS*

We have come to something important-the real reason for the rule to multiply matrices. *At last we discover why!* Two linear transformations *T* and *S* are represented by two matrices *A* and *B.* Now compare *TS* with the multiplication *AB:* 

When we apply the transformation *T* to the output from *S,* we get *TS* by this rule:

*(TS)(* u) *is defined to be T(S(* u)). The output *S(* u) becomes the input to *T.* 

When we apply the matrix *A* to the output from *B,* we multiply *AB* by this rule:

*(AB)(x)* is defined to be *A(Bx* ). The output *Bx* becomes the input to *A.* 

*Matrix multiplication gives the correct matrix AB to represent TS.* 

The transformation *S* is from a space U to V. Its matrix *B* uses a basis u1, ... , *up*  for U and a basis v 1, ... , *Vn* for V. That matrix is n by *p.* The transformation Tis from V to W as before. *Its matrix A must use the same basis* v 1, ... , *Vn for* V-this is the output space for *S* and the input space for *T. Then the matrix AB matches TS.* 

**Multiplication** The linear transformation *TS* starts with any vector *u* in U, goes to *S(u)* in V and then to *T(S(u))* in W. The matrix *AB* starts with any x in RP, goes to *Bx* in *<sup>R</sup>n* and then to *ABx* in Rm. **The matrix** *AB* **correctly represents** *TS:*

| $TS$ : | $\mathbf{U} \rightarrow \mathbf{V} \rightarrow \mathbf{W}$ | $AB$ : | $(m \text{ by } n)(n \text{ by } p) = (m \text{ by } p).$ |
|--------|------------------------------------------------------------|--------|-----------------------------------------------------------|
|        |                                                            |        |                                                           |

The input is *u* <sup>=</sup>x <sup>1</sup>u1+ · · · + *XpUp.* The output *T(S(u))* matches the output *ABx. Product of transformations TS matches product of matrices AB.* 

The most important cases are when the spaces U, V, W are the same and their bases are the same. With *m* = *n* = *p* we have square matrices that we can multiply.

**Example 5** *S* rotates the plane by *0* and *T* also rotates by *0.* Then *TS* rotates by 20. This transformation T <sup>2</sup>corresponds to the rotation matrix A 2 through 20 :

| $T = S$ | $A = B$ | $T^2 = \text{rotation by } 2\theta$ | $A^2 = \begin{bmatrix} \cos 2\theta & -\sin 2\theta \\ \sin 2\theta & \cos 2\theta \end{bmatrix} \cdot (-1)^n$ |
|---------|---------|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 1       | 1       | 1                                   | 1                                                                                                              |
| 2       | 1       | 1                                   | 1                                                                                                              |
| 3       | 1       | 1                                   | 1                                                                                                              |
| 4       | 1       | 1                                   | 1                                                                                                              |
| 5       | 1       | 1                                   | 1                                                                                                              |
| 6       | 1       | 1                                   | 1                                                                                                              |
| 7       | 1       | 1                                   | 1                                                                                                              |
| 8       | 1       | 1                                   | 1                                                                                                              |
| 9       | 1       | 1                                   | 1                                                                                                              |
| 10      | 1       | 1                                   | 1                                                                                                              |
| 11      | 1       | 1                                   | 1                                                                                                              |
| 12      | 1       | 1                                   | 1                                                                                                              |
| 13      | 1       | 1                                   | 1                                                                                                              |
| 14      | 1       | 1                                   | 1                                                                                                              |
| 15      | 1       | 1                                   | 1                                                                                                              |
| 16      | 1       | 1                                   | 1                                                                                                              |
| 17      | 1       | 1                                   | 1                                                                                                              |
| 18      | 1       | 1                                   | 1                                                                                                              |
| 19      | 1       | 1                                   | 1                                                                                                              |
| 20      | 1       | 1                                   | 1                                                                                                              |
| 21      | 1       | 1                                   | 1                                                                                                              |
| 22      | 1       | 1                                   | 1                                                                                                              |
| 23      | 1       | 1                                   | 1                                                                                                              |
| 24      | 1       | 1                                   | 1                                                                                                              |
| 25      | 1       | 1                                   | 1                                                                                                              |
| 26      | 1       | 1                                   | 1                                                                                                              |
| 27      | 1       | 1                                   | 1                                                                                                              |
| 28      | 1       | 1                                   | 1                                                                                                              |
| 29      | 1       | 1                                   | 1                                                                                                              |
| 30      | 1       | 1                                   | 1                                                                                                              |
| 31      | 1       | 1                                   | 1                                                                                                              |
| 32      | 1       | 1                                   | 1                                                                                                              |
| 33      | 1       | 1                                   | 1                                                                                                              |
| 34      | 1       | 1                                   | 1                                                                                                              |
| 35      | 1       | 1                                   | 1                                                                                                              |
| 36      | 1       | 1                                   | 1                                                                                                              |
| 37      | 1       | 1                                   | 1                                                                                                              |
| 38      | 1       | 1                                   | 1                                                                                                              |
| 39      | 1       | 1                                   | 1                                                                                                              |
| 40      | 1       | 1                                   | 1                                                                                                              |
| 41      | 1       | 1                                   | 1                                                                                                              |
| 42      | 1       | 1                                   | 1                                                                                                              |
| 43      | 1       | 1                                   | 1                                                                                                              |
| 44      | 1       | 1                                   | 1                                                                                                              |
| 45      | 1       | 1                                   | 1                                                                                                              |
| 46      | 1       | 1                                   | 1                                                                                                              |
| 47      | 1       | 1                                   | 1                                                                                                              |
| 48      | 1       | 1                                   | 1                                                                                                              |
| 49      | 1       | 1                                   | 1                                                                                                              |
| 50      | 1       | 1                                   | 1                                                                                                              |
| 51      | 1       | 1                                   | 1                                                                                                              |
| 52      | 1       | 1                                   | 1                                                                                                              |
| 53      | 1       | 1                                   | 1                                                                                                              |
| 54      | 1       | 1                                   | 1                                                                                                              |
| 55      | 1       | 1                                   | 1                                                                                                              |
| 56      | 1       | 1                                   | 1                                                                                                              |
| 57      | 1       | 1                                   | 1                                                                                                              |
| 58      | 1       | 1                                   | 1                                                                                                              |
| 59      | 1       | 1                                   | 1                                                                                                              |
| 60      | 1       | 1                                   | 1                                                                                                              |
| 61      | 1       | 1                                   | 1                                                                                                              |
| 62      | 1       | 1                                   | 1                                                                                                              |
| 63      | 1       | 1                                   | 1                                                                                                              |
| 64      | 1       | 1                                   | 1                                                                                                              |
| 65      | 1       | 1                                   | 1                                                                                                              |
| 66      | 1       | 1                                   | 1                                                                                                              |
| 67      | 1       | 1                                   | 1                                                                                                              |
| 68      | 1       | 1                                   | 1                                                                                                              |
| 69      | 1       | 1                                   | 1                                                                                                              |
| 70      | 1       | 1                                   | 1                                                                                                              |
| 71      | 1       | 1                                   | 1                                                                                                              |
| 72      | 1       | 1                                   | 1                                                                                                              |
| 73      | 1       | 1                                   | 1                                                                                                              |
| 74      | 1       | 1                                   | 1                                                                                                              |
| 75      | 1       | 1                                   | 1                                                                                                              |
| 76      | 1       | 1                                   | 1                                                                                                              |
| 77      | 1       | 1                                   | 1                                                                                                              |
| 78      | 1       | 1                                   | 1                                                                                                              |
| 79      | 1       | 1                                   | 1                                                                                                              |
| 80      | 1       | 1                                   | 1                                                                                                              |
| 81      | 1       | 1                                   | 1                                                                                                              |
| 82      | 1       | 1                                   | 1                                                                                                              |
| 83      | 1       | 1                                   | 1                                                                                                              |
| 84      | 1       | 1                                   | 1                                                                                                              |
| 85      | 1       | 1                                   | 1                                                                                                              |
| 86      | 1       | 1                                   | 1                                                                                                              |
| 87      | 1       | 1                                   | 1                                                                                                              |
| 88      | 1       | 1                                   | 1                                                                                                              |
| 89      | 1       | 1                                   | 1                                                                                                              |
| 90      | 1       | 1                                   | 1                                                                                                              |
| 91      | 1       | 1                                   | 1                                                                                                              |
| 92      | 1       | 1                                   | 1                                                                                                              |
| 93      | 1       | 1                                   | 1                                                                                                              |
| 94      | 1       | 1                                   | 1                                                                                                              |
| 95      | 1       | 1                                   | 1                                                                                                              |
| 96      | 1       | 1                                   | 1                                                                                                              |
| 97      | 1       | 1                                   | 1                                                                                                              |
| 98      | 1       | 1                                   | 1                                                                                                              |
| 99      | 1       | 1                                   |                                                                                                                |

By matching (transformation)<sup>2</sup>with (matrix)<sup>2</sup> , we pick up the formulas for cos 2<sup>0</sup> and sin 20. Multiply *A* times *A:* 

$$\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} = \begin{bmatrix} \cos^2 \theta - \sin^2 \theta & -2 \sin \theta \cos \theta \\ 2 \sin \theta \cos \theta & \cos^2 \theta - \sin^2 \theta \end{bmatrix}. \quad (5)$$

Comparing ( 4) with ( 5) produces cos 20 = co<sup>s</sup> <sup>2</sup>0 - <sup>s</sup>in 2 0 and sin 20 Trigonometry (the double angle rule) comes from linear algebra. 2 sin0 cos *0.*

**Example 6** S rotates by the angle 0 and T rotates by -0. Then TS = I leads to AB = I. In this case *T(S(u))* is *u.* We rotate forward and back. For the matrices to match, ABx must be x. *The two matrices are inverses.* Check this by putting cos(-0) = cos *<sup>0</sup>* and sin( *-0)* = - <sup>s</sup>in *0* into the backward rotation matrix A:

$$AB = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} = \begin{bmatrix} \cos^2 \theta + \sin^2 \theta & 0 \\ 0 & \cos^2 \theta + \sin^2 \theta \end{bmatrix} = I.$$

### **Choosing the Best Bases**

Now comes the final step in this section of the book. **Choose bases that diagonalize the matrix.** With the standard basis (the columns of J) our transformation T produces some matrix A-probably not diagonal. That same T is represented by different matrices when we choose different bases. The two great choices are eigenvectors and singular vectors:

**Eigenvectors** If T transforms R <sup>n</sup>to R n , its matrix A is square. But using the standard basis, that matrix *A* is probably not diagonal. If there are n independent eigenvectors, *choose those as the input and output basis.* In this good basis, **the matrix for** T **is the diagonal eigenvalue matrix A.** 

**Example 7 The projection matrix** T projects every *v* = *(x, y)* in **<sup>R</sup> <sup>2</sup>**onto the line y = -x. Using the standard basis, v1 = (1,0) projects to T(v*1)* = (½,-½) For v2 = (0, 1) the projection is T(v*2)* = (-½,½)-Those are the columns of *A:* 

| Projection matrix | $A = \begin{bmatrix} \frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{bmatrix}$ | has $A^T = A$ and $A^2 = A$ . |
|-------------------|----------------------------------------------------------------------------------------------|-------------------------------|
| Standard bases    |                                                                                              |                               |
| Not diagonal      |                                                                                              |                               |

**When the basis vectors are eigenvectors, the matrix becomes diagonal.** 

$$v_1 = w_1 = (1, -1)$$
 projects to itself :  $T(v_1) = v_1$  and  $\lambda_1 = 1$   
 $v_2 = w_2 = (1, -1)$  projects to zero :  $T(v_2) = 0$  and  $\lambda_2 = 0$ 

| <b>Eigenvector bases</b> | The new matrix is $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} = \Lambda.$ | (6) |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----|
| <b>Diagonal matrix</b>   |                                                                                                                                            |     |

Eigenvectors are the perfect basis vectors. They produce the eigenvalue matrix A.

What about other choices of *input basis* = *output basis?* Put those basis vectors into the columns of *B.* We saw above that the change of basis matrices (between standard basis and new basis) are Bin = *B* and Bout = B-1 . The new matrix for *T* is **similar** to *A:* 

**Anew** <sup>=</sup>**B-<sup>1</sup>***AB* **in the new basis of** *b's* **is similar to** *A* **in the standard basis:** 

| $Ab's$ to $b's = B^{-1}$ standard to $b's$ | $A_{\text{standard}}$ | $Bb's$ to standard | (7) |
|--------------------------------------------|-----------------------|--------------------|-----|
|                                            |                       |                    |     |

I used the multiplication rule for the transformation *IT I. The matrices for I, T, I were*  B-<sup>1</sup> , *A, B.* The matrix *B* contains the input vectors b in the standard basis.

Finally we allow *different spaces V and W, and different bases v's* and *w's.* When we know *T* and we choose bases, we get a matrix *A.* Probably *A* is not symmetric or even square. But we can always choose *v's* and *w's* that produce a diagonal matrix. This will be the *singular value matrix* l"; = diag ( o-1, •.. , *a* r) in the decomposition *A* = U�VT.

**Singular vectors** The SVD says that u-1 *AV* = �- The right singular vectors v 1, ... , *Vn* will be the input basis. The left singular vectors u1, ... , *Um* will be the output basis. By the rule for matrix multiplication, the matrix for the same transformation in these new bases is *B;;<sup>u</sup> �AB;n* = u- <sup>1</sup>*AV=�-*

I can't say that� is "similar" to *A.* We are working now with two bases, input and output. But those are *orthonormal bases* and they preserve the lengths of vectors. Following a good suggestion by David Vogan, I propose that we say: 1": **is "isometric" to** *A.*

Definition *C* = Q1 <sup>1</sup>*AQ2 is isometric to A if* Q1 *and* Q2 *are orthogonal.* 

Definition 
$$C = Q_1^{-1} A Q_2$$
 is isometric to  $A$  if  $Q_1$  and  $Q_2$  are orthogonal.

**Example 8** To construct the matrix *A* for the transformation *T* = *ix,* we chose the input basis 1, *x, x , x <sup>3</sup>*and the output basis 1, *x, x .* The matrix A was simple but unfortunately it wasn't diagonal. But we can take each basis *in the opposite order.* 

Now the input basis is *x , x , x,* 1 and the output basis is *x , x,* 1. The change of basis matrices B;n and Bout are permutations. The matrix for *T(u)* = *du/dx* with the new bases is **the diagonal singular value matrix** B;;u�ABin <sup>=</sup>1": with *cr's* = 3, 2, 1:

$$B_{\text{out}}^{-1}AB_{\text{in}} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}. \quad (8)$$

Well, this was a tough section. We found that *x , x , x,* 1 have derivatives 3x<sup>2</sup> , 2x, 1, 0.

■ REVIEW OF THE KEY IDEAS ■1. If we know  $T(v_1), \dots, T(v_n)$  for a basis, linearity will determine all other  $T(v)$ .

$$2. \left\{ \begin{array}{l} \text{Linear transformation } T \\ \text{Input basis } v_1, \dots, v_n \\ \text{Output basis } w_1, \dots, w_m \end{array} \right\} \rightarrow \begin{array}{l} \text{Matrix } A \text{ (} m \text{ by } n \text{)} \\ \text{represents } T \\ \text{in these bases} \end{array}$$

3. The change of basis matrix  $B = W^{-1}V = B_{\text{out}}^{-1}B_{\text{in}}$  represents the identity  $T(v) = v$ .

4. If  $A$  and  $B$  represent  $T$  and  $S$ , and the output basis for  $S$  is the input basis for  $T$ , then the matrix  $AB$  represents the transformation  $T(S(u))$ .

5. The best input-output bases are eigenvectors and/or singular vectors of  $A$ . Then

$$B^{-1}AB = \Lambda = \text{eigenvalues} \quad B_{\text{out}}^{-1}AB_{\text{in}} = \Sigma = \text{singular values}.$$

■ WORKED EXAMPLES ■**8.2 A** The space of 2 by 2 matrices has these four “vectors” as a basis:

$$v_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \quad v_2 = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \quad v_3 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} \quad v_4 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}.$$

 $T$  is the linear transformation that *transposes* every 2 by 2 matrix. What is the matrix  $A$  that represents  $T$  in this basis (output basis = input basis)? What is the inverse matrix  $A^{-1}$ ? What is the transformation  $T^{-1}$  that inverts the transpose operation?

**Solution** Transposing those four “basis matrices” just reverses  $v_2$  and  $v_3$ :

$$\begin{array}{ll} T(v_1) = v_1 & \\ T(v_2) = v_3 & \text{gives the four columns of } A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \\ T(v_3) = v_2 & \\ T(v_4) = v_4 & \end{array}$$

The inverse matrix  $A^{-1}$  is the same as  $A$ . The inverse transformation  $T^{-1}$  is the same as  $T$ . If we transpose and transpose again, the final matrix equals the original matrix.

Notice that the space of 2 by 2 matrices is 4-dimensional. So the matrix  $A$  (for the transpose  $T$ ) is 4 by 4. The nullspace of  $A$  is  $\mathbf{Z}$  and the kernel of  $T$  is the zero matrix—the only matrix that transposes to zero. The eigenvalues of  $A$  are 1, 1, 1, -1.

Which line of matrices has  $T(A) = A^T = -A$  with that eigenvalue  $\lambda = -1$ ?

### **Problem Set 8.2**

#### **Questions 1-4 extend the first derivative example to higher derivatives.**

**<sup>1</sup>**The transformation *S* takes the *second derivative.* Keep 1, x, x 2 , x*3* as the input basis vi, v<sup>2</sup> , V3, V4 and also as output basis w1, w<sup>2</sup> , W3, W4. Write S(v1), S(v2), S( v3), S( v4) in terms of thew's. Find the 4 by 4 matrix A2 for S. **<sup>2</sup>**What functions have S ( *v)* = **O?** They are in the kernel of the second derivative S. What vectors are in the nullspace of its matrix A2 in Problem 1? **<sup>3</sup>**The second derivative A2 is not the square of a rectangular first derivative matrix A1:

| $A_1 = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix}$ | does not allow $A_1^2 = A_2$ . |
|---------------------------------------------------------------------------------------|--------------------------------|
|---------------------------------------------------------------------------------------|--------------------------------|

Add a zero row 4 to A1 so that output space= input space. Compare *Ar* with A2. Conclusion: We want output basis = \_\_ basis. Then *m* = *n.* 

- **<sup>4</sup>**(a) The product TS of first and second derivatives produces the *third* derivative. Add zeros to make 4 by 4 matrices, then compute A1A2<sup>=</sup>A3.
  - (b) The matrix *A�* corresponds to S <sup>2</sup>= *fourth* derivative. Why is this zero?

#### **Questions 5-9 are about a particular transformation** *T* **and its matrix** *A.*

**<sup>5</sup>**With bases V1, V<sup>2</sup> , V3 andw1, w<sup>2</sup> , W3, suppose T(v1) = w2 and T(v2) = T(v3) <sup>=</sup> w1 + *w<sup>3</sup> . T* is a linear transformation. Find the matrix *A* and multiply by the vector (1, 1, 1). What is the output from *T* when the input is v1 + v2<sup>+</sup>v3? **<sup>6</sup>**Since T( v<sup>2</sup> ) = T( v3), the solutions to T( v) = **<sup>0</sup>**are v = \_\_ . What vectors are in the nullspace of A? Find all solutions to T ( *v)* = w2. **<sup>7</sup>**Find a vector that is not in the column space of *A.* Find a combination of *w's* that is not in the range of the transformation *T.*  **<sup>8</sup>**You don't have enough information to determine T<sup>2</sup> . Why is its matrix not necessarily A<sup>2</sup> ? What more information do you need? **<sup>9</sup>**Find the *rank* of *A.* The rank is not the dimension of the whole output space **W.** It is the dimension of the of *T.* 

#### **Questions 10-13 are about invertible linear transformations.**

- **<sup>10</sup>**Suppose T(v1) = w1 + w2<sup>+</sup>W3 and T(v2) = w2<sup>+</sup>w3 and T(v3) = W3. Find the matrix *A* for T using these basis vectors. What input vector *v* gives *T( v)* = w1? **<sup>11</sup>**Invert the matrix *A* in Problem 10. Also invert the transformation T-what are r- 1 (wi) and r-1 (w<sup>2</sup> ) and r-1 (w3)? **<sup>12</sup>**Which of these are true and why is the other one ridiculous?
  - (a) *r-<sup>1</sup>r* =*I* (b) r- <sup>1</sup> (T(v<sup>1</sup> )) = v1 (c) r-1 (T(w1)) = w1.

- 13 Suppose the spaces V and W have the same basis v1, v<sup>2</sup> .
  - (a) Describe a transformation *T* (not I) that is its own inverse.
  - (b) Describe a transformation *T* (not I) that equals T .
  - (c) Why can't the same T be used for both (a) and (b)?

#### Questions 14-19 are about changing the basis.

- 14 (a) What matrix *B* transforms (1, 0) into (2, 5) and transforms (0, 1) to (1, 3)?
  - (b) What matrix *C* transforms (2, 5) to (1, 0) and (1, 3) to (0, 1)?
- (c) Why does no matrix transform (2, 6) to (1, 0) and (1, 3) to (0, 1)? 15 (a) What matrix M transforms (1, 0) and (0, 1) to *(r,* t) and *(s, u)?*
  - (b) What matrix *N* transforms *(a,* c) and *(b, d)* to (1, 0) and (0, 1)?
- (c) What condition on *a, b,* c, *d* will make part (b) impossible? 16 (a) How do Mand Nin Problem 15 yield the matrix that transforms *(a,* c) to *(r, t)* and *(b, d)* to *(s, u)?*
- (b) What matrix transforms (2, 5) to (1, 1) and (1, 3) to (0, 2)? 17 If you keep the same basis vectors but put them in a different order, the change of basis matrix *B* is a \_\_ matrix. If you keep the basis vectors in order but change their lengths, *B* is a \_\_ matrix. 18 The matrix that rotates the axis vectors ( 1, 0) and ( 0, 1) through an angle 0 is *Q.*  What are the coordinates ( *a, b)* of the original ( 1, 0) using the new (rotated) axes? This *inverse* can be tricky. Draw a figure or solve for *a* and b:

$$Q = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = a \begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix} + b \begin{bmatrix} -\sin \theta \\ \cos \theta \end{bmatrix}.$$

19 The matrix that transforms (1, 0) and (0, 1) to (1, 4) and (1, 5) is *B* = The combination a(l, 4) + b(l, 5) that equals (1, 0) has *(a, b)* = ( , ). How are those new coordinates of (1, 0) related to *B* or B-17

#### Questions 20-23 are about the space of quadratic polynomials y = *A* + *Bx* + *C x<sup>2</sup> •*

- 20 The parabola w1 = ½(x<sup>2</sup>+x) equals one at x = 1, and zero at x = 0 and x = -1. Find the parabolas w2, w3, and then find y(x) by linearity.
  - (a) w2 equals one at x = 0 and zero at x = 1 and x = -1.
  - (b) w3 equals one at x = -1 and zero at x = 0 and x = 1.
- (c) y(x) equals 4 at x = 1 and 5 at x = 0 and 6 at x = -1. Use w1, w<sup>2</sup> , W3. 21 One basis for second-degree polynomials is v1 = 1 and v2 = *x* and v3 = x<sup>2</sup> . Another basis is w1, w<sup>2</sup> , w3 from Problem 20. Find two change of basis matrices, from thew's to the v's and from the v's to thew's.

- 22 What are the three equations for *A, B, C* if the parabola y *=A+ Bx+ Cx<sup>2</sup>*equals 4 at *x* = *a* and 5 at *x* = *b* and 6 at *x* = c? Find the determinant of the 3 by 3 matrix. That matrix transforms values like 4, 5, 6 to parabolas *y-or* is it the other way? **<sup>23</sup>**Under what condition on the numbers m<sup>1</sup> , m<sup>2</sup> , ... , m9 do these three parabolas give a basis for the space of all parabolas *a* + *bx* + cx2 ? V1 = m1 + m2x + m3x , v2 = m4 + *m5x* + m5x<sup>2</sup> , V3 = m7 + *msx* + mgx<sup>2</sup> . 24 The Gram-Schmidt process changes a basis a<sup>1</sup> , a<sup>2</sup> , a3 to an orthonormal basis q1 , q2 , *q<sup>3</sup> .* These are columns in *A* = *QR.* Show that *R* is the change of basis matrix from the a's to the *q's* (a**2** is what combination of *q's* when *A= QR?).* 25 Elimination changes the rows of A to the rows of U with A = LU. Row 2 of A is what combination of the rows of U? Writing A <sup>T</sup>=UT L <sup>T</sup>to work with columns, the change of basis matrix is *B* = LT. We have *bases* if the matrices are \_\_ . 26 Suppose v<sup>1</sup> , v<sup>2</sup> , v3 are eigenvectors for *T.* This means *T(* vi) = *Ai Vi* for i = 1, 2, 3. What is the matrix for *T* when the input and output bases are the v's? 27 Every invertible linear transformation can have I as its matrix! Choose any input basis v<sup>1</sup> , ... , *Vn.* For output basis choose *Wi* <sup>=</sup>*T(* vi)- Why must *T* be invertible? **<sup>28</sup>**Using v1 = w1 and v2 = w2 find the standard matrix for these *T's:*
- (a) *T(vi)* = 0 and T(v<sup>2</sup> ) = 3v1 (b) T(v<sup>1</sup> ) = v1 and *T(v1*<sup>+</sup>v<sup>2</sup> ) = v1. **<sup>29</sup>**Suppose *T* reflects the *xy* plane across the *x* axis and *S* is reflection across the *y* axis. If *v* = *(x,* y) what is *S(T( v* ))? Find a simpler description of the product *ST.* 30 Suppose Tis reflection across the 45° line, and *S* is reflection across the y axis. If *v* = (2, 1) then *T(v)* = (1, 2). Find *S(T(v))* and *T(S(v)).* Usually *ST# TS.* **31 The product of two reflections** is **a rotation.** Multiply these reflection matrices to find the rotation angle: [ cos 20 sin 20] sin 20 - cos 20 [ cos 2a sin 2a] sin 2a - cos 2a **<sup>32</sup>**Suppose A is a 3 by 4 matrix of rank *r* = 2, and *T(* v) = Av. Choose input basis vectors v<sup>1</sup> , v2 from the row space of *A* and v*3,* v*4*from the nullspace. Choose output basis vectors w1 = Av*1,* w2 = Av*2* in the column space and w*3*from the nullspace of AT. What specially simple matrix represents Tin these special bases? 33 The space M of 2 by 2 matrices has the basis v<sup>1</sup> , v2, v*3,* v*4*in Worked Example **8.2 A.** Suppose *T* multiplies each matrix by [ � �] . With w 's equal to *v's,* what 4 by 4 matrix *A* represents this transformation *Ton* matrix space? **<sup>34</sup>**True or False: If we know *T(v)* for *n* different nonzero vectors in *R<sup>n</sup> ,* then we know *T* ( v) for every vector v in *R<sup>n</sup> .*

| $\begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}$ | $\begin{bmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|

# **8.3 The Search for a Good Basis**

1 With a new input basis Bin and output basis Bout , every matrix *A* becomes *B�t* AB;**0.**  Bin <sup>=</sup>Bout = **"generalized eigenvectors of** *A"* produces the **Jordan form** J = B- <sup>1</sup>*AB.*  The **Fourier matrix** *F* = Bin = Bout diagonalizes every circulant matrix (use the **FFT).**  Sines and cosines, Legendre and Chebyshev: those are great bases for **function space.** 

This is an important section of the book. I am afraid that most readers will skip it-or won't get this far. The first chapters prepared the way by explaining the idea of a **basis.**  Chapter 6 introduced the eigenvectors x and Chapter 7 found singular vectors v and u. Those are two winners but many other choices are very valuable.

First comes the pure algebra from Section 8.2 and then come good bases. The input basis vectors will be the columns of B;0• The output basis vectors will be the columns of Bout· Always B;0 and Bout are *invertible-basis* vectors are independent!

**Pure algebra** If *A* is the matrix for a transformation *T* in the standard basis, then

*B;;:}* AB;**0** is the matrix in the new bases. (1)

The standard basis vectors are the *columns of the identity:* B;n = Inxn and Bout = Imx <sup>m</sup> · Now we are choosing special bases to make the matrix clearer and simpler than *A.* When Bin <sup>=</sup>Bout = *B,* the square matrix B- <sup>1</sup>*AB* is *similar* to *A.* 

**Applied algebra** Applications are all about choosing good bases. Here are four important choices for vectors and three choices for functions. Eigenvectors and singular vectors led to A and I: in Section 8.2. The Jordan form is new.

- **1 B;0** =Bout= **eigenvector matrix** *X.* Then **x- <sup>1</sup>***AX* <sup>=</sup>**eigenvalues in A.**  This choice requires *A* to be a square matrix with n independent eigenvectors. "A must be diagonalizable." We get A when B;0<sup>=</sup>Bout is the eigenvector matrix X. 2 B;0 = *V* and Bout = *U:* singular vectors of *A.* Then u- <sup>1</sup>*AV* = diagonal :E. I: is the singular value matrix (with u1, ... , *O"r* on its diagonal) when Bin and Bout are the singular vector matrices *V* and *U.* Recall that those columns of Bin and Bout are orthonormal eigenvectors of A <sup>T</sup>A andAA <sup>T</sup> . Then A= UI:V<sup>T</sup>gives I:= u- <sup>1</sup>AV. **3 B;0** = Bout = **generalized eigenvectors of** *A.* Then **B-<sup>1</sup>***AB=* **Jordan form** *J. A* is a square matrix but it may only have *s* independent eigenvectors. (If *s* = *n* then *B* is *X* and J is A.) In all cases Jordan constructed n - s additional "generalized" eigenvectors, aiming to make the Jordan form J *as diagonal as possible* :
  - i) There ares square blocks along the diagonal of *J.*
  - ii) Each block has one eigenvalue >., one eigenvector, and 1 's above the diagonal.

The good case has n l x 1 blocks, each containing an eigenvalue. Then J is A ( diagonal).

**Example 1** This Jordan matrix  $J$  has eigenvalues  $\lambda = 2, 2, 3, 3$  (two double eigenvalues). Those eigenvalues lie along the diagonal because  $J$  is triangular. There are two independent eigenvectors for  $\lambda = 2$ , but there is only *one line of eigenvectors* for  $\lambda = 3$ . This will be true for every matrix  $C = BJB^{-1}$  that is similar to  $J$ .

$$\text{Jordan matrix } J = \begin{bmatrix} 2 & & & \\ & 2 & & \\ & & 3 & 1 \\ & & 0 & 3 \end{bmatrix} \quad \begin{array}{l} \text{Two 1 by 1 blocks} \\ \text{One 2 by 2 block} \\ \text{Three eigenvectors} \\ \text{Eigenvalues } 2, 2, 3, 3 \end{array}$$

Two eigenvectors for  $\lambda = 2$  are  $x_1 = (1, 0, 0, 0)$  and  $x_2 = (0, 1, 0, 0)$ . One eigenvector for  $\lambda = 3$  is  $x_3 = (0, 0, 1, 0)$ . The “generalized eigenvector” for this Jordan matrix is the fourth standard basis vector  $x_4 = (0, 0, 0, 1)$ . The eigenvectors for  $J$  (normal and generalized) are just the columns  $x_1, x_2, x_3, x_4$  of the identity matrix  $I$ .

*Notice  $(J - 3I)x_4 = x_3$ .* **The generalized eigenvector  $x_4$  connects to the true eigenvector  $x_3$ .** A true  $x_4$  would have  $(J - 3I)x_4 = 0$ , but that doesn’t happen here.

Every matrix  $C = BJB^{-1}$  that is similar to this  $J$  will have true eigenvectors  $b_1, b_2, b_3$  in the first three columns of  $B$ . The fourth column of  $B$  will be a generalized eigenvector  $b_4$  of  $C$ , tied to the true  $b_3$ . Here is a quick proof that uses  $Bx_3 = b_3$  and  $Bx_4 = b_4$  to show: The fourth column  $b_4$  is tied to  $b_3$  by  $(C - 3I)b_4 = b_3$ .

$$(BJB^{-1} - 3I)b_4 = BJx_4 - 3Bx_4 = B(J - 3I)x_4 = Bx_3 = b_3. \quad (2)$$

The point of Jordan’s theorem is that every square matrix  $A$  has a complete set of eigenvectors and generalized eigenvectors. When those go into the columns of  $B$ , the matrix  $B^{-1}AB = J$  is in Jordan form. Based on Example 1, here is a description of  $J$ .

## The Jordan Form

For every  $A$ , we want to choose  $B$  so that  $B^{-1}AB$  is as *nearly diagonal as possible*. When  $A$  has a full set of  $n$  eigenvectors, they go into the columns of  $B$ . Then  $B = X$ . The matrix  $X^{-1}AX$  is diagonal, period. This is the Jordan form of  $A$ —when  $A$  can be diagonalized. In the general case, eigenvectors are missing and  $\Lambda$  can’t be reached.

Suppose  $A$  has  $s$  independent eigenvectors. Then it is similar to a Jordan matrix with  $s$  blocks. Each block has an *eigenvalue on the diagonal with 1’s just above it*. This block accounts for exactly one eigenvector of  $A$ . Then  $B$  contains generalized eigenvectors as well as ordinary eigenvectors.

When there are  $n$  eigenvectors, all  $n$  blocks will be 1 by 1. In that case  $J = \Lambda$ .

The Jordan form solves the differential equation  $du/dt = Au$  for **any square matrix**  $A = BJB^{-1}$ . The solution  $e^{At}u(0)$  becomes  $u(t) = Be^{Jt}B^{-1}u(0)$ .  $J$  is triangular and its matrix exponential  $e^{Jt}$  involves  $e^{\lambda t}$  times powers  $1, t, \dots, t^{s-1}$ .

**(Jordan form)** If *A* has s independent eigenvectors, it is similar to a matrix J that has *s* Jordan blocks J1 ... , *J5* on its diagonal. Some matrix *B* puts *A* into Jordan form:

Jordan form 
$$B^{-1}AB = \begin{bmatrix} J_1 & & \\ & \ddots & \\ & & J_s \end{bmatrix} = J.$$
 (3)

Each block Ji has one eigenvalue *Ai,* one eigenvector, and 1 's just above the diagonal:

$$\text{Jordan block } J_i = \begin{bmatrix} \lambda_i & 1 & & \\ & \ddots & & \\ & & \ddots & 1 \\ & & & \lambda_i \end{bmatrix}. \quad (4)$$

*Matrices are similar if they share the same Jordan form J-not otherwise.* 

The Jordan form J has an off-diagonal 1 for each missing eigenvector (and the l's are next to the eigenvalues). In every family of similar matrices, we are picking one outstanding member called J. It is nearly diagonal ( or if possible completely diagonal). We can quickly solve *du/ dt* = *Ju* and take powers *J k .* Every other matrix in the family has the form *BJ* B-<sup>1</sup> .

Jordan's Theorem is proved in my textbook *Linear Algebra and Its Applications.*  Please refer to that book (or more advanced books) for the proof. The reasoning is rather intricate and in actual computations the Jordan form is not at all popular-its calculation is not stable. A slight change in *A* will separate the repeated eigenvalues and remove the off-diagonal 1 's-switching Jordan to a diagonal A.

Proved or not, you have caught the central idea of similarity-to make *A* as simple as possible while preserving its essential properties. The best basis *B* gives B-<sup>1</sup>*AB* = J.

**Question** Find the eigenvalues and all possible Jordan forms if *A* <sup>2</sup>=zero matrix.

**Answer** The eigenvalues must all be zero, because *Ax* = AX leads to *A <sup>2</sup>x* = A *<sup>2</sup>x* = *Ox.*  The Jordan form of *A* has J <sup>2</sup>=0 because J <sup>2</sup>=(B-<sup>1</sup>*AB)(B-<sup>1</sup>AB)* = B-1 A <sup>2</sup>*B* = 0. Every block in J has *A=* 0 on the diagonal. Look at Jf for block sizes 1, 2, 3:

| $[\ 0\ ]^2 = [\ 0\ ]$ | $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}^2 = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}^2 = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ |
|-----------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|-----------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|

Conclusion: If J <sup>2</sup>=0 then all block sizes must be 1 or 2. J <sup>2</sup>is not zero for 3 by 3.

The rank of J (and *A)* will be the total number of 1 's. **The maximum rank is** n/2. This happens when there are *n/2* blocks, each of size 2 and rank 1.

Now come the great bases of applied mathematics. Their discrete forms are vectors in R n . Their continuous forms are functions in a function space. Since they are chosen once and for all, *without knowing the matrix A,* these bases Bin = *Bout* probably don't diagonalize *A.* But for many important matrices *A* in applied mathematics, the matrices *B�<sup>1</sup>AB* are *close to diagonal.* 

## 4 B;n = Bout <sup>=</sup>Fourier matrix *F* Then *Fx* is a Disc.rete Fourier Transform of *x.*

Those words are telling us : The Fourier matrix with columns ( 1, . .\, .,\, 2 , .,\, 3 ) in equation (6) is important. Those are good basis vectors to work with.

We ask: Which matrices are diagonalized by *F?* This time we are starting with the eigenvectors ( 1, >-, ), <sup>2</sup> , .,\, <sup>3</sup> ) and finding the matrices that have those eigenvectors :

$$\text{If } \lambda^4 = 1 \text{ then } Px = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ \lambda \\ \lambda^2 \\ \lambda^3 \end{bmatrix} = \lambda \begin{bmatrix} 1 \\ \lambda \\ \lambda^2 \\ \lambda^3 \end{bmatrix} = \lambda x. \quad (5)$$

P is a permutation matrix. The equation Px >-x says that x is an eigenvector and .,\, is an eigenvalue of *P.* Notice how the fourth row of this vector equation is 1 = .,\, <sup>4</sup> . That rule for ), makes everything work.

Does this give four different eigenvalues.,\,? *Yes.* The four numbers.,\,= 1, i, -1, -i all satisfy .,\,4 = 1. (You lmow i <sup>2</sup>= -1. Squaring both sides gives i <sup>4</sup>= 1.) So those four numbers are the eigenvalues of *P,* each with its eigenvector x = (1, >-, ), 2, .,\,<sup>3</sup> ). The eigenvector matrix *F* diagonalizes the permutation matrix *P* :

| <span> </span> | <b>Eigenvalue</b>                  | $\begin{bmatrix} 1 & i & \\ & -1 & \\ & & -i \end{bmatrix}$ | <b>Eigenvector</b> | $\begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ i & i & i & i & i \\ 1 & i^2 & i & i & i \\ 1 & i^3 & i & i & i \\ 1 & i^4 & i & i & i \end{bmatrix}$ | <b>A1</b> |  |
|----------------|------------------------------------|-------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------|--|
| <span> </span> | <b>matrix <math>\Lambda</math></b> |                                                             |                    |                                                                                                                                             |           |  |

Those columns of Fare orthogonal because they are eigenvectors of *P* (an orthogonal matrix). Unfortunately this Fourier matrix *F* is complex (it is the most important complex matrix in the world). Multiplications *Fx* are done millions of times very quickly, by the Fast Fourier Transform. The FFT comes in Section 9.3.

Key question : What other matrices beyond *P* have this same eigenvector matrix *F* ? We know that P *<sup>2</sup>*and P*3* and P <sup>4</sup>have the same eigenvectors as P. The same matrix F diagonalizes all powers of P. And the eigenvalues of P*2* and P*3* and P4 are the numbers .,\, <sup>2</sup>and .,\,3 and .,\,<sup>4</sup> . For example *P<sup>2</sup>*x = >-*2*x:

$$P^2 \mathbf{x} = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ \lambda \\ \lambda^2 \\ \lambda^3 \end{bmatrix} = \lambda^2 \begin{bmatrix} 1 \\ \lambda \\ \lambda^2 \\ \lambda^3 \end{bmatrix} = \lambda^2 \mathbf{x} \text{ when } \lambda^4 = 1.$$

The fourth power is special because  $P^4 = I$ . When we do the “cyclic permutation” four times,  $P^4 x$  is the same vector  $x$  that we started with. The eigenvalues of  $P^4 = I$  are just 1, 1, 1, 1. And that number 1 agrees with the fourth power of all the eigenvalues of  $P$ :  $1^4 = 1$  and  $i^4 = 1$  and  $(-1)^4 = 1$  and  $(-i)^4 = 1$ .

One more step brings in many more matrices. If  $P$  and  $P^2$  and  $P^3$  and  $P^4 = I$  have the same eigenvector matrix  $F$ , so does any combination  $C = c_1 P + c_2 P^2 + c_3 P^3 + c_0 I$ :

$$\text{Circulant matrix } C = \begin{bmatrix} c_0 & c_1 & c_2 & c_3 \\ c_3 & c_0 & c_1 & c_2 \\ c_2 & c_3 & c_0 & c_1 \\ c_1 & c_2 & c_3 & c_0 \end{bmatrix} \begin{array}{l} \text{has eigenvectors in the Fourier matrix } F \\ \text{has four eigenvalues } c_0 + c_1 \lambda + c_2 \lambda^2 + c_3 \lambda^3 \\ \text{from the four numbers } \lambda = 1, i, -1, -i \\ \text{The eigenvalue from } \lambda = 1 \text{ is } c_0 + c_1 + c_2 + c_3 \end{array}$$

That was a big step. We have found all the matrices (circulant matrices  $C$ ) whose eigenvectors are the Fourier vectors in  $F$ . We also know the four eigenvalues of  $C$ , but we haven’t given them a good formula or a name until now:

$$\text{The four eigenvalues of } C \text{ are given by the Fourier transform } Fc \quad Fc = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ c_3 \end{bmatrix} = \begin{bmatrix} c_0 + c_1 + c_2 + c_3 \\ c_0 + ic_1 - c_2 - ic_3 \\ c_0 - c_1 + c_2 - c_3 \\ c_0 - ic_1 - c_2 + ic_3 \end{bmatrix}$$

**Example 2** The same ideas work for a Fourier matrix  $F$  and a circulant matrix  $C$  of any size. Two by two matrices look trivial but they are very useful. Now eigenvalues of  $P$  have  $\lambda^2 = 1$  instead of  $\lambda^4 = 1$  and the complex number  $i$  is not needed:  $\lambda = \pm 1$ .

$$\text{Fourier matrix } F \text{ from eigenvectors of } P \text{ and } C \quad F = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \quad P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \quad \text{Circulant } C = \begin{bmatrix} c_0 & c_1 \\ c_1 & c_0 \end{bmatrix}.$$

The eigenvalues of  $C$  are  $c_0 + c_1$  and  $c_0 - c_1$ . Those are given by the Fourier transform  $Fc$  when the vector  $c$  is  $(c_0, c_1)$ . This transform  $Fc$  gives the eigenvalues of  $C$  for any size  $n$ .

Notice that **circulant matrices have constant diagonals**. The same number  $c_0$  goes down the main diagonal. The number  $c_1$  is on the diagonal above, and that diagonal “wraps around” or “circles around” to the southwest corner of  $C$ . This explains the name *circulant* and it indicates that these matrices are *periodic* or *cyclic*. Even the powers of  $\lambda$  cycle around because  $\lambda^4 = 1$  leads to  $\lambda^5, \lambda^6, \lambda^7, \lambda^8 = \lambda, \lambda^2, \lambda^3, \lambda^4$ .

Constancy down the diagonals is a crucial property of  $C$ . It corresponds to *constant coefficients* in a differential equation. This is exactly when Fourier works perfectly!

$$\text{The equation } \frac{d^2 u}{dt^2} = -u \quad \text{is solved by } u = c_0 \cos t + c_1 \sin t.$$

$$\text{The equation } \frac{d^2 u}{dt^2} = tu \quad \text{cannot be solved by elementary functions.}$$

These equations are linear. The first is the oscillation equation for a simple spring. It is Newton’s Law  $f = ma$  with mass  $m = 1$ ,  $a = d^2 u / dt^2$ , and force  $f = -u$ . Constant coefficients produce the differential equations that you can really solve.

The equation *u 11* = *tu* has a variable coefficient *t.* This is Airy's equation in physics and optics (it was derived to explain a rainbow). The solutions change completely when *<sup>t</sup>* passes through zero, and those solutions require infinite series. *We won't go there.*

The point is that equations with constant coefficients have simple solutions like e . You discover ,\ by substituting e >-t into the differential equation. That number ,\ is like an eigenvalue. For *u* = cost and *u* = sin *t* the number is ,\ = i. Euler's great formula e it =cost+ i sin *t* introduces complex numbers as we saw in the eigenvalues of *P* and *C.*

# **Bases for Function Space**

For functions of *x,* the first basis I would think of contains the powers 1, *x,* x , *x , ...* Unfortunately this is a terrible basis. Those functions x <sup>n</sup>are just barely independent. *x* <sup>10</sup>is *almost* a combination of other basis vectors 1, *x, ... , x*<sup>9</sup> . It is virtually impossible to compute with this poor "ill-conditioned" basis.

If we had vectors instead of functions, the test for a good basis would look at *B<sup>T</sup>B.* This matrix contains all inner products between the basis vectors (columns of B). *The basis is orthonormal when B<sup>T</sup>B* = *I.* That is best possible. But the basis 1, *x,* x , ... produces the evil **Hilbert matrix** : *B<sup>T</sup>B* has an enormous ratio between its largest and smallest eigenvalues. A large condition number signals an unhappy choice of basis.

*Note* Now the columns of *B* are functions instead of vectors. We still use *B<sup>T</sup>B* to test for independence. So we need to know the dot product (inner product is a better name) of two functions-those are the numbers in *B<sup>T</sup>B.*

The dot product of vectors is just x <sup>T</sup> y = x1y1 + · · · + XnY<sup>n</sup> · The inner product of functions will integrate instead of adding, but the idea is completely parallel :

Inner product 
$$(f, g) \equiv \int f(x)g(x) dx$$

Complex inner product 
$$(\mathbf{f}, \mathbf{g}) = \int \bar{f}(\mathbf{x}) g(\mathbf{x}) d\mathbf{x}$$
,  $\bar{\mathbf{f}} = \text{complex conjugate}$ 

Weighted inner product *(f, g*) <sup>w</sup>*fw(x)f(x) g(x)dx, w=* weightfunction When the integrals go from *x* = 0 to *x* = 1, the inner product of *x <sup>i</sup>*with *x<sup>j</sup>*is

$$\int_0^1 x^i x^j dx = \frac{x^{i+j+1}}{i+j+1} \bigg]_{x=0}^{x=1} = \frac{1}{i+j+1} = \text{entries of Hilbert matrix } B^T B$$

By changing to the symmetric interval from *x* = -1 to *x* = 1, we immediately have *orthogonality between all even functions and all odd functions:* 

| Interval $[-1, 1]$ | $\int_{-1}^1 x^2 x^5 dx = 0$ | $\int_{-1}^1 \text{even}(x) \text{odd}(x) dx = 0.$ |
|--------------------|------------------------------|----------------------------------------------------|
|                    |                              |                                                    |

This change makes half of the basis functions orthogonal to the other half. It is so simple that we continue using the symmetric interval -1 to 1 (or -1r to 1r). But we want a better basis than the powers x n-hopefully an orthogonal basis.

### **Orthogonal Bases for Function Space**

Here are the three leading even-odd bases for theoretical and numerical computations:

| <b>5. The Fourier basis</b>   | $1, \sin x, \cos x, \sin 2x, \cos 2x, \dots$         |
|-------------------------------|------------------------------------------------------|
| <b>6. The Legendre basis</b>  | $1, x, x^2 - \frac{1}{3}, x^3 - \frac{3}{5}x, \dots$ |
| <b>7. The Chebyshev basis</b> | $1, x, 2x^2 - 1, 4x^3 - 3x, \dots$                   |

The Fourier basis functions (sines and cosines) are all *periodic.* They repeat over every 21r interval because cos(x+21r) = cos *x* and sin(x+21r) = sin *x.* So this basis is especially good for functions *f* ( x) that are themselves periodic : *f* ( x + 21r) = *f* ( x).

This basis is also *orthogonal.* Every sine and cosine is orthogonal to every other sine and cosine. Of course we don't expect the basis function cos nx to be orthogonal to itself.

Most important, the sine-cosine basis is also *excellent for approximation.* If we have a smooth periodic function *f* ( x), then a few sines and cosines (low frequencies) are all we need. Jumps in f(x) and noise in the signal are seen in higher frequencies (larger *n).* We hope and expect that the signal is not drowned by the noise.

The *Fourier transform* connects *f* ( x) to the coefficients ak and bk in its Fourier series:

| Fourier series | $f(x) = a_0 + b_1 \sin x + a_1 \cos x + b_2 \sin 2x + a_2 \cos 2x + \dots$ |
|----------------|----------------------------------------------------------------------------|
|                |                                                                            |

We see that **function space is infinite-dimensional.** It takes infinitely many basis functions to capture perfectly a typical *f* ( x). But the formula for each coefficient (for example a3) is just like the formula b <sup>T</sup>a/ a <sup>T</sup> a for projecting a vector *b* onto the line through a.

Here we are projecting the function *f* ( x) onto the line in function space through cos *3x* :

**Fourier coefficient 
$$a_3$$** =  $\frac{(f(x), \cos 3x)}{(\cos 3x, \cos 3x)} = \frac{\int f(x) \cos 3x dx}{\int \cos 3x \cos 3x dx}$ . (7)

**Example 3** The double angle formula in trigonometry is cos 2x = 2 cos2 x -1. This tells us that cos<sup>2</sup>*x*= ½ + ½ cos 2x. A very short Fourier series. So is sin<sup>2</sup>*x*= ½ - ½ cos 2x.

**Fourier series is just linear algebra in function space.** Let me explain that properly as a highlight of Chapter 10 about applications.

# **Legendre Polynomials and Chebyshev Polynomials**

The Legendre polynomials are the result of applying the Gram-Schmidt idea (Section 4.4). The plan is to orthogonalize the powers 1, *x,* x , . . . To start, the odd function *x* is already orthogonal to the even function 1 over the interval from -1 to 1. Their product ( *x)* ( 1) = *x*  integrates to zero. But the inner product between x <sup>2</sup>and 1 is *J* x <sup>2</sup>*dx* = 2/3:

| $\frac{(x^2, 1)}{(1, 1)} = \frac{\int x^2 dx}{\int 1 dx} = \frac{2/3}{2} = \frac{1}{3}$ | Gram-Schmidt gives $x^2 - \frac{1}{3} = \mathbf{Legendre}$ |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------|
|                                                                                         |                                                            |

Similarly the odd power *x <sup>3</sup>*has a component 3x / 5 in the direction of the odd function *x* :

$$\frac{(x^3, x)}{(x, x)} = \frac{\int x^4 dx}{\int x^2 dx} = \frac{2/5}{2/3} = \frac{3}{5} \quad \text{Gram-Schmidt gives } x^3 - \frac{3}{5}x = \text{Legendre}$$

Continuing Gram-Schmidt for *x 4 , x ,* ... produces every Legendre function-a good basis.

Finally we turn to the Chebyshev polynomials 1, *x,* 2x2 - 1, *4x<sup>3</sup>*- 3x. They don't come from Gram-Schmidt. Instead they are connected to 1, cos 0, cos 20, cos 30. This gives a giant computational advantage-we can use the Fast Fourier Transform. The connection of Chebyshev to Fourier appears when we set x = cos 0 :

| Chebyshev  | $2x^2 - 1 = 2(\cos \theta)^2 - 1 = \cos 2\theta$               |
|------------|----------------------------------------------------------------|
| to Fourier | $4x^3 - 3x = 4(\cos \theta)^3 - 3(\cos \theta) = \cos 3\theta$ |

The *n th* degree Chebyshev polynomial T<sup>n</sup> (x) converts to Fourier's cos *n0* = T<sup>n</sup> ( cos *0). Note* These polynomials are the basis for a big software project called **"chebfun".** Every function *f(x)* is replaced by a super-accurate Chebyshev approximation. Then you can integrate *f(x),* and solve *f(x)* = 0, and find its maximum or minimum. More than that, you can solve differential equations involving f ( x )-fast and to high accuracy.

When **chebfun** replaces *f(x)* by a polynomial, you are ready to solve problems.

#### **• REVIEW OF THE KEY IDEAS •**

- **1.** A basis is good if its matrix *B* is well-conditioned. Orthogonal bases are best.
- **2.** Also good if A= B-<sup>1</sup>*AB* is diagonal. But the Jordan form *J* can be very unstable.
- 3. The Fourier matrix diagonalizes constant-coefficient periodic equations: perfection.
- **4.** The basis 1, *x,* x , ... leads to *B <sup>T</sup>B* <sup>=</sup>Hillbert matrix: Terrible for computations.
- 5. Legendre and Chebyshev polynomials are excellent bases for function space.

# **Problem Set 8.3**

**<sup>1</sup>**In Example 1, what is the rank of *J* - *31* ? What is the dimension of its nullspace? This dimension gives the number of independent eigenvectors for ,,\ = 3. The algebraic multiplicity is 2, because det ( *J* - H) has the repeated factor ( ,,\ -3) <sup>2</sup> . The geometric multiplicity is 1, because there is only 1 independent eigenvector. **<sup>2</sup>**These matrices A1 and A2 are similar to *J.* Solve A1B1 = *B1J* and A2B2 = *B2J* to find the basis matrices B1 and B2 with *J* = B1 <sup>1</sup>A1B1 and *J* = R2 <sup>1</sup>A2B<sup>2</sup> .

$$J = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \quad A_1 = \begin{bmatrix} 0 & 4 \\ 0 & 0 \end{bmatrix} \quad A_2 = \begin{bmatrix} 4 & -8 \\ 2 & -4 \end{bmatrix}$$

**<sup>3</sup>**This transpose block *J <sup>T</sup>*has the same triple eigenvalue 2 (with only one eigenvector) as *J.* Find the basis change *B* so that *J* = B-1 *J <sup>T</sup>B* (which means *BJ= J <sup>T</sup>*B):

| $J = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$ | $J^T = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 1 & 2 \end{bmatrix}$ |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
|                                                                         |                                                                           |

**<sup>4</sup>***J* and *K* are Jordan forms with the same zero eigenvalues and the same rank 2. But show that no invertible *B* solves *BK* = *J B,* so *K is not similar to* J:

$$J = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \quad K = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

- **<sup>5</sup>**If *<sup>A</sup> <sup>3</sup>*= 0 show that all,,\ = 0, and all Jordan blocks with *J <sup>3</sup>*= 0 have size 1, 2, or
- 3. It follows that rank *(A)* ::; 2n/3. If *<sup>A</sup>n* = 0 why is rank *(A)* < *n?* **<sup>6</sup>**Show that *u(t)* = [ *<sup>t</sup> ::t <sup>t</sup>*] solves �: = *Ju* with *J* = [ � �] and *u(O)* = [ �]. *J* is not diagonalizable so *te >--t* enters the solution. 7 Show that the difference equation *Vk+<sup>2</sup>*- 2,,\vk+l + *,,\ vk* = 0 is solved by *Vk* = ,,\ *k* and also by *vk* = *k,,\ <sup>k</sup> .* Those correspond to *e >--t* and *te >--t* in Problem 6. 8 What are the 3 solutions to ,,\ <sup>3</sup>= 1? They are complex numbers,,\ = cos *0+i* sin *0* = . Then ,,\ <sup>3</sup>= *<sup>e</sup>* <sup>3</sup>*i*<sup>0</sup>= 1 when the angle *30* is O or 21r or 41r. Write the 3 by 3 Fourier matrix *F* with columns (1, ,,\, ,,\ ). **<sup>9</sup>**Check that any 3 by 3 circulant *C* has eigenvectors (1, >-, >- ) from Problem 8. If the diagonals of your matrix *C* contain c0, c1, c2 then its eigenvalues are in *Fe.* **<sup>10</sup>**Using formula(7)finda<sup>3</sup> cos3xin theFourierseries off(x) ={ � ;�;-f ! l:I! <sup>2</sup> �

