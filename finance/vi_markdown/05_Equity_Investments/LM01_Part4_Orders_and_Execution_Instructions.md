# Tập 5: Đầu tư Cổ phần (Volume 5: Equity Investments)
## Học phần 1: Tổ chức và Cấu trúc Thị trường (Learning Module 1: Market Organization and Structure)
### Phần 4/6: Các Loại Lệnh và Chỉ thị Thực hiện (Orders and Execution Instructions) (PDF Pages 54–69)

---

<!-- PDF Page 54 -->

Nếu giá trị vốn chủ sở hữu giảm xuống dưới mức yêu cầu ký quỹ duy trì (*maintenance margin requirement*), người mua sẽ nhận được một **lệnh gọi ký quỹ bổ sung (*margin call*)**, tức là yêu cầu phải nộp thêm vốn chủ sở hữu. Nếu người mua không nộp bổ sung vốn chủ sở hữu cho nhà môi giới một cách kịp thời, nhà môi giới sẽ đóng vị thế đó lại (bán chứng khoán đi) để ngăn chặn các khoản lỗ phát sinh thêm và qua đó đảm bảo việc thu hồi khoản vay ký quỹ. 

Khi bạn mua chứng khoán ký quỹ, bạn phải biết mức giá mà tại đó bạn sẽ nhận được lệnh gọi ký quỹ bổ sung nếu giá giảm xuống. Câu trả lời cho câu hỏi này phụ thuộc vào vốn chủ sở hữu ban đầu của bạn và vào mức yêu cầu ký quỹ duy trì. 

##### **VÍ DỤ 20 (EXAMPLE 20)** 

### **Mức Giá Gọi Ký quỹ Bổ sung (Margin Call Price)** 

1. Một nhà giao dịch mua cổ phiếu ký quỹ bằng cách nộp 40 phần trăm giá cổ phiếu ban đầu ($\$20$) làm vốn chủ sở hữu. Yêu cầu ký quỹ duy trì đối với vị thế này là 25 phần trăm. Dưới mức giá nào thì một lệnh gọi ký quỹ bổ sung (*margin call*) sẽ xảy ra? 

### **Giải pháp (Solution):** 

Vốn chủ sở hữu ban đầu của nhà giao dịch là 40 phần trăm của mức giá cổ phiếu ban đầu $\$20$, tức là $\$8$ mỗi cổ phiếu. Những thay đổi tiếp theo trong vốn chủ sở hữu trên mỗi cổ phiếu đúng bằng mức thay đổi của giá cổ phiếu, sao cho vốn chủ sở hữu trên mỗi cổ phiếu bằng $\$8 + (P - 20)$, trong đó $P$ là giá cổ phiếu hiện hành. Lệnh gọi ký quỹ bổ sung diễn ra khi vốn chủ sở hữu giảm xuống dưới mức yêu cầu ký quỹ duy trì 25 phần trăm. Mức giá mà dưới ngưỡng đó lệnh gọi ký quỹ bổ sung sẽ diễn ra là nghiệm của phương trình sau đây: 

$$\frac{\text{Vốn chủ sở hữu/cổ phiếu (Equity/share)}}{\text{Giá/cổ phiếu (Price/share)}} = \frac{\$8 + P - 20}{P} = 25\%$$

Phương trình trên cho nghiệm tại $P = 16$. Khi giá giảm xuống dưới mức $\$16$, vốn chủ sở hữu sẽ ở mức dưới $\$4/\text{cổ phiếu}$, tức là thấp hơn 25 phần trăm của mức giá thị trường. 
*(Công thức tổng quát thường dùng: $\text{Giá Margin Call} = P_0 \times \frac{1 - \text{Ký quỹ ban đầu}}{1 - \text{Ký quỹ duy trì}} = 20 \times \frac{1 - 0,40}{1 - 0,25} = \$16$).*

Các nhà giao dịch thực hiện bán khống chứng khoán (*sell securities short*) cũng phải tuân thủ các yêu cầu ký quỹ bởi vì họ đã đi vay chứng khoán. Ban đầu, vốn chủ sở hữu của nhà giao dịch nâng đỡ cho vị thế bán khống ít nhất phải bằng tỷ lệ yêu cầu ký quỹ nhân với giá trị ban đầu của vị thế bán khống. Nếu giá chứng khoán tăng lên, vốn chủ sở hữu sẽ bị hao hụt. Đến một thời điểm nào đó, người bán khống sẽ phải đóng góp thêm vốn chủ sở hữu để đáp ứng yêu cầu ký quỹ duy trì. Nếu không, nhà môi giới sẽ mua lại chứng khoán trên thị trường để đóng vị thế bán khống (*cover the short position*) nhằm ngăn chặn các khoản lỗ phát sinh thêm và qua đó đảm bảo việc hoàn trả khoản vay cổ phiếu. 

# **<mark>12</mark> CÁC LOẠI LỆNH VÀ CHỈ THỊ THỰC HIỆN (ORDERS AND EXECUTION INSTRUCTIONS)** 

so sánh các chỉ thị thực hiện, chỉ thị hiệu lực và chỉ thị bù trừ thanh toán  
so sánh lệnh thị trường với lệnh giới hạn 

Người mua và người bán giao tiếp với các nhà môi giới, sở giao dịch và các nhà tạo lập thị trường giúp thu xếp giao dịch cho họ bằng cách phát ra các **lệnh giao dịch (*orders*)**. Tất cả các lệnh đều chỉ định rõ cần giao dịch công cụ nào, giao dịch số lượng bao nhiêu, và là mua hay bán. Hầu hết các lệnh cũng có các chỉ thị khác đính kèm theo chúng. Những chỉ thị bổ sung này có thể bao gồm chỉ thị thực hiện, chỉ thị hiệu lực, và chỉ thị bù trừ thanh toán. **Chỉ thị thực hiện (*Execution instructions*)** cho biết cách thức khớp lệnh, **chỉ thị hiệu lực (*validity instructions*)** cho biết khi nào lệnh có thể được khớp, và **chỉ thị bù trừ thanh toán (*clearing instructions*)** cho biết cách thức thu xếp việc thanh toán cuối cùng cho giao dịch. 


<!-- PDF Page 55 -->

Trong phần này, chúng tôi giới thiệu các chỉ thị lệnh khác nhau và giải thích cách thức các nhà giao dịch sử dụng chúng để đạt được mục tiêu của mình. Chúng tôi sẽ thảo luận về các cơ chế thực hiện lệnh — cách thức các sở giao dịch, nhà môi giới và nhà tạo lập thị trường khớp lệnh — trong phần tiếp theo. Tuy nhiên, để hiểu được các khái niệm trong phần này, bạn cần biết một chút về các cơ chế thực hiện lệnh. 

Trên hầu hết các thị trường, các nhà tạo lập thị trường (*dealers*) và nhiều nhà giao dịch tự doanh khác thường sẵn lòng mua từ, hoặc bán cho, các nhà giao dịch khác đang muốn bán hoặc mua. Các mức giá mà tại đó họ sẵn lòng mua vào được gọi là **giá chào mua (*bid prices*)** và các mức giá mà tại đó họ sẵn lòng bán ra được gọi là **giá chào bán (*ask prices*)**, hoặc đôi khi được gọi là **giá chào (*offer prices*)**. Giá chào bán (*ask prices*) luôn luôn cao hơn giá chào mua (*bid prices*). 

Các nhà giao dịch sẵn lòng giao dịch tại các mức giá khác nhau cũng có thể cho biết số lượng mà họ sẽ giao dịch tại những mức giá đó. Những số lượng này được gọi là **khối lượng chào mua (*bid sizes*)** và **khối lượng chào bán (*ask sizes*)** tùy thuộc vào việc chúng gắn với giá chào mua hay giá chào bán. 

Những người hành nghề nói rằng các nhà giao dịch đưa ra lời chào giao dịch là những người **tạo lập thị trường (*make a market*)**. Những người chấp nhận giao dịch với họ là những người **nhận/lấy thanh khoản thị trường (*take the market*)**. 

Mức giá chào mua cao nhất trên thị trường được gọi là **giá chào mua tốt nhất (*best bid*)**, và mức giá chào bán thấp nhất trên thị trường được gọi là **giá chào bán tốt nhất (*best offer* / *best ask*)**. Phần chênh lệch giữa giá chào mua tốt nhất và giá chào bán tốt nhất là **chênh lệch giá chào mua–chào bán của thị trường (*market bid–ask spread*)**. Khi các nhà giao dịch hỏi: “Thị trường đang thế nào?” (*“What’s the market?”*), họ muốn biết mức giá chào mua và chào bán tốt nhất cùng với khối lượng tương ứng của chúng. Chênh lệch giá chào mua–chào bán (*bid–ask spreads*) là một chi phí giao dịch ngầm định (*implicit cost of trading*). Những thị trường có chênh lệch giá chào mua–chào bán nhỏ là những thị trường mà tại đó chi phí giao dịch thấp, ít nhất là đối với các khối lượng được yết giá. Các *dealers* thường yết cả giá chào mua lẫn giá chào bán, và trong trường hợp đó, những người hành nghề nói rằng họ yết giá một **thị trường hai chiều (*two-sided market*)**. Mức chênh lệch giá chung của toàn thị trường (*market spread*) không bao giờ lớn hơn mức chênh lệch giá của bất kỳ một *dealer* riêng lẻ nào (*dealer spread*). 

### **Chỉ thị Thực hiện (Execution Instructions)** 

Lệnh thị trường và lệnh giới hạn truyền tải những chỉ thị thực hiện phổ biến nhất. Một **lệnh thị trường (*market order*)** chỉ thị cho nhà môi giới hoặc sở giao dịch phải đạt được mức giá tốt nhất hiện có ngay lập tức khi khớp lệnh đó. Một **lệnh giới hạn (*limit order*)** truyền tải gần như cùng một chỉ thị đó: Hãy lấy mức giá tốt nhất hiện có ngay lập tức, nhưng trong mọi trường hợp không được chấp nhận một mức giá cao hơn mức **giá giới hạn (*limit price*)** đã chỉ định khi mua hoặc không được chấp nhận một mức giá thấp hơn mức giá giới hạn đã chỉ định khi bán. 

Nhiều người lầm tưởng rằng lệnh giới hạn chỉ định mức giá chính xác mà tại đó các lệnh sẽ được giao dịch. Mặc dù các lệnh giới hạn thường được khớp tại đúng mức giá giới hạn của chúng, hãy nhớ rằng chỉ thị đầu tiên và trước nhất vẫn là phải lấy được mức giá tốt nhất hiện có. Nếu có những mức giá tốt hơn mức giá giới hạn đang sẵn có trên thị trường, các nhà môi giới và sở giao dịch phải lấy được những mức giá tốt hơn đó cho khách hàng của mình. 

Các lệnh thị trường nhìn chung được thực hiện ngay lập tức nếu có các nhà giao dịch khác sẵn lòng đứng ở phía đối ứng của giao dịch. Nhược điểm chính của lệnh thị trường là chúng có thể rất đắt đỏ khi thực hiện, đặc biệt là khi lệnh được đặt vào một thị trường của một chứng khoán có giao dịch thưa thớt (*thinly traded security*), hoặc tổng quát hơn, khi quy mô lệnh là lớn tương đối so với hoạt động giao dịch bình thường trên thị trường đó. Trong trường hợp đó, một lệnh mua thị trường có thể bị khớp ở mức giá rất cao, hoặc một lệnh bán thị trường có thể bị khớp ở mức giá rất thấp nếu không có nhà giao dịch nào sẵn lòng giao dịch ở các mức giá tốt hơn. Giá mua cao và giá bán thấp đại diện cho những sự nhượng bộ về giá (*price concessions*) trao cho các nhà giao dịch khác nhằm khuyến khích họ đứng vào phía đối ứng của giao dịch. Bởi vì quy mô của sự nhượng bộ về giá có thể rất khó dự đoán, và bởi vì giá cả thường thay đổi trong khoảng thời gian giữa lúc nhà giao dịch gửi lệnh đi và lúc lệnh cuối cùng được khớp, nên mức giá thực hiện (*execution prices*) đối với các lệnh thị trường thường không chắc chắn. 

Những người mua và người bán lo ngại về khả năng phải giao dịch ở những mức giá không thể chấp nhận được sẽ thêm các chỉ thị giá giới hạn vào lệnh của mình. Vấn đề chính đối với các lệnh giới hạn là chúng có thể không được thực hiện (*may not execute*). Lệnh giới hạn sẽ không được thực hiện nếu mức giá giới hạn trên một lệnh mua là quá thấp, hoặc nếu mức giá giới hạn trên một lệnh bán là quá cao. Ví dụ, nếu một nhà quản lý đầu tư gửi một lệnh giới hạn mua tại mức giá giới hạn là 20 (*buy limit 20*) và không có ai sẵn lòng bán ở mức giá bằng hoặc dưới 20, thì lệnh đó sẽ không được khớp. Nếu giá không bao giờ giảm xuống 20, nhà quản lý sẽ không bao giờ mua được. Nếu sau đó giá tăng lên, nhà quản lý sẽ đánh mất cơ hội kiếm lời từ đợt tăng giá đó. 


<!-- PDF Page 56 -->

Việc các nhà giao dịch sử dụng lệnh thị trường hay lệnh giới hạn khi cố gắng thu xếp giao dịch phụ thuộc vào mối quan tâm của họ về giá cả, tốc độ giao dịch nhanh chóng, và rủi ro không khớp được lệnh. Tính trung bình, các lệnh giới hạn giao dịch được ở mức giá tốt hơn so với các lệnh thị trường, nhưng chúng thường không khớp được. Các nhà giao dịch nhìn chung cảm thấy hối tiếc khi các lệnh giới hạn của họ không khớp được bởi vì thông thường họ đã có thể kiếm được lợi nhuận nếu như lệnh đó đã khớp. Các lệnh mua giới hạn không khớp được khi giá đang tăng lên, và các lệnh bán giới hạn không khớp được khi giá đang giảm xuống. Trong cả hai trường hợp, các nhà giao dịch lẽ ra đã có lợi hơn nếu lệnh của họ được khớp. 

Xác suất để một lệnh giới hạn được thực hiện phụ thuộc vào vị trí đặt lệnh tương đối so với giá thị trường. Một lệnh được định giá quyết liệt (*aggressively priced order*) có nhiều khả năng giao dịch được hơn so với một lệnh được định giá kém quyết liệt hơn. Một lệnh mua giới hạn được định giá quyết liệt khi mức giá giới hạn của nó ở mức cao tương đối so với giá chào mua và chào bán của thị trường. Nếu mức giá giới hạn mua được đặt cao hơn hoặc bằng giá chào bán tốt nhất (*best offer*), lệnh mua đó nhìn chung sẽ được khớp một phần hoặc toàn bộ ngay tại mức giá chào bán tốt nhất, tùy thuộc vào khối lượng hiện có tại mức giá chào bán tốt nhất đó. Những lệnh giới hạn như vậy được gọi là **lệnh giới hạn có thể khớp ngay (*marketable limit orders*)** bởi vì ít nhất một phần của lệnh có thể giao dịch được ngay lập tức. Một lệnh mua giới hạn với mức giá rất cao so với thị trường thì về bản chất chính là một lệnh thị trường. 

Nếu lệnh mua giới hạn được đặt cao hơn giá chào mua tốt nhất (*best bid*) nhưng thấp hơn giá chào bán tốt nhất (*best offer*), các nhà giao dịch nói rằng lệnh đó **tạo lập một thị trường mới (*makes a new market*)** bởi vì nó trở thành mức giá chào mua tốt nhất mới. Những lệnh như vậy nhìn chung sẽ không khớp ngay lập tức, nhưng chúng có thể thu hút những người bán đang quan tâm đến việc giao dịch. Một lệnh mua được đặt ngay tại mức giá chào mua tốt nhất hiện hành được gọi là **tạo lập thị trường (*make market*)**. Nó có thể phải xếp hàng chờ cho đến khi tất cả các lệnh mua khác đã đặt trước tại mức giá đó được giao dịch xong. Cuối cùng, một lệnh mua được đặt thấp hơn giá chào mua tốt nhất được gọi là **nằm phía sau thị trường (*behind the market*)**. Nó sẽ không được thực hiện trừ khi giá thị trường giảm xuống. Các nhà giao dịch gọi những lệnh giới hạn đang nằm chờ để được giao dịch là **lệnh giới hạn chờ khớp (*standing limit orders*)**. 

Các lệnh bán giới hạn được coi là định giá quyết liệt nếu mức giá giới hạn ở mức thấp tương đối so với giá thị trường. Giá giới hạn của một lệnh bán giới hạn có thể khớp ngay (*marketable sell limit order*) nằm ở mức bằng hoặc thấp hơn giá chào mua tốt nhất (*best bid*). Một lệnh bán giới hạn được đặt nằm giữa giá chào mua tốt nhất và giá chào bán tốt nhất sẽ tạo lập một thị trường mới (*makes a new market*) ở phía bên bán, một lệnh đặt ngay tại mức giá chào bán tốt nhất sẽ tạo lập thị trường (*makes market*), và một lệnh đặt cao hơn mức giá chào bán tốt nhất là nằm phía sau thị trường (*behind the market*). 

Bảng 2 (Exhibit 2) trình bày một **sổ lệnh giới hạn (*limit order book*)** giản lược, trong đó các lệnh được trình bày xếp hạng theo mức giá giới hạn của chúng đối với một thị trường giả định. Thị trường này đang ở trạng thái “chào mua ở 26, chào bán ở 28” (*“26 bid, offered at 28”*) bởi vì giá chào mua tốt nhất là 26 và giá chào bán tốt nhất là 28. 


<!-- PDF Page 57 -->

**Bảng 2 (Exhibit 2): Các Thuật ngữ Nhà giao dịch Sử dụng để Mô tả Các Lệnh Giới hạn Chờ khớp (Standing Limit Orders)** 

||**Giá đặt lệnh (Order Prices)**|||
|---|---|---|---|
||**Chào mua (*Bids*)**|**Chào bán (*Offers / Asks*)**|**Mô tả trạng thái lệnh**|
|||33|Các lệnh bán được định giá kém quyết liệt nhất nằm *xa thị trường* (*far from the market*).|
|||32||
|||31<br>30|Các lệnh bán này nằm *phía sau thị trường* (*behind the market*). Chúng ta cũng nói rằng chúng nằm *cách xa thị trường* (*away from the market*).|
|||29||
|||**28**|*Giá chào bán tốt nhất* (*best offer*) nằm *ngay tại thị trường* (*at the market*).|
|Giá chào mua tốt nhất và giá chào bán tốt nhất *tạo lập thị trường* (*make the market*).|||Khoảng không gian giữa giá chào mua tốt nhất và giá chào bán tốt nhất hiện tại được gọi là *bên trong thị trường* (*inside the market*). Nếu một lệnh giới hạn mới đến và nằm ở đây, nó *tạo lập một thị trường mới* (*makes a new market*).|
||**26**||*Giá chào mua tốt nhất* (*best bid*) nằm *ngay tại thị trường* (*at the market*).|
||25|||
||24<br>23||Các lệnh mua này nằm *phía sau thị trường* (*behind the market*). Chúng ta cũng nói rằng chúng nằm *cách xa thị trường* (*away from the market*).|
||22|||
||21||Các lệnh mua được định giá kém quyết liệt nhất nằm *xa thị trường* (*far from the market*).|



_Nguồn_ : _Trading and Exchanges_ .<sup>1</sup> 

##### **VÍ DỤ 21 (EXAMPLE 21)** 

### **Tạo lập Thị trường và Nhận Thanh khoản Thị trường (Making and Taking)** 

1. Sự khác biệt giữa việc tạo lập thị trường (*making a market*) và việc nhận thanh khoản thị trường (*taking a market*) là gì? 

#### **Giải pháp (Solution):** 

Một nhà giao dịch tạo lập thị trường khi nhà giao dịch đó đưa ra lời chào để giao dịch (cung cấp thanh khoản). Một nhà giao dịch nhận thanh khoản thị trường khi nhà giao dịch đó chấp nhận một lời chào giao dịch có sẵn (tiêu thụ thanh khoản). 

2. Những loại lệnh nào có khả năng cao nhất gắn liền với việc tạo lập thị trường và việc nhận thanh khoản thị trường? 

#### **Giải pháp (Solution):** 

Các nhà giao dịch đặt các lệnh giới hạn chờ khớp (*standing limit orders*) nhằm trao cho các nhà giao dịch khác cơ hội để giao dịch. Do đó, các lệnh giới hạn chờ khớp tạo lập thị trường. Ngược lại, các nhà giao dịch sử dụng lệnh thị trường (*market orders*) hoặc lệnh giới hạn có thể khớp ngay (*marketable limit orders*) để chấp nhận các lời chào giao dịch có sẵn. Những lệnh có thể khớp ngay này nhận thanh khoản thị trường (*take the market*). 


<!-- PDF Page 58 -->

Tồn tại một sự đánh đổi (*trade-off*) giữa mức độ định giá quyết liệt của một lệnh và mức giá giao dịch cuối cùng đạt được. Mặc dù các lệnh được định giá quyết liệt sẽ khớp nhanh hơn và chắc chắn hơn so với các lệnh giới hạn được định giá kém quyết liệt hơn, nhưng mức giá mà tại đó chúng được thực hiện lại kém thuận lợi hơn. Những người mua muốn giao dịch nhanh chóng phải trả mức giá cao hơn để làm tăng xác suất giao dịch nhanh. Tương tự, những người bán muốn giao dịch nhanh chóng phải chấp nhận mức giá thấp hơn để làm tăng xác suất giao dịch nhanh. 

Một số chỉ thị thực hiện lệnh quy định các điều kiện về quy mô khối lượng. Ví dụ, **lệnh thực hiện toàn bộ hoặc hủy bỏ (*all-or-nothing orders* – AON)** chỉ có thể giao dịch nếu toàn bộ khối lượng của lệnh đó có thể được giao dịch hết cùng lúc. Tương tự, các nhà giao dịch có thể chỉ định khối lượng khớp tối thiểu (*minimum fill sizes*). Quy định cụ thể này rất phổ biến khi chi phí thanh toán bù trừ phụ thuộc vào số lượng giao dịch được thực hiện để lấp đầy một lệnh chứ không phụ thuộc vào tổng quy mô của lệnh đó. 

**Chỉ thị hiển thị (*Exposure instructions*)** cho biết liệu có nên hiển thị lệnh hay không, hiển thị như thế nào, và có thể là hiển thị cho ai biết. **Lệnh ẩn (*Hidden orders*)** chỉ được hiển thị cho các nhà môi giới hoặc sở giao dịch tiếp nhận chúng. Các tổ chức này không được phép tiết lộ các lệnh ẩn cho các nhà giao dịch khác biết cho đến khi họ có thể khớp được chúng. Các nhà giao dịch sử dụng lệnh ẩn khi họ lo sợ rằng các nhà giao dịch khác có thể hành xử một cách chiến lược gây bất lợi cho họ nếu biết rằng đang có một lệnh lớn nằm trên thị trường. Các nhà giao dịch chỉ có thể phát hiện ra khối lượng ẩn bằng cách gửi vào những lệnh sẽ thực sự giao dịch đối ứng với khối lượng đó. Như vậy, các nhà giao dịch chỉ có thể biết về khối lượng ẩn sau khi họ đã cam kết giao dịch với nó. 

Các nhà giao dịch cũng thường chỉ định một **khối lượng hiển thị (*display size*)** cụ thể cho các lệnh của mình. Khi đó, các nhà môi giới và sở giao dịch chỉ phơi bày phần khối lượng được phép hiển thị của các lệnh này. Bất kỳ phần khối lượng bổ sung nào vượt quá mức đó đều được ẩn giấu khỏi công chúng nhưng vẫn có thể được khớp nếu có một lệnh đối ứng đủ lớn đi vào thị trường. Các nhà giao dịch đôi khi gọi những lệnh như vậy là **lệnh tảng băng trôi (*iceberg orders*)** bởi vì phần lớn khối lượng của lệnh đều bị chìm/ẩn đi. Các nhà giao dịch chỉ định khối lượng hiển thị khi họ không muốn để lộ toàn bộ quy mô thực sự của mình, nhưng vẫn muốn các nhà giao dịch khác biết rằng đang có người sẵn lòng giao dịch tại mức giá được hiển thị đó. Các nhà giao dịch ở phía đối ứng muốn giao dịch thêm khối lượng tại mức giá đó chỉ có thể khám phá ra phần khối lượng ẩn nếu họ giao dịch hết phần khối lượng đang hiển thị; tại thời điểm đó, nhà môi giới hoặc sở giao dịch sẽ tiếp tục hiển thị phần khối lượng còn lại tối đa bằng mức khối lượng hiển thị đã quy định. Họ cũng có thể khám phá ra phần khối lượng ẩn bằng cách gửi vào các lệnh lớn để giao dịch trực tiếp với phần khối lượng đó. 

##### **VÍ DỤ 22 (EXAMPLE 22)** 

### **Lệnh Thị trường so với Lệnh Giới hạn và Lệnh Ẩn so với Lệnh Hiển thị (Market versus Limit and Hidden versus Displayed Orders)** 

Bạn là nhà giao dịch bên mua (*buy-side trader*) làm việc cho một nhà quản lý đầu tư rất thông minh. Nhà quản lý này đã thuê một công ty vệ tinh thương mại chụp ảnh định kỳ các bãi đậu xe nơi các đại lý xe hơi mới lưu giữ hàng tồn kho của họ. Quỹ cũng đã thuê một số nhân viên bán thời gian để đếm số lượng xe ô tô trên các bãi đậu đó. Với thông tin này cùng một số phân tích kinh tế lượng, nhà quản lý có thể dự đoán các thông báo doanh số bán xe hơi mới hàng tuần chính xác hơn hầu hết các chuyên gia phân tích khác. Nhà quản lý thường kiếm được mức lợi nhuận một phần tư phần trăm ($0,25\%$) mỗi tuần nhờ chiến lược này. Mỗi tuần một lần, vào một ngày trước khi các thông báo doanh số được công bố, nhà quản lý giao cho bạn các lệnh lớn để mua hoặc bán cổ phiếu của các nhà sản xuất ô tô dựa trên những hiểu biết sâu sắc của ông ấy về doanh số của các đại lý. Bạn nên cân nhắc những vấn đề chính nào khi quyết định xem nên: 

1. sử dụng lệnh thị trường hay lệnh giới hạn để thực hiện các lệnh của ông ấy? 

#### **Giải pháp (Solution):** 

Thông tin của nhà quản lý rất dễ bị "hết hạn/mất giá trị" nhanh chóng (*perishable*). Nếu các lệnh của ông ấy không được khớp trước khi doanh số hàng tuần được báo cáo ra công chúng, nhà quản lý sẽ mất đi cơ hội kiếm lời từ thông tin đó vì giá cả sẽ ngay lập tức điều chỉnh theo tin tức mới. Do đó, nhà quản lý cần phải khớp được các lệnh một cách nhanh chóng. Cân nhắc này gợi ý rằng các lệnh nên được gửi dưới dạng lệnh thị 


<!-- PDF Page 59 -->

trường (*market orders*). Nếu được gửi dưới dạng lệnh giới hạn, các lệnh có thể không được thực hiện và công ty sẽ đánh mất cơ hội kiếm lời. 

Tuy nhiên, các lệnh thị trường có quy mô lớn có thể rất đắt đỏ khi thực hiện, đặc biệt nếu có ít người sẵn lòng giao dịch khối lượng đáng kể ở phía đối ứng của thị trường. Bởi vì chi phí giao dịch (nhượng bộ giá) có thể dễ dàng vượt quá mức tỷ suất sinh lợi kỳ vọng $0,25\%$, bạn nên gửi các lệnh giới hạn (*limit orders*) nhằm giới hạn mức giá thực hiện mà bạn sẵn lòng chấp nhận. Thà không giao dịch được còn tốt hơn là giao dịch ở những mức giá gây thua lỗ. 

##### 2. hiển thị công khai các lệnh hay ẩn chúng đi? 

#### **Giải pháp (Solution):** 

Các lệnh lớn của bạn có thể dễ dàng làm dịch chuyển giá thị trường theo hướng bất lợi nếu nhiều người biết về chúng, và thậm chí còn bất lợi hơn nữa nếu những người khác biết rằng bạn đang giao dịch thay mặt cho một nhà giao dịch dựa trên thông tin rất thành công. Do đó, bạn nên cân nhắc việc gửi các lệnh ẩn (*hidden orders*). Nhược điểm của các lệnh ẩn là chúng không cho mọi người biết rằng họ có thể giao dịch ở phía đối ứng nếu họ muốn. 

## **CHỈ THỊ HIỆU LỰC VÀ CHỈ THỊ BÙ TRỪ THANH TOÁN (VALIDITY INSTRUCTIONS AND CLEARING INSTRUCTIONS)** 

# **<mark>13</mark>** 

so sánh các chỉ thị thực hiện, chỉ thị hiệu lực và chỉ thị bù trừ thanh toán 

**Chỉ thị hiệu lực (*Validity instructions*)** cho biết khi nào một lệnh có thể được thực hiện. Chỉ thị hiệu lực phổ biến nhất là **lệnh trong ngày (*day order*)**. Lệnh trong ngày chỉ có giá trị trong ngày giao dịch mà nó được gửi đi. Nếu nó chưa được khớp tính đến thời điểm đóng cửa phiên giao dịch trong ngày, lệnh đó sẽ hết hạn mà không được thực hiện (*expires unfilled*). 

**Lệnh có hiệu lực cho đến khi bị hủy (*Good-till-cancelled orders* – GTC)** có ý nghĩa đúng như tên gọi của nó. Trên thực tế, hầu hết các nhà môi giới đều giới hạn khoảng thời gian tối đa mà họ sẽ quản lý một lệnh để đảm bảo rằng họ không khớp những lệnh mà khách hàng của mình đã lãng quên từ lâu. Các nhà môi giới như vậy có thể giới hạn thời hạn các lệnh GTC của họ trong vòng vài tháng. 

**Lệnh thực hiện ngay hoặc hủy (*Immediate or cancel orders* – IOC)** chỉ có hiệu lực ngay tại thời điểm nhà môi giới hoặc sở giao dịch tiếp nhận lệnh. Nếu chúng không thể được khớp ngay một phần hoặc toàn bộ, phần không khớp sẽ bị hủy bỏ ngay lập tức. Trên một số thị trường, những lệnh này còn được biết đến với tên gọi là **lệnh khớp toàn bộ hoặc hủy ngay (*fill or kill orders* – FOK)** *(Lưu ý: Trong chương trình CFA này, tác giả dùng hai thuật ngữ IOC và Fill or Kill gần như tương đương nhau)*. Khi tìm kiếm nguồn thanh khoản ẩn, các hệ thống giao dịch thuật toán điện tử (*electronic algorithmic trading systems*) thường gửi hàng ngàn lệnh IOC như vậy cho mỗi một lệnh mà chúng thực sự khớp được. 

**Lệnh có hiệu lực lúc đóng cửa (*Good-on-close orders*)** chỉ có thể được khớp vào thời điểm đóng cửa phiên giao dịch. Những lệnh này thường là các lệnh thị trường, vì vậy các nhà giao dịch gọi chúng là **lệnh thị trường lúc đóng cửa (*market-on-close orders* – MOC)**. Các nhà giao dịch thường sử dụng các lệnh lúc đóng cửa khi họ muốn giao dịch tại chính mức giá sẽ được công bố là giá đóng cửa của ngày hôm đó. Các quỹ tương hỗ thường thích giao dịch tại những mức giá như vậy bởi vì họ định giá danh mục đầu tư (tính NAV) theo giá đóng cửa. Nhiều nhà giao dịch cũng sử dụng **lệnh có hiệu lực lúc mở cửa (*good-on-open orders*)**. 

### **Lệnh Dừng (Stop Orders)** 

**Lệnh dừng (*Stop order*)** là một lệnh mà trong đó nhà giao dịch đã chỉ định một điều kiện **giá dừng (*stop price condition*)**. Lệnh dừng không được phép khớp cho đến khi điều kiện giá dừng đã được thỏa mãn. Đối với một lệnh bán dừng (*stop-sell order*), điều kiện giá dừng sẽ treo/tạm hoãn việc thực hiện lệnh cho đến khi có một giao dịch trên thị trường diễn ra tại mức giá bằng hoặc thấp hơn mức giá dừng. Sau khi giao dịch đó xảy ra, điều kiện dừng được thỏa mãn và lệnh bắt đầu có hiệu lực để được thực hiện, tuân theo tất cả các chỉ thị thực hiện khác đính kèm với 


<!-- PDF Page 60 -->

nó. Nếu sau đó giá thị trường tăng trở lại lên trên mức giá dừng của lệnh bán trước khi lệnh kịp khớp, lệnh đó vẫn tiếp tục có hiệu lực. Tương tự, một lệnh mua có điều kiện dừng (*stop-buy order*) chỉ bắt đầu có hiệu lực sau khi giá thị trường tăng lên đạt hoặc vượt qua mức giá dừng đã chỉ định. 

Các nhà giao dịch thường gọi các lệnh dừng là **lệnh dừng lỗ / lệnh cắt lỗ (*stop-loss orders*)** bởi vì nhiều nhà giao dịch sử dụng chúng với hy vọng chặn đứng các khoản thua lỗ trên những vị thế mà họ đã thiết lập. Ví dụ, một nhà giao dịch đã mua cổ phiếu ở giá 40 có thể muốn bán cổ phiếu đó đi nếu giá giảm xuống dưới 30. Trong trường hợp đó, nhà giao dịch có thể gửi một lệnh “GTC, dừng ở 30, bán thị trường” (*“GTC, stop 30, market sell”*). Nếu giá giảm xuống mức bằng hoặc dưới 30, lệnh thị trường bắt đầu có hiệu lực và nó sẽ được thực hiện ngay lập tức tại mức giá tốt nhất hiện có trên thị trường vào lúc đó. Mức giá đó có thể thấp hơn đáng kể so với 30 nếu thị trường đang lao dốc nhanh chóng. Do đó, lệnh cắt lỗ không đảm bảo chắc chắn việc chặn đứng khoản lỗ ngay tại đúng mức giá dừng. Nếu những người bán tiềm năng lo lắng về việc phải giao dịch ở một mức giá quá thấp, họ có thể đính kèm chỉ thị dừng vào các lệnh giới hạn thay vì lệnh thị trường. Trong ví dụ này, nếu nhà giao dịch không sẵn lòng bán dưới mức giá 25, nhà giao dịch sẽ gửi một lệnh “GTC, dừng ở 30, bán giới hạn ở 25” (*“GTC, stop 30, limit 25 sell”*). 

Nếu một nhà giao dịch muốn có sự đảm bảo chắc chắn rằng anh ta có thể bán được ở đúng mức giá 30, nhà giao dịch đó sẽ mua một hợp đồng quyền chọn bán (*put option contract*) có giá thực hiện tại 30. Giá mua của quyền chọn sẽ bao gồm một khoản phí quyền chọn (*premium*) cho sự bảo hiểm mà nhà giao dịch đang mua. Hợp đồng quyền chọn có thể được xem như những lệnh giới hạn mà việc thực hiện được bảo đảm chắc chắn tại mức giá thực hiện (*strike price*). Tương tự, một nhà giao dịch có thể sử dụng một lệnh mua dừng (*stop-buy order*) hoặc một quyền chọn mua (*call option*) để giới hạn mức lỗ đối với một vị thế bán khống (*short position*). 

Một nhà quản lý danh mục đầu tư có thể sử dụng lệnh mua dừng (*stop-buy order*) khi nhà quản lý tin rằng một chứng khoán đang bị định giá thấp nhưng lại không sẵn lòng giao dịch nếu chưa có sự xác nhận từ thị trường (*market confirmation*). Ví dụ, giả sử rằng một cổ phiếu hiện đang giao dịch ở mức giá 50 Nhân dân tệ (RMB) và một nhà quản lý tin rằng nó xứng đáng có giá trị là 100 RMB. Hơn nữa, nhà quản lý tin rằng cổ phiếu đó sẽ có khả năng cao hơn nhiều đạt tới giá trị 100 RMB nếu các nhà giao dịch khác sẵn lòng mua nó ở mức giá trên 65 RMB. Để tận dụng tốt nhất thông tin này, nhà quản lý sẽ cân nhắc việc phát ra một lệnh “GTC, dừng ở 65 RMB, mua giới hạn ở 100 RMB” (*“GTC, stop 65 RMB, limit 100 RMB buy”*). Tuy nhiên, lưu ý rằng nếu nhà quản lý dựa dẫm quá nhiều vào biến động thị trường khi đưa ra quyết định giao dịch này, anh ta có thể vi phạm Chuẩn mực Đạo đức Nghề nghiệp CFA V.A.2 (*CFA Standard of Professional Conduct V.A.2*), vốn yêu cầu mọi hành động đầu tư phải có cơ sở hợp lý và đầy đủ được hỗ trợ bởi nghiên cứu và điều tra thích hợp. 

Bởi vì các lệnh bán dừng trở nên có hiệu lực khi giá đang giảm và các lệnh mua dừng trở nên có hiệu lực khi giá đang tăng, các nhà giao dịch sử dụng lệnh dừng sẽ góp phần thúc đẩy **đà quán tính của thị trường (*market momentum*)** khi các lệnh bán của họ đẩy giá sụt giảm sâu hơn nữa và các lệnh mua của họ đẩy giá tăng cao hơn nữa. Do đó, mức giá thực hiện đạt được đối với các lệnh dừng thường khá tệ. 

##### **VÍ DỤ 23 (EXAMPLE 23)** 

### **Chỉ thị Giới hạn và Chỉ thị Dừng (Limit and Stop Instructions)** 

1. Chỉ thị giới hạn (*limit instructions*) và chỉ thị dừng (*stop instructions*) khác nhau ở những điểm nào? 

### **Giải pháp (Solution):** 

Mặc dù cả chỉ thị giới hạn và chỉ thị dừng đều quy định các mức giá, nhưng vai trò mà các mức giá này nắm giữ trong việc thu xếp một giao dịch là hoàn toàn khác nhau. Một mức giá giới hạn (*limit price*) đặt ra một giới hạn về việc những mức giá giao dịch nào sẽ được nhà giao dịch chấp nhận. Một người mua sẽ chỉ chấp nhận các mức giá bằng hoặc thấp hơn giá giới hạn, trong khi một người bán sẽ chỉ chấp nhận các mức giá bằng hoặc cao hơn giá giới hạn. 

Ngược lại, một mức giá dừng (*stop price*) cho biết khi nào một lệnh bắt đầu có thể được khớp (tức là một chỉ thị hiệu lực). Một lệnh mua dừng chỉ có thể được khớp một khi thị trường đã giao dịch tại một mức giá bằng hoặc cao hơn giá dừng. Một lệnh bán dừng chỉ có thể được khớp một khi thị trường đã giao dịch tại một mức giá bằng hoặc thấp hơn giá dừng. 

Cả hai chỉ thị lệnh này đều có thể làm trì hoãn hoặc ngăn cản việc thực hiện một lệnh. Một lệnh mua giới hạn sẽ không thực hiện cho đến khi có ai đó sẵn lòng bán ở mức giá bằng hoặc dưới giá giới hạn. Tương tự, một lệnh bán giới hạn sẽ không thực hiện cho đến khi có ai đó 


<!-- PDF Page 61 -->

sẵn lòng mua ở mức giá bằng hoặc trên giá bán giới hạn. Ngược lại, một lệnh mua dừng sẽ không thực hiện nếu giá thị trường không bao giờ tăng lên chạm tới mức giá dừng. Tương tự, một lệnh bán dừng sẽ không thực hiện nếu giá thị trường không bao giờ giảm xuống chạm tới mức giá dừng. 

### **Chỉ thị Bù trừ Thanh toán (Clearing Instructions)** 

**Chỉ thị bù trừ thanh toán (*Clearing instructions*)** cho các nhà môi giới và sở giao dịch biết cách thức thu xếp việc thanh toán cuối cùng cho các giao dịch. Các nhà giao dịch nhìn chung không đính kèm những chỉ thị này vào từng lệnh riêng lẻ — thay vào đó họ cung cấp chúng dưới dạng các chỉ thị mặc định thường trực (*standing instructions*). Những chỉ thị này cho biết tổ chức nào chịu trách nhiệm bù trừ và thanh toán giao dịch. Đối với các giao dịch cá nhân/bán lẻ, tổ chức đó chính là nhà môi giới của khách hàng. Đối với các giao dịch định chế, tổ chức đó có thể là một ngân hàng giám hộ (*custodian*) hoặc một nhà môi giới khác. Khi một khách hàng sử dụng một nhà môi giới này để thu xếp thực hiện giao dịch và một nhà môi giới khác để thanh toán giao dịch, các nhà giao dịch nói rằng nhà môi giới thứ nhất chuyển giao/nhường lại giao dịch (*gives up the trade*) cho nhà môi giới kia, bên thường được gọi là **nhà môi giới chính (*prime broker*)**. Các nhà giao dịch định chế cung cấp các chỉ thị này để họ có thể nhận được các dịch vụ thực hiện lệnh chuyên biệt từ nhiều nhà môi giới khác nhau trong khi vẫn duy trì một tài khoản tổng duy nhất cho các dịch vụ lưu ký giám hộ và các dịch vụ môi giới chính khác, chẳng hạn như vay ký quỹ. 

Một chỉ thị bù trừ thanh toán quan trọng bắt buộc phải xuất hiện trên các lệnh bán chứng khoán là chỉ báo cho biết giao dịch bán đó là **bán từ vị thế mua đang sở hữu (*long sale*)** hay là **bán khống (*short sale*)**. Trong cả hai trường hợp, nhà môi giới đại diện cho lệnh bán phải đảm bảo rằng nhà giao dịch có thể giao chứng khoán để thanh toán. Đối với một giao dịch bán thông thường (*long sale*), nhà môi giới phải xác nhận rằng các chứng khoán đang nắm giữ có sẵn để chuyển giao. Đối với một giao dịch bán khống (*short sale*), nhà môi giới phải đứng ra vay chứng khoán thay mặt cho khách hàng hoặc phải xác nhận rằng khách hàng có thể vay được chứng khoán đó. 

## **THỊ TRƯỜNG CHỨNG KHOÁN SƠ CẤP (PRIMARY SECURITY MARKETS)** 

# **<mark>14</mark>** 

định nghĩa thị trường sơ cấp và thị trường thứ cấp cũng như giải thích cách thức thị trường thứ cấp hỗ trợ thị trường sơ cấp 

Khi các tổ chức phát hành lần đầu tiên bán chứng khoán của họ cho các nhà đầu tư, những người hành nghề nói rằng các giao dịch đó diễn ra trên **thị trường sơ cấp (*primary markets*)**. Một tổ chức phát hành thực hiện **chào bán cổ phiếu lần đầu ra công chúng (*initial public offering* – IPO)** — đôi khi được gọi là một đợt phân phối (*placing*) — đối với một đợt phát hành chứng khoán khi tổ chức đó bán chứng khoán đó ra công chúng lần đầu tiên. Một chứng khoán đã lưu hành (*seasoned security*) là một chứng khoán mà tổ chức phát hành đã phát hành trước đó rồi. Nếu tổ chức phát hành muốn bán thêm các đơn vị của một chứng khoán đã được phát hành trước đó, tổ chức đó sẽ thực hiện một **đợt chào bán bổ sung (*seasoned offering*** – đôi khi được gọi là **chào bán thứ cấp – *secondary offering***). Cả hai loại hình chào bán này đều diễn ra trên **thị trường sơ cấp (*primary market*)**, nơi các tổ chức phát hành bán chứng khoán của mình cho các nhà đầu tư. Sau đó, nếu các nhà đầu tư giao dịch mua bán lại các chứng khoán này với nhau, họ giao dịch trên **thị trường thứ cấp (*secondary markets*)**. Phần này thảo luận về các thị trường sơ cấp và các thủ tục mà các tổ chức phát hành sử dụng để chào bán chứng khoán của mình ra công chúng. 

### **Chào bán Ra Công chúng (Public Offerings)** 

Các tập đoàn nhìn chung ký hợp đồng với một ngân hàng đầu tư (*investment bank*) để giúp họ bán chứng khoán ra công chúng. Sau đó, ngân hàng đầu tư sẽ tập hợp một danh sách những người đăng ký mua (*subscribers*) sẽ mua chứng khoán đó. Các chuyên gia ngân hàng đầu tư gọi quá trình này là **dựng sổ (*book building*)**. Tại Luân Đôn, tổ chức dựng sổ (*book builder*) được gọi là *book runner*. Ngân hàng cố gắng xây dựng một cuốn sổ tập hợp các lệnh đặt mua mà họ có thể bán chứng khoán trong đợt chào bán cho những lệnh đó. Các ngân hàng đầu tư thường hỗ trợ quá trình dựng sổ của mình bằng cách cung cấp thông tin đầu tư và ý kiến đánh giá về tổ chức phát hành cho khách hàng của họ và cho 


<!-- PDF Page 62 -->

công chúng. Trước đợt chào bán, tổ chức phát hành nhìn chung phải thực hiện việc công bố thông tin rất chi tiết về hoạt động kinh doanh của mình, về những rủi ro vốn có trong hoạt động đó, và về các mục đích sử dụng đối với nguồn vốn mới huy động được. 

Khi thời gian là yếu tố cấp bách, các tổ chức phát hành tại Châu Âu có thể phát hành chứng khoán thông qua hình thức **dựng sổ cấp tốc (*accelerated book build*)**, trong đó ngân hàng đầu tư thu xếp đợt chào bán chỉ trong vòng một hoặc hai ngày. Những đợt bán như vậy thường diễn ra ở mức giá có chiết khấu (*discounted prices*). 

Đợt chào bán cổ phiếu phổ thông lần đầu ra công chúng (IPO) của một công ty bao gồm các cổ phiếu mới được phát hành để công ty bán ra. Nó cũng có thể bao gồm cả những cổ phiếu mà các nhà sáng lập (*founders*) và các nhà đầu tư giai đoạn đầu khác trong công ty muốn bán ra. Đợt chào bán lần đầu ra công chúng cung cấp cho những nhà đầu tư ban đầu này một phương tiện để hiện thực hóa/thanh lý khoản đầu tư của họ (*liquidating their investments*). 

Trong một **đợt chào bán có bảo lãnh phát hành (*underwritten offering*)** — loại hình chào bán phổ biến nhất — ngân hàng đầu tư bảo lãnh việc bán toàn bộ đợt phát hành tại một mức giá chào bán (*offering price*) mà ngân hàng đàm phán với tổ chức phát hành. Nếu đợt phát hành không được đăng ký mua hết (*undersubscribed*), ngân hàng sẽ phải tự bỏ tiền mua lại bất kỳ số chứng khoán nào mà họ không thể bán được tại mức giá chào bán đó. Trong trường hợp IPO, tổ chức bảo lãnh phát hành (*underwriter*) thường cũng hứa sẽ tạo lập thị trường (*make a market*) cho chứng khoán đó trong khoảng một tháng để đảm bảo rằng thị trường thứ cấp sẽ có tính thanh khoản và để cung cấp sự hỗ trợ giá (*price support*) nếu cần thiết. Đối với các đợt phát hành quy mô lớn, một tổ hợp bảo lãnh (*syndicate*) gồm nhiều ngân hàng đầu tư và các công ty môi giới–tự doanh sẽ giúp **tổ chức bảo lãnh phát hành chính (*lead underwriter*)** dựng sổ. Tổ chức phát hành thường trả một khoản **phí bảo lãnh phát hành (*underwriting fee*)** khoảng 7 phần trăm cho các dịch vụ đa dạng này. Phí bảo lãnh phát hành là một chi phí phân phối (*placement cost*) của đợt chào bán. 

Trong một **đợt chào bán theo hình thức nỗ lực tối đa (*best effort offering*)**, ngân hàng đầu tư chỉ đóng vai trò là người môi giới (*broker*). Nếu đợt chào bán không được đăng ký mua hết, tổ chức phát hành sẽ không bán được nhiều chứng khoán như họ hy vọng. 

Đối với cả hai loại hình chào bán trên, tổ chức phát hành và ngân hàng thường cùng nhau ấn định mức giá chào bán sau một cuộc đàm phán. Nếu họ ấn định một mức giá mà người mua cho là quá cao, đợt chào bán sẽ bị đăng ký mua thiếu (*undersubscribed*), và họ sẽ thất bại trong việc bán hết toàn bộ đợt phát hành. Nếu họ ấn định mức giá quá thấp, đợt chào bán sẽ được đăng ký mua vượt mức (*oversubscribed*); trong trường hợp đó, các chứng khoán thường được phân bổ cho các khách hàng ưu tiên hoặc phân bổ theo tỷ lệ đăng ký (*pro-rata basis*). 

(Lưu ý rằng Chuẩn mực Đạo đức Nghề nghiệp CFA III.B — Đối xử Công bằng / *Fair Dealing* — yêu cầu việc phân bổ phải được dựa trên một chính sách bằng văn bản đã được công bố cho khách hàng và khuyến nghị rằng các chứng khoán nên được chào bán theo tỷ lệ *pro-rata* cho tất cả các khách hàng có mối quan hệ tương đương với công ty môi giới–tự doanh của họ.) 

Các ngân hàng đầu tư có một sự xung đột lợi ích (*conflict of interest*) liên quan đến mức giá chào bán trong các đợt chào bán có bảo lãnh phát hành. Với tư cách là đại lý cho các tổ chức phát hành, nhìn chung họ được kỳ vọng phải lựa chọn mức giá chào bán nào giúp huy động được nhiều tiền nhất cho tổ chức phát hành. Nhưng với tư cách là tổ chức bảo lãnh phát hành, họ lại có động lực rất mạnh mẽ để chọn một mức giá thấp. Nếu giá thấp, các ngân hàng có thể phân bổ những cổ phiếu có giá trị cao cho các khách hàng của mình hưởng lợi và qua đó gián tiếp mang lại lợi ích cho chính ngân hàng. Nếu giá quá cao, các tổ chức bảo lãnh phát hành sẽ phải tự ôm mua lại những cổ phiếu bị định giá quá cao trong đợt chào bán và có thể là cả trong tháng tiếp theo nếu họ phải mua đỡ giá trên thị trường thứ cấp, điều này trực tiếp gây tốn kém chi phí cho ngân hàng. Những cân nhắc này có xu hướng làm hạ thấp mức giá chào bán ban đầu, khiến cho giá trên thị trường thứ cấp thường tăng vọt ngay lập tức sau một đợt IPO. Những vấn đề này ít quan trọng hơn trong một đợt chào bán bổ sung (*seasoned offering*) bởi vì hoạt động giao dịch sẵn có trên thị trường thứ cấp giúp xác định mức giá phù hợp cho đợt chào bán. 

Các tổ chức phát hành lần đầu nhìn chung chấp nhận mức giá chào bán thấp hơn bởi vì bản thân họ và nhiều người khác tin rằng một đợt IPO bị ế (*undersubscribed IPO*) sẽ truyền tải thông tin cực kỳ bất lợi ra thị trường về triển vọng của công ty vào đúng thời điểm mà công ty dễ bị tổn thương nhất trước dư luận công chúng về triển vọng của mình. Họ lo sợ rằng một đợt IPO không được đăng ký mua hết sẽ làm cho việc huy động thêm vốn trong các đợt chào bán bổ sung tiếp theo trở nên khó khăn hơn rất nhiều. 


<!-- PDF Page 63 -->

##### **VÍ DỤ 24 (EXAMPLE 24)** 

### **Đợt Chào bán Lần đầu Ra Công chúng (IPO) của Công ty Healthybots (The Healthybots Initial Public Offering)** 

Healthybots là một công ty chăm sóc sức khỏe chuyên điều trị bệnh bằng các giải pháp dựa trên trí tuệ nhân tạo. Healthybots đã huy động được tổng số tiền gộp khoảng 265 triệu bảng Anh (£265 million) thông qua một đợt chào bán lần đầu ra công chúng gồm 103.142.466 cổ phiếu phổ thông ở mức giá £2,57 mỗi cổ phiếu phổ thông. Sau đợt chào bán lần đầu ra công chúng, Healthybots có tổng cộng 213.333.333 cổ phiếu phổ thông đã phát hành và đang lưu hành. 

Công ty Healthybots nhận được tổng số tiền thu gộp (*gross proceeds*) khoảng 34,3 triệu bảng Anh và số tiền thu ròng (*net proceeds*) là 31,8 triệu bảng Anh. Số cổ phiếu phổ thông được bán ra công chúng chiếm khoảng 48 phần trăm tổng số cổ phiếu phổ thông đã phát hành của Healthybots. 

Các cổ phiếu bắt đầu giao dịch lúc 8:00 sáng trên thị trường AIM của Sở Giao dịch Chứng khoán Luân Đôn (LSE), nơi cổ phiếu Healthybots mở cửa ở mức giá £2,74, giao dịch 37 triệu cổ phiếu trong biên độ từ £2,68 đến £2,74, và đóng cửa ở mức giá £2,73. 

1. Có xấp xỉ bao nhiêu cổ phiếu mới đã được phát hành bởi công ty và bao nhiêu cổ phiếu đã được bán ra bởi các nhà sáng lập của công ty? Các nhà sáng lập đã bán đi tỷ lệ bao nhiêu trong tổng số cổ phần nắm giữ của họ tại công ty? 

#### **Giải pháp (Solution):** 

Công ty Healthybots nhận được số tiền thu gộp là 34,3 triệu bảng Anh tại mức giá £2,57 mỗi cổ phiếu, vì vậy công ty đã phát hành mới và bán ra 13.346.304 cổ phiếu ($= £34,3 \text{ triệu}/£2,57 \text{ mỗi cổ phiếu}$). Tổng đợt phân phối là 103.142.466 cổ phiếu, do đó các nhà sáng lập đã bán ra 89.796.162 cổ phiếu ($= 103.142.466 \text{ cổ phiếu} - 13.346.304 \text{ cổ phiếu}$). Bởi vì có xấp xỉ 200 triệu cổ phiếu ($= 213,3 \text{ triệu cổ phiếu} - 13,3 \text{ triệu cổ phiếu}$) đang lưu hành trước đợt phân phối này, nên các nhà sáng lập đã bán đi xấp xỉ 45 phần trăm ($= 90 \text{ triệu cổ phiếu}/200 \text{ triệu cổ phiếu}$) cổ phần của công ty. 

2. Những người đăng ký mua tham gia vào đợt IPO đã kiếm được mức tỷ suất sinh lợi xấp xỉ bao nhiêu ngay trong ngày giao dịch đầu tiên? 

#### **Giải pháp (Solution):** 

Những người đăng ký mua đã mua cổ phiếu với giá £2,57 mỗi cổ phiếu, và nó đóng cửa ở mức giá £2,73. Do đó, tỷ suất sinh lợi trong ngày đầu tiên là:

$$\text{Tỷ suất sinh lợi ngày đầu} = \frac{2,73 - 2,57}{2,57} \times 100 = 6,2\%$$

3. Công ty Healthybots đã trả chi phí phân phối (*placement costs*) xấp xỉ bao nhiêu khi tính theo tỷ lệ phần trăm trên nguồn vốn mới huy động được? 

#### **Giải pháp (Solution):** 

Healthybots thu được số tiền gộp là 34,3 triệu bảng Anh nhưng chỉ huy động được số tiền ròng là 31,8 triệu bảng Anh. Khoản chênh lệch 2,5 triệu bảng Anh chính là tổng chi phí của đợt phân phối mà doanh nghiệp phải chịu, tương đương với 7,9 phần trăm của số tiền thu ròng hay nguồn vốn mới huy động được ($£2,5 \text{ triệu}/£31,8 \text{ triệu}$). 

### **Phát hành Riêng lẻ và Các Giao dịch Thị trường Sơ cấp Khác (Private Placements and Other Primary Market Transactions)** 

Đôi khi các tập đoàn phát hành chứng khoán của mình thông qua các đợt phát hành riêng lẻ. Trong một **đợt phát hành riêng lẻ (*private placement*)**, các tập đoàn bán chứng khoán trực tiếp cho một nhóm nhỏ các nhà đầu tư đủ điều kiện (*qualified investors*), thường là với sự hỗ trợ của một ngân hàng đầu tư. Các nhà đầu tư đủ điều kiện có đủ kiến thức và kinh nghiệm để nhận diện những rủi ro mà họ gánh nhận, và có đủ sự giàu có về tài sản để gánh nhận những rủi ro đó một cách có trách nhiệm. Hầu hết các quốc gia đều cho phép các tập đoàn thực hiện phát hành riêng lẻ mà không cần phải công bố thông tin ra công chúng nhiều như mức độ được yêu cầu đối với các đợt chào bán đại 


<!-- PDF Page 64 -->

chúng. Do đó, phát hành riêng lẻ có thể rẻ hơn (ít tốn kém chi phí phát hành hơn) so với chào bán đại chúng, nhưng những người mua nhìn chung lại đòi hỏi mức tỷ suất sinh lợi cao hơn (tức giá mua thấp hơn) bởi vì sau đó họ không thể tự do giao dịch các chứng khoán này trên một thị trường thứ cấp có tổ chức. 

Đôi khi các tập đoàn bán các đợt phát hành mới của các chứng khoán đã lưu hành trực tiếp ra công chúng theo từng phần nhỏ (*piecemeal basis*) thông qua hình thức đăng ký phát hành từng phần/đăng ký sẵn trên kệ. Trong một **đăng ký phát hành từng phần (*shelf registration*)**, tập đoàn thực hiện tất cả các công bố thông tin đại chúng giống như đối với một đợt chào bán thông thường, nhưng không bán toàn bộ số cổ phiếu đó trong một giao dịch duy nhất. Thay vào đó, tập đoàn bán cổ phiếu trực tiếp vào thị trường thứ cấp dần dần theo thời gian, thường là vào những lúc tập đoàn cần thêm vốn. Hình thức đăng ký phát hành từng phần mang lại cho các tập đoàn sự linh hoạt về mặt thời điểm thực hiện các giao dịch huy động vốn, đồng thời có thể làm giảm bớt áp lực đè nặng làm giảm giá cổ phiếu vốn thường gắn liền với các đợt chào bán bổ sung quy mô lớn. 

Nhiều tập đoàn cũng có thể phát hành cổ phiếu thông qua **các chương trình tái đầu tư cổ tức (*dividend reinvestment plans* – viết tắt là DRPs hoặc DRIPs)** cho phép các cổ đông của họ dùng tiền cổ tức để tái đầu tư vào các cổ phiếu mới phát hành của tập đoàn (cụ thể, các chương trình DRP quy định rằng tập đoàn phát hành cổ phiếu mới cho chương trình chứ không phải mua lại cổ phiếu trên thị trường mở). Đôi khi những chương trình này cũng cho phép các cổ đông hiện hữu và các nhà đầu tư khác mua thêm cổ phiếu ở một mức chiết khấu nhẹ so với giá thị trường hiện hành. 

Cuối cùng, các tập đoàn có thể phát hành cổ phiếu mới thông qua một **đợt chào bán quyền mua cổ phần (*rights offering*)**. Trong một đợt chào bán quyền mua cổ phần, tập đoàn phân phối các quyền (*rights*) được mua cổ phiếu tại một mức giá cố định cho các cổ đông hiện hữu theo tỷ lệ tương ứng với lượng cổ phần họ đang nắm giữ. Bởi vì các quyền mua này không bắt buộc phải thực hiện, nên chúng chính là các quyền chọn (*options*). Tuy nhiên, mức giá thực hiện (*exercise price*) được ấn định thấp hơn giá thị trường hiện hành của cổ phiếu sao cho việc dùng quyền để mua cổ phiếu sẽ mang lại lợi nhuận ngay lập tức. Hệ quả là, các cổ đông sẽ trải qua sự **pha loãng (*dilution*)** trong giá trị của các cổ phiếu hiện hữu mà họ đang nắm giữ. Họ có thể bù đắp khoản tổn thất do pha loãng này bằng cách thực hiện quyền mua của mình hoặc bằng cách bán các quyền mua đó cho những người khác sẽ thực hiện chúng. Các cổ đông nhìn chung không thích các đợt chào bán quyền mua cổ phần bởi vì họ buộc phải bỏ thêm vốn (hoặc phải bán quyền mua đi) để tránh bị thiệt hại do pha loãng giá trị. Các chuyên gia phân tích tài chính nhận thức rằng các chứng khoán này, mặc dù được gọi là quyền mua (*rights*), thực chất chính là các chứng quyền cổ phiếu ngắn hạn (*short-term stock warrants*) và định giá chúng theo đúng bản chất đó. 

Chính phủ quốc gia của các nước có nền tài chính vững mạnh nhìn chung phát hành trái phiếu dài hạn, trái phiếu trung hạn và tín phiếu của mình trong các **phiên đấu thầu công khai (*public auctions*)** được tổ chức bởi một cơ quan chính phủ (thường gắn liền với bộ tài chính). Họ cũng có thể bán chúng trực tiếp cho các nhà tạo lập thị trường (*dealers*). 

Các chính phủ quốc gia nhỏ hơn và có nền tài chính kém vững chắc hơn cùng hầu hết các chính quyền địa phương/khu vực thường ký hợp đồng với các ngân hàng đầu tư để giúp họ bán và phân phối chứng khoán của mình. Tuy nhiên, luật pháp của nhiều chính phủ bắt buộc họ phải đấu thầu chứng khoán của mình. 

##### **VÍ DỤ 25 (EXAMPLE 25)** 

### **Phát hành Riêng lẻ và Phát hành Đại chúng (Private and Public Placements)** 

1. Phát hành riêng lẻ (*private placements*) khác với phát hành đại chúng (*public placements*) ở những điểm nào? 

### **Giải pháp (Solution):** 

Các tổ chức phát hành thực hiện phát hành riêng lẻ cho một số lượng hạn chế các nhà đầu tư mà nhìn chung là những người am hiểu sâu sắc về tài chính và nắm rõ thông tin về rủi ro. Các nhà đầu tư này thường có một mối quan hệ nhất định với tổ chức phát hành. Các tổ chức phát hành thực hiện phát hành đại chúng khi họ bán chứng khoán cho công chúng nói chung. Phát hành đại chúng nhìn chung đòi hỏi việc công bố thông tin tài chính nhiều hơn đáng kể so với phát hành riêng lẻ. 


<!-- PDF Page 65 -->

### **Tầm quan trọng của Thị trường Thứ cấp đối với Thị trường Sơ cấp (Importance of Secondary Markets to Primary Markets)** 

Các tập đoàn và chính phủ có thể huy động tiền trên các thị trường sơ cấp với chi phí thấp hơn khi chứng khoán của họ sẽ được giao dịch trên các thị trường thứ cấp có tính thanh khoản cao. Trong một **thị trường thanh khoản (*liquid market*)**, các nhà giao dịch có thể mua hoặc bán với chi phí giao dịch thấp và mức nhượng bộ giá nhỏ bất cứ khi nào họ muốn giao dịch. Người mua coi trọng tính thanh khoản bởi vì họ có thể cần bán chứng khoán của mình đi để đáp ứng các nhu cầu thanh khoản đột xuất. Do đó, các nhà đầu tư sẽ trả giá cao hơn cho những chứng khoán mà họ có thể dễ dàng bán lại so với những chứng khoán mà họ không thể dễ dàng bán lại. Giá bán chứng khoán cao hơn đồng nghĩa với chi phí sử dụng vốn (*costs of capital*) thấp hơn cho các tổ chức phát hành. 

## **CẤU TRÚC THỊ TRƯỜNG CHỨNG KHOÁN THỨ CẤP VÀ THỊ TRƯỜNG HỢP ĐỒNG (SECONDARY SECURITY MARKET AND CONTRACT MARKET STRUCTURES)** 

# **<mark>15</mark>** 

định nghĩa thị trường sơ cấp và thị trường thứ cấp cũng như giải thích cách thức thị trường thứ cấp hỗ trợ thị trường sơ cấp  

mô tả cách thức các chứng khoán, hợp đồng và tiền tệ được giao dịch trên thị trường định hướng theo báo giá, thị trường định hướng theo lệnh và thị trường qua môi giới 

Giao dịch là kết quả thành công của một quá trình tìm kiếm song phương (*bilateral search*) mà trong đó người mua tìm kiếm người bán và người bán tìm kiếm người mua. Nhiều cấu trúc thị trường đã phát triển nhằm làm giảm chi phí của quá trình tìm kiếm này. Các thị trường có tính thanh khoản cao khi chi phí tìm kiếm một đối tác phù hợp cho giao dịch ở mức thấp. 

Hoạt động giao dịch chứng khoán và hợp đồng diễn ra trong nhiều cấu trúc thị trường khác nhau. Các cấu trúc này khác nhau ở thời điểm các giao dịch có thể được thu xếp, ai là người thu xếp giao dịch, họ thu xếp bằng cách nào, và làm thế nào các nhà giao dịch biết được về các cơ hội giao dịch tiềm năng cũng như các giao dịch đã được thực hiện. Phần này giới thiệu các cấu trúc thị trường khác nhau được sử dụng để giao dịch chứng khoán và hợp đồng. Trước hết chúng ta xem xét các phiên giao dịch (*trading sessions*), tiếp theo là các cơ chế thực hiện lệnh (*execution mechanisms*), và cuối cùng là các hệ thống thông tin thị trường (*market information systems*). 

### **Các Phiên Giao dịch (Trading Sessions)** 

Các thị trường được tổ chức dưới dạng thị trường khớp lệnh định kỳ hoặc thị trường giao dịch liên tục. Trong một **thị trường khớp lệnh định kỳ (*call market*)**, các giao dịch chỉ có thể được thu xếp khi thị trường được triệu tập/gọi khớp (*called*) tại một thời điểm và địa điểm cụ thể. Ngược lại, trong một **thị trường giao dịch liên tục (*continuous trading market*)**, các giao dịch có thể được thu xếp và thực hiện vào bất kỳ thời điểm nào khi thị trường đang mở cửa. 

Người mua có thể dễ dàng tìm thấy người bán và ngược lại trong các thị trường khớp lệnh định kỳ bởi vì tất cả các nhà giao dịch quan tâm đến việc giao dịch (hoặc các lệnh đại diện cho lợi ích của họ) đều có mặt tại cùng một thời điểm và địa điểm. Do đó, các thị trường khớp lệnh định kỳ có tiềm năng đạt tính thanh khoản rất cao vào đúng thời điểm chúng được gọi khớp lệnh. Nhưng chúng lại hoàn toàn không có thanh khoản (*completely illiquid*) trong khoảng thời gian giữa các phiên gọi khớp lệnh. Ngược lại, các nhà giao dịch có thể thu xếp và thực hiện giao dịch của mình vào bất kỳ lúc nào trong các thị trường giao dịch liên tục, nhưng việc thực hiện điều đó có thể gặp khó khăn nếu người mua và người bán (hoặc các lệnh của họ) không cùng có mặt tại một thời điểm. 

Hầu hết các thị trường khớp lệnh định kỳ sử dụng phương thức **đấu giá một mức giá duy nhất (*single price auctions*)** để ghép nối người mua với người bán. Trong các phiên đấu giá này, thị trường xây dựng các sổ lệnh đại diện cho tất cả các lệnh mua và tất cả các lệnh bán. Sau đó, thị trường lựa chọn một mức giá giao dịch chung duy nhất giúp tối đa hóa tổng khối lượng giao dịch (*maximize the total volume of trade*). Các sổ lệnh chính là các biểu cung và biểu cầu, và giao điểm nơi chúng cắt nhau sẽ xác định mức giá giao dịch. 

Các thị trường khớp lệnh định kỳ thường chỉ được tổ chức mỗi ngày một lần, nhưng một số thị trường tổ chức các đợt gọi khớp lệnh định kỳ với tần suất thường xuyên hơn. 


<!-- PDF Page 66 -->

Nhiều thị trường giao dịch liên tục bắt đầu ngày giao dịch của mình bằng một phiên đấu giá khớp lệnh định kỳ (*call market auction*). Trong suốt giai đoạn tiền mở cửa (*pre-opening period*), các nhà giao dịch gửi lệnh của mình vào cho đợt khớp lệnh định kỳ mở cửa. Vào thời điểm mở cửa, bất kỳ giao dịch nào có thể ghép khớp được sẽ được thu xếp thực hiện và sau đó hoạt động giao dịch tiếp tục diễn ra trong phiên giao dịch liên tục. Một số thị trường giao dịch liên tục cũng kết thúc ngày giao dịch của mình bằng một đợt khớp lệnh định kỳ đóng cửa (*closing call*). Trên các thị trường này, những nhà giao dịch chỉ quan tâm đến việc giao dịch trong đợt khớp lệnh định kỳ đóng cửa sẽ gửi các lệnh thị trường lúc đóng cửa (*market-on-close*) hoặc lệnh giới hạn lúc đóng cửa (*limit-on-close*). 

##### **VÍ DỤ 26 (EXAMPLE 26)** 

### **Thị trường Khớp lệnh Định kỳ và Thị trường Giao dịch Liên tục (Call Markets and Continuous Trading Markets)** 

1. Ưu điểm chính của thị trường khớp lệnh định kỳ (*call market*) so với thị trường giao dịch liên tục (*continuous trading market*) là gì? 

#### **Giải pháp (Solution):** 

Bằng cách tập hợp tất cả các nhà giao dịch đến cùng một nơi vào cùng một thời điểm, thị trường khớp lệnh định kỳ giúp người mua dễ dàng tìm thấy người bán hơn và ngược lại. Ngược lại, nếu người mua và người bán (hoặc các lệnh của họ) không có mặt cùng một lúc trên thị trường giao dịch liên tục, họ sẽ không thể giao dịch được với nhau. 

2. Ưu điểm chính của thị trường giao dịch liên tục so với thị trường khớp lệnh định kỳ là gì? 

#### **Giải pháp (Solution):** 

Trong một thị trường giao dịch liên tục, một người mua và một người bán sẵn lòng giao dịch có thể thực hiện giao dịch vào bất kỳ thời điểm nào khi thị trường đang mở cửa. Ngược lại, trong một thị trường khớp lệnh định kỳ, việc giao dịch chỉ có thể diễn ra vào đúng thời điểm thị trường được gọi khớp lệnh. 

### **Các Cơ chế Thực hiện Lệnh (Execution Mechanisms)** 

Ba loại cấu trúc thị trường chính là thị trường định hướng theo báo giá (đôi khi được gọi là thị trường định hướng theo giá hoặc thị trường của các nhà tạo lập thị trường – *price-driven or dealer markets*), thị trường định hướng theo lệnh, và thị trường qua môi giới. Trong **thị trường định hướng theo báo giá (*quote-driven markets*)**, khách hàng giao dịch trực tiếp với các nhà tạo lập thị trường (*dealers*). Trong **thị trường định hướng theo lệnh (*order-driven markets*)**, một hệ thống khớp lệnh được vận hành bởi một sở giao dịch, một nhà môi giới, hoặc một hệ thống giao dịch thay thế (ATS) sử dụng các quy tắc (*rules*) để thu xếp giao dịch dựa trên các lệnh mà các nhà giao dịch gửi vào. Hầu hết các sở giao dịch và các mạng thông tin điện tử (ECNs) đều tổ chức các thị trường định hướng theo lệnh. Trong **thị trường qua môi giới (*brokered markets*)**, các nhà môi giới đứng ra thu xếp giao dịch giữa các khách hàng của họ. Thị trường qua môi giới rất phổ biến đối với các giao dịch của những công cụ độc bản (*unique instruments*), chẳng hạn như các bất động sản, tài sản sở hữu trí tuệ, hoặc các lô chứng khoán quy mô rất lớn (*large blocks of securities*). Nhiều hệ thống giao dịch kết hợp sử dụng nhiều hơn một loại cấu trúc thị trường. 

##### **_Thị trường Định hướng theo Báo giá (Quote-Driven Markets)_** 

Trên phạm vi toàn cầu, hầu hết các hoạt động giao dịch, ngoại trừ giao dịch cổ phiếu, đều diễn ra trên các thị trường định hướng theo báo giá. Hầu như tất cả các trái phiếu và tiền tệ cùng phần lớn các hàng hóa giao ngay đều được giao dịch trên các thị trường định hướng theo báo giá. Các nhà giao dịch gọi chúng là định hướng theo báo giá (hoặc định hướng theo giá hay thị trường *dealer*) bởi vì khách hàng giao dịch tại các mức giá do các *dealers* báo giá. Tùy thuộc vào công cụ được giao dịch, các *dealers* làm việc cho các ngân hàng thương mại, ngân hàng đầu tư, công ty môi giới–tự doanh (*broker–dealers*), hoặc các công ty giao dịch tự doanh (*proprietary trading houses*). 

Các thị trường định hướng theo báo giá cũng thường được gọi là **thị trường phi tập trung / thị trường qua quầy (*over-the-counter markets* – OTC)** bởi vì trước đây các chứng khoán theo đúng nghĩa đen từng được giao dịch qua mặt quầy giao dịch trong văn phòng của các *dealers*. Ngày nay, hầu hết các giao dịch trên thị trường OTC đều được thực hiện qua các mạng lưới truyền thông máy tính độc quyền, qua điện thoại, hoặc đôi khi qua các hệ thống nhắn tin tức thời (*instant messaging systems*). 


<!-- PDF Page 67 -->

##### **_Thị trường Định hướng theo Lệnh (Order-Driven Markets)_** 

Các thị trường định hướng theo lệnh thu xếp giao dịch bằng cách sử dụng các quy tắc để ghép các lệnh mua với các lệnh bán. Các lệnh này có thể được gửi vào bởi các khách hàng hoặc bởi các *dealers*. Hầu như tất cả các sở giao dịch đều sử dụng hệ thống giao dịch định hướng theo lệnh, và mọi hệ thống giao dịch tự động đều là hệ thống định hướng theo lệnh. 

Bởi vì các quy tắc tự động ghép nối người mua với người bán, nên các nhà giao dịch thường giao dịch với những người hoàn toàn xa lạ. Do đó, các thị trường định hướng theo lệnh bắt buộc phải có các thủ tục để đảm bảo rằng người mua và người bán sẽ thực hiện đúng các hợp đồng giao dịch của mình. Nếu không, những nhà giao dịch thiếu trung thực sẽ tham gia vào các hợp đồng mà sau đó họ sẽ chối bỏ không thanh toán nếu sự thay đổi trong điều kiện thị trường làm cho việc thanh toán trở nên bất lợi, thua lỗ. 

Hai bộ quy tắc đặc trưng cho các cơ chế thị trường định hướng theo lệnh là: **Quy tắc khớp lệnh (*order matching rules*)** và **quy tắc định giá giao dịch (*trade pricing rules*)**. Quy tắc khớp lệnh ghép các lệnh mua với các lệnh bán. Quy tắc định giá giao dịch xác định mức giá mà tại đó các giao dịch đã được ghép cặp sẽ diễn ra. 

##### **Quy tắc Khớp lệnh (Order Matching Rules)** 

Các hệ thống giao dịch định hướng theo lệnh ghép nối người mua với người bán bằng cách sử dụng các quy tắc xếp hạng các lệnh mua và các lệnh bán dựa trên mức giá, và thường kèm theo các tiêu chí thứ cấp khác. Sau đó, hệ thống sẽ ghép lệnh mua có thứ hạng cao nhất với lệnh bán có thứ hạng cao nhất. Nếu người mua sẵn lòng trả mức giá ít nhất cao bằng mức giá mà người bán sẵn lòng nhận về, hệ thống sẽ thu xếp một giao dịch cho khối lượng nhỏ hơn giữa khối lượng mua và khối lượng bán (*minimum of the buy and sell quantities*). Phần khối lượng còn lại chưa khớp hết, nếu có, sau đó sẽ được ghép tiếp với lệnh kế tiếp ở phía đối ứng và quá trình này cứ thế tiếp diễn cho đến khi không thể thu xếp thêm bất kỳ giao dịch nào nữa. 

**Hệ thống phân cấp thứ tự ưu tiên lệnh (*Order precedence hierarchy*)** xác định những lệnh nào được quyền thực hiện trước. Quy tắc đầu tiên là **ưu tiên về giá (*price priority*)**: Các lệnh mua có mức giá cao nhất và các lệnh bán có mức giá thấp nhất sẽ được đi trước. Đó chính là những lệnh được định giá quyết liệt nhất. **Các quy tắc ưu tiên thứ cấp (*Secondary precedence rules*)** xác định cách thức xếp hạng các lệnh có cùng mức giá. Hầu hết các hệ thống giao dịch sử dụng **ưu tiên về thời gian (*time precedence*)** để xếp hạng các lệnh có cùng mức giá. Lệnh nào đến hệ thống trước sẽ có quyền ưu tiên hơn so với các lệnh đến sau. Trong các hệ thống giao dịch cho phép các lệnh ẩn và lệnh ẩn một phần, các khối lượng được hiển thị công khai (*displayed quantities*) tại một mức giá nhất định nhìn chung có quyền ưu tiên trước các khối lượng không hiển thị (*undisplayed quantities*). Vì vậy, hệ thống phân cấp thứ tự ưu tiên hoàn chỉnh được quy định lần lượt bởi: **ưu tiên về giá (*price priority*)**, **ưu tiên hiển thị (*display precedence*)** tại một mức giá nhất định, và cuối cùng là **ưu tiên về thời gian (*time precedence*)** giữa tất cả các lệnh có cùng trạng thái hiển thị tại một mức giá nhất định. Những quy tắc này tạo động lực cho các nhà giao dịch cải thiện mức giá đặt lệnh, hiển thị công khai lệnh của mình, và gửi lệnh đến sớm nếu họ muốn giao dịch được nhanh chóng. Những động lực này làm tăng tính thanh khoản của thị trường. 

##### **Quy tắc Định giá Giao dịch (Trade Pricing Rules)** 

Sau khi các lệnh đã được ghép cặp với nhau, hệ thống giao dịch sẽ sử dụng quy tắc định giá giao dịch của mình để xác định mức giá giao dịch thực tế. Ba quy tắc mà các thị trường định hướng theo lệnh khác nhau sử dụng để định giá giao dịch của chúng là quy tắc định giá đồng nhất, quy tắc định giá phân biệt, và quy tắc định giá phái sinh. 

Các thị trường khớp lệnh định kỳ (*call markets*) thường sử dụng **quy tắc định giá đồng nhất (*uniform pricing rule*)**. Theo quy tắc này, tất cả các giao dịch đều được thực hiện tại cùng một mức giá chung duy nhất. Thị trường lựa chọn mức giá nào giúp tối đa hóa tổng khối lượng được giao dịch. 

Các thị trường giao dịch liên tục (*continuous trading markets*) sử dụng **quy tắc định giá phân biệt (*discriminatory pricing rule*)**. Theo quy tắc này, mức giá giới hạn của lệnh hoặc báo giá nào đã đến hệ thống trước — tức **lệnh đang chờ khớp (*standing order*)** — sẽ quyết định mức giá giao dịch. Quy tắc này cho phép một nhà giao dịch có lệnh lớn mới đi vào thị trường phân biệt đối xử giữa các lệnh giới hạn đang chờ khớp bằng cách khớp các lệnh được định giá quyết liệt nhất trước tại mức giá giới hạn của chúng, rồi sau đó mới khớp tiếp đến các lệnh được định giá kém quyết liệt hơn tại mức giá giới hạn kém thuận lợi hơn (xét dưới góc nhìn của nhà giao dịch mới đến). Nếu các hệ thống giao dịch không sử dụng quy tắc định giá này, các nhà giao dịch lớn sẽ tự mình chia nhỏ lệnh của họ ra thành nhiều phần để tự thực hiện việc phân biệt giá. 


<!-- PDF Page 68 -->

##### **VÍ DỤ 27 (EXAMPLE 27)** 

### **Khớp một Lệnh Lớn trên Thị trường Giao dịch Liên tục (Filling a Large Order in a Continuous Trading Market)** 

1. Trước khi có một lệnh lớn đi vào thị trường, Sở Giao dịch Chứng khoán Tokyo đang có các lệnh giới hạn chờ khớp sau đây trên sổ lệnh của mình: 

|**Người mua (*Buyer*)**|**Khối lượng mua (*Bid Size*)**|**Giá giới hạn (*Limit Price* – ¥)**|**Khối lượng bán (*Offer Size*)**|**Người bán (*Seller*)**|
|---|---|---|---|---|
|Takumi|15|100,1|||
|Hiroto|8|100,2|||
|Shou|10|100,3|||
|||100,4|4|Hina|
|||100,5|6|Sakura|
|||100,6|12|Miku|



Tsubasa gửi một lệnh trong ngày (*day order*) để mua 15 hợp đồng, giá giới hạn là ¥100,5. Anh ấy sẽ giao dịch với những ai, mức giá giao dịch trung bình của anh ấy là bao nhiêu, và sổ lệnh giới hạn sẽ trông như thế nào sau đó? 

### **Giải pháp (Solution):** 

Lệnh mua của Tsubasa trước tiên sẽ được khớp với lệnh bán được định giá quyết liệt nhất (giá chào bán thấp nhất), đó là lệnh của Hina bán 4 hợp đồng. Một giao dịch diễn ra tại mức giá ¥100,4 cho 4 hợp đồng; lệnh của Hina được khớp hết hoàn toàn, và Tsubasa vẫn còn lại 11 hợp đồng cần mua thêm. 

Lệnh bán được định giá quyết liệt nhất tiếp theo là lệnh của Sakura bán 6 hợp đồng. Một giao dịch thứ hai diễn ra tại mức giá ¥100,5 cho 6 hợp đồng; lệnh của Sakura được khớp hết hoàn toàn, và Tsubasa vẫn còn lại 5 hợp đồng chưa khớp. Lệnh bán được định giá quyết liệt nhất tiếp theo là lệnh của Miku tại mức giá ¥100,6. Tuy nhiên, không thể thực hiện thêm giao dịch nào nữa bởi vì mức giá bán giới hạn của cô ấy (¥100,6) cao hơn mức giá mua giới hạn của Tsubasa (¥100,5). Mức giá giao dịch trung bình của Tsubasa là:

$$\text{Giá giao dịch trung bình} = \frac{4 \times ¥100,4 + 6 \times ¥100,5}{4 + 6} = ¥100,46$$

Bởi vì Tsubasa đã phát ra một lệnh trong ngày (*day order*), phần còn lại chưa khớp của lệnh (5 hợp đồng) được đưa vào nằm chờ trên sổ lệnh ở phía bên mua tại mức giá ¥100,5. Khi đó, các lệnh sau đây đang nằm trên sổ lệnh: 

|**Người mua (*Buyer*)**|**Khối lượng mua (*Bid Size*)**|**Giá giới hạn (*Limit Price* – ¥)**|**Khối lượng bán (*Offer Size*)**|**Người bán (*Seller*)**|
|---|---|---|---|---|
|Takumi|15|100,1|||
|Hiroto|8|100,2|||
|Shou|10|100,3|||
|||100,4|||
|Tsubasa|5|100,5|||
|||100,6|12|Miku|



Nếu Tsubasa phát ra một lệnh thực hiện ngay hoặc hủy (*immediate-or-cancel order* – IOC), thì 5 hợp đồng còn lại đó sẽ bị hủy bỏ ngay lập tức. 

Các mạng lưới khớp lệnh chéo sử dụng quy tắc định giá phái sinh. **Mạng lưới khớp lệnh chéo (*Crossing networks*)** là các hệ thống giao dịch ghép nối những người mua và người bán sẵn lòng giao dịch tại các mức giá được lấy từ các thị trường khác. Hầu hết các hệ thống này khớp chéo các giao dịch của họ tại **điểm giữa (*midpoint*)** của báo giá chào mua tốt nhất (*best bid*) và chào bán tốt nhất (*best ask*) được công bố bởi sở giao dịch chính nơi chứng khoán đó giao dịch. 


<!-- PDF Page 69 -->

Quy tắc định giá này được gọi là **quy tắc định giá phái sinh (*derivative pricing rule*)** bởi vì mức giá được bắt nguồn (phái sinh) từ một thị trường khác. Cụ thể, mức giá này không phụ thuộc vào các lệnh được gửi vào mạng lưới khớp lệnh chéo. Một số mạng lưới khớp lệnh chéo được tổ chức dưới dạng thị trường khớp lệnh định kỳ (*call markets*) và một số khác dưới dạng thị trường giao dịch liên tục. Thị trường khớp lệnh chéo quan trọng nhất là hệ thống giao dịch cổ phiếu POSIT. 

##### **_Thị trường Qua Môi giới (Brokered Markets)_** 

Cơ chế thực hiện thứ ba là **thị trường qua môi giới (*brokered market*)**, trong đó các nhà môi giới đứng ra thu xếp giao dịch giữa các khách hàng của mình. Các nhà môi giới tổ chức thị trường cho những công cụ mà việc tìm kiếm một người mua hoặc một người bán sẵn lòng giao dịch là rất khó khăn bởi vì các công cụ đó có tính độc bản (*unique*) và do đó chỉ thu hút sự quan tâm của một số lượng hạn chế các cá nhân hoặc định chế. Những công cụ này nhìn chung cũng ít khi được giao dịch và rất tốn kém nếu phải nắm giữ trong hàng tồn kho. Ví dụ về các công cụ như vậy bao gồm các lô cổ phiếu quy mô cực lớn (*very large blocks of stock*), các bất động sản, các kiệt tác nghệ thuật hội họa, tài sản sở hữu trí tuệ, các công ty đang hoạt động, giấy phép kinh doanh rượu, và giấy phép hành nghề taxi (*taxi medallions*). Bởi vì các nhà tạo lập thị trường (*dealers*) nhìn chung không thể hoặc không sẵn lòng nắm giữ những tài sản này trong kho của mình, nên họ sẽ không tạo lập thị trường cho chúng. Việc tổ chức các thị trường định hướng theo lệnh cho những công cụ này cũng không hợp lý bởi vì sẽ có quá ít nhà giao dịch gửi lệnh vào đó. 

Các nhà môi giới thành công trên những thị trường này cố gắng quen biết tất cả mọi người có thể sẵn lòng giao dịch ngay bây giờ hoặc trong tương lai. Họ dành phần lớn thời gian của mình trên điện thoại và trong các cuộc gặp gỡ để xây dựng mạng lưới quan hệ của mình. 

##### **VÍ DỤ 28 (EXAMPLE 28)** 

### **Thị trường Định hướng theo Báo giá, Định hướng theo Lệnh và Thị trường Qua Môi giới (Quote-Driven, Order-Driven, and Brokered Markets)** 

1. Những ưu điểm chính của thị trường định hướng theo báo giá, thị trường định hướng theo lệnh, và thị trường qua môi giới là gì? 

### **Giải pháp (Solution):** 

Trong một thị trường định hướng theo báo giá (*quote-driven market*), các nhà tạo lập thị trường (*dealers*) nhìn chung luôn có mặt sẵn sàng để cung cấp thanh khoản. Trong một thị trường định hướng theo lệnh (*order-driven market*), các nhà giao dịch có thể tự cung cấp thanh khoản cho nhau. Trong một thị trường qua môi giới (*brokered market*), các nhà môi giới giúp tìm kiếm những nhà giao dịch sẵn lòng giao dịch khi các *dealers* không sẵn lòng tạo lập thị trường và khi các nhà giao dịch không sẵn lòng đăng công khai các lệnh của mình. 

### **Các Hệ thống Thông tin Thị trường (Market Information Systems)** 

Các thị trường khác nhau về loại hình và khối lượng dữ liệu mà chúng phổ biến ra công chúng. Các nhà giao dịch nói rằng một thị trường có **tính minh bạch trước giao dịch (*pre-trade transparent*)** nếu thị trường đó công bố dữ liệu theo thời gian thực (*real-time data*) về các báo giá (*quotes*) và các lệnh đang chờ (*orders*). Các thị trường có **tính minh bạch sau giao dịch (*post-trade transparent*)** nếu thị trường đó công bố mức giá và khối lượng giao dịch ngay sau khi các giao dịch vừa diễn ra. 

Các nhà giao dịch bên mua (*buy-side traders*) đánh giá cao tính minh bạch bởi vì nó cho phép họ quản lý tốt hơn hoạt động giao dịch của mình, nắm bắt được giá trị thị trường, và ước tính được chi phí giao dịch dự kiến cũng như thực tế của họ. Ngược lại, các nhà tạo lập thị trường (*dealers*) lại ưa thích giao dịch trong các **thị trường thiếu minh bạch / thị trường mờ đục (*opaque markets*)** bởi vì, với tư cách là những người giao dịch thường xuyên, họ có lợi thế thông tin vượt trội so với những người biết ít hơn họ. Chênh lệch giá chào mua–chào bán (*bid–ask spreads*) có xu hướng rộng hơn và chi phí giao dịch có xu hướng cao hơn trong các thị trường thiếu minh bạch bởi vì việc tìm kiếm mức giá tốt nhất hiện có là khó khăn hơn đối với các nhà giao dịch trong những thị trường như vậy.
