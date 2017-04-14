# doseresponse

A minimal dose response class for calculating EC50 values and hill-slopes.

```python
from doseresponse import DoseResponse

# create some example data
concentrations = [10, 3, 1, 0.4, 0.12, 0.04, 0.013, 0.004] * 2
response = [5, 12, 28, 53, 78, 92, 98, 100, 8, 14, 30, 56, 80, 94, 100, 102]

dr = DoseResponse()
dr.fit(concentrations, response)
```

This returns an array of `[hillslope, min, max, EC50]`

```
array([   1.05328595,    2.59972129,  101.31058779,    0.40938031])
```

Which can be accessed through the object

```python
dr.hill_slope

>>> 1.05328595
```
