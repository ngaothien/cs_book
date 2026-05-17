# 8 Optimizations in the compiler

 
where a #define directive never takes memory space. A floating point constant always 
takes memory space, even when it has not been given a name. 
 
#define directives when used as macros are sometimes more efficient than functions. 
See page 49 for a discussion. 
 
7.35 Namespaces 
There is no cost in terms of execution speed to using namespaces. 
 
 
8 Optimizations in the compiler 
8.1 How compilers optimize 
Modern compilers can do a lot of modifications to the code in order to improve performance. 
It is useful for the programmer to know what the compiler can do and what it can not do. 
The following sections describe some of the compiler optimizations that it is relevant for the 
programmer to know about. 
Function inlining 
The compiler can replace a function call by the body of the called function. Example: 
 
// Example 8.1a 
float square (float a) { 
   return a * a;} 
 
float parabola (float x) { 
   return square(x) + 1.0f;} 
 
The compiler may replace the call to square by the code inside square: 
 
// Example 8.1b 
float parabola (float x) { 
   return x * x + 1.0f;} 
 
The advantages of function inlining are:  
The overhead of call and return and parameter transfer are eliminated. 
Code caching will be better because the code becomes contiguous. 
The code becomes smaller if there is only one call to the inlined function. 
Function inlining can open the possibility for other optimizations, as explained below. 
 
The disadvantage of function inlining is that the code becomes bigger if there is more than 
one call to the inlined function and the function is big. The compiler is more likely to inline a 
function if it is small or if it is called from only one or a few places. 
Constant folding and constant propagation 
An expression or subexpression containing only constants will be replaced by the calculated 
result. Example: 
 
// Example 8.2a 
double a, b; 
a = b + 2.0 / 3.0; 
 
The compiler will replace this by 
 
// Example 8.2b 


---

 
a = b + 0.666666666666666666667; 
 
This is actually quite convenient. It is easier to write 2.0/3.0 than to calculate the value 
and write it with many decimals. It is recommended to put a parenthesis around such a 
subexpression to make sure the compiler recognizes it as a subexpression. For example, 
b*2.0/3.0 will be calculated as (b*2.0)/3.0 rather than as b*(2.0/3.0) unless you 
put a parenthesis around the constant subexpression. 
 
A constant can be propagated through a series of calculations: 
 
// Example 8.3a 
float parabola (float x) { 
   return x * x + 1.0f;} 
 
float a, b; 
a = parabola (2.0f); 
b = a + 1.0f; 
 
The compiler may replace this by 
 
// Example 8.3b 
a = 5.0f; 
b = 6.0f; 
 
Constant folding and constant propagation is not possible if the expression contains a 
function which cannot be inlined or cannot be calculated at compile time. For example: 
 
// Example 8.4 
double a = sin(0.8); 
 
The sin function is defined in a separate function library and you cannot expect the 
compiler to be able to inline this function and calculate it at compile time. Some compilers 
are able to calculate the most common math functions such as sqrt and pow at compile-
time, but not the more complicated functions like sin. 
Pointer elimination 
A pointer or reference can be eliminated if the target pointed to is known. Example: 
 
// Example 8.5a 
void Plus2 (int * p) { 
   *p = *p + 2;} 
 
int a; 
Plus2 (&a); 
 
The compiler may replace this by 
 
// Example 8.5b 
a += 2; 
Common subexpression elimination 
If the same subexpression occurs more than once then the compiler may calculate it only 
once. Example: 
 
// Example 8.6a 
int a, b, c; 
b = (a+1) * (a+1); 
c = (a+1) / 4; 
 


---

 
The compiler may replace this by 
 
// Example 8.6b 
int a, b, c, temp; 
temp = a+1; 
b = temp * temp; 
c = temp / 4; 
Register variables 
The most commonly used variables are stored in registers (see page 27).  
 
The maximum number of integer register variables is approximately six in 32-bit systems 
and fourteen in 64-bit systems. 
 
The maximum number of floating point register variables is eight in 32-bit systems and 
sixteen in 64-bit systems. Some compilers have difficulties making floating point register 
variables in 32-bit systems unless the SSE2 (or later) instruction set is enabled. 
 
The compiler will choose the variables that are used most for register variables. This 
includes pointers and references, which can be stored in integer registers. Typical 
candidates for register variables are temporary intermediates, loop counters, function 
parameters, pointers, references, 'this' pointer, common subexpressions, and induction 
variables (see below). 
 
A variable cannot be stored in a register if its address is taken, i.e. if there is a pointer or 
reference to it. Therefore, you should avoid making any pointer or reference to a variable 
that could benefit from register storage. 
Live range analysis 
The live range of a variable is the range of code in which the variable is used. An optimizing 
compiler can use the same register for more than one variable if their live-ranges do not 
overlap or if they are sure to have the same value. This is useful when the number of 
available registers is limited. Example: 
 
// Example 8.7 
int SomeFunction (int a, int x[]) { 
   int b, c; 
   x[0] = a; 
   b = a + 1; 
   x[1] = b; 
   c = b + 1; 
   return c; 
} 
 
In this example, a, b and c can share the same register because their live ranges do not 
overlap. If c = b + 1 is changed to c = a + 2 then a and b cannot use the same 
register because their live ranges now overlap. 
 
Compilers do not normally use this principle for objects stored in memory. It will not use the 
same memory area for different objects even when their live ranges do not overlap. See 
page 90 for an example of how to make different objects share the same memory area. 
Join identical branches 
The code can be made more compact by joining identical pieces of code. Example: 
 
// Example 8.8a 
double x, y, z;  bool b; 
if (b) { 
   y = sin(x); 


---

 
   z = y + 1.; 
} 
else { 
   y = cos(x); 
   z = y + 1.; 
} 
 
The compiler may replace this by 
 
// Example 8.8b 
double x, y;  bool b; 
if (b) { 
   y = sin(x); 
} 
else { 
   y = cos(x); 
} 
z = y + 1.; 
 
Eliminate jumps 
Jumps can be avoided by copying the code that it jumps to. Example: 
 
// Example 8.9a 
int SomeFunction (int a, bool b) { 
   if (b) { 
      a = a * 2; 
   } 
   else { 
      a = a * 3; 
   } 
   return a + 1; 
} 
 
This code has a jump from a=a*2; to return a+1;. The compiler can eliminate this jump 
by copying the return statement: 
 
// Example 8.9b 
int SomeFunction (int a, bool b) { 
   if (b) { 
      a = a * 2; 
      return a + 1; 
   } 
   else { 
      a = a * 3; 
      return a + 1; 
   } 
} 
 
A branch can be eliminated if the condition can be reduced to always true or always false: 
 
// Example 8.10a 
if (true) { 
   a = b; 
} 
else { 
   a = c; 
} 
 
Can be reduced to: 
 
// Example 8.10b 


---

 
a = b; 
 
A branch can also be eliminated if the condition is known from a previous branch. Example: 
 
// Example 8.11a 
int SomeFunction (int a, bool b) { 
   if (b) { 
      a = a * 2; 
   } 
   else { 
      a = a * 3; 
   } 
   if (b) { 
      return a + 1; 
   } 
   else { 
      return a - 1; 
   } 
} 
 
The compiler may reduce this to: 
 
// Example 8.11b 
int SomeFunction (int a, bool b) { 
   if (b) { 
      a = a * 2; 
      return a + 1; 
   } 
   else { 
      a = a * 3; 
      return a - 1; 
   } 
} 
Loop unrolling 
Some compilers will unroll loops if a high degree of optimization is requested. See page 45. 
This may be advantageous if the loop body is very small or if it opens the possibility for 
further optimizations. Loops with a very low repeat count may be completely unrolled to 
avoid the loop overhead. Example: 
 
// Example 8.12a 
int i, a[2]; 
for (i = 0; i < 2; i++) a[i] = i+1; 
 
The compiler may reduce this to: 
 
// Example 8.12b 
int a[2]; 
a[0] = 1; a[1] = 2; 
 
Unfortunately, some compilers unroll too much. Excessive loop unrolling is not optimal 
because it takes too much space in the code cache and it fills up the loop buffer that some 
microprocessors have. In some cases it can be useful to turn off the loop unroll option in the 
compiler. 
Loop invariant code motion 
A calculation may be moved out of a loop if it is independent of the loop counter. Example: 
 
// Example 8.13a 
int i, a[100], b; 
for (i = 0; i < 100; i++) { 


---

 
   a[i] = b * b + 1; 
} 
 
The compiler may change this to: 
 
// Example 8.13b 
int i, a[100], b, temp; 
temp = b * b + 1; 
for (i = 0; i < 100; i++) { 
   a[i] = temp; 
} 
Induction variables 
An expression that is a linear function of a loop counter can be calculated by adding a 
constant to the previous value. Example: 
 
// Example 8.14a 
int i, a[100]; 
for (i = 0; i < 100; i++) { 
   a[i] = i * 9 + 3; 
} 
 
The compiler may avoid the multiplication by changing this to: 
 
// Example 8.14b 
int i, a[100], temp; 
temp = 3; 
for (i = 0; i < 100; i++) { 
   a[i] = temp; 
   temp += 9; 
} 
 
Induction variables are often used for calculating the addresses of array elements. Example: 
 
// Example 8.15a 
struct S1 {double a; double b;}; 
S1 list[100];  int i; 
for (i = 0; i < 100; i++) { 
   list[i].a = 1.0; 
   list[i].b = 2.0; 
} 
 
In order to access an element in list, the compiler must calculate its address. The 
address of list[i] is equal to the address of the beginning of list plus i*sizeof(S1). 
This is a linear function of i which can be calculated by an induction variable. The compiler 
can use the same induction variable for accessing list[i].a and list[i].b. It can also 
eliminate i and use the induction variable as loop counter when the final value of the 
induction variable can be calculated in advance. This reduces the code to: 
 
// Example 8.15b 
struct S1 {double a; double b;}; 
S1 list[100], *temp; 
for (temp = &list[0]; temp < &list[100]; temp++) { 
   temp->a = 1.0; 
   temp->b = 2.0; 
} 
 
The factor sizeof(S1) = 16 is actually hidden behind the C++ syntax in example 8.15b. 
The integer representation of &list[100] is (int)(&list[100]) = 


---

 
(int)(&list[0]) + 100*16, and temp++ actually adds 16 to the integer value of 
temp. 
 
The compiler doesn't need induction variables to calculate the addresses of array elements 
of simple types because the CPU has hardware support for calculating the address of an 
array element if the address can be expressed as a base address plus a constant plus an 
index multiplied by a factor of 1, 2, 4 or 8, but not any other factor. If a and b in example 
8.15a were float instead of double, then sizeof(S1) would be 8 and no induction 
variable would be needed because the CPU has hardware support for multiplying the index 
by 8. 
 
The compilers I have studied do not make induction variables for floating point expressions 
or more complex integer expressions. See page 81 for an example of how to use induction 
variables for calculating a polynomial. 
Scheduling 
A compiler may reorder instructions for the sake of parallel execution. Example: 
 
// Example 8.16 
float a, b, c, d, e, f, x, y; 
x = a + b + c; 
y = d + e + f; 
 
The compiler may interleave the two formulas in this example so that a+b is calculated first, 
then d+e, then c is added to the first sum, then f is added to the second sum, then the first 
result is stored in x, and last the second result is stored in y. The purpose of this is to help 
the CPU doing multiple calculations in parallel. Modern CPUs are actually able to reorder 
instructions without help of the compiler (see page 105), but the compiler can make this 
reordering easier for the CPU. 
Algebraic reductions 
Most compilers can reduce simple algebraic expressions using the fundamental laws of 
algebra. For example, a compiler may change the expression -(-a)  to a.  
 
I don't think that programmers write expressions like -(-a)  very often, but such 
expressions may occur as a result of other optimizations such as function inlining. 
Reducible expressions also occur quite often as a result of macro expansions. 
 
Programmers do, however, often write expressions that can be reduced. This may be 
because the non-reduced expression better explains the logic behind the program or 
because the programmer hasn't thought about the possibility of algebraic reduction. For 
example, a programmer may prefer to write if(!a && !b) rather than the equivalent 
if(!(a || b)) even though the latter has one operator less. Fortunately, all compilers 
are able to do the reduction in this case. 
 
You cannot expect a compiler to reduce complicated algebraic expressions. For example, 
only one of the compilers I have tested were able to reduce (a*b*c)+(c*b*a) to 
a*b*c*2. It is quite difficult to implement the many rules of algebra in a compiler. Some 
compilers can reduce some types of expressions and other compilers can reduce other 
types of expressions, but no compiler I have ever seen can reduce them all. In the case of 
Boolean algebra, it is possible to implement a universal algorithm (e.g. Quine–McCluskey or 
Espresso) that can reduce any expression, but none of the compilers I have tested seem to 
do so. 
 
The compilers are better at reducing integer expressions than floating point expressions, 
even though the rules of algebra are the same in both cases. This is because algebraic 


---

 
manipulations of floating point expressions may have undesired effects. This effect can be 
illustrated by the following example: 
 
// Example 8.17 
char a = -100, b = 100, c = 100, y; 
y = a + b + c; 
 
Here, y will get the value -100+100+100 = 100. Now, according to the rules of algebra, we 
may write: 
 
y = c + b + a; 
 
This may be useful if the subexpression c+b can be reused elsewhere. In this example, we 
are using 8-bit integers which range from -128 to +127. An integer overflow will make the 
value wrap around. Adding 1 to 127 will generate -128, and subtracting 1 from -128 
generates 127. The calculation of c+b will generate an overflow and give the result -56 
rather than 200. Next, we are adding -100 to -56 which will generate an underflow and give 
the result 100 rather than -156. Surprisingly, we end up with the correct result because the 
overflow and underflow neutralize each other. This is the reason why it is safe to use 
algebraic manipulations on integer expressions (except for the <, <=, > and >= operators). 
 
The same argument does not apply to floating point expressions. Floating point variables do 
not wrap around on overflow and underflow. The range of floating point variables is so large 
that we do not have to worry much about overflow and underflow except in special mathe-
matical applications. But we do have to worry about loss of precision. Let's repeat the above 
example with floating point numbers: 
 
// Example 8.18 
float a = -1.0E8, b = 1.0E8, c = 1.23456, y; 
y = a + b + c; 
 
The calculation here gives a+b=0, and then 0+1.23456 = 1.23456. But we will not get 
the same result if we change the order of the operands and add b and c first. b+c = 
100000001.23456. The float type holds a precision of approximately seven significant 
digits, so the value of b+c will be rounded to 100000000. When we add a to this number 
we get 0 rather than 1.23456. 
 
The conclusion to this argument is that the order of floating point operands cannot be 
changed without the risk of losing precision. The compilers will not do so unless you specify 
an option that allows less precise floating point calculations. Even with all relevant 
optimization options turned on, the compilers will not do such obvious reductions as 0/a = 
0 because this would be invalid if a was zero or infinity or NAN (not a number). Different 
compilers behave differently because there are different opinions on which imprecisions 
should be allowed and which not. 
 
You cannot rely on the compiler to do any algebraic reductions on floating point code and 
you can rely on only the most simple reductions on integer code. It is more safe to do the 
reductions manually. I have tested the capability to reduce various algebraic expressions on 
seven different compilers. The results are listed in table 8.1 below. 
Devirtualization 
An optimizing compiler can bypass the virtual table lookup for a virtual function call if it is 
known which version of the virtual function is needed. Example: 
 
// Example 8.19. Devirtualization 
class C0 { 
   public: 
   virtual void f(); 


---

 
}; 
 
class C1 : public C0 { 
   public: 
   virtual void f(); 
}; 
 
void g() { 
   C1 obj1; 
   C0 * p = & obj1; 
   p->f();               // Virtual call to C1::f 
} 
 
Without optimization, the compiler needs to look up in a virtual table to see whether the call 
p->f() goes to C0::f or C1::f. But an optimizing compiler will see that p always points 
to an object of class C1, so it can call C1::f directly without using the virtual table. 
Unfortunately, few compilers are able to do this optimization. 
 
8.2 Comparison of different compilers 
I have made a series of experiments on seven different brands of C++ compilers to see 
whether they were able to do different kinds of optimizations. The results are summarized in 
table 8.1. The table shows whether the different compilers succeeded in applying the 
various optimization methods and algebraic reductions in my test examples.  
 
The table can give some indication of which optimizations you can expect a particular 
compiler to do and which optimizations you have to do manually. 
 
It must be emphasized that the compilers may behave differently on different test examples. 
You cannot expect a compiler to always behave according to the table. 
 
Optimization method 
Microsoft 
Borland 
Intel 
Gnu 
PathScale 
PGI 
Digital 
Mars 
Watcom 
Codeplay 
Function inlining 
x 
- 
x 
x 
x 
x 
- 
- 
x 
Constant folding 
x 
x 
x 
x 
x 
x 
x 
x 
x 
Constant propagation 
x 
- 
x 
x 
x 
x 
- 
- 
x 
Pointer elimination 
x 
x 
x 
x 
x 
x 
x 
x 
x 
Common subexpression elimin., integer 
x 
(x) 
x 
x 
x 
x 
x 
x 
x 
Common subexpression elimin., float 
x 
- 
x 
x 
x 
x 
- 
x 
x 
Register variables, integer 
x 
x 
x 
x 
x 
x 
x 
x 
x 
Register variables, float 
x 
- 
x 
x 
x 
x 
- 
x 
x 
Live range analysis 
x 
x 
x 
x 
x 
x 
x 
x 
x 
Join identical branches 
x 
- 
- 
x 
- 
- 
- 
x 
- 
Eliminate jumps 
x 
x 
x 
x 
x 
x 
- 
x 
x 
Eliminate branches 
x 
- 
x 
x 
x 
x 
- 
- 
- 
Remove branch that is always true/false 
x 
- 
x 
x 
x 
x 
x 
x 
x 
Loop unrolling 
x 
- 
x 
x 
x 
x 
- 
- 
x 
Loop invariant code motion 
x 
- 
x 
x 
x 
x 
x 
x 
x 
Induction variables for array elements 
x 
x 
x 
x 
x 
x 
x 
x 
x 
Induction variables for other integer 
expressions 
x 
- 
x 
x 
x 
- 
x 
x 
x 
Induction variables for float expressions 
- 
- 
- 
- 
- 
- 
- 
- 
- 
Automatic vectorization 
- 
- 
x 
x 
x 
x 
- 
- 
x 
Devirtualization 
- 
- 
- 
x 
- 
- 
- 
- 
- 


---

 
Profile-guided optimization 
x 
- 
x 
x 
x 
x 
- 
- 
- 
Whole program optimization 
x 
- 
x 
x 
x 
- 
- 
- 
- 
 
 
 
 
 
 
 
 
 
 
Integer algebra reductions: 
 
 
 
 
 
 
 
 
 
a+b = b+a 
x 
(x) 
x 
x 
x 
x 
- 
x 
x 
a*b = b*a 
x 
(x) 
x 
x 
x 
x 
- 
x 
x 
(a+b)+c = a+(b+c) 
x 
- 
x 
x 
- 
- 
x 
x 
- 
a+b+c = c+b+a 
x 
- 
- 
x 
- 
- 
- 
- 
- 
a+b+c+d = (a+b)+(c+d) 
- 
- 
x 
x 
- 
- 
- 
- 
- 
a*b+a*c = a*(b+c) 
x 
- 
x 
x 
x 
- 
- 
- 
x 
a*x*x*x + b*x*x + c*x + d = 
((a*x+b)*x+c)*x+d 
x 
- 
x 
x 
x 
- 
- 
- 
x 
x*x*x*x*x*x*x*x = ((x2) 2) 2 
- 
- 
x 
- 
- 
- 
- 
- 
- 
a+a+a+a = a*4 
x 
- 
x 
x 
- 
- 
- 
- 
x 
-(-a) = a 
x 
- 
x 
x 
x 
x 
x 
x 
- 
a-(-b) = a+b 
x 
- 
x 
x 
x 
x 
- 
x 
- 
a-a = 0 
x 
- 
x 
x 
x 
x 
x 
x 
x 
a+0 = a 
x 
x 
x 
x 
x 
x 
x 
x 
x 
a*0 = 0 
x 
x 
x 
x 
x 
x 
x 
- 
x 
a*1 = a 
x 
x 
x 
x 
x 
x 
x 
x 
x 
(-a)*(-b) = a*b 
x 
- 
x 
x 
x 
- 
- 
- 
- 
a/a = 1 
- 
- 
- 
- 
x 
- 
- 
- 
x 
a/1 = a 
x 
x 
x 
x 
x 
x 
x 
x 
x 
0/a = 0 
- 
- 
- 
x 
- 
- 
- 
x 
x 
(-a == -b) = (a == b) 
- 
- 
- 
x 
x 
- 
- 
- 
- 
(a+c == b+c) = (a == b) 
- 
- 
- 
- 
x 
- 
- 
- 
- 
!(a < b) = (a >= b) 
x 
x 
x 
x 
x 
x 
x 
x 
x 
(a<b && b<c && a<c) = (a<b && b<c) 
- 
- 
- 
- 
- 
- 
- 
- 
- 
Multiply by constant = shift and add 
x 
x 
x 
x 
- 
x 
x 
x 
- 
Divide by constant = multiply and shift 
x 
- 
x 
x 
x 
(-) 
x 
- 
- 
 
 
 
 
 
 
 
 
 
 
Floating point algebra reductions: 
 
 
 
 
 
 
 
 
 
a+b = b+a 
x 
- 
x 
x 
x 
x 
- 
- 
x 
a*b = b*a 
x 
- 
x 
x 
x 
x 
- 
- 
x 
a+b+c = a+(b+c) 
x 
- 
x 
x 
- 
- 
- 
- 
- 
(a+b)+c = a+(b+c) 
- 
- 
x 
x 
- 
- 
- 
- 
- 
a*b*c = a*(b*c) 
x 
- 
- 
x 
- 
- 
- 
- 
- 
a+b+c+d = (a+b)+(c+d) 
- 
- 
- 
x 
- 
- 
- 
- 
- 
a*b+a*c = a*(b+c) 
x 
- 
- 
- 
x 
- 
- 
- 
x 
a*x*x*x + b*x*x + c*x + d = 
((a*x+b)*x+c)*x+d 
x 
- 
x 
x 
x 
- 
- 
- 
- 
x*x*x*x*x*x*x*x = ((x2) 2) 2 
- 
- 
- 
x 
- 
- 
- 
- 
- 
a+a+a+a = a*4 
x 
- 
- 
x 
x 
- 
- 
- 
- 
-(-a) = a 
- 
- 
x 
x 
x 
x 
x 
x 
- 
a-(-b) = a+b 
- 
- 
- 
x 
x 
x 
- 
x 
- 
a+0 = a 
x 
- 
x 
x 
x 
x 
x 
x 
- 
a*0 = 0 
- 
- 
x 
x 
x 
x 
- 
x 
x 
a*1 = a 
x 
- 
x 
x 
x 
x 
x 
- 
x 
(-a)*(-b) = a*b 
- 
- 
- 
x 
x 
x 
- 
- 
- 
a/a = 1 
- 
- 
- 
- 
- 
- 
- 
- 
x 
a/1 = a 
x 
- 
x 
x 
x 
- 
x 
- 
- 
0/a = 0 
- 
- 
- 
x 
x 
- 
- 
x 
x 
(-a == -b) = (a == b) 
- 
- 
- 
x 
x 
- 
- 
- 
- 
(-a > -b) = (a < b) 
- 
- 
- 
x 
x 
- 
- 
- 
x 
Divide by constant = multiply by 
reciprocal 
x 
x 
- 
x 
x 
- 
- 
x 
- 


---

 
 
 
 
 
 
 
 
 
 
 
Boolean algebra reductions: 
 
 
 
 
 
 
 
 
 
!(!a) = a 
x 
- 
x 
x 
x 
x 
x 
x 
x 
(a&&b) || (a&&c) = a&&(b||c) 
x 
- 
x 
x 
x 
- 
- 
- 
- 
!a && !b = !(a || b) 
x 
x 
x 
x 
x 
x 
x 
x 
x 
a && !a = false, a || !a = true 
x 
- 
x 
x 
x 
x 
- 
- 
- 
a && true = a, a || false = a 
x 
x 
x 
x 
x 
x 
x 
x 
- 
a && false = false, a || true = true 
x 
- 
x 
x 
x 
x 
x 
x 
- 
a && a = a 
x 
- 
x 
x 
x 
x 
- 
- 
- 
(a&&b) || (a&&!b) = a 
x 
- 
- 
x 
x 
- 
- 
- 
- 
(a&&b) || (!a&&c) = a ? b : c 
x 
- 
x 
x 
- 
- 
- 
- 
- 
(a&&b) || (!a&&c) || (b&&c) = a ? b : c 
x 
- 
- 
x 
- 
- 
- 
- 
- 
(a&&b) || (a&&b&&c) = a&&b 
x 
- 
- 
x 
x 
- 
- 
- 
- 
(a&&b) || (a&&c) || (a&&b&&c) = 
a&&(b||c) 
x 
- 
- 
x 
x 
- 
- 
- 
- 
(a&&!b) || (!a&&b) = a XOR b 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
 
 
 
 
 
 
 
 
 
Bit vector algebra reductions: 
 
 
 
 
 
 
 
 
 
~(~a) = a 
x 
- 
x 
x 
x 
x 
x 
- 
- 
(a&b)|(a&c) = a&(b|c) 
x 
- 
x 
x 
x 
x 
- 
- 
x 
(a|b)&(a|c) = a|(b&c) 
x 
- 
x 
x 
x 
x 
- 
- 
x 
~a & ~b = ~(a | b) 
- 
- 
x 
x 
x 
x 
- 
- 
- 
a & a = a 
x 
- 
- 
x 
x 
x 
- 
- 
x 
a & ~a = 0 
- 
- 
x 
x 
x 
x 
- 
- 
- 
a & -1 = a,  a | 0 = a 
x 
- 
x 
x 
x 
x 
x 
x 
x 
a & 0 = 0,  a | -1 = -1 
x 
- 
x 
x 
x 
x 
x 
x 
x 
(a&b) | (~a&c) | (b&c) = (a&b) | (~a&c) 
- 
- 
- 
- 
- 
- 
- 
- 
- 
a&b&c&d = (a&b)&(c&d) 
- 
- 
- 
x 
- 
- 
- 
- 
- 
a ^ 0 = a 
x 
x 
x 
x 
x 
- 
x 
x 
x 
a ^ -1 = ~a 
x 
- 
x 
x 
x 
- 
x 
x 
- 
a ^ a = 0 
x 
- 
x 
x 
x 
x 
- 
x 
x 
a ^ ~a = -1 
- 
- 
- 
x 
x 
x 
- 
- 
- 
(a&~b) | (~a&b) = a ^ b 
- 
- 
- 
- 
- 
- 
- 
- 
- 
~a ^ ~b = a ^ b 
- 
- 
- 
x 
x 
- 
- 
- 
- 
a<<b<<c = a<<(b+c) 
x 
- 
x 
x 
x 
- 
- 
x 
x 
 
 
 
 
 
 
 
 
 
 
Integer XMM (vector) reductions: 
 
 
 
 
 
 
 
 
 
Common subexpression elimination 
x 
n.a. 
x 
x 
x 
- 
n.a. 
n.a. 
x 
Constant folding 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a+b = b+a, a*b = b*a 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
x 
(a+b)+c = a+(b+c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a*b+a*c = a*(b+c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
x*x*x*x*x*x*x*x = ((x2) 2) 2 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a+a+a+a = a*4 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
-(-a) = a 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a-a = 0 
- 
n.a. 
x 
- 
- 
- 
n.a. 
n.a. 
- 
a+0 = a 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a*0 = 0 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a*1 = a 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
(-a)*(-b) = a*b 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
!(a < b) = (a >= b) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
 
 
 
 
 
 
 
 
 
 
Floating point XMM (vector) 
reductions: 
 
 
 
 
 
 
 
 
 
a+b = b+a,  a*b = b*a 
x 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
x 
a+b+c = a+(b+c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 


---

 
a*b+a*c = a*(b+c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
-(-a) = a 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a-a = 0 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a+0 = a 
- 
n.a. 
x 
- 
- 
- 
n.a. 
n.a. 
- 
a*0 = 0 
- 
n.a. 
x 
- 
- 
- 
n.a. 
n.a. 
- 
a*1 = a 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a/1 = a 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
0/a = 0 
- 
n.a. 
x 
x 
- 
- 
n.a. 
n.a. 
- 
Divide by constant = multiply by 
reciprocal 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
 
 
 
 
 
 
 
 
 
 
Boolean XMM (vector) reductions: 
 
 
 
 
 
 
 
 
 
~(~a) = a 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
(a&b)|(a&c) = a&(b|c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a & a = a,  a | a = a 
- 
n.a. 
x 
x 
- 
- 
n.a. 
n.a. 
- 
a & ~a = 0 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a & -1 = a,  a | 0 = a 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a & 0 = 0 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a | -1 = -1 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
a ^ a = 0 
- 
n.a. 
x 
x 
- 
- 
n.a. 
n.a. 
- 
andnot(a,a) = 0 
- 
n.a. 
- 
x 
- 
- 
n.a. 
n.a. 
- 
a<<b<<c = a<<(b+c) 
- 
n.a. 
- 
- 
- 
- 
n.a. 
n.a. 
- 
Table 8.1. Comparison of optimizations in different C++ compilers 
The tests were carried out with all relevant optimization options turned on, including relaxed 
floating point precision. The following compiler versions were tested: 
Microsoft C++ Compiler v. 14.00 for 80x86 / x64 (Visual Studio 2005). 
Borland C++ 5.82 (Embarcadero/CodeGear/Borland C++ Builder 5, 2009). 
Intel C++ Compiler v. 11.1 for IA-32/Intel64, 2009. 
Gnu C++ v. 4.1.0, 2006 (Red Hat). 
PathScale C++ v. 3.1, 2007. 
PGI C++ v. 7.1-4, 2008. 
Digital Mars Compiler v. 8.42n, 2004. 
Open Watcom C/C++ v. 1.4, 2005. 
Codeplay VectorC v. 2.1.7, 2004. 
No differences were observed between the optimization capabilities for 32-bit and 64-bit code for 
the Microsoft, Intel, Gnu and PathScale compilers.  
 
8.3 Obstacles to optimization by compiler 
There are several factors that can prevent the compiler from doing the optimizations that we 
want it to do. It is important for the programmer to be aware of these obstacles and to know 
how to avoid them. Some important obstacles to optimization are discussed below. 
Cannot optimize across modules 
The compiler doesn't have information about functions in other modules than the one it is 
compiling. This prevents it from making optimizations across function calls. Example: 
 
// Example 8.20 
module1.cpp 
int Func1(int x) { 
   return x*x + 1; 
} 
 
module2.cpp 
int Func2() { 
   int a = Func1(2); 
   ... 


---

 
} 
 
If Func1 and Func2 were in the same module then the compiler would be able do function 
inlining and constant propagation and reduce a to the constant 5. But the compiler doesn't 
have the necessary information about Func1 when compiling module2.cpp. 
 
The simplest way to solve this problem is to combine the multiple .cpp modules into one by 
means of #include directives. This is sure to work on all compilers. Some compilers have 
a feature called whole program optimization, which will enable optimizations across 
modules (See page 82). 
Pointer aliasing 
When accessing a variable through a pointer or reference, the compiler may not be able to 
completely rule out the possibility that the variable pointed to is identical to some other 
variable in the code. Example: 
 
// Example 8.21 
void Func1 (int a[], int * p) { 
   int i; 
   for (i = 0; i < 100; i++) { 
      a[i] = *p + 2; 
   } 
} 
 
void Func2() { 
   int list[100]; 
   Func1(list, &list[8]); 
} 
 
Here, it is necessary to reload *p and calculate *p+2 a hundred times because the value 
pointed to by p is identical to one of the elements in a[] which will change during the loop. 
It is not permissible to assume that *p+2 is a loop-invariant code that can be moved out of 
the loop. Example 8.21 is indeed a very contrived example, but the point is that the compiler 
cannot rule out the theoretical possibility that such contrived examples exist. Therefore the 
compiler is prevented from assuming that *p+2 is a loop-invariant expression that it can 
move outside the loop. 
 
Most compilers have an option for assuming no pointer aliasing (/Oa). The easiest way to 
overcome the obstacle of possible pointer aliasing is to turn on this option. This requires that 
you analyze all pointers and references in the code carefully to make sure that no variable 
or object is accessed in more than one way in the same part of the code. It is also possible 
to tell the compiler that a specific pointer does not alias anything by using the keyword 
__restrict or __restrict__, if supported by the compiler. 
 
We can never be sure that the compiler takes the hint about no pointer aliasing. The only 
way to make sure that the code is optimized is to do it explicitly. In example 8.21, you could 
calculate *p+2 and store it in a temporary variable outside the loop if you are sure that the 
pointer does not alias any elements in the array. This method requires that you can predict 
where the obstacles to optimization are. 
Dynamic memory allocation 
Any array or object that is allocated dynamically (with new or malloc) is necessarily 
accessed through a pointer. It may be obvious to the programmer that pointers to different 
dynamically allocated objects are not overlapping or aliasing, but the compiler is usually not 
able to see this. It also prevents the compiler from aligning the data optimally, or from 
knowing that the objects are aligned. It is preferred to declare objects and fixed size arrays 
inside the function that needs them. 


---

 
Pure functions 
A pure function is a function that has no side-effects and its return value depends only on 
the values of its arguments. This closely follows the mathematical notion of a "function". 
 
Multiple calls to a pure function with the same arguments are sure to produce the same 
result. A compiler can eliminate common subexpressions that contain pure function calls 
and it can move out loop-invariant code containing pure function calls. Unfortunately, the 
compiler cannot know that a function is pure if the function is defined in a different module 
or a function library. 
 
Therefore, it is necessary to do optimizations such as common subexpression elimination, 
constant propagation, and loop-invariant code motion manually when it involves pure 
function calls. 
 
The Gnu compiler and the Intel compiler for Linux have an attribute which can be applied to 
a function prototype to tell the compiler that this is a pure function. Example: 
 
// Example 8.22 
#ifdef __GNUC__ 
#define pure_function  __attribute__((const)) 
#else 
#define pure_function 
#endif 
 
double Func1(double) pure_function ; 
 
double Func2(double x) { 
   return Func1(x) * Func1(x) + 1.; 
} 
 
Here, the Gnu compiler will make only one call to Func1, while other compilers will make 
two. 
 
Some other compilers (Microsoft, Intel) know that standard library functions like sqrt, pow 
and log are pure functions, but unfortunately there is no way to tell these compilers that a 
user-defined function is pure. 
Virtual functions and function pointers 
It is rarely possible for the compiler to predict with certainty which version of a virtual 
function will be called, or what a function pointer points to. Therefore, it cannot inline the 
function or otherwise optimize across the function call. 
Algebraic reduction 
Most compilers can do simple algebraic reductions such as -(-a) = a, but they are not able to 
do more complicated reductions. Algebraic reduction is a complicated process which is 
difficult to implement in a compiler. 
 
Many algebraic reductions are not permissible for reasons of mathematical purity. In many 
cases it is possible to construct obscure examples where the reduction would cause 
overflow or loss of precision, especially in floating point expressions (see page 73). The 
compiler cannot rule out the possibility that a particular reduction would be invalid in a 
particular situation, but the programmer can. It is therefore necessary to do the algebraic 
reductions explicitly in many cases. 
 
Integer expressions are less susceptible to problems of overflow and loss of precision for 
reasons explained on page 73. It is therefore possible for the compiler to do more 
reductions on integer expressions than on floating point expressions. Most reductions 
involving integer addition, subtraction and multiplication are permissible in all cases, while 


---

 
many reductions involving division and relational operators (e.g. '>') are not permissible for 
reasons of mathematical purity. For example, compilers cannot reduce the integer 
expression -a > -b to a < b because of a very obscure possibility of overflow. 
 
Table 8.1 (page 78) shows which reductions the compilers are able to do, at least in some 
situations, and which reductions they cannot do. All the reductions that the compilers cannot 
do must be done manually by the programmer. 
Floating point induction variables 
Compilers cannot make floating point induction variables for the same reason that they 
cannot make algebraic reductions on floating point expressions. It is therefore necessary to 
do this manually. This principle is useful whenever a function of a loop counter can be 
calculated more efficiently from the previous value than from the loop counter. Any 
expression that is an n'th degree polynomial of the loop counter can be calculated by n 
additions and no multiplications. The following example shows the principle for a 2'nd order 
polynomial: 
 
// Example 8.23a. Loop to make table of polynomial 
const double A = 1.1, B = 2.2, C = 3.3; // Polynomial coefficients 
double Table[100];                      // Table 
int x;                                  // Loop counter 
for (x = 0; x < 100; x++) { 
   Table[x] = A*x*x + B*x + C;          // Calculate polynomial 
} 
 
The calculation of this polynomial can be done with just two additions by the use of two 
induction variables: 
 
// Example 8.23b. Calculate polynomial with induction variables 
const double A = 1.1, B = 2.2, C = 3.3; // Polynomial coefficients 
double Table[100];                      // Table 
int x;                                  // Loop counter 
const double A2 = A + A;                // = 2*A 
double Y = C;                           // = A*x*x + B*x + C 
double Z = A + B;                       // = Delta Y 
for (x = 0; x < 100; x++) { 
   Table[x] = Y;                        // Store result 
   Y += Z;                              // Update induction variable Y 
   Z += A2;                             // Update induction variable Z 
} 
 
The loop in example 8.23b has two loop-carried dependency chains, namely the two 
induction variables Y and Z. Each dependency chain has a latency which is the same as the 
latency of a floating point addition. This is small enough to justify the method. A longer loop-
carried dependency chain would make the induction variable method unfavorable, unless 
the value is calculated from a value that is two or more iterations back. 
 
The method of induction variables can also be vectorized if you take into account that each 
value is calculated from the value that lies r places back in the sequence, where r is the 
number of elements in a vector or the loop unroll factor. A little math is required for finding 
the right formula in each case. 
Inlined functions have a non-inlined copy 
Function inlining has the complication that the same function may be called from another 
module. The compiler has to make a non-inlined copy of the inlined function for the sake of 
the possibility that the function is also called from another module. This non-inlined copy is 
dead code if no other modules call the function. This fragmentation of the code makes 
caching less efficient. 
 


---

 
There are various ways around this problem. If a function is not referenced from any other 
module then add the keyword static to the function definition. This tells the compiler that 
the function cannot be called from any other module. The static declaration makes it 
easier for the compiler to evaluate whether it is optimal to inline the function, and it prevents 
the compiler from making an unused copy of an inlined function. The static keyword also 
makes various other optimizations possible because the compiler doesn't have to obey any 
specific calling conventions for functions that are not accessible from other modules. You 
may add the static keyword to all local non-member functions. 
 
Unfortunately, this method doesn't work for class member functions because the static 
keyword has a different meaning for member functions. You can force a member function to 
be inlined by declaring the function body inside the class definition. This will prevent the 
compiler from making a non-inlined copy of the function, but it has the disadvantage that the 
function is always inlined even when it is not optimal to do so (i.e. if the member function is 
big and is called from many different places). 
 
Some compilers have an option (Windows: /Gy, Linux: -ffunction-sections) which 
allows the linker to remove unreferenced functions. It is recommended to turn on this option. 
  
8.4 Obstacles to optimization by CPU 
Modern CPUs can do a lot of optimization by executing instructions out of order. Long 
dependency chains in the code prevent the CPU from doing out-of-order execution, as 
explained on page 22. Avoid long dependency chains, especially loop-carried dependency 
chains with long latencies. 
 
8.5 Compiler optimization options 
All C++ compilers have various optimization options that you can turn on and off. It is 
important to study the available options for the compiler you are using and turn on all 
relevant options. 
 
Many optimization options are incompatible with debugging. A debugger can execute a 
code one line at a time and show the values of all variables. Obviously, this is not possible 
when parts of the code have been reordered, inlined, or optimized away. It is common to 
make two versions of a program executable: a debug version with full debugging support 
which is used during program development, and a release version with all relevant 
optimization options turned on. Most IDE's (Integrated Development Environments) have 
facilities for making a debug version and a release version of object files and executables. 
Make sure to distinguish these two versions and turn off debugging and profiling support in 
the optimized version of the executable. 
 
Most compilers offer the choice between optimizing for size and optimizing for speed. 
Optimizing for size is relevant when the code is fast anyway and you want the executable to 
be as small as possible or when code caching is critical. Optimizing for speed is relevant 
when CPU access and memory access are critical time consumers. Choose the strongest 
optimization option available. 
 
Some compilers offer profile-guided optimization. This works in the following way. First you 
compile the program with profiling support. Then you make a test run with a profiler which 
determines the program flow and the number of times each function and branch is 
executed. The compiler can then use this information to optimize the code and put the 
different functions in the optimal order. 
 
Some compilers have support for whole program optimization. This works by compiling in 
two steps. All source files are first compiled to an intermediate file format instead of the 
usual object file format. The intermediate files are then linked together in the second step 


---

 
where the compilation is finished. Register allocation and function inlining is done at the 
second step. The intermediate file format is not standardized. It is not even compatible with 
different versions of the same compiler. It is therefore not possible to distribute function 
libraries in this format. 
 
Other compilers offer the possibility of compiling multiple .cpp files into a single object file. 
This enables the compiler to do cross-module optimizations when interprocedural 
optimization is enabled. A more primitive, but efficient, way of doing whole program 
optimization is to join all source files into one by means of #include directives and declare 
all functions static or inline. This will enable the compiler to do interprocedural optimizations 
of the whole program. 
 
During the history of CPU development, each new generation of CPUs increased the 
available instruction set. The newer instruction sets enable the compiler to make more 
efficient code, but this makes the code incompatible with old CPUs. The Pentium Pro 
instruction set makes floating point comparisons more efficient. This instruction set is 
supported by all modern CPUs. The SSE2 instruction set is particularly interesting because 
it makes floating point code more efficient in some cases and it makes it possible to use 
vector instructions (see page 107). Using the SSE2 instruction set is not always optimal, 
though. In some cases the SSE2 instruction set makes floating point code slower, especially 
when the code mixes float and double (see page 143). The SSE2 instruction set is 
supported by most CPUs and operating systems available today. 
 
You may choose a newer instruction set when compatibility with old CPUs is not needed. 
Even better, you may make multiple versions of the most critical part of the code to support 
different CPUs. This method is explained on page 125. 
 
The code becomes more efficient when there is no exception handling. It is recommended 
to turn off support for exception handling unless the code relies on structured exception 
handling and you want the code to be able to recover from exceptions. See page 62. 
 
It is recommended to turn off support for runtime type identification (RTTI). See page 55. 
 
It is recommended to enable fast floating point calculations or turn off requirements for strict 
floating point calculations unless the strictness is required. See page 74 and 73 for 
discussions. 
 
Turn on the option for "function level linking" if available. See page 82 for an explanation of 
this option. 
 
Use the option for "assume no pointer aliasing" if you are sure the code has no pointer 
aliasing. See page 79 for an explanation. (The Microsoft compiler supports this option only 
in the Professional and Enterprise editions). 
 
Do not turn on correction for the "FDIV bug". The FDIV bug is a minor error in the oldest 
Pentium CPUs which may cause slight imprecision in some rare cases of floating point 
division. Correction for the FDIV bug causes floating point division to be slower. 
 
Many compilers have an option for "standard stack frame" or "frame pointer". The standard 
stack frame is used for debugging and exception handling. Omitting the standard stack 
frame makes function calls faster and makes an extra register available for other purposes. 
This is advantageous because registers is a scarce resource. Do not use a stack frame 
unless your program relies on exception handling. 
 


---

 
8.6 Optimization directives 
Some compilers have many keywords and directives which are used for giving specific 
optimization instructions at specific places in the code. Many of these directives are 
compiler-specific. You cannot expect a directive for a Windows compiler to work on a Linux 
compiler, or vice versa. But most of the Microsoft directives work on the Intel compiler for 
Windows and the Gnu compiler for Windows, while most of the Gnu directives work on the 
PathScale and Intel compilers for Linux. 
Keywords that work on all C++ compilers 
The register keyword can be added to a variable declaration to tell the compiler that you 
want this to be a register variable. The register keyword is only a hint and the compiler may 
not take the hint, but it can be useful in situations where the compiler is unable to predict 
which variables will be used most. 
 
The opposite of register is volatile. The volatile keyword makes sure that a 
variable is never stored in a register, not even temporarily. This is intended for variables that 
are shared between multiple threads, but it can also be used for turning off all optimizations 
of a variable for test purposes. 
 
The const keyword tells that a variable is never changed. This will allow the compiler to 
optimize away the variable in many cases. For example: 
 
// Example 8.24. Integer constant 
const int ArraySize = 1000; 
int List[ArraySize]; 
... 
for (int i = 0; i < ArraySize; i++) List[i]++; 
 
Here, the compiler can replace all occurrences of ArraySize by the value 1000. The loop 
in example 8.24 can be implemented in a more efficient way if the value of the loop count 
(ArraySize) is constant and known to the compiler at compile time. No memory will be 
allocated for an integer constant, unless the address of it (&ArraySize) is taken. 
 
A const pointer or const reference cannot change what it points to. A const member 
function cannot modify data members. It is recommended to use the const keyword 
wherever appropriate to give the compiler additional information about a variable, pointer or 
member function because this may improve the possibilities for optimization. For example, 
the compiler can safely assume that the value of a class data member is unchanged across 
a call to a const function that is member of the same class. 
 
The static keyword has several meanings depending on the context. The keyword 
static, when applied to a non-member function, means that the function is not accessed 
by any other modules. This makes inlining more efficient and enables interprocedural 
optimizations. See page 81. 
 
The keyword static, when applied to a global variable means that it is not accessed by 
any other modules. This enables interprocedural optimizations. 
 
The keyword static, when applied to a local variable inside a function means that the 
variable will be preserved when the function returns and remain unchanged the next time 
the function is called. This may be inefficient because some compilers will insert extra code 
to guard the variable against access from multiple threads simultaneously. This may apply 
even if the variable is const. 
 
There may, nevertheless, be a reason to make a local variable static and const to make 
sure it is initialized only the first time the function is called. Example: 
 


---

 
// Example 8.25 
void Func () { 
   static const double log2 = log(2.0); 
   ... 
} 
 
Here, log(2.0) is only calculated the first time Func is executed. Without static, the 
logarithm would be re-calculated every time Func is executed. This has the disadvantage 
that the function must check if it has been called before. This is faster than calculating the 
logarithm again, but it would be even faster to make log2 a global const variable or 
replace it with the calculated value. 
 
The keyword static, when applied to a class member function means that it cannot 
access any non-static data members or member functions. A static member function is 
called faster than a non-static member function because it doesn't need a 'this' pointer. It 
is recommended to make member functions static where appropriate. 
Compiler-specific keywords 
Fast function calling. __fastcall or __attribute__((fastcall)). The fastcall 
modifier can make function calls faster in 32-bit mode. The first two integer parameters are 
transferred in registers rather than on the stack (three parameters on CodeGear compiler). 
Fastcall functions are not compatible across compilers. Fastcall is not needed in 64-bit 
mode where the parameters are transferred in registers anyway. 
 
Pure function. __attribute__((const))  (Linux only). Specifies a function to be pure. 
This allows common subexpression elimination and loop-invariant code motion. See page 
80. 
 
Assume no pointer aliasing. __declspec(noalias) or __restrict or 
#pragma optimize("a",on). Specifies that pointer aliasing does not occur. See page 
79 for an explanation. Note that these directives do not always work. 
 
Data alignment. __declspec(align(16)) or __attribute__((aligned(16))). 
Specifies alignment of arrays and structures. Useful for vector operations, see page 107. 
 
8.7 Checking what the compiler does 
It can be very useful to study the code that a compiler generates to see how well it 
optimizes the code. Sometimes the compiler does quite ingenious things to make the code 
more efficient, and sometimes it does incredibly stupid things. Looking at the compiler 
output can often reveal things that can be improved by modifications of the source code, as 
the example below shows. 
 
The best way to check the code that the compiler generates is to use a compiler option for 
assembly language output. On most compilers you can do this by invoking the compiler 
from the command line with all the relevant optimization options and the options -S or /Fa 
for assembly output. The assembly output option is also available from the IDE on some 
systems. If the compiler doesn't have an assembly output option then use an object file 
disassembler. 
 
Note that the Intel compiler has an option for source annotation in the assembly output 
(/FAs or -fsource-asm). This option makes the assembly output more readable but 
unfortunately it prevents certain optimizations. Do not use the source annotation option if 
you want to see the result of full optimization. 
 
It is also possible to see the compiler-generated code in the disassembly window of a 
debugger. However, the code that you see in the debugger is not the optimized version 


---

 
because the debugging options prevent optimization. The debugger cannot set a breakpoint 
in the fully optimized code because it doesn't have the line number information. It is often 
possible to insert a fixed breakpoint in the code with an inline assembly instruction for 
interrupt 3. The code is __asm int 3; or __asm ("int 3"); or __debugbreak();. 
If you run the optimized code (release version) in the debugger then it will break at the 
interrupt 3 breakpoint and show a disassembly, probably without information about function 
names and variable names. Remember to remove the interrupt 3 breakpoint again. 
 
The following example shows what the assembly output of a compiler can look like and how 
you can use it for improving the code. 
 
// Example 8.26a 
void Func(int a[], int & r) { 
   int i; 
   for (i = 0; i < 100; i++) { 
      a[i] = r + i/2; 
   } 
} 
 
The Intel compiler generates the following assembly code from example 8.26a (32-bit 
mode): 
 
; Example 8.26a compiled to assembly: 
ALIGN     4                                ; align by 4 
PUBLIC ?Func@@YAXQAHAAH@Z                  ; mangled function name 
?Func@@YAXQAHAAH@Z PROC NEAR              ; start of Func 
; parameter 1: 8 + esp                     ; a 
; parameter 2: 12 + esp                    ; r 
$B1$1:                                     ; unused label 
        push      ebx                      ; save ebx on stack 
        mov       ecx, DWORD PTR [esp+8]   ; ecx = a 
        xor       eax, eax                 ; eax = i = 0 
        mov       edx, DWORD PTR [esp+12]  ; edx = r 
$B1$2:                                     ; top of loop 
        mov       ebx, eax                 ; compute i/2 in ebx 
        shr       ebx, 31                  ; shift down sign bit of i 
        add       ebx, eax                 ; i + sign(i) 
        sar       ebx, 1                   ; shift right = divide by 2 
        add       ebx, DWORD PTR [edx]     ; add what r points to 
        mov       DWORD PTR[ecx+eax*4],ebx ; store result in array 
        add       eax, 1                   ; i++ 
        cmp       eax, 100                 ; check if i < 100 
        jl        $B1$2                    ; repeat loop if true 
$B1$3:                                     ; unused label 
        pop       ebx                      ; restore ebx from stack 
        ret                                ; return 
        ALIGN     4                        ; align 
?Func@@YAXQAHAAH@Z ENDP                    ; mark end of procedure 
 
Most of the comments generated by the compiler have been replaced by my comments, in 
green. It takes some experience to get used to read and understand compiler-generated 
assembly code. Let me explain the above code in details. The funny looking name 
?Func@@YAXQAHAAH@Z is the name of Func with a lot of added information about the 
function type and its parameters. This is called name mangling. The characters '?', '@' and 
'$' are allowed in assembly names. The details about name mangling are explained in 
manual 5: "Calling conventions for different C++ compilers and operating systems". The 
parameters a and r are transferred on the stack at address esp+8 and esp+12 and loaded 
into ecx and edx, respectively. (In 64-bit mode, the parameters would be transferred in 
registers rather than on the stack). ecx now contains the address of the first element of the 
array a and edx contains the address of the variable that r points to. A reference is the 
same as a pointer in assembly code. Register ebx is pushed on the stack before it is used 


---

 
and popped from the stack before the function returns. This is because the register usage 
convention says that a function is not allowed to change the value of ebx. Only the registers 
eax, ecx and edx can be changed freely. The loop counter i is stored as a register 
variable in eax. The loop initialisation i=0; has been translated to the instruction 
xor eax,eax. This is a common way of setting a register to zero that is more efficient than 
mov eax,0. The loop body begins at the label $B1$2:. This is just an arbitrary name that 
the compiler has chosen for the label. It uses ebx as a temporary register for computing 
i/2+r. The instructions mov ebx,eax / shr ebx,31 copies the sign bit of i into the 
least significant bit of ebx. The next two instructions add ebx, eax / sar ebx,1 adds 
this to i and shifts one place to the right in order to divide i by 2. The instruction add 
ebx, DWORD PTR [edx] adds, not edx but the variable whose address is in edx, to ebx. 
The square brackets mean use the value in edx as a memory pointer. This is the variable 
that r points to. Now ebx contains i/2+r. The next instruction mov DWORD PTR 
[ecx+eax*4],ebx stores this result in a[i]. Note how efficient the calculation of the 
array address is. ecx contains the address of the beginning of the array. eax holds the 
index, i. This index must be multiplied by the size (in bytes) of each array element in order 
to calculate the address of element number i. The size of an int is 4. So the address of 
array element a[i] is ecx+eax*4. The result ebx is then stored at address 
[ecx+eax*4]. This is all done in a single instruction. The CPU supports this kind of 
instructions for fast access to array elements. The instruction add eax,1 is the loop 
increment i++. cmp eax, 100 / jl $B1$2 is the loop condition i < 100. It compares 
eax with 100 and jumps back to the $B1$2 label if i < 100. pop ebx restores the value 
of ebx that was saved in the beginning. ret returns from the function. 
 
The assembly listing reveals three things that can be optimized further. The first thing we 
notice is that it does some funny things with the sign bit of i in order to divide i by 2. The 
compiler has not noticed that i can never be negative so that we don't have to care about 
the sign bit. We can tell it this by making i an unsigned int or by type-casting i to 
unsigned int before dividing by 2 (See page 140). 
 
The second thing we notice is that the value pointed to by r is re-loaded from memory a 
hundred times. This is because we forgot to tell the compiler to assume no pointer aliasing 
(see page 79). Adding the compiler option "assume no pointer aliasing" (if valid) can 
possibly improve the code. 
 
The third thing that can be improved is that r+i/2 could be calculated by an induction 
variable because it is a staircase function of the loop index. The integer division prevents 
the compiler from making an induction variable unless the loop is rolled out by 2. (See page 
72). 
 
The conclusion is that we can help the compiler optimize example 8.26a by rolling out the 
loop by two and making an explicit induction variable. (This eliminates the need for the first 
two suggested improvements). 
 
// Example 8.26b  
void Func(int a[], int & r) { 
   int i; 
   int Induction = r; 
   for (i = 0; i < 100; i += 2) { 
      a[i] = Induction; 
      a[i+1] = Induction; 
      Induction++; 
   } 
} 
 
The compiler generates the following assembly code from example 8.26b: 
 


---

