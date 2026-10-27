# Soft Margin SVM (SVMs3)


<!-- PAGE 2181 -->
$$view([-1 -1 1]);$$
$$xlabel(’X’,’fontsize’,14);ylabel(’Y’,’fontsize’,14);$$
$$zlabel(’Z’,’fontsize’,14);$$
$$hold off$$
$$end$$
end end

## B.3 Soft Margin SVM (SVM )

$$s3$$
The following Matlab programs implement the method described in Section 54.12. The main function doSVMs3b is given below. function [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w,b,eta,nw,fail] $=$ doSVMs3b (nu,rho,u,v,K) % % Soft margin nu-SVM version s3 % % Computes eta using the duality gap % Needs a single support vector of type $1$ % % $p$ green vectors $u_1$, ..., $u_p$ in $n x p$ array $u$ % $q$ red vectors $v_1$, ..., $v_q$ in $n x q$ array $v$ % % First builds the matrices for the dual program % $K$ is a scale factor % $p =$ size(u,2); $q =$ size(v,2); $n =$ size(u,1); [A,c,X,P2,Pa,qa] $=$ buildSVMs3b (nu,u,v,K); % % Runs quadratic solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d ’,ns) fprintf(’ kk $=$ %d $\n’,kk)$ noconv $= 0$; if kk $>$ iternum noconv $= 1$; fprintf(’** qsolve did not converge. Problem not solvable ** $\n’)$ end

<!-- PAGE 2182 -->
lam $= x(1:(p+q),1)$; alpha $= x((p+q+1):2*p+q,1)$; beta $= x(2*p+q+1:2*(p+q),1); w =$ -X*lam; nw $=$ sqrt(w’*w); % norm of $w$ fprintf(’nw $=$ %d $\n’,nw)$ lamb $=$ x(1:p,1); mu $= x(p+1:p+q,1); b =$ -(sum(lamb) - sum(mu)); fprintf(’b $=$ %.15f $\n’,b)$ % tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < K$ - tolh [lambnz,numsvl1] $=$ findpsv2(lamb,K,tols,tolh); % tols $< mu_i < K$ - tolh [munz,numsvm1] $=$ findpsv2(mu,K,tols,tolh); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= K$ - tolh [lamK,pf] $=$ countumf2(lamb,K,tolh); % number of blue margin failures % $mu_j >= K$ - tolh [muK,qf] $=$ countvmf2(mu,K,tolh); % number of red margin failures fprintf(’pf $=$ %d ’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % number of points such that $lambda_i >$ tols [~,qm] $=$ countmlv2(mu,tols); % number of points such that $mu_i > 0$ fprintf(’pm $=$ %d ’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ fprintf(’p - pm $=$ %d ’,p - pm) fprintf(’ $q$ - qm $=$ %d $\n’,q$ - qm) lnu $=$ (pf $+ qf)/(p+q)$; unu $=$ (pm $+ qm)/(p+q)$; fprintf(’lnu $=$ %d ’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ if nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
else
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
end

<!-- PAGE 2183 -->
sx1 $=$ zeros(n,1); num1 $= 0$; sKu $=$ zeros(n,1); Knum1 $= 0$; for $i =$ 1:p
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
end % Knum2 % computes eta from the duality gap errterm $=$ w’*(sKv - sKu) $+$ (pf - qf)*b; Pterm $= (1/K)*(lam’*P2*lam)$; denom $= (p+q)*nu$ - pf -qf; fprintf(’denom $=$ %.15f $\n’,denom)$ epsilon $= 0$; xi $= 0$; if denom $> 0$ eta $=$ (errterm $+ Pterm)/denom$; fprintf(’eta $=$ %.15f $\n’,eta)$ if eta $< 10^(-10)$
$$fprintf(’** Warning; eta is too small or negative ** \n’)$$
end tolxi $= 10^(-10)$; % tols $< lambda_i < K$ - tolh or $K$ - tolh $<= lambda_i$ and $epsilon_i <$ tolxi [lamsv,psf,epsilon] $=$ findsvl2(lamb,w,b,u,eta,K,tols,tolh,tolxi);

<!-- PAGE 2184 -->
% tols $< mu_i < K$ - tolh or $K$ - tolh $<= mu_i$ and $xi_i <$ tolxi [musv,qsf,xi] $=$ findsvm2(mu,w,b,v,eta,K,tols,tolh,tolxi); fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ fprintf(’pf - psf $=$ %d ’,pf - psf) fprintf(’ qf - qsf $=$ %d $\n’,qf$ - qsf) else eta $= 0$; denom $= 0$; fprintf(’** Warning, nu $=$ (pf $+ qf)/(p+q)$ ** $\n’)$ end Km $= (p+q)*nu*K$; fprintf(’K $=$ %.15f ’,K) fprintf(’ $(p+q)*nu*Ks =$ %.15f $\n’,Km)$ fprintf(’sum(lambda) $+ sum(mu)=$ %.15f $\n’,sum(lamb) +$ sum(mu)) eta1 $= 0$; if numsvl1 $> 0$ || numsvm1 $> 0$ if numsvl1 $>$ numsvm1
$$eta1 =w’*sx1/num1 - b;$$
else
$$eta1 =b - w’*sx2/num2;$$
end fprintf(’eta1 $=$ %.15f $\n’,eta1)$ else
$$fprintf(’** Warning: not enough support vectors ** \n’)$$
end if denom $== 0$ if numsvl1 $> 0$ || numsvm1 $> 0$
$$eta = eta1;$$
$$fail = 0;$$
else
$$fail = 1;$$
$$fprintf(’** Warning, denom = 0 and not enough support vectors **\n’)$$
end else fail $= 0$; end end The main function doSVMs3b is executed by the following function:

<!-- PAGE 2185 -->
function [lamb,mu,alpha,beta,lambnz,munz,w] $=$ runSVMs3b(nu,rho,u,v,K) % % Runs soft margin nu-SVM version s3 % % Computes eta using the duality gap % Needs a single support vector of type $1$ % % $p$ green vectors $u_1$, ..., $u_p$ in $n x p$ array $u$ % $q$ red vectors $v_1$, ..., $v_q$ in $n x q$ array $v$ % % First builds the matrices for the dual program % $K$ is a scale factor % $p =$ size(u,2); $q =$ size(v,2); $n =$ size(u,1); [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w,b,eta,nw,fail] $=$ doSVMs3b(nu,rho,u,v,K); if $n == 2$
$$[ll,mm] = showdata(u,v);$$
$$if fail == 0$$
$$showSVMs2(w,b,eta,ll,mm,nw)$$
$$end$$
else
$$if n == 3$$
$$showpointsSVM(u,v)$$
$$if fail == 0$$
$$offset = 10;$$
$$C1 = [1 0 1];% magenta$$
$$plotplaneSVM(u,v,w,b,offset,C1)$$
$$C2 = [0 0 1];% blue$$
$$plotplaneSVM(u,v,w,b+eta,offset,C2)$$
$$C3 = [1,0,0];% red$$
$$plotplaneSVM(u,v,w,b-eta,offset,C3)$$
$$end$$
$$axis equal$$
% axis([ll(1) mm(1) ll(2) mm(2)]);
$$view([-1 -1 1]);$$
$$xlabel(’X’,’fontsize’,14);ylabel(’Y’,’fontsize’,14);zlabel(’Z’,$$
$$’fontsize’,14);$$
$$hold off$$
$$end$$
