# -SV Hồi quy


<!-- PAGE 2186 -->
Kết thúc/cuối kết thúc/cuối hàm buildSVMs3b xây dựng ràng buộc ma trận và các ma trận định nghĩa toàn phương bài toán quy hoạch. hàm [,c,X,P2,Pa,q] $=$ buildSVMs3b(nu,u,v,K) % xây dựng ma trận của các ràng buộc $A$ cho % lề mềm (soft margin) nu-SVM s3 và vế phải $c$ % $u$: vectơ của $p$ xanh lam các điểm (mỗi n-dim vectơ) % $v$: vectơ của $q$ đỏ các điểm (mỗi n-dim vectơ) % xây dựng ma trận $X = [-u_1$... $-u_p$ v1.... $v_q]$ % và ma trận Xa như $2(p+q)$ ma trận thu được % bởi augmenting X’*X với các không điểm % $K$ là scale nhân tử $(K =$ Ks) $p =$ kích thước(u,2); $q =$ kích thước(v,2); % Ks $= 1/(p+q)$; Ks $= K$; Km $= (p+q)*K*nu; A =$ [các một(1,p) các một(1,q) $zeros(1,p+q)$; eye(p) các không điểm(p,q) eye(p) các không điểm(p,q); các không điểm(q,p) eye(q) các không điểm(q,p) eye(q) ]; $c =$ [Km; $Ks*ones(p+q,1)]; X = [-u v]$; XX1 $=$ X’*X; XX2 $=$ [các một(p,1)*các một(p,1)’ -các một(p,1)*các một(q,1)’;
$$-ones(q,1)*ones(p,1)’ ones(q,1)*ones(q,1)’];$$
P2 $=$ XX1 $+$ XX2; Pa $=$ [P2 $zeros(p+q,p+q); zeros(p+q, 2*(p+q))]; q = zeros(2*(p+q),1)$; kết thúc/cuối B.4 $\nu$ -SV Hồi quy $g$ chính hàm donuregb là cho trước ở dưới. hàm [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,numsvl1,numsvm1,w,epsilon,b]
$$= donuregb (rho,nu,X,y,C)$$
% % Lề mềm (soft margin) nu-regression % với ràng buộc % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu

<!-- PAGE 2187 -->
% (Mà không có biến gamma) % % Input: một ma trận cỡ $m x n$ của dữ liệu các điểm được biểu diễn như % như các hàng của $X$, và $y$ vectơ trong $R^n$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $C$ là scale nhân tử % $m =$ kích thước(X,1); $n =$ kích thước(X,2); [,c,P,Pa,qa] $=$ buildnuregb(nu,X,y,C); % % Chạy toàn phương solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); % fprintf(’nr $=$ %d ’,nr) % fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’nr $=$ %d’,nr) fprintf(’ ns $=$ %d’,ns) fprintf(’ kk $=$ %d $\n’,kk)$ noconv $= 0$; nếu kk $>$ iternum noconv $= 1$; fprintf(’** qsolve đã thực hiện không hội tụ. Bài toán không giải được ** $\n’)$ kết thúc/cuối lamb $=$ x(1:m,1); mu $= x(m+1:2*m,1)$; alpha $= x((2*m+1):3*m,1)$; beta $= x(3*m+1:4*m,1); w =$ X’*(mu - lamb); % $b = 0$; epsilon $= 0$; tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < C/m$ - tolh [lambnz,numsvl1] $= findpsv2(lamb,C/m,tols,tolh)$; % tols $< mu_i < C/m$ - tolh [munz,numsvm1] $= findpsv2(mu,C/m,tols,tolh)$; fprintf(’numsvl1 $=$ %d’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= C/m$ - tolh [lamK,pf] $= countumf2(lamb,C/m,tolh)$; % số của xanh lam lề (margin) failures % $mu_j >= C/m$ - tolh

<!-- PAGE 2188 -->
[muK,qf] $= countvmf2(mu,C/m,tolh)$; % số của đỏ lề (margin) failures fprintf(’pf $=$ %d’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % số của các điểm sao cho $lambda_i >$ tols [~,qm] $=$ countmlv2(mu,tols); % số của các điểm sao cho $mu_i > 0$ fprintf(’pm $=$ %d’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ % $lambda_i <=$ tols [lmz,nz] $=$ countLzero(lamb,mu,tols); pm2 $=$ numsvl1 $+$ pf; qm2 $=$ numsvm1 $+$ qf; fprintf(’pm2 $=$ %d’,pm2) fprintf(’ qm2 $=$ %d $\n’,qm2)$ lnu $= max(2*pf/m,2*qf/m)$; unu $= min(2*pm/m,2*qm/m)$; fprintf(’lnu $=$ %d’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ fprintf(’nz $=$ %d $\n’,nz)$ nếu nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
Khác
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
Kết thúc/cuối $fprintf(’C/m =$ %.15f $’,C/m)$ fprintf(’ $(C nu)/2 =$ %.15f $\n’,(C*nu)/2)$ fprintf(’tổng(lambda) $=$ %.15f ’,tổng(lamb)) fprintf(’ tổng(mu) $=$ %.15f $\n’,sum(mu))$ lamsv $= 0$; musv $= 0$; xi $= 0$; xip $= 0$; nếu numsvl1 $> 0$ && numsvm1 $> 0$ sx1 $=$ các không điểm(n,1); sy1 $= 0$; num1 $= 0$; sx2 $=$ các không điểm(n,1); sy2 $= 0$; num2 $= 0$; cho $i =$ 1:m
$$if lambnz(i) > 0$$
$$sx1 = sx1 + X(i,:)’; sy1 = sy1 + y(i);$$
$$num1 = num1 + 1;$$
$$end$$
$$if munz(i) > 0$$
$$sx2 = sx2 + X(i,:)’; sy2 = sy2 + y(i);$$
$$num2 = num2 + 1;$$
$$end$$
Kết thúc/cuối

<!-- PAGE 2189 -->
% num1 % num2 $b = (sy1/num1 + sy2/num2$ - $w’*(sx1/num1 + sx2/num2))/2$; fprintf(’b $=$ %.15f $\n’,b)$ epsilon $= (w’*(sx1/num1$ - $sx2/num2) + sy2/num2$ - $sy1/num1)/2$; fprintf(’epsilon $=$ %.15f $\n’,epsilon)$ nếu epsilon $< 10^(-10)$
$$fprintf(’** Warning; epsilon is too small or negative ** \n’)$$
Kết thúc/cuối nw $=$ sqrt(w’*w); % chuẩn (norm) của $w$ fprintf(’nw $=$ %.15f $\n’,nw)$ % tolxi $= 10^(-10)$; % tols $< lambda_i < C/m$ - tolh hoặc $C/m$ - tolh $<= lambda_i$ và $xi_i <$ tolxi [lamsv,psf,xi] $= findnuregsvl2(lamb,w,b,X,y,epsilon,C/m,tols,tolh,tolxi)$; % tols $< mu_i < C/m$ - tolh hoặc $C/m$ - tolh $<= mu_i$ và $xi_i’ <$ tolxi [musv,qsf,xip] $= findnuregsvm2(mu,w,b,X,y,epsilon,C/m,tols,tolh,tolxi)$; fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ khác fprintf(’** Không đủ hỗ trợ/giá (support) các vectơ ** $\n’)$ kết thúc/cuối kết thúc/cuối Đến chạy donuregb sử dụng hàm runuregb được liệt kê ở dưới. hàm [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w] $=$ runuregb (rho,nu,X,y,C) % % Chạy lề mềm (soft margin) nu-regression % với ràng buộc % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu % (Mà không có biến gamma) % % Input: một ma trận cỡ $m x n$ của dữ liệu các điểm được biểu diễn như % như các hàng của $X$, và $y$ vectơ trong $R^n$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $C$ là scale nhân tử % $m =$ kích thước(X,1); $n =$ kích thước(X,2); [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,numsvl1,numsvm1,w,epsilon,b]
$$= donuregb(rho,nu,X,y,C);$$

<!-- PAGE 2190 -->
Nếu $n == 1$
$$[ll,mm] = showgraph(X,y);$$
$$ww = [w;-1]; n1 = sqrt(ww’*ww);$$
$$if numsvl1 > 0 && numsvm1 > 0$$
$$showSVMs2(ww,-b,epsilon,ll,mm,n1)$$
$$end$$
Khác
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
Kết thúc/cuối kết thúc/cuối hàm buildnuregb creates ràng buộc ma trận và các ma trận định nghĩa toàn phương phiếm hàm. hàm [,c,P,Pa,qa] $=$ buildnuregb (nu,X,y,C) % xây dựng ma trận của các ràng buộc $A$ cho % lề mềm (soft margin) nu-regression % với ràng buộc % $\sum_{i = 1}^m + \sum_{j = 1}^m mu_j = C$ nu % (mà không có biến gamma) % và vế phải $c$. % Input: một ma trận cỡ $m x n$ $X$ của dữ liệu các điểm được biểu diễn như % như các hàng của $X$, và $y$ vectơ trong $R^n$. % xây dựng ma trận cỡ $m x m$ $X*X^T$, 2m $x$ 2m ma trận % $P = [X*X^T -X*X^T; -X*X^T X*X^T]$, % và ma trận Pa như 4m $x$ 4m ma trận thu được % bởi augmenting với các không điểm. % Cũng xây dựng vectơ $q_a (q$ augmented với các không điểm). % $C$ là scale nhân tử. $m =$ kích thước(X,1); $n =$ kích thước(X,2);

<!-- PAGE 2191 -->
% Ks $= 1/(p+q)$; Ks $= C$; Km $=$ C*nu; $A =$ [các một(1,m) -các một(1,m) các không điểm(1,2*m); các một(1,m) các một(1,m) các không điểm(1,2*m); eye(m) các không điểm(m,m) eye(m) các không điểm(m,m); các không điểm(m,m) eye(m) các không điểm(m,m) eye(m)]; $c = [0$; Km; $(Ks/m)*ones(2*m,1)]$; XX1 $=$ X*X’; $P =$ [XX1 -XX1; -XX1 XX1]; Pa $= [P$ các không điểm(2*m,2*m); các không điểm(2*m, 4*m)]; qa $= [y; -y$; các không điểm(2*m,1)]; kết thúc/cuối

<!-- PAGE 2192 -->
