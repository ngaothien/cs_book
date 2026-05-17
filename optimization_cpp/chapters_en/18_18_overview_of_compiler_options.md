# 18  Overview of compiler options

 
18 Overview of compiler options 
 
Table 18.1. Command line options relevant to optimization 
 
 
MS compiler 
Windows 
Gnu compiler 
Linux 
Intel compiler 
Windows 
Intel compiler 
Linux 
Optimize for speed 
/O2 or /Ox 
-O3 or 
-Ofast 
/O3 
-O3 
Interprocedural 
optimization 
/Og 
 
 
 
Whole program 
optimization 
/GL 
--combine  
-fwhole-
program 
/Qipo 
-ipo 
No exception 
handling 
/EHs- 
 
 
 
No stack frame 
/Oy 
-fomit-
frame-
pointer 
 
-fomit-
frame-
pointer 
No runtime type 
identification (RTTI) 
/GR– 
-fno-rtti 
/GR- 
-fno-rtti 
Assume no pointer 
aliasing 
/Oa 
 
 
-fno-alias 
Non-strict floating 
point 
 
-ffast-math 
/fp:fast 
/fp:fast=2 
-fp-model 
fast, -fp-
model fast=2 
Simple member 
pointers 
/vms 
 
 
 
Fastcall functions 
/Gr 
 
 
 
Function level linking 
(remove unreferen-
ced functions) 
/Gy 
-ffunction-
sections 
/Gy 
-ffunction-
sections 
SSE instruction set 
(128 bit float vectors) 
/arch:SSE 
-msse 
/arch:SSE 
-msse 
SSE2 instruction set 
(128 vectors of inte-
ger or double) 
/arch:SSE2 
-msse2 
/arch:SSE2 
-msse2 
SSE3 instruction set 
 
-msse3 
/arch:SSE3 
-msse3 
Suppl. SSE3 instr. set  
-mssse3 
/arch:SSSE2 
-mssse3 
SSE4.1 instr. set 
 
-msse4.1 
/arch:SSE4.1 -msse4.1 
AVX instr. set 
/arch:AVX 
-mAVX 
/arch:AVX 
-mAVX 
Automatic CPU 
dispatch 
 
 
/QaxSSE3, etc. 
(Intel CPU only) 
-axSSE3, etc. 
(Intel CPU only) 
Automatic 
vectorization 
 
-O3 or 
better: 
-Ofast 
-mveclibabi 
(requires no specific option) 
Automatic paralleli-
zation by multiple 
threads 
 
 
/Qparallel 
-parallel 
Parallelization by 
OpenMP directives 
/openmp 
-fopenmp 
/Qopenmp 
-openmp 
32 bit code 
 
-m32 
 
 
64 bit code 
 
-m64 
 
 
Static linking 
(multithreaded) 
/MT 
-static 
/MT 
-static 


---

 
Generate assembly 
listing 
/FA 
-S -
masm=intel 
/FA 
-S 
Generate map file 
/Fm 
 
 
 
Generate 
optimization report 
 
 
/Qopt-report -opt-report 
 
 
Table 18.2. Compiler directives and keywords relevant to optimization 
 
 
MS compiler 
Windows 
Gnu compiler 
Linux 
Intel compiler 
Windows 
Intel compiler 
Linux 
Align by 16 
__declspec( 
align(16)) 
__attribute(( 
aligned(16))) 
__declspec( 
align(16)) 
__attribute(( 
aligned(16))) 
Assume 
pointer is 
aligned 
 
 
#pragma vector 
aligned 
#pragma vector 
aligned 
Assume 
pointer not 
aliased 
#pragma 
optimize("a", 
on) 
__restrict 
__restrict 
__declspec( 
noalias) 
__restrict 
#pragma ivdep 
__restrict 
#pragma ivdep 
Assume 
function is 
pure 
 
__attribute(( 
const)) 
 
__attribute(( 
const)) 
Assume 
function 
does not 
throw 
exceptions 
throw() 
throw() 
throw() 
throw() 
Assume 
function 
called only 
from same 
module 
static 
static 
static 
static 
Assume 
member 
function 
called only 
from same 
module 
 
__attribute__ 
((visibility 
("internal"))) 
 
__attribute__ 
((visibility 
("internal"))) 
Vectorize 
 
 
#pragma vector 
always 
#pragma vector 
always 
Optimize 
function 
#pragma 
optimize(...) 
 
 
 
Fastcall 
function 
__fastcall 
__attribute(( 
fastcall)) 
__fastcall 
 
Noncached 
write 
 
 
#pragma vector 
nontemporal 
#pragma vector 
nontemporal 
 
 
Table 18.3. Predefined macros 
 
 
MS compiler 
Windows 
Gnu compiler 
Linux 
Intel compiler 
Windows 
Intel compiler 
Linux 
Compiler 
identification 
_MSC_VER and not 
__INTEL_COMPILER 
__GNUC__ and not 
__INTEL_COMPILER 
__INTEL_COMPILER 
__INTEL_COMPILER 
16 bit 
platform 
not _WIN32 
n.a. 
n.a. 
n.a. 


---

 
32 bit 
platform 
not _WIN64 
 
not _WIN64 
 
64 bit 
platform 
_WIN64 
_LP64 
_WIN64 
_LP64 
Windows 
platform 
_WIN32 
 
_WIN32 
 
Linux 
platform 
n.a. 
__unix__ 
__linux__ 
 
__unix__ 
__linux__ 
x86 platform _M_IX86 
 
_M_IX86 
 
x86-64 
platform 
_M_IX86 and 
_WIN64 
 
_M_X64 
_M_X64 
 


---

