# Week 9 - Exercise 1.1 (CPU Matrix Multiplication): cache-efficient loop order

import numpy as np
from numba import jit


@jit(nopython=True)
def matmul(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(A.shape[1]):
            for j in range(B.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C
