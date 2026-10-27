# Lề mềm (soft margin) SVM (SVMs2')


<!-- PAGE 2173 -->
Hàm showdata displays dữ liệu các điểm ($u_{i}$ và $v_{j})$ và hàm showSVMs2 displays tách đường thẳng và hai lề (margin) các đường thẳng. hàm showSVMs2(w,b,eta,ll,mm,nw) % % Hàm đến display kết quả của chạy SVM % trên $p$ xanh lam các điểm $u_1$,..., $u_p$ trong $u$ % và $q$ đỏ các điểm $v_1$,..., $v_q$ trong $v l =$ makeline(w,b,ll,mm,nw); % làm cho tách đường thẳng lm1 $= makeline(w,b+eta,ll,mm,nw)$; % làm cho xanh lam lề (margin) đường thẳng lm2 $=$ makeline(w,b-eta,ll,mm,nw); % làm cho đỏ lề (margin) đường thẳng plot(l(1,:),l(2,:),’-m’,’LineWidth’,1.2) % plots tách đường thẳng plot(lm1(1,:),lm1(2,:),’-b’,’LineWidth’,1.2) % plots xanh lam lề (margin) đường thẳng plot(lm2(1,:),lm2(2,:),’-r’,’LineWidth’,1.2) % plots đỏ lề (margin) đường thẳng đúng ra kết thúc/cuối Thực sự, cài đặt ở trên hàm là không hoàn toàn tầm thường. Nó là cần đến viết hàm makeline đến plot đường thẳng đoạn thẳng mà là phần của đường thẳng của phương trình $w_{1}x+w_{2}y = b$ bên trong hình hộp chứa dữ liệu các điểm. Ta để lại chi tiết các bài tập.

## B.2 Lề mềm (soft margin) SVM (SVM)

$$s2'$$
Sau đây Matlab các bài toán quy hoạch cài đặt phương pháp được mô tả trong Mục 54.8. hàm doSVMs2pbv3 gọi hàm solve1 cho trước trong Mục 52.7. hàm [lamb,mu,alpha,beta,lambnz,munz,numsvl1,numsvm1,badnu,w,nw,b,eta] $=$ doSVMs2pbv3(nu,rho,u,v,K) % % Tốt nhất phiên bản % Sử dụng khoảng cách đối ngẫu (duality gap) để tính eta % Trong nguyên lý, cần đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$ % % Lề mềm (soft margin) nu-SVM phiên bản s2’ % với ràng buộc % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (mà không có biến gamma) % % $p$ xanh lục các vectơ $u_1$,..., $u_p$ trong $n x p$ mảng (array) $u$ % $q$ đỏ các vectơ $v_1$,..., $v_q$ trong $n x q$ mảng (array) $v$

<!-- PAGE 2174 -->
% % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $K$ là scale nhân tử % $p =$ kích thước(u,2); $q =$ kích thước(v,2); $n =$ kích thước(u,1); [,c,X,Pa,qa] $=$ buildSVMs2pb(nu,u,v,K); % % Chạy toàn phương solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [x,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’kk $=$ %d $\n’,kk)$ noconv $= 0$; nếu kk $>$ iternum noconv $= 1$; fprintf(’** qsolve đã thực hiện không hội tụ. Bài toán không giải được ** $\n’)$ kết thúc/cuối lam $= x(1:(p+q),1)$; alpha $= x((p+q+1):2*p+q,1)$; beta $= x(2*p+q+1:2*(p+q),1); w =$ -X*lam; nw $=$ sqrt(w’*w); % chuẩn (norm) của $w$ fprintf(’nw $=$ %d $\n’,nw)$ % lamb $=$ x(1:p,1); mu $= x(p+1:p+q,1)$; tols $= 10^(-10)$; tolh $= 10^(-9)$; % tols $< lambda_i < K$ - tolh [lambnz,numsvl1] $=$ findpsv2(lamb,K,tols,tolh); % tols $< mu_i < K$ - tolh [munz,numsvm1] $=$ findpsv2(mu,K,tols,tolh); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ % $lambda_i >= K$ - tolh [lamK,pf] $=$ countumf2(lamb,K,tolh); % số của xanh lam lề (margin) failures % $mu_j >= K$ - tolh [muK,qf] $=$ countvmf2(mu,K,tolh); % số của đỏ lề (margin) failures fprintf(’pf $=$ %d ’,pf) fprintf(’ qf $=$ %d $\n’,qf)$ [~,pm] $=$ countmlu2(lamb,tols); % số của các điểm sao cho $lambda_i >$ tols

<!-- PAGE 2175 -->
[~,qm] $=$ countmlv2(mu,tols); % số của các điểm sao cho $mu_i > 0$ fprintf(’pm $=$ %d ’,pm) fprintf(’ qm $=$ %d $\n’,qm)$ fprintf(’p - pm $=$ %d ’,p - pm) fprintf(’ $q$ - qm $=$ %d $\n’,q$ - qm) lnu $= max(2*pf/(p+q),2*qf/(p+q))$; unu $= min(2*pm/(p+q),2*qm/(p+q))$; fprintf(’lnu $=$ %d ’,lnu) fprintf(’ unu $=$ %d $\n’,unu)$ nếu nu $<$ lnu
$$fprintf(’** Warning; nu is too small ** \n’)$$
Khác
$$if nu > unu$$
$$fprintf(’** Warning; nu is too big ** \n’)$$
$$end$$
Kết thúc/cuối sx1 $=$ các không điểm(n,1); num1 $= 0$; sKu $=$ các không điểm(n,1); Knum1 $= 0$; cho $i =$ 1:p
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
Kết thúc/cuối % Knum2

<!-- PAGE 2176 -->
$b = 0$; eta $= 0$; epsilon $= 0$; xi $= 0$; P2 $=$ X’*X; badnu $= 0$; nếu numsvl1 $> 0$ nếu numsvm1 $> 0$
$$b =(w’*(sx1/num1 + sx2/num2))/2;$$
$$fprintf(’b =%.15f \n’,b)$$
$$eta =(w’*(sx1/num1 - sx2/num2))/2;$$
$$fprintf(’eta =%.15f \n’,eta)$$
Khác
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
Kết thúc/cuối khác nếu numsvm1 $> 0$
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
Khác
$$fprintf(’** Not enough support vectors ** \n’)$$
Kết thúc/cuối

<!-- PAGE 2177 -->
Kết thúc/cuối Km $= (p+q)*nu*K$; fprintf(’K $=$ %.15f ’,K) fprintf(’ $(p+q)*nu*Ks/2 =$ %.15f $\n’,Km/2)$ fprintf(’tổng(lambda) $=$ %.15f ’,tổng(lamb)) fprintf(’ tổng(mu) $=$ %.15f $\n’,sum(mu))$ nếu (numsvl1 $> 0$ || numsvm1 $> 0)$ && badnu $== 0$ nếu eta $< 10^(-9)$
$$fprintf(’** Warning, eta too small or negative ** \n’)$$
$$eta = 0;$$
Kết thúc/cuối delta $= eta/nw$; fprintf(’delta $=$ %.15f $\n’,delta)$ tolxi $= 10^(-10)$; % tols $< lambda_i < K$ - tolh hoặc $K$ - tolh $<= lambda_i$ và $epsilon_i <$ tolxi [lamsv,psf,epsilon] $=$ findsvl2(lamb,w,b,u,eta,K,tols,tolh,tolxi); % tols $< mu_i < K$ - tolh hoặc $K$ - tolh $<= mu_i$ và $xi_i <$ tolxi [musv,qsf,xi] $=$ findsvm2(mu,w,b,v,eta,K,tols,tolh,tolxi); fprintf(’psf $=$ %d ’,psf) fprintf(’ qsf $=$ %d $\n’,qsf)$ fprintf(’pf - psf $=$ %d ’,pf - psf) fprintf(’ qf - qsf $=$ %d $\n’,qf$ - qsf) % tính eta từ khoảng cách đối ngẫu (duality gap) errterm $=$ w’*(sKv - sKu) $+$ (pf - qf)*b; Pterm $= (1/K)*(lam’*P2*lam)$; denom $= (p+q)*nu$ - pf -qf; fprintf(’denom $=$ %.15f $\n’,denom)$ nếu denom $> 0$
$$eta1 = (errterm + Pterm)/denom;$$
$$fprintf(’eta1 =%.15f \n’,eta1)$$
Kết thúc/cuối kết thúc/cuối kết thúc/cuối ràng buộc ma trận và các ma trận định nghĩa toàn phương bài toán quy hoạch được xây dựng bởi hàm buildSVMs2pb. hàm [,c,X,Pa,q] $=$ buildSVMs2pb(nu,u,v,K) % xây dựng ma trận của các ràng buộc $A$ cho % lề mềm (soft margin) nu-SVM s2’

<!-- PAGE 2178 -->
% với ràng buộc % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (mà không có biến gamma) và vế phải $c$ % $u$: vectơ của $p$ xanh lam các điểm (mỗi n-dim vectơ) % $v$: vectơ của $q$ đỏ các điểm (mỗi n-dim vectơ) % xây dựng ma trận $X = [-u_1$... $-u_p$ v1.... $v_q]$ % và ma trận Pa như $2(p+q)$ ma trận thu được % bởi augmenting X’*X với các không điểm % $K$ là scale nhân tử $(K =$ Ks) $p =$ kích thước(u,2); $q =$ kích thước(v,2); % Ks $= 1/(p+q)$; Ks $= K$; Km $= (p+q)*K*nu; A =$ [các một(1,p) -các một(1,q) $zeros(1,p+q)$; các một(1,p) các một(1,q) $zeros(1,p+q)$; eye(p) các không điểm(p,q) eye(p) các không điểm(p,q); các không điểm(q,p) eye(q) các không điểm(q,p) eye(q) ]; $c = [0$; Km; $Ks*ones(p+q,1)]; X = [-u v]; XX =$ X’*X; Pa $= [XX zeros(p+q,p+q); zeros(p+q, 2*(p+q))]; q = zeros(2*(p+q),1)$; kết thúc/cuối hàm findpsv2 làm cho vectơ của $\lambda_{i}$ (và $\mu_{j}$) tương ứng với hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. hàm [lampsv,num] $=$ findpsv2(lambda,K,tols,tolh) % % hàm này tìm vectơ của % $lambda_i’s$ sao cho $0 < lambda_i < K$ % và số của như vậy $lambda_i$. % % tols $= 10^(-11)$; % nhỏ hơn điều này là, lớn hơn số của
$$%points on the margin$$
% tolh $= 10^(-9)$; % $m =$ kích thước(lambda,1); lampsv $=$ các không điểm(m,1); num $= 0$; cho $i =$ 1:m nếu lambda(i) $>$ tols && lambda(i) $< K$ - tolh
$$lampsv(i) = lambda(i);$$
$$num = num + 1;$$
Kết thúc/cuối

<!-- PAGE 2179 -->
Kết thúc/cuối kết thúc/cuối hàm countumf2 tìm những phần tử đó $\lambda_{i}$ sao cho $\lambda_{i}  = K$. hàm [lamK,mf] $=$ countumf2(lambda,K,tolh) % Counts số của lề (margin) failures, nghĩa là, % các điểm $u_i$ (trong $u)$ sao cho $lambda_i = K p =$ kích thước(lambda,1); mf $= 0$; lamK $=$ các không điểm(p,1); cho $i =$ 1:p nếu lambda(i) $>= K$ - tolh
$$mf = mf + 1;$$
$$lamK(i) = lambda(i);$$
Kết thúc/cuối kết thúc/cuối kết thúc/cuối Tương tự, hàm countvmf2 tìm những phần tử đó $\mu_{j}$ sao cho $\mu_{j}  = K$. hàm countmlu2 tìm những phần tử đó $\lambda_{i}$ sao cho $\lambda_{i}  > 0$. hàm [lambnz, mlu] $=$ countmlu2(lambda,tols) % Counts số của các điểm $u_i$ (trong $u)$ % sao cho $lambda_i > 0$ và trả về vectơ % của các phần tử này $lambda_i$ % tols $= 10^(-11); p =$ kích thước(lambda,1); lambnz $=$ các không điểm(p,1); mlu $= 0$; cho $i =$ 1:p nếu lambda(i) $>$ tols
$$mlu = mlu + 1;$$
$$lambnz(i) = lambda(i);$$
Kết thúc/cuối kết thúc/cuối kết thúc/cuối Tương tự, hàm countmlv2 tìm những phần tử đó $\mu_{j}$ sao cho $\mu_{j}  > 0$. hàm findsvl2 tìm $\lambda_{i}$ tương ứng với xanh lam hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ và $2$ và sai số vectơ $\epsilon$. số của xanh lam các sai số là psf ($u_{i}$ cho mà $\epsilon_{i}  > 0)$. Tương tự hàm findsvm2 tìm $\mu_{j}$ tương ứng với đỏ hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ và $2$ và sai số vectơ $\xi$. số của đỏ các sai số là qsf ($v_{j}$ cho mà $\xi_{j}  > 0)$.

<!-- PAGE 2180 -->
Chính hàm runSVMs2pbv3 gọi doSVMs2pbv3 và displays tách đường thẳng (hoặc mặt phẳng) và hai lề (margin) các đường thẳng (hoặc các mặt phẳng). hàm [lamb,mu,alpha,beta,lambnz,munz,w] $=$ runSVMs2pbv3(nu,rho,u,v,K) % % Tốt nhất phiên bản % Sử dụng khoảng cách đối ngẫu (duality gap) để tính eta % Trong nguyên lý, cần đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$ % % Chạy lề mềm (soft margin) nu-SVM phiên bản s2’ % với ràng buộc % $\sum_{i = 1}^p + \sum_{j = 1}^q mu_j = K_m$ % (mà không có biến gamma) % % $p$ xanh lục các vectơ $u_1$,..., $u_p$ trong $n x p$ mảng (array) $u$ % $q$ đỏ các vectơ $v_1$,..., $v_q$ trong $n x q$ mảng (array) $v$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $K$ là scale nhân tử % $p =$ kích thước(u,2); $q =$ kích thước(v,2); $n =$ kích thước(u,1); [lamb,mu,alpha,beta,lambnz,munz,numsvl1,numsvm1,badnu,w,nw,b,eta]
$$= doSVMs2pbv3(nu,rho,u,v,K);$$
Nếu $n == 2$
$$[ll,mm] = showdata(u,v);$$
$$if (numsvl1 > 0 || numsvm1 > 0) && badnu == 0$$
$$showSVMs2(w,b,eta,ll,mm,nw)$$
$$end$$
Khác
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
