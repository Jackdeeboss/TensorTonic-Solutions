import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    def norm(x):
        squared_sum = float(0)
        for i in range(len(x)):
            squared_sum += (x[i])**2
        l2_norm = squared_sum**0.5
        return l2_norm

    def dot(a, b):
        sum = float(0)
        for i in range(len(a)):
            sum += (a[i] * b[i])
        return sum

    if (norm(a) == 0 or norm(b) == 0):
        return float(0)
    else:
        cosine = dot(a,b) / (norm(a) * norm(b))

    return cosine
    pass