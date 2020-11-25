import numpy as np
import scipy.optimize as opt


def garch_log_likelihood(params, data):
    """ 
    Use Negative Normal log-likelihood as the loss function to minimize
    using BFGS (scipy.opt). 
    
    Assume zero mean
    inputs:
    -------
        params (list): 
            omega (float): initial guess for alpha_0
            alpha (float): initial guesses for alpha values (length p)
            beta (float): initial guesses for beta values (length q)
            
        data (array): The input log-return process r_t
    """
    t_len = np.size(data, 0)
    omega = params[0]
    alpha = params[1]
    beta = params[2]
    var = np.zeros(t_len + 1)
    var[0] = np.var(data)
    loglikelihood = 0
    
    # evaluate the GARCH(p,q) process
    for t in range(1, t_len):
        var[t] = (omega + alpha * data[t-1]**2 + beta * var[t-1])
    
    loglikelihood = -0.5 * (np.log(2*np.pi) + np.log(var) + data**2  / var)
    loglikelihood = np.sum(loglikelihood)
    
    return loglikelihood
    

    
    
    