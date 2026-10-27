# Lề mềm (soft margin) SVM (SVMs3)


<!-- PAGE 2181 -->
$$view([-1 -1 1]);$$
$$xlabel(’X’,’fontsize’,14);ylabel(’Y’,’fontsize’,14);$$
$$zlabel(’Z’,’fontsize’,14);$$
$$hold off$$
$$end$$
Kết thúc/cuối kết thúc/cuối

## B.3 Lề mềm (soft margin) SVM (SVM)

$$s3$$
Sau đây Matlab các bài toán quy hoạch cài đặt phương pháp được mô tả trong Mục 54.12. chính hàm doSVMs3b là cho trước ở dưới. hàm [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w,b,eta,nw,thất bại] $=$ doSVMs3b (nu,rho,u,v,K) % % Lề mềm (soft margin) nu-SVM phiên bản s3 % % Tính eta bằng cách sử dụng khoảng cách đối ngẫu (duality gap) % Cần đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$ % % $p$ xanh lục các vectơ $u_1$,..., $u_p$ trong $n x p$ mảng (array) $u$ % $q$ đỏ các vectơ $v_1$,..., $v_q$ trong $n x q$ mảng (array) $v$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $K$ là scale nhân tử % $p =$ kích thước(u,2); $q =$ kích thước(v,2); $n =$ kích thước(u,1); [,c,X,P2,Pa,qa] $=$ buildSVMs3b (nu,u,v,K); % % Chạy toàn phương solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d ’,ns) fprintf(’ kk $=$ %d $\n’,kk)$ noconv $= 0$; nếu kk $>$ iternum noconv $= 1$; fprintf(’** qsolve đã thực hiện không hội tụ. Bài toán không giải được ** $\n’)$ kết thúc/cuối

<!-- PAGE 2182 -->
Lam $= x(1:(p+q),1)$; alpha $= x((p+q+1):2*p+q,1)$; beta $= x(2*p+q+1:2*(p+q),1); w =$ -X*lam; nw $=$ sqrt(w’*w); % chuẩn (norm) của $w$ fprintf(’nw $=$ %d $\n’,nw)$ lamb $=$ x(1:p,1); mu $= x(p+1:p+q,1); b =$ -(tổng(lamb) - tổng(mu)); fprintf(’b $=$ %.15f $\n’,b)$ % tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < K$ - tolh [lambnz,numsvl1] $=$ findpsv2(lamb,K,tols,tolh); % tols $< mu_i < K$ - tolh [munz,numsvm1] $=$ findpsv2(mu,K,tols,tolh); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= K$ - tolh [lamK,pf] $=$ countumf2(lamb,K,tolh); % số của xanh lam lề (margin) failures % $mu_j >= K$ - tolh [muK,qf] $=$ countvmf2(mu,K,tolh); % số của đỏ lề (margin) failures fprintf(’pf $=$ %d ’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % số của các điểm sao cho $lambda_i >$ tols [~,qm] $=$ countmlv2(mu,tols); % số của các điểm sao cho $mu_i > 0$ fprintf(’pm $=$ %d ’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ fprintf(’p - pm $=$ %d ’,p - pm) fprintf(’ $q$ - qm $=$ %d $\n’,q$ - qm) lnu $=$ (pf $+ qf)/(p+q)$; unu $=$ (pm $+ qm)/(p+q)$; fprintf(’lnu $=$ %d ’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ nếu nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
Khác
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
Kết thúc/cuối

<!-- PAGE 2183 -->
Sx1 $=$ các không điểm(n,1); num1 $= 0$; sKu $=$ các không điểm(n,1); Knum1 $= 0$; cho $i =$ 1:p
$$if lambnz(i) > 0$$
$$sx1 = sx1 + u(:,i);$$
$$num1 = num1 + 1;$$
$$end$$
$$if lamK(i) > 0$$
$$sKu = sKu + u(:,i);$$
$$Knum1 = Knum1 + 1;$$
$$end$$
Kết thúc/cuối % Knum1 sx2 $=$ các không điểm(n,1); num2 $= 0$; sKv $=$ các không điểm(n,1); Knum2 $= 0$; cho $j =$ 1:q
$$if munz(j) > 0$$
$$sx2 = sx2 + v(:,j);$$
$$num2 = num2 + 1;$$
$$end$$
$$if muK(j) > 0$$
$$sKv = sKv + v(:,j);$$
$$Knum2 = Knum2 + 1;$$
$$end$$
Kết thúc/cuối % Knum2 % tính eta từ khoảng cách đối ngẫu (duality gap) errterm $=$ w’*(sKv - sKu) $+$ (pf - qf)*b; Pterm $= (1/K)*(lam’*P2*lam)$; denom $= (p+q)*nu$ - pf -qf; fprintf(’denom $=$ %.15f $\n’,denom)$ epsilon $= 0$; xi $= 0$; nếu denom $> 0$ eta $=$ (errterm $+ Pterm)/denom$; fprintf(’eta $=$ %.15f $\n’,eta)$ nếu eta $< 10^(-10)$
$$fprintf(’** Warning; eta is too small or negative ** \n’)$$
Kết thúc/cuối tolxi $= 10^(-10)$; % tols $< lambda_i < K$ - tolh hoặc $K$ - tolh $<= lambda_i$ và $epsilon_i <$ tolxi [lamsv,psf,epsilon] $=$ findsvl2(lamb,w,b,u,eta,K,tols,tolh,tolxi);

<!-- PAGE 2184 -->
% tols $< mu_i < K$ - tolh hoặc $K$ - tolh $<= mu_i$ và $xi_i <$ tolxi [musv,qsf,xi] $=$ findsvm2(mu,w,b,v,eta,K,tols,tolh,tolxi); fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ fprintf(’pf - psf $=$ %d ’,pf - psf) fprintf(’ qf - qsf $=$ %d $\n’,qf$ - qsf) khác eta $= 0$; denom $= 0$; fprintf(’** Warning, nu $=$ (pf $+ qf)/(p+q)$ ** $\n’)$ kết thúc/cuối Km $= (p+q)*nu*K$; fprintf(’K $=$ %.15f ’,K) fprintf(’ $(p+q)*nu*Ks =$ %.15f $\n’,Km)$ fprintf(’tổng(lambda) $+ sum(mu)=$ %.15f $\n’,sum(lamb) +$ tổng(mu)) eta1 $= 0$; nếu numsvl1 $> 0$ || numsvm1 $> 0$ nếu numsvl1 $>$ numsvm1
$$eta1 =w’*sx1/num1 - b;$$
Khác
$$eta1 =b - w’*sx2/num2;$$
Kết thúc/cuối fprintf(’eta1 $=$ %.15f $\n’,eta1)$ khác
$$fprintf(’** Warning: not enough support vectors ** \n’)$$
Kết thúc/cuối nếu denom $== 0$ nếu numsvl1 $> 0$ || numsvm1 $> 0$
$$eta = eta1;$$
$$fail = 0;$$
Khác
$$fail = 1;$$
$$fprintf(’** Warning, denom = 0 and not enough support vectors **\n’)$$
Kết thúc/cuối khác thất bại $= 0$; kết thúc/cuối kết thúc/cuối chính hàm doSVMs3b là executed bởi sau đây hàm:

<!-- PAGE 2185 -->
Hàm [lamb,mu,alpha,beta,lambnz,munz,w] $=$ runSVMs3b(nu,rho,u,v,K) % % Chạy lề mềm (soft margin) nu-SVM phiên bản s3 % % Tính eta bằng cách sử dụng khoảng cách đối ngẫu (duality gap) % Cần đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$ % % $p$ xanh lục các vectơ $u_1$,..., $u_p$ trong $n x p$ mảng (array) $u$ % $q$ đỏ các vectơ $v_1$,..., $v_q$ trong $n x q$ mảng (array) $v$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $K$ là scale nhân tử % $p =$ kích thước(u,2); $q =$ kích thước(v,2); $n =$ kích thước(u,1); [lamb,mu,alpha,beta,lambnz,munz,lamK,muK,w,b,eta,nw,thất bại] $=$ doSVMs3b(nu,rho,u,v,K); nếu $n == 2$
$$[ll,mm] = showdata(u,v);$$
$$if fail == 0$$
$$showSVMs2(w,b,eta,ll,mm,nw)$$
$$end$$
Khác
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
% trục([ll(1) mm(1) ll(2) mm(2)]);
$$view([-1 -1 1]);$$
$$xlabel(’X’,’fontsize’,14);ylabel(’Y’,’fontsize’,14);zlabel(’Z’,$$
$$’fontsize’,14);$$
$$hold off$$
$$end$$
