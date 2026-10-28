import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    if isinstance(x, np.ndarray):
        x = x.tolist()

    n = len(x)
    mean = np.mean(x)

    total = 0
    for i in range(n):
        total += (x[i] - mean)**2

    var = total / (n - 1)
    std = var**0.5

    return {
        'variance': float(var),
        'standard_deviation': float(std)
    }