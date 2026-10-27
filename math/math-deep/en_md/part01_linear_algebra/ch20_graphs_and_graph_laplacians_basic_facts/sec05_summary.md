# Summary


<!-- PAGE 733 -->
$$Figure 20.7: A weighted graph and its partition into two clusters.$$
A way to get around this problem is to normalize the cuts by dividing by some measure of each subset $A_{i}$. A solution using the volume $vol(A_{i})$ of $A_{i}$ (for $K = 2)$ was proposed and investigated in a seminal paper of Shi and Malik $[166]$. Subsequently, Yu (in her dissertation $[197])$ and Yu and Shi $[199]$ extended the method to $K > 2$ clusters. The idea is to minimize the cost function
$$Ncut(A_{1}, \dots  , A_{K}) = \sum_{i=1}^{K}  \frac{links(A_{i}\overline{, A}_{i})}{vol(A_{i})} = \sum_{i=1}^{K}  \frac{cut(A_{i})}{vol(A_{i})} .$$
The next step is to express our optimization problem in matrix form, and this can be done in terms of Rayleigh ratios involving the graph Laplacian in the numerators. This theory is very beautiful, but we do not have the space to present it here. The interested reader is referred to Gallier $[75]$.

## 20.5 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Directed graphs, undirected graphs. $\bullet$  Incidence matrices, adjacency matrices. $\bullet$  Weighted graphs. $\bullet$  Degree matrix. $\bullet$  Graph Laplacian (unnormalized).
