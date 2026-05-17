# 1 Introduction

 
13.2 Model-specific dispatching .................................................................................... 127 
13.3 Difficult cases ........................................................................................................ 128 
13.4 Test and maintenance .......................................................................................... 129 
13.5 Implementation ..................................................................................................... 129 
13.6 CPU dispatching in Gnu compiler ......................................................................... 131 
13.7 CPU dispatching in Intel compiler ......................................................................... 133 
14 Specific optimization topics ......................................................................................... 135 
14.1 Use lookup tables ................................................................................................. 135 
14.2 Bounds checking .................................................................................................. 137 
14.3 Use bitwise operators for checking multiple values at once ................................... 138 
14.4 Integer multiplication ............................................................................................. 139 
14.5 Integer division ...................................................................................................... 140 
14.6 Floating point division ........................................................................................... 142 
14.7 Don't mix float and double ..................................................................................... 143 
14.8 Conversions between floating point numbers and integers ................................... 144 
14.9 Using integer operations for manipulating floating point variables ......................... 145 
14.10 Mathematical functions ....................................................................................... 149 
14.11 Static versus dynamic libraries ............................................................................ 149 
14.12 Position-independent code .................................................................................. 151 
14.13 System programming .......................................................................................... 153 
15 Metaprogramming ....................................................................................................... 154 
16 Testing speed .............................................................................................................. 157 
16.1 Using performance monitor counters .................................................................... 159 
16.2 The pitfalls of unit-testing ...................................................................................... 159 
16.3 Worst-case testing ................................................................................................ 160 
17 Optimization in embedded systems ............................................................................. 162 
18 Overview of compiler options....................................................................................... 164 
19 Literature ..................................................................................................................... 167 
20 Copyright notice .......................................................................................................... 168 
 
1 Introduction 
This manual is for advanced programmers and software developers who want to make their 
software faster. It is assumed that the reader has a good knowledge of the C++ 
programming language and a basic understanding of how compilers work. The C++ 
language is chosen as the basis for this manual for reasons explained on page 8 below. 
 
This manual is based mainly on my study of how compilers and microprocessors work. The 
recommendations are based on the x86 family of microprocessors from Intel, AMD and VIA 
including the 64-bit versions. The x86 processors are used in the most common platforms 
with Windows, Linux, BSD and Mac OS X operating systems, though these operating 
systems can also be used with other microprocessors. Many of the advices may apply to 
other platforms and other compiled programming languages as well. 
 
This is the first in a series of five manuals: 
 
1. Optimizing software in C++: An optimization guide for Windows, Linux and Mac 
platforms. 
 
2. Optimizing subroutines in assembly language: An optimization guide for x86 
platforms. 
 
3. The microarchitecture of Intel, AMD and VIA CPUs: An optimization guide for 
assembly programmers and compiler makers. 
 


---

 
4. Instruction tables: Lists of instruction latencies, throughputs and micro-operation 
breakdowns for Intel, AMD and VIA CPUs. 
 
5. Calling conventions for different C++ compilers and operating systems. 
 
The latest versions of these manuals are always available from www.agner.org/optimize. 
Copyright conditions are listed on page 168 below. 
 
Those who are satisfied with making software in a high-level language need only read this 
first manual. The subsequent manuals are for those who want to go deeper into the 
technical details of instruction timing, assembly language programming, compiler 
technology, and microprocessor microarchitecture. A higher level of optimization can 
sometimes be obtained by the use of assembly language for CPU-intensive code, as 
described in the subsequent manuals. 
 
Please note that my optimization manuals are used by thousands of people. I simply don't 
have the time to answer questions from everybody. So please don't send your programming 
questions to me. You will not get any answer. Beginners are advised to seek information 
elsewhere and get a good deal of programming experience before trying the techniques in 
the present manual. There are various discussion forums on the Internet where you can get 
answers to your programming questions if you cannot find the answers in the relevant 
books and manuals. 
 
I want to thank the many people who have sent me corrections and suggestions for my 
optimization manuals. I am always happy to receive new relevant information. 
 
1.1 The costs of optimizing 
University courses in programming nowadays stress the importance of structured and 
object-oriented programming, modularity, reusability and systematization of the software 
development process. These requirements are often conflicting with the requirements of 
optimizing the software for speed or size. 
 
Today, it is not uncommon for software teachers to recommend that no function or method 
should be longer than a few lines. A few decades ago, the recommendation was the 
opposite: Don't put something in a separate subroutine if it is only called once. The reasons 
for this shift in software writing style are that software projects have become bigger and 
more complex, that there is more focus on the costs of software development, and that 
computers have become more powerful. 
 
The high priority of structured software development and the low priority of program 
efficiency is reflected, first and foremost, in the choice of programming language and 
interface frameworks. This is often a disadvantage for the end user who has to invest in 
ever more powerful computers to keep up with the ever bigger software packages and who 
is still frustrated by unacceptably long response times, even for simple tasks. 
 
Sometimes it is necessary to compromise on the advanced principles of software develop-
ment in order to make software packages faster and smaller. This manual discusses how to 
make a sensible balance between these considerations. It is discussed how to identify and 
isolate the most critical part of a program and concentrate the optimization effort on that 
particular part. It is discussed how to overcome the dangers of a relatively primitive 
programming style that doesn't automatically check for array bounds violations, invalid 
pointers, etc. And it is discussed which of the advanced programming constructs are costly 
and which are cheap, in relation to execution time. 
 
 


---

