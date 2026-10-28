import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    if len(x) == len(y):
        length = len(x)
        sum = float(0)
        for i in range(length):
            sum += x[i] * y[i]

        return sum
    pass