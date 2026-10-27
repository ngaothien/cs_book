# Hard Margin (SVMh2)


<!-- PAGE 2169 -->
Appendix $B$ Matlab Programs

## B.1 Hard Margin (SVM )

$$h2$$
The following Matlab programs implement the method described in Section 52.7. The first program is the heart of the method; it implements ADMM for quadratic programming. function [x,u,nr,ns,k] $=$ qsolve1(P, $q, A, b$, rho, tolr, tols, iternum) % Solve a quadratic programming problem % min $(1/2) x^T P x + x^T q + r$ % subject to Ax $= b, x >= 0$ using ADMM % $P n x n, q, r$, in $R^n, A m x n, b$ in $R^m$ % $A$ of rank $m m =$ size(A,1); fprintf(’m $=$ %d ’,m) $n =$ size(P,1); fprintf(’ $n =$ %d $\n’,n) u =$ ones(n,1); u(1,1) $= 0$; % to initialize $u z =$ ones(n,1); % to initialize $z$ % iternum $=$ maximum number of iterations; % iternum $= 80000$ works well $k = 0; nr= 1$; ns $= 1$; % typically tolr $= 10^(-10)$; tols $= 10^(-10)$; % Convergence is controlled by the norm nr of the primal residual $r$ % and the norm ns of the dual residual $s$ while $(k <=$ iternum) && (ns $>$ tols || nr $>$ tolr) z0 $= z; k = k+1$; % Makes KKT matrix $KK = [P +$ rho* eye(n) A’; $A$ zeros(m,m)];
$$2169$$

<!-- PAGE 2170 -->
% Makes right hand side of KKT equation bb $= [-q +$ rho*(z - $u); b]$; % Solves KKT equation xx $= KK\bb$; % update $x, z, u$ (ADMM update steps) $x =$ xx(1:n); $z =$ poslin(x $+ u); u = u + x$ - $z$; % to test stopping criterion $r = x$ - $z$; % primal residual nr $=$ sqrt(r’*r); % norm of primal residual $s =$ rho*(z - z0); % dual residual ns $=$ sqrt(s’*s); % norm of dual residual end end The second program SBVMhard2 implements hard margin SVM (version $2)$. function [lamb,mu,w] $=$ SVMhard2(rho,u,v) % % Runs hard margin SVM version $2$ % % $p$ green vectors $u_1$, ..., $u_p$ in $n x p$ array $u$ % $q$ red vectors $v_1$, ..., $v_q$ in $n x q$ array $v$ % % First builds the matrices for the dual program % $p =$ size(u,2); $q =$ size(v,2); $n =$ size(u,1); [A,c,X,Pa,qa] $=$ buildhardSVM2(u,v); % % Runs quadratic solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [lam,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’kk $=$ %d $\n’,kk)$ if kk $>$ iternum fprintf(’** qsolve did not converge. Problem not solvable ** $\n’)$ end $w =$ -X*lam; nw $=$ sqrt(w’*w); % norm of $w$ fprintf(’nw $=$ %.15f $\n’,nw)$

<!-- PAGE 2171 -->
delta $= 1/nw$; fprintf(’delta $=$ %.15f $\n’,delta)$ if delta $< 10^(-9)$ fprintf(’** Warning, delta too small, program does not converge ** $\n’)$ end % lamb $=$ lam(1:p,1); mu $= lam(p+1:p+q,1); b = 0$; tols $= 10^(-10)$; % tols $< lambda_i$; finds the nonzero $lambda_i$ [lambnz,numsvl1] $=$ countmlu2(lamb,tols); % tols $< mu_i$; finds the nonzero $mu_j$ [munz,numsvm1] $=$ countmlv2(mu,tols); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ if numsvl1 $> 0$ && numsvm1 $> 0$ sx1 $=$ zeros(n,1); num1 $= 0$; sx2 $=$ zeros(n,1); num2 $= 0$; for $i =$ 1:p
$$if lambnz(i) > 0$$
$$sx1 = sx1 + u(:,i);$$
$$num1 = num1 + 1;$$
$$end$$
end for $j =$ 1:q
$$if munz(j) > 0$$
$$sx2 = sx2 + v(:,j);$$
$$num2 = num2 + 1;$$
$$end$$
end $b = (w’*(sx1/num1 + sx2/num2))/2$; fprintf(’b $=$ %.15f $\n’,b)$ else fprintf(’** Not enough support vectors ** $\n’)$ end if $n == 2$ [ll,mm] $=$ showdata(u,v); if numsvl1 $> 0$ && numsvm1 $> 0$
$$showSVMs2(w,b,1,ll,mm,nw)$$

<!-- PAGE 2172 -->
end end end The function buildhardSVM2 builds the constraint matrix and the matrices defining the quadratic functional. function [A,c,X,Xa,q] $=$ buildhardSVM2(u,v) % builds the matrix of constraints $A$ for % hard SVM h2, and the right hand side $c$ % Aso builds $X$ and Xa $=$ X’*X, and the vector $q = -1_{p+q}$ % for the linear part of the quadratic function % The right-hand side is $c = 0$ (Ax $= 0). p =$ size(u,2); $q =$ size(v,2); $A =$ [ones(1,p) -ones(1,q)]; $c = 0; X = [-u v]$; Xa $=$ X’*X; $q = -ones(p+q,1)$; end The function countmlu2 returns a vector consisting of those $\lambda_{i}$  such that $\lambda_{i}  > 0$, and the number of such $\lambda_{i}$ . function [lambnz, mlu] $=$ countmlu2(lambda,tols) % Counts the number of points $u_i$ (in $u)$ % such that $lambda_i > 0$ and returns a vector % of these $lambda_i$ % tols $= 10^(-11); p =$ size(lambda,1); lambnz $=$ zeros(p,1); mlu $= 0$; for $i =$ 1:p if lambda(i) $>$ tols
$$mlu = mlu + 1;$$
$$lambnz(i) = lambda(i);$$
end end end The function countmlv2 returns a vector consisting of those $\mu_{j}$  such that $\mu_{j}  > 0$, and the number of such $\mu_{j}$ . It is similar to countmlu2. Here a judicious choice of tols is crucial and one has to experiment with various values.
