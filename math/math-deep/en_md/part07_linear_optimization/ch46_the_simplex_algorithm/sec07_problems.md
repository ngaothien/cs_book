# Problems


<!-- PAGE 1635 -->
Understanding the complexity of linear programing, in particular of the simplex algorithm, is still ongoing. The interested reader is referred to Matousek and Gardner $[127]$ (Chapter $5$, Section 5.9) for some pointers. In the next section we consider important theoretical criteria for determining whether a set of constraints Ax $\le b$ and $x \ge 0$ has a solution or not.

## 46.6 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Degenerate and nondegenerate basic feasible solution. $\bullet$  Pivoting step. $\bullet$  Pivot rule. $\bullet$  Cycling. $\bullet$  Bland’s rule, Dantzig’s rule, steepest edge rule, random edge rule, largest increase rule, lexicographic rule. $\bullet$  Phase I and Phase II of the simplex algorithm. $\bullet$  eta matrix, eta factorization. $\bullet$  Revised simplex method. $\bullet$  Reduced cost. $\bullet$  Full tableaux. $\bullet$  The Hirsch conjecture.

## 46.7 Problems

Problem 46.1. In Section 46.2 prove that if Case $(A)$ arises, then the basic feasible solution $u$ is an optimal solution. Prove that if Case (B1) arises, then the linear program is unbounded. Prove that if Case (B3) arises, then $(u^{+}, K^{+})$ is a basic feasible solution.
Problem 46.2. In Section 46.2 prove that the following equivalences hold:
$$Case (A) \Leftarrow \Rightarrow B = \emptyset ,Case (B) \Leftarrow \Rightarrow B \neq  \emptyset$$
$$Case (B1) \Leftarrow \Rightarrow B_{1} \neq  \emptyset$$
$$Case (B2) \Leftarrow \Rightarrow B_{2} \neq  \emptyset$$
$$Case (B3) \Leftarrow \Rightarrow B_{3} \neq  \emptyset .$$

<!-- PAGE 1636 -->
Furthermore, prove that Cases $(A)$ and $(B)$, Cases (B1) and (B3), and Cases (B2) and (B3) are mutually exclusive, while Cases (B1) and (B2) are not.
Problem 46.3. Consider the linear program (due to E.M.L. Beale):
$$maximize(3/4)x_{1} -150x_{2} + (1/50)x_{3} -6x_{4}$$
$$subject to$$
$$(1/4)x_{1} -60x_{2} -(1/25)x_{3} + 9x_{4} \le 0$$
$$(1/4)x_{1} -90x_{2} -(1/50)x_{3} + 3x_{4} \le 0$$
$$x_{3} \le 1$$
$$x_{1} \ge 0, x_{2} \ge 0, x_{3} \ge 0, x_{4} \ge 0.$$
$(1)$ Convert the above program to standard form.
$(2)$ Show that if we apply the simplex algorithm with the pivot rule which selects the column entering the basis as the column of smallest index, then the method cycles.
Problem 46.4. Read carefully the proof given by Chvatal that the lexicographic pivot rule and Bland’s pivot rule prevent cycling; see Chvatal $[40]$ (Chapter $3$, pages 34-38).
Problem 46.5. Solve the following linear program (from Chvatal $[40]$, Chapter $3$, page $44)$ using the two-phase simplex algorithm:
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} + x_{2} \le 4$$
$$x_{1} \ge 0, x_{2} \ge 0.$$
Problem 46.6. Solve the following linear program (from Chvatal $[40]$, Chapter $3$, page $44)$ using the two-phase simplex algorithm:
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} + x_{2} \le 2$$
$$x_{1} \ge 0, x_{2} \ge 0.$$

<!-- PAGE 1637 -->
Problem 46.7. Solve the following linear program (from Chvatal $[40]$, Chapter $3$, page $44)$ using the two-phase simplex algorithm:
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} -x_{2} \le 2$$
$$x_{1} \ge 0, x_{2} \ge 0.$$
Problem 46.8. Show that the following linear program (from Chvatal $[40]$, Chapter $3$, page $43)$ is unbounded.
$$maximizex_{1} + 3x_{2} -x_{3}$$
$$subject to$$
$$2x_{1} + 2x_{2} -x_{3} \le 10$$
$$3x_{1} -2x_{2} + x_{3} \le 10$$
$$x_{1} -3x_{2} + x_{3} \le 10$$
$$x_{1} \ge 0, x_{2} \ge 0, x_{3} \ge 0.$$
Hint. Try $x_{1} = 0, x_{3} = t$, and a suitable value for $x_{2}$.

<!-- PAGE 1638 -->
