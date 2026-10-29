import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    summation = 0
    for i in range(len(x)):
        summation += (x[i]*p[i])
        
    return float(summation)
    pass