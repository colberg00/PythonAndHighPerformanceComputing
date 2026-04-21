import numpy as np


def standardize_rows(data, mean, std):
    return (data - mean) / std


def outer(x, y):
    return x[:, None] * y


def distmat_1d(x, y):
    return np.abs(x[:, None] - y)
