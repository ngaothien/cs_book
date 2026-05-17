# 4 Performance and usability

 
one or two floating point multiplication units. This means that it is possible to do an integer 
addition, a floating point addition, and a floating point multiplication at the same time. 
 
A code that does floating point calculations should therefore preferably have a balanced mix 
of additions and multiplications. Subtractions use the same unit as additions. Divisions take 
longer time. It is possible to do integer operations in-between the floating point operations 
without reducing the performance because the integer operations use different execution 
units. For example, a loop that does floating point calculations will typically use integer 
operations for incrementing a loop counter, comparing the loop counter with its limit, etc. In 
most cases, you can assume that these integer operations do not add to the total 
computation time. 
 
 
4 Performance and usability 
A better performing software product is one that saves time for the user. Time is a precious 
resource for many computer users and much time is wasted on software that is slow, 
difficult to use, incompatible or error prone. All these problems are usability issues, and I 
believe that software performance should be seen in the broader perspective of usability.  
 
This is not a manual on usability, but I think that it is necessary here to draw the attention of 
software programmers to some of the most common obstacles to efficient use of software. 
For more on this topic, see my free E-book Usability for Nerds at Wikibooks. 
 
The following list points out some typical sources of frustration and waste of time for 
software users as well as important usability problems that software developers should be 
aware of. 
 
 
Big runtime frameworks. The .NET framework and the Java virtual machine are 
frameworks that typically take much more resources than the programs they are 
running. Such frameworks are frequent sources of resource problems and compatibility 
problems and they waste a lot of time both during installation of the framework itself, 
during installation of the program that runs under the framework, during start of the 
program, and while the program is running. The main reason why such runtime 
frameworks are used at all is for the sake of cross-platform portability. Unfortunately, the 
cross-platform compatibility is not always as good as expected. I believe that the 
portability could be achieved more efficiently by better standardization of programming 
languages, operating systems, and API's. 
 
 
Memory swapping. Software developers typically have more powerful computers with 
more RAM than end users have. The developers may therefore fail to see the excessive 
memory swapping and other resource problems that cause the resource-hungry 
applications to perform poorly for the end user. 
 
 
Installation problems. The procedures for installation and uninstallation of programs 
should be standardized and done by the operating system rather than by individual 
installation tools. 
 
 
Automatic updates. Automatic updating of software can cause problems if the network is 
unstable or if the new version causes problem that were not present in the old version. 
Updating mechanisms often disturb the users with nagging pop-up messages saying 
please install this important new update or even telling the user to restart the computer 
while he or she is busy concentrating on important work. The updating mechanism 
should never interrupt the user but only show a discrete icon signaling the availability of 
an update, or update automatically when the computer is restarted anyway. Software 
distributors are often abusing the update mechanism to advertise new versions of their 


---

