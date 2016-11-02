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
        self.min = None
        self.max = None
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
        """
        fit function

        Returns:
        --------
            Array : [hill_slope, min, max, ec50]
        """
        params, cov = curve_fit(self._param_4_sigmoid, dose, response)
        self.dose = dose
        self.response = response
        self.hill_slope = params[0]
        self.min = params[1]
        self.max = [2]
        self.ec50 = params[3]
        self._cov = cov
        return params


    # FIXME fix issues with replicates
    # TODO return an interpolated curve with variable number of points
    # TODO watch out for np.unique or set() sorting values which may not
    #      actually be ordered
    def curve():
        """
        create points to plot a curve from the function

        Parameters:
        -----------
            b : hill-slope
            c : min response
            d : max response
            e : EC50

        Returns:
        --------
            list - [[dose], [response]]
        """
        # check we have the parameters to create a function
        params = [self.hill_slope, self.min, self.max, self.ec50]
        if any(param == None for param in params):
            raise NotImplementedError("No parameters found, have you called fit()?")
        # need to use the dose data for xdata, to predict response
        # need to watch out for replicates, so create a set from concentration
        set_dose = set(self.dose)
        if len(set_dose) < len(self.dose):
            raise RuntimeWarning("Dose replicates found, creating a set of \
                                  single concentrations")
        fitted_response = self._param_4_sigmoid(set_dose, self.hill_slope,
                                                self.min, self.max, self.ec50)
        assert len(set_dose) == len(fitted_response)
        return [set_dose, fitted_response]