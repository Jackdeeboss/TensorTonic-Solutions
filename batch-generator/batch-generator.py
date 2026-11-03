import numpy as np

def batch_generator(X: list, y: list, batch_size: int,
                    seed: int = 42, drop_last: bool = False):

    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    if batch_size <= 0:
        raise ValueError("batch_size must be positive")

    length = len(X)

    indices = np.arange(length)

    rng = np.random.default_rng(seed)
    rng.shuffle(indices)

    X = np.asarray(X)
    y = np.asarray(y)

    for i in range(0, length, batch_size):

        batch_indices = indices[i:i + batch_size]

        if drop_last and len(batch_indices) < batch_size:
            break

        X_batch = X[batch_indices]
        y_batch = y[batch_indices]

        yield X_batch, y_batch