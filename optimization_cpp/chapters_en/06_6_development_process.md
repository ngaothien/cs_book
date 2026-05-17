# 6 Development process

 
dramatically for very large data bases, but there is no reason to use it for lists that are so 
small that a binary search, or even a linear search, is fast enough. A hash table increases 
the size of the program as well as the size of data files. This can actually reduce speed if 
the bottleneck is file access or cache access rather than CPU time. Another disadvantage of 
complicated algorithms is that it makes program development more expensive and more 
error prone. 
 
A discussion of different algorithms for different purposes is beyond the scope of this 
manual. You have to consult the general literature on algorithms and data structures for 
standard tasks such as sorting and searching, or the specific literature for more complicated 
mathematical tasks. 
 
Before you start to code, you may consider whether others have done the job before you. 
Optimized function libraries for many standard tasks are available from a number of 
sources. For example, the Boost collection contains well-tested libraries for many common 
purposes (www.boost.org). The "Intel Math Kernel Library" contains many functions for 
common mathematical calculations including linear algebra and statistics, and the "Intel 
Performance Primitives" library contains many functions for audio and video processing, 
signal processing, data compression and cryptography (www.intel.com). If you are using an 
Intel function library then make sure it works well on non-Intel processors, as explained on 
page 133. 
 
It is often easier said than done to choose the optimal algorithm before you start to program. 
Many programmers have discovered that there are smarter ways of doing things only after 
they have put the whole software project together and tested it. The insight you gain by 
testing and analyzing program performance and studying the bottlenecks can lead to a 
better understanding of the whole structure of the problem. This new insight can lead to a 
complete redesign of the program, for example when you discover that there are smarter 
ways of organizing the data. 
 
A complete redesign of a program that already works is of course a considerable job, but it 
may be quite a good investment. A redesign can not only improve the performance, it is also 
likely to lead to a more well-structured program that is easier to maintain. The time you 
spend on redesigning a program may in fact be less than the time you would have spent 
fighting with the problems of the original, poorly designed program. 
 
 
6 Development process 
There is a considerable debate about which software development process and software 
engineering principles to use. I am not going to recommend any specific model. Instead, I 
will make a few comments about how the development process can influence the 
performance of the final product. 
 
It is good to do a thorough analysis of the data structure, data flow and algorithms in the 
planning phase in order to predict which resources are most critical. However, there may be 
so many unknown factors in the early planning stage that a detailed overview of the problem 
cannot easily be obtained. In the latter case, you may view the software development work 
as a learning process where the main feedback comes from testing. Here, you should be 
prepared for several iterations of redesign. 
 
Some software development models have a strict formalism that requires several layers of 
abstraction in the logical architecture of the software. You should be aware that there are 
inherent performance costs to such a formalism. The splitting of software into an excessive 
number of separate layers of abstraction is a common cause of reduced performance. 
 


---

