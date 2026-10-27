# Đầy đủ hóa của Không gian vectơ định chuẩn (normed vector space)


<!-- PAGE 1428 -->
Bằng cách sử dụng $(*_{2})$, ta cũng có
$$\|f_{m}(u)\|\le \|f_{m}\|\|u\|\le (\|f_{n}\|+ \epsilon ) \|u\|for all m, n \ge N,$$
Rằng là,
$$\|f_{m}(u)\|\le (\|f_{n}\|+ \epsilon ) \|u\|for all m, n \ge N.(*_{3})$$
Đúng $n \ge N$ cố định và cho $m$ tiến tới đến $+\infty$ trong $(*_{3})$. Vì chuẩn (norm) là liên tục, ta thu được
$$\|f(u)\|\le (\|f_{n}\|+ \epsilon ) \|u\|,$$
Mà chỉ ra rằng $f$ là liên tục. Bước $4$. hàm $f$ là giới hạn của $(f_{n})$ cho chuẩn toán tử (operator norm). Nhắc lại $(*_{1})$:
$$\|f_{m}(u) -f_{n}(u)\|\le \epsilon  \|u\|for all m, n \ge N.(*_{1})$$
Đúng $n \ge N$ cố định nhưng điều này time cho $m$ tiến tới đến $+\infty$ trong $(*_{1})$. Bởi tính liên tục của chuẩn (norm) ta thu được
$$\|f(u) -f_{n}(u)\|= \|(f -f_{n})(u)\|\le \epsilon  \|u\|.$$
Theo định nghĩa của chuẩn toán tử (operator norm),
$$\|f -f_{n}\|= \sup{\|(f -f_{n})(u)\|| \|u\|= 1} \le \epsilon for all n \ge N,$$
Mà chứng tỏ rằng $f_{n}$ hội tụ đến $f$ cho chuẩn toán tử (operator norm). Như đặc biệt trường hợp của Định lý 37.62, nếu ta cho $F = \mathbb{R}$ (hoặc $F = \mathbb{C}$ trong trường hợp của phức
$$\mathbb{R} \mathbb{C} \mathbb{R} \mathbb{C}$$
Các không gian vectơ) ta xem rằng E' $= \mathcal{L}(E$;) (hoặc E' $= \mathcal{L}(E$;)) là đầy đủ (vì và là đầy đủ). không gian E' của liên tục các dạng tuyến tính trên $E$ được gọi là đối ngẫu (dual) của $E$. Nó là không gian con của đại số đối ngẫu (dual) $E^{*}$ của $E$ mà bao gồm của tất cả các dạng tuyến tính trên $E$, không nhất thiết liên tục. Nó có thể cũng được hiển thị rằng nếu $E, F$ và $G$ là các không gian vectơ định chuẩn, và nếu $G$ là Không gian Banach (Banach space), thì $\mathcal{L}_{2}(E, F; G)$ là Không gian Banach (Banach space). chứng minh là về cơ bản đồng nhất.

## 37.12 Đầy đủ hóa của Không gian vectơ định chuẩn (normed vector space)

Dễ hệ quả của Định lý 37.53 và Định lý 37.52 là rằng mọi không gian vectơ định chuẩn (normed vector space) có thể được được nhúng trong đầy đủ không gian vectơ định chuẩn (normed vector space), nghĩa là, Không gian Banach (Banach space).

> **Định lý 37.63.** Nếu $(E, \|\|)$ là không gian vectơ định chuẩn (normed vector space), thì của nó đầy đủ hóa (E,d) như mêtric
$$b b$$
Không gian (ở đâu $E$ là cho trước mêtric d(x, $y) = \|x$ - $y\|)$ có thể được cho trước duy nhất không gian vectơ (vector space) cấu trúc mở rộng không gian vectơ (vector space) cấu trúc trên $E$, và chuẩn (norm) $\|\|_{E}$, sao cho $(E, \|\|_{E})$ là
$$b$$
$$bb$$
Không gian Banach (Banach space), và mêtric $d$ là liên kết với chuẩn (norm) $\|\|_{E}$. Hơn nữa, phép đẳng cự (isometry)
$$b$$
$$b$$
$\phi$: $E \to E$ là tuyến tính phép đẳng cự (isometry).
$$b$$

<!-- PAGE 1429 -->

*Chứng minh.* phép cộng phép toán $+: E \times  E \to E$ là liên tục đều (uniformly continuous) bởi vì
$$\|(u'+ v') -(u''+ v'')\|\le \|u'-u''\|+ \|v'-v''\|.$$
Nó là không khó để chỉ ra rằng $E \times E$ là không gian mêtric đầy đủ và rằng $E \times  E$ là trù mật
$$b b$$
Trong $E \times E$. Thì, theo Định lý 37.52, liên tục đều (uniformly continuous) hàm $+$ có duy nhất $b  b$ liên tục mở rộng $+: E \times E \to E$.
$$b bb$$
Ánh xạ $\cdot$: $\mathbb{R} \times  E \to E$ là không liên tục đều (uniformly continuous), nhưng với mọi cố định $\lambda  \in \mathbb{R}$, ánh xạ $L_{\lambda}$: $E \to E$ cho trước bởi $L_{\lambda}(u) = \lambda  \cdot  u$ là liên tục đều (uniformly continuous), do đó theo Định lý 37.52 hàm $L_{\lambda}$ có duy nhất liên tục mở rộng $L_{\lambda}$: $E \to E$, mà ta sử dụng để định nghĩa vô hướng (scalar)
$$bb$$
Phép nhân $\cdot$: $\mathbb{R} \times E \to E$. Nó là dễ dàng đã kiểm tra rằng với ở trên phép cộng và vô hướng (scalar)
$$bb$$
Phép nhân, $E$ là không gian vectơ (vector space).
$$b$$
Vì chuẩn (norm) $\|\|$ trên $E$ là liên tục đều (uniformly continuous), nó có duy nhất liên tục mở rộng $\|\|_{E}$: $E \to \mathbb{R}_{+}$. các đồng nhất thức $\|u + v\|\le \|u\| + \|v\|$ và $\|\lambda u\|\le |\lambda$ | $\|u\|$ mở rộng đến $E$ bởi $b  b b$ tính liên tục. phương trình
$$d(u, v) = \|u -v\|$$
Cũng mở rộng đến $E$ bởi tính liên tục và cho ta
$$b$$
$$d(\alpha , \beta ) = \|\alpha  -\beta \|_{E},$$
$$b$$
$$b$$
Mà chỉ ra rằng $\|\|_{E}$ là thật vậy chuẩn (norm), và rằng mêtric $d$ là liên kết với nó. Cuối cùng, nó
$$b$$
Là dễ để kiểm chứng $that^{b}$ ánh xạ $\phi$ là tuyến tính. tính duy nhất của cấu trúc của không gian vectơ định chuẩn (normed vector space) suy ra từ tính duy nhất của liên tục các mở rộng trong Định lý 37.52. Định lý 37.63 và Định lý 37.52 sẽ được sử dụng để chỉ ra rằng mọi Không gian Hermite (Hermitian space) có thể được được nhúng trong Không gian Hilbert (Hilbert space). sau đây phiên bản của Định lý 37.52 cho các không gian vectơ định chuẩn là cần thiết trong lý thuyết của phép lấy tích phân.

> **Định lý 37.64.** Cho $E$ và $F$ là hai các không gian vectơ định chuẩn, cho $E_{0}$ là trù mật không gian con của $E$, và cho $f_{0}$: $E_{0} \to F$ là hàm liên tục (continuous function). Nếu $f_{0}$ là liên tục đều (uniformly continuous) và nếu $F$ là đầy đủ, thì tồn tại duy nhất một liên tục đều (uniformly continuous) hàm $f$: $E \to F$ mở rộng $f_{0}$. Hơn nữa, nếu $f_{0}$ là liên tục ánh xạ tuyến tính (linear map), thì $f$ là cũng tuyến tính ánh xạ liên tục (continuous map), và $\|f\| = \|f_{0}\|$.

*Chứng minh.* Ta chỉ cần để chứng minh thứ hai phát biểu. Cho trước bất kỳ hai các vectơ $x, y \in E$, vì $E_{0}$ là trù mật trên $E$ ta có thể chọn các dãy $(x_{n})$ và $(y_{n})$ của các vectơ $x_{n}, y_{n} \in E_{0}$ sao cho $x = lim_{n\mapsto \infty} x_{n}$ và $y = lim_{n\mapsto \infty} y_{n}$. Vì phép cộng và vô hướng (scalar) phép nhân là liên tục, ta thu được
$$x + y = lim(x_{n} + y_{n})$$
$$n\mapsto \infty$$
$$\lambda x = lim(\lambda x_{n})$$
$$n\mapsto \infty$$

<!-- PAGE 1430 -->
Với mọi $\lambda  \in \mathbb{R}$ (hoặc $\lambda  \in \mathbb{C})$. Vì f(x) được định nghĩa bởi
$$f(x) = limf_{0}(x_{n})$$
$$n\mapsto \infty$$
Một cách độc lập của dãy $(x_{n})$ hội tụ đến $x$, và tương tự cho f(y) và f(x $+ y)$, vì $f_{0}$ là tuyến tính, ta có
$$f(x + y) = limf_{0}(x_{n} + y_{n})$$
$$n\mapsto \infty$$
$$= lim(f_{0}(x_{n}) + f_{0}(y_{n}))$$
$$n\mapsto \infty$$
$$= limf_{0}(x_{n}) + limf_{0}(y_{n})$$
$$n\mapsto \infty n\mapsto \infty$$
$$= f(x) + f(y).$$
Tương tự,
$$f(\lambda x) = limf_{0}(\lambda x_{n})$$
$$n\mapsto \infty$$
$$= lim\lambda f_{0}(x_{n})$$
$$n\mapsto \infty$$
$$= \lambda  limf_{0}(x_{n})$$
$$n\mapsto \infty$$
$$= \lambda f(x).$$
Vì vậy, $f$ là tuyến tính. Vì chuẩn (norm) là liên tục, ta có
$$\|f(x)\|= limf_{0}(x_{n}) = lim\|f_{0}(x_{n})\|,$$
$$n\mapsto \infty n\mapsto \infty$$
Và vì $f_{0}$ là liên tục
$$\|f_{0}(x_{n})\|\le \|f_{0}\|\|x_{n}\|for all n \ge 1,$$
Do đó ta thu được
$$lim\|f_{0}(x_{n})\|\le lim\|f_{0}\|\|x_{n}\|for all n \ge 1,$$
$$n\mapsto \infty n\mapsto \infty$$
Rằng là,
$$\|f(x)\|\le \|f_{0}\|\|x\|.$$
Vì
$$\|f\|=\sup\|f(x)\|,$$
$$\|x\|=1, x\in E$$
Ta suy ra rằng $\|f\|\le \|f_{0}\|$. Nhưng vì $E_{0} \subseteq E$ và $f$ agrees với $f_{0}$ trên $E_{0}$, ta cũng có
$$\|f_{0}\|=\sup\|f_{0}(x)\|=\sup\|f(x)\|\le \sup\|f(x)\|= \|f\|,$$
$$\|x\|=1, x\in E0\|x\|=1, x\in E0\|x\|=1, x\in E$$
Và do đó $\|f\| = \|f_{0}\|$. Cuối cùng, ta xét được chuẩn (norm) các không gian afin.
