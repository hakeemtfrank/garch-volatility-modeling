# ARCH/GARCH Implementation

ARMA models are used to model the conditional mean of a process when the conditional variance is constant. Autoregressive conditionally heteroscedastic __(ARCH)__ models were introduced to model changes in a process' volatility. 

Let <img src="https://render.githubusercontent.com/render/math?math=x_t"> be the __value of an asset__ and <img src="https://render.githubusercontent.com/render/math?math=r_t"> be the __return of the asset__. Then

<center>
<img src="https://latex.codecogs.com/gif.latex?r_t%20%3D%20%5Cfrac%7Bx_t%20-%20x_%7Bt-1%7D%7D%7Bx_%7Bt-1%7D%7D">
</center>

If <img src="https://render.githubusercontent.com/render/math?math=r_{t \in T}"> is small in magnitude:

<center>
<img src="https://latex.codecogs.com/gif.latex?r_t%20%5Capprox%20%5Cnabla%20%5Clog%28x_t%29">
</center>



## ARCH(p) 

In an ARCH model, $r_t$ is modeled as __white noise__ <img src="https://render.githubusercontent.com/render/math?math=\epsilon_t"> with a __conditional variance__ <img src="https://render.githubusercontent.com/render/math?math=\sigma^2_t"> that depends on the __previous return__ <img src="https://render.githubusercontent.com/render/math?math=r_{t - j}">, <img src="https://render.githubusercontent.com/render/math?math=\forall j \in [1, p]">. 


<center>
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Baligned%7D%20r_t%20%26%3D%20%5Csigma_t%20%5Cepsilon_t%5C%5C%20%5Csigma_t%5E2%20%26%3D%20%5Calpha_0%20&plus;%20%5Csum_%7Bi%3D1%7D%5Ep%20%5Calpha_i%20r%5E2_%7Bt-i%7D%20%5Cend%7Baligned%7D">
</center>


## GARCH(p,q)

The __generalized ARCH__ (GARCH) model incorporates the effect of past variances <img src="https://render.githubusercontent.com/render/math?math=\sigma^2_{t-j}">, <img src="https://render.githubusercontent.com/render/math?math=\forall j \in [1,q]">.

<center>
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Baligned%7D%20r_t%20%26%3D%20%5Csigma_t%20%5Cepsilon_t%5C%5C%20%5Csigma%5E2_t%20%26%3D%20%5Calpha_0%20&plus;%20%5Csum_%7Bj%3D1%7D%5Ep%20%5Calpha_j%20r%5E2_%7Bt-j%7D%20&plus;%20%5Csum_%7Bj%3D1%7D%5Eq%20%5Cbeta_j%5Csigma%5E2%20_%7Bt-j%7D%20%5Cend%7Baligned%7D">
</center>