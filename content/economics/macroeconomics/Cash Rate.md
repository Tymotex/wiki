---
title: Cash Rate
description: Cash Rate
---

The cash rate, which is set by the [[economics/macroeconomics/Central Bank|RBA]] as part of its [[economics/macroeconomics/Monetary Policy|monetary policy]], is a short-term interest rate charged on the 'overnight' loans between banks.
- To 'tighten' monetary policy means to raise the cash rate to discourage lending and therefore lower production.
- To 'loosen' monetary policy means to lower the cash rate to incentivise lending and therefore boost production.

### Payment Settlement
Suppose Commbank owes Westpac an outstanding $10 million AUD. The payment needs to proceed through accounts held at the RBA, called **Exchange Settlement Accounts (ESA)** which must never have a negative balance. Commbank transfers $10 million from their ESA to Westpac’s ESA. 

If Commbank ever has insufficient funds in their reserve, then it must borrow those funds from another bank which expects full repayment in $<24$ hours (which is where the term ‘overnight’ comes from). When borrowing from other banks' ESAs, the loans are charged an interest rate known as the *cash rate*.

There are 3 interest rates that the RBA defines:
- $i^T$ — the RBA’s target cash rate.
- $i^T-0.25$ — the interest rate RBA pays to banks for their ESAs. The $0.25$ is a typical value, but it can be tweaked.
- $i^T+0.25$ — the interest rate for banks to borrow from other banks’ ESAs.

This creates a 50 basis point ‘channel’ which defines the range the actual cash rate value can be in. *Note*: a 'basis point' is just $\frac{1}{100}$ of $1\%$. 

![[economics/macroeconomics/assets/cash-rate-channel-system.png|500]]

### Open Market Operations
*Open market operations* is the trading of goverment bonds between the central bank and the private sector. The RBA mainly buys bonds from banks to increase their ESA and therefore the [[economics/macroeconomics/Money#Money Supply|money supply]], and sells bonds to banks to decrease their ESA and bring down money supply.

### Supply & Demand for ES Funds
Below is the demand curve for banks' ES funds in the overnight cash market.

![[economics/macroeconomics/assets/ES-funds-demand-curve.png|500]]

Below is the supply curve for ES funds in the overnight cash market.

![[economics/macroeconomics/assets/ES-funds-supply-curve.png|500]]

Supply is affected exogenously by the value of the open market operations the RBA undertakes with banks, and the transfers government make to households (by transferring funds into the bank’s ESA, therefore increasing ES funds).

By undertaking open market operations, the RBA can push the supply curve to intersect with the demand curve as shown above. This is how the RBA sets the *actual* cash rate to be the *target* cash rate that they’ve announced.

### Expectations Hypothesis
The *expectations hypothesis* predicts how short-term interest rates like the cash rate affects the long-term interest rates.

The long-term interest rate, $i^N_0$, is simply the average of the current interest rate (at term 0) and all *expected* future interest rates. This is summarised in the following equation:
$$\colorbox{#FFFFBF}{$i^N_0 = \frac{1}{N}(i^1_0+i^2_1+\ldots+i^N_{N-1})$}$$
where $i^\alpha_\beta$ is the interest rate associated with a loan spanning $\alpha$ total terms starting from at time $\beta$.

Generally, the cash rate can be expected to have a very large effect on the mortgage rate, savings bank account interest rates, exchange rate (currency tends to appreciate when cash rate rises), and so on.

### Policy Rule
A *policy rule*, also called a *monetary policy reaction function*, is a simple approximation of how the cash rate affects macroeconomic variables. The *Taylor rule* is a well-known policy rule, which asserts:
$$
	i_\text{nominal cash rate}=1+1.5\pi+0.5\tilde{Y},
$$
where $\tilde{Y}$ is the output gap. Alternatively, using the *real* cash rate, this would be $r_\text{real cash rate} = 1 + 0.5\pi + 0.5\tilde{Y}$.


