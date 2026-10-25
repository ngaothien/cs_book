# Volume 1: Quantitative Methods
## Learning Module 6 Simulation Methods
### Part 2/2: Practice Problems (PDF Pages 199–200)

---

<!-- PDF Page 199 -->

# **~~PRACTICE PROBLEMS~~** 

**1.** The weekly closing prices of Mordice Corporation shares are as follows: 

**Exhibit 1: Mordice Corporation Shares** 

|**Date**|**Closing Price (euros)**|
|---|---|
|1 August|112|
|8 August|160|
|15 August|120|



The continuously compounded return of Mordice Corporation shares for the period August 1 to August 15 is _closest_ to: 

**A.** 6.90 percent. 

   - **B.** 7.14 percent. 

   - **C.** 8.95 percent. 

**2.** In contrast to normal distributions, lognormal distributions: 

   - **A.** are skewed to the left. 

   - **B.** have outcomes that cannot be negative. 

   - **C.** are more suitable for describing asset returns than asset prices. 

**3.** The lognormal distribution is a more accurate model for the distribution of stock prices than the normal distribution because stock prices are: 

   - **A.** symmetrical. 

   - **B.** unbounded. 

   - **C.** non-negative. 

**4.** Analysts performing bootstrap: 

   - **A.** seek to create statistical inferences of population parameters from a single sample. 

   - **B.** repeatedly draw samples of the same size, with replacement, from the original population. 

   - **C.** must specify probability distributions for key risk factors that drive the underlying random variables. 


<!-- PDF Page 200 -->

# **~~SOLUTIONS~~** 

1. A is correct. The continuously compounded return of an asset over a period is equal to the natural log of the asset’s price change during the period. In this case, ln(120/112) = 6.90%. 

Note that the continuously compounded return from period 0 to period T is the sum of the incremental one-period continuously compounded returns, which in this case are weekly returns. Specifically: 

Week 1 return: ln(160/112) = 35.67%. 

Week 2 return: ln(120/160) = –28.77%. 

Continuously compounded return = 35.67% + –28.77% = 6.90%. 

2. B is correct. By definition, lognormal random variables cannot have negative values (bounded below by 0) and have distributions that are skewed to the right. 

3. C is correct. A lognormal distributed variable has a lower bound of zero. The lognormal distribution is also right skewed, which is a useful property in describing asset prices. 

4. A is correct. Bootstrapping through random sampling generates the observed variable from a random sampling with unknown population parameters. The analyst does not know the true population distribution, but through sampling can infer the population parameters from the randomly generated sample. B is incorrect because, when performing bootstrap, the analyst repeatedly draws samples from the original sample and not population, where each individual resample has the same size as the original sample and each item drawn is replaced for the next draw. C is incorrect because, when performing bootstrap, analysts simply use the observed empirical distribution of the underlying variables. In a Monte Carlo simulation, in contrast, the analyst would specify probability distributions for key risk factors that drive the underlying variables. 

