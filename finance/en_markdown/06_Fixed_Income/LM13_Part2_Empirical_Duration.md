# Volume 6: Fixed Income
## Learning Module 13 Curve-Based and Empirical Fixed-Income Risk Measures
### Part 2/2: Empirical Duration (PDF Pages 347–354)

---

<!-- PDF Page 347 -->

|**Maturity**|**1 year**|**5 years**|**10 years**|**20 years**|**30 years**|
|---|---|---|---|---|---|
|Expected|+100 bps|+150 bps|+200 bps|+250 bps|+300 bps|
|change||||||



##### Relevant details on the two bonds are as follows: 

||**Tenor**|**Key Rate Duration**|
|---|---|---|
|Bond A|5 years|2.702|
|Bond B|10 years|3.953|



1. Based on the information above, identify which bond will have a greater percentage change in its price due to the benchmark par curve shift. **Solution** Bond B. For Bond A, ∆ _PV_ / _PV_ = –2.702 × 0.015 = –4.05%. For Bond B, ∆ _PV_ / _PV_ = –3.953 × 0.020 = –7.91%. 

2. If the values in the table above on the non-parallel yield curve shifts were forecasts and your portfolio contains equal positions in the two bonds, which of the following would be the best course of action? 

   - **A.** Sell Bond A. **B.** Sell Bond B. **C.** Sell both Bond A and Bond B. 

   - **Solution** C is correct. Sell both Bonds A and B, since both are expected to see price declines. 

3. Explain why key rate durations might be useful for a portfolio manager even though key rate duration values of the bonds in a portfolio sum to the portfolio duration. 

##### **Solution** 

- Knowing the portfolio duration and overall movement of the benchmark yield curve can provide a quick estimate of gains or losses; however, by using key rate durations, a portfolio manager can over- or underweight specific tenors to maximize risk-adjusted return. 

# **EMPIRICAL DURATION** **<mark>5</mark>** 

describe the difference between empirical duration and analytical duration 

The approaches taken so far to estimate duration and convexity statistics using mathematical formulas is often referred to as **analytical duration** ; the measures we have covered are summarized in Exhibit 6. Importantly, estimates of the impact of benchmark yield changes on bond prices using analytical duration implicitly assume that 


<!-- PDF Page 348 -->

government bond yields and spreads are independent variables and are uncorrelated. Analytical duration offers a reasonable approximation of the price–yield relationship in many situations. 

**Exhibit 6: Curve-Based and Empirical Duration Measures** 

|**Measure**|**Definition**|**Interpretation**|
|---|---|---|
|Approximate<br>Modified<br>Duration|Estimates the slope of the line tan-<br>gent to a bond’s price–yield curve|Yield-based method to estimate<br>modified duration|
|Effective<br>Duration|Sensitivity of a bond’s price to a<br>change in a benchmark yield curve|Curve-based method to estimate<br>modified duration for complex<br>bonds with uncertain cash flows|
|Key Rate|Measures bond sensitivity to a<br>benchmark yield change for a spe-<br>cific maturity|l<br>Partial duration statistic that gauges<br>a bond’s sensitivity to non-parallel<br>benchmark yield curve changes|
|Empirical|i<br>Measure using historical data in<br>statistical models and incorporat-<br>ing factors affecting bond prices<br>to determine the price–yield<br>relationship|Statistical estimate that accounts<br>for correlation between yield<br>spreads and benchmark<br>yield-to-maturity changes under<br>different economic scenarios|



However, in practice, there is another important type of duration: Fixed-income professionals often use historical data in statistical models that incorporate various factors affecting bond prices to calculate **empirical duration** estimates (see Exhibit 6). These estimates are calculated over time and in different interest rate environments to inform the fixed-income portfolio decision-making process. 

For instance, during crises, investors typically sell risky assets and purchase government bonds. Such a “flight to quality” can cause government benchmark yields to fall while credit spreads widen. Exhibit 7 depicts the flight to quality during the onset of the COVID-19 pandemic at the end of February 2020. 

##### **Exhibit 7: 10-Year US Treasury Yield vs. US Corporate BB Credit Spread, Q1 2020** 

![](assets/Fixed_Income.pdf-0348-10.png)

<!-- Start of picture text -->
8%<br>7%<br>6%<br>5%<br>4%<br>3%<br>2%<br>1%<br>0%<br>12/31/19 1/14/20 1/28/20 2/11/20 2/25/20 3/10/20 3/24/20<br>10-year treasury BB yield spread<br><!-- End of picture text -->


<!-- PDF Page 349 -->

During such periods, we might expect analytical and empirical duration estimates to differ. For a government bond with little or no credit risk, we would expect analytical and empirical duration to be similar because benchmark yield changes largely drive bond prices. Conversely, credit spreads (and liquidity spreads) would widen because of an increase in expected default risk. Since credit spreads and benchmark yields are negatively correlated under this scenario, wider credit spreads will partially or fully offset the decline in government benchmark yields, resulting in lower empirical duration estimates than analytical duration estimates (in other words, the expected _increase_ in a bond’s price from declining government benchmark yields is offset by a _decrease_ in price from widening credit spreads). Analysts must consider the correlation between benchmark yields and credit spreads when deciding whether to use empirical or analytical duration estimates. 

##### **EXAMPLE 4** 

#### **Viswan Family Office’s Corporate Bond Portfolio— Empirical vs. Analytical Duration** 

In addition to equity holdings, the Viswan Family Office (VFO) manages a government bond portfolio and a corporate bond portfolio. Positions in the government bond portfolio are mainly medium-term US Treasury securities but also include debt of other highly rated developed-market sovereign issuers. About half of the corporate bond portfolio is invested in investment-grade issues, and the other half consists of high-yield issues, with a mix of maturities and a mix of North American, European, and Asian companies. 

Explain why empirical duration is likely to be a more relevant interest rate risk measure for VFO’s corporate bond portfolio than for its government bond portfolio. 

##### **Solution:** 

The government bond portfolio includes debt securities of the US government and other highly rated developed-market sovereign issuers. Since benchmark yields are the primary driver of changes in overall bond yields in this portfolio, the results of analytical duration and empirical duration should be broadly similar. 

The corporate bond portfolio includes a wide variety of debt securities with varying levels of credit quality and liquidity risk and, therefore, different credit and liquidity spreads. 

Correlations between benchmark yield changes and the sizes of the credit and liquidity spreads are negative, particularly during stressed market conditions, such that during such times, lower benchmark yields are more than offset by higher credit and liquidity spreads. So, for the lower-quality corporate bonds, yields increase, which makes their empirical duration significantly lower than their analytical duration. 

Consequently, empirical duration, not analytical duration, is the more accurate interest rate risk measure for the corporate bond portfolio. 

##### **QUESTION SET** 

1. When comparing analytical duration and empirical duration, which of the following statements is correct? 

   - **A.** Empirical duration and convexity are estimated duration and convexity statistics using mathematical formulas. 


<!-- PDF Page 350 -->

- **B.** Analytical duration and convexity are estimated using historical data in non-statistical models that incorporate various factors affecting bond prices. 

- **C.** Neither A nor B 

##### **Solution:** 

C is correct. 

A is incorrect because it is _analytical_ , not empirical, duration and convexity that are measured using mathematical formulas. 

B is incorrect because it is _empirical_ , not analytical, duration and convexity that are estimated using historical data in non-statistical models that incorporate various factors affecting bond prices. 

2. True or false: Empirical duration estimates provide better estimates than the analytical duration estimates for bonds that have credit risk. 

##### **Solution:** 

True. Macroeconomic factors drive government bond yields lower in a market stress scenario, and the flight to safety will cause high-yield bond credit spreads to widen because of an increase in expected default risk. Since credit spreads and benchmark yields are negatively correlated under this scenario, wider credit spreads will partially or fully offset the decline in government benchmark yields. Analytical duration, however, assumes that benchmark yields and spreads are uncorrelated. Empirical duration estimates are a more accurate method of forecasting for bonds with credit risk. 

3. Identify some of the challenges that may be encountered in estimating empirical duration. 

##### **Solution:** 

Empirical duration estimation utilizes historical data based on multiple factors. What factors to use and not use, what weight to give the factors, and how to weight current data versus older data (e.g., the time period to measure duration) are some challenges. 


<!-- PDF Page 351 -->

## **~~PRACTICE PROBLEMS~~** 

### **The following information relates to questions 1-8** 

An investor’s well-diversified portfolio has $200,000 in cash. The investor aims to invest in short-term, one-year Large-Cap Company bonds, prior to using the cash to invest in an upcoming IPO. There are currently two Large-Cap Company bonds on the market to purchase, both with one-year maturities. One of the bonds, Bond A, is a non-callable bond, while Bond B is a callable bond. As a fixed-income analyst, you are asked to conduct an analysis. 

**1.** For the two bonds offered by Large-Cap Company, which duration calculation would be the _most_ appropriate to use to measure interest rate risk? 

   - **A.** Modified duration 

   - **B.** Macaulay duration 

   - **C.** Effective duration 

**2.** For Bond B, as the benchmark yield curve declines, the slope of the line tangent to the bond flattens as the benchmark yield declines and reaches an inflection point, after which the effective convexity becomes: 

   - **A.** positive. 

   - **B.** negative. 

   - **C.** neither positive nor negative. 

**3.** The following information on Bonds A and B was obtained: 

||**Effective**|**Effective**|
|---|---|---|
|**Bond**|**f**<br>**Duration**|**f**<br>**Convexity**|
|A|7.48621|29.35972|
|B|7.23852|–321.75618|



Compare the interest rate risk of Bond A and Bond B. 

   - **A.** Bond A is riskier than Bond B. 

   - **B.** Bond B is riskier than Bond A. 

   - **C.** Bond A and Bond B have approximately the same interest rate risk. 

**4.** For the percentage price change for Bond A, given a 200 bp increase in benchmark yield, what part of the price change is of the most concern? 

   - **A.** Duration 

   - **B.** Convexity 

   - **C.** Not able to determine with given information 


<!-- PDF Page 352 -->

**5.** A colleague asks whether you also considered looking at the key rate durations when comparing the interest rate risks of Bond A and Bond B. Would research into key rate durations for Bond A and Bond B help you make a better decision about the interest rate risk of the two bonds? 

   - **A.** Yes 

   - **B.** No 

   - **C.** Inconclusive 

**6.** The investor’s portfolio is diversified, and the fixed-income component of the portfolio has bonds of various maturities, with a duration of 7.48621. What would happen to the effective duration of the fixed-income component of the investor’s portfolio if Bond A is added to the portfolio? 

   - **A.** It would increase. 

   - **B.** If would decrease. 

   - **C.** It would stay the same. 

**7.** For the two bonds under consideration, would analytical duration estimates or empirical duration estimates be _most_ appropriate in conducting your analysis? 

   - **A.** Analytical duration estimates 

   - **B.** Empirical duration estimates 

   - **C.** Either type of estimate would be appropriate. 

**8.** What impact would a “flight to safety” (i.e., government bond yields falling and credit spreads widening) have on the analytical duration estimate of Bond A? 

   - **A.** Decreased duration 

   - **B.** Increased duration 

   - **C.** No impact 


<!-- PDF Page 353 -->

## **~~SOLUTIONS~~** 

1. C is correct. Since Bond B is callable, it has an embedded option, and effective duration is the most appropriate duration measure. Effective duration also works on bonds without embedded options and would allow the analyst to compare the interest rate risk of the two bonds. 

2. B is correct. Since the bond is callable, after a certain point on the yield curve, the issuer will exercise the call and the owner will not be able to realize additional gains from declines in the benchmark yield curve. 

3. B is correct. Bond B is riskier since the 100 bps upward shift in the yield curve results in a greater percentage price decrease, owing to its negative effective convexity: 

   - %∆ _PV_<sup>_Full_</sup> Bond A ≈ (–7.48621 × 0.0200) + [½ × 29.35972 × (–0.0200)<sup>2</sup> ] = –7.33941%. 

%∆ _PV_<sup>_Full_</sup> Bond B ≈ (–7.23853 × 0.0200) + [½ × –321.75618 × (0.0200)<sup>2</sup> ] = –8.84730%. 

4. A is correct. Typically, the effect of duration is much larger than the effect of convexity. 

%∆ _PV_<sup>_Full_</sup> Bond A, Duration ≈ –7.48621 × 0.0200 = –14.97242%. 

%∆ _PV_<sup>_Full_</sup> Bond A, Convexity Adjustment ≈ ½ × 29.35972 × (–0.0200)<sup>2</sup> = –0.58719%. 

5. B is correct. Since both bonds mature in one year, key rate duration analysis would not give you any additional insight, since both bonds would undergo the same shift in the curve. 

6. C is correct. Bond A has the same effective duration as the portfolio effective duration. 

7. B is correct. Since both Bond A and Bond B are corporate bonds, they have credit risk, and as such, empirical duration would be the most appropriate because benchmark yields and credit spreads may not be positively correlated. 

8. C is correct. There would be no impact on the analytical duration estimate. However, an empirical duration estimate would be impacted. A flight to safety would result in an increase in the bond price due to the falling benchmark yield being offset by widening credit spread. This would lead to a lower empirical duration than analytical duration. 


<!-- PDF Page 354 -->

