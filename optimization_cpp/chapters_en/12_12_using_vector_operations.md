# 12 Using vector operations

 
Very long dependency chains put a strain on the out-of-order resources of the CPU, even if 
they do not carry into the next iteration of a loop. A modern CPU can typically handle more 
than a hundred pending operations (see manual 3: "The microarchitecture of Intel, AMD and 
VIA CPUs"). It may be useful to split up a loop and store intermediate results in order to 
break an extremely long dependency chain. 
 
 
12 Using vector operations 
Today's microprocessors have vector instructions that make it possible to do operations on 
all elements of a vector simultaneously. This is also called Single-Instruction-Multiple-Data 
(SIMD) operations. The total size of each vector can be 64 bits (MMX), 128 bits (XMM), 256 
bits (YMM), and 512 bits (ZMM). 
 
Vector operations are useful when doing calculations on large data sets where the same 
operation is performed on multiple data elements and the program logic allows parallel 
calculations. Examples are image processing, sound processing, and mathematical 
operations on vectors and matrixes. Algorithms that are inherently serial, such as most 
sorting algorithms, are not suited for vector operations. Algorithms that rely heavily on table 
lookup or require a lot of data shuffling, such as many encryption algorithms, are perhaps 
less suited for vector operations. 
 
The vector operations use a set of special vector registers. The maximum size of each 
vector register is 128 bits (XMM) if the SSE2 instruction set is available, 256 bits (YMM) if 
the AVX instruction set is supported by the microprocessor and the operating system, and 
512 bits when the AVX512 instruction set is available. The number of elements in each 
vector depends on the size and type of data elements, as follows: 
 


---

 
Type of 
elements 
Size of each 
element, 
bits 
Number of 
elements 
Total size of 
vector, bits 
Instruction 
set 
char 
MMX 
short int 
MMX 
int 
MMX 
int64_t 
MMX 
 
 
 
 
 
char 
SSE2 
short int 
SSE2 
int 
SSE2 
int64_t 
SSE2 
float 
SSE 
double 
SSE2 
 
 
 
 
 
char 
AVX2 
short int 
AVX2 
int 
AVX2 
int64_t 
AVX2 
float 
AVX 
double 
AVX 
 
 
 
 
 
char 
AVX512BW 
short int 
AVX512BW 
int 
AVX512 
int64_t 
AVX512 
float 
AVX512 
double 
AVX512 
 
 
 
 
 
Table 12.1. Vector classes defined in Intel header files 
 
For example, a 128-bit XMM register can be organized as a vector of eight 16-bit integers or 
four float's when the SSE2 instruction set is available. The older MMX registers, which 
are 64 bits wide, should be avoided because they cannot be mixed with x87 style floating 
point code. 
 
The 128-bit XMM vectors must be aligned by 16, i.e. stored at a memory address that is 
divisible by 16 (see below). The 256-bit YMM vectors are preferably aligned by 32 and the 
512-bit ZMM registers by 64, but the alignment requirements are less strict when compiling 
for the AVX and later instruction sets. 
 
Vector operations are particularly fast on newer processors. Many processors can calculate 
a vector just as fast as a scalar (Scalar means not a vector). The first generation of 
processors that support a new vector size often have execution units, memory ports, etc. of 
only half the size of the largest vector. These units are used twice for handling a full size 
vector. 
 
The use of vector operations is more advantageous the smaller the data elements are. For 
example, you get four float additions in the same time that it takes to do two additions 
with double's. It is almost always advantageous to use vector operations on contemporary 
CPUs if the data fit nicely into the vector registers. It may not be advantageous if a lot of 
data manipulation is required for putting the right data into the right vector elements. 
 


---

 
12.1 AVX instruction set and YMM registers 
The 128-bit XMM registers are extended to 256-bit registers named YMM in the AVX 
instruction set. The main advantage of the AVX instruction set is that it allows larger floating 
point vectors. There are also other advantages that may improve the performance 
somewhat. The AVX2 instruction set also allows 256-bit integer vectors. 
 
Code that is compiled for the AVX instruction set can run only if AVX is supported by both 
the CPU and the operating system. AVX is supported in Windows 7 and Windows Server 
2008 R2 as well as in Linux kernel version 2.6.30 and later. The AVX instruction set is 
supported in the latest compilers from Microsoft, Intel, Gnu and Clang. 
 
There is a problem when mixing code compiled with and without AVX support on some Intel 
processors. There is a performance penalty when going from AVX code to non-AVX code 
because of a change in the YMM register state. This penalty should be avoided by calling 
the intrinsic function _mm256_zeroupper() before any transition from AVX code to non-
AVX code. This can be necessary in the following cases: 
 
 
If part of a program is compiled with AVX support and another part of the program is 
compiled without AVX support then call _mm256_zeroupper() before leaving the 
AVX part. 
   
 
If a function is compiled in multiple versions with and without AVX using CPU 
dispatching then call _mm256_zeroupper() before leaving the AVX part. 
   
 
If a piece of code compiled with AVX support calls a function in a library other than 
the library that comes with the compiler, and the library has no AVX support, then 
call _mm256_zeroupper() before calling the library function. 
 
12.2 AVX512 instruction set and ZMM registers 
The 256-bit YMM registers are extended to 512-bit registers named ZMM in the AVX512 
instruction set. The number of vector registers is extended from 16 to 32 in 64 bit mode. 
There are only 8 vector registers in 32-bit mode. The 128-bit XMM registers are extended to 
256-bit registers named YMM in the AVX instruction set. Therefore, AVX512 code should 
preferably be compiled for 64-bit mode. 
 
The AVX512 instruction set also adds a set of mask registers. These are used as Boolean 
vectors. Almost any vector instruction can be masked with a mask register so that each 
vector element is calculated only if the corresponding bit in the mask register is 1. This 
makes vectorization of code with branches more efficient. 
 
There are several additional extensions to AVX512. All processors with AVX512 have some 
of these extensions, but no processor so far has them all (writing in 2016). The known and 
planned extensions to AVX512 are the following: 
 
 
AVX512F. Foundation. All AVX512 processors have this. Includes operations on 32-
bit and 64-bit integers, float and double in 512-bit vectors, including masked 
operations. 
 
AVX512VL. Includes the same operations on 128-bit and 256-bit vectors, including 
masked operations and 32 vector registers. 
 
AVX512BW. Operations on 8-bit and 16-bit integers in 512-bit vectors. 
 
AVX512DQ. Multiplication and conversion instructions with 64-bit integers. Various 
other instructions on float and double. 
 
AVX512ER. Fast reciprocal, reciprocal square root, and exponential function. 
Precise on float; approximate on double. 
 
AVX512CD. Conflict detection. Find duplicate elements in a vector. 


---

 
 
AVX512PF. Prefetch instructions with gather/scatter logic. 
 
AVX512VBMI. Permutation and shift with 8-bit granularity. 
 
AVX512IFMA. Fused multiply-and-add on 52-bit integers. 
 
AVX512_4VNNIW. Iterated dot product on 16-bit integers.  
 
AVX512_4FMAPS. Iterated fused multiply-and-add, single precision.  
 
This makes CPU dispatching more complicated. You may pick the extensions that are 
useful for a particular task and make a code branch for processors that have this extension. 
 
The use of _mm256_zeroupper() is probably not needed in AVX512 code, but this issue 
is currently under discussion. See manual 5: "Calling conventions" chapter 6.3. 
 
12.3 Automatic vectorization 
Good compilers such as the Gnu, Clang and Intel compilers can use vector operations 
automatically in cases where the parallelism is obvious. See the compiler documentation for 
detailed instructions. Example: 
 
// Example 12.1a. Automatic vectorization 
const int size = 1024; 
int a[size], b[size]; 
// ... 
for (int i = 0; i < size; i++) { 
   a[i] = b[i] + 2; 
} 
 
A good compiler will optimize this loop by using vector operations when the SSE2 or later 
instruction set is specified. The code will read four, eight, or sixteen elements of b into a 
vector register depending on the instruction set, and do an addition with another vector 
register containing (2,2,2,...), and store the four results in a. This operation will then be 
repeated as many times as the array size divided by the number of elements per vector. 
The speed is improved accordingly. It is best when the loop count is divisible by the number 
of elements per vector. You may even add dummy elements at the end of the array to make 
the array size a multiple of the vector size. 
 
There is a disadvantage when the arrays are accessed through pointers, e.g.: 
 
// Example 12.1b. Vectorization with alignment problem 
void AddTwo(int * __restrict aa, int * __restrict bb) { 
   for (int i = 0; i < size; i++) { 
      aa[i] = bb[i] + 2; 
   } 
} 
 
The most efficient vector operations require that the arrays are aligned by the vector size, 
i.e. stored at a memory address that is divisible by 16, 32 or 64. In example 12.1a, the 
compiler can align the arrays as required, but in example 12.1b, the compiler cannot know 
for sure whether the arrays are properly aligned or not. The loop can still be vectorized, but 
the code will be less efficient because the compiler has to take extra precautions to account 
for unaligned arrays. There are various things you can do to make the code more efficient 
when arrays are accessed through pointers or references: 
 
 
If the Intel compiler is used, then use #pragma vector aligned or the 
__assume_aligned directive to tell the compiler that the arrays are aligned, and 
make sure that they are. 
   


---

 
 
Declare the function inline. This may enable the compiler to reduce example 
12.1b to 12.1a. 
   
 
Enable the instruction set with the largest vector size if possible. The AVX and later 
instruction sets have very few restrictions on alignment and the resultant code will be 
efficient whether the arrays are aligned or not.  
 
The automatic vectorization works best if the following conditions are satisfied: 
 
1. Use a compiler that supports automatic vectorization, such as Gnu, Clang, Intel or 
PathScale. 
 
2. Use the latest version of the compiler. The compilers are becoming better and better 
at vectorization. 
   
3. Use appropriate compiler options to enable the desired instruction set 
(/arch:SSE2, /arch:AVX etc. for Windows, -msse2, -mavx, etc. for Linux) 
 
4. Align arrays and big structures by 16 for SSE2, preferably 32 for AVX and preferably 
64 for AVX512. 
   
5. The loop count should preferably be a constant that is divisible by the number of 
elements in a vector.  
   
6. If arrays are accessed through pointers so that the alignment is not visible in the 
scope of the function where you want vectorization then follow the advice given 
above. 
 
7. If the arrays or structures are accessed through pointers or references then tell the 
compiler explicitly that pointers do not alias, if appropriate. See the compiler 
documentation for how to do this. 
   
8. Minimize the use of branches at the vector element level 
   
9. Avoid table lookup at the vector element level 
 
You may look at the assembly output listing to see if the code is indeed vectorized as 
intended (see page 85). 
 
The compiler can also use vector operations where there is no loop if the same operation is 
performed on a sequence of consecutive variables. Example: 
 
// Example 12.2 
__declspec(align(16))     // Make all instances of S1 aligned 
struct S1 {               // Structure of 4 floats 
   float a, b, c, d; 
}; 
 
void Func() { 
   S1 x, y; 
   ... 
   x.a = y.a + 1.; 
   x.b = y.b + 2.; 
   x.c = y.c + 3.; 
   x.d = y.d + 4.; 
}; 
 


---

 
A structure of four float's fits into a 128-bit XMM register. In example 12.2, the optimized 
code will load the structure y into a vector register, add the constant vector (1,2,3,4), 
and store the result in x.  
 
The compiler is not always able to predict correctly whether vectorization will be 
advantageous or not. The Intel compiler allows you to use the #pragma vector always 
to tell the compiler to vectorize, or #pragma novector to tell the compiler not to 
vectorize. The pragmas must be placed immediately before the loop or the series of 
statements that you want them to apply to. 
 
It is advantageous to use the smallest data size that fits the application. In example 12.3a, 
for example, you can double the speed by using short int instead of int.  A short 
int is 16 bits wide, while an int is 32 bits, so you can have eight numbers of type 
short int in one vector, while you can only have four numbers of type int. Therefore, it 
is advantageous to use the smallest integer size that is big enough to hold the numbers in 
question without generating overflow. Likewise, it is advantageous to use float rather than 
double if the code can be vectorized, because a float uses 32 bits while a double uses 
64 bits.  
 
The SSE2 vector instruction set cannot multiply integers of any size other than short int 
(16 bits). There are no instructions for integer division in vectors, but the vector class library 
and the asmlib function library have functions for integer vector division. 
 
12.4 Using intrinsic functions 
It is difficult to predict whether the compiler will vectorize a loop or not. The following 
example shows a code that some compilers may not vectorize automatically. The code has 
a branch that chooses between two expressions for every element in the arrays: 
 
// Example 12.4a. Loop with branch 
 
// Loop with branch 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
 
   for (int i = 0; i < 256; i++) { 
      aa[i] = (bb[i] > 0) ? (cc[i] + 2) : (bb[i] * cc[i]); 
   } 
} 
 
It is possible to vectorize code explicitly by using the so-called intrinsic functions. This is 
useful in situations like example 12.4a where current compilers don't vectorize the code 
automatically. It is also useful in situations where automatic vectorization leads to 
suboptimal code. 
 
Intrinsic functions are primitive operations in the sense that each intrinsic function call is 
translated to just one or a few machine instructions. Intrinsic functions are supported by the 
Gnu, Clang, Intel, Microsoft and PathScale compilers. (The PGI compiler supports intrinsic 
functions, but in a very inefficient way. The Codeplay compiler has some support for intrinsic 
functions, but the function names are not compatible with the other compilers). The best 
performance is obtained with the Gnu, Clang and Intel compilers. 
 
We want to vectorize the loop in example 12.4a so that we can handle eight elements at a 
time in vectors of eight 16-bit integers. The branch inside the loop can be implemented in 
various ways depending on the available instruction set. The most compatible way is to 
make a bit-mask which is all 1's when bb[i] > 0 is true, and all 0's when false. The value 
of cc[i]+2 is AND'ed with this mask, and bb[i]*cc[i] is AND'ed with the inverted 
mask. The expression that is AND'ed with all 1's is unchanged, while the expression that is 


---

 
AND'ed with all 0's gives zero. An OR combination of these two gives the chosen 
expression.  
 
Example 12.4b shows how this can be implemented with intrinsic functions for the SSE2 
instruction set: 
 
// Example 12.4b. Vectorized with SSE2 
#include <emmintrin.h>       // Define SSE2 intrinsic functions 
 
// Function to load unaligned integer vector from array 
static inline __m128i LoadVector(void const * p) { 
   return _mm_loadu_si128((__m128i const*)p); 
} 
 
// Function to store unaligned integer vector into array 
static inline void StoreVector(void * d, __m128i const & x) { 
   _mm_storeu_si128((__m128i *)d, x); 
} 
 
// Branch/loop function vectorized: 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
 
   // Make a vector of (0,0,0,0,0,0,0,0) 
   __m128i zero = _mm_set1_epi16(0); 
   // Make a vector of (2,2,2,2,2,2,2,2) 
   __m128i two  = _mm_set1_epi16(2); 
 
   // Roll out loop by eight to fit the eight-element vectors: 
   for (int i = 0; i < 256; i += 8) { 
      // Load eight consecutive elements from bb into vector b: 
      __m128i b = LoadVector(bb + i); 
      // Load eight consecutive elements from cc into vector c: 
      __m128i c = LoadVector(cc + i); 
      // Add 2 to each element in vector c 
      __m128i c2 = _mm_add_epi16(c, two); 
      // Multiply b and c 
      __m128i bc = _mm_mullo_epi16 (b, c); 
      // Compare each element in b to 0 and generate a bit-mask: 
      __m128i mask = _mm_cmpgt_epi16(b, zero); 
      // AND each element in vector c2 with the bit-mask: 
      c2 = _mm_and_si128(c2, mask); 
      // AND each element in vector bc with the inverted bit-mask: 
      bc = _mm_andnot_si128(mask, bc); 
      // OR the results of the two AND operations: 
      __m128i a = _mm_or_si128(c2, bc); 
      // Store the result vector in eight consecutive elements in aa: 
      StoreVector(aa + i, a); 
   } 
} 
 
The resulting code will be very efficient because it handles eight elements at a time and it 
avoids the branch inside the loop. Example 12.4b executes three to seven times faster than 
example 12.4a, depending on how predictable the branch inside the loop is. 
 
The type __m128i defines a 128 bit vector containing integers. It can contain either 
sixteen integers of 8 bits each, eight integers of 16 bits each, four integers of 32 bits each, 
or two integers of 64 bits each. The type __m128 defines a 128 bit vector of four float. 
The type __m128d defines a 128 bit vector of two double.  
 
The intrinsic vector functions have names that begin with _mm. These functions are listed in 
the compiler manual or in the programming manuals from Intel: "IA-32 Intel Architecture 


---

 
Software Developer’s Manual", Volume 2A and 2B. There are hundreds of different intrinsic 
functions and it can be difficult to find the right function for a particular purpose. 
 
The clumsy AND-OR construction in example 12.4b can be replaced by a blend instruction 
if the SSE4.1 instruction set is available: 
 
// Example 12.4c. Same example, vectorized with SSE4.1 
 
// Function to load unaligned integer vector from array 
static inline __m128i LoadVector(void const * p) { 
   return _mm_loadu_si128((__m128i const*)p); 
} 
 
// Function to store unaligned integer vector into array 
static inline void StoreVector(void * d, __m128i const & x) { 
   _mm_storeu_si128((__m128i *)d, x); 
} 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
 
   // Make a vector of (0,0,0,0,0,0,0,0) 
   __m128i zero = _mm_set1_epi16(0); 
   // Make a vector of (2,2,2,2,2,2,2,2) 
   __m128i two  = _mm_set1_epi16(2); 
 
   // Roll out loop by eight to fit the eight-element vectors: 
   for (int i = 0; i < 256; i += 8) { 
      // Load eight consecutive elements from bb into vector b: 
      __m128i b = LoadVector(bb + i); 
      // Load eight consecutive elements from cc into vector c: 
      __m128i c = LoadVector(cc + i); 
      // Add 2 to each element in vector c 
      __m128i c2 = _mm_add_epi16(c, two); 
      // Multiply b and c 
      __m128i bc = _mm_mullo_epi16 (b, c); 
      // Compare each element in b to 0 and generate a bit-mask: 
      __m128i mask = _mm_cmpgt_epi16(b, zero); 
      // Use mask to choose between c2 and bc for each element 
      __m128i a = _mm_blendv_epi8(bc, c2, mask); 
      // Store the result vector in eight consecutive elements in aa: 
      StoreVector(aa + i, a); 
   } 
} 
 
You have to include the appropriate header file for the instruction set that you want to 
compile for. The names of the header files are as follows: 
 
Instruction set 
Header file 
MMX 
mmintrin.h 
SSE 
xmmintrin.h 
SSE2 
emmintrin.h 
SSE3 
pmmintrin.h 
Suppl. SSE3 
tmmintrin.h 
SSE4.1 
smmintrin.h 
SSE4.2 
nmmintrin.h (MS) 
smmintrin.h (Gnu) 
AES, PCLMUL 
wmmintrin.h 
AVX 
immintrin.h 
AMD SSE4A 
ammintrin.h 
AMD XOP 
ammintrin.h (MS) 
xopintrin.h (Gnu) 


---

 
AMD FMA4 
fma4intrin.h (Gnu) 
all 
intrin.h (MS) 
x86intrin.h (Gnu) 
Table 12.2. Header files for intrinsic functions 
 
You have to make sure that the CPU supports the corresponding instruction set. If you are 
including a header file for a higher instruction set than the CPU supports then you are 
risking to insert an instruction that the CPU doesn't support, and the program will crash. See 
page 125 for how to check for the supported instruction set. 
Aligning data 
Loading data into a vector goes faster if the data are aligned to an address divisible by the 
vector size (16 or 32 bytes). This has a significant effect on older processors and on Intel 
Atom processors, but is less important on most newer processors. The following example 
shows how to align arrays. 
 
// Example 12.5. Aligned arrays 
 
// Define macro for aligning data 
#ifdef _MSC_VER              // If Microsoft compiler 
#define Alignd(X) __declspec(align(16)) X 
#else                        // Gnu compiler, etc. 
#define Alignd(X) X __attribute__((aligned(16))) 
#endif 
 
const int size = 256;           // Array size 
 
Alignd ( short int aa[size] );  // Make three aligned arrays 
Alignd ( short int bb[size] ); 
Alignd ( short int cc[size] ); 
 
// Function to load aligned integer vector from array 
static inline __m128i LoadVectorA(void const * p) { 
   return _mm_load_si128((__m128i const*)p); 
} 
 
// Function to store aligned integer vector into array 
static inline void StoreVectorA(void * d, __m128i const & x) { 
   _mm_store_si128((__m128i *)d, x); 
} 
 
Vectorized table lookup 
Lookup tables can be useful for optimizing code, as explained on page 135. Unfortunately, 
table lookup is often an obstacle to vectorization. The newest instruction sets include a few 
instructions that may be used for vectorized table lookup. These instructions are 
summarized below. 
 


---

 
Intrinsic function 
Max. number 
of elements 
in table 
Size of each table 
element 
Number of 
simultaneous 
lookups 
Instruction set 
needed 
_mm_shuffle_epi8 
1 byte = char 
SSSE3 
_mm_perm_epi8 
1 byte = char 
XOP, AMD only 
_mm_permutevar_ps 
4 bytes = float or int 
AVX 
_mm256_permutevar_ps 
4 bytes = float or int 
AVX2 
_mm_i32gather_epi32 
unlimited 
4 bytes = int 
AVX2 
_mm256_i32gather_epi32 
unlimited 
4 bytes = int 
AVX2 
_mm_i64gather_epi32 
unlimited 
8 bytes = int64_t 
AVX2 
_mm256_i64gather_epi32 
unlimited 
8 bytes = int64_t 
AVX2 
_mm_i32gather_ps 
unlimited 
4 bytes = float 
AVX2 
_mm256_i32gather_ps 
unlimited 
4 bytes = float 
AVX2 
_mm_i64gather_pd 
unlimited 
8 bytes = double 
AVX2 
_mm256_i64gather_pd 
unlimited 
8 bytes = double 
AVX2 
Table 12.3. Intrinsic functions for vectorized table lookup 
 
Using intrinsic functions can be quite tedious and the code becomes bulky and difficult to 
read. It is often easier to use vector classes, as explained in the next section. 
 
12.5 Using vector classes 
Programming in the way of example 12.4b and 12.4c is quite tedious indeed. It is possible 
to write the same in a more clear and intelligible way by wrapping the vectors into C++ 
classes and using overloaded operators for things like adding vectors. The operators are 
inlined so that the resulting machine code becomes the same as if you had used intrinsic 
functions. It is just easier to write a + b than to write _mm_add_epi16(a,b). 
 
Various libraries of predefined vector classes are currently available, including one from 
Intel and one from me. My vector class library (VCL) has many features, see 
http://www.agner.org/optimize/ - vectorclass www.agner.org/optimize/#vectorclass. The Intel 
vector class library has not been updated lately and may be considered obsolete. 
 
Vector class library 
Intel 
VCL (Agner) 
Available from 
Intel and Microsoft C++ 
compilers 
www.agner.org/ 
optimize/#vectorclass 
Include file 
dvec.h 
vectorclass.h 
Supported compilers 
Intel, Microsoft 
Intel, Microsoft, Gnu, Clang 
Supported operating systems 
Windows, Linux, Mac 
Windows, Linux, Mac, BSD 
Instruction set control 
no 
yes 
License 
license included in 
compiler price 
GNU General Public License, 
optional commercial license 
Table 12.4. Vector class libraries 
 
 
The following table lists the available vector classes. Including the appropriate header file 
will give you access to all of these classes. 
 


---

 
Size of each 
element, 
bits 
Number of 
elements in 
vector 
Type of 
elements 
Total size of 
vector, bits 
Vector 
class, Intel 
Vector 
class, VCL 
char 
Is8vec8 
 
unsigned 
char 
Iu8vec8 
 
short int 
Is16vec4 
 
unsigned 
short int 
Iu16vec4 
 
int 
Is32vec2 
 
unsigned 
int 
Iu32vec2 
 
int64_t 
I64vec1 
 
char 
Is8vec16 
Vec16c 
unsigned 
char 
Iu8vec16 
Vec16uc 
short int 
Is16vec8 
Vec8s 
unsigned 
short int 
Iu16vec8 
Vec8us 
int 
Is32vec4 
Vec4i 
unsigned 
int 
Iu32vec4 
Vec4ui 
int64_t 
I64vec2 
Vec2q 
uint64_t 
 
Vec2uq 
char 
 
Vec32c 
unsigned 
char 
 
Vec32uc 
short int 
 
Vec16s 
unsigned 
short int 
 
Vec16us 
int 
 
Vec8i 
unsigned 
int 
 
Vec8ui 
int64_t 
 
Vec4q 
uint64_t 
 
Vec4uq 
int 
 
Vec16i 
unsigned 
int 
 
Vec16ui 
int64_t 
 
Vec8q 
uint64_t 
 
Vec8uq 
float 
F32vec4 
Vec4f 
double 
F64vec2 
Vec2d 
float 
F32vec8 
Vec8f 
double 
F64vec4 
Vec4d 
float 
 
Vec16f 
double 
 
Vec8d 
Table 12.5. Vector classes defined in two libraries 
 
It is not recommended to use the vectors of 64 bits total size, because these are 
incompatible with floating point code. If you do use the 64-bit vectors then you have to 
execute _mm_empty() after the 64-bit vector operations and before any floating point 
code. The bigger vectors do not have this problem.  
Vectors of 256 and 512 bits size are only available if supported by the CPU and the 
operating system (see page 109). My VCL vector class library can emulate a 256-bit vector 
as two 128-bit vectors or a 512-bit vector as two 256-bit vectors or four 128-bit vectors. 
 


---

 
The following example shows the same code as example 12.4b, rewritten with the use of 
Intel vector classes: 
 
// Example 12.4d. Same example, using Intel vector classes 
#include <dvec.h>  // Define vector classes 
 
// Function to load unaligned integer vector from array 
static inline __m128i LoadVector(void const * p) { 
   return _mm_loadu_si128((__m128i const*)p);} 
 
// Function to store unaligned integer vector into array 
static inline void StoreVector(void * d, __m128i const & x) { 
   _mm_storeu_si128((__m128i *)d, x);} 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
 
   // Make a vector of (0,0,0,0,0,0,0,0) 
   Is16vec8 zero(0,0,0,0,0,0,0,0); 
   // Make a vector of (2,2,2,2,2,2,2,2) 
   Is16vec8 two(2,2,2,2,2,2,2,2); 
 
   // Roll out loop by eight to fit the eight-element vectors: 
   for (int i = 0; i < 256; i += 8) { 
      // Load eight consecutive elements from bb into vector b: 
      Is16vec8 b = LoadVector(bb + i); 
      // Load eight consecutive elements from cc into vector c: 
      Is16vec8 c = LoadVector(cc + i); 
      // result = b > 0 ? c + 2 : b * c; 
      Is16vec8 a = select_gt(b, zero, c + two, b * c); 
      // Store the result vector in eight consecutive elements in aa: 
      StoreVector(aa + i, a); 
   } 
} 
 
The same example using my VCL vector classes looks like this: 
 
// Example 12.4e. Same example, using VCL 
#include "vectorclass.h"     // Define vector classes 
 
void SelectAddMul(short int aa[], short int bb[], short int cc[]) { 
   // Define vector objects 
   Vec16s a, b, c; 
 
   // Roll out loop by eight to fit the eight-element vectors: 
   for (int i = 0; i < 256; i += 16) { 
      // Load eight consecutive elements from bb into vector b: 
      b.load(bb+i); 
      // Load eight consecutive elements from cc into vector c: 
      c.load(cc+i); 
      // result = b > 0 ? c + 2 : b * c; 
      a = select(b > 0, c + 2, b * c); 
      // Store the result vector in eight consecutive elements in aa: 
      a.store(aa+i); 
   } 
} 
 
The Microsoft compiler does not allow vector objects as function parameters because of 
alignment problems. It is recommended to use a constant reference instead: 
 
// Example 12.6. Function with vector parameters 
Vec4f polynomial (Vec4f const & x) { 
   // polynomial(x) = 2.5*x^2 - 8*x + 2 
   return (2.5f * x - 8.0f) * x + 2.0f; 


---

 
} 
 
CPU dispatching with vector classes 
The VCL vector class library makes it possible to compile for different instruction sets from 
the same source code. The library has preprocessing directives that select the best 
implementation for a given instruction set. 
 
The following example shows how to make the SelectAddMul example (12.4e) with 
automatic CPU dispatching. The code in this example should be compiled three times, one 
for the SSE2 instruction set, one for SSE4.1 and one for AVX2 and all three versions should 
be linked into the same executable. SSE2 is the minimum supported instruction set for the 
vector class library, SSE4.1 gives an advantage in the select function, and the AVX2 
instruction set gives the advantage of bigger vector registers. The vector class library will 
use one 256-bit vector register for the class Vec16s when compiling for AVX2, or two 128-
bit vector registers when compiling for a lower instruction set. The preprocessing macro 
INSTRSET is used for giving the function a different name for each instruction set. A CPU 
dispatcher then sets a function pointer to the best possible version. See the vectorclass 
manual for details. 
 
// Example 12.7. Vector class code with automatic CPU dispatching 
#include "vectorclass.h"  // vector class library 
#include <stdio.h>        // define fprintf 
 
// define function type 
typedef void FuncType(short int aa[], short int bb[], short int cc[]); 
 
// function prototypes for each version 
FuncType SelectAddMul, SelectAddMul_SSE2, SelectAddMul_SSE41, 
SelectAddMul_AVX2, SelectAddMul_dispatch;  
 
// Define function name depending on instruction set 
#if   INSTRSET == 2                    // SSE2 
#define FUNCNAME SelectAddMul_SSE2 
#elif INSTRSET == 5                    // SSE4.1 
#define FUNCNAME SelectAddMul_SSE41 
#elif INSTRSET == 8                    // AVX2 
#define FUNCNAME SelectAddMul_AVX2 
#endif 
 
// specific version of the function. Compile once for each version 
void FUNCNAME(short int aa[], short int bb[], short int cc[]) { 
   Vec16s a, b, c; // Define biggest possible vector objects 
   // Roll out loop by 16 to fit the biggest vectors: 
   for (int i = 0; i < 256; i += 16) { 
      b.load(bb+i); 
      c.load(cc+i); 
      a = select(b > 0, c + 2, b * c); 
      a.store(aa+i); 
   } 
} 
 
#if INSTRSET == 2 
// make dispatcher in only the lowest of the compiled versions 
#include "instrset_detect.cpp" // instrset_detect function 
 
// Function pointer initially points to the dispatcher. 
// After first call it points to the selected version 
FuncType * SelectAddMul_pointer = &SelectAddMul_dispatch; 
  
// Dispatcher 
void SelectAddMul_dispatch(short int aa[], short int bb[], 


---

 
   short int cc[]) { 
   // Detect supported instruction set 
   int iset = instrset_detect(); 
   // Set function pointer 
   if      (iset >= 8) SelectAddMul_pointer = &SelectAddMul_AVX2; 
   else if (iset >= 5) SelectAddMul_pointer = &SelectAddMul_SSE41; 
   else if (iset >= 2) SelectAddMul_pointer = &SelectAddMul_SSE2; 
   else { 
      // Error: lowest instruction set not supported 
      fprintf(stderr, "\nError: Instruction set SSE2 not supported"); 
      return; 
    } 
   // continue in dispatched version 
   return (*SelectAddMul_pointer)(aa, bb, cc); 
} 
 
// Entry to dispatched function call 
inline void SelectAddMul(short int aa[], short int bb[], 
   short int cc[]) { 
   // go to dispatched version 
   return (*SelectAddMul_pointer)(aa, bb, cc); 
} 
 
#endif  // INSTRSET == 2 
 
 
12.6 Transforming serial code for vectorization 
Not all code has a parallel structure that can easily be organized into vectors. A lot of code 
is serial in the sense that each calculation depends on the previous one. It may neverthe-
less be possible to organize the code in a way that can be vectorized if the code is 
repetitive. The simplest case is a sum of a long list of numbers: 
 
// Example 12.8a. Sum of a list 
float a[100]; 
float sum = 0; 
for (int i = 0; i < 100; i++) sum += a[i]; 
 
The above code is serial because each value of sum depends on the preceding value of 
sum. The trick is to roll out the loop by n and reorganize the code so that each value 
depends on the value that is n places back, where n is the number of elements in a vector. If 
n = 4, we have: 
 
// Example 12.8b. Sum of a list, rolled out by 4 
float a[100]; 
float s0 = 0, s1 = 0, s2 = 0, s3 = 0, sum; 
for (int i = 0; i < 100; i += 4) { 
   s0 += a[i]; 
   s1 += a[i+1]; 
   s2 += a[i+2]; 
   s3 += a[i+3]; 
} 
sum = (s0+s1)+(s2+s3); 
 
Now s0, s1, s2 and s3 can be combined into a 128-bit vector so that we can do four 
additions in one operation. A good compiler will convert example 12.8a to 12.8b 
automatically and vectorize the code if we specify the options for fast math and the SSE or 
higher instruction set. 
 
More complicated cases cannot be vectorized automatically. For example, let's look at the 
example of a Taylor series. The exponential function can be calculated by the series: 


---

 




!
n
n
x
n
x
e
 
A C++ implementation may look like this: 
 
// Example 12.9a. Taylor series 
float Exp(float x) {       // Approximate exp(x) for small x 
   float xn = x;           // x^n 
   float sum = 1.f;        // sum, initialize to x^0/0! 
   float nfac = 1.f;       // n factorial 
   for (int n = 1; n <= 16; n++) { 
      sum += xn / nfac; 
      xn *= x; 
      nfac *= n+1; 
   } 
   return sum; 
} 
 
Here, each value xn is calculated from the previous value as xn = x∙xn-1, and each value of n! 
is calculated from the previous value as n! = n∙(n-1)!. If we want to roll out the loop by four, 
we will have to calculate each value from the value that is four places back. Thus, we will 
calculate xn as x4∙xn-4. There is no easy way to roll out the calculation of the factorials, but 
this is not necessary because the factorials don't depend on x so we can store the values in 
a pre-calculated table. Even better: store the reciprocal factorials so that we don't have to do 
the divisions (Division is slow, you know). The code can now be vectorized as follows (using 
Intel vector classes): 
 
// Example 12.9b. Taylor series, vectorized 
#include <dvec.h>          // Define vector classes (Intel) 
#include <pmmintrin.h>     // SSE3 required 
 
// This function adds the elements of a vector, uses SSE3. 
// (This is faster than the function add_horizontal) 
static inline float add_elements(__m128 const & x) { 
   __m128 s; 
   s = _mm_hadd_ps(x, x); 
   s = _mm_hadd_ps(s, s); 
   return _mm_cvtss_f32(s); 
} 
 
float Exp(float x) {       // Approximate exp(x) for small x 
   __declspec(align(16))   // align table by 16 
   const float coef[16] = {      // table of 1/n! 
      1., 1./2., 1./6., 1./24., 1./120., 1./720., 1./5040., 
      1./40320., 1./362880., 1./3628800., 1./39916800.,  
      1./4.790016E8, 1./6.22702E9, 1./8.71782E10, 
      1./1.30767E12, 1./2.09227E13}; 
   float x2 = x * x;              // x^2 
   float x4 = x2 * x2;            // x^4 
   // Define vectors of four floats 
   F32vec4 xxn(x4, x2*x, x2, x);  // x^1, x^2, x^3, x^4 
   F32vec4 xx4(x4);               // x^4 
   F32vec4 s(0.f, 0.f, 0.f, 1.f); // initialize sum 
   for (int i = 0; i < 16; i += 4) {  // Loop by 4 
      s += xxn * _mm_load_ps(coef+i); // s += x^n/n! 
      xxn *= xx4;                     // next four x^n 
   } 
   return add_elements(s);            // add the four sums 
} 
 
This loop calculates four consecutive terms in one vector. It may be worthwhile to unroll the 
loop further if the loop is long because the speed here is likely to be limited by the latency of 
the multiplication of xxn rather than the throughput (see p. 105). The table of coefficients is 


---

 
calculated at compile time here. It may be more convenient to calculate the table at runtime, 
if only you make sure it is only calculated once, rather than each time the function is called. 
 
12.7 Mathematical functions for vectors 
There are various function libraries for computing mathematical functions such as 
logarithms, exponential functions, trigonometric functions, etc. in vectors. These function 
libraries are useful for vectorizing mathematical code.  
 
There are two different kinds of vector math libraries: long vector libraries and short vector 
libraries. To explain the difference, let's say that you want to calculate the same function on 
a thousand numbers. With a long vector library, you are feeding an array of thousand 
numbers as a parameter to the library function, and the function stores the thousand results 
in another array. The disadvantage of using a long vector library is that if you are doing a 
sequence of calculations then you have to store the intermediate result of each step of the 
sequence in a temporary array before calling the function for the next step. With a short 
vector library, you divide the data set into sub-vectors that fit the size of the vector registers 
in the CPU. If the vector registers can hold e.g. four numbers, then you have to call the 
library function 250 times with four numbers at a time packed into a vector register. The 
library function will return the result in a vector register which can be fed directly to the next 
step in the sequence of calculations without the need to store intermediate results in RAM 
memory. This may be faster despite the extra function calls because the CPU can do 
calculations while simultaneously prefetching the code of the next function. However, the 
short vector method may be at a disadvantage if the sequence of calculations forms a long 
dependency chain. We want the CPU to start calculations on the second sub-vector before 
it has finished the calculations on the first sub-vector. A long dependency chain may fill up 
the queue of pending instructions in the CPU and prevent it from fully utilizing its out-of-
order calculation capabilities. 
 
Here is a list of some long vector math libraries: 
 
 
Intel vector math library (VML, MKL). Works with all x86 platforms. This library has 
reduced performance on non-Intel CPUs unless you are overriding Intel's CPU 
dispatcher. See page 134. 
 
Intel Performance Primitives (IPP). Works with all x86 platforms. Works well with 
non-Intel CPUs. Includes many functions for statistics, signal processing and image 
processing. 
 
Yeppp. Open source library. Supports x86 and ARM platforms and various 
programming languages. www.yeppp.info 
 
And here is a list of short vector math libraries: 
 
 
Intel short vector math library (SVML). This is supplied with Intel's compilers and 
invoked with automatic vectorization. The Gnu compiler can use this library with the 
option -mveclibabi=svml. This library may have reduced performance on non-
Intel CPUs unless you are overriding Intel's CPU dispatcher. See page 134. 
 
AMD LIBM library. Only available for 64-bit Linux and Windows platforms. This 
library has reduced performance on CPUs without the FMA4 instruction set. (This 
instruction set was originally designed by Intel but is currently only supported on 
AMD CPUs). The Gnu compiler can use this library with the option 
-mveclibabi=acml. 
 
My VCL vector class library. Open source. Supports all x86 platforms. Microsoft, 
Intel, Gnu and Clang compilers. The code is inlined - no need to link with external 
libraries. www.agner.org/optimize/#vectorclass 
 
All these libraries have very good performance and precision. The speed is many times 
faster than any non-vector library. 


---

 
 
The function names in the SVML and LIBM libraries are not well documented. The 
examples in this table may be of some help if you want to call the library functions directly: 
 
Library 
exp function of 4 
floats 
exp function of 2 double 
Intel SVML v.10.2 & earlier 
vmlsExp4 
vmldExp2 
Intel SVML v.10.3 & later 
__svml_expf4 
__svml_exp2 
Intel SVML + ia32intrin.h 
_mm_exp_ps 
_mm_exp_pd 
AMD Core Math Library 
__vrs4_expf 
__vrd2_exp 
AMD LIBM Library 
amd_vrs4_expf 
amd_vrd2_exp 
VCL vector class library 
exp 
exp 
 
12.8 Aligning dynamically allocated memory 
Memory allocated with new or malloc is typically aligned by 8 rather than by 16. This is a 
problem with vector operations when alignment by 16 is required. The Intel compiler has 
solved this problem by defining _mm_malloc and _mm_free.  
 
A more general method is to wrap the allocated array into a container class that takes care 
of the alignment. See www.agner.org/optimize/cppexamples.zip for examples of how to 
make aligned arrays with vector access. 
 
12.9 Aligning RGB video or 3-dimensional vectors 
RGB image data have three values per point. This does not fit into a vector of e.g. four 
floats. The same applies to 3-dimensional geometry and other odd-sized vector data. The 
data have to be aligned by the vector size for the sake of efficiency. Using unaligned reads 
and writes may slow down the execution to the point where it is less advantageous to use 
vector operations. You may choose one of the following solutions, depending on what fits 
best into the algorithm in question: 
 
 
Put in an unused fourth value to make the data fit into the vector. This is a simple 
solution, but it increases the amount of memory used. You may avoid this method if 
memory access is a bottleneck. 
   
 
Organize the data into groups of four (or eight) points with the four R value in one 
vector, the four G values in the next vector, and the four B value in the last vector. 
   
 
Organize the data with all the R values first, then all the G values, and last all the B 
values. 
 
The choice of which method to use depends on what fits best into the algorithm in question. 
You may choose the method that gives the simplest code. 
 
If the number of points is not divisible by the vector size then add a few unused points in the 
end in order to get an integral number of vectors. 
 
12.10 Conclusion 
There is a lot to gain in speed by using vectors if the code contains natural parallelism. The 
gain depends on the number of elements per vector. The simplest and most clean solution 
is to rely on automatic vectorization by the compiler. The compiler will vectorize the code 
automatically in simple cases where the parallelism is obvious and the code contains only 
simple standard operations. All you have to do is to enable the SSE2 or later instruction set. 
 


---

 
However, there are many cases where the compiler is unable to vectorize the code 
automatically or does so in a suboptimal way. Here you have to vectorize the code explicitly. 
There are various ways to do this: 
 
 
Use assembly language 
   
 
Use intrinsic functions 
   
 
Use predefined vector classes 
   
The easiest way to vectorize code explicitly is by using a vector class library. You may 
combine this with intrinsic functions if you need things that are not defined in the vector 
class library. Whether you choose to use intrinsic functions or vector classes is just a matter 
of convenience - there is no difference in performance. A good optimizing compiler should 
produce the same code in either case. Intrinsic functions look clumsy and tedious. The code 
becomes more readable when you are using vector classes and overloaded operators. 
 
A good compiler is often able to optimize the code further after you have vectorized it 
manually. The compiler can use optimization techniques such as function inlining, common 
subexpression elimination, constant propagation, loop optimization, etc. These techniques 
are rarely used in manual assembly coding because it makes the code unwieldy, error 
prone, and almost impossible to maintain. The combination of manual vectorization with 
further optimization by the compiler can therefore give the best result in many cases. 
Current compilers are not always good at constant propagation and certain other 
optimization techniques on vector code. Therefore, it is sometimes better to rely on 
automatic vectorization by the compiler in cases where the compiler can do so without 
problems. Some experimentation may be needed to find the best solution. 
 
Vectorized code often contains a lot of extra instructions for converting the data to the right 
format and getting them into the right positions in the vectors. This data conversion and 
shuffling can sometimes take more time than the actual calculations. This should be taken 
into account when deciding whether it is profitable to use vectorized code or not.  
 
I will conclude this section by summing up the factors that decide how advantageous 
vectorization is. 
 
Factors that make vectorization favorable: 
 
Small data types: char, short int, float. 
 
Similar operations on all data in large arrays. 
 
Array size divisible by vector size. 
 
Unpredictable branches that select between two simple expressions. 
 
Operations that are only available with vector operands: minimum, maximum, 
saturated addition, fast approximate reciprocal, fast approximate reciprocal square 
root, RGB color difference. 
 
Vector instruction set available, e.g. AVX, AVX2, AVX-512 
 
Mathematical vector function libraries. 
 
Use Gnu, Clang or Intel compiler. 
 
Use CPUs with execution units same size as vector register. 
 
Factors that make vectorization less favorable: 
 
Larger data types: int64_t, double. 
 
Misaligned data. 
 
Extra data conversion, shuffling, packing, unpacking needed. 
 
Predictable branches that can skip large expressions when not selected. 
 
Compiler has insufficient information about pointer alignment and aliasing. 


---

