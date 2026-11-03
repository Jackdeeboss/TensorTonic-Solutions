import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """

    if len(y_pred) != len(y_true):
        return {"wrong value"}
        
    n = len(y_pred)
    SSE = float(0)
    
    for i in range(n):
        SSE += (y_pred[i] - y_true[i])**2

    MSE = SSE / n

    return MSE