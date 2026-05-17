# 11 Out of order execution

 
 
11 Out of order execution 
All modern x86 CPUs can execute instructions out of order or do more than one thing at the 
same time, except for some small low-power CPUs (Intel Atom). The following example 
shows how to take advantage of this capability: 
 
// Example 11.1a 
float a, b, c, d, y; 
y = a + b + c + d; 
 
This expression is calculated as ((a+b)+c)+d. This is a dependency chain where each 
addition has to wait for the result of the preceding one. You can improve this by writing: 
 
// Example 11.1b 
float a, b, c, d, y; 
y = (a + b) + (c + d); 
 
Now the two parentheses can be calculated independently. The CPU will start to calculate 
(c+d) before it has finished the calculation of (a+b). This can save several clock cycles. 
You cannot assume that an optimizing compiler will change the code in example 11.1a to 
11.1b automatically, although it appears to be an obvious thing to do. The reason why 
compilers do not make this kind of optimizations on floating point expressions is that it may 
cause a loss of precision, as explained on page 73. You have to set the parentheses 
manually. 
 
The effect of dependency chains is stronger when they are long. This is often the case in 
loops. Consider the following example, which calculates the sum of 100 numbers: 
 
// Example 11.2a 
const int size = 100; 
float list[size], sum = 0;  int i; 
for (i = 0; i < size; i++) sum += list[i]; 
 
This has a long dependency chain. If a floating point addition takes 5 clock cycles, then this 
loop will take approximately 500 clock cycles. You can improve the performance 
dramatically by unrolling the loop and splitting the dependency chain in two: 
 
// Example 11.2b 
const int size = 100; 
float list[size], sum1 = 0, sum2 = 0;  int i; 
for (i = 0; i < size; i += 2) { 
   sum1 += list[i]; 
   sum2 += list[i+1];} 
sum1 += sum2; 
 
If the microprocessor is doing an addition to sum1 from time T to T+5, then it can do another 
addition to sum2 from time T+1 to T+6, and the whole loop will take only 256 clock cycles. 
 
Calculations in a loop where each iteration needs the result of the preceding one is called a 
loop-carried dependency chain. Such dependency chains can be very long and very time-
consuming. There is a lot to gain if such dependency chains can be broken up. The two 
summation variables sum1 and sum2 are called accumulators. Current CPUs have only one 
floating point addition unit, but this unit is pipelined, as explained above, so that it can start a 
new addition before the preceding addition is finished. 
 
The optimal number of accumulators for floating point addition and multiplication may be 
three or four, depending on the CPU.  
 


---

 
Unrolling a loop becomes a little more complicated if the number of iterations is not divisible 
by the unroll factor. For example, if the number of elements in list in example 11.2b was 
an odd number then we would have to add the last element outside the loop or add an extra 
dummy element to list and make this extra element zero. 
 
It is not necessary to unroll a loop and use multiple accumulators if there is no loop-carried 
dependency chain. A microprocessor with out-of-order capabilities can overlap the iterations 
and start the calculation of one iteration before the preceding iteration is finished. Example: 
 
// Example 11.3 
const int size = 100;  int i; 
float a[size], b[size], c[size]; 
float register temp; 
for (i = 0; i < size; i++) { 
   temp = a[i] + b[i]; 
   c[i] = temp * temp; 
} 
 
Microprocessors with out-of-order capabilities are very smart. They can detect that the value 
of register temp in one iteration of the loop in example 11.3 is independent of the value in 
the previous iteration. This allows it to begin calculating a new value of temp before it is 
finished using the previous value. It does this by assigning a new physical register to temp 
even though the logical register that appears in the machine code is the same. This is called 
register renaming. The CPU can hold many renamed instances of the same logical register. 
 
This advantage comes automatically. There is no reason to unroll the loop and have a 
temp1 and temp2. Modern CPUs are capable of register renaming and doing multiple 
calculations in parallel if certain conditions are satisfied. The conditions that make it possible 
for the CPU to overlap the calculations of loop iterations are: 
 
 
No loop-carried dependency chain. Nothing in the calculation of one iteration should 
depend on the result of the previous iteration (except for the loop counter, which is 
calculated fast if it is an integer). 
 
 
All intermediate results should be saved in registers, not in memory. The renaming 
mechanism works only on registers, not on variables in memory or cache. Most 
compilers will make temp a register variable in example 11.3 even without the 
register keyword. The CodeGear compiler cannot make floating point register 
variables, but will save temp in memory. This prevents the CPU from overlapping 
calculations. 
   
 
The loop branch should be predicted. This is no problem if the repeat count is large 
or constant. If the loop count is small and changing then the CPU may occasionally 
predict that the loop exits, when in fact it does not, and therefore fail to start the next 
calculation. However, the out-of-order mechanism allows the CPU to increment the 
loop counter ahead of time so that it may detect the misprediction before it is too 
late. You should therefore not be too worried about this condition. 
 
In general, the out-of-order execution mechanism works automatically. However, there are a 
couple of things that the programmer can do to take maximum advantage of out-of-order 
execution. The most important thing is to avoid long dependency chains. Another thing that 
you can do is to mix different kinds of operations in order to divide the work evenly between 
the different execution units in the CPU. It can be advantageous to mix integer and floating 
point calculations as long as you don't need conversions between integers and floating point 
numbers. It can also be advantageous to mix floating point addition with floating point 
multiplication, to mix simple integer with vector integer operations, and to mix mathematical 
calculations with memory access. 
 


---

