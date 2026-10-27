# -SV Regression


<!-- PAGE 2186 -->
end end The function buildSVMs3b builds the constraint matrix and the matrices defining the quadratic program. function [A,c,X,P2,Pa,q] $=$ buildSVMs3b(nu,u,v,K) % builds the matrix of constraints $A$ for % soft margin nu-SVM s3 and the right-hand side $c$ % $u$: vector of $p$ blue points (each an n-dim vector) % $v$: vector of $q$ red points (each an n-dim vector) % builds the matrix $X = [-u_1$ ... $-u_p$ v1 .... $v_q]$ % and the matrix Xa as $2(p+q)$ matrix obtained % by augmenting X’*X with zeros % $K$ is a scale factor $(K =$ Ks) $p =$ size(u,2); $q =$ size(v,2); % Ks $= 1/(p+q)$; Ks $= K$; Km $= (p+q)*K*nu; A =$ [ones(1,p) ones(1,q) $zeros(1,p+q)$ ; eye(p) zeros(p,q) eye(p) zeros(p,q); zeros(q,p) eye(q) zeros(q,p) eye(q) ]; $c =$ [Km; $Ks*ones(p+q,1)]; X = [-u v]$; XX1 $=$ X’*X; XX2 $=$ [ones(p,1)*ones(p,1)’ -ones(p,1)*ones(q,1)’;
$$-ones(q,1)*ones(p,1)’ ones(q,1)*ones(q,1)’];$$
P2 $=$ XX1 $+$ XX2; Pa $=$ [P2 $zeros(p+q,p+q); zeros(p+q, 2*(p+q))]; q = zeros(2*(p+q),1)$; end B.4 $\nu$ -SV Regression $g$ The main function donuregb is given below. function [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,numsvl1,numsvm1,w,epsilon,b]
$$= donuregb (rho,nu,X,y,C)$$
% % Soft margin nu-regression % with the constraint % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu

<!-- PAGE 2187 -->
% (Without the variable gamma) % % Input: an $m x n$ matrix of data points represented as % as the rows of $X$, and $y$ a vector in $R^n$ % % First builds the matrices for the dual program % $C$ is a scale factor % $m =$ size(X,1); $n =$ size(X,2); [A,c,P,Pa,qa] $=$ buildnuregb(nu,X,y,C); % % Runs quadratic solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); % fprintf(’nr $=$ %d ’,nr) % fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’nr $=$ %d’,nr) fprintf(’ ns $=$ %d’,ns) fprintf(’ kk $=$ %d $\n’,kk)$ noconv $= 0$; if kk $>$ iternum noconv $= 1$; fprintf(’** qsolve did not converge. Problem not solvable ** $\n’)$ end lamb $=$ x(1:m,1); mu $= x(m+1:2*m,1)$; alpha $= x((2*m+1):3*m,1)$; beta $= x(3*m+1:4*m,1); w =$ X’*(mu - lamb); % $b = 0$; epsilon $= 0$; tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < C/m$ - tolh [lambnz,numsvl1] $= findpsv2(lamb,C/m,tols,tolh)$; % tols $< mu_i < C/m$ - tolh [munz,numsvm1] $= findpsv2(mu,C/m,tols,tolh)$; fprintf(’numsvl1 $=$ %d’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= C/m$ - tolh [lamK,pf] $= countumf2(lamb,C/m,tolh)$; % number of blue margin failures % $mu_j >= C/m$ - tolh

<!-- PAGE 2188 -->
[muK,qf] $= countvmf2(mu,C/m,tolh)$; % number of red margin failures fprintf(’pf $=$ %d’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % number of points such that $lambda_i >$ tols [~,qm] $=$ countmlv2(mu,tols); % number of points such that $mu_i > 0$ fprintf(’pm $=$ %d’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ % $lambda_i <=$ tols [lmz,nz] $=$ countLzero(lamb,mu,tols); pm2 $=$ numsvl1 $+$ pf; qm2 $=$ numsvm1 $+$ qf; fprintf(’pm2 $=$ %d’,pm2) fprintf(’ qm2 $=$ %d $\n’,qm2)$ lnu $= max(2*pf/m,2*qf/m)$; unu $= min(2*pm/m,2*qm/m)$; fprintf(’lnu $=$ %d’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ fprintf(’nz $=$ %d $\n’,nz)$ if nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
else
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
end $fprintf(’C/m =$ %.15f $’,C/m)$ fprintf(’ $(C nu)/2 =$ %.15f $\n’,(C*nu)/2)$ fprintf(’sum(lambda) $=$ %.15f ’,sum(lamb)) fprintf(’ sum(mu) $=$ %.15f $\n’,sum(mu))$ lamsv $= 0$; musv $= 0$; xi $= 0$; xip $= 0$; if numsvl1 $> 0$ && numsvm1 $> 0$ sx1 $=$ zeros(n,1); sy1 $= 0$; num1 $= 0$; sx2 $=$ zeros(n,1); sy2 $= 0$; num2 $= 0$; for $i =$ 1:m
$$if lambnz(i) > 0$$
$$sx1 = sx1 + X(i,:)’; sy1 = sy1 + y(i);$$
$$num1 = num1 + 1;$$
$$end$$
$$if munz(i) > 0$$
$$sx2 = sx2 + X(i,:)’; sy2 = sy2 + y(i);$$
$$num2 = num2 + 1;$$
$$end$$
end

<!-- PAGE 2189 -->
% num1 % num2 $b = (sy1/num1 + sy2/num2$ - $w’*(sx1/num1 + sx2/num2))/2$; fprintf(’b $=$ %.15f $\n’,b)$ epsilon $= (w’*(sx1/num1$ - $sx2/num2) + sy2/num2$ - $sy1/num1)/2$; fprintf(’epsilon $=$ %.15f $\n’,epsilon)$ if epsilon $< 10^(-10)$
$$fprintf(’** Warning; epsilon is too small or negative ** \n’)$$
end nw $=$ sqrt(w’*w); % norm of $w$ fprintf(’nw $=$ %.15f $\n’,nw)$ % tolxi $= 10^(-10)$; % tols $< lambda_i < C/m$ - tolh or $C/m$ - tolh $<= lambda_i$ and $xi_i <$ tolxi [lamsv,psf,xi] $= findnuregsvl2(lamb,w,b,X,y,epsilon,C/m,tols,tolh,tolxi)$; % tols $< mu_i < C/m$ - tolh or $C/m$ - tolh $<= mu_i$ and $xi_i’ <$ tolxi [musv,qsf,xip] $= findnuregsvm2(mu,w,b,X,y,epsilon,C/m,tols,tolh,tolxi)$; fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ else fprintf(’** Not enough support vectors ** $\n’)$ end end To run donuregb use the function runuregb listed below. function [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w] $=$ runuregb (rho,nu,X,y,C) % % Runs soft margin nu-regression % with the constraint % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu % (Without the variable gamma) % % Input: an $m x n$ matrix of data points represented as % as the rows of $X$, and $y$ a vector in $R^n$ % % First builds the matrices for the dual program % $C$ is a scale factor % $m =$ size(X,1); $n =$ size(X,2); [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,numsvl1,numsvm1,w,epsilon,b]
$$= donuregb(rho,nu,X,y,C);$$

<!-- PAGE 2190 -->
if $n == 1$
$$[ll,mm] = showgraph(X,y);$$
$$ww = [w;-1]; n1 = sqrt(ww’*ww);$$
$$if numsvl1 > 0 && numsvm1 > 0$$
$$showSVMs2(ww,-b,epsilon,ll,mm,n1)$$
$$end$$
else
$$if n == 2$$
$$offset = 10;$$
$$[ll,mm] = showpoints(X,y,offset);$$
$$if numsvl1 > 0 && numsvm1 > 0$$
$$showplanes(w,b,ll,mm,epsilon)$$
$$end$$
$$axis equal$$
$$axis([ll(1) mm(1) ll(2) mm(2)]);$$
$$view([-1 -1 1]);$$
$$xlabel(’X’,’fontsize’,14);ylabel(’Y’,’fontsize’,14);$$
$$zlabel(’Z’,’fontsize’,14);$$
$$end$$
end end The function buildnuregb creates the constraint matrix and the matrices defining the quadratic functional. function [A,c,P,Pa,qa] $=$ buildnuregb (nu,X,y,C) % builds the matrix of constraints $A$ for % soft margin nu-regression % with the constraint % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu % (without the variable gamma) % and the right-hand side $c$. % Input: an $m x n$ matrix $X$ of data points represented as % as the rows of $X$, and $y$ a vector in $R^n$. % builds the $m x m$ matrix $X*X^T$, the 2m $x$ 2m matrix % $P = [X*X^T -X*X^T; -X*X^T X*X^T]$, % and the matrix Pa as the 4m $x$ 4m matrix obtained % by augmenting with zeros. % Also builds the vector $q_a (q$ augmented with zeros). % $C$ is a scale factor. $m =$ size(X,1); $n =$ size(X,2);

<!-- PAGE 2191 -->
% Ks $= 1/(p+q)$; Ks $= C$; Km $=$ C*nu; $A =$ [ones(1,m) -ones(1,m) zeros(1,2*m); ones(1,m) ones(1,m) zeros(1,2*m) ; eye(m) zeros(m,m) eye(m) zeros(m,m); zeros(m,m) eye(m) zeros(m,m) eye(m)]; $c = [0$; Km; $(Ks/m)*ones(2*m,1)]$; XX1 $=$ X*X’; $P =$ [XX1 -XX1; -XX1 XX1]; Pa $= [P$ zeros(2*m,2*m); zeros(2*m, 4*m )]; qa $= [y; -y$; zeros(2*m,1)]; end

<!-- PAGE 2192 -->
