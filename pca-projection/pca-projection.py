import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X = np.array(X, dtype=float)
    n = len(X)
    
    #vectorised operation for centering mean of columns
    feature_means = np.mean(X, axis=0)
    X_centered = X - feature_means

    #vectorised operation for computing sample covariance matrix
    C = (X_centered.T @ X_centered) / (n - 1)

    #using .eigh() since covariance matrix are symmetric
    eigenvalues, eigenvectors = np.linalg.eigh(C)
    indices = np.argsort(eigenvalues)[::-1]
    top_k_indices = indices[:k]
    W = eigenvectors[:, top_k_indices]
    X_proj = X_centered @ W

    
    return X_proj