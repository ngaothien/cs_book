# Các cơ sở của Các tích tenxơ


<!-- PAGE 1186 -->

## 33.3 Các cơ sở của Các tích tenxơ

Ta đã chỉ ra rằng $E_{1} \otimes \cdots \otimes E_{n}$ được sinh bởi các vectơ của tạo thành $u_{1} \otimes \cdots \otimes u_{n}$. Tuy nhiên, các vectơ này là không độc lập tuyến tính (linearly independent). tình huống này có thể được cố định khi xét các cơ sở. Đến giải thích ý tưởng của chứng minh, xét trường hợp khi ta có hai các không gian $E$ và $F$ cả hai có số chiều $3$. Cho trước cơ sở (basis) $(e_{1}, e_{2}, e_{3})$ của $E$ và cơ sở (basis) $(f_{1}, f_{2}, f_{3})$ của $F$, ta sẽ like để chứng minh rằng $e_{1} \otimes f_{1}, e_{1} \otimes f_{2}, e_{1} \otimes f_{3}, e_{2} \otimes f_{1}, e_{2} \otimes f_{2}, e_{2} \otimes f_{3}, e_{3} \otimes f_{1}, e_{3} \otimes f_{2}, e_{3} \otimes f_{3}$ là độc lập tuyến tính (linearly independent). để chứng minh điều này, nó suffices để chỉ ra rằng với mọi không gian vectơ (vector space) $G$, nếu $w_{11}, w_{12}, w_{13}, w_{21}, w_{22}, w_{23}, w_{31}, w_{32}, w_{33}$ là bất kỳ các vectơ trong $G$, thì có một ánh xạ song tuyến tính (bilinear map) $h: E \times  F \to G$ sao cho
$$h(e_{i}, e_{j}) = w_{ij},1 \le i, j \le 3.$$
Bởi vì $h$ cho ta duy nhất ánh xạ tuyến tính (linear map) $h_{\otimes}: E \otimes F \to G$ sao cho
$$h_{\otimes}(e_{i} \otimes e_{j}) = w_{ij},1 \le i, j \le 3,$$
Và theo Mệnh đề 33.4, các vectơ $e_{1} \otimes f_{1}, e_{1} \otimes f_{2}, e_{1} \otimes f_{3}, e_{2} \otimes f_{1}, e_{2} \otimes f_{2}, e_{2} \otimes f_{3}, e_{3} \otimes f_{1}, e_{3} \otimes f_{2}, e_{3} \otimes f_{3}$ là độc lập tuyến tính (linearly independent). Điều này suggests understanding cách mà song tuyến tính hàm $f$: $E\times F \to G$ được biểu diễn theo của nó các giá trị $f(e_{i}, f_{j})$ trên cơ sở (basis) các vectơ $(e_{1}, e_{2}, e_{3})$ và $(f_{1}, f_{2}, f_{3})$, và điều này có thể được được thực hiện dễ dàng. Bằng cách sử dụng tính song tuyến tính ta thu được $f(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}f_{1} + v_{2}f_{2} + v_{3}f_{3}) = u_{1}v_{1}f(e_{1}, f_{1}) + u_{1}v_{2}f(e_{1}, f_{2}) + u_{1}v_{3}f(e_{1}, f_{3})$
$$+ u_{2}v_{1}f(e_{2}, f_{1}) + u_{2}v_{2}f(e_{2}, f_{2}) + u_{2}v_{3}f(e_{2}, f_{3})$$
$$+ u_{3}v_{1}f(e_{3}, f_{1}) + u_{3}v_{2}f(e_{3}, f_{2}) + u_{3}v_{3}f(e_{3}, f_{3}).$$
Vì vậy, cho trước $w_{11}, w_{12}, w_{13}, w_{21}, w_{22}, w_{23}, w_{31}, w_{32}, w_{33} \in G$, hàm $h$ cho trước bởi
$$h(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}f_{1} + v_{2}f_{2} + v_{3}f_{3}) = u_{1}v_{1}w_{11} + u_{1}v_{2}w_{12} + u_{1}v_{3}w_{13}$$
$$+ u_{2}v_{1}w_{21} + u_{2}v_{2}w_{22} + u_{2}v_{3}w_{23}$$
$$+ u_{3}v_{1}w_{31} + u_{3}v_{2}w_{33} + u_{3}v_{3}w_{33}$$
Là rõ ràng song tuyến tính, và bởi cách xây dựng $h(e_{i}, f_{j}) = w_{ij}$, do đó nó thực hiện job. tổng quát hóa của điều này lập luận đến bất kỳ số của các không gian vectơ của bất kỳ số chiều (chẵn/ngay cả vô hạn) là trực tiếp/dễ dàng.

> **Mệnh đề 33.12.** Cho trước $n \ge 2$ các không gian vectơ $E_{1}, \dots  , E_{n}$, nếu $(u_{i}^{k} )_{i\in Ik}$ là cơ sở (basis) cho $E_{k}, 1 \le k \le n$, thì họ của các vectơ
$$(u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n})_{(i1,...,in)\in I1\times...\times In}$$
Là cơ sở (basis) của tích tenxơ (tensor product) $E_{1} \otimes \cdots  \otimes E_{n}$.
