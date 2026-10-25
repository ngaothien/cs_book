# Volume 1: Quantitative Methods
## Learning Module 10 Simple Linear Regression
### Part 5/6: Practice Problems (PDF Pages 318–329)

---

<!-- PDF Page 318 -->

# **~~PRACTICE PROBLEMS~~** 

## **The following information relates to questions 1-3** 

An analyst has estimated a model that regresses a company’s return on equity (ROE) against its growth opportunities (GO), defined as the company’s three-year compounded annual growth rate in sales, over 20 years, and produces the following estimated simple linear regression: 

ROEi = 4 + 1.8 GOi + εi. 

Both variables are stated in percentages, so a GO observation of 5 percent is included as 5. 

**1.** The predicted value of the company’s ROE if its GO is 10 percent is closest to: 

   - **A.** 1.8 percent. 

   - **B.** 15.8 percent. 

   - **C.** 22.0 percent. 

**2.** The change in ROE for a change in GO from 5 percent to 6 percent is closest to: 

   - **A.** 1.8 percent. 

   - **B.** 4.0 percent. 

   - **C.** 5.8 percent. 

**3.** The residual in the case of a _GO_ of 8 percent and an observed _ROE_ of 21 percent is closest to: 

   - **A.** −1.8 percent. 

   - **B.** 2.6 percent. 

   - **C.** 12.0 percent. 

**4.** Homoskedasticity is best described as the situation in which the variance of the residuals of a regression is: 

   - **A.** zero. 

   - **B.** normally distributed. 

   - **C.** constant across observations. 


<!-- PDF Page 319 -->

## **The following information relates to questions 5-8** 

An analyst is examining the annual growth of the money supply for a country over the past 30 years. This country experienced a central bank policy shift 15 years ago, which altered the approach to the management of the money supply. The analyst estimated a model using the annual growth rate in the money supply regressed on the variable (SHIFT) that takes on a value of 0 before the policy shift and 1 after. She estimated the values in Exhibit 1: 

**Exhibit 1: SHIFT Estimates** 

||**Coefficients**|**Standard Error**|**_t_-Stat.**|
|---|---|---|---|
|Intercept|5.767264|0.445229|12.95348|
|SHIFT|−5.13912|0.629649|−8.16188|



_Critical t-values, level of significance of 0.05: eOne-sided, left side:_ −1.701 _fOne-sided, right side:_ +1.701 _gTwo-sided:_ ±2.048 

**5.** The variable SHIFT is best described as: 

   - **A.** an indicator variable. 

   - **B.** a dependent variable. 

   - **C.** a continuous variable. 

**6.** The interpretation of the intercept is the mean of the annual growth rate of the money supply: 

   - **A.** before the shift in policy. 

   - **B.** over the entire period. 

   - **C.** after the shift in policy. 

**7.** The interpretation of the slope is the: 

   - **A.** change in the annual growth rate of the money supply per year. 

   - **B.** average annual growth rate of the money supply after the shift in policy. 

   - **C.** difference in the average annual growth rate of the money supply from before to after the shift in policy. 

**8.** Testing whether there is a change in the money supply growth after the shift in policy, using a 0.05 level of significance, we conclude that there is: 

   - **A.** sufficient evidence that the money supply growth changed. 

   - **B.** not enough evidence that the money supply growth is different from zero. 

   - **C.** not enough evidence to indicate that the money supply growth changed. 


<!-- PDF Page 320 -->

## **The following information relates to questions 9-12** 

Kenneth McCoin, CFA, is a challenging interviewer. Last year, he handed each job applicant a sheet of paper with the information in Exhibit 1, and he then asked several questions about regression analysis. Some of McCoin’s questions, along with a sample of the answers he received to each, are given below. McCoin told the applicants that the independent variable is the ratio of net income to sales for restaurants with a market cap of more than $100 million and the dependent variable is the ratio of cash flow from operations to sales for those restaurants. Which of the choices provided is the best answer to each of McCoin’s questions? 

**Exhibit 1: Regression Analysis** 

|**Regression Statistics**||
|---|---|
|_R_<sup>2</sup>|0.7436|
|Standard error|0.0213|
|Observations|24|



![](assets/Quantitative_method.pdf-0320-07.png)

|||**Sum of**|**Mean**|||
|---|---|---|---|---|---|
|**Source**|**df**|**Squares**|**Square**|**_F_**|**_p_-Value**|
|Regression|1|0.029|0.029000|63.81|0|
|Residual|22|0.010|0.000455|||
|Total|23|0.040||||



||**Coefficients**|**Standard**<br>**Error**|**_t_-Statistic**|**_p_-Value**|
|---|---|---|---|---|
|Intercept|0.077|0.007|11.328|0|
|Net income to|0.826|0.103|7.988|0|
|sales (%)|||||



**9.** The coefficient of determination is _closest_ to: 

   - **A.** 0.7436. 

**B.** 0.8261. 

**C.** 0.8623. 

**10.** The correlation between _X_ and _Y_ is _closest_ to: 

   - **A.** −0.7436. 

**B.** 0.7436. 

**C.** 0.8623. 

**11.** If the ratio of net income to sales for a restaurant is 5 percent, the predicted ratio of cash flow from operations (CFO) to sales is _closest_ to: 

   - **A.** −4.054. 


<!-- PDF Page 321 -->

   - **B.** 0.524. 

   - **C.** 4.207. 

**12.** Is the relationship between the ratio of cash flow to operations and the ratio of net income to sales significant at the 0.05 level? 

   - **A.** No, because the _R_<sup>2</sup> is greater than 0.05 

   - **B.** No, because the _p_ -values of the intercept and slope are less than 0.05 

   - **C.** Yes, because the _p_ -values for _F_ and _t_ for the slope coefficient are less than 0.05 

## **The following information relates to questions 13-17** 

Howard Golub, CFA, is preparing to write a research report on Stellar Energy Corp. common stock. One of the world’s largest companies, Stellar is in the business of refining and marketing oil. As part of his analysis, Golub wants to evaluate the sensitivity of the stock’s returns to various economic factors. For example, a client recently asked Golub whether the price of Stellar Energy Corp. stock has tended to rise following increases in retail energy prices. Golub believes the association between the two variables is negative, but he does not know the strength of the association. 

Golub directs his assistant, Jill Batten, to study the relationships between (1) Stellar monthly common stock returns and the previous month’s percentage change in the US Consumer Price Index for Energy (CPIENG) and (2) Stellar monthly common stock returns and the previous month’s percentage change in the US Producer Price Index for Crude Energy Materials (PPICEM). Golub wants Batten to run both a correlation and a linear regression analysis. In response, Batten compiles the summary statistics shown in Exhibit 1 for 248 months. All the data are in decimal form, where 0.01 indicates a 1 percent return. Batten also runs a regression analysis using Stellar monthly returns as the dependent variable and the monthly change in CPIENG as the independent variable. Exhibit 2 displays the results of this regression model. 

### **Exhibit 1: Descriptive Statistics** 

||**Stellar Common**<br>**Stock Monthly**<br>**Return**|**Lagged Mon**<br>**CPIENG**|**thly Change**<br>**PPICEM**|
|---|---|---|---|
|Mean|0.0123|0.0023|0.0042|
|Standard deviation|0.0717|0.0160|0.0534|
|Covariance, Stellar vs. CPIENG|−0.00017|||
|Covariance, Stellar vs. PPICEM|−0.00048|||
|Covariance, CPIENG vs. PPICEM|0.00044|||
|Correlation, Stellar vs. CPIENG|−0.1452|||




<!-- PDF Page 322 -->

### **Exhibit 2: Regression Analysis with CPIENG** 

||**Regression Statistics**||
|---|---|---|
|_R_<sup>2</sup>|0.0211||
|Standard error of the estimate|0.0710||
|Observations|248||
||**Coefficients**<br>**Standard**<br>**Error**|**_t_-Statistic**|
|Intercept|0.0138<br>0.0046|3.0275|
|CPIENG (%)|−0.6486<br>0.2818|−2.3014|



_Critical t-values One-sided, left side:_ −1.651 _One-sided, right side:_ +1.651 _Two-sided:_ ±1.967 

**13.** Which of the following best describes Batten’s regression? 

   - **A.** Time-series regression 

   - **B.** Cross-sectional regression 

   - **C.** Time-series and cross-sectional regression 

**14.** Based on the regression, if the CPIENG _decreases_ by 1.0 percent, the expected return on Stellar common stock during the next period is _closest_ to: 

   - **A.** 0.0073 (0.73 percent). 

   - **B.** 0.0138 (1.38 percent). 

   - **C.** 0.0203 (2.03 percent). 

**15.** Based on Batten’s regression model, the coefficient of determination indicates that: 

   - **A.** Stellar’s returns explain 2.11 percent of the variability in CPIENG. 

   - **B.** Stellar’s returns explain 14.52 percent of the variability in CPIENG. 

   - **C.** changes in CPIENG explain 2.11 percent of the variability in Stellar’s returns. 

**16.** For Batten’s regression model, 0.0710 is the standard deviation of: 

   - **A.** the dependent variable. 

   - **B.** the residuals from the regression. 

   - **C.** the predicted dependent variable from the regression. 

**17.** For the analysis run by Batten, which of the following is an _incorrect_ conclusion from the regression output? 

   - **A.** The estimated intercept from Batten’s regression is statistically different from zero at the 0.05 level of significance. 


<!-- PDF Page 323 -->

- **B.** In the month after the CPIENG declines, Stellar’s common stock is expected to exhibit a positive return. 

- **C.** Viewed in combination, the slope and intercept coefficients from Batten’s regression are not statistically different from zero at the 0.05 level of significance. 

## **The following information relates to questions 18-26** 

Anh Liu is an analyst researching whether a company’s debt burden affects investors’ decision to short the company’s stock. She calculates the short interest ratio (the ratio of short interest to average daily share volume, expressed in days) for 50 companies as of the end of the year and compares this ratio with the companies’ debt ratio (the ratio of total liabilities to total assets, expressed in decimal form). Liu provides a number of statistics in Exhibit 1. She also estimates a simple regression to investigate the effect of the debt ratio on a company’s short interest ratio. The results of this simple regression, including the analysis of variance (ANOVA), are shown in Exhibit 2. 

In addition to estimating a regression equation, Liu graphs the 50 observations using a scatter plot, with the short interest ratio on the vertical axis and the debt ratio on the horizontal axis. 

**Exhibit 1: Summary Statistics** 

|**Statistic**|**Debt Ratio (****_Xi_)**<br>**Short Interest Ratio (****_Yi_)**|
|---|---|
|Sum|19.8550<br>192.3000|
|Sum of squared deviations<br>from the mean|∑ _i_=1<br>_n_<br>  ( _X_ _i_−<sup>_</sup><br>_X_) <sup>2</sup>= 2.2225.<br> ∑ _i_=1<br>_n_<br>  ( _Y_ _i_−<sup>_</sup><br>_Y_) <sup>2</sup>= 412.2042.|
|Sum of cross-products of devi-<br>ations from the mean|∑ _i_=1<br>_n_<br> ( _X_ _i_−<sup>_</sup><br>_X_) ( _Y_ _i_−<sup>_</sup><br>_Y_)= − 9.2430.|



**Exhibit 2: Regression of the Short Interest Ratio on the Debt Ratio** 

|**ANOVA**|**Degrees of Free-**<br>**dom (df)**|**Sum of Squares**|**Mean Square**|
|---|---|---|---|
|Regression|1|38.4404|38.4404|
|Residual|48|373.7638|7.7867|
|Total|49|412.2042||
|**Regression Statistics**||||
|_R_<sup>2</sup>|0.0933|||
|Standard error of estimate|2.7905|||




<!-- PDF Page 324 -->

|**ANOVA**|**Degrees of Free-**<br>**dom (df)**|**Sum of Squares**|**Mean Square**|
|---|---|---|---|
|Observations|50|||
||**Coefficients**|**Standard Error**|**_t_-Statistic**|
|Intercept|5.4975|0.8416|6.5322|
|Debt ratio (%)|−4.1589|1.8718|−2.2219|



_Critical t-values for a 0.05 level of significance: One-sided, left side:_ −1.677 _One-sided, right side:_ +1.677 _Two-sided:_ ±2.011 

Liu is considering three interpretations of these results for her report on the relationship between debt ratios and short interest ratios: 

- Interpretation 1 Companies’ higher debt ratios cause lower short interest ratios. 

- Interpretation 2 Companies’ higher short interest ratios cause higher debt ratios. 

- Interpretation 3 Companies with higher debt ratios tend to have lower short interest ratios. 

She is especially interested in using her estimation results to predict the short interest ratio for MQD Corporation, which has a debt ratio of 0.40. 

**18.** Based on Exhibit 1 and Exhibit 2, if Liu were to graph the 50 observations, the scatter plot summarizing this relation would be _best_ described as: 

   - **A.** horizontal. 

   - **B.** upward sloping. 

   - **C.** downward sloping. 

**19.** Based on Exhibit 1, the sample covariance is _closest to_ : 

   - **A.** −9.2430. 

   - **B.** −0.1886. 

   - **C.** 8.4123. 

**20.** Based on Exhibit 1 and Exhibit 2, the correlation between the debt ratio and the short interest ratio is _closest to_ : 

   - **A.** −0.3054. 

   - **B.** 0.0933. 

   - **C.** 0.3054. 

**21.** Which of the interpretations _best_ describes Liu’s findings? 

   - **A.** Interpretation 1 


<!-- PDF Page 325 -->

   - **B.** Interpretation 2 

   - **C.** Interpretation 3 

**22.** The dependent variable in Liu’s regression analysis is the: 

   - **A.** intercept. 

   - **B.** debt ratio. 

   - **C.** short interest ratio. 

**23.** Based on Exhibit 2, the number of degrees of freedom for the _t_ -test of the slope coefficient in this regression is: 

   - **A.** 48. 

   - **B.** 49. 

   - **C.** 50. 

**24.** Which of the following should Liu conclude from the results shown in Exhibit 2? 

   - **A.** The average short interest ratio is 5.4975. 

   - **B.** The estimated slope coefficient is different from zero at the 0.05 level of significance. 

   - **C.** The debt ratio explains 30.54 percent of the variation in the short interest ratio. 

**25.** Based on Exhibit 2, the short interest ratio expected for MQD Corporation is _closest_ to: 

   - **A.** 3.8339. 

   - **B.** 5.4975. 

   - **C.** 6.2462. 

**26.** Based on Liu’s regression results in Exhibit 2, the _F_ -statistic for testing whether the slope coefficient is equal to zero is _closest_ to: 

   - **A.** −2.2219. 

   - **B.** 3.5036. 

   - **C.** 4.9367. 

## **The following information relates to questions 27-29** 

Doug Abitbol is a portfolio manager for Polyi Investments, a hedge fund that trades in the United States. Abitbol manages the hedge fund with the help of Robert Olabudo, a junior portfolio manager. Abitbol looks at economists’ inflation forecasts and would like to examine the 


<!-- PDF Page 326 -->

relationship between the US Consumer Price Index (US CPI) consensus forecast and the actual US CPI using regression analysis. Olabudo estimates regression coefficients to test whether the consensus forecast is unbiased. If the consensus forecasts are unbiased, the intercept should be 0.0 and the slope will be equal to 1.0. Regression results are presented in Exhibit 1. Additionally, Olabudo calculates the 95 percent prediction interval of the actual CPI using a US CPI consensus forecast of 2.8. 

**Exhibit 1: Regression Output: Estimating US CPI** 

|**Regression Statistics**||||
|---|---|---|---|
|_R_<sup>2</sup>|0.9859|||
|Standard error of estimate|0.0009|||
|Observations|60|||
||**Coefficients**|**Standard Error**|**_t_-Statistic**|
|Intercept|0.0001|0.0002|0.5000|
|US CPI consensus forecast|0.9830|0.0155|63.4194|



_Notes:_ 

**1.** The absolute value of the critical value for the _t_ -statistic is 2.002 at the 5 percent level of significance. 

**2.** The standard deviation of the US CPI consensus forecast is _sx_ = 0.7539. 

**3.** The mean of the US CPI consensus forecast is _X_<sup>_</sup> = 1.3350. 

Finally, Abitbol and Olabudo discuss the forecast and forecast interval: 

   - Observation 1. For a given confidence level, the forecast interval is the same no matter the US CPI consensus forecast. 

   - Observation 2. A larger standard error of the estimate will result in a wider confidence interval. 

**27.** Based on Exhibit 1, Olabudo should: 

   - **A.** conclude that the inflation predictions are unbiased. 

   - **B.** reject the null hypothesis that the slope coefficient equals one. 

   - **C.** reject the null hypothesis that the intercept coefficient equals zero. 

**28.** Based on Exhibit 1, Olabudo should calculate a prediction interval for the actual US CPI _closest_ to: 

   - **A.** 2.7506 to 2.7544. 

   - **B.** 2.7521 to 2.7529. 

   - **C.** 2.7981 to 2.8019. 

**29.** Which of Olabudo’s observations of forecasting is correct? 

   - **A.** Only Observation 1 


<!-- PDF Page 327 -->

- **B.** Only Observation 2 

- **C.** Both Observation 1 and Observations 2 

## **The following information relates to questions 30-34** 

Elena Vasileva recently joined EnergyInvest as a junior portfolio analyst. Vasileva’s supervisor asks her to evaluate a potential investment opportunity in Amtex, a multinational oil and gas corporation based in the United States. Vasileva’s supervisor suggests using regression analysis to examine the relation between Amtex shares and returns on crude oil. 

Vasileva notes the following assumptions of regression analysis: 

- Assumption 1. The error term is uncorrelated across observations. 

- Assumption 2. The variance of the error term is the same for all observations. 

- Assumption 3. The dependent variable is normally distributed. 

Vasileva runs a regression of Amtex share returns on crude oil returns using the monthly data she collected. Selected data used in the regression are presented in Exhibit 1, and selected regression output is presented in Exhibit 2. She uses a 1 percent level of significance in all her tests. 

**Exhibit 1: Selected Data for Crude Oil Returns and Amtex Share Returns** 

||**Oil Return**<br>**(****_Xi_)**|**Amtex Return**<br>**(****_Yi_)**|**Cross-Product**<br> ( _X_ _i_**−**<br>**_**<br>_X_) ( _Y_ _i_**−**<br>**_**<br>_Y_)|**Predicted**<br>**Amtex Return**<br>**(**<sup>ˆ</sup><br>_Yi_**)**|**Regression**<br>**Residual**<br>**(**_Y_ _i_**−**ˆ<br>_Yi_ <sup>**)**</sup>|**Squared**<br>**Residual**<br> ( _Y_ _i_**−**<sup>ˆ</sup><br>_Yi_ )<br>**2**|
|---|---|---|---|---|---|---|
|Month 1|−0.032000|0.033145|−0.000388|0.002011|−0.031134|0.000969|
|⁝|⁝|⁝|⁝|⁝|⁝|⁝|
|Month 36|0.028636|0.062334|0.002663|0.016282|−0.046053|0.002121|
|Sum|||0.085598|||0.071475|
|Average|−0.018056|0.005293|||||



**Exhibit 2: Selected Regression Output, Dependent Variable: Amtex Share Return** 

||**Coefficient**|**Standard Error**|
|---|---|---|
|Intercept|0.0095|0.0078|
|Oil return|0.2354|0.0760|



Critical _t_ -values for a 1 percent level of significance: 

One-sided, left side: −2.441 


<!-- PDF Page 328 -->

One-sided, right side: +2.441 Two-sided: ±2.728 

Vasileva expects the crude oil return next month, Month 37, to be −0.01. She computes the standard error of the forecast to be 0.0469. 

**30.** Which of Vasileva’s assumptions regarding regression analysis is _incorrect_ ? **A.** Assumption 1 **B.** Assumption 2 **C.** Assumption 3 

**31.** Based on Exhibit 1, the standard error of the estimate is _closest_ to: **A.** 0.04456. **B.** 0.04585. **C.** 0.05018. 

**32.** Based on Exhibit 2, Vasileva should reject the null hypothesis that: **A.** the slope is less than or equal to 0.15. 

   - **B.** the intercept is less than or equal to zero. 

**C.** crude oil returns do not explain Amtex share returns. 

**33.** Based on Exhibit 2 and Vasileva’s prediction of the crude oil return for Month 37, the estimate of Amtex share return for Month 37 is _closest_ to: **A.** −0.0024. **B.** 0.0071. **C.** 0.0119. 

**34.** Using information from Exhibit 2, the 99 percent prediction interval for Amtex share return for Month 37 is _best_ described as: **A.** _Y_<sup>ˆ</sup> _f_ ± 0.0053 . **B.** _Y_<sup>ˆ</sup> _f_ ± 0.0469 . **C.** _Y_<sup>ˆ</sup> _f_ ± 0.1279 . 

## **The following information relates to questions 35-38** 

Espey Jones is examining the relation between the net profit margin (NPM) of companies, in percent, and their fixed asset turnover (FATO). He collected a sample of 35 companies for the most recent fiscal year and fit several different functional forms, settling on the following model: 


<!-- PDF Page 329 -->

### ln(NPM _i_ ) = _b_ 0 + _b_ 1  FATO _i_ . 

The results of this estimation are provided in Exhibit 1. 

**Exhibit 1: Results of Regressing NPM on FATO** 

|**Source**|**df**|**Sum of**<br>**Squares**|**Mean**<br>**Square**|**_F_**|**_p_-Value**|
|---|---|---|---|---|---|
|Regression|1|102.9152|102.9152|1,486.7079|0.0000|
|Residual|32|2.2152|0.0692|||
|Total|33|105.1303||||



||**fi**|**Standard**|||
|---|---|---|---|---|
||**Coefficients**|**Error**|**_t_- Statistic**|**_p_-Value**|
|Intercept|0.5987|0.0561|10.6749|0.0000|
|FATO|0.2951|0.0077|38.5579|0.0000|



**35.** The coefficient of determination is _closest_ to: 

   - **A.** 0.0211. 

   - **B.** 0.9789. 

   - **C.** 0.9894. 

**36.** The standard error of the estimate is _closest_ to: 

   - **A.** 0.2631. 

   - **B.** 1.7849. 

   - **C.** 38.5579. 

**37.** At a 0.01 level of significance, Jones should conclude that: 

   - **A.** the mean net profit margin is 0.5987 percent. 

   - **B.** the variation of the fixed asset turnover explains the variation of the natural log of the net profit margin. 

   - **C.** a change in the fixed asset turnover from three to four times is likely to result in a change in the net profit margin of 0.5987 percent. 

**38.** The predicted net profit margin for a company with a fixed asset turnover of 2 times is _closest_ to: 

   - **A.** 1.1889 percent. 

   - **B.** 1.8043 percent. 

   - **C.** 3.2835 percent 

