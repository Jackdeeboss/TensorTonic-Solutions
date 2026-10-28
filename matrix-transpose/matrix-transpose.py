import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    original_rows = len(A)
    original_columns = len(A[0])

    A_np = np.array(A)
    new = np.empty((original_columns, original_rows))
     
    for r in range(original_rows):
        for c in range(original_columns):
            new[c, r] = A_np[r, c]

    return new
    pass
