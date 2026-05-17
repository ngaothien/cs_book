# 15 Metaprogramming

 
15 Metaprogramming 
Metaprogramming means to make code that makes code. For example, in interpreted script 
languages, it is often possible to make a piece of code that produces a string and then 
interpret that string as code. 
 
Metaprogramming can be useful in compiled languages such as C++ for doing some 
calculations at compile time rather than at runtime if all the inputs to the calculations are 
available at compile time. (Of course there is no such advantage in interpreted languages 
where everything happens at runtime). 
 
The following techniques can be considered metaprogramming in C++: 
 
 
Preprocessor directives. For example use #if instead of if. This is a very efficient 
way of removing superfluous code, but there are serious limitations to what the 
preprocessor can do because it comes before the compiler and it understands only 
the simplest expressions and operators.  
   
 
Make a C++ program that produces another C++ program (or part of it). This can be 
useful in some cases, for example to produce tables of mathematical functions that 
you want as static arrays in the final program. This requires, of course, that you 
compile the output of the first program. 
   
 
An optimizing compiler may try to do as much as possible at compile time. For 
example, all good compilers will reduce  int x = 2 * 5;  to  int x = 10;  
   
 
Templates are instantiated at compile time. A template instance has its parameters 
replaced by their actual values before it is compiled. This is the reason why there is 
virtually no cost to using templates (see p. 58). It is possible to express any 
algorithm with template metaprogramming, but this method is extremely complicated 
and clumsy, as you will see shortly. 
 
The following examples explain how metaprogramming can be used to speed up the 
calculation of the power function when the exponent is an integer known at compile time. 
 
// Example 15.1a. Calculate x to the power of 10 
double xpow10(double x) { 
   return pow(x,10); 
} 
 
The pow function uses logarithms in the general case, but in this case it will recognize that 
10 is an integer, so that the result can be calculated using multiplications only. The following 
algorithm is used inside the pow function when the exponent is a positive integer: 
 
// Example 15.1b. Calculate integer power using loop 
double ipow (double x, unsigned int n) { 
   double y = 1.0;               // used for multiplication 
   while (n != 0) {              // loop for each bit in nn 
      if (n & 1) y *= x;         // multiply if bit = 1 
      x *= x;                    // square x 
      n >>= 1;                   // get next bit of n 
   } 
   return y;                     // return y = pow(x,n) 
} 
 
double xpow10(double x) { 
   return ipow(x,10);            // ipow faster than pow 
} 
 


---

 
The method used in example 15.1b is easier to understand when we roll out the loop and 
reorganize: 
 
// Example 15.1c. Calculate integer power, loop unrolled 
double xpow10(double x) { 
   double x2  = x *x;            // x^2 
   double x4  = x2*x2;           // x^4 
   double x8  = x4*x4;           // x^8 
   double x10 = x8*x2;           // x^10 
   return x10;                   // return x^10 
} 
 
As we can see, it is possible to calculate pow(x,10) with only four multiplications. How 
was it possible to come from example 15.1b  to 15.1c? We took advantage of the fact that n 
is known at compile time to eliminate everything that depends only on n, including the 
while loop, the if statement and all the integer calculations. The code in example 15.1c is 
faster than 15.1b, and in this case it may be smaller as well. 
 
The conversion from example 15.1b  to 15.1c was done by me manually, but if we want to 
generate a piece of code that works for any compile-time constant n, then we need 
metaprogramming. None of the compilers I have tested can convert example 15.1a  to 
15.1c automatically, and only the Gnu compiler will convert example 15.1b  to 15.1c. We 
can only hope that future compilers will do such optimizations automatically, but as long as 
this is not the case we may need metaprogramming. 
 
The next example shows this calculation implemented with template metaprogramming. 
Don't panic if you don't understand it. I am giving this example only to show how tortuous 
and convoluted template metaprogramming is. 
 
// Example 15.1d. Integer power using template metaprogramming 
 
// Template for pow(x,N) where N is a positive integer constant. 
// General case, N is not a power of 2: 
template <bool IsPowerOf2, int N>  
class powN {  
public: 
   static double p(double x) {    
   // Remove right-most 1-bit in binary representation of N: 
   #define N1 (N & (N-1)) 
      return powN<(N1&(N1-1))==0,N1>::p(x) * powN<true,N-N1>::p(x); 
   #undef N1 
   } 
}; 
 
// Partial template specialization for N a power of 2 
template <int N> 
class powN<true,N> { 
public: 
   static double p(double x) { 
      return powN<true,N/2>::p(x) * powN<true,N/2>::p(x); 
   } 
}; 
 
// Full template specialization for N = 1. This ends the recursion 
template<> 
class powN<true,1> { 
public: 
   static double p(double x) { 
      return x; 
   } 
}; 
 


---

 
// Full template specialization for N = 0 
// This is used only for avoiding infinite loop if powN is  
// erroneously called with IsPowerOf2 = false where it should be true. 
template<> 
class powN<true,0> { 
public: 
   static double p(double x) { 
      return 1.0; 
   } 
}; 
 
// Function template for x to the power of N 
template <int N> 
static inline double IntegerPower (double x) { 
   // (N & N-1)==0 if N is a power of 2 
   return powN<(N & N-1)==0,N>::p(x); 
} 
 
// Use template to get x to the power of 10 
double xpow10(double x) { 
   return IntegerPower<10>(x); 
} 
 
If you want to know how this works, here's an explanation. Please skip the following 
explanation if you are not sure you need it. 
 
In C++ template metaprogramming, loops are implemented as recursive templates. The 
powN template is calling itself in order to emulate the while loop in example 15.1b. 
Branches are implemented by (partial) template specialization. This is how the if branch in 
example 15.1b is implemented. The recursion must always end with a non-recursing 
template specialization, not with a branch inside the template. 
 
The powN template is a class template rather than a function template because partial 
template specialization is allowed only for classes. The splitting of N into the individual bits 
of its binary representation is particularly tricky. I have used the trick that  N1 = N&(N-1)  
gives the value of N with the rightmost 1-bit removed. If N is a power of 2 then  N&(N-1)  
is 0. The constant N1 could have been defined in other ways than by a macro, but the 
method used here is the only one that works on all the compilers I have tried. 
 
The Microsoft, Intel and Gnu compilers are actually reducing example 15.1d to 15.1c as 
intended, while the Borland and Digital Mars compilers produce less optimal code because 
they fail to eliminate common sub-expressions. 
 
Why is template metaprogramming so complicated? Because the C++ template feature was 
never designed for this purpose. It just happened to be possible. Template meta-
programming is so complicated that I consider it unwise to use it. Complicated code is a risk 
factor in itself, and the cost of verifying, debugging and maintaining such code is so high 
that it rarely justifies the relatively small gain in performance. 
 
There are cases, however, where template metaprogramming is the only way to make sure 
that certain calculations are done at compile time. (Examples can be found in my vector 
class library). 
 
The D language allows compile-time if statements (called static if), but no compile-
time loops or compile-time generation of identifier names. We can only hope that such 
feature will become available in the future. If a future version of C++ should allow compile-
time if and compile-time while loops, then the transformation of example 15.1b to 
metaprogramming would be straightforward. The MASM assembly language has full 
metaprogramming features, including the ability to define function names and variable 


---

