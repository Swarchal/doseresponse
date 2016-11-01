import numpy as np
from scipy.optimize import curve_fit

class DoseResponse():

    """
    Dose Response measurements, fit by 4-parameter sigmoidal curve,
    curve fit optimised by non-linear least squares.
    """
    
    def __init__(self):
        self.dose = None
        self.response = None
        self.hill_slope = None
        self.ec50 = None 

    def __repr__(self):
        pass
   

    def fit(self, dose, response):
        self.dose = dose
        self.response = response
        params, cov = curve_fit(param_4_sigmoid, dose, response)
        self.hill_slope = params[0]
        self.ec50 = params[-1]
        return params

def param_4_sigmoid(x, b, c, d, e):
    """
    4 parameter sigmoidal curve
    Parameters
    ----------
    b : hill-slope
    c : min response
    d : max response
    e : EC50
    """
    return (c+(d-c) / (1 + np.exp(b*(np.log(x)-np.log(e)))))
