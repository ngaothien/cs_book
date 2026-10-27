# Lề cứng (hard margin) (SVMh2)


<!-- PAGE 2169 -->
Phụ lục $B$ Matlab Các bài toán quy hoạch

## B.1 Lề cứng (hard margin) (SVM)

$$h2$$
Sau đây Matlab các bài toán quy hoạch cài đặt phương pháp được mô tả trong Mục 52.7. thứ nhất bài toán quy hoạch là heart của phương pháp; nó các cài đặt ADMM cho toàn phương quy hoạch. hàm [x,u,nr,ns,k] $=$ qsolve1(P, $q, A, b$, rho, tolr, tols, iternum) % Giải toàn phương quy hoạch bài toán % min $(1/2) x^T P x + x^T q + r$ % subject đến Ax $= b, x >= 0$ bằng cách sử dụng ADMM % $P n x n, q, r$, trong $R^n, A m x n, b$ trong $R^m$ % $A$ của hạng (rank) $m m =$ kích thước(,1); fprintf(’m $=$ %d ’,m) $n =$ kích thước(P,1); fprintf(’ $n =$ %d $\n’,n) u =$ các một(n,1); u(1,1) $= 0$; % đến initialize $u z =$ các một(n,1); % đến initialize $z$ % iternum $=$ cực đại số của các vòng lặp; % iternum $= 80000$ hoạt động tốt $k = 0; nr= 1$; ns $= 1$; % typically tolr $= 10^(-10)$; tols $= 10^(-10)$; % Sự hội tụ là controlled bởi chuẩn (norm) nr của gốc (primal) phần dư (residual) $r$ % và chuẩn (norm) ns của đối ngẫu (dual) phần dư (residual) $s$ trong khi $(k <=$ iternum) && (ns $>$ tols || nr $>$ tolr) z0 $= z; k = k+1$; % Làm cho KKT ma trận $KK = [P +$ rho* eye(n) ’; $A$ các không điểm(m,m)];
$$2169$$

<!-- PAGE 2170 -->
% Làm cho phải hand vế/cạnh của KKT phương trình bb $= [-q +$ rho*(z - $u); b]$; % Giải KKT phương trình xx $= KK\bb$; % update $x, z, u$ (ADMM update các bước) $x =$ xx(1:n); $z =$ poslin(x $+ u); u = u + x$ - $z$; % đến test stopping tiêu chuẩn $r = x$ - $z$; % gốc (primal) phần dư (residual) nr $=$ sqrt(r’*r); % chuẩn (norm) của gốc (primal) phần dư (residual) $s =$ rho*(z - z0); % đối ngẫu (dual) phần dư (residual) ns $=$ sqrt(s’*s); % chuẩn (norm) của đối ngẫu (dual) phần dư (residual) kết thúc/cuối kết thúc/cuối thứ hai bài toán quy hoạch SBVMhard2 các cài đặt lề cứng (hard margin) SVM (phiên bản $2)$. hàm [lamb,mu,w] $=$ SVMhard2(rho,u,v) % % Chạy lề cứng (hard margin) SVM phiên bản $2$ % % $p$ xanh lục các vectơ $u_1$,..., $u_p$ trong $n x p$ mảng (array) $u$ % $q$ đỏ các vectơ $v_1$,..., $v_q$ trong $n x q$ mảng (array) $v$ % % Thứ nhất xây dựng các ma trận cho đối ngẫu (dual) bài toán quy hoạch % $p =$ kích thước(u,2); $q =$ kích thước(v,2); $n =$ kích thước(u,1); [,c,X,Pa,qa] $=$ buildhardSVM2(u,v); % % Chạy toàn phương solver % tolr $= 10^(-10)$; tols $= 10^(-10)$; iternum $= 80000$; [lam,U,nr,ns,kk] $=$ qsolve1(Pa, qa, $A, c$, rho, tolr, tols, iternum); fprintf(’nr $=$ %d ’,nr) fprintf(’ ns $=$ %d $\n’,ns)$ fprintf(’kk $=$ %d $\n’,kk)$ nếu kk $>$ iternum fprintf(’** qsolve đã thực hiện không hội tụ. Bài toán không giải được ** $\n’)$ kết thúc/cuối $w =$ -X*lam; nw $=$ sqrt(w’*w); % chuẩn (norm) của $w$ fprintf(’nw $=$ %.15f $\n’,nw)$

<!-- PAGE 2171 -->
Delta $= 1/nw$; fprintf(’delta $=$ %.15f $\n’,delta)$ nếu delta $< 10^(-9)$ fprintf(’** Warning, delta cũng nhỏ, bài toán quy hoạch thực hiện không hội tụ ** $\n’)$ kết thúc/cuối % lamb $=$ lam(1:p,1); mu $= lam(p+1:p+q,1); b = 0$; tols $= 10^(-10)$; % tols $< lambda_i$; tìm khác không $lambda_i$ [lambnz,numsvl1] $=$ countmlu2(lamb,tols); % tols $< mu_i$; tìm khác không $mu_j$ [munz,numsvm1] $=$ countmlv2(mu,tols); fprintf(’numsvl1 $=$ %d ’,numsvl1) fprintf(’ numsvm1 $=$ %d $\n’,numsvm1)$ nếu numsvl1 $> 0$ && numsvm1 $> 0$ sx1 $=$ các không điểm(n,1); num1 $= 0$; sx2 $=$ các không điểm(n,1); num2 $= 0$; cho $i =$ 1:p
$$if lambnz(i) > 0$$
$$sx1 = sx1 + u(:,i);$$
$$num1 = num1 + 1;$$
$$end$$
Kết thúc/cuối cho $j =$ 1:q
$$if munz(j) > 0$$
$$sx2 = sx2 + v(:,j);$$
$$num2 = num2 + 1;$$
$$end$$
Kết thúc/cuối $b = (w’*(sx1/num1 + sx2/num2))/2$; fprintf(’b $=$ %.15f $\n’,b)$ khác fprintf(’** Không đủ hỗ trợ/giá (support) các vectơ ** $\n’)$ kết thúc/cuối nếu $n == 2$ [ll,mm] $=$ showdata(u,v); nếu numsvl1 $> 0$ && numsvm1 $> 0$
$$showSVMs2(w,b,1,ll,mm,nw)$$

<!-- PAGE 2172 -->
Kết thúc/cuối kết thúc/cuối kết thúc/cuối hàm buildhardSVM2 xây dựng ràng buộc ma trận và các ma trận định nghĩa toàn phương phiếm hàm. hàm [,c,X,Xa,q] $=$ buildhardSVM2(u,v) % xây dựng ma trận của các ràng buộc $A$ cho % khó SVM h2, và phải hand vế/cạnh $c$ % Aso xây dựng $X$ và Xa $=$ X’*X, và vectơ $q = -1_{p+q}$ % cho tuyến tính phần của toàn phương hàm % vế phải là $c = 0$ (Ax $= 0). p =$ kích thước(u,2); $q =$ kích thước(v,2); $A =$ [các một(1,p) -các một(1,q)]; $c = 0; X = [-u v]$; Xa $=$ X’*X; $q = -ones(p+q,1)$; kết thúc/cuối hàm countmlu2 trả về vectơ bao gồm của những phần tử đó $\lambda_{i}$ sao cho $\lambda_{i}  > 0$, và số của như vậy $\lambda_{i}$. hàm [lambnz, mlu] $=$ countmlu2(lambda,tols) % Counts số của các điểm $u_i$ (trong $u)$ % sao cho $lambda_i > 0$ và trả về vectơ % của các phần tử này $lambda_i$ % tols $= 10^(-11); p =$ kích thước(lambda,1); lambnz $=$ các không điểm(p,1); mlu $= 0$; cho $i =$ 1:p nếu lambda(i) $>$ tols
$$mlu = mlu + 1;$$
$$lambnz(i) = lambda(i);$$
Kết thúc/cuối kết thúc/cuối kết thúc/cuối hàm countmlv2 trả về vectơ bao gồm của những phần tử đó $\mu_{j}$ sao cho $\mu_{j}  > 0$, và số của như vậy $\mu_{j}$. Nó là đồng dạng đến countmlu2. Ở đây judicious lựa chọn của tols là then chốt và một có đến experiment với khác nhau các giá trị.
