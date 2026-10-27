# Summary


<!-- PAGE 744 -->
Fuller (1895–1983). The Montr´eal Biosph`ere is an example of a geodesic dome designed by Buckminster Fuller. $A =$ full(bucky); $D =$ diag(sum(A)); $L = D$ - $A; [v, e] =$ eig(L); gplot(A, $v(:, [2 3]))$ hold on; gplot(A,v(:, $[2 3])$, ’o’) Figure 21.5 shows a graph drawing of the Buckyball. This picture seems a bit squashed for two reasons. First, it is really a 3-dimensional graph; second, $\lambda_{2}  =$ 0.2434 is a triple eigenvalue. (Actually, the Laplacian of $L$ has many multiple eigenvalues.) What we should
$$\mathbb{R}^{3}$$
really do is to plot this graph in using three orthonormal eigenvectors associated with $\lambda_{2}$ .
$$0.25$$
$$0.2$$
$$0.15$$
$$0.1$$
$$0.05$$
$$0$$
$$-0.05$$
$$-0.1$$
$$-0.15$$
$$-0.2$$
$$-0.25\overline{-0.25}\overline{-0.2}\overline{-0.15}\overline{-0.1}\overline{-0.05}\overline{0}\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}$$
$$Figure 21.5: Drawing of the graph of the Buckyball.$$
A 3D picture of the graph of the Buckyball is produced by the following Matlab program, and its image is shown in Figure 21.6. It looks better! $[x, y] =$ gplot(A, $v(:, [2 3])); [x, z] =$ gplot(A, $v(:, [2 4]))$; plot3(x,y,z)

## 21.3 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Graph drawing.

<!-- PAGE 745 -->
$$0.25$$
$$0.2$$
$$0.15$$
$$0.1$$
$$0.05$$
$$0$$
$$-0.05$$
$$-0.1$$
$$-0.15$$
$$-0.2$$
$$-0.25$$
$$0.4$$
$$0.2$$
$$0$$
$$0.20.3$$
$$-0.200.1$$
$$-0.2-0.1$$
$$-0.4-0.4-0.3$$
$$Figure 21.6: Drawing of the graph of the Buckyball in \mathbb{R}^{3}.$$
$\bullet$  Matrix of a graph drawing. $\bullet$  Balanced graph drawing. $\bullet$  Energy $\mathcal{E}(R)$ of a graph drawing. $\bullet$  Orthogonal graph drawing. $\bullet$  Delaunay triangulation. $\bullet$  Buckyball.

<!-- PAGE 746 -->
