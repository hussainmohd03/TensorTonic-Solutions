import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    A = np.asarray(A)                         
    n, m = A.shape
    AT = np.empty((m, n), dtype=A.dtype)      

    for i in range(n):
        AT[:, i] = A[i]                       

    return AT