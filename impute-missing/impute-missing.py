import numpy as np

def impute_missing(X, strategy="mean"):
    X = np.array(X, dtype=float, copy=True)

    # Check if input is 1D
    is_1d = X.ndim == 1

    if is_1d:
        X = X.reshape(-1, 1)

    # Calculate mean or median of each column
    if strategy == "mean":
        values = np.nanmean(X, axis=0)
    elif strategy == "median":
        values = np.nanmedian(X, axis=0)
    else:
        raise ValueError("Invalid strategy")

    # Replace NaN statistics (entirely missing columns) with 0
    values = np.nan_to_num(values, nan=0.0)

    # Find missing values and replace them
    rows, cols = np.where(np.isnan(X))
    X[rows, cols] = values[cols]

    if is_1d:
        return X.ravel()

    return X