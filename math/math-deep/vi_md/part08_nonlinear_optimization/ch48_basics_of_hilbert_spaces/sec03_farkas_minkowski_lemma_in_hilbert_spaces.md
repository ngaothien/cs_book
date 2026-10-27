# Farkas–Minkowski Bổ đề trong Các không gian Hilbert


<!-- PAGE 1699 -->

## 48.3 Farkas–Minkowski Bổ đề trong Các không gian Hilbert

Trong mục này $(V, \langle$ -, $-\rangle$) được giả sử là thực Không gian Hilbert (Hilbert space). phép chiếu bổ đề có thể được được sử dụng để chỉ ra thú vị phiên bản của Farkas–Minkowski bổ đề trong Không gian Hilbert (Hilbert space). Cho trước hữu hạn dãy của các vectơ $(a_{1}, \dots  , a_{m})$ với $a_{i} \in V$, cho $C$ là nón đa diện (polyhedral cone)
$$$$
$$C = cone(a_{1}, \dots  , a_{m}) = \sum_{i=1}^{m}  \lambda_{i} a_{i} | \lambda_{i}  \ge 0, i = 1, \dots  , m.$$
Với mọi vectơ $b \in V$, Farkas–Minkowski bổ đề cho tiêu chuẩn cho kiểm tra liệu $b \in C$. Trong Mệnh đề 44.2 ta được chứng minh rằng mọi nón đa diện (polyhedral cone) $cone(a_{1}, \dots  , a_{m})$ với $a_{i} \in \mathbb{R}^{n}$ là đóng. Close examination của chứng minh chỉ ra rằng nó đi qua nếu $a_{i} \in V$ ở đâu $V$ là bất kỳ không gian vectơ (vector space) có thể của vô hạn số chiều, bởi vì quan trọng sự kiện là rằng số $m$ của các vectơ này là hữu hạn, không số chiều của chúng.

> **Định lý 48.12.** (Farkas–Minkowski Bổ đề trong Các không gian Hilbert) Cho $(V, \langle$ -, $-\rangle$) là thực Không gian Hilbert (Hilbert space). Với mọi hữu hạn dãy của các vectơ $(a_{1}, \dots  , a_{m})$ với $a_{i} \in V$, nếu $C$ là nón đa diện (polyhedral cone) $C = cone(a_{1}, \dots  , a_{m})$, với mọi vectơ $b \in V$, ta có $b \in / C$ khi và chỉ khi có một vectơ $u \in V$ sao cho
$$\langle a_{i}, u\rangle \ge 0i = 1, \dots  , m,and\langle b, u\rangle < 0.$$
Tương đương, $b \in C$ khi và chỉ khi với mọi $u \in V$,
$$if \langle a_{i}, u\rangle \ge 0i = 1, \dots  , m,then\langle b, u\rangle \ge 0.$$

*Chứng minh.* Ta suy ra Ciarlet $[41]$ (Chương $9$, Định lý 9.1.1). Ta đã được thiết lập trong Mệnh đề 44.2 rằng nón đa diện (polyhedral cone) $C = cone(a_{1}, \dots  , a_{m})$ là đóng. Tiếp theo ta khẳng định sau đây: Khẳng định: Nếu $C$ là khác rỗng, đóng, lồi tập con của Không gian Hilbert (Hilbert space) $V$, và $b \in V$ là bất kỳ vectơ sao cho $b \in / C$, thì ở đó tồn tại một số $u \in V$ và một cách vô hạn nhiều các vô hướng $\alpha  \in \mathbb{R}$ sao cho
$$\langle v, u\rangle > \alpha for every v \in C$$
$$\langle b, u\rangle < \alpha .$$
Ta sử dụng phép chiếu bổ đề (Mệnh đề 48.5) mà nói rằng rằng vì $b \in / C$ tồn tại một duy nhất $c = p_{C}(b) \in C$ sao cho
$$\|b -c\|= \inf \|b -v\|> 0$$
$$v\in C$$
$$\langle b -c, v -c\rangle \le 0for all v \in C,$$
