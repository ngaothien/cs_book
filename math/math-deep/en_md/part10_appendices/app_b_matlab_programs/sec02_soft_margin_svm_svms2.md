# Soft Margin SVM (SVMs2')


<!-- PAGE 2173 -->
The function showdata displays the data points (the $u_{i}$ and the $v_{j})$ and the function showSVMs2 displays the separating line and the two margin lines. function showSVMs2(w,b,eta,ll,mm,nw) % % Function to display the result of running SVM % on $p$ blue points $u_1$, ..., $u_p$ in $u$ % and $q$ red points $v_1$, ..., $v_q$ in $v l =$ makeline(w,b,ll,mm,nw); % makes separating line lm1 $= makeline(w,b+eta,ll,mm,nw)$; % makes blue margin line lm2 $=$ makeline(w,b-eta,ll,mm,nw); % makes red margin line plot(l(1,:),l(2,:),’-m’,’LineWidth’,1.2) % plots separating line plot(lm1(1,:),lm1(2,:),’-b’,’LineWidth’,1.2) % plots blue margin line plot(lm2(1,:),lm2(2,:),’-r’,’LineWidth’,1.2) % plots red margin line hold off end Actually, implementing the above function is not entirely trivial. It is necessary to write a function makeline to plot the line segment which is part of the line of equation $w_{1}x+w_{2}y = b$ inside a box containing the data points. We leave the details an exercises.

## B.2 Soft Margin SVM (SVM )

$$s2'$$
The following Matlab programs implement the method described in Section 54.8. The function doSVMs2pbv3 calls the function solve1 given in Section 52.7. function [lamb,mu,alpha,beta,lambnz,munz,numsvl1,numsvm1,badnu,w,nw,b,eta] $=$ doSVMs2pbv3(nu,rho,u,v,K) % % Best version % Uses the duality gap to compute eta % In principle, needs a single support vector of type $1$ % % Soft margin nu-SVM version s2’ % with the constraint % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (without the variable gamma) % % $p$ green vectors $u_1$, ..., $u_p$ in $n x p$ array $u$ % $q$ red vectors $v_1$, ..., $v_q$ in $n x q$ array $v$

<!-- PAGE 2174 -->
% % First builds the matrices for the dual program % $K$ is a scale factor % $p =$ size(u,2); $q =$ size(v,2); $n =$ size(u,1); [A,c,X,Pa,qa] $=$ buildSVMs2pb(nu,u,v,K); % % Runs quadratic solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’kk $=$ %d $\n’,kk)$ noconv $= 0$; if kk $>$ iternum noconv $= 1$; fprintf(’** qsolve did not converge. Problem not solvable ** $\n’)$ end lam $= x(1:(p+q),1)$; alpha $= x((p+q+1):2*p+q,1)$; beta $= x(2*p+q+1:2*(p+q),1); w =$ -X*lam; nw $=$ sqrt(w’*w); % norm of $w$ fprintf(’nw $=$ %d $\n’,nw)$ % lamb $=$ x(1:p,1); mu $= x(p+1:p+q,1)$; tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < K$ - tolh [lambnz,numsvl1] $=$ findpsv2(lamb,K,tols,tolh); % tols $< mu_i < K$ - tolh [munz,numsvm1] $=$ findpsv2(mu,K,tols,tolh); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= K$ - tolh [lamK,pf] $=$ countumf2(lamb,K,tolh); % number of blue margin failures % $mu_j >= K$ - tolh [muK,qf] $=$ countvmf2(mu,K,tolh); % number of red margin failures fprintf(’pf $=$ %d ’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % number of points such that $lambda_i >$ tols

<!-- PAGE 2175 -->
[~,qm] $=$ countmlv2(mu,tols); % number of points such that $mu_i > 0$ fprintf(’pm $=$ %d ’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ fprintf(’p - pm $=$ %d ’,p - pm) fprintf(’ $q$ - qm $=$ %d $\n’,q$ - qm) lnu $= max(2*pf/(p+q),2*qf/(p+q))$; unu $= min(2*pm/(p+q),2*qm/(p+q))$; fprintf(’lnu $=$ %d ’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ if nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
else
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
end sx1 $=$ zeros(n,1); num1 $= 0$; sKu $=$ zeros(n,1); Knum1 $= 0$; for $i =$ 1:p
$$if lambnz(i) > 0$$
$$sx1 = sx1 + u(:,i);$$
$$num1 = num1 + 1;$$
$$end$$
$$if lamK(i) > 0$$
$$sKu = sKu + u(:,i);$$
$$Knum1 = Knum1 + 1;$$
$$end$$
end % Knum1 sx2 $=$ zeros(n,1); num2 $= 0$; sKv $=$ zeros(n,1); Knum2 $= 0$; for $j =$ 1:q
$$if munz(j) > 0$$
$$sx2 = sx2 + v(:,j);$$
$$num2 = num2 + 1;$$
$$end$$
$$if muK(j) > 0$$
$$sKv = sKv + v(:,j);$$
$$Knum2 = Knum2 + 1;$$
$$end$$
end % Knum2

<!-- PAGE 2176 -->
$b = 0$; eta $= 0$; epsilon $= 0$; xi $= 0$; P2 $=$ X’*X; badnu $= 0$; if numsvl1 $> 0$ if numsvm1 $> 0$
$$b =(w’*(sx1/num1 + sx2/num2))/2;$$
$$fprintf(’b =%.15f \n’,b)$$
$$eta =(w’*(sx1/num1 - sx2/num2))/2;$$
$$fprintf(’eta =%.15f \n’,eta)$$
else
$$errterm = w’*(sKv - sKu) + (pf - qf)*w’*(sx1/num1);$$
$$Pterm = (1/K)*(lam’*P2*lam);$$
$$denomqf = (p+q)*nu-2*qf;$$
$$fprintf(’denomqf =%.15f \n’,denomqf)$$
$$if denomqf > 0$$
$$eta = (errterm + Pterm)/denomqf;$$
$$fprintf(’eta =%.15f \n’,eta)$$
$$b = -eta + w’*sx1/num1;$$
$$else$$
$$badnu = 1;$$
$$fprintf(’** Warning: numsvl1 > 0, numsvm1 = 0 and nu = 2*qf/(p+q) **\n’)$$
$$end$$
end else if numsvm1 $> 0$
$$errterm = w’*(sKv - sKu) + (pf - qf)*w’*(sx2/num2);$$
$$Pterm = (1/K)*(lam’*P2*lam);$$
$$denompf = (p+q)*nu-2*pf;$$
$$fprintf(’denompf =%.15f \n’,denompf)$$
$$if denompf > 0$$
$$eta = (errterm + Pterm)/denompf;$$
$$fprintf(’eta =%.15f \n’,eta)$$
$$b = eta + w’*sx2/num2;$$
$$else$$
$$badnu = 1;$$
$$fprintf(’** Warning: numsvm1 > 0, numsvl1 = 0 and nu = 2*pf/(p+q) **\n’)$$
$$end$$
else
$$fprintf(’** Not enough support vectors ** \n’)$$
end

<!-- PAGE 2177 -->
end Km $= (p+q)*nu*K$; fprintf(’K $=$ %.15f ’,K) fprintf(’ $(p+q)*nu*Ks/2 =$ %.15f $\n’,Km/2)$ fprintf(’sum(lambda) $=$ %.15f ’,sum(lamb)) fprintf(’ sum(mu) $=$ %.15f $\n’,sum(mu))$ if (numsvl1 $> 0$ || numsvm1 $> 0)$ && badnu $== 0$ if eta $< 10^(-9)$
$$fprintf(’** Warning, eta too small or negative ** \n’)$$
$$eta = 0;$$
end delta $= eta/nw$; fprintf(’delta $=$ %.15f $\n’,delta)$ tolxi $= 10^(-10)$; % tols $< lambda_i < K$ - tolh or $K$ - tolh $<= lambda_i$ and $epsilon_i <$ tolxi [lamsv,psf,epsilon] $=$ findsvl2(lamb,w,b,u,eta,K,tols,tolh,tolxi); % tols $< mu_i < K$ - tolh or $K$ - tolh $<= mu_i$ and $xi_i <$ tolxi [musv,qsf,xi] $=$ findsvm2(mu,w,b,v,eta,K,tols,tolh,tolxi); fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ fprintf(’pf - psf $=$ %d ’,pf - psf) fprintf(’ qf - qsf $=$ %d $\n’,qf$ - qsf) % computes eta from the duality gap errterm $=$ w’*(sKv - sKu) $+$ (pf - qf)*b; Pterm $= (1/K)*(lam’*P2*lam)$; denom $= (p+q)*nu$ - pf -qf; fprintf(’denom $=$ %.15f $\n’,denom)$ if denom $> 0$
$$eta1 = (errterm + Pterm)/denom;$$
$$fprintf(’eta1 =%.15f \n’,eta1)$$
end end end The constraint matrix and the matrices defining the quadratic program are constructed by the function buildSVMs2pb. function [A,c,X,Pa,q] $=$ buildSVMs2pb(nu,u,v,K) % builds the matrix of constraints $A$ for % soft margin nu-SVM s2’

<!-- PAGE 2178 -->
% with the constraint % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (without the variable gamma) and the right-hand side $c$ % $u$: vector of $p$ blue points (each an n-dim vector) % $v$: vector of $q$ red points (each an n-dim vector) % builds the matrix $X = [-u_1$ ... $-u_p$ v1 .... $v_q]$ % and the matrix Pa as $2(p+q)$ matrix obtained % by augmenting X’*X with zeros % $K$ is a scale factor $(K =$ Ks) $p =$ size(u,2); $q =$ size(v,2); % Ks $= 1/(p+q)$; Ks $= K$; Km $= (p+q)*K*nu; A =$ [ones(1,p) -ones(1,q) $zeros(1,p+q)$; ones(1,p) ones(1,q) $zeros(1,p+q)$ ; eye(p) zeros(p,q) eye(p) zeros(p,q); zeros(q,p) eye(q) zeros(q,p) eye(q) ]; $c = [0$; Km; $Ks*ones(p+q,1)]; X = [-u v]; XX =$ X’*X; Pa $= [XX zeros(p+q,p+q); zeros(p+q, 2*(p+q))]; q = zeros(2*(p+q),1)$; end The function findpsv2 makes a vector of $\lambda_{i}$  (and $\mu_{j}$ ) corresponding to support vectors of type $1$. function [lampsv,num] $=$ findpsv2(lambda,K,tols,tolh) % % This function find the vector of % $lambda_i’s$ such that $0 < lambda_i < K$ % and the number of such $lambda_i$. % % tols $= 10^(-11)$; % the smaller this is, the larger the number of
$$%points on the margin$$
% tolh $= 10^(-9)$; % $m =$ size(lambda,1); lampsv $=$ zeros(m,1); num $= 0$; for $i =$ 1:m if lambda(i) $>$ tols && lambda(i) $< K$ - tolh
$$lampsv(i) = lambda(i);$$
$$num = num + 1;$$
end

<!-- PAGE 2179 -->
end end The function countumf2 finds those $\lambda_{i}$  such that $\lambda_{i}  = K$. function [lamK,mf] $=$ countumf2(lambda,K,tolh) % Counts the number of margin failures, that is, % points $u_i$ (in $u)$ such that $lambda_i = K p =$ size(lambda,1); mf $= 0$; lamK $=$ zeros(p,1); for $i =$ 1:p if lambda(i) $>= K$ - tolh
$$mf = mf + 1;$$
$$lamK(i) = lambda(i);$$
end end end Similarly, the function countvmf2 finds those $\mu_{j}$  such that $\mu_{j}  = K$. The function countmlu2 finds those $\lambda_{i}$  such that $\lambda_{i}  > 0$. function [lambnz, mlu] $=$ countmlu2(lambda,tols) % Counts the number of points $u_i$ (in $u)$ % such that $lambda_i > 0$ and returns a vector % of these $lambda_i$ % tols $= 10^(-11); p =$ size(lambda,1); lambnz $=$ zeros(p,1); mlu $= 0$; for $i =$ 1:p if lambda(i) $>$ tols
$$mlu = mlu + 1;$$
$$lambnz(i) = lambda(i);$$
end end end Similarly, the function countmlv2 finds those $\mu_{j}$  such that $\mu_{j}  > 0$. The function findsvl2 finds the $\lambda_{i}$  corresponding to blue support vectors of type $1$ and $2$ and the error vector $\epsilon$ . The number of blue errors is psf (the $u_{i}$ for which $\epsilon_{i}  > 0)$. Similarly the function findsvm2 finds the $\mu_{j}$  corresponding to red support vectors of type $1$ and $2$ and the error vector $\xi$ . The number of red errors is qsf (the $v_{j}$ for which $\xi_{j}  > 0)$.

<!-- PAGE 2180 -->
The main function runSVMs2pbv3 calls doSVMs2pbv3 and displays the separating line (or plane) and the two margin lines (or planes). function [lamb,mu,alpha,beta,lambnz,munz,w] $=$ runSVMs2pbv3(nu,rho,u,v,K) % % Best version % Uses the duality gap to compute eta % In principle, needs a single support vector of type $1$ % % Runs soft margin nu-SVM version s2’ % with the constraint % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (without the variable gamma) % % $p$ green vectors $u_1$, ..., $u_p$ in $n x p$ array $u$ % $q$ red vectors $v_1$, ..., $v_q$ in $n x q$ array $v$ % % First builds the matrices for the dual program % $K$ is a scale factor % $p =$ size(u,2); $q =$ size(v,2); $n =$ size(u,1); [lamb,mu,alpha,beta,lambnz,munz,numsvl1,numsvm1,badnu,w,nw,b,eta]
$$= doSVMs2pbv3(nu,rho,u,v,K);$$
if $n == 2$
$$[ll,mm] = showdata(u,v);$$
$$if (numsvl1 > 0 || numsvm1 > 0) && badnu == 0$$
$$showSVMs2(w,b,eta,ll,mm,nw)$$
$$end$$
else
$$if n == 3$$
$$showpointsSVM(u,v)$$
$$if (numsvl1 > 0 || numsvm1 > 0) && badnu == 0$$
$$offset = 10;$$
$$C1 = [1 0 1];% magenta$$
$$plotplaneSVM(u,v,w,b,offset,C1)$$
$$C2 = [0 0 1];% blue$$
$$plotplaneSVM(u,v,w,b+eta,offset,C2)$$
$$C3 = [1,0,0];% red$$
$$plotplaneSVM(u,v,w,b-eta,offset,C3)$$
$$end$$
$$axis equal$$
