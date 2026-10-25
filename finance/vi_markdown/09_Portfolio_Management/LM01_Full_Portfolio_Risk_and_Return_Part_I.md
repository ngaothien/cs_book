# Tập 9: Quản lý Danh mục Đầu tư (Portfolio Management)
## Learning Module 1 Portfolio Risk and Return: Part I (Trang PDF 13–70)

---

# Tập 9: Quản lý Danh mục Đầu tư (*Portfolio Management*)
## Học phần 1: Rủi ro và Lợi nhuận Danh mục Đầu tư: Phần I (*Portfolio Risk and Return: Part I*)
### Phần 1/4: Giới thiệu (*Introduction*) (Trang PDF 13–27)

---

<!-- PDF Page 13 -->

#### H Ọ C P H Ầ N

# **<mark>1</mark>**

### **Rủi ro và Lợi nhuận Danh mục Đầu tư: Phần I (*Portfolio Risk and Return: Part I*)**

**bởi Vijay Singal, PhD, CFA.**

_Vijay Singal, PhD, CFA, công tác tại Virginia Tech (Hoa Kỳ)._

###### **<mark>MỤC TIÊU HỌC TẬP (*LEARNING OUTCOMES*)</mark>**

|**_Mức độ thành thạo_**|**_Ứng viên cần có khả năng:_**|
|---|---|
||mô tả đặc điểm của các nhóm tài sản chính (*major asset classes*) mà nhà đầu tư xem xét khi hình thành danh mục đầu tư|
||giải thích sự ngại rủi ro (*risk aversion*) và các hàm ý của nó đối với việc lựa chọn danh mục đầu tư (*portfolio selection*)|
||giải thích việc lựa chọn danh mục đầu tư tối ưu (*optimal portfolio*), khi biết độ hữu dụng (*utility*) (hoặc mức độ ngại rủi ro) của nhà đầu tư và đường phân bổ vốn (*capital allocation line* – CAL)|
||tính toán và diễn giải giá trị trung bình (*mean*), phương sai (*variance*), và hiệp phương sai (*covariance*) (hoặc hệ số tương quan – *correlation*) của tỷ suất sinh lợi tài sản dựa trên dữ liệu lịch sử|
||tính toán và diễn giải độ lệch chuẩn của danh mục đầu tư (*portfolio standard deviation*)|
||mô tả tác động lên rủi ro của danh mục đầu tư khi đầu tư vào các tài sản có tương quan nhỏ hơn mức tương quan hoàn hảo (*less than perfectly correlated*)|
||mô tả và diễn giải đường biên phương sai tối thiểu (*minimum-variance frontier*) và đường biên hiệu quả (*efficient frontier*) của các tài sản rủi ro cùng với danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*)|

##### **GIỚI THIỆU (*INTRODUCTION*)**

## **<mark>1</mark>**

Xây dựng một danh mục đầu tư tối ưu (*optimal portfolio*) là một mục tiêu quan trọng đối với nhà đầu tư. Trong bài đọc này, chúng ta sẽ khám phá quy trình xem xét các đặc điểm rủi ro và lợi nhuận (*risk and return characteristics*) của từng tài sản riêng lẻ, tạo lập tất cả các danh mục đầu tư khả thi, lựa chọn những danh mục đầu tư hiệu quả nhất (*most efficient portfolios*), và cuối cùng là chọn ra danh mục đầu tư tối ưu phù hợp với từng cá nhân cụ thể.

Trong quá trình xây dựng danh mục đầu tư tối ưu, một số yếu tố và đặc điểm đầu tư sẽ được xem xét. Quan trọng nhất trong số các yếu tố đó là rủi ro và lợi nhuận của từng tài sản riêng lẻ đang được cân nhắc. Mối tương quan (*correlations*) giữa các tài sản riêng lẻ cùng với rủi ro và lợi nhuận là những yếu tố quyết định quan trọng đối với rủi ro của danh mục đầu tư (*portfolio risk*). Việc tạo lập một danh mục đầu tư cho nhà đầu tư đòi hỏi sự thấu hiểu về hồ sơ rủi ro (*risk profile*) của nhà đầu tư đó. Mặc dù chúng ta sẽ không thảo luận về quy trình xác định mức độ ngại rủi ro (*risk aversion*) cho các nhà đầu tư cá nhân hoặc tổ chức, nhưng việc thu thập thông tin như vậy là cần thiết để đưa ra một


<!-- PDF Page 14 -->

## **<mark>2</mark>**

quyết định có đầy đủ cơ sở thông tin. Trong bài đọc này, chúng ta sẽ giải thích các nhóm nhà đầu tư chính và cách thức sở thích rủi ro – lợi nhuận (*risk–return preferences*) của họ có thể được chuẩn hóa thành mô hình để lựa chọn danh mục đầu tư tối ưu từ vô số danh mục đầu tư nằm trong tập hợp cơ hội đầu tư (*investment opportunity set*).

Bài đọc được cấu trúc như sau: Phần 2–3 thảo luận về các đặc điểm đầu tư của tài sản. Phần 4–6 thảo luận về sự ngại rủi ro (*risk aversion*) và cách thức xây dựng các đường bàng quan (*indifference curves*) – công cụ kết hợp sở thích cá nhân của nhà đầu tư. Các đường bàng quan này sau đó được áp dụng vào việc lựa chọn một danh mục đầu tư tối ưu sử dụng hai tài sản rủi ro. Phần 7–9 cung cấp kiến thức và cách tính toán rủi ro danh mục đầu tư. Vai trò của hệ số tương quan (*correlation*) và việc đa dạng hóa rủi ro danh mục đầu tư (*diversification of portfolio risk*) được xem xét chi tiết. Phần 10–12 bắt đầu với các tài sản rủi ro hiện có cho nhà đầu tư và xây dựng một số lượng lớn các danh mục đầu tư rủi ro. Phần này minh họa quy trình thu hẹp các lựa chọn thành một tập hợp hiệu quả các danh mục đầu tư rủi ro (*efficient set of risky portfolios*) trước khi xác định danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*). Danh mục đầu tư rủi ro này được kết hợp với sở thích rủi ro của nhà đầu tư để tạo ra danh mục đầu tư tối ưu của nhà đầu tư (*investor's optimal portfolio*). Một phần tóm tắt sẽ khép lại bài đọc này.

##### **LỢI NHUẬN VÀ RỦI RO LỊCH SỬ (*HISTORICAL RETURN AND RISK*)**

mô tả đặc điểm của các nhóm tài sản chính (*major asset classes*) mà nhà đầu tư xem xét khi hình thành danh mục đầu tư

Trước khi xem xét dữ liệu lịch sử, việc phân biệt giữa tỷ suất sinh lợi trung bình lịch sử (*historical mean return*) và tỷ suất sinh lợi kỳ vọng (*expected return*) là rất hữu ích; đây là hai khái niệm rất khác nhau nhưng lại dễ gây nhầm lẫn. Lợi nhuận lịch sử (*historical return*) là những gì thực tế đã kiếm được trong _quá khứ_, trong khi lợi nhuận kỳ vọng (*expected return*) là những gì nhà đầu tư dự kiến sẽ kiếm được trong _tương lai_.

Tỷ suất sinh lợi kỳ vọng (*expected return*) là tỷ suất sinh lợi danh nghĩa (*nominal return*) khiến nhà đầu tư cận biên (*marginal investor*) quyết định đầu tư vào một tài sản dựa trên lãi suất phi rủi ro thực (*real risk-free interest rate*, $r_{rF}$), lạm phát kỳ vọng (*expected inflation*, $E(\pi)$), và phần bù rủi ro kỳ vọng (*expected risk premium*) cho rủi ro của tài sản đó [$E(RP)$]. Lãi suất phi rủi ro thực được kỳ vọng là số dương như một khoản đền bù cho việc trì hoãn tiêu dùng. Tương tự, phần bù rủi ro được kỳ vọng là số dương trong hầu hết các trường hợp.<sup>1</sup> Tỷ lệ lạm phát kỳ vọng nhìn chung là số dương, ngoại trừ khi nền kinh tế đang trong tình trạng giảm phát (*deflationary state*) và giá cả đang giảm xuống. Do đó, tỷ suất sinh lợi kỳ vọng nhìn chung là số dương. Mối quan hệ giữa tỷ suất sinh lợi kỳ vọng và lãi suất phi rủi ro thực, tỷ lệ lạm phát, cùng phần bù rủi ro có thể được biểu diễn bằng phương trình sau:

$$1 + E(R) = (1 + r_{rF}) \times [1 + E(\pi)] \times [1 + E(RP)]$$

Tuy nhiên, tỷ suất sinh lợi trung bình lịch sử (*historical mean return*) đối với khoản đầu tư vào một tài sản cụ thể lại được thu thập từ tỷ suất sinh lợi thực tế (*actual return*) mà nhà đầu tư đã kiếm được. Bởi vì khoản đầu tư có rủi ro, không có gì đảm bảo rằng lợi nhuận thực tế sẽ bằng với lợi nhuận kỳ vọng. Trên thực tế, rất khó có khả năng hai mức lợi nhuận này bằng nhau trong một khoảng thời gian cụ thể đang được xem xét. Với một khoảng thời gian đủ dài, chúng ta có thể _kỳ vọng_ rằng tỷ suất sinh lợi tương lai (kỳ vọng) sẽ bằng với tỷ suất sinh lợi lịch sử trung bình. Thật không may, chúng ta không biết khoảng thời gian đó dài bao lâu—10 năm, 50 năm, hay 100 năm. Trên thực tế, chúng ta thường giả định rằng tỷ suất sinh lợi trung bình lịch sử là một đại diện thỏa đáng cho tỷ suất sinh lợi kỳ vọng, mặc dù giả định này có thể không chính xác. Ví dụ, Bảng minh họa 1 (*Exhibit 1*) cho thấy tỷ suất sinh lợi cổ phiếu lịch sử trong tám năm qua (2010–2017) đối với cổ phiếu các công ty lớn của Hoa Kỳ là dương trong khi tỷ suất sinh lợi thực tế lại âm trong thập kỷ trước đó, nhưng nhìn chung gần như luôn luôn dương trong lịch sử. Tuy nhiên, tỷ suất sinh lợi dài hạn hơn

> 1 Có những ngoại lệ khi một tài sản làm giảm rủi ro tổng thể của danh mục đầu tư. Chúng ta sẽ xem xét những ngoại lệ đó trong Phần 9.


<!-- PDF Page 15 -->

(1926–2017) là dương và có thể nhất quán với tỷ suất sinh lợi kỳ vọng. Mặc dù chưa rõ liệu tỷ suất sinh lợi trung bình lịch sử có đại diện chính xác cho tỷ suất sinh lợi kỳ vọng hay không, đây vẫn là một giả định thường được đưa ra.

**Bảng minh họa 1: Rủi ro và Lợi nhuận của các Nhóm Tài sản tại Hoa Kỳ theo Thập kỷ (%)**

|**Nhóm tài sản (*Asset Class*)**|**Chỉ tiêu**|**1930s**|**1940s**|**1950s**|**1960s**|**1970s**|**1980s**|**1990s**|**2000s**|**2010s***|**1926–2017**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Cổ phiếu công ty lớn (*Large company stocks*)|Lợi nhuận (*Return*)|−0.1|9.2|19.4|7.8|5.9|17.6|18.2|−1.0|13.9|10.2|
||Rủi ro (*Risk*)|41.6|17.5|14.1|13.1|17.2|19.4|15.9|16.3|13.6|19.8|
|Cổ phiếu công ty nhỏ (*Small company stocks*)|Lợi nhuận (*Return*)|1.4|20.7|16.9|15.5|11.5|15.8|15.1|6.3|14.8|12.1|
||Rủi ro (*Risk*)|78.6|34.5|14.4|21.5|30.8|22.5|20.2|26.1|19.4|31.7|
|Trái phiếu doanh nghiệp dài hạn (*Long-term corporate bonds*)|Lợi nhuận (*Return*)|6.9|2.7|1|1.7|6.2|13|8.4|7.7|8.3|6.1|
||Rủi ro (*Risk*)|5.3|1.8|4.4|4.9|8.7|14.1|6.9|11.7|8.8|8.3|
|Trái phiếu chính phủ dài hạn (*Long-term government bonds*)|Lợi nhuận (*Return*)|4.9|3.2|−0.1|1.4|5.5|12.6|8.8|7.7|6.8|5.5|
||Rủi ro (*Risk*)|5.3|2.8|4.6|6|8.7|16|8.9|12.4|10.8|9.9|
|Tín phiếu Kho bạc (*Treasury bills*)|Lợi nhuận (*Return*)|0.6|0.4|1.9|3.9|6.3|8.9|4.9|2.8|0.2|3.4|
||Rủi ro (*Risk*)|0.2|0.1|0.2|0.4|0.6|0.9|0.4|0.6|0.1|3.1|
|Lạm phát (*Inflation*)|Lợi nhuận (*Return*)|−2.0|5.4|2.2|2.5|7.4|5.1|2.9|2.5|1.7|2.9|
||Rủi ro (*Risk*)|2.5|3.1|1.2|0.7|1.2|1.3|0.7|1.6|1.1|4.0|

_* Tính đến ngày 31 tháng 12 năm 2017. Lưu ý:_ Lợi nhuận được đo lường bằng tỷ suất sinh lợi trung bình nhân hàng năm (*annualized geometric mean returns*). _Rủi ro được đo lường bằng cách chuẩn hóa theo năm các độ lệch chuẩn hàng tháng. Nguồn:_ Niên giám SBBI 2018 (Bảng 1.2, 1.3, 2.3 và 6.2).

Trong phần tiếp theo, hãy lưu ý phân biệt rõ giữa tỷ suất sinh lợi kỳ vọng và tỷ suất sinh lợi trung bình lịch sử. Chúng tôi sẽ lưu ý người đọc bất cứ khi nào tỷ suất sinh lợi lịch sử được sử dụng để ước tính tỷ suất sinh lợi kỳ vọng.

###### **Tỷ suất sinh lợi danh nghĩa của các nhóm tài sản chính tại Hoa Kỳ (*Nominal Returns of Major US Asset Classes*)**

Chúng ta tập trung vào ba danh mục tài sản chính trong Bảng minh họa 1: cổ phiếu (*stocks*), trái phiếu (*bonds*), và tín phiếu Kho bạc (*T-bills*). Tỷ suất sinh lợi danh nghĩa trung bình của các nhóm tài sản tại Hoa Kỳ được báo cáo theo từng thập kỷ kể từ những năm 1930. Tổng hợp cho giai đoạn 1926–2017 nằm ở cột cuối cùng. Tất cả các mức lợi nhuận đều là tỷ suất sinh lợi trung bình nhân hàng năm (*annual geometric mean returns*). Cổ phiếu công ty lớn có tỷ suất sinh lợi hàng năm tổng thể là 10,2% trong suốt giai đoạn 92 năm. Tỷ suất sinh lợi này âm vào những năm 1930 và những năm 2000, và dương trong tất cả các thập kỷ còn lại. Những năm 1950 và 1990 là những thập kỷ tốt nhất đối với cổ phiếu công ty lớn. Cổ phiếu công ty nhỏ thậm chí còn có kết quả tốt hơn. Tỷ suất sinh lợi danh nghĩa chưa bao giờ âm trong bất kỳ thập kỷ nào, và có mức tăng trưởng hai chữ số trong tất cả các thập kỷ ngoại trừ hai thập kỷ, dẫn đến tỷ suất sinh lợi hàng năm tổng thể trong 92 năm đạt 12,1%.

Trái phiếu doanh nghiệp dài hạn (*long-term corporate bonds*) và trái phiếu chính phủ dài hạn (*long-term government bonds*) đạt tỷ suất sinh lợi tổng thể lần lượt là 6,1% và 5,5%. Trái phiếu doanh nghiệp không có một thập kỷ nào mang lại lợi nhuận âm, mặc dù trái phiếu chính phủ ghi nhận mức lợi nhuận âm vào những năm 1950 khi cổ phiếu đang hoạt động cực kỳ tốt. Trái phiếu cũng có một số thập kỷ xuất sắc, đạt mức lợi nhuận hai chữ số vào những năm 1980 và 2000.

Tín phiếu Kho bạc (*Treasury bills* – chứng khoán chính phủ ngắn hạn) không có lợi nhuận âm trong bất kỳ thập kỷ nào. Trên thực tế, tín phiếu Kho bạc chỉ có lợi nhuận âm vào năm 1938 (–0,02%) khi tỷ lệ lạm phát là –2,78%. Tỷ suất sinh lợi dương nhất quán đối với tín phiếu Kho bạc không có gì đáng ngạc nhiên bởi vì lãi suất danh nghĩa (*nominal interest rates*) hầu như không bao giờ


<!-- PDF Page 16 -->

âm và tín phiếu Kho bạc chịu rất ít rủi ro lãi suất (*interest rate risk*) hoặc rủi ro lạm phát (*inflation risk*). Kể từ cuộc Đại Suy thoái (*Great Depression*), không có sự giảm phát nào trong bất kỳ thập kỷ nào, mặc dù tỷ lệ lạm phát ở mức âm rất sâu vào năm 1930 (–6,03%), năm 1931 (–9,52%), và năm 1932 (–10,30%). Ngược lại, tỷ lệ lạm phát rất cao vào cuối những năm 1970 và đầu những năm 1980, lên tới 13,31% vào năm 1979. Tỷ lệ lạm phát phần lớn dao động trong biên độ từ 1% đến 3% từ năm 1991 đến năm 2017. Nhìn chung, tỷ lệ lạm phát là 2,9% trong giai đoạn 92 năm.

###### **Tỷ suất sinh lợi thực của các nhóm tài sản chính tại Hoa Kỳ (*Real Returns of Major US Asset Classes*)**

Bởi vì tỷ lệ lạm phát hàng năm có thể biến động rất lớn, từ –10,30% đến +13,31% trong 92 năm qua, việc so sánh giữa các giai đoạn thời gian khác nhau bằng cách sử dụng tỷ suất sinh lợi danh nghĩa là rất khó khăn và dễ gây hiểu lầm. Do đó, việc dựa vào tỷ suất sinh lợi thực (*real returns*) sẽ hiệu quả hơn. Tỷ suất sinh lợi thực của cổ phiếu, trái phiếu, và tín phiếu Kho bạc được báo cáo từ năm 1900 trong Bảng minh họa 2 và Bảng minh họa 3.

**Bảng minh họa 2: Lợi nhuận tích lũy của các Nhóm Tài sản tại Hoa Kỳ theo Giá trị Thực, 1900–2017 (*Cumulative Returns on US Asset Classes in Real Terms, 1900–2017*)**

![](assets/Portfolio_Management.pdf-0016-07.png)

<!-- Picture Text: 1,654<br>1,000<br>100<br>10 10.2<br>2.6<br>1<br>0.10<br>1900 10 20 30 40 50 60 70 80 90 2000 10<br>Equities 6.5% per year Bonds 2.0% per year Bills 0.8% per year<br> -->

> **Chú thích hình ảnh:** Trục hoành biểu diễn các năm từ 1900 đến 2017; trục tung (thang logarit) biểu diễn giá trị tích lũy thực từ 0,10 đến 1.654. Ba đường biểu diễn: Cổ phiếu (*Equities*) tăng lên 1.654 (6,5%/năm), Trái phiếu (*Bonds*) tăng lên 10,2 (2,0%/năm), và Tín phiếu (*Bills*) tăng lên 2,6 (0,8%/năm).

_Nguồn_: E. Dimson, P. Marsh, và M. Staunton, _Credit Suisse Global Investment Returns Yearbook 2018_, Viện Nghiên cứu Credit Suisse (Tháng 2 năm 2018). Biểu đồ này được cập nhật hàng năm và có thể tìm thấy tại https://www.credit-suisse.com/media/assets/corporate/docs/about-us/media/media-release/2018/02/giry-summary-2018.pdf.

Bảng minh họa 2 cho thấy 1 đô la sẽ tăng trưởng lên thành 1.654 đô la nếu được đầu tư vào cổ phiếu, chỉ lên mức 10,20 đô la nếu được đầu tư vào trái phiếu, và lên mức 2,60 đô la nếu được đầu tư vào tín phiếu Kho bạc. Sự khác biệt về mức tăng trưởng giữa ba danh mục tài sản là rất lớn, mặc dù sự khác biệt về tỷ suất sinh lợi thực hàng năm dường như không lớn đến vậy: 6,5% mỗi năm đối với cổ phiếu so với 2,0% mỗi năm đối với trái phiếu. Sự khác biệt này thể hiện tác động của lãi kép (*compounding*) trong suốt giai đoạn 118 năm.

Bảng minh họa 3 báo cáo tỷ suất sinh lợi thực. Như chúng ta đã thảo luận trước đó và như được thể hiện trong bảng, trung bình nhân (*geometric mean* – GM) không bao giờ lớn hơn trung bình cộng (*arithmetic mean* – AM). Phân tích của chúng ta về lợi nhuận tập trung vào trung bình nhân bởi vì nó là sự thể hiện chính xác hơn về tỷ suất sinh lợi cho nhiều kỳ nắm giữ (*multiple holding periods*) so với trung bình cộng. Chúng ta quan sát thấy rằng tỷ suất sinh lợi thực của cổ phiếu cao hơn tỷ suất sinh lợi thực của trái phiếu.


<!-- PDF Page 17 -->

**Bảng minh họa 3: Tỷ suất sinh lợi thực và Phần bù rủi ro của các Nhóm Tài sản (1900–2017) (*Real Returns and Risk Premiums for Asset Classes (1900–2017)*)**

|**Chỉ tiêu**|**_Tài sản_ (*Asset*)**|**Hoa Kỳ (*United States*)**|||**Thế giới (*World*)**|||**Thế giới ngoại trừ Hoa Kỳ (*World excluding United States*)**|||
|---|---|---|---|---|---|---|---|---|---|---|
|||**_GM_ (%)**|**_AM_ (%)**|**_SD_ (%)**|**_GM_ (%)**|**_AM_ (%)**|**_SD_ (%)**|**_GM_ (%)**|**_AM_ (%)**|**_SD_ (%)**|
|**Tỷ suất sinh lợi thực (*Real Returns*)**|Cổ phiếu (*Equities*)|6.5|8.4|20.0|5.2|6.6|17.4|4.5|6.2|18.9|
||Trái phiếu (*Bonds*)|2.0|2.5|10.4|2.0|2.5|11.0|1.7|2.7|14.4|
|**Phần bù (*Premiums*)**|Cổ phiếu so với trái phiếu (*Equities vs. bonds*)|4.4|6.5|20.7|3.2|4.4|15.3|2.8|3.8|14.4|

_Lưu ý:_ Tất cả tỷ suất sinh lợi được tính bằng phần trăm mỗi năm đo lường theo đồng đô la Mỹ (US$). GM = trung bình nhân (*geometric mean*), AM = trung bình cộng (*arithmetic mean*), SD = độ lệch chuẩn (*standard deviation*).

_“Thế giới” bao gồm 21 quốc gia phát triển:_ Úc, Áo, Bỉ, Canada, Đan Mạch, Phần Lan, Pháp, Đức, Ireland, Ý, Nhật Bản, Hà Lan, New Zealand, Na Uy, Bồ Đào Nha, Nam Phi, Tây Ban Nha, Thụy Điển, Thụy Sĩ, Vương quốc Anh, và Hoa Kỳ. Tỷ trọng được tính theo quy mô vốn hóa thị trường tương đối của mỗi quốc gia. Xem nguồn để biết chi tiết về các phép tính.

_Nguồn:_ Credit Suisse Global Investment Returns Sourcebook, 2018.

###### **Tỷ suất sinh lợi danh nghĩa và thực của các nhóm tài sản tại các quốc gia lớn (*Nominal and Real Returns of Asset Classes in Major Countries*)**

Cùng với tỷ suất sinh lợi của Hoa Kỳ, tỷ suất sinh lợi thực của các nhóm tài sản chính cho một thế giới gồm 21 quốc gia và thế giới ngoại trừ Hoa Kỳ cũng được trình bày trong Bảng minh họa 3. Tỷ suất sinh lợi cổ phiếu được tính trọng số theo GDP của mỗi quốc gia trước năm 1968 do thiếu dữ liệu vốn hóa thị trường đáng tin cậy. Tỷ suất sinh lợi được tính trọng số theo vốn hóa thị trường của quốc gia bắt đầu từ năm 1968. Tương tự, tỷ suất sinh lợi trái phiếu được xác định bởi một chỉ số trái phiếu gồm 21 quốc gia, ngoại trừ việc GDP được sử dụng để tạo trọng số bởi vì cách tính trọng số theo vốn hóa thị trường cổ phiếu là không phù hợp đối với một chỉ số trái phiếu và dữ liệu vốn hóa thị trường trái phiếu không có sẵn.

Tỷ suất sinh lợi trung bình nhân thực đối với chỉ số cổ phiếu thế giới trong 117 năm qua là 5,2%, và trái phiếu có tỷ suất sinh lợi trung bình nhân thực là 2,0%. Tỷ suất sinh lợi trung bình nhân thực đối với thế giới ngoại trừ Hoa Kỳ là 4,5% đối với cổ phiếu và 1,7% đối với trái phiếu. Đối với cả cổ phiếu và trái phiếu, Hoa Kỳ đều đạt tỷ suất sinh lợi cao hơn thế giới ngoại trừ Hoa Kỳ. Tương tự, tỷ suất sinh lợi thực đối với cổ phiếu và trái phiếu tại Hoa Kỳ cao hơn tỷ suất sinh lợi thực của phần còn lại của thế giới.

###### **Rủi ro của các nhóm tài sản chính (*Risk of Major Asset Classes*)**

Rủi ro của các nhóm tài sản chính tại Hoa Kỳ được báo cáo cho giai đoạn 1926–2017 trong Bảng minh họa 1, và rủi ro của các nhóm tài sản chính đối với Hoa Kỳ, thế giới, và thế giới ngoại trừ Hoa Kỳ được báo cáo cho giai đoạn 1900–2017 trong Bảng minh họa 3. Bảng minh họa 1 cho thấy cổ phiếu các công ty nhỏ của Hoa Kỳ có rủi ro cao nhất là 31,7%, tiếp theo là cổ phiếu các công ty lớn của Hoa Kỳ ở mức 19,8%. Trái phiếu chính phủ dài hạn và trái phiếu doanh nghiệp dài hạn có rủi ro thấp hơn ở mức 9,9% và 8,3%, với tín phiếu Kho bạc có rủi ro thấp nhất ở mức khoảng 3,1%.

Bảng minh họa 3 cho thấy rủi ro đối với cổ phiếu thế giới là 17,4% và đối với trái phiếu thế giới là 11,0%. Thế giới ngoại trừ Hoa Kỳ có mức rủi ro là 18,9% đối với cổ phiếu và 14,4% đối với trái phiếu. Tác động của sự đa dạng hóa (*diversification*) thể hiện rõ rệt khi rủi ro thế giới được so sánh với rủi ro Hoa Kỳ và rủi ro thế giới ngoại trừ Hoa Kỳ. Mặc dù rủi ro của cổ phiếu Hoa Kỳ là 20,0% và rủi ro của cổ phiếu thế giới ngoại trừ Hoa Kỳ là 18,9%, sự kết hợp này mang lại mức rủi ro chỉ 17,4% cho cổ phiếu thế giới.


<!-- PDF Page 18 -->

###### **Sự đánh đổi giữa Rủi ro và Lợi nhuận (*Risk–Return Trade-off*)**

Cụm từ “sự đánh đổi giữa rủi ro và lợi nhuận (*risk–return trade-off*)” đề cập đến mối quan hệ cùng chiều (*positive relationship*) giữa rủi ro và lợi nhuận kỳ vọng. Nói cách khác, không thể đạt được mức lợi nhuận cao hơn trong các **thị trường hiệu quả (*efficient markets*)** và trong các khoảng thời gian dài mà không chấp nhận mức rủi ro cao hơn. Lợi nhuận kỳ vọng phải lớn hơn đối với những tài sản có rủi ro lớn hơn.

Dữ liệu lịch sử được trình bày ở trên cho thấy sự đánh đổi giữa rủi ro và lợi nhuận. Bảng minh họa 1 chỉ ra rằng tại Hoa Kỳ, cổ phiếu công ty nhỏ có rủi ro cao hơn và lợi nhuận cao hơn so với cổ phiếu công ty lớn. Cổ phiếu công ty lớn có lợi nhuận cao hơn và rủi ro cao hơn so với cả trái phiếu doanh nghiệp dài hạn và trái phiếu chính phủ dài hạn. Trái phiếu có lợi nhuận cao hơn và rủi ro cao hơn tín phiếu Kho bạc. Tuy nhiên, một điểm khác thường là trái phiếu chính phủ dài hạn lại có tổng rủi ro (*total risk*) cao hơn trái phiếu doanh nghiệp dài hạn, mặc dù lợi nhuận của trái phiếu doanh nghiệp cao hơn một chút. Những yếu tố này không có nghĩa là trái phiếu chính phủ dài hạn có rủi ro vỡ nợ (*default risk*) lớn hơn, mà chỉ đơn giản là chúng biến động nhiều hơn so với trái phiếu doanh nghiệp trong giai đoạn lịch sử này.

Bảng minh họa 3 cho thấy rủi ro và lợi nhuận của cổ phiếu là cao nhất trong các nhóm tài sản, còn rủi ro và lợi nhuận của trái phiếu thấp hơn cổ phiếu đối với Hoa Kỳ, thế giới, và thế giới ngoại trừ Hoa Kỳ.

Một cách khác để nhìn nhận sự đánh đổi giữa rủi ro và lợi nhuận là tập trung vào **phần bù rủi ro (*risk premium*)**, tức là khoản lợi nhuận tăng thêm mà nhà đầu tư có thể kỳ vọng khi gánh chịu thêm rủi ro, sau khi đã tính đến lãi suất phi rủi ro. Phần bù rủi ro danh nghĩa (*nominal risk premium*) là tỷ suất sinh lợi có rủi ro danh nghĩa trừ đi lãi suất phi rủi ro danh nghĩa (vốn đã bao gồm cả khoản đền bù cho lạm phát kỳ vọng và lãi suất phi rủi ro thực). Phần bù rủi ro thực (*real risk premium*) là tỷ suất sinh lợi có rủi ro thực trừ đi lãi suất phi rủi ro thực. Phần bù rủi ro cổ phiếu toàn cầu được báo cáo ở cuối Bảng minh họa 3 cho thấy cổ phiếu có thành quả vượt trội hơn trái phiếu. Các nhà đầu tư vào cổ phiếu kiếm được tỷ suất sinh lợi cao hơn các nhà đầu tư vào trái phiếu vì rủi ro ở cổ phiếu cao hơn.

Một sự thể hiện ấn tượng hơn về sự đánh đổi giữa rủi ro và lợi nhuận được trình bày trong Bảng minh họa 2, cho thấy lợi nhuận tích lũy của các nhóm tài sản tại Hoa Kỳ theo giá trị thực. Đường biểu diễn tín phiếu Kho bạc ít biến động hơn nhiều so với các đường khác. Sau khi điều chỉnh lạm phát, tỷ suất sinh lợi thực trung bình của tín phiếu Kho bạc là 0,8% mỗi năm. Đường biểu diễn trái phiếu biến động nhiều hơn đường tín phiếu Kho bạc nhưng ít biến động hơn đường biểu diễn cổ phiếu. Tổng lợi nhuận đối với cổ phiếu bao gồm cổ tức (*dividends*) và lãi vốn (*capital gains*) cho thấy 1 đô la được đầu tư vào đầu năm 1900 đã tăng lên thành 1.654 đô la như thế nào, tạo ra tỷ suất sinh lợi chuẩn hóa theo năm là 6,5% theo giá trị thực.

Qua những khoảng thời gian dài, chúng ta quan sát thấy rằng rủi ro cao hơn thực sự mang lại tỷ suất sinh lợi trung bình cao hơn. Do đó, hoàn toàn hợp lý khi khẳng định rằng, trong dài hạn, giá cả thị trường đền đáp rủi ro cao hơn bằng mức lợi nhuận cao hơn – đây chính là đặc điểm của một nhà đầu tư ngại rủi ro (*risk-averse investor*), một chủ đề mà chúng ta sẽ thảo luận trong Phần 4.

## **<mark>3</mark> CÁC ĐẶC ĐIỂM ĐẦU TƯ KHÁC (*OTHER INVESTMENT CHARACTERISTICS*)**

mô tả đặc điểm của các nhóm tài sản chính (*major asset classes*) mà nhà đầu tư xem xét khi hình thành danh mục đầu tư

Khi đánh giá các khoản đầu tư chỉ sử dụng giá trị trung bình (lợi nhuận kỳ vọng) và phương sai (rủi ro), chúng ta đang ngầm đưa ra hai giả định quan trọng: 1) rằng tỷ suất sinh lợi có phân phối chuẩn (*normally distributed*) và có thể được mô tả đầy đủ bằng giá trị trung bình và phương sai của chúng, và 2) rằng thị trường không chỉ hiệu quả về mặt thông tin (*informationally efficient*) mà còn hiệu quả về mặt vận hành (*operationally efficient*). Trong chừng mực mà các giả định này bị vi phạm, chúng ta cần phải xem xét thêm các đặc điểm đầu tư bổ sung. Những đặc điểm này được thảo luận dưới đây.


<!-- PDF Page 19 -->

###### **Đặc điểm phân phối (*Distributional Characteristics*)**

Như đã giải thích trong một bài đọc trước, một **phân phối chuẩn (*normal distribution*)** có ba đặc điểm chính: giá trị trung bình (*mean*) và trung vị (*median*) của nó bằng nhau; nó được xác định hoàn toàn bởi hai tham số là giá trị trung bình và phương sai (*variance*); và nó đối xứng quanh giá trị trung bình với:

- 68% các quan sát nằm trong khoảng $\pm 1\sigma$ quanh giá trị trung bình,

- 95% các quan sát nằm trong khoảng $\pm 2\sigma$ quanh giá trị trung bình, và

- 99% các quan sát nằm trong khoảng $\pm 3\sigma$ quanh giá trị trung bình.

Việc chỉ sử dụng giá trị trung bình và phương sai sẽ phù hợp để đánh giá các khoản đầu tư nếu tỷ suất sinh lợi có phân phối chuẩn. Tuy nhiên, tỷ suất sinh lợi không có phân phối chuẩn; sự sai lệch khỏi phân phối chuẩn xảy ra vì cả hai lý do: tỷ suất sinh lợi bị lệch (*skewed*), nghĩa là chúng không đối xứng quanh giá trị trung bình, và xác suất xảy ra các sự kiện cực đoan (*extreme events*) lớn hơn đáng kể so với những gì phân phối chuẩn gợi ý. Sự sai lệch thứ hai này được gọi là độ nhọn (*kurtosis*) hay đuôi béo (*fat tails*) trong phân phối tỷ suất sinh lợi. Các phần tiếp theo sẽ thảo luận sâu hơn về những sự sai lệch này.

###### **Độ lệch (*Skewness*)**

**Độ lệch (*Skewness*)** đề cập đến tính bất đối xứng của phân phối tỷ suất sinh lợi, nghĩa là tỷ suất sinh lợi không đối xứng quanh giá trị trung bình. Một phân phối được gọi là lệch trái (*left skewed*) hoặc lệch âm (*negatively skewed*) nếu phần lớn phân phối tập trung về phía bên phải, và lệch phải (*right skewed*) hoặc lệch dương (*positively skewed*) nếu phần lớn tập trung về phía bên trái. Bảng minh họa 4 cho thấy hình ảnh đại diện điển hình của độ lệch âm và độ lệch dương, trong khi Bảng minh họa 5 chứng minh độ lệch âm của tỷ suất sinh lợi cổ phiếu bằng cách vẽ biểu đồ tần suất (*histogram*) tỷ suất sinh lợi cổ phiếu của các công ty lớn tại Hoa Kỳ trong giai đoạn 1926–2017.

###### **Bảng minh họa 4: Độ lệch (*Skewness*)**

![](assets/Portfolio_Management.pdf-0019-11.png)

Phân phối lệch phải (Lệch dương – *Positively Skewed*) | Phân phối lệch trái (Lệch âm – *Negatively Skewed*)

_Nguồn_: In lại từ _Fixed Income Readings for the Chartered Financial Analyst_® _Program._ Bản quyền thuộc Viện CFA (CFA Institute).


<!-- PDF Page 20 -->

![](assets/Portfolio_Management.pdf-0020-03.png)

<!-- Picture Text: Exhibit 5: Histogram of US Large Company Stock Returns, 1926–2017<br>(Percent)<br> -->

> **Chú thích hình ảnh:** Bảng minh họa 5: Biểu đồ tần suất (*Histogram*) tỷ suất sinh lợi cổ phiếu công ty lớn tại Hoa Kỳ, 1926–2017 (Phần trăm).

![](assets/Portfolio_Management.pdf-0020-04.png)

<!-- Picture Text: 2016<br>2014<br>2012<br>2010<br>2015 2006 2017<br>2011 2004 2009 2013<br>2000 2007 1988 2003 1997<br>1990 2005 1986 1999 1995<br>1981 1994 1979 1998 1991<br>1977 1993 1972 1996 1989<br>1969 1992 1971 1983 1985<br>1962 1987 1968 1982 1980<br>1953 1984 1965 1976 1975<br>1946 1978 1964 1967 1955<br>2001 1940 1970 1959 1963 1950<br>1973 1939 1960 1952 1961 1945<br>2002 1966 1934 1956 1949 1951 1938 1958<br>2008 1974 1957 1932 1948 1944 1943 1936 1935 1954<br>1931 1937 1939 1941 1929 1947 1926 1942 1927 1928 1933<br>–60 –50 –40 –30 –20 –10 0 10 20 30 40 50 60 70<br> -->

> **Chú thích hình ảnh:** Biểu đồ tần suất phân bổ các năm từ 1926 đến 2017 theo các khoảng tỷ suất sinh lợi từ –60% đến +70% trên trục hoành.

_Nguồn_: Niên giám SBBI 2018 (Phụ lục A1)

###### **Độ nhọn (*Kurtosis*)**

**Độ nhọn (*Kurtosis*)** đề cập đến hiện tượng đuôi béo (*fat tails*) hoặc xác suất xảy ra các mức lợi nhuận cực đoan cao hơn mức bình thường, và có tác động làm tăng rủi ro của một tài sản mà không được phản ánh trong khung phân tích trung bình – phương sai (*mean–variance framework*), như được minh họa trong Bảng minh họa 6. Các nhà đầu tư cố gắng đánh giá tác động của độ nhọn bằng cách sử dụng các kỹ thuật thống kê như giá trị có rủi ro (*Value at Risk* – VaR) và kỳ vọng đuôi có điều kiện (*conditional tail expectations*).<sup>2</sup> Nhiều thành viên tham gia thị trường lưu ý rằng xác suất và mức độ nghiêm trọng của các sự kiện cực đoan thường bị đánh giá thấp và đó là một yếu tố chính góp phần dẫn đến cuộc khủng hoảng tài chính năm 2008.<sup>3</sup> Xác suất cao hơn của các kết quả âm cực đoan trong tỷ suất sinh lợi cổ phiếu cũng có thể được quan sát thấy trong Bảng minh họa 5.

> 2 Giá trị có rủi ro (*Value at risk* – VaR) là một thước đo bằng tiền về mức lỗ tối thiểu dự kiến của một danh mục đầu tư trong một khoảng thời gian xác định tại một mức xác suất cho trước. Nó thường được sử dụng để đo lường các khoản lỗ mà một danh mục đầu tư có thể gánh chịu trong điều kiện thị trường bình thường. Ví dụ, nếu VaR một ngày ở mức 10% của một danh mục đầu tư là 200.000 bảng Anh (£200,000), điều đó ngụ ý rằng có 10% xác suất giá trị của danh mục đầu tư sẽ giảm hơn 200.000 bảng Anh trong khoảng thời gian một ngày duy nhất (dưới điều kiện thị trường bình thường). Xác suất này ngụ ý rằng danh mục đầu tư sẽ trải qua khoản lỗ ít nhất 200.000 bảng Anh vào một trong số mỗi mười ngày.

> 3 Ví dụ, xem Bogle (2008) và Taleb (2007).


<!-- PDF Page 21 -->

###### **Bảng minh họa 6: Độ nhọn (*Kurtosis*)**

![](assets/Portfolio_Management.pdf-0021-03.png)

<!-- Picture Text: Fat Tails Distribution<br>Normal Distribution<br>–5 –4 –3 –2 –1 0 1 2 3 4 5<br>Standard Deviations<br> -->

> **Chú thích hình ảnh:** So sánh giữa Phân phối đuôi béo (*Fat Tails Distribution*) và Phân phối chuẩn (*Normal Distribution*) theo Độ lệch chuẩn (*Standard Deviations*) từ –5 đến 5 trên trục hoành.

_Nguồn_: In lại từ _Fixed Income Readings for the Chartered Financial Analyst® Program._ Bản quyền thuộc Viện CFA (CFA Institute).

###### **Đặc điểm thị trường (*Market Characteristics*)**

Trong phân tích trước đó, chúng ta đã ngầm giả định rằng thị trường vừa hiệu quả về mặt thông tin vừa hiệu quả về mặt vận hành. Mặc dù tính hiệu quả về mặt thông tin của thị trường là một chủ đề nằm ngoài phạm vi của bài đọc này, chúng ta cần làm nổi bật một số hạn chế về mặt vận hành của thị trường có ảnh hưởng đến việc lựa chọn các khoản đầu tư. Một hạn chế như vậy là **tính thanh khoản (*liquidity*)**. Chi phí giao dịch có ba thành phần chính—hoa hồng môi giới (*brokerage commission*), chênh lệch giá mua – bán (*bid–ask spread*), và tác động giá (*price impact*). Tính thanh khoản ảnh hưởng đến hai thành phần sau. Các cổ phiếu có tính thanh khoản thấp có thể có mức chênh lệch giá mua – bán rộng. Chênh lệch giá mua – bán, tức là khoản chênh lệch giữa giá mua và giá bán, phát sinh như một chi phí khi giao dịch chứng khoán. Chênh lệch giá mua – bán càng lớn thì chi phí giao dịch càng cao. Nếu một cổ phiếu giá 100 đô la có mức chênh lệch là 10 xu, thì chênh lệch giá mua – bán chỉ là 0,1% (\$0,10/\$100). Mặt khác, nếu một cổ phiếu giá 10 đô la có mức chênh lệch là 10 xu, thì chênh lệch giá mua – bán là 1%. Rõ ràng, cổ phiếu giá 10 đô la đắt đỏ hơn khi giao dịch và nhà đầu tư sẽ cần phải kiếm thêm 0,9% lợi nhuận để bù đắp cho chi phí giao dịch cao hơn so với cổ phiếu giá 100 đô la.

Tính thanh khoản cũng có những hàm ý đối với tác động giá (*price impact*) của giao dịch. Tác động giá đề cập đến cách giá cả biến động để phản ứng lại một lệnh giao dịch trên thị trường. Các lệnh nhỏ thường có rất ít tác động, đặc biệt là đối với các cổ phiếu có tính thanh khoản cao. Ví dụ, một lệnh mua 100 cổ phiếu của một mã cổ phiếu giá 100 đô la với mức chênh lệch 1 xu có thể không gây ra tác động nào đến giá. Mặt khác, một lệnh mua 100.000 cổ phiếu có thể có tác động đáng kể đến giá vì người mua phải thu hút ngày càng nhiều cổ đông bán lại cổ phiếu của họ. Mức độ tác động giá phụ thuộc vào tính thanh khoản của cổ phiếu. Một cổ phiếu giao dịch hàng triệu cổ phiếu mỗi ngày có thể ít bị ảnh hưởng hơn so với một cổ phiếu chỉ giao dịch vài trăm nghìn cổ phiếu mỗi ngày. Các nhà đầu tư, đặc biệt là các nhà đầu tư tổ chức quản lý những khoản tiền lớn, phải luôn lưu tâm đến tính thanh khoản của cổ phiếu khi đưa ra quyết định đầu tư.

Tính thanh khoản là một mối quan ngại lớn hơn ở các thị trường mới nổi (*emerging markets*) so với các thị trường phát triển (*developed markets*) do khối lượng giao dịch ở các thị trường đó nhỏ hơn. Tương tự, tính thanh khoản là một mối quan ngại quan trọng hơn trên thị trường trái phiếu doanh nghiệp và đặc biệt là đối với các trái phiếu có


<!-- PDF Page 22 -->

## **<mark>4</mark>**

chất lượng tín dụng thấp hơn so với trên thị trường cổ phiếu, bởi vì một đợt phát hành trái phiếu doanh nghiệp riêng lẻ có thể không được giao dịch trong nhiều ngày hoặc nhiều tuần. Điều này chắc chắn đã trở nên rõ ràng trong suốt cuộc khủng hoảng tài chính toàn cầu.

Có những đặc điểm khác liên quan đến thị trường ảnh hưởng đến các quyết định đầu tư bởi vì chúng có thể củng cố niềm tin lớn hơn vào chứng khoán hoặc có thể ảnh hưởng đến chi phí thực hiện giao dịch kinh doanh. Những đặc điểm này bao gồm mức độ theo dõi của các chuyên gia phân tích (*analyst coverage*), sự sẵn có của thông tin (*availability of information*), quy mô doanh nghiệp (*firm size*), v.v. Những đặc điểm này về các công ty và thị trường tài chính là những thành phần thiết yếu của việc ra quyết định đầu tư.

##### **SỰ NGẠI RỦI RO VÀ LỰA CHỌN DANH MỤC ĐẦU TƯ (*RISK AVERSION AND PORTFOLIO SELECTION*)**

giải thích sự ngại rủi ro (*risk aversion*) và các hàm ý của nó đối với việc lựa chọn danh mục đầu tư

Như chúng ta đã thấy, cổ phiếu, trái phiếu, và tín phiếu Kho bạc mang lại các mức lợi nhuận khác nhau và có các mức độ rủi ro khác nhau. Mặc dù việc đầu tư vào cổ phiếu có thể phù hợp với một nhà đầu tư này, nhưng một nhà đầu tư khác có thể không muốn chấp nhận rủi ro đi kèm với một cổ phần và có thể thích nắm giữ nhiều tiền mặt hơn. Trong phần trước, chúng ta đã xem xét các đặc điểm đầu tư của tài sản để hiểu rõ rủi ro và lợi nhuận của chúng. Trong phần này, chúng ta xem xét các đặc điểm của nhà đầu tư, cả cá nhân lẫn tổ chức, nhằm nỗ lực ghép nối đúng kiểu nhà đầu tư với đúng loại hình đầu tư.

Trước hết, chúng ta thảo luận về sự ngại rủi ro (*risk aversion*) và lý thuyết hữu dụng (*utility theory*). Sau đó, chúng ta thảo luận về các hàm ý của chúng đối với việc lựa chọn danh mục đầu tư.

###### **Khái niệm về Sự ngại rủi ro (*The Concept of Risk Aversion*)**

Khái niệm về **sự ngại rủi ro (*risk aversion*)** có liên quan đến hành vi của các cá nhân trong điều kiện không chắc chắn (*uncertainty*). Giả sử một cá nhân được đưa ra hai phương án lựa chọn: một phương án mà người đó chắc chắn sẽ nhận được 50 bảng Anh (£50) và phương án kia là một trò cá cược (*gamble*) với 50% cơ hội nhận được 100 bảng Anh (£100) và 50% cơ hội không nhận được gì. Giá trị kỳ vọng (*expected value*) trong cả hai trường hợp đều là 50 bảng Anh, một bên là chắc chắn và một bên là không chắc chắn. Nhà đầu tư sẽ chọn phương án nào? Có ba khả năng xảy ra: nhà đầu tư chọn trò cá cược, nhà đầu tư chọn 50 bảng Anh chắc chắn, hoặc nhà đầu tư bàng quan (*indifferent* – thấy hai phương án như nhau). Hãy cùng xem xét lần lượt từng trường hợp. Tuy nhiên, xin hiểu rằng đây chỉ là một ví dụ mang tính đại diện, và một lựa chọn đơn lẻ không quyết định mức độ ngại rủi ro của một nhà đầu tư.

###### **_Yêu thích rủi ro (Risk Seeking)_**

Nếu một nhà đầu tư chọn trò cá cược, thì nhà đầu tư đó được gọi là người yêu thích rủi ro (*risk loving*) hay tìm kiếm rủi ro (*risk seeking*). Trò cá cược có kết quả không chắc chắn, nhưng có cùng giá trị kỳ vọng với kết quả được đảm bảo chắc chắn. Do đó, việc một nhà đầu tư chọn trò cá cược có nghĩa là nhà đầu tư đó nhận được thêm “độ hữu dụng (*utility*)” từ sự không chắc chắn gắn liền với trò cá cược. Độ hữu dụng tăng thêm đó đáng giá bao nhiêu? Liệu nhà đầu tư đó có sẵn sàng chấp nhận một giá trị kỳ vọng nhỏ hơn bởi vì anh ta nhận được thêm độ hữu dụng từ rủi ro hay không? Thực vậy, những người tìm kiếm rủi ro sẽ chấp nhận mức lợi nhuận thấp hơn vì sự hấp dẫn của rủi ro đi kèm với trò cá cược. Ví dụ, một người tìm kiếm rủi ro có thể chọn một trò cá cược có giá trị kỳ vọng là 45 bảng Anh thay vì một kết quả được đảm bảo chắc chắn là 50 bảng Anh.

Có một chút bản năng cờ bạc trong nhiều người chúng ta. Mọi người mua vé số mặc dù giá trị kỳ vọng thấp hơn số tiền họ bỏ ra để mua nó. Hoặc mọi người đánh bạc tại các sòng bạc với sự hiểu biết đầy đủ rằng tỷ suất sinh lợi kỳ vọng là âm – một đặc điểm của những người tìm kiếm rủi ro. Tuy nhiên, những hành động này hay bất kỳ hành động đơn lẻ nào khác không thể được dùng để đánh giá bản chất tổng thể của nhà đầu tư, ngoại trừ đối với những người nghiện cờ bạc.


<!-- PDF Page 23 -->

###### **_Trung lập với rủi ro (Risk Neutral)_**

Nếu một nhà đầu tư bàng quan giữa trò cá cược và kết quả được đảm bảo chắc chắn, thì nhà đầu tư đó có thể là người trung lập với rủi ro (*risk neutral*). Sự trung lập với rủi ro (*risk neutrality*) có nghĩa là nhà đầu tư chỉ quan tâm đến lợi nhuận mà không quan tâm đến rủi ro, vì vậy các khoản đầu tư có lợi nhuận cao hơn sẽ được mong muốn hơn ngay cả khi chúng đi kèm với rủi ro cao hơn. Nhiều nhà đầu tư có thể thể hiện các đặc điểm của sự trung lập với rủi ro khi khoản đầu tư đang xét chỉ là một phần không đáng kể trong tổng tài sản của họ. Ví dụ, một tỷ phú có thể hoàn toàn bàng quan giữa việc chọn trò cá cược hay một kết quả được đảm bảo chắc chắn là 50 bảng Anh.

###### **_Ngại rủi ro (Risk Averse)_**

Nếu một nhà đầu tư chọn kết quả được đảm bảo chắc chắn, người đó được gọi là **ngại rủi ro (*risk averse*)** bởi vì nhà đầu tư không muốn mạo hiểm với khả năng không nhận được gì cả. Tùy thuộc vào mức độ ngại rủi ro, một nhà đầu tư có thể sẵn sàng chấp nhận một kết quả được đảm bảo chắc chắn là 45 bảng Anh thay vì một trò cá cược có giá trị kỳ vọng là 50 bảng Anh.

Nhìn chung, các nhà đầu tư có xu hướng tránh xa các khoản đầu tư rủi ro để đổi lấy một mức lợi nhuận thấp hơn nhưng được đảm bảo chắc chắn. Đó là lý do tại sao họ muốn tối thiểu hóa rủi ro cho cùng một mức lợi nhuận, và tối đa hóa lợi nhuận cho cùng một mức rủi ro. Sự đánh đổi giữa rủi ro và lợi nhuận được thảo luận trước đó chính là một chỉ báo của sự ngại rủi ro. Một nhà đầu tư trung lập với rủi ro sẽ tối đa hóa lợi nhuận bất kể rủi ro và một nhà đầu tư tìm kiếm rủi ro sẽ tối đa hóa cả rủi ro lẫn lợi nhuận.

Dữ liệu được trình bày trong phần trước minh họa mối quan hệ lịch sử cùng chiều giữa rủi ro và lợi nhuận, điều này chứng tỏ rằng giá cả thị trường được hình thành dựa trên các giao dịch và khoản đầu tư của những nhà đầu tư ngại rủi ro và phản ánh sự ngại rủi ro. Do đó, vì mọi mục đích thực tiễn và cho các cuộc thảo luận tiếp theo của chúng ta, chúng ta sẽ giả định rằng nhà đầu tư đại diện (*representative investor*) là một nhà đầu tư ngại rủi ro. Giả định này là cách tiếp cận tiêu chuẩn được áp dụng trong ngành đầu tư trên toàn cầu.

###### **_Khả năng chịu đựng rủi ro (Risk Tolerance)_**

**Khả năng chịu đựng rủi ro (*Risk tolerance*)** đề cập đến lượng rủi ro mà một nhà đầu tư có thể chấp nhận để đạt được một mục tiêu đầu tư. Khả năng chịu đựng rủi ro càng cao thì sự sẵn lòng chấp nhận rủi ro càng lớn. Do đó, khả năng chịu đựng rủi ro có mối quan hệ ngược chiều (*negatively related*) với sự ngại rủi ro.

##### **LÝ THUYẾT HỮU DỤNG VÀ ĐƯỜNG BÀNG QUAN (*UTILITY THEORY AND INDIFFERENCE CURVES*)**

**<mark>5</mark>**

giải thích sự ngại rủi ro (*risk aversion*) và các hàm ý của nó đối với việc lựa chọn danh mục đầu tư

Tiếp tục với ví dụ trước của chúng ta, một nhà đầu tư ngại rủi ro sẽ xếp hạng kết quả được đảm bảo chắc chắn là 50 bảng Anh cao hơn so với kết quả không chắc chắn có giá trị kỳ vọng là 50 bảng Anh. Chúng ta có thể nói rằng độ hữu dụng (*utility*) mà một nhà đầu tư hay một cá nhân nhận được từ kết quả chắc chắn 50 bảng Anh lớn hơn độ hữu dụng hay sự thỏa mãn hoặc niềm vui mà người đó nhận được từ phương án thay thế kia. Nói một cách tổng quát, độ hữu dụng là thước đo mức độ thỏa mãn tương đối từ việc tiêu dùng các hàng hóa và dịch vụ khác nhau, hoặc trong trường hợp đầu tư, là sự thỏa mãn mà một nhà đầu tư nhận được từ một danh mục đầu tư.

Bởi vì các cá nhân có sở thích khác nhau, tất cả những cá nhân ngại rủi ro có thể không xếp hạng các phương án đầu tư theo cùng một cách. Hãy xem xét lại trò cá cược 50 bảng Anh. Tất cả những cá nhân ngại rủi ro sẽ xếp hạng kết quả chắc chắn 50 bảng Anh cao hơn trò cá cược. Điều gì sẽ xảy ra nếu kết quả chắc chắn chỉ là 40 bảng Anh? Một số nhà đầu tư ngại rủi ro có thể coi 40 bảng Anh là không thỏa đáng, những người khác có thể chấp nhận nó, và một số người khác nữa giờ đây có thể trở nên bàng quan giữa mức 50 bảng Anh không chắc chắn và mức 40 bảng Anh chắc chắn.


<!-- PDF Page 24 -->

Một cách triển khai đơn giản của lý thuyết hữu dụng cho phép chúng ta lượng hóa thứ hạng của các lựa chọn đầu tư bằng cách sử dụng rủi ro và lợi nhuận. Có một số giả định về hành vi cá nhân mà chúng ta đưa ra trong định nghĩa về độ hữu dụng được cho trong phương trình dưới đây. Chúng ta giả định rằng các nhà đầu tư là những người ngại rủi ro. Họ luôn thích nhiều hơn ít (lợi nhuận lớn hơn so với lợi nhuận nhỏ hơn). Họ có khả năng xếp hạng các danh mục đầu tư khác nhau theo thứ tự ưu tiên của mình và các thứ hạng đó có tính nhất quán nội tại (*internally consistent*). Nếu một cá nhân thích X hơn Y và thích Y hơn Z, thì người đó phải thích X hơn Z. Tính chất này ngụ ý rằng các đường bàng quan (*indifference curves* – xem Bảng minh họa 7) của cùng một cá nhân không bao giờ có thể chạm hoặc cắt nhau. Một ví dụ về hàm hữu dụng (*utility function*) được cho dưới đây:

![](assets/Portfolio_Management.pdf-0024-04.png)

<!-- Formula Text: U  =  E(r) −  1 _ 2 A σ 2 -->

$$U = E(r) - \frac{1}{2} A \sigma^2$$

trong đó, $U$ là độ hữu dụng của một khoản đầu tư, $E(r)$ là tỷ suất sinh lợi kỳ vọng, và $\sigma^2$ là phương sai của khoản đầu tư đó.

Trong phương trình trên, $A$ là thước đo mức độ ngại rủi ro (*measure of risk aversion*), được đo lường bằng phần thưởng cận biên (*marginal reward*) mà một nhà đầu tư đòi hỏi để chấp nhận thêm rủi ro. Những nhà đầu tư ngại rủi ro nhiều hơn đòi hỏi mức đền bù lớn hơn để chấp nhận thêm rủi ro. Do đó, $A$ cao hơn đối với những cá nhân ngại rủi ro nhiều hơn. Như đã đề cập trước đó, một nhà đầu tư trung lập với rủi ro sẽ tối đa hóa lợi nhuận bất kể rủi ro và một nhà đầu tư tìm kiếm rủi ro sẽ tối đa hóa cả rủi ro lẫn lợi nhuận.

Chúng ta có thể rút ra một số kết luận từ hàm hữu dụng này. Thứ nhất, độ hữu dụng không bị giới hạn ở cả hai phía (*unbounded on both sides*). Nó có thể dương rất lớn hoặc âm rất sâu. Thứ hai, lợi nhuận cao hơn góp phần mang lại độ hữu dụng cao hơn. Thứ ba, phương sai cao hơn làm giảm độ hữu dụng nhưng mức giảm độ hữu dụng này bị khuếch đại bởi hệ số ngại rủi ro (*risk aversion coefficient*), $A$. Độ hữu dụng luôn có thể được gia tăng, dù chỉ ở mức cận biên, bằng cách đạt được lợi nhuận cao hơn hoặc rủi ro thấp hơn. Thứ tư, độ hữu dụng tự nó không chỉ ra hay đo lường trực tiếp sự thỏa mãn—nó chỉ có thể hữu ích trong việc xếp hạng các khoản đầu tư khác nhau. Ví dụ, một danh mục đầu tư có độ hữu dụng bằng 4 không nhất thiết tốt gấp hai lần so với một danh mục đầu tư có độ hữu dụng bằng 2. Danh mục đầu tư có độ hữu dụng bằng 4 có thể làm tăng niềm vui của chúng ta gấp 10 lần hoặc chỉ tăng thêm một chút ở mức cận biên. Nhưng chúng ta chắc chắn thích một danh mục đầu tư có độ hữu dụng bằng 4 hơn một danh mục đầu tư có độ hữu dụng bằng 2. Độ hữu dụng không thể được đem ra so sánh giữa các cá nhân hay các nhà đầu tư với nhau bởi vì nó là một khái niệm mang tính cá nhân rất cao. Từ góc độ xã hội, với cùng lập luận đó, độ hữu dụng không thể được cộng gộp giữa các cá nhân.

Hãy cùng khám phá sâu hơn về hàm hữu dụng. Hệ số ngại rủi ro, $A$, lớn hơn 0 đối với một nhà đầu tư ngại rủi ro. Vì vậy, bất kỳ sự gia tăng nào về rủi ro đều làm giảm độ hữu dụng của người đó. Hệ số ngại rủi ro đối với một nhà đầu tư trung lập với rủi ro là bằng 0, và những thay đổi về rủi ro không ảnh hưởng đến độ hữu dụng của họ. Đối với một người yêu thích rủi ro, hệ số ngại rủi ro mang giá trị âm, tạo ra một tình huống ngược lại sao cho rủi ro tăng thêm lại góp phần làm tăng độ hữu dụng của người đó. Lưu ý rằng một tài sản phi rủi ro ($\sigma^2 = 0$) tạo ra cùng một mức độ hữu dụng cho tất cả các cá nhân.

###### **Đường bàng quan (*Indifference Curves*)**

Một **đường bàng quan (*indifference curve*)** biểu diễn các tập hợp cặp rủi ro – lợi nhuận mà một nhà đầu tư sẵn sàng chấp nhận để duy trì một mức độ hữu dụng nhất định (tức là, nhà đầu tư hoàn toàn bàng quan giữa các kết hợp nằm trên cùng một đường cong bởi vì chúng đều mang lại cùng một mức độ hữu dụng tổng thể). Do đó, các đường bàng quan được xác định dựa trên sự đánh đổi giữa tỷ suất sinh lợi kỳ vọng và phương sai của tỷ suất sinh lợi. Bởi vì có vô số sự kết hợp giữa rủi ro và lợi nhuận có thể tạo ra cùng một độ hữu dụng cho cùng một nhà đầu tư, nên các đường bàng quan là những đường liên tục tại mọi điểm.


<!-- PDF Page 25 -->

**Bảng minh họa 7: Đường bàng quan đối với các Nhà đầu tư Ngại rủi ro (*Indifference Curves for Risk-Averse Investors*)**

![](assets/Portfolio_Management.pdf-0025-03.png)

<!-- Picture Text: High Moderate Low<br>E ( Ri ) Utility Utility Utility<br>1 2 3<br>b<br>x<br>a<br>x<br>x c<br>0 i<br>Standard Deviation<br>Expected Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn (*Standard Deviation* $\sigma_i$), trục tung là Lợi nhuận kỳ vọng (*Expected Return* $E(R_i)$). Ba đường bàng quan 1, 2, 3 tương ứng với Độ hữu dụng Cao (*High Utility*), Độ hữu dụng Trung bình (*Moderate Utility*), và Độ hữu dụng Thấp (*Low Utility*). Điểm $a$ và $b$ nằm trên đường 1; điểm $c$ nằm trên đường 2 có cùng độ lệch chuẩn với điểm $b$.

Một tập hợp các đường bàng quan được vẽ trong Bảng minh họa 7. Theo định nghĩa, tất cả các điểm nằm trên bất kỳ một đường nào trong ba đường cong đều có cùng độ hữu dụng. Một nhà đầu tư không bận tâm liệu mình đang ở Điểm **a** hay Điểm **b** trên Đường bàng quan 1. Điểm **a** có rủi ro thấp hơn và lợi nhuận thấp hơn Điểm **b**, nhưng độ hữu dụng của cả hai điểm là như nhau bởi vì mức lợi nhuận cao hơn tại Điểm **b** đã bị bù trừ bởi mức rủi ro cao hơn.

Giống như Đường 1, tất cả các điểm trên Đường 2 đều có cùng độ hữu dụng và nhà đầu tư hoàn toàn bàng quan về việc mình đang ở vị trí nào trên Đường 2. Bây giờ hãy so sánh Điểm **c** với Điểm **b**. Điểm **c** có cùng mức rủi ro nhưng có lợi nhuận thấp hơn đáng kể so với Điểm **b**, điều đó có nghĩa là độ hữu dụng tại Điểm **c** nhỏ hơn độ hữu dụng tại Điểm **b**. Với việc tất cả các điểm trên Đường 1 có cùng độ hữu dụng, tất cả các điểm trên Đường 2 có cùng độ hữu dụng, và Điểm **b** có độ hữu dụng cao hơn Điểm **c**, suy ra Đường 1 có độ hữu dụng cao hơn Đường 2. Do đó, một nhà đầu tư ngại rủi ro với hai Đường bàng quan 1 và 2 sẽ thích Đường 1 hơn Đường 2. Độ hữu dụng của một nhà đầu tư ngại rủi ro luôn tăng lên khi dịch chuyển về phía tây bắc (*northwest*)—lợi nhuận cao hơn với rủi ro thấp hơn. Bởi vì tất cả các nhà đầu tư đều thích độ hữu dụng nhiều hơn là ít hơn, nên các nhà đầu tư luôn muốn dịch chuyển về phía tây bắc để đến đường bàng quan có độ hữu dụng cao nhất.

Đường bàng quan của các nhà đầu tư ngại rủi ro chạy theo hướng từ tây nam lên đông bắc (*southwest to northeast*) do sự đánh đổi giữa rủi ro và lợi nhuận. Nếu rủi ro tăng lên (đi về phía đông) thì nó phải được đền bù bằng mức lợi nhuận cao hơn (đi về phía bắc) để tạo ra cùng một độ hữu dụng. Các đường bàng quan có dạng lồi (*convex*) do quy luật độ hữu dụng cận biên giảm dần của lợi nhuận (hoặc tài sản) (*diminishing marginal utility of return or wealth*). Khi rủi ro tăng lên, nhà đầu tư cần mức lợi nhuận lớn hơn để đền bù cho rủi ro cao hơn với một tốc độ ngày càng tăng (tức là đường cong ngày càng dốc hơn). Đường bàng quan lồi dốc lên này có hệ số góc (*slope coefficient*) liên hệ mật thiết với hệ số ngại rủi ro. Độ dốc càng lớn thì mức độ ngại rủi ro của nhà đầu tư càng cao, vì cần phải có một mức tăng lợi nhuận lớn hơn để chấp nhận một mức tăng rủi ro nhất định.

Các đường bàng quan của những nhà đầu tư có các mức độ ngại rủi ro khác nhau được vẽ trong Bảng minh họa 8. Nhà đầu tư ngại rủi ro nhất có đường bàng quan với độ dốc lớn nhất. Khi độ biến động (*volatility*) tăng lên, nhà đầu tư này đòi hỏi mức lợi nhuận ngày càng cao hơn để đền bù cho rủi ro. Nhà đầu tư ít ngại rủi ro nhất có đường bàng quan với độ dốc nhỏ nhất, và do đó nhu cầu đòi hỏi lợi nhuận cao hơn khi rủi ro tăng lên không gay gắt như đối với nhà đầu tư ngại rủi ro nhiều hơn. Tuy nhiên, đường bàng quan của nhà đầu tư yêu thích rủi ro lại thể hiện độ dốc âm (*negative slope*), ngụ ý rằng người yêu thích rủi ro rất vui lòng thay thế lợi nhuận bằng rủi ro.


<!-- PDF Page 26 -->

Đối với người yêu thích rủi ro, độ hữu dụng tăng lên khi cả rủi ro cao hơn và lợi nhuận cao hơn. Cuối cùng, các đường bàng quan của những nhà đầu tư trung lập với rủi ro là những đường nằm ngang (*horizontal*) bởi vì độ hữu dụng không thay đổi theo rủi ro.

**Bảng minh họa 8: Đường bàng quan đối với các Nhóm Nhà đầu tư Khác nhau (*Indifference Curves for Various Types of Investors*)**

![](assets/Portfolio_Management.pdf-0026-05.png)

<!-- Picture Text: High Risk Moderate Risk<br>E ( Ri ) Aversion Aversion<br>Low Risk<br>2 Aversion<br>1 3<br>Risk Neutral<br>4<br>5<br>Risk Lover<br>0<br>i<br>Standard Deviation<br>Expected Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn (*Standard Deviation* $\sigma_i$), trục tung là Lợi nhuận kỳ vọng (*Expected Return* $E(R_i)$). Các đường cong biểu diễn: 1 – Ngại rủi ro cao (*High Risk Aversion*), 2 – Ngại rủi ro trung bình (*Moderate Risk Aversion*), 3 – Ngại rủi ro thấp (*Low Risk Aversion*), 4 – Trung lập với rủi ro (*Risk Neutral*, đường nằm ngang), 5 – Yêu thích rủi ro (*Risk Lover*, đường dốc xuống).

Trong các phần còn lại của bài đọc này, tất cả các nhà đầu tư đều được giả định là ngại rủi ro trừ khi có tuyên bố khác.

###### **VÍ DỤ 1**

###### **So sánh một Trò cá cược với một Kết quả được Đảm bảo chắc chắn (*Comparing a Gamble with a Guaranteed Outcome*)**

Giả sử bạn được trao một khoản đầu tư có tỷ suất sinh lợi kỳ vọng là 10% và rủi ro (độ lệch chuẩn) là 20%, và hệ số ngại rủi ro của bạn là 3.

1. Độ hữu dụng của bạn đối với khoản đầu tư này là bao nhiêu?

###### **Lời giải:**

   - $U = 0,10 - 0,5 \times 3 \times 0,20^2 = 0,04$.

2. Tỷ suất sinh lợi phi rủi ro tối thiểu mà bạn phải kiếm được để có cùng mức độ hữu dụng đó là bao nhiêu?

###### **Lời giải:**

Độ lệch chuẩn $\sigma$ của tỷ suất sinh lợi phi rủi ro bằng 0, vì vậy số hạng thứ hai triệt tiêu. Để nhận được cùng mức độ hữu dụng ($0,04$), tỷ suất sinh lợi phi rủi ro phải đạt ít nhất là 4%. Do đó, trong tâm trí của bạn, một tỷ suất sinh lợi có rủi ro ở mức 10% tương đương với một tỷ suất sinh lợi phi rủi ro hay một kết quả được đảm bảo chắc chắn ở mức 4%.


<!-- PDF Page 27 -->

###### **VÍ DỤ 2**

###### **Tính toán Độ hữu dụng (*Computation of Utility*)**

Dựa trên thông tin đầu tư được cho dưới đây và công thức tính độ hữu dụng $U = E(r) - 0,5 A \sigma^2$, hãy trả lời các câu hỏi sau. Tỷ suất sinh lợi và độ lệch chuẩn đều được biểu thị bằng phần trăm mỗi năm. Tuy nhiên, khi sử dụng công thức độ hữu dụng, tỷ suất sinh lợi và độ lệch chuẩn phải được biểu thị dưới dạng số thập phân.

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng $E(r)$**|**Độ lệch chuẩn $\sigma$**|
|---|---|---|
|1|12%|30%|
|2|15|35|
|3|21|40|
|4|24|45|

1. Một nhà đầu tư ngại rủi ro có hệ số ngại rủi ro bằng 4 sẽ chọn khoản đầu tư nào, và một nhà đầu tư ngại rủi ro có hệ số ngại rủi ro bằng 2 sẽ chọn khoản đầu tư nào?

###### **Lời giải:**

Độ hữu dụng đối với các nhà đầu tư ngại rủi ro có $A = 4$ và $A = 2$ cho từng khoản đầu tư trong bốn khoản đầu tư được trình bày trong bảng sau. Phép tính đầy đủ cho Khoản đầu tư 1 với $A = 4$ như sau: $U = 0,12 - 0,5 \times 4 \times 0,30^2 = -0,06$.

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng $E(r)$**|**Độ lệch chuẩn $\sigma$**|**Độ hữu dụng $A = 4$**|**Độ hữu dụng $A = 2$**|
|---|---|---|---|---|
|1|12%|30%|−0.0600|0.0300|
|2|15|35|−0.0950|0.0275|
|3|21|40|−0.1100|0.0500|
|4|24|45|−0.1650|0.0375|

Nhà đầu tư ngại rủi ro có hệ số ngại rủi ro bằng 4 nên chọn Khoản đầu tư 1. Nhà đầu tư ngại rủi ro có hệ số ngại rủi ro bằng 2 nên chọn Khoản đầu tư 3.

2. Một nhà đầu tư trung lập với rủi ro sẽ chọn khoản đầu tư nào?

###### **Lời giải:**

Một nhà đầu tư trung lập với rủi ro chỉ quan tâm đến lợi nhuận. Nói cách khác, hệ số ngại rủi ro của người đó bằng 0. Do đó, một nhà đầu tư trung lập với rủi ro sẽ chọn Khoản đầu tư 4 bởi vì nó có lợi nhuận cao nhất.

3. Một nhà đầu tư yêu thích rủi ro sẽ chọn khoản đầu tư nào?

###### **Lời giải:**

Một nhà đầu tư yêu thích rủi ro thích cả rủi ro cao hơn và lợi nhuận cao hơn. Nói cách khác, hệ số ngại rủi ro của người đó mang giá trị âm. Do đó, một nhà đầu tư yêu thích rủi ro sẽ chọn Khoản đầu tư 4 bởi vì nó có lợi nhuận cao nhất và rủi ro cao nhất trong số bốn khoản đầu tư.


---

# Tập 9: Quản lý Danh mục Đầu tư (*Portfolio Management*)
## Học phần 1: Rủi ro và Lợi nhuận Danh mục Đầu tư: Phần I (*Portfolio Risk and Return: Part I*)
### Phần 2/4: Ứng dụng Lý thuyết Hữu dụng vào Lựa chọn Danh mục Đầu tư (*Application of Utility Theory to Portfolio Selection*) (Trang PDF 28–40)

---

<!-- PDF Page 28 -->

# **<mark>6</mark>**

## **ỨNG DỤNG LÝ THUYẾT HỮU DỤNG VÀO LỰA CHỌN DANH MỤC ĐẦU TƯ (*APPLICATION OF UTILITY THEORY TO PORTFOLIO SELECTION*)**

giải thích sự ngại rủi ro (*risk aversion*) và các hàm ý của nó đối với việc lựa chọn danh mục đầu tư
giải thích việc lựa chọn danh mục đầu tư tối ưu (*optimal portfolio*), khi biết độ hữu dụng (*utility*) (hoặc mức độ ngại rủi ro) của nhà đầu tư và đường phân bổ vốn (*capital allocation line*)

Ứng dụng đơn giản nhất của lý thuyết hữu dụng và sự ngại rủi ro là đối với một danh mục đầu tư gồm hai tài sản: một tài sản phi rủi ro (*risk-free asset*) và một tài sản rủi ro (*risky asset*). Tài sản phi rủi ro có rủi ro bằng không và có tỷ suất sinh lợi là $R_f$. Tài sản rủi ro có mức rủi ro là $\sigma_i$ ($> 0$) và tỷ suất sinh lợi kỳ vọng là $E(R_i)$. Bởi vì tài sản rủi ro có rủi ro lớn hơn so với tài sản phi rủi ro, nên tỷ suất sinh lợi kỳ vọng từ tài sản rủi ro sẽ lớn hơn tỷ suất sinh lợi từ tài sản phi rủi ro, tức là $E(R_i) > R_f$.

Chúng ta có thể xây dựng một danh mục đầu tư gồm hai tài sản này với tỷ suất sinh lợi kỳ vọng của danh mục đầu tư là $E(R_p)$ và rủi ro của danh mục đầu tư là $\sigma_p$, dựa trên các công thức được cung cấp dưới đây. Trong các phương trình dưới đây, $w_1$ là tỷ trọng đầu tư vào tài sản phi rủi ro và $(1 - w_1)$ là tỷ trọng đầu tư vào tài sản rủi ro. Bởi vì $\sigma_f = 0$ đối với tài sản phi rủi ro, nên số hạng thứ nhất và thứ ba trong công thức tính phương sai đều bằng 0, chỉ còn lại số hạng thứ hai. Chúng ta thu được phương trình cuối cùng bằng cách lấy căn bậc hai của cả hai vế, cho thấy biểu thức tính độ lệch chuẩn của một danh mục đầu tư gồm hai tài sản khi một tài sản là tài sản phi rủi ro:

![](assets/Portfolio_Management.pdf-0028-09.png)

<!-- Formula Text: E(R p)  =  w 1 R f + (1 − w 1)E(R i) -->

$$E(R_p) = w_1 R_f + (1 - w_1)E(R_i)$$

![](assets/Portfolio_Management.pdf-0028-10.png)

<!-- Formula Text: σ P 2   =  w 1 2 σ f 2 + (1 − w 1) 2 σ i 2 + 2 w 1(1 − w 1) ρ 12 σ f σ i  =  (1 − w 1) 2 σ i 2 σ p  =  (1 − w 1) σ i -->

$$\sigma_p^2 = w_1^2 \sigma_f^2 + (1 - w_1)^2 \sigma_i^2 + 2w_1(1 - w_1)\rho_{12}\sigma_f\sigma_i = (1 - w_1)^2 \sigma_i^2$$

$$\sigma_p = (1 - w_1)\sigma_i$$

Danh mục đầu tư gồm hai tài sản được vẽ trong Bảng minh họa 9 bằng cách thay đổi $w_1$ từ 0% đến 100%. Độ lệch chuẩn của danh mục đầu tư nằm trên trục hoành và tỷ suất sinh lợi của danh mục đầu tư nằm trên trục tung. Nếu chỉ có hai tài sản này trong nền kinh tế và tài sản rủi ro đại diện cho thị trường, thì đường thẳng trong Bảng minh họa 9 được gọi là **đường phân bổ vốn (*capital allocation line* – CAL)**. Đường phân bổ vốn biểu diễn các danh mục đầu tư hiện có dành cho một nhà đầu tư. Phương trình của đường thẳng này có thể được suy ra từ hai phương trình trên bằng cách viết lại phương trình thứ hai thành $w_1 = 1 - \frac{\sigma_p}{\sigma_i}$. Thay giá trị của $w_1$ vào phương trình tính tỷ suất sinh lợi kỳ vọng, chúng ta thu được phương trình sau đây cho đường phân bổ vốn:

![](assets/Portfolio_Management.pdf-0028-12.png)

<!-- Formula Text: E(R p)  =  (1 − σ p _ σ i ) R f + σ p _ σ i E(R i) -->

$$E(R_p) = \left(1 - \frac{\sigma_p}{\sigma_i}\right) R_f + \frac{\sigma_p}{\sigma_i} E(R_i)$$

Phương trình này có thể được viết lại dưới dạng dễ sử dụng hơn:

![](assets/Portfolio_Management.pdf-0028-14.png)

<!-- Formula Text: E(R p)  =  R f + (E(R i) − R f) _ σ i σ p -->

$$E(R_p) = R_f + \frac{E(R_i) - R_f}{\sigma_i} \sigma_p$$

Đường phân bổ vốn có tung độ gốc (*intercept*) là $R_f$, và hệ số góc (*slope*) là $\frac{E(R_i) - R_f}{\sigma_i}$, tức là mức lợi nhuận yêu cầu tăng thêm cho mỗi đơn vị rủi ro tăng thêm, và đôi khi được gọi là cái giá thị trường của rủi ro (*market price of risk*).


<!-- PDF Page 29 -->

**Bảng minh họa 9: Đường phân bổ vốn với Hai Tài sản (*Capital Allocation Line with Two Assets*)**

![](assets/Portfolio_Management.pdf-0029-03.png)

<!-- Picture Text: E ( Rp )<br>E ( Ri ) x<br>Rf<br>0<br>i p<br>Portfolio Standard Deviation<br>Expected Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn của danh mục đầu tư (*Portfolio Standard Deviation* $\sigma_p$), trục tung là Lợi nhuận kỳ vọng (*Expected Return* $E(R_p)$). Đường thẳng bắt đầu từ tung độ gốc $R_f$ (tại $\sigma_p = 0$) đi qua điểm tài sản rủi ro $(\sigma_i, E(R_i))$.

Bởi vì phương trình có dạng tuyến tính, đồ thị của đường phân bổ vốn là một đường thẳng. Đường thẳng bắt đầu với tài sản phi rủi ro ở điểm ngoài cùng bên trái có rủi ro bằng không và tỷ suất sinh lợi phi rủi ro là $R_f$. Tại điểm đó, danh mục đầu tư chỉ bao gồm tài sản phi rủi ro. Tuy nhiên, nếu 100% được đầu tư vào danh mục gồm tất cả các tài sản rủi ro, chúng ta sẽ có tỷ suất sinh lợi là $E(R_i)$ với mức rủi ro là $\sigma_i$.

Chúng ta có thể di chuyển xa hơn dọc theo đường thẳng này để theo đuổi mức lợi nhuận cao hơn bằng cách đi vay với lãi suất phi rủi ro và đầu tư số tiền vay được vào danh mục gồm tất cả các tài sản rủi ro. Nếu vay thêm 50% tại mức lãi suất phi rủi ro, thì $w_1 = -0,50$ và 150% được phân bổ vào tài sản rủi ro, mang lại tỷ suất sinh lợi $= 1,50 E(R_i) - 0,50 R_f$, lớn hơn $E(R_i)$ bởi vì $E(R_i) > R_f$.

Đường thẳng được vẽ trong Bảng minh họa 9 bao gồm vô số cặp rủi ro – lợi nhuận hay các danh mục đầu tư. Nhà đầu tư nên chọn _một_ danh mục nào trong số các danh mục đầu tư này? Câu trả lời nằm ở việc kết hợp các đường bàng quan (*indifference curves*) từ lý thuyết hữu dụng với đường phân bổ vốn (*capital allocation line*) từ lý thuyết danh mục đầu tư. Lý thuyết hữu dụng cho chúng ta hàm hữu dụng hoặc các đường bàng quan của một cá nhân, như trong Bảng minh họa 9, và đường phân bổ vốn cho chúng ta tập hợp các khoản đầu tư khả thi (*set of feasible investments*). Việc chồng các đường bàng quan của mỗi cá nhân lên đường phân bổ vốn sẽ mang lại cho chúng ta danh mục đầu tư tối ưu (*optimal portfolio*) cho nhà đầu tư đó. Bảng minh họa 10 minh họa quy trình lựa chọn danh mục đầu tư này.


<!-- PDF Page 30 -->

**Bảng minh họa 10: Lựa chọn Danh mục Đầu tư (*Portfolio Selection*)**

![](assets/Portfolio_Management.pdf-0030-05.png)

<!-- Picture Text: E ( Rp )<br>1 2 3<br>l x<br>x a<br>m<br>x<br>n<br>x<br>x<br>b<br>0<br>Portfolio Standard Deviation p<br>Expected Portfolio Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Ba đường bàng quan 1, 2, 3 được vẽ cùng với Đường phân bổ vốn (CAL). Đường 2 tiếp xúc với CAL tại điểm $m$; Đường 3 cắt CAL tại điểm $a$ và $b$ (với điểm $n$ nằm dưới điểm $m$ ở cùng mức rủi ro); Đường 1 (có điểm $l$) nằm hoàn toàn phía trên CAL.

Đường phân bổ vốn bao gồm tập hợp các danh mục đầu tư khả thi. Các điểm nằm dưới đường phân bổ vốn có thể đạt được nhưng không được bất kỳ nhà đầu tư nào ưa thích bởi vì nhà đầu tư có thể nhận được lợi nhuận cao hơn với cùng mức rủi ro bằng cách di chuyển lên đường phân bổ vốn. Các điểm nằm phía trên đường phân bổ vốn là đáng mong muốn nhưng không thể đạt được với các tài sản hiện có.

Ba đường bàng quan của cùng một cá nhân cũng được thể hiện trong Bảng minh họa 10. Đường 1 nằm phía trên đường phân bổ vốn, Đường 2 tiếp xúc (*tangential*) với đường phân bổ vốn, và Đường 3 cắt đường phân bổ vốn tại hai điểm. Đường 1 có độ hữu dụng cao nhất và Đường 3 có độ hữu dụng thấp nhất. Bởi vì Đường 1 nằm hoàn toàn phía trên đường phân bổ vốn, các điểm trên Đường 1 không thể đạt được với các tài sản hiện có trên đường phân bổ vốn. Đường 3 cắt đường phân bổ vốn tại hai Điểm, **a** và **b**. Nhà đầu tư có thể đầu tư tại Điểm **a** hoặc Điểm **b** để nhận được sự đánh đổi rủi ro – lợi nhuận và độ hữu dụng gắn liền với Đường 3. Khi so sánh các điểm có cùng mức rủi ro, hãy quan sát thấy rằng Điểm **n** trên Đường 3 có cùng mức rủi ro như Điểm **m** trên Đường 2, nhưng Điểm **m** lại có tỷ suất sinh lợi kỳ vọng cao hơn. Do đó, tất cả các nhà đầu tư sẽ chọn Đường 2 thay vì Đường 3. Đường 2 tiếp xúc với đường phân bổ vốn tại Điểm **m**. Điểm **m** nằm trên đường phân bổ vốn và có thể đầu tư được. Điểm **m** và độ hữu dụng gắn liền với Đường 2 là kết quả tốt nhất mà nhà đầu tư có thể đạt được bởi vì người đó không thể dịch chuyển lên một đường bàng quan có độ hữu dụng cao hơn. Như vậy, chúng ta đã có thể lựa chọn danh mục đầu tư tối ưu cho nhà đầu tư có các Đường bàng quan 1, 2, và 3. Điểm **m**, danh mục đầu tư tối ưu đối với một nhà đầu tư này, có thể không phải là tối ưu đối với một nhà đầu tư khác. Tuy nhiên, chúng ta có thể tuân theo cùng một quy trình để tìm ra danh mục đầu tư tối ưu cho các nhà đầu tư khác: danh mục đầu tư tối ưu chính là tiếp điểm (*point of tangency*) giữa đường phân bổ vốn và đường bàng quan của nhà đầu tư đó. Nói cách khác, danh mục đầu tư tối ưu tối đa hóa lợi nhuận trên mỗi đơn vị rủi ro (vì nó nằm trên đường phân bổ vốn), đồng thời mang lại cho nhà đầu tư sự thỏa mãn (độ hữu dụng) lớn nhất.

Để minh họa, Bảng minh họa 11 cho thấy hai đường bàng quan của hai nhà đầu tư khác nhau: Kelly với hệ số ngại rủi ro bằng 2 và Jane với hệ số ngại rủi ro bằng 4. Đường bàng quan của Kelly nằm về phía bên phải so với đường bàng quan của Jane bởi vì Kelly ít ngại rủi ro hơn Jane và có thể chấp nhận một lượng rủi ro cao hơn, tức là có khả năng chịu đựng rủi ro (*tolerance for risk*) cao hơn. Theo đó, danh mục đầu tư tối ưu của họ là khác nhau:


<!-- PDF Page 31 -->

Điểm **k** là danh mục đầu tư tối ưu cho Kelly và Điểm **j** là danh mục đầu tư tối ưu cho Jane. Ngoài ra, đối với cùng một mức lợi nhuận, độ dốc trên đường cong của Jane cao hơn của Kelly, cho thấy rằng Jane cần mức lợi nhuận tăng thêm lớn hơn để đền bù cho việc chấp nhận thêm một lượng rủi ro so với Kelly.

#### **Bảng minh họa 11: Lựa chọn Danh mục Đầu tư cho Hai Nhà đầu tư có các Mức độ Ngại rủi ro Khác nhau (*Portfolio Selection for Two Investors with Various Levels of Risk Aversion*)**

![](assets/Portfolio_Management.pdf-0031-05.png)

<!-- Picture Text: E ( Rp ) Indifference Curves<br>Capital Allocation<br>Line<br>A = 2<br>x<br>k<br>A = 4<br>x<br>j<br>0<br>Portfolio Standard Deviation p<br>Expected Portfolio Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Đường bàng quan của Jane ($A = 4$) tiếp xúc với Đường phân bổ vốn (*Capital Allocation Line*) tại điểm $j$; đường bàng quan của Kelly ($A = 2$) tiếp xúc với Đường phân bổ vốn tại điểm $k$ ở mức rủi ro và lợi nhuận cao hơn.

## **RỦI RO DANH MỤC ĐẦU TƯ & DANH MỤC GỒM HAI TÀI SẢN RỦI RO (*PORTFOLIO RISK & PORTFOLIO OF TWO RISKY ASSETS*)**

# **<mark>7</mark>**

tính toán và diễn giải giá trị trung bình (*mean*), phương sai (*variance*), và hiệp phương sai (*covariance*) (hoặc hệ số tương quan – *correlation*) của tỷ suất sinh lợi tài sản dựa trên dữ liệu lịch sử

tính toán và diễn giải độ lệch chuẩn của danh mục đầu tư (*portfolio standard deviation*)

mô tả tác động lên rủi ro của danh mục đầu tư khi đầu tư vào các tài sản có tương quan nhỏ hơn mức tương quan hoàn hảo (*less than perfectly correlated*)

Trước đây chúng ta đã thấy rằng các nhà đầu tư là những người ngại rủi ro và đòi hỏi tỷ suất sinh lợi cao hơn cho một khoản đầu tư rủi ro hơn. Do đó, các cách thức kiểm soát rủi ro danh mục đầu tư mà không làm ảnh hưởng đến lợi nhuận là vô cùng có giá trị. Như một bước đệm cho việc quản lý rủi ro, phần này giải thích và phân tích các thành phần của rủi ro danh mục đầu tư. Cụ thể, phần này xem xét và mô tả cách một danh mục đầu tư bao gồm các tài sản có tương quan thấp có tiềm năng làm giảm rủi ro mà không nhất thiết làm giảm lợi nhuận.

### **Danh mục Đầu tư gồm Hai Tài sản Rủi ro (*Portfolio of Two Risky Assets*)**

Lợi nhuận và rủi ro của một danh mục đầu tư gồm hai tài sản đã được giới thiệu trong Phần 2–3 của bài đọc này. Trong phần này, chúng ta ôn lại ngắn gọn cách tính toán lợi nhuận và mở rộng khái niệm về rủi ro danh mục đầu tư cùng các thành phần của nó.


<!-- PDF Page 32 -->

#### **_Lợi nhuận Danh mục Đầu tư (Portfolio Return)_**

Khi nhiều tài sản riêng lẻ được kết hợp lại thành một danh mục đầu tư, chúng ta có thể tính toán tỷ suất sinh lợi của danh mục đầu tư dưới dạng bình quân gia quyền (*weighted average*) của các tỷ suất sinh lợi trong danh mục đó. Tỷ suất sinh lợi của danh mục đầu tư đơn giản là bình quân gia quyền của tỷ suất sinh lợi của các khoản đầu tư, hay tài sản riêng lẻ. Nếu Tài sản 1 có tỷ suất sinh lợi là 20% và chiếm 25% tổng vốn đầu tư của danh mục, thì mức đóng góp vào tỷ suất sinh lợi của danh mục đầu tư là 5% ($= 25\%$ của $20\%$). Nhìn chung, nếu Tài sản $i$ có tỷ suất sinh lợi là $R_i$ và có tỷ trọng là $w_i$ trong danh mục đầu tư, thì tỷ suất sinh lợi của danh mục đầu tư, $R_P$, được cho bởi:

![](assets/Portfolio_Management.pdf-0032-06.png)

<!-- Formula Text: R P  =  ∑ i=1 N w i R i,    ∑ i=1 N w i  =  1 -->

$$R_P = \sum_{i=1}^{N} w_i R_i, \quad \sum_{i=1}^{N} w_i = 1$$

Lưu ý rằng tổng các tỷ trọng phải bằng 1 bởi vì các tài sản trong một danh mục đầu tư, bao gồm cả tiền mặt, phải chiếm 100% tổng vốn đầu tư. Ngoài ra, lưu ý rằng đây là tỷ suất sinh lợi đơn kỳ (*single period returns*), vì vậy không có dòng tiền nào phát sinh trong kỳ và các tỷ trọng được giữ nguyên không đổi.

Khi hai tài sản riêng lẻ được kết hợp trong một danh mục đầu tư, chúng ta có thể tính toán tỷ suất sinh lợi của danh mục đầu tư dưới dạng bình quân gia quyền của tỷ suất sinh lợi của hai tài sản đó. Hãy xét Tài sản 1 và 2 với tỷ trọng lần lượt là 25% và 75% trong một danh mục đầu tư. Nếu tỷ suất sinh lợi của chúng là 20% và 5%, thì tỷ suất sinh lợi bình quân gia quyền $= (0,25 \times 20\%) + (0,75 \times 5\%) = 8,75\%$. Tổng quát hơn, tỷ suất sinh lợi của danh mục đầu tư có thể được viết như dưới đây, trong đó $R_p$ là tỷ suất sinh lợi của danh mục đầu tư, $w_1$ và $w_2$ là tỷ trọng của hai tài sản, và $R_1, R_2$ là tỷ suất sinh lợi của hai tài sản:

![](assets/Portfolio_Management.pdf-0032-09.png)

<!-- Formula Text: R p  =  w 1 R 1 + (1 − w 1) R 2 -->

$$R_p = w_1 R_1 + (1 - w_1) R_2$$

#### **_Rủi ro Danh mục Đầu tư (Portfolio Risk)_**

Giống như tỷ suất sinh lợi của danh mục đầu tư, chúng ta có thể tính toán phương sai của danh mục đầu tư (*portfolio’s variance*). Mặc dù tỷ suất sinh lợi của một danh mục đầu tư chỉ đơn giản là bình quân gia quyền của tỷ suất sinh lợi của từng chứng khoán, nhưng điều này không đúng với độ lệch chuẩn của một danh mục đầu tư (trừ khi tất cả các chứng khoán có tương quan hoàn hảo—tức là hệ số tương quan bằng 1). Phương sai có thể được biểu diễn tổng quát hơn cho $N$ chứng khoán trong một danh mục đầu tư bằng cách sử dụng ký hiệu từ phép tính tỷ suất sinh lợi danh mục đầu tư ở trên:

![](assets/Portfolio_Management.pdf-0032-12.png)

<!-- Formula Text: ∑ i=1 N w i  =  1 σ P 2   =  Var(R P)  =  Var(∑ i=1 N w i R i) -->

$$\sum_{i=1}^{N} w_i = 1$$

$$\sigma_P^2 = \text{Var}(R_P) = \text{Var}\left(\sum_{i=1}^{N} w_i R_i\right)$$

Lưu ý rằng tổng các tỷ trọng phải bằng 1. Vế phải của phương trình là phương sai của tỷ suất sinh lợi bình quân gia quyền của các chứng khoán riêng lẻ. Tỷ trọng là một hằng số, nhưng tỷ suất sinh lợi là các biến số có phương sai được ký hiệu bởi $\text{Var}(R_i)$. Chúng ta có thể viết lại phương trình như trình bày tiếp theo đây. Bởi vì hiệp phương sai (*covariance*) của một tài sản với chính nó chính là phương sai của tài sản đó, chúng ta có thể tách riêng các phương sai khỏi các hiệp phương sai trong phương trình thứ hai:

![](assets/Portfolio_Management.pdf-0032-14.png)

<!-- Formula Text: σ P 2   =   ∑ i,j=1 N w i w j Cov(R i, R j) σ P 2   =  ∑ i=1 N w i 2 Var(R i) +   ∑ i,j=1,i≠j N w i w j Cov(R i, R j) -->

$$\sigma_P^2 = \sum_{i,j=1}^{N} w_i w_j \text{Cov}(R_i, R_j)$$

$$\sigma_P^2 = \sum_{i=1}^{N} w_i^2 \text{Var}(R_i) + \sum_{i,j=1, i \neq j}^{N} w_i w_j \text{Cov}(R_i, R_j)$$

$\text{Cov}(R_i, R_j)$ là hiệp phương sai của các tỷ suất sinh lợi, $R_i$ và $R_j$, và có thể được biểu diễn bằng tích của hệ số tương quan giữa hai tỷ suất sinh lợi ($\rho_{1,2}$) và độ lệch chuẩn của hai tài sản. Do đó, $\text{Cov}(R_i, R_j) = \rho_{ij} \sigma_i \sigma_j$.

Đối với một danh mục đầu tư gồm hai tài sản, biểu thức tính phương sai của danh mục đầu tư được rút gọn thành công thức sau đây khi sử dụng hiệp phương sai và sau đó là sử dụng hệ số tương quan:


<!-- PDF Page 33 -->

![](assets/Portfolio_Management.pdf-0033-02.png)

<!-- Formula Text: σ P 2   =  w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 Cov(R 1, R 2) σ P 2   =  w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 ρ 12 σ 1 σ 2 -->

$$\sigma_P^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(R_1, R_2)$$

$$\sigma_P^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

Độ lệch chuẩn của một danh mục đầu tư gồm hai tài sản được tính bằng căn bậc hai của phương sai danh mục đầu tư:

![](assets/Portfolio_Management.pdf-0033-04.png)

<!-- Formula Text: σ P  =  √ ______________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 Cov(R 1, R 2) -->

$$\sigma_P = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(R_1, R_2)}$$

hoặc,

$$\sigma_P = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2}$$

#### **VÍ DỤ 3**

### **Lợi nhuận và Rủi ro của một Danh mục Đầu tư gồm Hai Tài sản (*Return and Risk of a Two-Asset Portfolio*)**

1. Giả sử là một nhà đầu tư Hoa Kỳ, bạn quyết định nắm giữ một danh mục đầu tư với 80% được đầu tư vào chỉ số cổ phiếu S&P 500 của Hoa Kỳ và 20% còn lại vào chỉ số MSCI Thị trường Mới nổi (*MSCI Emerging Markets index*). Tỷ suất sinh lợi kỳ vọng là 9,93% đối với S&P 500 và 18,20% đối với chỉ số Thị trường Mới nổi. Rủi ro (độ lệch chuẩn) là 16,21% đối với S&P 500 và 33,11% đối với chỉ số Thị trường Mới nổi. Tỷ suất sinh lợi kỳ vọng và rủi ro của danh mục đầu tư sẽ là bao nhiêu khi biết rằng hiệp phương sai giữa S&P 500 và chỉ số Thị trường Mới nổi là 0,5% hay 0,0050? Lưu ý rằng đơn vị của hiệp phương sai và phương sai được viết là $\%^2$ khi không được biểu thị dưới dạng số thập phân. Đây là các đơn vị đo lường giống như feet vuông (*squared feet*) và bản thân các con số không thực sự bị bình phương thêm lần nữa.

**Lời giải:**

Tỷ suất sinh lợi của danh mục đầu tư, $R_P = w_1 R_1 + (1 - w_1) R_2 = (0,80 \times 0,0993) + (0,20 \times 0,1820) = 0,1158 = 11,58\%$.

![](assets/Portfolio_Management.pdf-0033-12.png)

<!-- Formula Text: Portfolio risk  =  σ P  =  √ ______________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 Cov(R 1, R 2) σ p 2  =  w US 2   σ US 2   + w EM 2   σ EM 2   + 2 w US w EM Co v US,EM σ p 2  =  (0.80 2 × 0.1621 2) + (0.20 2 × 0.3311 2) +  (2 × 0.80 × 0.20 × 0.0050) σ p 2  =  0.01682 + 0.00439 + 0.00160  =  0.02281 σ p  =  0.15103  =  15.10% -->

$$\text{Rủi ro danh mục đầu tư} = \sigma_P = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(R_1, R_2)}$$

$$\sigma_p^2 = w_{\text{US}}^2 \sigma_{\text{US}}^2 + w_{\text{EM}}^2 \sigma_{\text{EM}}^2 + 2 w_{\text{US}} w_{\text{EM}} \text{Cov}_{\text{US,EM}}$$

$$\sigma_p^2 = (0,80^2 \times 0,1621^2) + (0,20^2 \times 0,3311^2) + (2 \times 0,80 \times 0,20 \times 0,0050)$$

$$\sigma_p^2 = 0,01682 + 0,00439 + 0,00160 = 0,02281$$

$$\sigma_p = 0,15103 = 15,10\%$$

Tỷ suất sinh lợi kỳ vọng của danh mục đầu tư là 11,58% và rủi ro của danh mục đầu tư là 15,10%. Hãy quan sát kỹ ví dụ này. Nó cho thấy rằng chúng ta có thể lấy danh mục đầu tư của một nhà đầu tư Hoa Kỳ vốn chỉ đầu tư vào S&P 500, kết hợp nó với một danh mục đầu tư _rủi ro hơn_ bao gồm các chứng khoán thị trường mới nổi, và lợi nhuận của nhà đầu tư Hoa Kỳ tăng từ 9,93% lên 11,58% trong khi rủi ro của danh mục đầu tư thực tế lại giảm từ 16,21% xuống còn 15,10%. Bảng minh họa 12 mô tả cách thức sự kết hợp của hai tài sản mang lại sự đánh đổi rủi ro – lợi nhuận vượt trội. Nhà đầu tư không chỉ nhận được mức lợi nhuận cao hơn mà còn đạt được điều đó ở một mức rủi ro thấp hơn. Đó chính là sức mạnh của sự đa dạng hóa (*power of diversification*) như bạn sẽ thấy ở phần sau của bài đọc này.


<!-- PDF Page 34 -->

#### **Bảng minh họa 12: Sự kết hợp của Hai Tài sản (*Combination of Two Assets*)**

![](assets/Portfolio_Management.pdf-0034-04.png)

<!-- Picture Text: 20%<br>ρ = 0.093<br>Emerging<br>Markets<br>Portfolio<br>10%<br>S&P 500<br>10% 20% 30%<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return E () R p<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn của danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Đường cong nối giữa S&P 500 và Thị trường Mới nổi (*Emerging Markets*) với hệ số tương quan $\rho = 0,093$ uốn cong về phía bên trái tại điểm Danh mục đầu tư (*Portfolio*), đạt lợi nhuận cao hơn và rủi ro thấp hơn so với chỉ nắm giữ S&P 500.

#### **_Hiệp phương sai và Hệ số tương quan (Covariance and Correlation)_**

**Hiệp phương sai (*covariance*)** trong công thức tính độ lệch chuẩn của danh mục đầu tư có thể được khai triển thành $\text{Cov}(R_1, R_2) = \rho_{12}\sigma_1\sigma_2$, trong đó $\rho_{12}$ là hệ số tương quan giữa các tỷ suất sinh lợi $R_1, R_2$. Mặc dù hiệp phương sai rất quan trọng, nhưng nó lại khó diễn giải bởi vì nó không bị giới hạn ở cả hai phía (*unbounded on both sides*). Sẽ dễ hiểu hơn khi sử dụng **hệ số tương quan (*correlation coefficient*)** ($\rho_{12}$), một đại lượng có giới hạn nhưng cung cấp thông tin tương tự.

Hệ số tương quan là thước đo tính nhất quán hoặc xu hướng hai khoản đầu tư biến động theo cách tương tự nhau. Hệ số tương quan, $\rho_{12}$, có thể dương hoặc âm và nằm trong khoảng từ $-1$ đến $+1$. Hãy xem xét ba giá trị khác nhau của hệ số tương quan:

- $\rho_{12} = +1$: Tỷ suất sinh lợi của hai tài sản có tương quan _dương_ hoàn hảo (*perfectly positively correlated*). Tài sản 1 và 2 biến động cùng chiều 100% thời gian.

- $\rho_{12} = -1$: Tỷ suất sinh lợi của hai tài sản có tương quan _âm_ hoàn hảo (*perfectly negatively correlated*). Tài sản 1 và 2 biến động ngược chiều nhau 100% thời gian.

- $\rho_{12} = 0$: Tỷ suất sinh lợi của hai tài sản _không tương quan (*uncorrelated*)_. Sự biến động của Tài sản 1 không cung cấp bất kỳ dự báo nào liên quan đến sự biến động của Tài sản 2.

Hệ số tương quan giữa hai tài sản quyết định tác động lên rủi ro danh mục đầu tư khi hai tài sản được kết hợp với nhau. Để thấy cách thức hoạt động của điều này, hãy xem xét hai giá trị khác nhau của $\rho_{12}$. Bạn sẽ thấy rằng rủi ro danh mục đầu tư không bị ảnh hưởng khi hai tài sản có tương quan hoàn hảo ($\rho_{12} = +1$). Nói cách khác, độ lệch chuẩn của danh mục đầu tư chỉ đơn giản là bình quân gia quyền của độ lệch chuẩn của hai tài sản, và do đó rủi ro của danh mục đầu tư không thay đổi khi bổ sung thêm các tài sản có cùng tham số rủi ro. Tuy nhiên, rủi ro danh mục đầu tư sẽ giảm xuống khi hai tài sản không tương quan hoàn hảo ($\rho_{12} < +1$). Các giá trị đủ thấp của hệ số tương quan có thể làm cho danh mục đầu tư trở nên hoàn toàn phi rủi ro (*riskless*) dưới những điều kiện nhất định.


<!-- PDF Page 35 -->

![](assets/Portfolio_Management.pdf-0035-02.png)

<!-- Formula Text: σ p 2  =  w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 ρ 12 σ 1 σ 2  =  w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 σ 1 σ 2 = (w 1 σ 1 + w 2 σ 2) 2 σ p  =  w 1 σ 1 + w 2 σ 2 -->

$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 = (w_1 \sigma_1 + w_2 \sigma_2)^2$$

$$\sigma_p = w_1 \sigma_1 + w_2 \sigma_2$$

Tập hợp các số hạng đầu tiên ở vế phải của phương trình đầu tiên chứa các số hạng thông thường của phương sai danh mục đầu tư. Bởi vì hệ số tương quan bằng $+1$, vế phải có thể được viết lại thành một bình phương hoàn chỉnh. Dòng thứ ba cho thấy rủi ro của danh mục đầu tư là bình quân gia quyền của rủi ro của từng tài sản riêng lẻ. Trước đó chúng ta đã chỉ ra rằng lợi nhuận của danh mục đầu tư là bình quân gia quyền của lợi nhuận của các tài sản. Bởi vì cả rủi ro và lợi nhuận đều chỉ là bình quân gia quyền của hai tài sản trong danh mục đầu tư, nên không có sự giảm thiểu rủi ro nào khi $\rho_{12} = +1$.

#### **Bây giờ giả sử $\rho_{12} < +1$**

Phân tích ở trên cho thấy rủi ro của danh mục đầu tư là bình quân gia quyền của rủi ro các tài sản khi $\rho_{12} = +1$. Khi $\rho_{12} < +1$, rủi ro của danh mục đầu tư nhỏ hơn bình quân gia quyền của rủi ro từng tài sản riêng lẻ.

Để chứng minh điều này, chúng ta bắt đầu bằng cách viết lại công thức tổng quát của rủi ro danh mục đầu tư, được biểu diễn bằng các số hạng ở bên trái dấu “$<$” dưới đây. Biểu thức ở bên phải dấu “$<$” thể hiện rủi ro danh mục đầu tư khi $\rho_{12} = +1$:

![](assets/Portfolio_Management.pdf-0035-07.png)

<!-- Formula Text: σ p  =  √ ____________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 ρ 12 σ 1 σ 2   <  √ _________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 σ 1 σ 2 = (w 1 σ 1 + w 2 σ 2) σ p  <  (w 1 σ 1 + w 2 σ 2) -->

$$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2} < \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2} = (w_1 \sigma_1 + w_2 \sigma_2)$$

$$\sigma_p < (w_1 \sigma_1 + w_2 \sigma_2)$$

Vế trái nhỏ hơn vế phải bởi vì hệ số tương quan ở vế trái đối với danh mục đầu tư mới nhỏ hơn 1 ($< 1$). Do đó, rủi ro của danh mục đầu tư nhỏ hơn bình quân gia quyền của các rủi ro trong khi lợi nhuận của danh mục đầu tư vẫn là bình quân gia quyền của các lợi nhuận.

Như bạn có thể thấy, chúng ta đã đạt được sự đa dạng hóa bằng cách kết hợp hai tài sản không tương quan hoàn hảo với nhau. Đối với trường hợp cực đoan trong đó $\rho_{12} = -1$ (tức là tỷ suất sinh lợi của hai tài sản biến động ngược chiều nhau), danh mục đầu tư có thể được thiết kế để trở nên hoàn toàn phi rủi ro.

#### **VÍ DỤ 4**

### **Tác động của Hệ số tương quan lên Rủi ro Danh mục Đầu tư (*Effect of Correlation on Portfolio Risk*)**

Hai cổ phiếu có cùng mức lợi nhuận và rủi ro (độ lệch chuẩn): 10% lợi nhuận với 20% rủi ro. Bạn lập một danh mục đầu tư gồm 50% Cổ phiếu 1 và 50% Cổ phiếu 2 để xem xét tác động của hệ số tương quan lên rủi ro.

1. Tính lợi nhuận và rủi ro của danh mục đầu tư nếu hệ số tương quan là 1,0.

**Lời giải:**

$R_1 = R_2 = 10\% = 0,10$; $\sigma_1 = \sigma_2 = 20\% = 0,20$; $w_1 = w_2 = 50\% = 0,50$.
Trường hợp 1: $\rho_{12} = +1$
$$R_p = w_1 R_1 + w_2 R_2$$
$$R_p = (0,5 \times 0,1) + (0,5 \times 0,1) = 0,10 = 10\%$$
$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{12}$$
$$\sigma_p^2 = (0,5^2 \times 0,2^2) + (0,5^2 \times 0,2^2) + (2 \times 0,5 \times 0,5 \times 0,2 \times 0,2 \times 1) = 0,04$$
$$\sigma_p = \sqrt{0,04} = 0,20 = 20\%$$

Phương trình này chứng minh quan điểm đã nêu trước đó rằng với hệ số tương quan bằng 1,0, rủi ro của danh mục đầu tư bằng đúng với rủi ro của các tài sản riêng lẻ.


<!-- PDF Page 36 -->

2. Tính lợi nhuận và rủi ro của danh mục đầu tư nếu hệ số tương quan là 0,0.

**Lời giải:**
$\rho_{12} = 0$
$$R_p = w_1 R_1 + w_2 R_2 = 0,10 = 10\%$$
$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{12}$$
$$\sigma_p^2 = (0,5^2 \times 0,2^2) + (0,5^2 \times 0,2^2) + (2 \times 0,5 \times 0,5 \times 0,2 \times 0,2 \times 0) = 0,02$$
$$\sigma_p = \sqrt{0,02} = 0,14 = 14\%$$

Phương trình này chứng minh quan điểm đã nêu trước đó rằng khi các tài sản có hệ số tương quan nhỏ hơn 1,0, chúng có thể được kết hợp trong một danh mục đầu tư có mức rủi ro thấp hơn so với từng tài sản riêng lẻ.

3. Tính lợi nhuận và rủi ro của danh mục đầu tư nếu hệ số tương quan là –1,0.

**Lời giải:**
$\rho_{12} = -1$
$$R_p = w_1 R_1 + w_2 R_2 = 0,10 = 10\%$$
$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{12}$$
$$\sigma_p^2 = (0,5^2 \times 0,2^2) + (0,5^2 \times 0,2^2) + (2 \times 0,5 \times 0,5 \times 0,2 \times 0,2 \times (-1)) = 0$$
$$\sigma_p = 0\%$$

Phương trình này chứng minh quan điểm đã nêu trước đó rằng nếu hệ số tương quan của các tài sản đủ thấp, trong trường hợp này là tương quan âm 100% hay –1,00 (có mối quan hệ nghịch đảo hoàn toàn), thì có thể thiết kế một danh mục đầu tư giúp loại bỏ hoàn toàn rủi ro. Các tài sản riêng lẻ vẫn giữ nguyên các đặc điểm rủi ro của chúng, nhưng danh mục đầu tư thì hoàn toàn phi rủi ro.

4. So sánh lợi nhuận và rủi ro của các danh mục đầu tư có hệ số tương quan khác nhau.

**Lời giải:**

Tỷ suất sinh lợi kỳ vọng là 10% trong cả ba trường hợp; tuy nhiên, tỷ suất sinh lợi sẽ biến động nhiều hơn trong Trường hợp 1 và ít biến động nhất trong Trường hợp 3. Trong trường hợp thứ nhất, không có sự đa dạng hóa rủi ro (mức rủi ro vẫn giữ nguyên như trước là 20%) và lợi nhuận giữ nguyên. Trong trường hợp thứ hai, với hệ số tương quan bằng 0, chúng ta đã đạt được sự đa dạng hóa rủi ro (rủi ro bây giờ là 14% thay vì 20%), một lần nữa với cùng mức lợi nhuận. Trong trường hợp thứ ba với hệ số tương quan bằng –1, danh mục đầu tư hoàn toàn phi rủi ro, mặc dù chúng ta vẫn tiếp tục nhận được cùng mức lợi nhuận là 10%. Ví dụ này cho thấy sức mạnh của sự đa dạng hóa mà chúng ta sẽ mở rộng thêm trong Phần 9.

#### **_Mối quan hệ giữa Rủi ro và Lợi nhuận Danh mục Đầu tư (Relationship between Portfolio Risk and Return)_**

Ví dụ trước đã minh họa tác động của hệ số tương quan lên rủi ro danh mục đầu tư trong khi giữ tỷ trọng của hai tài sản bằng nhau và không đổi. Trong phần này, chúng ta xem xét cách thức rủi ro và lợi nhuận của danh mục đầu tư thay đổi theo các tỷ trọng danh mục đầu tư khác nhau và các hệ số tương quan khác nhau.

Tài sản 1 có tỷ suất sinh lợi hàng năm là 7% và rủi ro chuẩn hóa theo năm là 12%, trong khi Tài sản 2 có tỷ suất sinh lợi hàng năm là 15% và rủi ro chuẩn hóa theo năm là 25%. Mối quan hệ này được lập bảng trong Bảng minh họa 13 cho hai tài sản và được biểu diễn bằng đồ thị trong Bảng minh họa 14.


<!-- PDF Page 37 -->

**Bảng minh họa 13: Mối quan hệ giữa Rủi ro và Lợi nhuận (*Relationship between Risk and Return*)**

|**Tỷ trọng ở Tài sản 1 (*Weight in Asset 1*) (%)**|**Lợi nhuận Danh mục (*Portfolio Return*)**|**Rủi ro Danh mục với Hệ số tương quan bằng (*Portfolio Risk with Correlation of*)**||||
|---|---|---|---|---|---|
|||**1.0**|**0.5**|**0.2**|**−1.0**|
|0|15.0|25.0|25.0|25.0|25.0|
|10|14.2|23.7|23.1|22.8|21.3|
|20|13.4|22.4|21.3|20.6|17.6|
|30|12.6|21.1|19.6|18.6|13.9|
|40|11.8|19.8|17.9|16.6|10.2|
|50|11.0|18.5|16.3|14.9|6.5|
|60|10.2|17.2|15.0|13.4|2.8|
|70|9.4|15.9|13.8|12.3|0.9|
|80|8.6|14.6|12.9|11.7|4.6|
|90|7.8|13.3|12.2|11.6|8.3|
|100|7.0|12.0|12.0|12.0|12.0|

**Bảng minh họa 14: Mối quan hệ giữa Rủi ro và Lợi nhuận (*Relationship between Risk and Return*)**

![](assets/Portfolio_Management.pdf-0037-06.png)

<!-- Picture Text: = .2<br>14<br> = –1<br> = 1<br>11<br> = .5<br>8<br>5 10 15 20 25<br>Standard Deviation of Portfolio<br>p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn của danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Đồ thị biểu diễn các đường rủi ro – lợi nhuận ứng với bốn mức hệ số tương quan: $\rho = 1$ (đường thẳng), $\rho = 0,5$, $\rho = 0,2$ (các đường cong lồi về bên trái), và $\rho = -1$ (hai đoạn thẳng gấp khúc chạm trục tung tại $\sigma_p = 0$).

Bảng trên cho thấy lợi nhuận và rủi ro của danh mục đầu tư ứng với bốn hệ số tương quan nằm trong khoảng từ $+1,0$ đến $-1,0$ và 11 mức tỷ trọng từ 0% đến 100%. Lợi nhuận và rủi ro của danh mục đầu tư lần lượt là 15% và 25% khi 0% được đầu tư vào Tài sản 1, so với 7% và 12% khi 100% được đầu tư vào Tài sản 1. Lợi nhuận của danh mục đầu tư thay đổi theo tỷ trọng nhưng không bị ảnh hưởng bởi hệ số tương quan.

Rủi ro của danh mục đầu tư trở nên nhỏ hơn sau mỗi lần giảm hệ số tương quan, với mức rủi ro nhỏ nhất khi $\rho_{12} = -1$. Đồ thị trong Bảng minh họa 14 cho thấy mối quan hệ rủi ro – lợi nhuận là một đường thẳng khi $\rho_{12} = +1$. Khi hệ số tương quan


<!-- PDF Page 38 -->

giảm xuống, rủi ro ngày càng trở nên nhỏ hơn như trong bảng. Bản chất đường cong (*curvilinear nature*) của một danh mục các tài sản có thể nhận thấy rõ trong tất cả các tập hợp cơ hội đầu tư (ngoại trừ tại hai thái cực nơi $\rho_{12} = -1$ hoặc $+1$).

#### **VÍ DỤ 5**

### **Danh mục Đầu tư gồm Hai Tài sản (*Portfolio of Two Assets*)**

Giả sử bạn là một nhà đầu tư tại Vương quốc Anh (UK) đang nắm giữ một danh mục đầu tư gồm 60% được đầu tư vào cổ phiếu vốn hóa lớn của Anh (được đại diện bởi Chỉ số FTSE 100) và 40% vào trái phiếu Kho bạc kỳ hạn trung bình trong nước (“gilts”). Tỷ suất sinh lợi kỳ vọng của FTSE 100 là 5,5% và của trái phiếu chính phủ Anh (gilts) kỳ hạn trung bình là 0,7%. Rủi ro (độ lệch chuẩn của tỷ suất sinh lợi) lần lượt là 13,2% và 4,2%. Hệ số tương quan giữa hai tài sản là –0,01.

Tỷ suất sinh lợi kỳ vọng của danh mục đầu tư này là:

$$R_p = w_1 \times R_1 + (1 - w_1) \times R_2 = 0,6 \times 0,055 + 0,4 \times 0,007 = 0,0358 \approx 3,6\%$$

Rủi ro của danh mục đầu tư này là:

![](assets/Portfolio_Management.pdf-0038-10.png)

<!-- Formula Text: σ p  =  √ __________________________________ w 1 2 σ 1 2   +   w 2 2 σ 2 2 + 2 × w 1 w 2 × ρ × σ 1 σ 2 . σ p= √ ____________________________________________________________ (0.6 2 × 0.132 2) + (0.4 2 × 0.042 2) + 2 × 0.6 × 0.4 × − 0.01 × 0.132 × 0.042 . -->

$$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 \times w_1 w_2 \times \rho \times \sigma_1 \sigma_2}$$

$$\sigma_p = \sqrt{(0,6^2 \times 0,132^2) + (0,4^2 \times 0,042^2) + 2 \times 0,6 \times 0,4 \times (-0,01) \times 0,132 \times 0,042}$$

$$\sigma_p = 0,0808 \approx 8,1\%$$

Bạn nhận thấy rằng so với trái phiếu Kho bạc Hoa Kỳ (*US Treasury bonds*), tỷ suất sinh lợi kỳ vọng của trái phiếu chính phủ Anh (gilts) thấp hơn và rủi ro của gilts lại cao hơn. Trái phiếu Kho bạc Hoa Kỳ có tỷ suất sinh lợi kỳ vọng đối với một nhà đầu tư tại Hoa Kỳ là 1,5% và rủi ro là 4,0%. Bạn tự hỏi liệu việc thay thế gilts trong danh mục đầu tư của mình bằng trái phiếu Kho bạc Hoa Kỳ (“Treasuries”) có cải thiện hồ sơ rủi ro và lợi nhuận của danh mục đầu tư hay không.

1. Các giả định về rủi ro và lợi nhuận đã cho đối với trái phiếu Kho bạc Hoa Kỳ có cho phép bạn, với tư cách là một nhà đầu tư tại Anh, tính toán tỷ suất sinh lợi kỳ vọng và rủi ro của danh mục đầu tư khi thay thế trái phiếu chính phủ Anh bằng trái phiếu Kho bạc Hoa Kỳ hay không?

#### **Lời giải:**

Không. Tỷ suất sinh lợi kỳ vọng và rủi ro đối với Trái phiếu Kho bạc Hoa Kỳ áp dụng cho một nhà đầu tư Hoa Kỳ, người đầu tư bằng đồng đô la Mỹ (USD). Để tính toán tỷ suất sinh lợi kỳ vọng và rủi ro bằng đồng bảng Anh (sterling – GBP) cho một danh mục đầu tư tại Anh gồm cổ phiếu FTSE 100 và Trái phiếu Kho bạc Hoa Kỳ, người ta cần phải tính đến tỷ giá hối đoái (*exchange rate*) giữa đồng đô la Mỹ và đồng bảng Anh. Tỷ giá hối đoái này có độ biến động (rủi ro) riêng của nó, và kỳ vọng lợi nhuận đối với tỷ giá hối đoái GBP/USD phải được xác định rõ. Nhằm mục đích tính toán lợi nhuận và rủi ro của một tài sản nước ngoài trong danh mục đầu tư của một nhà đầu tư trong nước, tài sản nước ngoài đó có thể được xem như một “danh mục đầu tư” gồm hai tài sản. Tỷ suất sinh lợi của một tài sản nước ngoài tính bằng đồng nội tệ (*domestic currency* – tức là đồng tiền không phải ngoại tệ) có thể được phân tách thành một cấu phần lợi nhuận bằng đồng bản tệ (*local currency return component*) và một cấu phần tỷ giá hối đoái (*exchange rate component*):

$$R_D = (1 + R_{lc}) \times (1 + R_{FX}) - 1$$

Bởi vì danh mục đầu tư chịu toàn bộ rủi ro trước sự biến động của cả giá trị tài sản tính bằng đồng bản tệ và tỷ giá hối đoái tiền tệ, nên đồng ngoại tệ và tài sản đó mỗi thứ đều có tỷ trọng danh mục là 100%. Lưu ý rằng tỷ giá hối đoái phải được yết giá theo dạng đồng nội tệ/đồng ngoại tệ (*domestic currency/foreign currency*) để quy đổi tỷ suất sinh lợi bằng đồng ngoại tệ sang đồng nội tệ của nhà đầu tư. Rủi ro có thể được tính toán như sau:


<!-- PDF Page 39 -->

![](assets/Portfolio_Management.pdf-0039-02.png)

<!-- Formula Text: σ D  =  √ _____________________________________ w 1 2 σ lc 2    +   w 2 2 σ FX 2   + 2 × w 1 w 2 × ρ × σ lc σ FX =  √ _________________________ σ lc 2  + σ FX 2   + 2 × ρ × σ lc × σ FX . -->

$$\sigma_D = \sqrt{w_1^2 \sigma_{lc}^2 + w_2^2 \sigma_{FX}^2 + 2 \times w_1 w_2 \times \rho \times \sigma_{lc} \sigma_{FX}} = \sqrt{\sigma_{lc}^2 + \sigma_{FX}^2 + 2 \times \rho \times \sigma_{lc} \times \sigma_{FX}}$$

Giả sử trong phần tiếp theo rằng rủi ro (được đo lường bằng độ lệch chuẩn kỳ vọng) của tỷ giá hối đoái tiền tệ GBP/USD là 9,0% và tỷ suất sinh lợi của Trái phiếu Kho bạc Hoa Kỳ có hệ số tương quan với tỷ giá hối đoái GBP/USD là 0,33. Giả sử thêm rằng bạn không có dự báo nào về giá trị tương lai của tỷ giá hối đoái USD/GBP, và do đó giả định mức sinh lợi tỷ giá bằng 0%.

2. Rủi ro kỳ vọng của Trái phiếu Kho bạc Hoa Kỳ đối với bạn, với tư cách là một nhà đầu tư tại Anh, sẽ là bao nhiêu?

**Lời giải:**

![](assets/Portfolio_Management.pdf-0039-05.png)

<!-- Formula Text: σ D  =    √ _________________________ σ lc 2  + σ FX 2   + 2 × ρ × σ lc × σ FX =  √ ____________________________________ 0.040 2 + 0.090 2 + 2 × 0.33 × 0.040 + 0.090 . -->

$$\sigma_D = \sqrt{\sigma_{lc}^2 + \sigma_{FX}^2 + 2 \times \rho \times \sigma_{lc} \times \sigma_{FX}} = \sqrt{0,040^2 + 0,090^2 + 2 \times 0,33 \times 0,040 \times 0,090}$$

$$\sigma_D = 0,110 = 11,0\%$$

Hệ số tương quan giữa FTSE 100, Trái phiếu Kho bạc Hoa Kỳ (*US Treasuries*), và tỷ giá hối đoái USD/GBP được mô tả trong ma trận tương quan (*correlation matrix*) sau đây.

||**FTSE 100**|**Trái phiếu Kho bạc Hoa Kỳ (*US Treasuries*)**|**GBP/USD**|
|---|---|---|---|
|FTSE 100|1.00|–0.32|–0.06|
|Trái phiếu Kho bạc Hoa Kỳ (*US Treasuries*)|–0.32|1.00|0.33|
|GBP/USD|–0.06|0.33|1.00|

3. Tỷ suất sinh lợi kỳ vọng và rủi ro đối với danh mục đầu tư của bạn sẽ là bao nhiêu nếu bạn thay thế trái phiếu chính phủ Anh (gilts) bằng Trái phiếu Kho bạc Hoa Kỳ?

   - **Lời giải:**

Tỷ suất sinh lợi kỳ vọng là bình quân gia quyền của tỷ suất sinh lợi kỳ vọng tính bằng đồng bảng Anh (GBP) của cổ phiếu vốn hóa lớn tại Anh và của Trái phiếu Kho bạc Hoa Kỳ. Hãy nhớ lại rằng tỷ suất sinh lợi của một tài sản nước ngoài tính bằng đồng nội tệ bao gồm một cấu phần ngoại tệ và một cấu phần bản thân tài sản đó. Tất cả các tỷ suất sinh lợi kỳ vọng có thể được tìm thấy ở trên.

$$R_p = w_1 \times R_1 + (1 - w_1) \times [(1 + R_{lc}) \times (1 + R_{FX}) - 1]$$

$$R_p = 0,6 \times 0,055 + 0,4 \times [(1 + 0,015) \times (1 + 0,0) - 1] = 0,039 = 3,9\%$$

Việc tính toán rủi ro của danh mục đầu tư liên quan đến một công thức phức tạp hơn một chút. Hãy nhớ lại rằng rủi ro của một danh mục đầu tư gồm hai tài sản phụ thuộc vào rủi ro và tỷ trọng của từng tài sản riêng lẻ cùng sự biến động cùng chiều (*co-movements*) giữa hai tài sản đó. Đối với một danh mục đầu tư gồm ba tài sản (một phần cổ phiếu, một phần thu nhập cố định nước ngoài, và mức tiếp xúc rủi ro ngoại tệ đi kèm), phép tính về cơ bản là giống nhau, tuy nhiên có ba cặp biến động cùng chiều giữa các tài sản thay vì chỉ một cặp.

Do đó, công thức tính độ lệch chuẩn của một danh mục đầu tư gồm ba tài sản là:

![](assets/Portfolio_Management.pdf-0039-16.png)

<!-- Formula Text: σ p  =  √ _______________________________________________________________________ w 1 2 σ 1 2   +   w 2 2 σ 2 2   +   w 3 2 σ 3 2 + 2 ρ 1,2 w 1 w 2 σ 1 σ 2 + 2 ρ 1,3 w 1 w 3 σ 1 σ 3 + 2 ρ 2,3 w 2 w 3 σ 2 σ 3 . -->

$$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + w_3^2 \sigma_3^2 + 2 \rho_{1,2} w_1 w_2 \sigma_1 \sigma_2 + 2 \rho_{1,3} w_1 w_3 \sigma_1 \sigma_3 + 2 \rho_{2,3} w_2 w_3 \sigma_2 \sigma_3}$$

Tỷ trọng danh mục đầu tư của mức tiếp xúc rủi ro ngoại tệ bằng với tỷ trọng danh mục đầu tư của Trái phiếu Kho bạc Hoa Kỳ. Sử dụng thông tin được cung cấp ở trên, chúng ta có thể tính toán rủi ro của danh mục đầu tư gồm cổ phiếu vốn hóa lớn của Anh và Trái phiếu Kho bạc Hoa Kỳ như sau:


<!-- PDF Page 40 -->

$$\sigma_p = \left(0,6^2 \times 0,132^2 + 0,4^2 \times 0,040^2 + 0,4^2 \times 0,090^2 + 2 \times (-0,32) \times 0,6 \times 0,4 \times 0,132 \times 0,040 + 2 \times (-0,06) \times 0,6 \times 0,4 \times 0,132 \times 0,090 + 2 \times 0,33 \times 0,4 \times 0,4 \times 0,040 \times 0,090\right)^{1/2}$$

$$\sigma_p = 0,0841 \approx 8,4\%$$

So với danh mục đầu tư cổ phiếu Anh/trái phiếu chính phủ Anh (gilts), danh mục đầu tư cổ phiếu Anh/Trái phiếu Kho bạc Hoa Kỳ có tỷ suất sinh lợi kỳ vọng cao hơn, bởi vì trái phiếu chính phủ Anh đã được thay thế bằng một tài sản có kỳ vọng sinh lợi vượt trội hơn. Tuy nhiên, rủi ro của danh mục đầu tư mới lại cao hơn một chút bất chấp mức rủi ro tính theo đồng bản tệ của Trái phiếu Kho bạc Hoa Kỳ thấp hơn so với gilts. Việc sở hữu Trái phiếu Kho bạc Hoa Kỳ với tư cách là một nhà đầu tư ngoài Hoa Kỳ đồng nghĩa với việc phải chịu rủi ro tỷ giá hối đoái (*exchange rate risk*), điều cần phải được cân nhắc khi đánh giá hồ sơ rủi ro.

# **<mark>8</mark> DANH MỤC ĐẦU TƯ GỒM NHIỀU TÀI SẢN RỦI RO (*PORTFOLIO OF MANY RISKY ASSETS*)**

tính toán và diễn giải độ lệch chuẩn của danh mục đầu tư (*portfolio standard deviation*)
mô tả tác động lên rủi ro của danh mục đầu tư khi đầu tư vào các tài sản có tương quan nhỏ hơn mức tương quan hoàn hảo (*less than perfectly correlated*)

Trong phần trước, chúng ta đã thảo luận về cách hệ số tương quan giữa hai tài sản có thể ảnh hưởng đến rủi ro của một danh mục đầu tư và hệ số tương quan càng nhỏ thì rủi ro càng thấp. Phân tích ở trên có thể được mở rộng cho một danh mục đầu tư gồm nhiều tài sản rủi ro ($N$). Hãy nhớ lại các phương trình trước đó về lợi nhuận và phương sai của danh mục đầu tư:

![](assets/Portfolio_Management.pdf-0040-10.png)

<!-- Formula Text: E(R p)  =  ∑ i=1 N w i E(R i),    σ P 2   =  (∑ i=1 N w i 2 σ i 2 +   ∑ i,j=1,i≠j N w i w jCov(i, j)),  ∑ i=1 N w i  =  1 -->

$$E(R_p) = \sum_{i=1}^{N} w_i E(R_i), \quad \sigma_P^2 = \left(\sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i,j=1, i \neq j}^{N} w_i w_j \text{Cov}(i, j)\right), \quad \sum_{i=1}^{N} w_i = 1$$

Để xem xét cách thức hoạt động của một danh mục đầu tư gồm nhiều tài sản rủi ro và các cách thức mà chúng ta có thể làm giảm rủi ro của một danh mục đầu tư, hãy giả sử rằng danh mục đầu tư có tỷ trọng bằng nhau ($1/N$) cho tất cả $N$ tài sản. Ngoài ra, giả sử rằng $\bar{\sigma}^2$ và $\overline{\text{Cov}}$ là phương sai trung bình (*average variance*) và hiệp phương sai trung bình (*average covariance*). Với các tỷ trọng bằng nhau và phương sai/hiệp phương sai trung bình, chúng ta có thể viết lại phương sai của danh mục đầu tư như dưới đây (các bước trung gian được lược bỏ để tập trung vào kết quả chính):

![](assets/Portfolio_Management.pdf-0040-12.png)

<!-- Formula Text: σ P 2   =  (∑ i=1 N w i 2 σ i 2 +   ∑ i,j=1,i≠j N w i w jCov(i, j)) σ P 2   =    _ σ  2 _ N  +  (N − 1) _ N  ‾ Cov -->

$$\sigma_P^2 = \left(\sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i,j=1, i \neq j}^{N} w_i w_j \text{Cov}(i, j)\right)$$

$$\sigma_P^2 = \frac{\bar{\sigma}^2}{N} + \frac{(N - 1)}{N} \overline{\text{Cov}}$$

Phương trình ở dòng thứ hai cho thấy rằng khi $N$ trở nên lớn, số hạng đầu tiên ở vế phải với mẫu số là $N$ ngày càng trở nên nhỏ hơn, ngụ ý rằng mức đóng góp của phương sai một tài sản đơn lẻ vào phương sai của danh mục đầu tư dần dần trở nên không đáng kể (*negligible*). Tuy nhiên, số hạng thứ hai lại tiến dần đến hiệp phương sai trung bình khi $N$ tăng lên. Hoàn toàn hợp lý khi nói rằng đối với các danh mục đầu tư có số lượng lớn tài sản, hiệp phương sai giữa các tài sản chiếm gần như toàn bộ rủi ro của danh mục đầu tư.

### **Tầm quan trọng của Hệ số tương quan trong một Danh mục Đầu tư gồm Nhiều Tài sản (*Importance of Correlation in a Portfolio of Many Assets*)**

Phân tích sẽ trở nên giàu tính minh họa và thú vị hơn nếu chúng ta giả định rằng tất cả các tài sản trong danh mục đầu tư có cùng phương sai và cùng hệ số tương quan giữa các tài sản. Trong trường hợp đó, rủi ro của danh mục đầu tư có thể được viết lại thành:


---

# Tập 9: Quản lý Danh mục Đầu tư (*Portfolio Management*)
## Học phần 1: Rủi ro và Lợi nhuận Danh mục Đầu tư: Phần I (*Portfolio Risk and Return: Part I*)
### Phần 3/4: Sức mạnh của Đa dạng hóa (*The Power of Diversification*) (Trang PDF 41–56)

---

<!-- PDF Page 41 -->

![](assets/Portfolio_Management.pdf-0041-02.png)

<!-- Formula Text: σ p  =  √ _____________ σ 2 _ N  +  (N − 1) _ N  ρ σ 2 -->

$$\sigma_p = \sqrt{\frac{\sigma^2}{N} + \frac{(N - 1)}{N} \rho \sigma^2}$$

Số hạng đầu tiên dưới dấu căn trở nên không đáng kể khi số lượng tài sản trong danh mục đầu tư tăng lên, để lại số hạng thứ hai (hệ số tương quan) là yếu tố quyết định chính đối với rủi ro của danh mục đầu tư. Nếu các tài sản không có mối liên hệ nào với nhau ($\rho = 0$), danh mục đầu tư có thể có mức rủi ro gần như bằng không. Trong phần tiếp theo, chúng ta sẽ xem xét lại các khái niệm này để tìm hiểu cách thức đa dạng hóa danh mục đầu tư.

## **SỨC MẠNH CỦA ĐA DẠNG HÓA (*THE POWER OF DIVERSIFICATION*)**

![](assets/Portfolio_Management.pdf-0041-05.png)

<!-- Picture Text: 9<br> -->

mô tả đặc điểm của các nhóm tài sản chính (*major asset classes*) mà nhà đầu tư xem xét khi hình thành danh mục đầu tư

mô tả tác động lên rủi ro của danh mục đầu tư khi đầu tư vào các tài sản có tương quan nhỏ hơn mức tương quan hoàn hảo (*less than perfectly correlated*)

Đa dạng hóa (*diversification*) là một trong những khái niệm quan trọng và mạnh mẽ nhất trong đầu tư. Bởi vì các nhà đầu tư là những người ngại rủi ro, họ luôn quan tâm đến việc giảm thiểu rủi ro mà tốt nhất là không làm giảm lợi nhuận. Trong những trường hợp khác, các nhà đầu tư có thể chấp nhận mức lợi nhuận thấp hơn nếu điều đó giúp làm giảm khả năng xảy ra những khoản lỗ thảm khốc (*catastrophic losses*). Trong các phần trước của bài đọc này, bạn đã tìm hiểu về tầm quan trọng của hệ số tương quan (*correlation*) và hiệp phương sai (*covariance*) trong việc quản lý rủi ro. Phần này áp dụng các khái niệm đó để khám phá những cách thức đa dạng hóa rủi ro. Chúng ta bắt đầu bằng một ví dụ đơn giản nhưng trực quan.

#### **VÍ DỤ 6**

### **Đa dạng hóa với Mưa và Nắng (*Diversification with Rain and Shine*)**

Giả sử một công ty có tên là Beachwear chuyên cho thuê thiết bị bãi biển. Tỷ suất sinh lợi hàng năm từ hoạt động kinh doanh của công ty là 20% vào những năm có nhiều ngày nắng nhưng giảm xuống mức 0% vào những năm mưa nhiều với ít ngày nắng. Xác suất của một năm nắng nhiều và một năm mưa nhiều là bằng nhau ở mức 50%. Do đó, tỷ suất sinh lợi trung bình là 10%, với 50% cơ hội đạt lợi nhuận 20% và 50% cơ hội đạt lợi nhuận 0%. Bởi vì Beachwear có thể kiếm được lợi nhuận 20% hoặc 0%, nên tỷ suất sinh lợi trung bình 10% của nó có rủi ro.

Bạn rất hào hứng với việc đầu tư vào Beachwear nhưng lại không thích rủi ro đó. Sau khi nghe nói về sự đa dạng hóa, bạn quyết định bổ sung thêm một doanh nghiệp khác vào danh mục đầu tư để giảm thiểu rủi ro đầu tư của mình.

- Có một cửa hàng đồ ăn nhẹ trên bãi biển (*Snackshop*) chuyên bán tất cả các loại thực phẩm lành mạnh mà bạn yêu thích. Bạn ước tính rằng tỷ suất sinh lợi hàng năm từ Snackshop cũng là 20% vào những năm có nhiều ngày nắng và 0% vào những năm khác. Giống như cửa hàng Beachwear, tỷ suất sinh lợi trung bình là 10%.

Bạn quyết định đầu tư 50% vào Snackshop và 50% vào Beachwear. Tỷ suất sinh lợi trung bình vẫn là 10%, với 50% của 10% từ Snackshop và 50% của 10% từ Beachwear. Vào một năm nắng nhiều, bạn sẽ kiếm được 20% ($= 50\%$ của $20\%$ từ Beachwear $+ 50\%$ của $20\%$ từ Snackshop). Vào một năm mưa nhiều, bạn sẽ kiếm được 0% ($= 50\%$ của $0\%$ từ Beachwear $+ 50\%$ của $0\%$ từ Snackshop). Kết quả được lập bảng trong Bảng minh họa 15.


<!-- PDF Page 42 -->

#### **Bảng minh họa 15**

|**Loại hình (*Type*)**|**Công ty (*Company*)**|**Phần trăm Đầu tư (*Percent Invested*)**|**Lợi nhuận trong Năm Nắng (*Return in Sunny Year*) (%)**|**Lợi nhuận trong Năm Mưa (*Return in Rainy Year*) (%)**|**Lợi nhuận Trung bình (*Average Return*) (%)**|
|---|---|---|---|---|---|
|Cổ phiếu đơn lẻ (*Single stock*)|Beachwear|100|20|0|10|
|Cổ phiếu đơn lẻ (*Single stock*)|Snackshop|100|20|0|10|
|Danh mục hai cổ phiếu (*Portfolio of two stocks*)|Beachwear|50|20|0|10|
||Snackshop|50|20|0|10|
||Tổng cộng (*Total*)|100|20|0|10|

Những kết quả này có vẻ trái ngược với trực giác. Bạn đã nghĩ rằng bằng cách bổ sung thêm một doanh nghiệp khác, bạn sẽ có thể đa dạng hóa và giảm thiểu rủi ro của mình, nhưng rủi ro vẫn hoàn toàn giống hệt như trước. Điều gì đã sai ở đây? Hãy lưu ý rằng cả hai doanh nghiệp đều ăn nên làm ra khi trời nắng và cả hai doanh nghiệp đều làm ăn kém khi trời mưa. Hệ số tương quan giữa hai doanh nghiệp là $+1,0$. Không có sự giảm thiểu rủi ro nào xảy ra khi hệ số tương quan bằng $+1,0$.

- Để giảm thiểu rủi ro, bạn phải xem xét một doanh nghiệp ăn nên làm ra vào một năm mưa nhiều. Bạn tìm thấy một công ty chuyên cho thuê đĩa DVD (*DVDrental*). Công ty DVDrental tương tự như công ty Beachwear, ngoại trừ việc tỷ suất sinh lợi hàng năm của nó là 20% vào năm mưa nhiều và 0% vào năm nắng nhiều, với tỷ suất sinh lợi trung bình là 10%. Tỷ suất sinh lợi 10% của DVDrental cũng có rủi ro giống hệt như tỷ suất sinh lợi của Beachwear.

Nếu bạn đầu tư 50% vào DVDrental và 50% vào Beachwear, thì tỷ suất sinh lợi trung bình vẫn là 10%, với 50% của 10% từ DVDrental và 50% của 10% từ Beachwear. Vào một năm nắng nhiều, bạn sẽ kiếm được 10% ($= 50\%$ của $20\%$ từ Beachwear $+ 50\%$ của $0\%$ từ DVDrental). Vào một năm mưa nhiều, bạn cũng sẽ kiếm được 10% ($= 50\%$ của $0\%$ từ Beachwear $+ 50\%$ của $20\%$ từ DVDrental). Bạn không chịu bất kỳ rủi ro nào bởi vì bạn đều kiếm được 10% trong cả những năm nắng và những năm mưa. Như vậy, bằng cách kết hợp DVDrental vào Beachwear, bạn đã làm giảm (loại bỏ hoàn toàn) rủi ro của mình mà không làm ảnh hưởng đến lợi nhuận. Kết quả được lập bảng trong Bảng minh họa 16.

#### **Bảng minh họa 16**

|**Loại hình (*Type*)**|**Công ty (*Company*)**|**Phần trăm Đầu tư (*Percent Invested*)**|**Lợi nhuận trong Năm Nắng (*Return in Sunny Year*) (%)**|**Lợi nhuận trong Năm Mưa (*Return in Rainy Year*) (%)**|**Lợi nhuận Trung bình (*Average Return*) (%)**|
|---|---|---|---|---|---|
|Cổ phiếu đơn lẻ (*Single stock*)|Beachwear|100|20|0|10|
|Cổ phiếu đơn lẻ (*Single stock*)|DVDrental|100|0|20|10|
|Danh mục hai cổ phiếu (*Portfolio of two stocks*)|Beachwear|50|20|0|10|
||DVDrental|50|0|20|10|
||Tổng cộng (*Total*)|100|10|10|10|


<!-- PDF Page 43 -->

Trong trường hợp này, hai doanh nghiệp có hệ số tương quan là –1,0. Khi hai doanh nghiệp có hệ số tương quan –1,0 được kết hợp với nhau, rủi ro luôn có thể được giảm xuống bằng không.

### **Hệ số tương quan và Đa dạng hóa Rủi ro (*Correlation and Risk Diversification*)**

Hệ số tương quan chính là chìa khóa trong việc đa dạng hóa rủi ro. Hãy lưu ý rằng tỷ suất sinh lợi từ Beachwear và DVDrental luôn biến động theo hướng ngược chiều nhau. Nếu một công ty làm ăn tốt thì công ty kia sẽ kém đi. Do đó, việc bổ sung các tài sản không hành xử giống như các tài sản khác trong danh mục đầu tư của bạn là điều tốt và có thể làm giảm rủi ro. Hai công ty trong ví dụ trên có hệ số tương quan là –1,0.

Ngay cả khi chúng ta mở rộng danh mục đầu tư ra nhiều tài sản, hệ số tương quan giữa các tài sản vẫn là yếu tố quyết định chính đối với rủi ro của danh mục đầu tư. Hệ số tương quan thấp hơn gắn liền với mức rủi ro thấp hơn. Thật không may, hầu hết các tài sản đều có hệ số tương quan dương cao. Thách thức trong việc đa dạng hóa rủi ro là tìm kiếm được những tài sản có hệ số tương quan thấp hơn nhiều so với $+1,0$.

### **Rủi ro và Hệ số tương quan Lịch sử (*Historical Risk and Correlation*)**

Khi chúng ta thảo luận về tỷ suất sinh lợi của tài sản trước đó, chúng ta đã cẩn thận phân biệt giữa tỷ suất sinh lợi lịch sử (hay quá khứ) và tỷ suất sinh lợi kỳ vọng (hay tương lai) bởi vì tỷ suất sinh lợi lịch sử có thể không phải là một chỉ báo tốt cho tỷ suất sinh lợi tương lai. Tỷ suất sinh lợi có thể dương rất cao trong giai đoạn này và âm rất sâu trong một giai đoạn khác tùy thuộc vào rủi ro của tài sản đó. Bảng minh họa 1 cho thấy tỷ suất sinh lợi đối với cổ phiếu các công ty lớn của Hoa Kỳ rất cao vào những năm 1990 nhưng lại rất thấp vào những năm 2000.

Tuy nhiên, rủi ro đối với một nhóm tài sản thường không thay đổi đột ngột từ giai đoạn này sang giai đoạn tiếp theo. Cổ phiếu vẫn luôn rủi ro ngay cả trong những giai đoạn có tỷ suất sinh lợi thấp. Tín phiếu Kho bạc (*T-bills*) luôn ít rủi ro hơn ngay cả khi chúng mang lại tỷ suất sinh lợi cao. Từ Bảng minh họa 1, chúng ta có thể thấy rằng rủi ro thường không thay đổi nhiều từ thập kỷ này sang thập kỷ tiếp theo, ngoại trừ việc rủi ro đối với trái phiếu đã cao hơn nhiều trong những thập kỷ gần đây khi so sánh với các thập kỷ trước đó. Do đó, không có gì là bất hợp lý khi giả định rằng rủi ro lịch sử (*historical risk*) có thể đóng vai trò là một đại diện tốt (*good proxy*) cho rủi ro tương lai.

Giống như rủi ro, hệ số tương quan khá ổn định giữa các tài sản trong cùng một quốc gia. Tuy nhiên, hệ số tương quan giữa các quốc gia (*intercountry correlations*) đã có xu hướng gia tăng trong vài thập kỷ qua như một hệ quả của quá trình toàn cầu hóa (*globalization*) và tự do hóa (*liberalization*) của nhiều nền kinh tế. Một hệ số tương quan trên 0,90 được coi là cao bởi vì các tài sản không mang lại nhiều cơ hội để đa dạng hóa rủi ro. Hệ số tương quan thấp—nhìn chung nhỏ hơn 0,50—là mức đáng mong muốn để đa dạng hóa danh mục đầu tư.

### **Hệ số tương quan Lịch sử giữa các Nhóm Tài sản (*Historical Correlation among Asset Classes*)**

Hệ số tương quan giữa các nhóm tài sản chính của Hoa Kỳ và cổ phiếu quốc tế được báo cáo trong Bảng minh họa 17 cho giai đoạn 1970–2017. Hệ số tương quan cao nhất là giữa cổ phiếu công ty lớn của Hoa Kỳ và cổ phiếu công ty nhỏ của Hoa Kỳ ở mức khoảng 70% (0,72), trong khi hệ số tương quan giữa cổ phiếu công ty lớn của Hoa Kỳ và cổ phiếu quốc tế là xấp xỉ 66%. Mặc dù đây là những mức tương quan cao nhất, chúng vẫn mang lại lợi ích đa dạng hóa bởi vì các hệ số tương quan này nhỏ hơn 100%. Hệ số tương quan giữa cổ phiếu quốc tế và cổ phiếu công ty nhỏ của Hoa Kỳ thấp hơn, ở mức 50%. Các mức tương quan thấp nhất


<!-- PDF Page 44 -->

là giữa cổ phiếu và trái phiếu, với một số hệ số tương quan mang giá trị âm, chẳng hạn như giữa cổ phiếu công ty nhỏ của Hoa Kỳ và trái phiếu chính phủ dài hạn của Hoa Kỳ. Tương tự, hệ số tương quan giữa tín phiếu Kho bạc và cổ phiếu gần như bằng không.<sup>4</sup>

**Bảng minh họa 17: Hệ số tương quan giữa các Tài sản Hoa Kỳ và Cổ phiếu Quốc tế (1970–2017) (*Correlation Among US Assets and International Stocks (1970–2017)*)**

|**Chuỗi tài sản (*Series*)**|**Cổ phiếu Quốc tế (*International Stocks*)**|**Cổ phiếu Công ty Lớn Hoa Kỳ (*US Large Company Stocks*)**|**Cổ phiếu Công ty Nhỏ Hoa Kỳ (*US Small Company Stocks*)**|**Trái phiếu Doanh nghiệp Dài hạn Hoa Kỳ (*US Long-Term Corporate Bonds*)**|**Trái phiếu Kho bạc Dài hạn Hoa Kỳ (*US Long-Term Treasury Bonds*)**|**Tín phiếu Kho bạc Hoa Kỳ (*US T-Bills*)**|**Lạm phát Hoa Kỳ (*US Inflation*)**|
|---|---|---|---|---|---|---|---|
|Cổ phiếu quốc tế (*International stocks*)|1.00|||||||
|Cổ phiếu công ty lớn Hoa Kỳ (*US large company stocks*)|0.66|1.00||||||
|Cổ phiếu công ty nhỏ Hoa Kỳ (*US small company stocks*)|0.50|0.72|1.00|||||
|Trái phiếu doanh nghiệp dài hạn Hoa Kỳ (*US long-term corporate bonds*)|0.02|0.23|0.06|1.00||||
|Trái phiếu Kho bạc dài hạn Hoa Kỳ (*US long-term Treasury bonds*)|−0.13|0.01|−0.15|0.89|1.00|||
|Tín phiếu Kho bạc Hoa Kỳ (*US T-bills*)|0.01|0.04|0.02|0.05|0.09|1.00||
|Lạm phát Hoa Kỳ (*US inflation*)|−0.06|−0.11|0.04|−0.32|−0.26|0.69|1.00|

_Nguồn:_ Niên giám SBBI 2018 (Bảng 12.13).

Hệ số tương quan thấp giữa cổ phiếu và trái phiếu rất hấp dẫn cho việc đa dạng hóa danh mục đầu tư. Tương tự, việc đưa các chứng khoán quốc tế vào danh mục đầu tư cũng có thể kiểm soát rủi ro danh mục đầu tư. Không có gì đáng ngạc nhiên khi hầu hết các danh mục đầu tư đa dạng hóa của nhà đầu tư đều bao gồm cổ phiếu trong nước, trái phiếu trong nước, cổ phiếu nước ngoài, trái phiếu nước ngoài, bất động sản (*real estate*), tiền mặt, và các nhóm tài sản khác.

### **Các Phương thức Đa dạng hóa (*Avenues for Diversification*)**

Lý do cho việc đa dạng hóa rất đơn giản. Bằng cách xây dựng một danh mục đầu tư gồm các tài sản không biến động cùng chiều với nhau, bạn tạo ra một danh mục đầu tư giúp giảm bớt những thăng trầm trong ngắn hạn nhưng vẫn tiếp tục tăng trưởng ổn định trong dài hạn. Do đó, đa dạng hóa làm cho danh mục đầu tư có khả năng chống chịu tốt hơn trước những biến động dữ dội trên thị trường tài chính.

Chúng tôi mô tả một số phương pháp tiếp cận để đa dạng hóa, một số phương pháp trong đó đã được thảo luận trước đây và một số phương pháp có vẻ quá hiển nhiên. Tuy nhiên, đa dạng hóa là một phần quan trọng của hoạt động đầu tư đến mức không bao giờ là thừa khi nhấn mạnh về nó, đặc biệt là khi chúng ta vẫn tiếp tục gặp và chứng kiến nhiều nhà đầu tư chưa thực hiện đa dạng hóa đúng cách.

- _Đa dạng hóa bằng các nhóm tài sản (Diversify with asset classes)._ Hệ số tương quan giữa các nhóm tài sản chính<sup>5</sup> thường không cao, như có thể quan sát thấy từ một vài nhóm tài sản của Hoa Kỳ được liệt kê trong Bảng minh họa 17. Hệ số tương quan đối với các nhóm tài sản khác và các quốc gia khác cũng thường ở mức thấp, điều này mang lại cho các nhà đầu tư cơ hội hưởng lợi từ việc đa dạng hóa giữa nhiều nhóm tài sản để đạt được lợi ích lớn nhất từ sự đa dạng hóa. Một danh sách không đầy đủ của các nhóm tài sản bao gồm: cổ phiếu vốn hóa lớn trong nước (*domestic large caps*), cổ phiếu vốn hóa nhỏ trong nước (*domestic small caps*), cổ phiếu tăng trưởng (*growth stocks*), cổ phiếu giá trị (*value stocks*), trái phiếu doanh nghiệp trong nước, trái phiếu chính phủ dài hạn trong nước, tín phiếu Kho bạc trong nước (tiền mặt),

> 4 Trong bất kỳ khoảng thời gian ngắn nào, tín phiếu Kho bạc hoàn toàn phi rủi ro và không tương quan với các nhóm tài sản khác. Ví dụ, một tín phiếu Kho bạc Hoa Kỳ kỳ hạn 3 tháng được thanh toán bằng đúng mệnh giá khi đáo hạn bất kể điều gì xảy ra với các tài sản khác. Tuy nhiên, khi chúng ta xem xét nhiều kỳ, tỷ suất sinh lợi của tín phiếu Kho bạc có thể có liên hệ với các nhóm tài sản khác bởi vì lãi suất ngắn hạn thay đổi tùy thuộc vào sức mạnh của nền kinh tế và triển vọng lạm phát.

> 5 Các nhóm tài sản chính (*major asset classes*) được phân biệt với các nhóm tài sản phụ (*sub-classes*), chẳng hạn như cổ phiếu giá trị Hoa Kỳ và cổ phiếu tăng trưởng Hoa Kỳ.


<!-- PDF Page 45 -->

cổ phiếu thị trường mới nổi (*emerging market stocks*), trái phiếu thị trường mới nổi (*emerging market bonds*), cổ phiếu thị trường phát triển (tức là các thị trường phát triển ngoại trừ thị trường trong nước), trái phiếu thị trường phát triển, bất động sản (*real estate*), cùng vàng và các hàng hóa khác (*commodities*). Ngoài ra, các ngành công nghiệp và lĩnh vực (*industries and sectors*) cũng được sử dụng để đa dạng hóa danh mục đầu tư. Ví dụ, cổ phiếu ngành năng lượng có thể không tương quan chặt chẽ với cổ phiếu ngành chăm sóc sức khỏe. Tỷ lệ chính xác mà các tài sản này nên được đưa vào danh mục đầu tư phụ thuộc vào các đặc điểm rủi ro, lợi nhuận, và hệ số tương quan của từng loại cũng như quốc gia bản địa của nhà đầu tư.

- _Đa dạng hóa bằng các quỹ chỉ số (Diversify with index funds)._ Việc đa dạng hóa giữa các nhóm tài sản có thể trở nên tốn kém đối với những danh mục đầu tư nhỏ do số lượng chứng khoán cần thiết. Ví dụ, việc tạo lập mức tiếp xúc đa dạng hóa đối với một danh mục đơn lẻ, chẳng hạn như nhóm tài sản công ty lớn trong nước, có thể đòi hỏi một nhóm gồm ít nhất 30 cổ phiếu. Việc tiếp xúc với 10 nhóm tài sản có thể đòi hỏi tới 300 chứng khoán, gây tốn kém chi phí để giao dịch và theo dõi. Thay vào đó, có thể sẽ rất hiệu quả nếu sử dụng các quỹ hoán đổi danh mục (*exchange-traded funds* – ETFs) hoặc các quỹ tương hỗ (*mutual funds*) bám sát các chỉ số tương ứng, giúp làm giảm chi phí gắn liền với việc xây dựng một danh mục đầu tư đa dạng hóa tốt. Do đó, nhiều nhà đầu tư nên cân nhắc các quỹ tương hỗ chỉ số (*index mutual funds*) như một công cụ đầu tư thay vì các chứng khoán riêng lẻ.

- _Đa dạng hóa giữa các quốc gia (Diversification among countries)._ Các quốc gia khác nhau do trọng tâm ngành công nghiệp, chính sách kinh tế, và môi trường chính trị khác nhau. Nền kinh tế Hoa Kỳ sản xuất nhiều dịch vụ tài chính và kỹ thuật cũng như đầu tư một lượng lớn vào nghiên cứu đổi mới sáng tạo. Tuy nhiên, nền kinh tế Trung Quốc và Ấn Độ lại tập trung vào sản xuất chế tạo (*manufacturing*). Các quốc gia trong Liên minh Châu Âu là những nền dân chủ sôi động trong khi các quốc gia Đông Á đang thử nghiệm mô hình dân chủ. Do đó, tỷ suất sinh lợi tài chính ở một quốc gia theo thời gian ít có khả năng tương quan cao với tỷ suất sinh lợi ở một quốc gia khác. Tỷ suất sinh lợi của các quốc gia cũng có thể khác nhau do các đồng tiền khác nhau. Nói cách khác, tỷ suất sinh lợi của một khoản đầu tư nước ngoài có thể khác đi khi được quy đổi sang đồng tiền của quốc gia bản địa. Bởi vì tỷ suất sinh lợi tiền tệ không tương quan với tỷ suất sinh lợi cổ phiếu, chúng có thể giúp làm giảm rủi ro khi đầu tư vào một quốc gia nước ngoài ngay cả khi quốc gia đó, nếu xét riêng lẻ, là một thị trường mới nổi rất rủi ro dưới góc độ đầu tư cổ phiếu. Đầu tư vào các quốc gia nước ngoài là một phần thiết yếu của một danh mục đầu tư được đa dạng hóa tốt.

- _Đa dạng hóa bằng cách_ không _sở hữu cổ phiếu của công ty nơi bạn làm việc (Diversify by not owning your employer’s stock)._ Các công ty thường khuyến khích nhân viên của họ đầu tư vào cổ phiếu của công ty thông qua các chương trình cổ phiếu dành cho nhân viên (*employee stock plans*) và các chương trình hưu trí (*retirement plans*). Tuy nhiên, bạn nên đánh giá việc đầu tư vào công ty của mình giống như cách bạn đánh giá bất kỳ khoản đầu tư nào khác. Ngoài ra, bạn nên xem xét các khoản đầu tư phi tài chính mà bạn đã thực hiện, đặc biệt là vốn nhân lực (*human capital*) mà bạn đã đầu tư vào công ty của mình. Bởi vì bạn làm việc cho chủ sử dụng lao động của mình, bạn đã đầu tư rất nhiều vào đó rồi—thu nhập của bạn phụ thuộc vào công ty đó. Mức thu nhập của bạn, liệu chế độ đãi ngộ của bạn có được cải thiện hay liệu bạn có được thăng chức hay không, đều phụ thuộc vào việc công ty của bạn hoạt động tốt như thế nào. Nếu một đối thủ cạnh tranh đẩy công ty của bạn ra khỏi thị trường, bạn sẽ mất việc. Các khoản đầu tư tài chính bổ sung vào công ty nơi bạn làm việc sẽ càng làm tập trung khối tài sản của bạn vào một tài sản duy nhất nhiều hơn nữa và khiến bạn kém đa dạng hóa hơn.

- _Đánh giá từng tài sản trước khi thêm vào danh mục đầu tư (Evaluate each asset before adding to a portfolio)._ Mỗi khi bạn thêm một chứng khoán hoặc một nhóm tài sản vào danh mục đầu tư, hãy nhận thức rằng luôn có một chi phí gắn liền với việc đa dạng hóa. Đó là chi phí giao dịch một tài sản cũng như chi phí theo dõi một danh mục đầu tư lớn hơn. Trong một số trường hợp, các chứng khoán hoặc tài sản có thể có tên gọi khác nhau nhưng lại thuộc cùng một nhóm tài sản mà bạn đã có


<!-- PDF Page 46 -->

mức độ tiếp xúc đầy đủ. Một quy tắc tổng quát để đánh giá xem liệu một tài sản mới có nên được đưa vào một danh mục đầu tư hiện hữu hay không được dựa trên mối quan hệ đánh đổi rủi ro – lợi nhuận sau đây:

![](assets/Portfolio_Management.pdf-0046-05.png)

<!-- Formula Text: E(R new)  =  R f + σ new ρ new,p _ σ p × [E(R p) − R f] -->

$$E(R_{\text{new}}) = R_f + \frac{\sigma_{\text{new}} \rho_{\text{new},p}}{\sigma_p} \times [E(R_p) - R_f]$$

trong đó $E(R)$ là tỷ suất sinh lợi từ tài sản, $R_f$ là tỷ suất sinh lợi của tài sản phi rủi ro, $\sigma$ là độ lệch chuẩn, $\rho$ là hệ số tương quan, và các chỉ số dưới $\text{new}$ và $p$ lần lượt đề cập đến cổ phiếu mới và danh mục đầu tư hiện hữu. Nếu tỷ suất sinh lợi đã điều chỉnh rủi ro (*risk-adjusted return*) của tài sản mới mang lại lợi ích cho danh mục đầu tư, thì tài sản đó nên được đưa vào. Điều kiện này có thể được viết lại bằng cách sử dụng tỷ số Sharpe (*Sharpe ratio*) ở cả hai vế của phương trình như sau:

![](assets/Portfolio_Management.pdf-0046-07.png)

<!-- Formula Text: E(R new) − R f _ σ new > E(R p) − R f _ σ p × ρ new,p -->

$$\frac{E(R_{\text{new}}) - R_f}{\sigma_{\text{new}}} > \frac{E(R_p) - R_f}{\sigma_p} \times \rho_{\text{new},p}$$

Nếu tỷ số Sharpe của tài sản mới lớn hơn tỷ số Sharpe của danh mục đầu tư hiện tại nhân với hệ số tương quan, thì việc thêm tài sản mới vào sẽ mang lại lợi ích.

- _Mua bảo hiểm cho các danh mục đầu tư rủi ro (Buy insurance for risky portfolios)._ Điều này có thể gây ngạc nhiên, nhưng bảo hiểm (*insurance*) chính là một tài sản đầu tư—chỉ là một loại tài sản khác biệt. Bảo hiểm có mối tương quan âm với các tài sản của bạn và do đó rất có giá trị. Bảo hiểm mang lại cho bạn tỷ suất sinh lợi dương khi tài sản của bạn mất giá trị, nhưng không chi trả gì cả nếu tài sản của bạn giữ nguyên giá trị. Theo thời gian, bảo hiểm tạo ra một tỷ suất sinh lợi trung bình âm. Tuy nhiên, nhiều cá nhân sẵn sàng chấp nhận một mức lợi nhuận âm nhỏ bởi vì bảo hiểm làm giảm mức độ tiếp xúc của họ trước một khoản lỗ cực đoan. Nhìn chung, hoàn toàn hợp lý khi bổ sung một khoản đầu tư có tỷ suất sinh lợi âm nếu khoản đầu tư đó làm giảm đáng kể rủi ro (một ví dụ điển hình về sự đánh đổi giữa rủi ro và lợi nhuận).

Ngoài ra, các khoản đầu tư có tương quan âm cũng tồn tại trên thị trường. Trong lịch sử, vàng (*gold*) có tương quan âm với cổ phiếu; tuy nhiên, tỷ suất sinh lợi kỳ vọng của vàng thường nhỏ và đôi khi thậm chí là âm. Các nhà đầu tư thường đưa vàng và các hàng hóa khác vào danh mục đầu tư của họ như một cách để giảm thiểu rủi ro tổng thể của danh mục đầu tư, bao gồm cả rủi ro tiền tệ và rủi ro lạm phát.

Mua quyền chọn bán (*buying put options*) là một cách khác để giảm thiểu rủi ro. Bởi vì quyền chọn bán chi trả tiền khi tài sản cơ sở giảm giá trị (tương quan âm), chúng có thể bảo vệ danh mục đầu tư của nhà đầu tư trước những khoản lỗ thảm khốc. Tất nhiên, quyền chọn bán tốn chi phí để mua, và tỷ suất sinh lợi kỳ vọng là bằng không hoặc âm một chút ở mức cận biên.

# **<mark>10</mark>**

## **ĐƯỜNG BIÊN HIỆU QUẢ: TẬP HỢP CƠ HỘI ĐẦU TƯ & CÁC DANH MỤC ĐẦU TƯ CÓ PHƯƠNG SAI TỐI THIỂU (*EFFICIENT FRONTIER: INVESTMENT OPPORTUNITY SET & MINIMUM VARIANCE PORTFOLIOS*)**

mô tả tác động lên rủi ro của danh mục đầu tư khi đầu tư vào các tài sản có tương quan nhỏ hơn mức tương quan hoàn hảo (*less than perfectly correlated*)
mô tả và diễn giải đường biên phương sai tối thiểu (*minimum-variance frontier*) và đường biên hiệu quả (*efficient frontier*) của các tài sản rủi ro cùng với danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*)


<!-- PDF Page 47 -->

Trong phần này, chúng ta chuẩn hóa tác động của sự đa dạng hóa và mở rộng tập hợp các khoản đầu tư để bao gồm tất cả các tài sản rủi ro hiện có trong khung phân tích trung bình – phương sai (*mean–variance framework*). Việc bổ sung một tài sản phi rủi ro sẽ tạo ra một danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*) và đường phân bổ vốn (*capital allocation line* – CAL). Sau đó, chúng ta có thể suy ra danh mục đầu tư tối ưu của nhà đầu tư (*investor’s optimal portfolio*) bằng cách chồng đường phân bổ vốn lên các đường bàng quan của nhà đầu tư.

### **Tập hợp Cơ hội Đầu tư (*Investment Opportunity Set*)**

Nếu hai tài sản có tương quan hoàn hảo, tập hợp cơ hội rủi ro – lợi nhuận (*risk–return opportunity set*) được biểu diễn bằng một đường thẳng nối hai tài sản đó. Đường thẳng này chứa các danh mục đầu tư được hình thành bằng cách thay đổi tỷ trọng của mỗi tài sản được đầu tư trong danh mục. Sự tương quan này đã được mô tả bằng đường thẳng (với $\rho = 1$) trong Bảng minh họa 14. Nếu hai tài sản không tương quan hoàn hảo, rủi ro của danh mục đầu tư sẽ nhỏ hơn rủi ro bình quân gia quyền của các thành phần, và danh mục đầu tư được hình thành từ hai tài sản sẽ phình ra về phía bên trái (*bulges on the left*) như được thể hiện bởi các đường cong có hệ số tương quan ($\rho$) nhỏ hơn 1,0 trong Bảng minh họa 14. Tất cả các điểm nối hai tài sản đều có thể đạt được (hay khả thi – *feasible*). Việc bổ sung thêm các tài sản mới vào danh mục đầu tư này sẽ tạo ra ngày càng nhiều danh mục đầu tư hơn nữa, vốn là sự kết hợp tuyến tính giữa danh mục đầu tư hiện hữu và tài sản mới hoặc là sự kết hợp dạng đường cong (*curvilinear combination*), tùy thuộc vào hệ số tương quan giữa danh mục đầu tư hiện hữu và tài sản mới.

Khi số lượng các tài sản hiện có tăng lên, số lượng các sự kết hợp khả thi tăng lên nhanh chóng. Khi tất cả các tài sản có thể đầu tư (*investable assets*) được xem xét, và có hàng trăm hàng nghìn tài sản như vậy, chúng ta có thể xây dựng một tập hợp cơ hội của các khoản đầu tư (*opportunity set of investments*). Tập hợp cơ hội thông thường sẽ bao phủ tất cả các điểm nằm bên trong một đường biên (*frontier*) bởi vì hoàn toàn có thể chạm tới mọi điểm khả thi bên trong đường cong đó bằng cách tạo lập một cách khéo léo một danh mục đầu tư từ các tài sản có thể đầu tư.

Chúng ta bắt đầu với các tài sản riêng lẻ có thể đầu tư và dần dần hình thành các danh mục đầu tư có thể được vẽ trên đồ thị để tạo thành một đường cong như trong Bảng minh họa 18. Tất cả các điểm nằm trên đường cong và các điểm nằm về phía bên phải của đường cong đều có thể đạt được bằng sự kết hợp của một hoặc nhiều tài sản có thể đầu tư. Tập hợp các điểm này được gọi là **tập hợp cơ hội đầu tư (*investment opportunity set*)**. Ban đầu, tập hợp cơ hội chỉ bao gồm các tài sản trong nước (*domestic assets only*) và được gắn nhãn như vậy trong Bảng minh họa 18.

#### **Bảng minh họa 18: Tập hợp Cơ hội Đầu tư (*Investment Opportunity Set*)**

![](assets/Portfolio_Management.pdf-0047-09.png)

<!-- Picture Text: E ( Rp )<br>With international assets<br>Domestic assets only<br>Individual Assets<br>0 Portfolio Standard Deviation<br>Portfolio Expected Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn danh mục đầu tư (*Portfolio Standard Deviation*), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư (*Portfolio Expected Return* $E(R_p)$). Các chấm tròn biểu diễn Các tài sản riêng lẻ (*Individual Assets*). Đường cong liền nét bên trong là Tập hợp cơ hội chỉ gồm các tài sản trong nước (*Domestic assets only*); đường cong nét đứt mở rộng ra phía tây bắc là Tập hợp cơ hội khi có thêm các tài sản quốc tế (*With international assets*).


<!-- PDF Page 48 -->

#### **_Bổ sung các Nhóm Tài sản (Addition of Asset Classes)_**

Bảng minh họa 18 cho thấy tác động của việc bổ sung thêm một nhóm tài sản mới, chẳng hạn như các tài sản quốc tế (*international assets*). Miễn là nhóm tài sản mới không tương quan hoàn hảo với nhóm tài sản hiện hữu, tập hợp cơ hội đầu tư sẽ mở rộng hơn nữa về phía tây bắc (*northwest*), mang lại một sự đánh đổi rủi ro – lợi nhuận vượt trội hơn.

Tập hợp cơ hội đầu tư có các tài sản quốc tế chiếm ưu thế vượt trội (*dominates*) so với tập hợp cơ hội chỉ bao gồm các tài sản trong nước. Việc bổ sung thêm các nhóm tài sản khác cũng sẽ có tác động tương tự lên tập hợp cơ hội. Do đó, chúng ta nên tiếp tục bổ sung các nhóm tài sản cho đến khi chúng không còn cải thiện thêm sự đánh đổi rủi ro – lợi nhuận nữa. Những lợi ích của sự đa dạng hóa có thể được nắm bắt trọn vẹn theo cách này trong việc xây dựng tập hợp cơ hội đầu tư, và cuối cùng là trong việc lựa chọn danh mục đầu tư tối ưu.

Trong phần thảo luận tiếp theo của mục này, chúng ta sẽ giả định rằng _tất cả_ các tài sản có thể đầu tư hiện có đối với một nhà đầu tư đều đã được đưa vào trong tập hợp cơ hội đầu tư và không cần phải dành sự chú ý đặc biệt nào cho các nhóm tài sản mới hay các cơ hội đầu tư mới nữa.

### **Các Danh mục Đầu tư có Phương sai Tối thiểu (*Minimum-Variance Portfolios*)**

Tập hợp cơ hội đầu tư bao gồm tất cả các tập hợp có thể đầu tư hiện có được thể hiện trong Bảng minh họa 19. Có một số lượng lớn các danh mục đầu tư sẵn có để đầu tư, nhưng chúng ta phải chọn ra một danh mục đầu tư tối ưu duy nhất. Trong tiểu mục này, chúng ta bắt đầu quy trình lựa chọn bằng cách thu hẹp sự lựa chọn xuống còn ít danh mục đầu tư hơn.

#### **Bảng minh họa 19: Đường biên Phương sai Tối thiểu (*Minimum-Variance Frontier*)**

![](assets/Portfolio_Management.pdf-0048-11.png)

<!-- Picture Text: E ( Rp ) Efficient Frontier<br>A B<br>X<br>D<br>C Minimum-Variance<br>Frontier<br>Global<br>Minimum-<br>Variance<br>Portfolio (Z)<br>0 Portfolio Standard Deviation<br>Portfolio Expected Return<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn danh mục đầu tư (*Portfolio Standard Deviation*), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư (*Portfolio Expected Return* $E(R_p)$). Toàn bộ đường cong bao ngoài bên trái là Đường biên phương sai tối thiểu (*Minimum-Variance Frontier*). Điểm ngoài cùng bên trái $Z$ là Danh mục đầu tư có phương sai tối thiểu toàn cục (*Global Minimum-Variance Portfolio*). Phần nhánh trên từ $Z$ qua $A$ đến $D$ là Đường biên hiệu quả (*Efficient Frontier*). Điểm $X$ nằm ngoài vùng khả thi (bên trái $A$), điểm $B$ nằm bên trong vùng khả thi (bên phải $A$), và điểm $C$ nằm ở nhánh dưới của đường biên phương sai tối thiểu.

#### **_Đường biên Phương sai Tối thiểu (Minimum-Variance Frontier)_**

Các nhà đầu tư ngại rủi ro tìm cách tối thiểu hóa rủi ro cho một mức lợi nhuận nhất định. Hãy xét các Điểm A, B, và X trong Bảng minh họa 19 và giả sử rằng chúng nằm trên cùng một đường thẳng nằm ngang theo cách dựng hình. Do đó, cả ba điểm đều có cùng tỷ suất sinh lợi kỳ vọng, $E(R_1)$, giống như tất cả các điểm khác nằm trên đường thẳng tưởng tượng nối A, B, và X. Khi được quyền lựa chọn, một nhà đầu tư sẽ chọn điểm có rủi ro tối thiểu, tức là Điểm X. Tuy nhiên, Điểm X không thể đạt được (*unattainable*) bởi vì nó không nằm trong tập hợp cơ hội đầu tư. Do đó, mức rủi ro tối thiểu


<!-- PDF Page 49 -->

mà chúng ta có thể đạt được cho mức lợi nhuận $E(R_1)$ là tại Điểm A. Điểm B và tất cả các điểm nằm về phía bên phải của Điểm A đều khả thi nhưng chúng lại có rủi ro cao hơn. Vì vậy, một nhà đầu tư ngại rủi ro sẽ chỉ chọn Điểm A thay vì bất kỳ danh mục đầu tư nào khác có cùng mức lợi nhuận.

Tương tự, Điểm C là điểm có phương sai tối thiểu đối với mức lợi nhuận kiếm được tại C. Các điểm nằm về phía bên phải của C đều có rủi ro cao hơn. Chúng ta có thể mở rộng phân tích trên cho tất cả các mức lợi nhuận khả thi. Trong mọi trường hợp, chúng ta đều thấy rằng **danh mục đầu tư có phương sai tối thiểu (*minimum-variance portfolio*)** là danh mục nằm trên đường cong liền nét được vẽ trong Bảng minh họa 19. Toàn bộ tập hợp các danh mục đầu tư có phương sai tối thiểu này được gọi là **đường biên phương sai tối thiểu (*minimum-variance frontier*)**. Đường biên phương sai tối thiểu xác định một tập hợp nhỏ hơn các danh mục đầu tư mà các nhà đầu tư muốn đầu tư vào. Lưu ý rằng không có nhà đầu tư ngại rủi ro nào lại chọn đầu tư vào một danh mục nằm về phía bên phải của đường biên phương sai tối thiểu bởi vì một danh mục đầu tư nằm ngay trên đường biên phương sai tối thiểu có thể mang lại cùng mức lợi nhuận nhưng ở một mức rủi ro thấp hơn.

#### **_Danh mục Đầu tư có Phương sai Tối thiểu Toàn cục (Global Minimum-Variance Portfolio)_**

Điểm ngoài cùng bên trái trên đường biên phương sai tối thiểu là danh mục đầu tư có phương sai nhỏ nhất trong số tất cả các danh mục đầu tư gồm các tài sản rủi ro, và được gọi là **danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*)**. Một nhà đầu tư không thể nắm giữ một danh mục đầu tư bao gồm các tài sản _rủi ro_ mà lại có mức rủi ro thấp hơn mức rủi ro của danh mục đầu tư có phương sai tối thiểu toàn cục. Hãy lưu ý sự nhấn mạnh vào cụm từ tài sản “rủi ro”. Sau này, việc đưa thêm một tài sản phi rủi ro vào sẽ cho phép chúng ta nới lỏng ràng buộc này.

#### **_Đường biên Hiệu quả của các Tài sản Rủi ro (Efficient Frontier of Risky Assets)_**

Đường biên phương sai tối thiểu mang lại cho chúng ta các danh mục đầu tư có phương sai nhỏ nhất cho một mức lợi nhuận nhất định. Tuy nhiên, các nhà đầu tư cũng muốn tối đa hóa lợi nhuận cho một mức rủi ro nhất định. Hãy quan sát Điểm A và Điểm C trên đường biên phương sai tối thiểu được thể hiện trong Bảng minh họa 19. Cả hai điểm này đều có cùng mức rủi ro. Khi được quyền lựa chọn, một nhà đầu tư sẽ chọn Danh mục A bởi vì nó có lợi nhuận cao hơn. Sẽ không ai chọn Danh mục C. Phân tích tương tự cũng áp dụng cho tất cả các điểm nằm trên đường biên phương sai tối thiểu ở phía dưới danh mục đầu tư có phương sai tối thiểu toàn cục. Do đó, các danh mục đầu tư nằm trên đường cong phía dưới danh mục có phương sai tối thiểu toàn cục và nằm về phía bên phải của nó đều không mang lại lợi ích và là những danh mục đầu tư không hiệu quả (*inefficient portfolios*) đối với một nhà đầu tư.

Đường cong nằm phía trên và về phía bên phải của danh mục đầu tư có phương sai tối thiểu toàn cục được gọi là **đường biên hiệu quả Markowitz (*Markowitz efficient frontier*)** bởi vì nó chứa tất cả các danh mục đầu tư gồm các tài sản rủi ro mà những nhà đầu tư hợp lý, ngại rủi ro (*rational, risk-averse investors*) sẽ lựa chọn.

Một quan sát quan trọng thường bị bỏ qua là độ dốc (*slope*) tại các điểm khác nhau trên đường biên hiệu quả. Khi chúng ta di chuyển sang phải từ danh mục đầu tư có phương sai tối thiểu toàn cục (Điểm Z) trong Bảng minh họa 19, có sự gia tăng về rủi ro đi kèm với sự gia tăng đồng thời về lợi nhuận. Tuy nhiên, mức tăng lợi nhuận ứng với mỗi đơn vị rủi ro tăng thêm lại liên tục giảm dần khi chúng ta di chuyển từ trái sang phải bởi vì độ dốc liên tục giảm. Độ dốc tại Điểm D nhỏ hơn độ dốc tại Điểm A, và độ dốc tại Điểm A lại nhỏ hơn độ dốc tại Điểm Z. Mức tăng lợi nhuận khi di chuyển từ Điểm Z đến Điểm A bằng với mức tăng lợi nhuận khi di chuyển từ Điểm A đến Điểm D. Có thể thấy rằng lượng rủi ro tăng thêm khi di chuyển từ Điểm A đến Điểm D gấp từ 3 đến 4 lần so với lượng rủi ro tăng thêm khi di chuyển từ Điểm Z đến Điểm A. Như vậy, các nhà đầu tư nhận được mức gia tăng lợi nhuận ngày càng giảm dần (*decreasing increases in returns*) khi họ gánh chịu thêm nhiều rủi ro.


<!-- PDF Page 50 -->

# **<mark>11</mark>**

## **ĐƯỜNG BIÊN HIỆU QUẢ: MỘT TÀI SẢN PHI RỦI RO VÀ NHIỀU TÀI SẢN RỦI RO (*EFFICIENT FRONTIER: A RISK-FREE ASSET AND MANY RISKY ASSETS*)**

giải thích việc lựa chọn danh mục đầu tư tối ưu (*optimal portfolio*), khi biết độ hữu dụng (*utility*) (hoặc mức độ ngại rủi ro) của nhà đầu tư và đường phân bổ vốn (*capital allocation line*)

Cho đến nay, chúng ta mới chỉ xem xét các tài sản rủi ro trong đó tỷ suất sinh lợi là có rủi ro hoặc không chắc chắn. Tuy nhiên, hầu hết các nhà đầu tư đều có quyền tiếp cận với một tài sản phi rủi ro (*risk-free asset*), đáng chú ý nhất là từ các chứng khoán do chính phủ phát hành. Việc bổ sung thêm một tài sản phi rủi ro làm cho tập hợp cơ hội đầu tư trở nên phong phú hơn nhiều so với tập hợp cơ hội đầu tư chỉ bao gồm các tài sản rủi ro.

### **Đường phân bổ vốn và Danh mục Đầu tư Rủi ro Tối ưu (*Capital Allocation Line and Optimal Risky Portfolio*)**

Theo định nghĩa, một tài sản phi rủi ro có rủi ro bằng không nên nó phải nằm trên trục tung (*y-axis*) trong đồ thị trung bình – phương sai. Một tài sản phi rủi ro có tỷ suất sinh lợi $R_f$ được vẽ trong Bảng minh họa 20. Tài sản này bây giờ có thể được kết hợp với một danh mục các tài sản rủi ro. Sự kết hợp giữa một tài sản phi rủi ro với một danh mục các tài sản rủi ro là một đường thẳng, giống như trong Phần 6 (xem Bảng minh họa 9). Tuy nhiên, không giống như trong Phần 6, chúng ta có nhiều danh mục đầu tư rủi ro để lựa chọn thay vì chỉ một danh mục đầu tư rủi ro duy nhất.

**Bảng minh họa 20: Danh mục Đầu tư Rủi ro Tối ưu (*Optimal Risky Portfolio*)**

![](assets/Portfolio_Management.pdf-0050-11.png)

<!-- Picture Text: CAL(P)<br>Y Efficient Frontier<br>X CAL(A) of Risky Assets<br>P<br>Optimal Risky<br>A Portfolio<br>Rf<br>Portfolio Standard Deviation<br>p<br>() ER p<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng ($E(R_p)$). Đường $\text{CAL}(A)$ nối từ $R_f$ cắt Đường biên hiệu quả của các tài sản rủi ro (*Efficient Frontier of Risky Assets*) tại điểm $A$. Đường $\text{CAL}(P)$ nối từ $R_f$ tiếp xúc với Đường biên hiệu quả tại điểm $P$ – Danh mục đầu tư rủi ro tối ưu (*Optimal Risky Portfolio*). Điểm $Y$ trên $\text{CAL}(P)$ nằm ngay phía trên điểm $X$ của Đường biên hiệu quả ở cùng mức độ lệch chuẩn.

Tất cả các danh mục đầu tư nằm trên đường biên hiệu quả đều là những ứng cử viên để được kết hợp với tài sản phi rủi ro. Hai sự kết hợp được thể hiện trong Bảng minh họa 20: một sự kết hợp giữa tài sản phi rủi ro và Danh mục hiệu quả A, và sự kết hợp kia là giữa tài sản phi rủi ro và Danh mục hiệu quả P. Khi so sánh đường phân bổ vốn A ($\text{CAL}(A)$) và đường phân bổ vốn P ($\text{CAL}(P)$), ta thấy rằng luôn có một điểm trên $\text{CAL}(P)$ có lợi nhuận cao hơn và cùng mức rủi ro đối với mỗi điểm trên $\text{CAL}(A)$. Nói cách khác, các danh mục đầu tư trên $\text{CAL}(P)$ chiếm ưu thế vượt trội (*dominate*) so với các danh mục đầu tư trên $\text{CAL}(A)$. Do đó, một nhà đầu tư sẽ chọn $\text{CAL}(P)$ thay vì $\text{CAL}(A)$. Chúng ta muốn dịch chuyển xa hơn nữa về phía tây bắc để đạt được những danh mục đầu tư tốt hơn nữa. Tuy nhiên, không có danh mục đầu tư nào trong số đó có thể đạt được bởi vì chúng nằm phía trên đường biên hiệu quả.


<!-- PDF Page 51 -->

Thế còn các điểm khác trên đường biên hiệu quả thì sao? Ví dụ, Điểm X nằm trên đường biên hiệu quả và có tỷ suất sinh lợi cao nhất trong số tất cả các danh mục đầu tư rủi ro ở mức rủi ro của nó. Tuy nhiên, Điểm Y trên $\text{CAL}(P)$, có thể đạt được bằng cách sử dụng đòn bẩy (*leveraging*) đối với Danh mục P như đã thấy trong Phần 6, nằm phía trên Điểm X và có cùng mức rủi ro nhưng lợi nhuận cao hơn. Theo cùng cách đó, chúng ta có thể quan sát thấy rằng $\text{CAL}(P)$ không chỉ chiếm ưu thế vượt trội so với $\text{CAL}(A)$ mà còn chiếm ưu thế vượt trội so với cả đường biên hiệu quả Markowitz của các tài sản rủi ro.

$\text{CAL}(P)$ là đường phân bổ vốn tối ưu (*optimal capital allocation line*) và Danh mục P là **danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*)**. Như vậy, với việc bổ sung thêm tài sản phi rủi ro, chúng ta có thể thu hẹp việc lựa chọn các danh mục đầu tư rủi ro xuống còn một danh mục đầu tư rủi ro tối ưu duy nhất, P, nằm tại tiếp điểm của $\text{CAL}(P)$ và đường biên hiệu quả của các tài sản rủi ro.

### **Định lý Phân tách Hai Quỹ (*The Two-Fund Separation Theorem*)**

**Định lý phân tách hai quỹ (*two-fund separation theorem*)** phát biểu rằng tất cả các nhà đầu tư bất kể thị hiếu, sở thích rủi ro, và mức tài sản ban đầu sẽ đều nắm giữ một sự kết hợp của hai danh mục đầu tư hay hai quỹ: một tài sản phi rủi ro và một danh mục đầu tư tối ưu gồm các tài sản rủi ro.<sup>6</sup>

Định lý phân tách cho phép chúng ta chia bài toán đầu tư của một nhà đầu tư thành hai bước riêng biệt: quyết định đầu tư (*investment decision*) và quyết định tài trợ (*financing decision*). Trong bước đầu tiên, giống như trong phân tích trước đó, nhà đầu tư xác định danh mục đầu tư rủi ro tối ưu. Danh mục đầu tư rủi ro tối ưu được lựa chọn từ vô số các danh mục đầu tư rủi ro mà không cần xem xét đến sở thích của nhà đầu tư. Quyết định đầu tư ở bước này được dựa trên tỷ suất sinh lợi, rủi ro, và các hệ số tương quan của danh mục đầu tư rủi ro tối ưu (một danh mục duy nhất).

Đường phân bổ vốn kết nối danh mục đầu tư rủi ro tối ưu và tài sản phi rủi ro. Tất cả các danh mục đầu tư tối ưu của nhà đầu tư đều phải nằm trên đường thẳng này. Danh mục đầu tư tối ưu của từng nhà đầu tư trên $\text{CAL}(P)$ được xác định ở bước thứ hai. Việc xem xét sở thích rủi ro của từng nhà đầu tư cá nhân, bằng cách sử dụng các đường bàng quan, sẽ quyết định mức phân bổ của nhà đầu tư vào tài sản phi rủi ro (cho vay – *lending*) và vào danh mục đầu tư rủi ro tối ưu. Các danh mục đầu tư nằm vượt quá danh mục đầu tư rủi ro tối ưu đạt được bằng cách đi vay (*borrowing*) với lãi suất phi rủi ro (tức là mua ký quỹ – *buying on margin*). Do đó, sở thích rủi ro của từng nhà đầu tư cá nhân sẽ quyết định quy mô tài trợ (tức là cho chính phủ vay thay vì đầu tư vào danh mục rủi ro tối ưu hoặc đi vay để mua thêm danh mục rủi ro tối ưu).

#### **VÍ DỤ 7**

### **Lựa chọn Đúng Danh mục Đầu tư (*Choosing the Right Portfolio*)**

Trong Bảng minh họa 21, rủi ro và lợi nhuận của các điểm được đánh dấu có giá trị như sau:

|**Điểm (*Point*)**|**Lợi nhuận (*Return*) (%)**|**Rủi ro (*Risk*) (%)**|**Điểm (*Point*)**|**Lợi nhuận (*Return*) (%)**|**Rủi ro (*Risk*) (%)**|
|---|---|---|---|---|---|
|A|15|10|B|11|10|
|C|15|30|D|25|30|
|F|4|0|G (vàng – *gold*)|10|30|
|P|16|17||||


<!-- PDF Page 52 -->

![](assets/Portfolio_Management.pdf-0052-04.png)

<!-- Picture Text: Exhibit 21<br>25.00 D Optimal CAL<br>20.00<br>P Stocks<br>C<br>A<br>15.00<br>G<br>10.00 B<br>Gold<br>5.00<br>F<br>0.00<br>0 10 20 30 40<br>Standard Deviation (%)<br>Expected Return (%)<br> -->

> **Chú thích hình ảnh:** Bảng minh họa 21: Trục hoành là Độ lệch chuẩn (%), trục tung là Lợi nhuận kỳ vọng (%). Đường CAL tối ưu (*Optimal CAL*) đi từ điểm $F(0, 4)$, qua $B(10, 11)$, tiếp xúc với đường biên hiệu quả tại $P(17, 16)$ (Cổ phiếu – *Stocks*), và kéo dài tới $D(30, 25)$. Điểm $A(10, 15)$ nằm phía trên đường CAL; điểm $C(30, 15)$ và $G(30, 10)$ (Vàng – *Gold*) nằm trên đường biên của tập hợp khả thi nhưng ở phía dưới đường CAL.

Hãy trả lời các câu hỏi sau đây với sự tham chiếu đến các điểm được vẽ trên Bảng minh họa 21 và giải thích câu trả lời của bạn. Nhà đầu tư đang lựa chọn một danh mục đầu tư dựa trên đồ thị này.

1. Điểm nào trong số các điểm trên không thể đạt được?

#### **Lời giải:**

Danh mục A không thể đạt được (*not attainable*) bởi vì nó nằm bên ngoài tập hợp khả thi và không nằm trên đường phân bổ vốn.

2. Danh mục đầu tư nào trong số các danh mục này sẽ không được lựa chọn bởi một nhà đầu tư hợp lý, ngại rủi ro?

#### **Lời giải:**

Danh mục G và C sẽ không được lựa chọn bởi vì D mang lại mức lợi nhuận cao hơn với cùng mức rủi ro. G và C là những điểm có thể đầu tư duy nhất không nằm trên đường phân bổ vốn.

3. Danh mục đầu tư nào trong số các danh mục này là phù hợp nhất cho một nhà đầu tư trung lập với rủi ro?

#### **Lời giải:**

Danh mục D là phù hợp nhất bởi vì một nhà đầu tư trung lập với rủi ro chỉ quan tâm đến lợi nhuận và danh mục D mang lại mức lợi nhuận cao nhất. $A = 0$ trong công thức tính độ hữu dụng.

4. Vàng nằm ở phần không hiệu quả của tập hợp khả thi. Tuy nhiên, vàng vẫn được sở hữu bởi nhiều nhà đầu tư hợp lý như một phần của một danh mục đầu tư lớn hơn. Tại sao?

#### **Lời giải:**

Vàng có thể được sở hữu như một phần của danh mục đầu tư (chứ không phải là _toàn bộ_ danh mục đầu tư) bởi vì vàng có hệ số tương quan thấp hoặc âm với nhiều tài sản rủi ro, chẳng hạn như cổ phiếu. Do đó, việc trở thành một phần của danh mục đầu tư có thể làm giảm rủi ro tổng thể mặc dù rủi ro đơn lẻ (*standalone risk*) của nó cao và lợi nhuận thấp. Lưu ý rằng giá vàng không hề ổn định—tỷ suất sinh lợi của nó rất rủi ro (30%). Ngay cả những người tìm kiếm rủi ro cũng sẽ chọn D thay vì G, vì D có cùng mức rủi ro nhưng lợi nhuận cao hơn.


<!-- PDF Page 53 -->

5. Độ hữu dụng của một nhà đầu tư tại điểm P với hệ số ngại rủi ro bằng 3 là bao nhiêu?

**Lời giải:**

- $U = E(r) - 0,5 A \sigma^2 = 0,16 - 0,5 \times 3 \times 0,0289 = 0,1167 = 11,67\%$.

## **ĐƯỜNG BIÊN HIỆU QUẢ: DANH MỤC ĐẦU TƯ TỐI ƯU CỦA NHÀ ĐẦU TƯ (*EFFICIENT FRONTIER: OPTIMAL INVESTOR PORTFOLIO*)**

# **<mark>12</mark>**

giải thích việc lựa chọn danh mục đầu tư tối ưu (*optimal portfolio*), khi biết độ hữu dụng (*utility*) (hoặc mức độ ngại rủi ro) của nhà đầu tư và đường phân bổ vốn (*capital allocation line*)

Đường $\text{CAL}(P)$ trong Bảng minh họa 22 chứa các danh mục đầu tư tốt nhất có thể hiện có dành cho các nhà đầu tư. Mỗi danh mục đầu tư trong số đó là một sự kết hợp tuyến tính giữa tài sản phi rủi ro và danh mục đầu tư rủi ro tối ưu. Trong số các danh mục đầu tư hiện có, việc lựa chọn danh mục đầu tư tối ưu của từng nhà đầu tư phụ thuộc vào sở thích rủi ro của nhà đầu tư đó. Trong Phần 4–6, chúng ta đã thảo luận rằng sở thích rủi ro của nhà đầu tư cá nhân được tích hợp vào các đường bàng quan của họ. Những đường này có thể được sử dụng để lựa chọn danh mục đầu tư tối ưu.

Bảng minh họa 22 cho thấy một đường bàng quan tiếp xúc (*tangent*) với đường phân bổ vốn, $\text{CAL}(P)$. Các đường bàng quan có độ hữu dụng cao hơn đường này đều nằm phía trên đường phân bổ vốn, vì vậy các danh mục đầu tư của chúng không thể đạt được. Các đường bàng quan nằm phía dưới đường này không được ưa thích bởi vì chúng có độ hữu dụng thấp hơn. Do đó, danh mục đầu tư tối ưu đối với nhà đầu tư có đường bàng quan này chính là danh mục C nằm trên $\text{CAL}(P)$, tại điểm tiếp xúc với đường bàng quan.

#### **Bảng minh họa 22: Danh mục Đầu tư Tối ưu của Nhà đầu tư (*Optimal Investor Portfolio*)**

![](assets/Portfolio_Management.pdf-0053-11.png)

<!-- Picture Text: CAL(P)<br>E ( Rp ) Indifference curve<br>Efficient frontier<br>of risky assets<br>C P<br>A Optimal risky<br>portfolio<br>Rf Optimal investor<br>portfolio<br>0 Standard Deviation (%) σ p<br>Expected Return (%)<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn ($\sigma_p$ %), trục tung là Lợi nhuận kỳ vọng ($E(R_p)$ %). Đường $\text{CAL}(P)$ bắt đầu từ $R_f$ tiếp xúc với Đường biên hiệu quả của các tài sản rủi ro (*Efficient frontier of risky assets*) tại điểm $P$ – Danh mục đầu tư rủi ro tối ưu (*Optimal risky portfolio*). Đường bàng quan (*Indifference curve*) tiếp xúc với $\text{CAL}(P)$ tại điểm $C$ – Danh mục đầu tư tối ưu của nhà đầu tư (*Optimal investor portfolio*).


<!-- PDF Page 54 -->

#### **VÍ DỤ 8**

### **Ví dụ Toàn diện về Lựa chọn Danh mục Đầu tư (*Comprehensive Example on Portfolio Selection*)**

Ví dụ toàn diện này ôn tập lại nhiều khái niệm đã học trong bài đọc này. Ví dụ bắt đầu với những thông tin đơn giản về các tài sản hiện có và xây dựng một danh mục đầu tư tối ưu của nhà đầu tư cho gia đình Lohrmann.

Giả sử gia đình Lohrmann chỉ có thể đầu tư vào hai tài sản rủi ro, A và B. Tỷ suất sinh lợi kỳ vọng và độ lệch chuẩn đối với tài sản A là 20% và 50%, còn tỷ suất sinh lợi kỳ vọng và độ lệch chuẩn đối với tài sản B là 15% và 33%. Hai tài sản này có hệ số tương quan với nhau bằng không.

1. Tính tỷ suất sinh lợi kỳ vọng của danh mục đầu tư và rủi ro (độ lệch chuẩn) của danh mục đầu tư nếu một nhà đầu tư đầu tư 10% vào A và 90% còn lại vào B.

#### **Lời giải:**

Chỉ số dưới “$rp$” có nghĩa là danh mục đầu tư rủi ro (*risky portfolio*).

$$R_{rp} = [0,10 \times 20\%] + [(1 - 0,10) \times 15\%] = 0,155 = 15,50\%$$

$$\sigma_{rp} = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{AB} \sigma_A \sigma_B}$$

$$= \sqrt{(0,10^2 \times 0,50^2) + (0,90^2 \times 0,33^2) + (2 \times 0,10 \times 0,90 \times 0,0 \times 0,50 \times 0,33)} = 0,3012 = 30,12\%$$

Lưu ý rằng hệ số tương quan bằng 0, vì vậy số hạng cuối cùng trong công thức độ lệch chuẩn bằng không.

2. Tổng quát hóa các phép tính trên cho lợi nhuận và rủi ro của danh mục đầu tư bằng cách giả định khoản đầu tư có tỷ trọng $w_A$ vào Tài sản A và khoản đầu tư có tỷ trọng $(1 - w_A)$ vào Tài sản B.

**Lời giải:**

![](assets/Portfolio_Management.pdf-0054-14.png)

<!-- Formula Text: R rp  =  w A × 20 %  + (1 − w A) × 15 %   =  0.05 w A + 0.15 σ rp  =  √ _________________________ w A 2  × 0.5 2 + (1 − w A) 2 × 0.33 2   =  √ ____________________________ 0.25 w A 2  + 0.1089(1 − 2 w A + w A 2 ) = √ ___________________________ 0.3589 w A 2  − 0.2178 w A + 0.1089 -->

$$R_{rp} = w_A \times 20\% + (1 - w_A) \times 15\% = 0,05 w_A + 0,15$$

$$\sigma_{rp} = \sqrt{w_A^2 \times 0,5^2 + (1 - w_A)^2 \times 0,33^2} = \sqrt{0,25 w_A^2 + 0,1089(1 - 2 w_A + w_A^2)}$$

$$= \sqrt{0,3589 w_A^2 - 0,2178 w_A + 0,1089}$$

Tập hợp cơ hội đầu tư có thể được xây dựng bằng cách sử dụng các tỷ trọng khác nhau trong các biểu thức tính $E(R_{rp})$ và $\sigma_{rp}$ ở Phần 1 của ví dụ này. Bảng minh họa 23 thể hiện sự kết hợp của Tài sản A và B.

#### **Bảng minh họa 23**

![](assets/Portfolio_Management.pdf-0054-17.png)

<!-- Picture Text: 25%<br>A = 20% return, 50% risk<br>20%<br>15%<br>B = 15% return, 33% risk<br>10%<br>5%<br>0%<br>0% 10% 20% 30% 40% 50% 60%<br>Standard Deviation of Portfolio<br>p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn của danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Đường cong nối giữa điểm $B$ (15% lợi nhuận, 33% rủi ro) và điểm $A$ (20% lợi nhuận, 50% rủi ro).


<!-- PDF Page 55 -->

3. Bây giờ hãy đưa thêm một tài sản phi rủi ro có tỷ suất sinh lợi là 3% vào. Hãy viết phương trình cho đường phân bổ vốn theo $w_A$ nối kết tài sản phi rủi ro với danh mục các tài sản rủi ro. (Gợi ý: sử dụng phương trình trong Phần 6 và thay thế các biểu thức của rủi ro và lợi nhuận danh mục đầu tư rủi ro từ Phần 2 ở trên).

#### **Lời giải:**

Phương trình của đường thẳng nối kết tài sản phi rủi ro với danh mục các tài sản rủi ro được cho dưới đây (xem Phần 6), trong đó chỉ số dưới “$rp$” đề cập đến danh mục đầu tư rủi ro thay vì “$i$”, và chỉ số dưới “$p$” đề cập đến danh mục đầu tư mới gồm hai tài sản rủi ro và một tài sản phi rủi ro.

![](assets/Portfolio_Management.pdf-0055-05.png)

<!-- Formula Text: E(R p)  =  R f + E(R i) − R f _ σ i σ p, Rewritten as E(R p)  =  R f + E(R rp) − R f _ σ rp σ p = 0.03 + 0.05 w A + 0.15 − 0.03 ________________________ √ ___________________________ 0.3589 w A 2  − 0.2178 w A + 0.1089   σ p = 0.03 + 0.05 w A + 0.12 ________________________ √ ___________________________ 0.3589 w A 2  − 0.2178 w A + 0.1089   σ p -->

$$E(R_p) = R_f + \frac{E(R_i) - R_f}{\sigma_i} \sigma_p, \quad \text{Được viết lại thành} \quad E(R_p) = R_f + \frac{E(R_{rp}) - R_f}{\sigma_{rp}} \sigma_p$$

$$= 0,03 + \frac{0,05 w_A + 0,15 - 0,03}{\sqrt{0,3589 w_A^2 - 0,2178 w_A + 0,1089}} \sigma_p$$

$$= 0,03 + \frac{0,05 w_A + 0,12}{\sqrt{0,3589 w_A^2 - 0,2178 w_A + 0,1089}} \sigma_p$$

Đường phân bổ vốn là đường thẳng có độ dốc lớn nhất bởi vì nó tiếp xúc với đường cong được tạo thành bởi các danh mục đầu tư của hai tài sản rủi ro. Bảng minh họa 24 thể hiện đường phân bổ vốn dựa trên một tài sản phi rủi ro được thêm vào nhóm các tài sản.

#### **Bảng minh họa 24**

![](assets/Portfolio_Management.pdf-0055-08.png)

<!-- Picture Text: 25%<br>A = 20% return, 50% risk<br>20%<br>15%<br>B = 15% return, 33% risk<br>10%<br>Capital Allocation Line<br>5%<br>0%<br>0% 10% 20% 30% 40% 50% 60%<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return  () ER p<br> -->

> **Chú thích hình ảnh:** Trục hoành là Độ lệch chuẩn của danh mục đầu tư ($\sigma_p$), trục tung là Lợi nhuận kỳ vọng của danh mục đầu tư ($E(R_p)$). Đường phân bổ vốn (*Capital Allocation Line*) xuất phát từ 3% trên trục tung và tiếp xúc với đường cong nối giữa $B$ và $A$.

4. Độ dốc của đường phân bổ vốn đạt giá trị cực đại khi tỷ trọng đầu tư vào Tài sản A là 38,20%.<sup>7</sup> Phương trình của đường phân bổ vốn sử dụng $w_A$ bằng 38,20% là gì?

#### **Lời giải:**

Bằng cách thay 38,20% cho $w_A$ vào phương trình ở Phần 3, chúng ta thu được $E(R_p) = 0,03 + 0,4978 \sigma_p$ làm phương trình đường phân bổ vốn.

> 7 Bạn có thể tối đa hóa $\frac{0,05 w_A + 0,12}{\sqrt{0,3589 w_A^2 - 0,2178 w_A + 0,1089}}$ bằng cách lấy đạo hàm bậc nhất của hệ số góc theo $w_A$ và cho nó bằng 0.


<!-- PDF Page 56 -->

5. Sau khi đã tạo lập được đường phân bổ vốn, chúng ta quay lại với gia đình Lohrmann. Độ lệch chuẩn của một danh mục đầu tư mang lại mức lợi nhuận 20% và nằm trên đường phân bổ vốn là bao nhiêu? Danh mục đầu tư này so với tài sản A thì như thế nào?

#### **Lời giải:**

Giải phương trình đường phân bổ vốn để tìm độ lệch chuẩn: $0,20 = 0,03 + 0,4978 \sigma_p \Rightarrow \sigma_p = 34,2\%$. Danh mục đầu tư có lợi nhuận 20% này có cùng mức lợi nhuận với Tài sản A nhưng có độ lệch chuẩn thấp hơn, 34,2% thay vì 50,0%.

6. Rủi ro của các danh mục đầu tư có mức lợi nhuận 3%, 9%, 15%, và 20% là bao nhiêu?

#### **Lời giải:**

Bạn có thể tìm rủi ro của danh mục đầu tư bằng cách sử dụng phương trình đường phân bổ vốn: $E(R_p) = 0,03 + 0,4978 \sigma_p$. Đối với một danh mục đầu tư có lợi nhuận 15%, hãy viết $0,15 = 0,03 + 0,4978 \sigma_p$. Giải tìm $\sigma_p$ cho kết quả là 24,1%. Bạn có thể tính toán tương tự rủi ro của các danh mục đầu tư khác với các mức lợi nhuận đã cho.

Rủi ro của danh mục đầu tư ứng với mức lợi nhuận 3% là 0,0%, ứng với mức lợi nhuận 9% là 12,1%, ứng với mức lợi nhuận 15% là 24,1%, và ứng với mức lợi nhuận 20% là 34,2%. Các điểm này được vẽ trong Bảng minh họa 25.

#### **Bảng minh họa 25**

![](assets/Portfolio_Management.pdf-0056-12.png)

<!-- Picture Text: 25%<br>A = 20% return, 50% risk<br>20%<br>20%<br>15%<br>15% B = 15% return, 33% risk<br>10%<br>9% Capital Allocation Line<br>5%<br>3%<br>0%<br>0% 10% 20% 30% 40% 50%<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Đồ thị biểu diễn các điểm lợi nhuận 3%, 9%, 15%, và 20% nằm dọc trên Đường phân bổ vốn (*Capital Allocation Line*) cùng với đường biên giữa hai tài sản $B$ và $A$.

7. Độ hữu dụng mà gia đình Lohrmann nhận được từ một danh mục đầu tư có lợi nhuận 3%, 9%, 15%, và 20% là bao nhiêu? Hệ số ngại rủi ro của gia đình Lohrmann là 2,5.

#### **Lời giải:**

Để tìm độ hữu dụng, hãy sử dụng công thức tính độ hữu dụng với hệ số ngại rủi ro bằng 2,5:
$$\text{Độ hữu dụng (Utility)} = E(R_p) - 0,5 \times 2,5 \sigma_p^2$$
$$\text{Utility}(3\%) = 0,0300$$
$$\text{Utility}(9\%) = 0,09 - 0,5 \times 2,5 \times 0,121^2 = +0,0717$$
$$\text{Utility}(15\%) = 0,15 - 0,5 \times 2,5 \times 0,241^2 = +0,0774$$
$$\text{Utility}(20\%) = 0,20 - 0,5 \times 2,5 \times 0,341^2 = +0,0546$$

Dựa trên thông tin trên, gia đình Lohrmann chọn danh mục đầu tư có tỷ suất sinh lợi 15% và độ lệch chuẩn 24,1% bởi vì nó có


---

# Tập 9: Quản lý Danh mục Đầu tư (*Portfolio Management*)
## Học phần 1: Rủi ro và Lợi nhuận Danh mục Đầu tư: Phần I (*Portfolio Risk and Return: Part I*)
### Phần 4/4: Tóm tắt & Bài tập Thực hành (*Summary & Practice Problems*) (Trang PDF 57–70)

---

<!-- PDF Page 57 -->

độ hữu dụng cao nhất: $0,0774$. Cuối cùng, Bảng minh họa 26 thể hiện đường bàng quan tiếp xúc với đường phân bổ vốn để tạo ra danh mục đầu tư tối ưu của nhà đầu tư cho gia đình Lohrmann.

![](assets/Portfolio_Management.pdf-0057-03.png)

<!-- Picture Text: Exhibit 26<br>Lohrmanns’ Utility Curve 20% A = 20% return, 50% risk<br>20% (not to scale)<br>15% 15% B = 15% return, 33% risk<br>10%<br>Lohrmanns’ Optimal portfolio<br>9%<br>5% Capital Allocation Line<br>3%<br>0%<br>0% 10% 20% 30% 40% 50%<br>Standard Deviation of Portfolio σ p<br>Expected Portfolio Return () ER p<br> -->

> **Chú thích hình ảnh:** Bảng minh họa 26: Đường cong hữu dụng của gia đình Lohrmann (*Lohrmanns’ Utility Curve*, không vẽ theo đúng tỷ lệ) tiếp xúc với Đường phân bổ vốn (*Capital Allocation Line*) tại mức lợi nhuận 15% – Danh mục đầu tư tối ưu của gia đình Lohrmann (*Lohrmanns’ Optimal portfolio*).

### **Sở thích của Nhà đầu tư và các Danh mục Đầu tư Tối ưu (*Investor Preferences and Optimal Portfolios*)**

Vị trí của một danh mục đầu tư tối ưu của nhà đầu tư phụ thuộc vào sở thích rủi ro của nhà đầu tư đó. Một nhà đầu tư rất ngại rủi ro có thể đầu tư một tỷ trọng lớn, thậm chí 100%, tài sản của mình vào tài sản phi rủi ro. Danh mục đầu tư tối ưu trong trường hợp của nhà đầu tư này sẽ nằm gần trục tung (*y-axis*). Tuy nhiên, một nhà đầu tư ít ngại rủi ro hơn có thể đầu tư một phần lớn tài sản của mình vào tài sản rủi ro tối ưu. Danh mục đầu tư tối ưu trong trường hợp của nhà đầu tư này sẽ nằm gần Điểm P hơn trong Bảng minh họa 22.

Một số nhà đầu tư ít ngại rủi ro hơn (tức là có khả năng chịu đựng rủi ro cao) có thể muốn chấp nhận nhiều rủi ro hơn nữa vì cơ hội đạt được lợi nhuận cao hơn. Một nhà đầu tư như vậy có thể vay tiền để đầu tư nhiều hơn vào danh mục đầu tư rủi ro. Nếu nhà đầu tư vay thêm một khoản tương đương 25% tài sản của mình, người đó có thể đầu tư 125% vào danh mục đầu tư rủi ro tối ưu. Danh mục đầu tư tối ưu của nhà đầu tư đối với một nhà đầu tư như vậy sẽ nằm về phía bên phải của Điểm P trên đường phân bổ vốn.

Như vậy, khi di chuyển từ tài sản phi rủi ro dọc theo đường phân bổ vốn, chúng ta sẽ bắt gặp những nhà đầu tư sẵn sàng chấp nhận nhiều rủi ro hơn. Tại Điểm P, nhà đầu tư đầu tư 100% vào danh mục đầu tư rủi ro tối ưu. Vượt quá Điểm P, nhà đầu tư chấp nhận nhiều rủi ro hơn nữa bằng cách vay tiền và đầu tư vào danh mục đầu tư rủi ro tối ưu.

Lưu ý rằng chúng ta có thể đáp ứng nhu cầu của tất cả các kiểu nhà đầu tư chỉ với hai danh mục đầu tư: tài sản phi rủi ro và danh mục đầu tư rủi ro tối ưu. Bảng minh họa 22 cũng là một minh họa cho định lý phân tách hai quỹ (*two-fund separation theorem*). Danh mục P là danh mục đầu tư rủi ro tối ưu được lựa chọn mà không cần xét đến sở thích của nhà đầu tư. Danh mục đầu tư tối ưu của nhà đầu tư được lựa chọn trên đường phân bổ vốn bằng cách chồng các đường bàng quan có tích hợp sở thích của nhà đầu tư lên đó.

# **TÓM TẮT (*SUMMARY*)**

Bài đọc này cung cấp mô tả và cách tính toán các đặc điểm đầu tư, chẳng hạn như rủi ro và lợi nhuận, mà các nhà đầu tư sử dụng khi đánh giá các tài sản để đầu tư. Tiếp theo đó là các phần nói về việc xây dựng danh mục đầu tư, lựa chọn một danh mục đầu tư rủi ro tối ưu, và sự thấu hiểu về mức độ ngại rủi ro cũng như các đường bàng quan. Cuối cùng,


<!-- PDF Page 58 -->

tiếp điểm (*tangency point*) của các đường bàng quan với đường phân bổ vốn cho phép xác định danh mục đầu tư tối ưu của nhà đầu tư. Các khái niệm trọng tâm được trình bày trong bài đọc bao gồm:

- Tỷ suất sinh lợi thời kỳ nắm giữ (*holding period return*) là phù hợp nhất cho một thời kỳ nắm giữ đơn lẻ, được xác định trước.

- Tỷ suất sinh lợi nhiều kỳ (*multiperiod returns*) có thể được tổng hợp theo nhiều cách. Mỗi phép tính lợi nhuận có những ứng dụng đặc thù để đánh giá các khoản đầu tư.

- Các nhà đầu tư ngại rủi ro (*risk-averse investors*) đưa ra các quyết định đầu tư dựa trên sự đánh đổi giữa rủi ro và lợi nhuận (*risk–return trade-off*), tối đa hóa lợi nhuận cho cùng một mức rủi ro, và tối thiểu hóa rủi ro cho cùng một mức lợi nhuận. Tuy nhiên, họ có thể quan ngại trước những sự sai lệch khỏi phân phối tỷ suất sinh lợi chuẩn (*normal return distribution*) và khỏi các giả định về tính hiệu quả vận hành (*operational efficiency*) của thị trường tài chính.

- Các nhà đầu tư là những người ngại rủi ro, và dữ liệu lịch sử xác nhận rằng các thị trường tài chính định giá tài sản dành cho những nhà đầu tư ngại rủi ro.

- Rủi ro của một danh mục đầu tư gồm hai tài sản phụ thuộc vào tỷ trọng của mỗi tài sản, độ lệch chuẩn của chúng và hệ số tương quan (hoặc hiệp phương sai) giữa tỷ suất sinh lợi của các tài sản. Khi số lượng tài sản trong một danh mục đầu tư tăng lên, hệ số tương quan giữa rủi ro của các tài sản trở thành một yếu tố quyết định quan trọng hơn đối với rủi ro của danh mục đầu tư.

- Việc kết hợp các tài sản có hệ số tương quan thấp giúp làm giảm rủi ro của danh mục đầu tư.

- Định lý phân tách hai quỹ (*two-fund separation theorem*) cho phép chúng ta tách biệt việc ra quyết định thành hai bước. Trong bước đầu tiên, danh mục đầu tư rủi ro tối ưu và đường phân bổ vốn được xác định, vốn giống nhau đối với tất cả các nhà đầu tư. Trong bước thứ hai, sở thích rủi ro của nhà đầu tư cho phép chúng ta tìm ra một danh mục đầu tư tối ưu duy nhất cho từng nhà đầu tư.

- Việc bổ sung thêm một tài sản phi rủi ro tạo ra các danh mục đầu tư chiếm ưu thế vượt trội (*dominant*) so với các danh mục đầu tư gồm các tài sản rủi ro trong mọi trường hợp ngoại trừ ngay tại danh mục đầu tư rủi ro tối ưu.

Bằng việc nắm vững nội dung của bài đọc này, bạn sẽ có thể tự tin tính toán danh mục đầu tư tối ưu của một nhà đầu tư khi biết sở thích rủi ro của nhà đầu tư đó và tập hợp các tài sản có thể đầu tư hiện có.


<!-- PDF Page 59 -->

# **TÀI LIỆU THAM KHẢO (*REFERENCES*)**

_2009 Ibbotson Stocks, Bonds, Bills, and Inflation (SBBI) Classic Yearbook_. 2009. Chicago, IL: Morningstar.

Bogle, John C. 2008. “Black Monday and Black Swans.” _Financial Analysts Journal_ 64, vol. , no. 2: 30–40. 10.2469/faj.v64.n2.9

Dimson, Elroy, Paul Marsh, and Mike Staunton. 2009. _Credit Suisse Global Investment Returns Sourcebook_. _2009._ Zurich, Switzerland: Credit Suisse Research Institute.

Taleb, Nassim N. 2007. _The Black Swan: The Impact of the Highly Improbable_. New York: Random House Inc.


<!-- PDF Page 60 -->

# **BÀI TẬP THỰC HÀNH (*PRACTICE PROBLEMS*)**

**1.** Liên quan đến chi phí giao dịch, tính thanh khoản (*liquidity*) _ít có khả năng_ tác động nhất đến:

   - **A.** giá cổ phiếu (*stock price*).

   - **B.** chênh lệch giá mua – bán (*bid–ask spreads*).

   - **C.** hoa hồng môi giới (*brokerage commissions*).

**2.** Bằng chứng về sự ngại rủi ro (*risk aversion*) được minh họa _tốt nhất_ bởi một mối quan hệ rủi ro – lợi nhuận mang tính chất:

   - **A.** ngược chiều (*negative*).

   - **B.** trung lập (*neutral*).

   - **C.** cùng chiều (*positive*).

**3.** Đối với các nhà đầu tư ngại rủi ro, một tài sản phi rủi ro (*risk-free asset*) sẽ tạo ra một giá trị độ hữu dụng bằng số (*numerical utility*):

   - **A.** giống nhau đối với tất cả các cá nhân.

   - **B.** dương đối với các nhà đầu tư ngại rủi ro.

   - **C.** bằng không đối với các nhà đầu tư tìm kiếm rủi ro.

**4.** Theo lý thuyết hữu dụng (*utility theory*), nhà đầu tư ngại rủi ro nhất sẽ có một đường bàng quan (*indifference curve*) với:

   - **A.** độ lồi lớn nhất (*most convexity*).

   - **B.** giá trị tung độ gốc nhỏ nhất (*smallest intercept value*).

   - **C.** hệ số góc lớn nhất (*greatest slope coefficient*).

**5.** Đối với hàm hữu dụng của một nhà đầu tư được biểu diễn là: $U = E(r) - \frac{1}{2} A \sigma^2$, giá trị nào sau đây của thước đo mức độ ngại rủi ro thể hiện mức độ ngại rủi ro _ít nhất_?

   - **A.** −4.

   - **B.** 0.

   - **C.** 4.

## **Thông tin sau đây liên quan đến các câu hỏi 6–7**

Một nhà hoạch định tài chính đã tạo lập dữ liệu sau đây để minh họa việc ứng dụng lý thuyết hữu dụng vào lựa chọn danh mục đầu tư:


<!-- PDF Page 61 -->

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|
|---|---|---|
|1|18|2|
|2|19|8|
|3|20|15|
|4|18|30|

**6.** Một nhà đầu tư trung lập với rủi ro (*risk-neutral investor*) _có nhiều khả năng nhất_ sẽ chọn:

   - **A.** Khoản đầu tư 1.

   - **B.** Khoản đầu tư 2.

   - **C.** Khoản đầu tư 3.

**7.** Nếu hàm hữu dụng của một nhà đầu tư được biểu diễn là $U = E(r) - \frac{1}{2} A \sigma^2$ và thước đo mức độ ngại rủi ro có giá trị là −2, thì nhà đầu tư tìm kiếm rủi ro (*risk-seeking investor*) _có nhiều khả năng nhất_ sẽ chọn:

   - **A.** Khoản đầu tư 2.

   - **B.** Khoản đầu tư 3.

   - **C.** Khoản đầu tư 4.

**8.** Nếu hàm hữu dụng của một nhà đầu tư được biểu diễn là $U = E(r) - \frac{1}{2} A \sigma^2$ và thước đo mức độ ngại rủi ro có giá trị là 2, thì nhà đầu tư ngại rủi ro _có nhiều khả năng nhất_ sẽ chọn:

   - **A.** Khoản đầu tư 1.

   - **B.** Khoản đầu tư 2.

   - **C.** Khoản đầu tư 3.

**9.** Nếu hàm hữu dụng của một nhà đầu tư được biểu diễn là $U = E(r) - \frac{1}{2} A \sigma^2$ và thước đo mức độ ngại rủi ro có giá trị là 4, thì nhà đầu tư ngại rủi ro _có nhiều khả năng nhất_ sẽ chọn:

   - **A.** Khoản đầu tư 1.

   - **B.** Khoản đầu tư 2.

   - **C.** Khoản đầu tư 3.

**10.** Theo lý thuyết danh mục đầu tư trung bình – phương sai (*mean–variance portfolio theory*), đường phân bổ vốn (*capital allocation line* – CAL) là sự kết hợp giữa tài sản phi rủi ro và một danh mục đầu tư gồm tất cả:

   - **A.** các tài sản rủi ro (*risky assets*).

   - **B.** các chứng khoán vốn cổ phần (*equity securities*).

   - **C.** các khoản đầu tư khả thi (*feasible investments*).

**11.** Hai nhà đầu tư cá nhân có mức độ ngại rủi ro khác nhau sẽ có các danh mục đầu tư tối ưu nằm:

   - **A.** phía dưới đường phân bổ vốn.


<!-- PDF Page 62 -->

   - **B.** trên đường phân bổ vốn.

   - **C.** phía trên đường phân bổ vốn.

**12.** Theo lý thuyết thị trường vốn (*capital market theory*), đặc điểm tài sản nào sau đây _ít có khả năng nhất_ tác động đến phương sai của một danh mục đầu tư có tỷ trọng đều (*equally weighted portfolio*) của nhà đầu tư?

   - **A.** Tỷ suất sinh lợi của tài sản (*Return on the asset*).

   - **B.** Độ lệch chuẩn của tài sản (*Standard deviation of the asset*).

   - **C.** Hiệp phương sai của tài sản đó với các tài sản khác trong danh mục đầu tư (*Covariances of the asset with the other assets in the portfolio*).

**13.** Một nhà quản lý danh mục đầu tư tạo lập danh mục đầu tư sau đây:

|**Chứng khoán (*Security*)**|**Tỷ trọng chứng khoán (*Security Weight*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|
|---|---|---|
|1|30|20|
|2|70|12|

Nếu hệ số tương quan của tỷ suất sinh lợi giữa hai chứng khoán là 0,40, độ lệch chuẩn kỳ vọng của danh mục đầu tư _gần nhất_ với:

   - **A.** 10,7%.

   - **B.** 11,3%.

   - **C.** 12,1%.

**14.** Một nhà quản lý danh mục đầu tư tạo lập danh mục đầu tư sau đây:

|**Chứng khoán (*Security*)**|**Tỷ trọng chứng khoán (*Security Weight*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|
|---|---|---|
|1|30|20|
|2|70|12|

Nếu hiệp phương sai của tỷ suất sinh lợi giữa hai chứng khoán là −0,0240, độ lệch chuẩn kỳ vọng của danh mục đầu tư _gần nhất_ với:

   - **A.** 2,4%.

   - **B.** 7,5%.

   - **C.** 9,2%.

## **Thông tin sau đây liên quan đến các câu hỏi 15–16**

Một nhà quản lý danh mục đầu tư tạo lập danh mục đầu tư sau đây:


<!-- PDF Page 63 -->

|**Chứng khoán (*Security*)**|**Tỷ trọng chứng khoán (*Security Weight*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|
|---|---|---|
|1|30|20|
|2|70|12|

**15.** Nếu độ lệch chuẩn của danh mục đầu tư là 14,40%, hệ số tương quan giữa hai chứng khoán bằng:

   - **A.** -1,0.

   - **B.** 0,0.

   - **C.** 1,0.

**16.** Nếu độ lệch chuẩn của danh mục đầu tư là 14,40%, hiệp phương sai giữa hai chứng khoán bằng:

   - **A.** 0,0006.

   - **B.** 0,0240.

   - **C.** 1,0000.

## **Thông tin sau đây liên quan đến các câu hỏi 17–19**

Một nhà quản lý danh mục đầu tư tạo lập danh mục đầu tư sau đây:

|**Chứng khoán (*Security*)**|**Lợi nhuận hàng năm kỳ vọng (*Expected Annual Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|
|---|---|---|
|1|16|20|
|2|12|20|

**17.** Nếu danh mục đầu tư gồm hai chứng khoán có tỷ suất sinh lợi kỳ vọng là 15%, tỷ trọng được đầu tư vào Chứng khoán 1 là:

   - **A.** 25%.

   - **B.** 50%.

   - **C.** 75%.

**18.** Nếu hệ số tương quan của tỷ suất sinh lợi giữa hai chứng khoán là −0,15, độ lệch chuẩn kỳ vọng của một danh mục đầu tư có tỷ trọng đều (*equal-weighted portfolio*) _gần nhất_ với:

   - **A.** 13,04%.

   - **B.** 13,60%.

   - **C.** 13,87%.

**19.** Nếu hai chứng khoán không tương quan (*uncorrelated*), độ lệch chuẩn kỳ vọng của một


<!-- PDF Page 64 -->

danh mục đầu tư có tỷ trọng đều _gần nhất_ với:

   - **A.** 14,00%.

   - **B.** 14,14%.

   - **C.** 20,00%.

## **Thông tin sau đây liên quan đến các câu hỏi 20–21**

Một chuyên gia phân tích đã đưa ra các dự phóng tỷ suất sinh lợi sau đây cho từng kịch bản trong ba kịch bản có khả năng xảy ra ngang nhau:

|**Tài sản (*Asset*)**|**Kịch bản 1 (*Outcome 1*) (%)**|**Kịch bản 2 (*Outcome 2*) (%)**|**Kịch bản 3 (*Outcome 3*) (%)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|
|---|---|---|---|---|
|1|12|0|6|6|
|2|12|6|0|6|
|3|0|6|12|6|

**20.** Nếu chuyên gia phân tích xây dựng các danh mục đầu tư gồm hai tài sản có tỷ trọng bằng nhau, cặp tài sản nào có độ lệch chuẩn kỳ vọng _thấp nhất_?

   - **A.** Tài sản 1 và Tài sản 2.

   - **B.** Tài sản 1 và Tài sản 3.

   - **C.** Tài sản 2 và Tài sản 3.

**21.** Nếu chuyên gia phân tích xây dựng các danh mục đầu tư gồm hai tài sản có tỷ trọng bằng nhau, cặp tài sản nào mang lại mức giảm thiểu rủi ro _ít nhất_?

   - **A.** Tài sản 1 và Tài sản 2.

   - **B.** Tài sản 1 và Tài sản 3.

   - **C.** Tài sản 2 và Tài sản 3.

**22.** Khi số lượng tài sản trong một danh mục đầu tư có tỷ trọng đều tăng lên, mức đóng góp của phương sai từng tài sản riêng lẻ vào độ biến động của danh mục đầu tư sẽ:

   - **A.** tăng lên.

   - **B.** giảm xuống.

   - **C.** giữ nguyên không đổi.

**23.** Đối với một danh mục đầu tư có tỷ trọng đều được tạo thành từ một số lượng lớn các tài sản, yếu tố nào sau đây đóng góp _nhiều nhất_ vào độ biến động của danh mục đầu tư?

   - **A.** Phương sai trung bình của các tài sản riêng lẻ.

   - **B.** Độ lệch chuẩn của các tài sản riêng lẻ.

   - **C.** Hiệp phương sai trung bình giữa tất cả các cặp tài sản.


<!-- PDF Page 65 -->

**24.** Hệ số tương quan giữa các tài sản trong một danh mục đầu tư gồm hai tài sản tăng lên trong một đợt suy giảm của thị trường. Nếu không có sự thay đổi nào về tỷ trọng của mỗi tài sản được nắm giữ trong danh mục hoặc độ lệch chuẩn kỳ vọng của các tài sản riêng lẻ, thì độ biến động của danh mục đầu tư _có nhiều khả năng nhất_ sẽ:

   - **A.** tăng lên.

   - **B.** giảm xuống.

   - **C.** giữ nguyên không đổi.

**25.** Phát biểu nào sau đây là _kém chính xác nhất_? Đường biên hiệu quả (*efficient frontier*) là tập hợp tất cả các tài sản rủi ro có thể đạt được với:

   - **A.** tỷ suất sinh lợi kỳ vọng cao nhất cho một mức rủi ro nhất định.

   - **B.** lượng rủi ro thấp nhất cho một mức lợi nhuận nhất định.

   - **C.** tỷ suất sinh lợi kỳ vọng cao nhất so với lãi suất phi rủi ro.

**26.** Danh mục đầu tư nằm trên đường biên phương sai tối thiểu (*minimum-variance frontier*) có độ lệch chuẩn thấp nhất là:

   - **A.** không thể đạt được (*unattainable*).

   - **B.** danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*).

   - **C.** danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*).

**27.** Tập hợp các danh mục đầu tư nằm trên đường biên phương sai tối thiểu chiếm ưu thế vượt trội so với tất cả các tập hợp danh mục đầu tư nằm phía dưới danh mục đầu tư có phương sai tối thiểu toàn cục là:

   - **A.** đường phân bổ vốn (*capital allocation line*).

   - **B.** đường biên hiệu quả Markowitz (*Markowitz efficient frontier*).

   - **C.** tập hợp các danh mục đầu tư rủi ro tối ưu (*set of optimal risky portfolios*).

**28.** Đường phân bổ vốn vượt trội (*dominant capital allocation line*) là sự kết hợp giữa tài sản phi rủi ro và:

   - **A.** danh mục đầu tư rủi ro tối ưu (*optimal risky portfolio*).

   - **B.** danh mục đầu tư có sử dụng đòn bẩy gồm các tài sản rủi ro (*levered portfolio of risky assets*).

   - **C.** danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*).

**29.** So với đường biên hiệu quả của các tài sản rủi ro, đường phân bổ vốn vượt trội có tỷ suất sinh lợi cao hơn đối với các mức rủi ro lớn hơn danh mục đầu tư rủi ro tối ưu nhờ vào khả năng của nhà đầu tư trong việc:

   - **A.** cho vay với lãi suất phi rủi ro (*lend at the risk-free rate*).

   - **B.** đi vay với lãi suất phi rủi ro (*borrow at the risk-free rate*).

   - **C.** mua tài sản phi rủi ro (*purchase the risk-free asset*).

**30.** Theo lý thuyết trung bình – phương sai, danh mục đầu tư tối ưu được quyết định bởi yếu tố nào của từng nhà đầu tư cá nhân?

   - **A.** Lãi suất phi rủi ro (*risk-free rate*).


<!-- PDF Page 66 -->

   - **B.** Lãi suất đi vay (*borrowing rate*).

   - **C.** Sở thích rủi ro (*risk preference*).


<!-- PDF Page 67 -->

# **LỜI GIẢI (*SOLUTIONS*)**

1. **C là đáp án đúng.** Hoa hồng môi giới (*brokerage commissions*) được thương lượng với công ty môi giới. Tính thanh khoản của một chứng khoán tác động đến tính hiệu quả vận hành của chi phí giao dịch. Cụ thể, tính thanh khoản tác động đến chênh lệch giá mua – bán (*bid–ask spread*) và có thể tác động đến giá cổ phiếu (nếu khả năng bán cổ phiếu bị suy giảm bởi sự không chắc chắn gắn liền với việc có thể bán được cổ phiếu đó).

2. **C là đáp án đúng.** Dữ liệu lịch sử qua các khoảng thời gian dài chỉ ra rằng tồn tại một mối quan hệ rủi ro – lợi nhuận cùng chiều (*positive risk–return relationship*), vốn là sự phản ánh mức độ ngại rủi ro của nhà đầu tư.

3. **A là đáp án đúng.** Một tài sản phi rủi ro có phương sai bằng không và không phụ thuộc vào việc nhà đầu tư là người trung lập với rủi ro, tìm kiếm rủi ro hay ngại rủi ro. Nghĩa là, khi biết hàm hữu dụng của một khoản đầu tư được biểu diễn là $U = E(r) - \frac{1}{2} A \sigma^2$, trong đó $A$ là thước đo mức độ ngại rủi ro, thì dấu của $A$ không còn liên quan nếu phương sai bằng không (giống như phương sai của một tài sản phi rủi ro).

4. **C là đáp án đúng.** Nhà đầu tư ngại rủi ro nhất có đường bàng quan với độ dốc lớn nhất (*greatest slope*).

5. **A là đáp án đúng.** Một giá trị âm trong hàm hữu dụng đã cho chỉ ra rằng nhà đầu tư là một người tìm kiếm rủi ro (*risk seeker*).

6. **C là đáp án đúng.** Khoản đầu tư 3 có tỷ suất sinh lợi cao nhất. Rủi ro không liên quan đối với một nhà đầu tư trung lập với rủi ro, người sẽ có thước đo mức độ ngại rủi ro bằng 0. Với hàm hữu dụng đã cho, nhà đầu tư trung lập với rủi ro sẽ thu được độ hữu dụng lớn nhất từ Khoản đầu tư 3.

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|**Độ hữu dụng (*Utility*) $A = 0$**|
|---|---|---|---|
|1|18|2|0.1800|
|2|19|8|0.1900|
|3|20|15|0.2000|
|4|18|30|0.1800|

7. **C là đáp án đúng.** Khoản đầu tư 4 mang lại giá trị độ hữu dụng cao nhất ($0,2700$) đối với một nhà đầu tư tìm kiếm rủi ro có thước đo mức độ ngại rủi ro bằng −2.

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|**Độ hữu dụng (*Utility*) $A = -2$**|
|---|---|---|---|
|1|18|2|0.1804|
|2|19|8|0.1964|
|3|20|15|0.2225|
|4|18|30|0.2700|

8. **B là đáp án đúng.** Khoản đầu tư 2 mang lại giá trị độ hữu dụng cao nhất ($0,1836$) đối với một nhà đầu tư ngại rủi ro có thước đo mức độ ngại rủi ro bằng 2.


<!-- PDF Page 68 -->

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|**Độ hữu dụng (*Utility*) $A = 2$**|
|---|---|---|---|
|1|18|2|0.1796|
|2|19|8|0.1836|
|3|20|15|0.1775|
|4|18|30|0.0900|

9. **A là đáp án đúng.** Khoản đầu tư 1 mang lại giá trị độ hữu dụng cao nhất ($0,1792$) đối với một nhà đầu tư ngại rủi ro có thước đo mức độ ngại rủi ro bằng 4.

|**Khoản đầu tư (*Investment*)**|**Lợi nhuận kỳ vọng (*Expected Return*) (%)**|**Độ lệch chuẩn kỳ vọng (*Expected Standard Deviation*) (%)**|**Độ hữu dụng (*Utility*) $A = 4$**|
|---|---|---|---|
|1|18|2|0.1792|
|2|19|8|0.1772|
|3|20|15|0.1550|
|4|18|30|0.0000|

10. **A là đáp án đúng.** Đường CAL là sự kết hợp giữa tài sản phi rủi ro có rủi ro bằng không và danh mục gồm tất cả các tài sản rủi ro nhằm tạo ra tập hợp các khoản đầu tư khả thi. Việc cho phép đi vay với lãi suất phi rủi ro và đầu tư vào danh mục gồm tất cả các tài sản rủi ro sẽ mang lại các danh mục đầu tư có thể đạt được và chiếm ưu thế vượt trội so với các tài sản rủi ro nằm phía dưới đường CAL.

11. **B là đáp án đúng.** Đường CAL đại diện cho tập hợp tất cả các khoản đầu tư khả thi. Đường bàng quan của mỗi nhà đầu tư xác định sự kết hợp tối ưu giữa tài sản phi rủi ro và danh mục gồm tất cả các tài sản rủi ro, do đó phải nằm trên đường CAL.

12. **A là đáp án đúng.** Tỷ suất sinh lợi của tài sản không được sử dụng để tính phương sai của danh mục đầu tư [chỉ có tỷ trọng của các tài sản, độ lệch chuẩn (hoặc phương sai), và hiệp phương sai (hoặc hệ số tương quan) mới được sử dụng].

13. **C là đáp án đúng.**

$$\sigma_{\text{port}} = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2}$$

$$= \sqrt{(0,3)^2 (20\%)^2 + (0,7)^2 (12\%)^2 + 2 (0,3)(0,7)(0,40)(20\%)(12\%)}$$
$$= (0,3600\% + 0,7056\% + 0,4032\%)^{0,5} = (1,4688\%)^{0,5} = 12,11\%$$

14. **A là đáp án đúng.**

![](assets/Portfolio_Management.pdf-0068-14.png)

<!-- Formula Text: σ port  =  √ ______________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 Cov(R 1 R 2) -->

$$\sigma_{\text{port}} = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(R_1, R_2)}$$

$$= \sqrt{(0,3)^2 (20\%)^2 + (0,7)^2 (12\%)^2 + 2 (0,3)(0,7)(-0,0240)}$$

$$= (0,3600\% + 0,7056\% - 1,008\%)^{0,5} = (0,0576\%)^{0,5} = 2,40\%$$

15. **C là đáp án đúng.** Độ lệch chuẩn của danh mục đầu tư ở mức 14,40% chính là mức bình quân gia quyền ($0,3 \times 20\% + 0,7 \times 12\% = 14,40\%$), điều này chỉ có thể xảy ra nếu hệ số tương quan giữa hai chứng khoán bằng 1,0.

16. **B là đáp án đúng.** Độ lệch chuẩn của danh mục đầu tư ở mức 14,40% là bình quân gia quyền, điều này chỉ có thể xảy ra nếu hệ số tương quan giữa hai chứng khoán bằng 1,0. Nếu hệ số tương quan bằng 1,0, thì hiệp phương sai phải bằng 0,0240, được tính như sau: $\text{Cov}(R_1, R_2) = \rho_{12} \sigma_1 \sigma_2 = (1,0)(20\%)(12\%) = 2,40\% = 0,0240$.


<!-- PDF Page 69 -->

17. **C là đáp án đúng.**

$$R_p = w_1 \times R_1 + (1 - w_1) \times R_2$$
$$R_p = w_1 \times 16\% + (1 - w_1) \times 12\%$$
$$15\% = 0,75(16\%) + 0,25(12\%)$$

18. **A là đáp án đúng.**

$$\sigma_{\text{port}} = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2}$$
$$= \sqrt{(0,5)^2 (20\%)^2 + (0,5)^2 (20\%)^2 + 2 (0,5)(0,5)(-0,15)(20\%)(20\%)}$$
$$= (1,0000\% + 1,0000\% - 0,3000\%)^{0,5} = (1,7000\%)^{0,5} = 13,04\%$$

19. **B là đáp án đúng.**

![](assets/Portfolio_Management.pdf-0069-08.png)

<!-- Formula Text: σ port  =  √ ____________________________ w 1 2 σ 1 2 + w 2 2 σ 2 2 + 2 w 1 w 2 ρ 1,2 σ 1 σ 2 = √ ___________________________________________________ (0.5) 2 (20%) 2 + (0.5) 2 (20%) 2 + 2(0.5)(0.5)(0.00)(20%)(20%) = (1.0000 %  + 1.0000 %  − 0.0000%) 0.5  =  (2.0000%) 0.5  =  14.14% -->

$$\sigma_{\text{port}} = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2}$$
$$= \sqrt{(0,5)^2 (20\%)^2 + (0,5)^2 (20\%)^2 + 2(0,5)(0,5)(0,00)(20\%)(20\%)}$$
$$= (1,0000\% + 1,0000\% - 0,0000\%)^{0,5} = (2,0000\%)^{0,5} = 14,14\%$$

20. **C là đáp án đúng.** Một danh mục đầu tư có tỷ trọng đều gồm Tài sản 2 và Tài sản 3 sẽ có độ lệch chuẩn danh mục thấp nhất, bởi vì ứng với mỗi kịch bản, danh mục đầu tư đều có cùng mức tỷ suất sinh lợi kỳ vọng là 6% (chúng có tương quan âm hoàn hảo).

21. **A là đáp án đúng.** Một danh mục đầu tư có tỷ trọng đều gồm Tài sản 1 và Tài sản 2 có mức độ biến động cao nhất trong ba cặp. Cả ba cặp đều có cùng tỷ suất sinh lợi kỳ vọng; tuy nhiên, danh mục gồm Tài sản 1 và Tài sản 2 mang lại mức giảm thiểu rủi ro ít nhất.

22. **B là đáp án đúng.** Mức đóng góp của phương sai (hoặc độ lệch chuẩn) của từng tài sản riêng lẻ vào độ biến động của danh mục đầu tư giảm xuống khi số lượng tài sản trong danh mục đầu tư có tỷ trọng đều tăng lên. Mức đóng góp của các thước đo biến động cùng chiều giữa các tài sản (tức là hiệp phương sai và hệ số tương quan) tăng lên khi số lượng tài sản trong danh mục đầu tư có tỷ trọng đều tăng lên. Phương trình sau đây đối với phương sai của một danh mục đầu tư có tỷ trọng đều minh họa những điểm này: $\sigma_p^2 = \frac{\bar{\sigma}^2}{N} + \frac{N - 1}{N} \overline{\text{COV}} = \frac{\bar{\sigma}^2}{N} + \frac{N - 1}{N} \bar{\rho} \bar{\sigma}^2$.

23. **C là đáp án đúng.** Các thước đo biến động cùng chiều giữa các tài sản tăng lên (tức là hiệp phương sai và hệ số tương quan) khi số lượng tài sản trong danh mục đầu tư có tỷ trọng đều tăng lên. Mức đóng góp của phương sai (hoặc độ lệch chuẩn) của từng tài sản riêng lẻ vào độ biến động của danh mục đầu tư giảm xuống khi số lượng tài sản trong danh mục đầu tư có tỷ trọng đều tăng lên. Phương trình sau đây đối với phương sai của một danh mục đầu tư có tỷ trọng đều minh họa những điểm này:

![](assets/Portfolio_Management.pdf-0069-13.png)

<!-- Formula Text: σ p 2  =    _ σ  2 _ N  +  N − 1 _ N   ‾ COV   =    _ σ  2 _ N  +  N − 1 _ N   _ ρ    _ σ  2. -->

$$\sigma_p^2 = \frac{\bar{\sigma}^2}{N} + \frac{N - 1}{N} \overline{\text{COV}} = \frac{\bar{\sigma}^2}{N} + \frac{N - 1}{N} \bar{\rho} \bar{\sigma}^2$$

24. **A là đáp án đúng.** Hệ số tương quan cao hơn sẽ tạo ra ít lợi ích đa dạng hóa hơn với điều kiện là các thành phần khác của độ lệch chuẩn danh mục đầu tư không thay đổi (tức là tỷ trọng và độ lệch chuẩn của các tài sản riêng lẻ).

25. **C là đáp án đúng.** Đường biên hiệu quả không tính đến lãi suất phi rủi ro. Đường biên hiệu quả là tập hợp tất cả các tài sản rủi ro có thể đạt được với tỷ suất sinh lợi kỳ vọng cao nhất cho một mức rủi ro nhất định hoặc lượng rủi ro thấp nhất cho một mức lợi nhuận nhất định.

26. **C là đáp án đúng.** Danh mục đầu tư có phương sai tối thiểu toàn cục (*global minimum-variance portfolio*) là danh mục nằm trên đường biên phương sai tối thiểu có độ lệch chuẩn thấp nhất. Mặc dù


<!-- PDF Page 70 -->

danh mục đầu tư này có thể đạt được, nhưng khi xét đến tài sản phi rủi ro, danh mục đầu tư có phương sai tối thiểu toàn cục không phải là danh mục đầu tư rủi ro tối ưu.

27. **B là đáp án đúng.** Đường biên hiệu quả Markowitz (*Markowitz efficient frontier*) có tỷ suất sinh lợi cao hơn cho một mức rủi ro nhất định. Xét theo danh mục đầu tư có phương sai tối thiểu, đường biên hiệu quả Markowitz là tập hợp các danh mục đầu tư nằm phía trên danh mục đầu tư có phương sai tối thiểu toàn cục và chiếm ưu thế vượt trội so với các danh mục đầu tư nằm phía dưới danh mục có phương sai tối thiểu toàn cục.

28. **A là đáp án đúng.** Việc sử dụng đòn bẩy và sự kết hợp giữa tài sản phi rủi ro với tài sản rủi ro tối ưu sẽ chiếm ưu thế vượt trội so với đường biên hiệu quả của các tài sản rủi ro (đường biên hiệu quả Markowitz).

29. **B là đáp án đúng.** Đường CAL chiếm ưu thế vượt trội so với đường biên hiệu quả tại mọi điểm ngoại trừ ngay tại danh mục đầu tư rủi ro tối ưu. Khả năng của nhà đầu tư trong việc mua thêm danh mục đầu tư rủi ro tối ưu bằng cách đi vay (tức là mua ký quỹ – *buying on margin*) tại mức lãi suất phi rủi ro giúp cho việc đạt được các mức tỷ suất sinh lợi cao hơn ở những mức rủi ro lớn hơn tài sản rủi ro tối ưu trở nên khả thi.

30. **C là đáp án đúng.** Sự kết hợp tối ưu của mỗi nhà đầu tư cá nhân giữa tài sản phi rủi ro và tài sản rủi ro tối ưu được quyết định bởi sở thích rủi ro (*risk preference*) của nhà đầu tư đó.
