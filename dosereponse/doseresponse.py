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


    def _param_4_sigmoid(self, x, b, c, d, e):
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


    def fit(self, dose, response):
        """fit function
        Returns:
        --------
        Array - [hill_slope, min, max, ec50]
        """
        self.dose = dose
        self.response = response
        params, cov = curve_fit(self._param_4_sigmoid, dose, response)
        self.hill_slope = params[0]
        self.ec50 = params[-1]
        return params
