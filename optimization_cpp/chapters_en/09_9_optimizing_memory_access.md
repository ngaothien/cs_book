# 9 Optimizing memory access

 
; Example 8.26b compiled to assembly: 
ALIGN     4                                ; align by 4 
PUBLIC ?Func@@YAXQAHAAH@Z                  ; mangled function name 
?Func@@YAXQAHAAH@Z PROC NEAR              ; start of Func 
; parameter 1: 4 + esp                     ; a 
; parameter 2: 8 + esp                     ; r 
$B1$1:                                     ; unused label 
        mov       eax, DWORD PTR [esp+4]   ; eax = address of a 
        mov       edx, DWORD PTR [esp+8]   ; edx = address in r 
        mov       ecx, DWORD PTR [edx]     ; ecx = Induction 
        lea       edx, DWORD PTR [eax+400] ; edx = point to end of a 
$B2$2:                                     ; top of loop 
        mov       DWORD PTR [eax], ecx     ; a[i] = Induction; 
        mov       DWORD PTR [eax+4], ecx   ; a[i+1] = Induction; 
        add       ecx, 1                   ; Induction++; 
        add       eax, 8                   ; point to a[i+2] 
        cmp       edx, eax                 ; compare with end of array 
        ja        $B2$2                    ; jump to top of loop  
$B2$3:                                     ; unused label 
        ret                                ; return from Func 
        ALIGN     4 
; mark_end; 
?Func2@@YAXQAHAAH@Z ENDP 
 
This solution is clearly better. The loop body now contains only six instructions rather than 
nine, even though it is doing two iterations in one. The compiler has replaced i by a second 
induction variable (eax) which contains the address of the current array element. Rather 
than comparing i with 100 in the loop control it compares the array pointer eax to the 
address of the end of the array, which it has calculated in advance and stored in edx. 
Furthermore, this solution is using one register less so that it doesn't have to push and pop 
ebx. 
 
 
9 Optimizing memory access 
9.1 Caching of code and data 
A cache is a proxy for the main memory in a computer. The proxy is smaller and closer to 
the CPU than the main memory and therefore it is accessed much faster. There may be two 
or three levels of cache for the sake of fastest possible access to the most used data. 
 
The speed of CPUs is increasing faster than the speed of RAM memory. Efficient caching is 
therefore becoming more and more important. 
 
9.2 Cache organization 
It is useful to know how a cache is organized if you are making programs that have big data 
structures with non-sequential access and you want to prevent cache contention. You may 
skip this section if you are satisfied with more heuristic guidelines.  
 
Most caches are organized into lines and sets. Let me explain this with an example. My 
example is a cache of 8 kb size with a line size of 64 bytes. Each line covers 64 consecutive 
bytes of memory. One kilobyte is 1024 bytes, so we can calculate that the number of lines is 
8*1024/64 = 128. These lines are organized as 32 sets  4 ways. This means that a 
particular memory address cannot be loaded into an arbitrary cache line. Only one of the 32 
sets can be used, but any of the 4 lines in the set can be used. We can calculate which set 
of cache lines to use for a particular memory address by the formula: (set) = (memory 
address) / (line size) % (number of sets). Here, / means integer division with truncation, and % 
means modulo. For example, if we want to read from memory address a = 10000, then we 


---

 
have (set) = (10000 / 64) % 32 = 28. This means that a must be read into one of the four 
cache lines in set number 28. The calculation becomes easier if we use hexadecimal 
numbers because all the numbers are powers of 2. Using hexadecimal numbers, we have a 
= 0x2710 and (set) = (0x2710 / 0x40) % 0x20 = 0x1C. Reading or writing a variable from 
address 0x2710 will cause the cache to load the entire 64 or 0x40 bytes from address 
0x2700 to 0x273F into one of the four cache lines from set 0x1C. If the program afterwards 
reads or writes to any other address in this range then the value is already in the cache so 
we don't have to wait for another memory access. 
 
Assume that a program reads from address 0x2710 and later reads from addresses 
0x2F00, 0x3700, 0x3F00 and 0x4700. These addresses all belong to set number 0x1C. 
There are only four cache lines in each set. If the cache always chooses the least recently 
used cache line then the line that covered the address range from 0x2700 to 0x273F will be 
evicted when we read from 0x4700. Reading again from address 0x2710 will cause a cache 
miss. But if the program had read from different addresses with different set values then the 
line containing the address range from 0x2700 to 0x273F would still be in the cache. The 
problem only occurs because the addresses are spaced a multiple of 0x800 apart. I will call 
this distance the critical stride. Variables whose distance in memory is a multiple of the 
critical stride will contend for the same cache lines. The critical stride can be calculated as 
(critical stride) = (number of sets)  (line size) = (total cache size) / (number of ways). 
 
If a program contains many variables and objects that are scattered around in memory then 
there is a risk that several variables happen to be spaced by a multiple of the critical stride 
and cause contentions in the data cache. The same can happen in the code cache if there 
are many functions scattered around in program memory. If several functions that are used 
in the same part of the program happen to be spaced by a multiple of the critical stride then 
this can cause contentions in the code cache. The subsequent sections describe various 
ways to avoid these problems. 
 
More details about how caches work can be found in Wikipedia under CPU cache 
(en.wikipedia.org/wiki/L2_cache). 
 
The details of cache organization for different processors are covered in manual 3: "The 
microarchitecture of Intel, AMD and VIA CPUs". 
 
9.3 Functions that are used together should be stored together 
The code cache works most efficiently if functions that are used near each other are also 
stored near each other in the code memory. The functions are usually stored in the order in 
which they appear in the source code. It is therefore a good idea to collect the functions that 
are used in the most critical part of the code together near each other in the same source 
file. Keep often used functions separate from seldom used functions, and put seldom used 
branches such as error handling in the end of a function or in a separate function. 
 
Sometimes, functions are kept in different source files for the sake of modularity. For 
example, it may be convenient to have the member functions of a parent class in one 
source file and the derived class in another source file. If the member functions of parent 
class and derived class are called from the same critical part of the program then it can be 
advantageous to keep the two modules contiguous in program memory. This can be done 
by controlling the order in which the modules are linked together. The link order is usually 
the order in which the modules appear in the project window or makefile. You can check the 
order of functions in memory by requesting a map file from the linker. The map file tells the 
address of each function relative to the beginning of the program. The map file includes the 
addresses of library functions linked from static libraries (.lib or .a), but not dynamic 
libraries (.dll or .so). There is no easy way to control the addresses of dynamically linked 
library functions. 
 


---

 
9.4 Variables that are used together should be stored together 
Cache misses are very expensive. A variable can be fetched from the cache in just a few 
clock cycles, but it can take more than a hundred clock cycles to fetch the variable from 
RAM memory if it is not in the cache. 
 
The cache works most efficiently if pieces of data that are used together are stored near 
each other in memory. Variables and objects should preferably be declared in the function 
in which they are used. Such variables and objects will be stored on the stack, which is very 
likely to be in the level-1 cache. The different kinds of variable storage are explained on 
page 26. Avoid global and static variables if possible, and avoid dynamic memory allocation 
(new and delete). 
 
Object oriented programming can be an efficient way of keeping data together. Data 
members of a class (also called properties) are always stored together in an object of the 
class. Data members of a parent class and a derived class are stored together in an object 
of the derived class (see page 52). 
 
The order in which data are stored can be important if you have big data structures. For 
example, if a program has two arrays, a and b, and the elements are accessed in the order 
a[0], b[0], a[1], b[1], ... then you may improve the performance by organizing the data 
as an array of structures: 
 
// Example 9.1a 
int Func(int); 
const int size = 1024; 
int a[size], b[size], i; 
... 
for (i = 0; i < size; i++) { 
   b[i] = Func(a[i]); 
} 
 
The data in this example can be accessed sequentially in memory if organized as follows: 
 
// Example 9.1b 
int Func(int); 
const int size = 1024; 
struct Sab {int a; int b;}; 
Sab ab[size]; 
int i; 
... 
for (i = 0; i < size; i++) { 
   ab[i].b = Func(ab[i].a); 
} 
 
There will be no extra overhead in the program code for making the structure in example 
9.1b. On the contrary, the code becomes simpler because it needs only calculate element 
addresses for one array rather than two. 
 
Some compilers will use different memory spaces for different arrays even if they are never 
used at the same time. Example: 
 
// Example 9.2a 
void F1(int   x[]); 
void F2(float x[]); 
 
void F3(bool y) {    
   if (y) { 
      int a[1000]; 
      F1(a); 
   } 


---

 
   else { 
      float b[1000]; 
      F2(b); 
   } 
} 
 
Here it is possible to use the same memory area for a and b because their live ranges do 
not overlap. You can save a lot of cache space by joining a and b in a union: 
 
// Example 9.2b 
void F3(bool y) {    
   union { 
      int   a[1000]; 
      float b[1000]; 
   }; 
   if (y) { 
      F1(a); 
   } 
   else { 
      F2(b); 
   } 
} 
 
Using a union is not a safe programming practice, of course, because you will get no 
warning from the compiler if the uses of a and b overlap. You should use this method only 
for big objects that take a lot of cache space. Putting simple variables into a union is not 
optimal because it prevents the use of register variables. 
 
9.5 Alignment of data 
A variable is accessed most efficiently if it is stored at a memory address which is divisible 
by the size of the variable. For example, a double takes 8 bytes of storage space. It should 
therefore preferably be stored at an address divisible by 8. The size should always be a 
power of 2. Objects bigger than 16 bytes should be stored at an address divisible by 16. 
You can generally assume that the compiler takes care of this alignment automatically. 
 
The alignment of structure and class members may cause a waste of cache space, as 
explained in example 7.39 page 53. 
 
You may choose to align large objects and arrays by the cache line size, which is typically 
64 bytes. This makes sure that the beginning of the object or array coincides with the 
beginning of a cache line. Some compilers will align large static arrays automatically but you 
may as well specify the alignment explicitly by writing: 
 
__declspec(align(64)) int BigArray[1024]; // Windows syntax 
 
or 
 
int BigArray[1024] __attribute__((aligned(64))); // Linux syntax 
 
See page 96 and 123 for discussion of aligning dynamically allocated memory. 
 
9.6 Dynamic memory allocation 
Objects and arrays can be allocated dynamically with new and delete, or malloc and 
free. This can be useful when the amount of memory required is not known at compile 
time. Four typical uses of dynamic memory allocation can be mentioned here: 
 


---

 
 
A large array can be allocated dynamically when the size of the array is not known at 
compile time. 
 
 
A variable number of objects can be allocated dynamically when the total number of 
objects is not known at compile time.  
 
 
Text strings and similar objects of variable size can be allocated dynamically. 
   
 
Arrays that are too large for the stack can be allocated dynamically. 
 
The advantages of dynamic memory allocation are: 
 
 
Gives a more clear program structure in some cases. 
 
 
Does not allocate more space than needed. This makes data caching more efficient 
than when a fixed-size array is made very big in order to cover the worst case 
situation of the maximum possible memory requirement. 
 
 
Useful when no reasonable upper limit to the required amount of memory space can 
be given in advance. 
 
The disadvantages of dynamic memory allocation are: 
 
 
The process of dynamic allocation and deallocation of memory takes much more 
time than other kinds of storage. See page 26. 
 
 
The heap space becomes fragmented when objects of different sizes are allocated 
and deallocated in random order. This makes data caching inefficient. 
 
 
An allocated array may need to be resized in the event that it becomes full. This may 
require that a new bigger memory block is allocated and the entire contents copied 
to the new block. Any pointers to data in the old block then become invalid. 
   
 
The heap manager will start garbage collection when the heap space has become 
too fragmented. This garbage collection may start at unpredictable times and cause 
delays in the program flow at inconvenient times when a user is waiting for 
response. 
 
 
It is the responsibility of the programmer to make sure that everything that has been 
allocated is also deallocated. Failure to do so will cause the heap to be filled up. This 
is a common programming error known as memory leaks. 
 
 
It is the responsibility of the programmer to make sure that no object is accessed 
after it has been deallocated. Failure to do so is also a common programming error. 
 
 
The allocated memory may not be optimally aligned. See page 123 for how to align 
dynamically allocated memory. 
   
 
It is difficult for the compiler to optimize code that uses pointers because it cannot 
rule out aliasing (see page 79). 
 
 
A matrix or multidimensional array is less efficient when the row length is not known 
at compile time because of the extra work needed for calculating row addresses at 
each access. The compiler may not be able to optimize this with induction variables. 
 
It is important to weigh the advantages over the disadvantages when deciding whether to 
use dynamic memory allocation. There is no reason to use dynamic memory allocation 


---

 
when the size of an array or the number of objects is known at compile time or a reasonable 
upper limit can be defined. 
 
The cost of dynamic memory allocation is negligible when the number of allocations is 
limited. Dynamic memory allocation can therefore be advantageous when a program has 
one or a few arrays of variable size. The alternative solution of making the arrays very big to 
cover the worst case situation is a waste of cache space. A situation where a program has 
several large arrays and where the size of each array is a multiple of the critical stride (see 
above, page 88) is likely to cause contentions in the data cache. 
 
If the number of elements in an array grows during program execution then it is preferable 
to allocate the final array size right from the beginning rather than allocating more space 
step by step. In most systems, you cannot increase the size of a memory block that has 
already been allocated. If the final size cannot be predicted or if the prediction turns out to 
be too small, then it is necessary to allocate a new bigger memory block and copy the 
contents of the old memory block into the beginning of the new bigger memory block. This is 
inefficient, of course, and causes the heap space to become fragmented. An alternative is to 
keep multiple memory blocks, either in the form of a linked list or with an index of memory 
blocks. A method with multiple memory blocks makes the access to individual array 
elements more complicated and time consuming. 
 
A collection of a variable number of objects is often implemented as a linked list. Each 
element in a linked list has its own memory block and a pointer to the next block. A linked 
list is less efficient than a linear array for the following reasons: 
 
 
Each object is allocated separately. The allocation, deallocation and garbage 
collection takes a considerable amount of time. 
 
 
The objects are not stored contiguously in the memory. This makes data caching 
less efficient. 
 
 
Extra memory space is used for the link pointers and for information stored by the 
heap manager for each allocated block. 
 
 
Walking through a linked list takes more time than looping through a linear array. No 
link pointer can be loaded until the previous link pointer has been loaded. This 
makes a critical dependency chain which prevents out-of-order execution. 
   
It is often more efficient to allocate one big block of memory for all the objects (memory 
pooling) than to allocate a small block for each object. 
 
A little-known alternative to using new and delete is to allocate variable-size arrays with 
alloca. This is a function that allocates memory on the stack rather than the heap. The 
space is automatically deallocated when returning from the function in which alloca was 
called. There is no need to deallocate the space explicitly when alloca is used. The 
advantages of alloca over new and delete or malloc and free are: 
 
 
There is very little overhead to the allocation process because the microprocessor 
has hardware support for the stack. 
 
 
The memory space never becomes fragmented thanks to the first-in-last-out nature 
of the stack. 
 
 
Deallocation has no cost because it goes automatically when the function returns. 
There is no need for garbage collection. 
 


---

 
 
The allocated memory is contiguous with other objects on the stack, which makes 
data caching very efficient. 
 
The following example shows how to make a variable-size array with alloca: 
 
// Example 9.3 
#include <malloc.h> 
 
void SomeFunction (int n) { 
   if (n > 0) { 
      // Make dynamic array of n floats: 
      float * DynamicArray = (float *)alloca(n * sizeof(float)); 
      // (Some compilers use the name _alloca) 
      for (int i = 0; i < n; i++) { 
         DynamicArray[i] = WhateverFunction(i); 
         // ... 
      } 
   } 
}  
 
Obviously, a function should never return any pointer or reference to anything it has 
allocated with alloca, because it is deallocated when the function returns. alloca may 
not be compatible with structured exception handling. See the manual for your compiler for 
restrictions on using alloca. 
 
9.7 Container classes 
Whenever dynamic memory allocation is used, it is recommended to wrap the allocated 
memory into a container class. The container class must have a destructor to make sure 
everything that is allocated is also de-allocated. This is the best way to prevent memory 
leaks and other common programming errors associated with dynamic memory allocation. 
 
Container classes can also be convenient for adding bounds-checking to an array and for 
more advanced data structures with First-In-First-Out or First-In-Last-Out access, sort and 
search facilities, binary trees, hash maps etc. 
 
It is common to make container classes in the form of templates where the type of objects 
they contain is provided as a template parameter. There is no performance cost to using 
templates. 
 
Ready made container class templates are available for many different purposes. The most 
commonly used set of containers is the Standard Template Library (STL) which comes with 
most modern C++ compilers. The advantage of using ready made containers is that you 
don't have to reinvent the wheel. The containers in the STL are universal, flexible, well 
tested, and very useful for many different purposes. 
 
However, the STL is designed for generality and flexibility, while execution speed, memory 
economy, cache efficiency and code size have got low priority. Especially the memory 
allocation is unnecessarily wasteful in the STL. Some STL templates, such as list, set 
and map are prone to even allocate more memory blocks than there are objects in the 
container. STL deque (doubly ended queue) allocates one memory block for every four 
objects. STL vector stores all the objects in the same memory block, but this memory 
block is re-allocated every time it is filled up, which happens quite often because the block 
size grows by only 50% or less each time. An experiment where 10 elements were inserted, 
one by one, into an STL vector turned up to cause seven memory allocations of sizes 1, 2, 
3, 4, 6, 9 and 13 objects, respectively (MS Visual Studio 2008 version). This wasteful 
behavior can be prevented by calling vector::reserve with a prediction or estimate of 


---

 
the final size needed before adding the first object to the vector. The other STL containers 
do not have such a feature for reserving memory in advance. 
 
The frequent allocation and de-allocation of memory with new and delete (or malloc and 
free) causes the memory to become fragmented and caching becomes inefficient. There is 
a large overhead cost to memory management and garbage collection, as mentioned 
above. 
 
The generality of the STL also costs in terms of code size. In fact, the STL has been 
criticized for code bloat and complexity (en.wikipedia.org/wiki/Standard_Template_Library). 
The objects stored in an STL container are allowed to have constructors and destructors. 
The copy constructors and destructors of each object are called every time an object is 
moved, which may happen quite often. This is necessary if the objects stored are containers 
themselves. But implementing a matrix in STL as a vector of vectors, as is often seen, is 
certainly a very inefficient solution. 
 
Many containers use linked lists. A linked list is a convenient way of making the container 
expandable, but it is very inefficient. Linear arrays are faster than linked lists in most cases.  
 
The so-called iterators that are used in STL for accessing container elements are 
cumbersome to use for many programmers and they are not necessary if you can use a 
linear list with a simple index. A good compiler can optimize away the extra overhead of the 
iterator in some cases, but not all. 
 
Fortunately, there are more efficient alternatives that can be used where execution speed, 
memory economy and small code size has higher priority than code generality. The most 
important remedy is memory pooling. It is more efficient to store many objects together in 
one big memory block than to store each object in its own allocated memory block. A large 
block containing many objects can be copied or moved with a single call to memcpy rather 
than moving each object separately if there are no copy constructors and destructors to call. 
 
I have implemented a collection of example container classes that use these methods to 
improve efficiency. These are available as an appendix to this manual at 
www.agner.org/optimize/cppexamples.zip containing container classes and templates for 
several different purposes. All these examples are optimized for execution speed and for 
minimizing memory fragmentation. Bounds checking is included for the sake of security, but 
may be removed after debugging if required for performance reasons. Use these example 
containers in cases where the performance of the STL is not satisfactory. 
 
The following considerations should be taken into account when choosing a container for a 
specific purpose: 
 
 
Contain one or multiple elements? If the container is to hold only one element then 
use a smart pointer (see page 38). 
   
 
Is the size known at compile time? If the number of elements is known at compile 
time or a not-too-big upper limit can be set then the optimal solution is a fixed size 
array or container without dynamic memory allocation. Dynamic memory allocation 
may be needed, however, if the array or container is too big for the stack. 
   
 
Is the size known before the first element is stored? If the total number of elements 
to store is known before the first element is stored (or if a reasonable estimate can 
be made) then it is preferred to use a container that allows you to reserve the 
amount of memory needed in advance rather than allocating piecewise or re-
allocating when a memory block turns out to be too small. 
   


---

 
 
Are objects numbered consecutively? If objects are identified by consecutive indices 
or by keys within a limited range then a simple array is the most efficient solution. 
   
 
Is a multidimensional structure needed? A matrix or multidimensional array should 
be stored in one contiguous memory block. Do not use one container for each row or 
column. The access is faster if the number of elements per row is a constant known 
at compile time. 
     
 
Are objects accessed in a FIFO manner? If objects are accessed on a First-In-First-
Out (FIFO) basis then use a queue. It is more efficient to implement a queue as a 
circular buffer than as a linked list. 
   
 
Are objects accessed in a FILO manner? If objects are accessed on a First-In-Last-
Out (FILO) basis then use a linear array with a top-of-stack index. 
 
 
Are objects identified by a key? If the key values are confined to a narrow range then 
a simple array can be used. If the number of objects is high then the most efficient 
solution may be a binary tree or a hash map.  
   
 
Do objects have a natural ordering? If you need to do searches of the kind: "what is 
the nearest element to x?" or "how many elements are there between x and y?" then 
you may use a sorted list or a binary tree. 
   
 
Is searching needed after all objects have been added? If search facilities are 
needed, but only after all objects have been stored in the container, then a linear 
array will be an efficient solution. Sort the array after all elements have been added 
and then use binary search for finding elements. A hash map may also be an 
efficient solution. 
   
 
Is searching needed before all objects have been added? If search facilities are 
needed, and new objects can be added at any time, then the solution is more 
complicated. If the total number of elements is small then a sorted list is the most 
efficient solution because of its simplicity. But a sorted list can be very inefficient if 
the list is large because the insertion of a new element in the list causes all 
subsequent elements in the sequence to be moved. A binary tree or a hash map is 
needed in this case. A binary tree may be used if elements have a natural order and 
there are search requests for elements in a specific interval. A hash map can be 
used if elements have no specific order but are identified by a unique key. 
   
 
Do objects have mixed types or sizes? It is possible to store objects of different 
types or strings of different lengths in the same memory pool. See 
www.agner.org/optimize/cppexamples.zip. If the number and types of elements is 
known at compile time then there is no need to use a container or memory pool. 
   
 
Alignment? Some applications require that data are aligned at round addresses. 
Especially the use of intrinsic vectors requires alignment to addresses divisible by 
16. Alignment of data structures to addresses divisible by the cache line size 
(typically 64) can improve performance in some cases. 
   
 
Multiple threads? Container classes are generally not thread safe if multiple threads 
can add, remove or modify objects simultaneously. In multithreaded applications it is 
much more efficient to have separate containers for each thread than to temporarily 
lock a container for exclusive access by each thread. 
   
 
Pointers to contained objects? It may not be safe to make a pointer to a contained 
object because the container may move the object in case memory re-allocation is 
needed. Objects inside containers should be identified by their index or key in the 


---

 
container rather than by pointers or references. It is OK, however, to pass a pointer 
or reference to such an object to a function that doesn't add or remove any objects if 
no other threads have access to the container. 
   
 
Can the container be recycled? There is a large cost to creating and deleting 
containers. If the program logic allows it, it may be more efficient to re-use a 
container than to delete it and create a new one. 
  
I have provided several examples of suitable containers class templates in 
www.agner.org/optimize/cppexamples.zip. These may be used as alternatives to the 
standard template library (STL) if the full generality and flexibility of the STL containers is 
not needed. You may write your own container classes or modify the ones that are available 
to fit specific needs. 
 
9.8 Strings 
Text strings typically have variable lengths that are not known at compile time. The storage 
of text strings in classes like string, wstring or CString uses new and delete to 
allocate a new memory block every time a string is created or modified. This can be quite 
inefficient if a program creates or modifies many strings.  
 
In most cases, the fastest way to handle strings is the old fashioned C style with character 
arrays. Strings can be manipulated with C functions such as strcpy, strcat, strlen, 
sprintf, etc. But beware that these functions have no check for overflow of the arrays. An 
array overflow can cause unpredictable errors elsewhere in the program that are very 
difficult to diagnose. It is the responsibility of the programmer to make sure the arrays are 
sufficiently large to handle the strings including the terminating zero and to make overflow 
checks where necessary. Fast versions of common string functions as well as efficient 
functions for string searching and parsing are provided in the asmlib library at 
www.agner.org/optimize/asmlib.zip. 
 
If you want to improve speed without jeopardizing safety, you may store all strings in a 
memory pool, as explained above. Examples are provided in an appendix to this manual at 
www.agner.org/optimize/cppexamples.zip. 
 
9.9 Access data sequentially 
A cache works most efficiently when the data are accessed sequentially. It works somewhat 
less efficiently when data are accessed backwards and much less efficiently when data are 
accessed in a random manner. This applies to reading as well as writing data. 
 
Multidimensional arrays should be accessed with the last index changing in the innermost 
loop. This reflects the order in which the elements are stored in memory. Example: 
 
// Example 9.4 
const int NUMROWS = 100, NUMCOLUMNS = 100; 
int matrix[NUMROWS][NUMCOLUMNS]; 
int row, column; 
for (row = 0; row < NUMROWS; row++) 
   for (column = 0; column < NUMCOLUMNS; column++)  
      matrix[row][column] = row + column; 
 
Do not swap the order of the two loops (except in Fortran where the storage order is 
opposite). 
 


---

 
9.10 Cache contentions in large data structures 
It is not always possible to access a multidimensional array sequentially. Some applications 
(e.g. in linear algebra) require other access patterns. This can cause severe delays if the 
distance between rows in a big matrix happen to be equal to the critical stride, as explained 
on page 89. This will happen if the size of a matrix line (in bytes) is a high power of 2. 
 
The following example illustrates this. My example is a function which transposes a 
quadratic matrix, i.e. each element matrix[r][c] is swapped with element 
matrix[c][r]. 
 
// Example 9.5a 
const int SIZE = 64;          // number of rows/columns in matrix 
 
void transpose(double a[SIZE][SIZE]) { // function to transpose matrix 
   // define a macro to swap two array elements: 
   #define swapd(x,y) {temp=x; x=y; y=temp;} 
 
   int r, c;  double temp; 
   for (r = 1; r < SIZE; r++) {        // loop through rows 
      for (c = 0; c < r; c++) {        // loop columns below diagonal 
         swapd(a[r][c], a[c][r]);      // swap elements 
      } 
   } 
} 
 
void test () { 
   __declspec(__align(64))       // align by cache line size 
   double matrix[SIZE][SIZE];    // define matrix 
   transpose(matrix);            // call transpose function 
} 
 
Transposing a matrix is the same as reflecting it at the diagonal. Each element 
matrix[r][c] below the diagonal is swapped with element matrix[c][r] at its mirror 
position above the diagonal. The c loop in example 9.5a goes from the leftmost column to 
the diagonal. The elements at the diagonal remain unchanged.  
 
The problem with this code is that if the elements matrix[r][c] below the diagonal are 
accessed row-wise, then the mirror elements matrix[c][r] above the diagonal are 
accessed column-wise. 
 
Assume now that we are running this code with a 6464 matrix on a Pentium 4 computer 
where the level-1 data cache is 8 kb = 8192 bytes, 4 ways, with a line size of 64. Each 
cache line can hold 8 double's of 8 bytes each. The critical stride is 8192 / 4 = 2048 bytes 
= 4 rows. 
 
Let's look at what happens inside the loop, for example when r = 28. We take the elements 
from row 28 below the diagonal and swap these elements with column 28 above the 
diagonal. The first eight elements in row 28 share the same cache line. But these eight 
elements will go into eight different cache lines in column 28 because the cache lines follow 
the rows, not the columns. Every fourth of these cache lines belong to the same set in the 
cache. When we reach element number 16 in column 28, the cache will evict the cache line 
that was used by element 0 in this column. Number 17 will evict number 1. Number 18 will 
evict number 2, etc. This means that all the cache lines we used above the diagonal have 
been lost at the time we are swapping column 29 with line 29. Each cache line has to be 
reloaded eight times because it is evicted before we need the next element. I have 
confirmed this by measuring the time it takes to transpose a matrix using example 9.5a on a 
Pentium 4 with different matrix sizes. The results of my experiment are given below. The 
time unit is clock cycles per array element. 
 


---

 
Matrix size 
Total kilobytes 
Time per element 
6363 
11.6 
6464 
16.4 
6565 
11.8 
127127 
12.2 
128128 
17.4 
129129 
14.4 
511511 
2040 
38.7 
512512 
2048 
230.7 
513513 
2056 
38.1 
Table 9.1. Time for transposition of different size matrices, 
clock cycles per element. 
 
The table shows that it takes 40% more time to transpose the matrix when the size of the 
matrix is a multiple of the level-1 cache size. This is because the critical stride is a multiple 
of the size of a matrix line. The delay is less than the time it takes to reload the level-1 
cache from the level-2 cache because the out-of-order execution mechanism can prefetch 
the data. 
 
The effect is much more dramatic when contentions occur in the level-2 cache. The level-2 
cache is 512 kb, 8 ways. The critical stride for the level-2 cache is 512 kb / 8 = 64 kb. This 
corresponds to 16 lines in a 512512 matrix. My experimental results in table 9.1 show that 
it takes six times as long time to transpose a matrix when contentions occur in the level-2 
cache as when contentions do not occur. The reason why this effect is so much stronger for 
level-2 cache contentions than for level-1 cache contentions is that the level-2 cache cannot 
prefetch more than one line at a time. 
 
A simple way of solving the problem is to make the rows in the matrix longer than needed in 
order to avoid that the critical stride is a multiple of the matrix line size. I tried to make the 
matrix 512520 and leave the last 8 columns unused. This removed the contentions and the 
time consumption was down to 36. 
 
There may be cases where it is not possible to add unused columns to a matrix. For 
example, a library of math functions should work efficiently on all sizes of matrices. An 
efficient solution in this case is to divide the matrix into smaller squares and handle one 
square at a time. This is called square blocking or tiling. This technique is illustrated in 
example 9.5b. 
 
// Example 9.5b 
void transpose(double a[SIZE][SIZE]) { 
   // Define macro to swap two elements: 
   #define swapd(x,y) {temp=x; x=y; y=temp;} 
   // Check if level-2 cache contentions will occur: 
   if (SIZE > 256 && SIZE % 128 == 0) { 
      // Cache contentions expected. Use square blocking: 
      int r1, r2, c1, c2; double temp; 
      // Define size of squares: 
      const int TILESIZE = 8;   // SIZE must be divisible by TILESIZE 
      // Loop r1 and c1 for all squares: 
      for (r1 = 0; r1 < SIZE; r1 += TILESIZE) { 
         for (c1 = 0; c1 < r1; c1 += TILESIZE) { 
            // Loop r2 and c2 for elements inside sqaure: 
            for (r2 = r1; r2 < r1+TILESIZE; r2++) { 
               for (c2 = c1; c2 < c1+TILESIZE; c2++) { 
                  swapd(a[r2][c2],a[c2][r2]); 
               } 
            } 


---

 
         } 
         // At the diagonal there is only half a square. 
         // This triangle is handled separately: 
         for (r2 = r1+1; r2 < r1+TILESIZE; r2++) { 
            for (c2 = r1; c2 < r2; c2++) { 
               swapd(a[r2][c2],a[c2][r2]); 
            } 
         } 
      } 
   } 
   else { 
      // No cache contentions. Use simple method. 
      // This is the code from example 9.5a: 
      int r, c;  double temp; 
      for (r = 1; r < SIZE; r++) {    // loop through rows 
         for (c = 0; c < r; c++) {    // loop columns below diagonal 
            swapd(a[r][c], a[c][r]);  // swap elements 
         } 
      } 
  } 
} 
 
This code took 50 clock cycles per element for a 512512 matrix in my experiments. 
 
Contentions in the level-2 cache are so expensive that it is very important to do something 
about them. You should therefore be aware of situations where the number of columns in a 
matrix is a high power of 2. Contentions in the level-1 cache are less expensive. Using 
complicated techniques like square blocking for the level-1 cache may not be worth the 
effort. 
 
Square blocking and similar methods are further described in the book "Performance 
Optimization of Numerically Intensive Codes", by S. Goedecker and A. Hoisie, SIAM 2001. 
 
9.11 Explicit cache control 
Microprocessors with the SSE and SSE2 instruction sets have certain instructions that allow 
you to manipulate the data cache. These instructions are accessible from compilers that 
have support for intrinsic functions (i.e. Microsoft, Intel and Gnu). Other compilers need 
assembly code to access these instructions.  
 
Function 
Assembly name 
Intrinsic function name 
Instruction 
set 
Prefetch 
PREFETCH 
_mm_prefetch 
SSE 
Store 4 bytes without cache 
MOVNTI 
_mm_stream_si32 
SSE2 
Store 8 bytes without cache 
MOVNTQ 
_mm_stream_pi 
SSE 
Store 16 bytes without cache 
MOVNTPS 
_mm_stream_ps 
SSE 
Store 16 bytes without cache 
MOVNTPD 
_mm_stream_pd 
SSE2 
Store 16 bytes without cache 
MOVNTDQ 
_mm_stream_si128 
SSE2 
Table 9.2. Cache control instructions. 
 
There are other cache control instructions than the ones mentioned in table 9.2, such as 
flush and fence instructions, but these are hardly relevant to optimization. 
Prefetching data 
The prefetch instruction can be used for fetching a cache line that we expect to use later in 
the program flow. However, this did not improve the execution speed in any of the examples 
I have tested. The reason is that modern processors prefetch data automatically thanks to 


---

 
out-of-order execution and advanced prediction mechanisms. Modern microprocessors are 
able to automatically prefetch data for regular access patterns containing multiple streams 
with different strides. Therefore, you don't have to prefetch data explicitly if data access can 
be arranged in regular patterns with fixed strides. 
Uncached memory store 
An uncached write is more expensive than an uncached read because the write causes an 
entire cache line to be read and written back. 
 
The so-called nontemporal write instructions (MOVNT) are designed to solve this problem. 
These instructions write directly to memory without loading a cache line. This is 
advantageous in cases where we are writing to uncached memory and we do not expect to 
read from the same or a nearby address again before the cache line would be evicted. Don't 
mix nontemporal writes with normal writes or reads to the same memory area. 
 
The nontemporal write instructions are not suitable for example 9.5 because we are reading 
and writing from the same address so a cache line will be loaded anyway. If we modify 
example 9.5 so that it writes only, then the effect of nontemporal write instructions becomes 
noticeable. The following example transposes a matrix and stores the result in a different 
array. 
 
// Example 9.6a 
const int SIZE = 512; // number of rows and columns in matrix 
 
// function to transpose and copy matrix 
void TransposeCopy(double a[SIZE][SIZE], double b[SIZE][SIZE]) { 
   int r, c;  
   for (r = 0; r < SIZE; r++) { 
      for (c = 0; c < SIZE; c++) { 
         a[c][r] = b[r][c]; 
      } 
   } 
} 
 
This function writes to matrix a in a column-wise manner where the critical stride causes all 
writes to load a new cache line in both the level-1 and the level-2 cache. Using the 
nontemporal write instruction prevents the level-2 cache from loading any cache lines for 
matrix a: 
 
// Example 9.6b. 
#include "xmmintrin.h"  // header for intrinsic functions 
 
// This function stores a double without loading a cache line: 
static inline void StoreNTD(double * dest, double const & source) { 
   _mm_stream_pi((__m64*)dest, *(__m64*)&source);  // MOVNTQ 
   _mm_empty();                                    // EMMS 
} 
 
const int SIZE = 512; // number of rows and columns in matrix 
// function to transpose and copy matrix 
void TransposeCopy(double a[SIZE][SIZE], double b[SIZE][SIZE]) { 
   int r, c;  
   for (r = 0; r < SIZE; r++) { 
      for (c = 0; c < SIZE; c++) { 
         StoreNTD(&a[c][r], b[r][c]); 
      } 
   } 
} 
 
The execution times per matrix cell for different matrix sizes were measured on a Pentium 4 
computer. The measured results were as follows: 


---

