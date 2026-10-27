# Các siêu phẳng và Các dạng tuyến tính


<!-- PAGE 435 -->

## 11.5 Các siêu phẳng và Các dạng tuyến tính

Thực sự Mệnh đề 11.7 ở dưới suy ra từ Các phần $(c)$ và $(d)$ của Định lý 11.4, nhưng ta feel rằng nó là cũng thú vị đến cho nhiều hơn/thêm chứng minh trực tiếp.

> **Mệnh đề 11.7.** Cho $E$ là không gian vectơ (vector space). Các tính chất sau đây đúng:
() Cho trước bất kỳ khác không dạng tuyến tính (linear form) $f^{*} \in E^{*}$, của nó hạt nhân (kernel) $H =$ Ker $f^{*}$ là siêu phẳng (hyperplane).
$(b)$ Với mọi siêu phẳng (hyperplane) $H$ trong $E$, có một (khác không) dạng tuyến tính (linear form) $f^{*} \in E^{*}$ sao cho $H =$ Ker $f^{*}$.
$(c)$ Cho trước bất kỳ siêu phẳng (hyperplane) $H$ trong $E$ và bất kỳ (khác không) dạng tuyến tính (linear form) $f^{*} \in E^{*}$ sao cho $H =$ Ker $f^{*}$, với mọi dạng tuyến tính (linear form) $g^{*} \in E^{*}, H =$ Ker $g^{*}$ khi và chỉ khi $g^{*} = \lambda f^{*}$ với một số $\lambda  \neq  0$ trong $K$.

*Chứng minh.* () Nếu $f^{*} \in E^{*}$ là khác không, tồn tại một vectơ $v_{0} \in E$ sao cho $f^{*} (v_{0}) \neq  0$. Cho $H =$ Ker $f^{*}$. Với mọi $v \in E$, ta có
$$f^{*} \begin{pmatrix} f^{*}(v) \\ v - & v_{0} \\ f^{*}(v_{0}) \end{pmatrix} = f^{*} (v) - \frac{f^{*}(v)}{f^{*}(v_{0})} f^{*}(v_{0}) = f^{*}(v) -f^{*}(v) = 0.$$
Do đó,
$$v - \frac{f^{*}(v)}{f^{*}(v_{0})} v_{0} = h \in H,$$
Và
$$v = h + \frac{f^{*}(v)}{f^{*}(v_{0})} v_{0},$$
Rằng là, $E = H + Kv_{0}$. Cũng vì $f^{*} (v_{0}) \neq  0$, ta có $v_{0} \in / H$, nghĩa là, $H \cap Kv_{0} = 0$. Do đó, $E = H \oplus Kv_{0}$, và $H$ là siêu phẳng (hyperplane).
$(b)$ Nếu $H$ là siêu phẳng (hyperplane), $E = H \oplus Kv_{0}$ với một số $v_{0} \in / H$. Thì mọi $v \in E$ có thể được được viết trong duy nhất cách như $v = h + \lambda v_{0}$. Do đó có một xác định tốt (well-defined) hàm $f^{*}$: $E \to K$, sao cho, $f^{*} (v) = \lambda$, với mọi $v = h + \lambda v_{0}$. Ta để lại như đơn giản bài tập verification rằng $f^{*}$ là dạng tuyến tính (linear form). Vì $f^{*} (v_{0}) = 1$, dạng tuyến tính (linear form) $f^{*}$ là khác không. Cũng, theo Định nghĩa, rõ ràng là $\lambda  = 0$ khi và chỉ khi $v \in H$, nghĩa là, Ker $f^{*} = H$.
$(c)$ Cho $H$ là siêu phẳng (hyperplane) trong $E$, và cho $f^{*} \in E^{*}$ là bất kỳ (khác không) dạng tuyến tính (linear form) sao cho $H =$ Ker $f^{*}$. Rõ ràng, nếu $g^{*} = \lambda f^{*}$ với một số $\lambda  \neq  0$, thì $H =$ Ker $g^{*}$. Ngược lại, giả sử rằng $H =$ Ker $g^{*}$ với một số khác không dạng tuyến tính (linear form) $g^{*}$. Từ (), ta có $E = H \oplus Kv_{0}$, với một số $v_{0}$ sao cho $f^{*} (v_{0}) \neq  0$ và $g^{*}(v_{0}) \neq  0$. Thì nhận thấy rằng
$$g^{*}- \frac{g^{*}(v_{0})}{f^{*}(v_{0})} f^{*}$$
Là dạng tuyến tính (linear form) rằng triệt tiêu trên $H$, vì cả hai $f^{*}$ và $g^{*}$ triệt tiêu trên $H$, nhưng cũng triệt tiêu trên $Kv_{0}$. Do đó, $g^{*} = \lambda f^{*}$, với
$$\lambda  = \frac{g^{*}(v_{0})}{f^{*}(v_{0})} .$$
