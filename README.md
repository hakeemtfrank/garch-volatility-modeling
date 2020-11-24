# ARCH/GARCH Implementation

ARMA models are used to model the conditional mean of a process when the conditional variance is constant. Autoregressive conditionally heteroscedastic __(ARCH)__ models were introduced to model changes in a process' volatility. 

Let $x_t$ be the __value of an asset__ and $r_t$ be the __return of the asset__ at time $t$. Then

$$
r_t = \frac{x_t - x_{t-1}}{x_{t-1}}
$$


If $r_{t \in T}$ is small in magnitude:

$$
r_t \approx \nabla \log(x_t)
$$





## ARCH(p) 

In an ARCH model, $r_t$ is modeled as __white noise__ $\epsilon_t$ with a __conditional variance__ $\sigma^2_t$ that depends on the __previous return__ $r_{t-j}$, $\forall j \in [1, p ]$. 

$$
\begin{aligned}
r_t &= \sigma_t \epsilon_t\\
\sigma_t^2 &= \alpha_0 + \sum_{i=1}^p \alpha_i r^2_{t-i}
\end{aligned}
$$



## GARCH(p,q)

The __generalized ARCH__ (GARCH) model incorporates the effect of past variances $\sigma^2_{t-j}, \forall \in [1, q]$.

$$
\begin{aligned}
r_t &= \sigma_t \epsilon_t\\
\sigma^2_t &= \alpha_0 + \sum_{j=1}^p \alpha_j r^2_{t-j} + \sum_{j=1}^q \beta_j\sigma^2
_{t-j}
\end{aligned}
$$

