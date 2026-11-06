import numpy as np

def relu(x) -> np.ndarray:
    x = np.asarray(x)
    return np.maximum(0, x)