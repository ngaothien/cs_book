# Tập 1: Các Phương pháp Định lượng (*Quantitative Methods*)
## Học phần 10: Hồi quy Tuyến tính Đơn (*Simple Linear Regression*)
### Phần 6/6: Lời giải Bài tập Thực hành (Trang PDF 330–334)

---

<!-- PDF Page 330 -->

# **LỜI GIẢI (*SOLUTIONS*)**

1. **C đúng.** Giá trị dự báo của $\text{ROE} = 4 + (1.8 \times 10) = 22$.

2. **A đúng.** Hệ số góc bằng $1.8$ là mức thay đổi kỳ vọng trong biến phụ thuộc ($\text{ROE}$) ứng với một đơn vị thay đổi trong biến độc lập ($\text{GO}$).

3. **B đúng.** Giá trị dự báo là $\text{ROE} = 4 + (1.8 \times 8) = 18.4$. Giá trị quan sát được của $\text{ROE}$ là $21$, vì vậy phần dư là $2.6 = 21.0 - 18.4$.

4. **C đúng.** Phương sai sai số không đổi (*Homoskedasticity*) là tình huống trong đó phương sai của phần dư là không đổi qua các quan sát.

5. **A đúng.** $\text{SHIFT}$ là một biến chỉ báo (*indicator variable*) hay biến giả (*dummy variable*) bởi vì nó chỉ nhận các giá trị 0 và 1.

6. **A đúng.** Trong một hồi quy đơn với một biến chỉ báo duy nhất, hệ số chặn là giá trị trung bình của biến phụ thuộc khi biến chỉ báo nhận giá trị bằng 0, tức là trước khi thay đổi chính sách trong trường hợp này.

7. **C đúng.** Trong khi hệ số chặn là trung bình của biến phụ thuộc khi biến chỉ báo bằng 0 (tức là trước khi thay đổi chính sách), thì hệ số góc là mức chênh lệch trong giá trị trung bình của biến phụ thuộc từ trước sang sau khi thay đổi chính sách.

8. **A đúng.** Giả thuyết không về việc không có sự khác biệt trong tốc độ tăng trưởng hàng năm bị bác bỏ tại mức ý nghĩa $0.05$: Thống kê kiểm định tính được là $-8.16188$ nằm ngoài phạm vi $\pm 2.048$.

9. **A đúng.** Hệ số xác định (*coefficient of determination*) chính là $R^2$, bằng $0.7436$ trong bảng.

10. **C đúng.** Bởi vì hệ số góc dương, hệ số tương quan giữa $X$ và $Y$ đơn giản là căn bậc hai của hệ số xác định: $\sqrt{0.7436} = 0.8623$.

11. **C đúng.** Để đưa ra dự báo bằng mô hình hồi quy, hãy nhân hệ số góc với giá trị dự báo của biến độc lập và cộng kết quả với hệ số chặn. Giá trị kỳ vọng của tỷ lệ CFO trên doanh thu $= 0.077 + (0.826 \times 5) = 4.207$.

12. **C đúng.** Trị số $p$ (*$p$-value*) là mức ý nghĩa nhỏ nhất mà tại đó các giả thuyết không liên quan đến hệ số góc có thể bị bác bỏ. Trong trường hợp này, trị số $p$ nhỏ hơn $0.05$, và do đó hồi quy của tỷ lệ dòng tiền từ hoạt động kinh doanh trên doanh thu theo tỷ lệ lợi nhuận ròng trên doanh thu có ý nghĩa thống kê tại mức 5%.

13. **A đúng.** Dữ liệu là các quan sát theo thời gian (*observations over time*).

14. **C đúng.** Từ phương trình hồi quy, Tỷ suất sinh lợi kỳ vọng $= 0.0138 + (-0.6486 \times -0.01) = 0.0138 + 0.006486 = 0.0203$, hay 2,03%.

15. **C đúng.** $R^2$ là hệ số xác định. Trong trường hợp này, nó cho thấy 2,11% sự biến thiên trong tỷ suất sinh lợi của Stellar được giải thích bởi những thay đổi trong CPIENG.

16. **B đúng.** Sai số chuẩn của ước lượng (*standard error of the estimate*) là độ lệch chuẩn của các phần dư hồi quy (*regression residuals*).

17. **C là câu trả lời đúng** bởi vì đây là một phát biểu sai. Hệ số góc và hệ số chặn đều khác 0 một cách có ý nghĩa thống kê tại mức ý nghĩa $0.05$.

<!-- PDF Page 331 -->

18. **C đúng.** Hệ số góc (được trình bày trong Bảng 2) là số âm.

19. **B đúng.** Hiệp phương sai mẫu được tính như sau:

$$\frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n - 1} = -9.2430 \div 49 = -0.1886$$

20. **A đúng.** Trong hồi quy đơn, $R^2$ là bình phương của hệ số tương quan cặp. Bởi vì hệ số góc âm, hệ số tương quan là giá trị âm của căn bậc hai của $0.0933$, hay $-0.3055$ (gần nhất với $-0.3054$).

21. **C đúng.** Không thể rút ra các kết luận về quan hệ nhân quả (*causation*); chỉ có thể rút ra kết luận về mối liên hệ (*association*); do đó, Cách diễn giải 1 và 2 là không chính xác.

22. **C đúng.** Liu giải thích sự biến thiên của tỷ lệ bán khống (*short interest ratio*) bằng cách sử dụng sự biến thiên của tỷ lệ nợ (*debt ratio*).

23. **A đúng.** Bậc tự do bằng số lượng quan sát trừ đi số lượng tham số được ước lượng, bằng 2 trong trường hợp này (hệ số chặn và hệ số góc). Số bậc tự do là $50 - 2 = 48$.

24. **B đúng.** Thống kê $t$ là $-2.2219$, nằm ngoài phạm vi được tạo bởi các giá trị $t$ tới hạn là $\pm 2.011$ cho kiểm định hai phía với mức ý nghĩa 5%. Giá trị $2.011$ là giá trị $t$ tới hạn cho mức ý nghĩa 5% (2,5% ở một phía) đối với 48 bậc tự do. A không chính xác vì giá trị trung bình của tỷ lệ bán khống là $192.3 \div 50 = 3.846$. C không chính xác vì tỷ lệ nợ giải thích 9,33% sự biến thiên của tỷ lệ bán khống.

25. **A đúng.** Giá trị dự báo của tỷ lệ bán khống $= 5.4975 + (-4.1589 \times 0.40) = 5.4975 - 1.6636 = 3.8339$.

26. **C đúng.** Phép tính là:

$$F = \frac{\text{Trung bình bình phương hồi quy (MSR)}}{\text{Trung bình bình phương sai số (MSE)}} = \frac{38.4404}{7.7867} = 4.9367$$

27. **A đúng.** Chúng ta không bác bỏ giả thuyết không về hệ số góc bằng 1, và chúng ta không bác bỏ giả thuyết không về hệ số chặn bằng 0. Kiểm định hệ số góc bằng $1.0$ là:

$$t = \frac{0.9830 - 1.000}{0.0155} = -1.09677$$

Kiểm định hệ số chặn bằng $0.0$ là:

$$t = \frac{0.0001 - 0.0000}{0.0002} = 0.5000$$

Do đó, chúng ta kết luận rằng các dự báo là không chệch (*unbiased*).

28. **A đúng.** Khoảng dự báo cho lạm phát được tính theo ba bước:

- *Bước 1.* Đưa ra dự báo khi biết dự báo US CPI là $2.8$:

$$\hat{Y} = \hat{b}_0 + \hat{b}_1 X = 0.0001 + (0.9830 \times 2.8) = 2.7525$$

- *Bước 2.* Tính phương sai của sai số dự báo:

<!-- PDF Page 332 -->

$$s_f^2 = s_e^2 \left\{ 1 + (1/n) + \frac{(X_f - \bar{X})^2}{(n - 1) \times s_X^2} \right\}$$

$$s_f^2 = 0.0009^2 \left\{ 1 + (1/60) + \frac{(2.8 - 1.3350)^2}{(60 - 1) \times 0.7539^2} \right\}$$

$$s_f^2 = 0.00000088 \implies s_f = 0.0009$$

- *Bước 3.* Tính khoảng dự báo:

$$\hat{Y} \pm t_c \times s_f = 2.7525 \pm (2.0 \times 0.0009)$$

- Cận dưới (*Lower bound*): $2.7525 - (2.0 \times 0.0009) = 2.7506$.

- Cận trên (*Upper bound*): $2.7525 + (2.0 \times 0.0009) = 2.7544$.

Với dự báo US CPI là $2.8$, khoảng dự báo 95% là từ $2.7506$ đến $2.7544$.

29. **B đúng.** Mức độ tin cậy ảnh hưởng đến độ rộng của khoảng dự báo thông qua giá trị $t$ tới hạn được sử dụng để tính khoảng cách từ giá trị dự báo (và bản thân khoảng dự báo cũng phụ thuộc vào giá trị dự báo $X_f$ thông qua $(X_f - \bar{X})^2$). Do đó, Nhận xét 1 không chính xác. Nhận xét 2 chính xác: Sai số chuẩn của ước lượng ($s_e$) càng lớn thì sai số chuẩn của dự báo ($s_f$) càng lớn, dẫn đến khoảng dự báo rộng hơn.

30. **C đúng.** Các giả định của mô hình hồi quy tuyến tính là (1) mối quan hệ giữa biến phụ thuộc và biến độc lập là tuyến tính theo các tham số $b_0$ và $b_1$, (2) các phần dư độc lập với nhau, (3) phương sai của hạng tử sai số là như nhau đối với tất cả các quan sát, và (4) hạng tử sai số có phân phối chuẩn. Giả định 3 không chính xác bởi vì biến phụ thuộc không nhất thiết phải có phân phối chuẩn.

31. **B đúng.** Sai số chuẩn của ước lượng cho mô hình hồi quy tuyến tính với một biến độc lập được tính bằng căn bậc hai của trung bình bình phương sai số:

$$s_e = \sqrt{\frac{0.071475}{34}} = 0.04585$$

32. **C đúng.** Tỷ suất sinh lợi dầu thô giải thích tỷ suất sinh lợi cổ phiếu Amtex nếu hệ số góc khác 0 một cách có ý nghĩa thống kê. Hệ số góc là $0.2354$, và thống kê $t$ tính được là:

$$t = \frac{0.2354 - 0.0000}{0.0760} = 3.0974$$

nằm ngoài phạm vi của các giá trị tới hạn là $\pm 2.728$.

Do đó, Vasileva nên bác bỏ giả thuyết không cho rằng tỷ suất sinh lợi dầu thô không giải thích được tỷ suất sinh lợi cổ phiếu Amtex, bởi vì hệ số góc khác 0 một cách có ý nghĩa thống kê.

A không chính xác vì thống kê $t$ tính được để kiểm định hệ số góc so với $0.15$ là $t = \frac{0.2354 - 0.1500}{0.0760} = 1.1237$, nhỏ hơn giá trị tới hạn $+2.441$. B không chính xác vì thống kê $t$ tính được là $t = \frac{0.0095 - 0.0000}{0.0078} = 1.2179$, nhỏ hơn giá trị tới hạn $+2.441$.

33. **B đúng.** Giá trị dự báo của biến phụ thuộc, tỷ suất sinh lợi cổ phiếu Amtex, khi biết giá trị của biến độc lập, tỷ suất sinh lợi dầu thô là $-0.01$, được tính

<!-- PDF Page 333 -->

bằng $\hat{Y} = \hat{b}_0 + \hat{b}_1 X_i = 0.0095 + [0.2354 \times (-0.01)] = 0.0071$.

34. **C đúng.** Tỷ suất sinh lợi cổ phiếu dự báo là $0.0095 + [0.2354 \times (-0.01)] = 0.0071$. Khoảng dao động là $t_c \times s_f = 2.728 \times 0.0469 = 0.1279$. Giới hạn dưới cho khoảng dự báo là $0.0071 - (2.728 \times 0.0469) = -0.1208$, và giới hạn trên cho khoảng dự báo là $0.0071 + (2.728 \times 0.0469) = 0.1350$.

A không chính xác vì các cận của khoảng dự báo phải dựa trên sai số chuẩn của dự báo và giá trị $t$ tới hạn, chứ không phải dựa trên giá trị trung bình của biến phụ thuộc.

B không chính xác vì các cận của khoảng dự báo dựa trên tích của sai số chuẩn của dự báo *và* giá trị $t$ tới hạn, chứ không chỉ đơn thuần là sai số chuẩn của dự báo.

35. **B đúng.** Hệ số xác định là $102.9152 \div 105.1303 = 0.9789$.

36. **A đúng.** Sai số chuẩn của ước lượng là căn bậc hai của trung bình bình phương sai số, hay $\sqrt{0.0692} = 0.2631$.

37. **B đúng.** Trị số $p$ tương ứng với hệ số góc nhỏ hơn $0.01$, vì vậy chúng ta bác bỏ giả thuyết không về hệ số góc bằng 0, kết luận rằng vòng quay tài sản cố định giải thích logarit tự nhiên của biên lợi nhuận ròng.

38. **C đúng.** Logarit tự nhiên dự báo của biên lợi nhuận ròng là $0.5987 + (2 \times 0.2951) = 1.1889$. Biên lợi nhuận ròng dự báo là $e^{1.1889} = 3.2835\%$.

<!-- PDF Page 334 -->
