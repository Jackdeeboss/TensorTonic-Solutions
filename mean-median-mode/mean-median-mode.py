from collections import Counter
import numpy as np
import math

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """

    sum = float(0)
    for i in range(len(x)):
        sum += x[i]
    mean = sum/len(x)

    x = sorted(x)
    n = len(x)
    if n % 2 == 0:
        median = (x[n // 2 - 1] + x[n // 2]) / 2
    else:
        median = x[n // 2]
    median = float(median)

    freq = {}
    for e in x:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1
    largest_freq = 0
    mode = None
    for key in sorted(freq):  # Sort keys in ascending order
        value = freq[key]
        if value > largest_freq:
            largest_freq = value
            mode = key
    mode = float(mode)
    
    return {'mean': mean, 'median': median, 'mode': mode}
    
    pass