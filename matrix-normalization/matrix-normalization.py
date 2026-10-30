import numpy as np

def matrix_normalization(matrix: list, axis=None,
                         norm_type: str = "l2") -> np.ndarray:
    X = np.array(matrix, dtype=float)

    if norm_type == "l1":
        order = 1
    elif norm_type == "l2":
        order = 2
    elif norm_type == "max":
        order = np.inf
    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")

    if axis is None:
        denominator = np.linalg.norm(X.ravel(), ord=order)
    else:
        denominator = np.linalg.norm(
            X, ord=order, axis=axis, keepdims=True
        )

    denominator = np.where(denominator == 0, 1, denominator)

    return X / denominator