---
title: Aggregate Supply and Demand
description: Aggregate Supply and Demand
---

The [[economics/macroeconomics/Income-Expenditure Model|income-expenditure model]] aims to determine the short-run real GDP. The *aggregate supply and demand model* aims to determine the real GDP in both the short-run and long-run.

### Aggregate Demand (AD)
Recall that the planned aggregate expenditure in a 4-sector economy is given as $PAE = C+I^P+G+X-M$.

One core assumption is that a rise in $r$ will tend to reduce consumption and planned investment. We can assume they are affected in the following way:
- $C=C_{0}+c(Y-T)-\alpha r$, where $\alpha >0$.
- $I^{P}= I_{0}- \beta r$, where $\beta > 0$.

Plugging these in and solving for the equilibrium real GDP, we get:
$$
\begin{align}
	Y_\text{equilibrium}&=PAE=\big[C_{0}+c(Y-T) -\alpha r\big]+ \big[I_{0}- \beta r\big] + G_0 + X_0 -mY \notag \\
	&= \frac{1}{1-c(1-t)+m}\bigg( \big(C_{0}- cT_{0}+ I_{0}+ G_{0}+ X_{0}\big)- r(\alpha + \beta) \bigg). \notag\\
\end{align}
$$

Now we've made $Y_\text{equilibrium}$ a function of $r$, we have a simple model for predicting the effects of [[economics/macroeconomics/Monetary Policy|monetary policy]] on real GDP.

To express $Y_\text{equilibrium}$ as a function of $\pi$, we can assume that the central bank will use the [[economics/macroeconomics/Cash Rate#Simple Policy Rule|simple policy rule]] reaction function which tells them to increase the real interest rate in response to an increase in inflation rate. With this assumption, we can relate the real interest rate with the inflation rate, $r= r_{0}+\gamma\pi$ and express $Y_\text{equilibrium}$ as a function of $\pi$:

$$
\begin{align}
	Y_\text{equilibrium} &= \frac{1}{1-c(1-t)+m}\bigg( \big(C_{0}- cT_{0}+ I_{0}+ G_{0}+ X_{0}\big)- r(\alpha + \beta) \bigg), \notag\\
	&= \frac{1}{1-c(1-t)+m}\bigg( \big(C_{0}- cT_{0}+ I_{0}+ G_{0}+ X_{0}\big)- (r_{0}+\gamma\pi)(\alpha + \beta) \bigg), \notag\\
	\notag\\
	\text{Supposing }k &= \frac{1}{1-c(1-t)+m}, \notag\\
	Y_\text{equilibrium} &= k\big(C_{0}- cT_{0}+ I_{0}+ G_{0}+ X_{0} - r_0(\alpha + \beta)\big)-k\gamma(\alpha +\beta)\pi. \notag\\
	\notag\\
\end{align}
$$
Supposing $A_0 = k\big(C_{0}- cT_{0}+ I_{0}+ G_{0}+ X_{0} - r_0(\alpha + \beta)\big)$, we now have an equation representing the aggregate demand curve:
$$\colorbox{#FFFFBF}{$ Y_\text{equilibrium} = A_0-k\gamma(\alpha +\beta)\pi$},$$
which relates the real GDP to the inflation rate.	
