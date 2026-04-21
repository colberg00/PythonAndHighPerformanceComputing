import sys
import numpy as np
import zarr
import multiprocessing


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 100


def compute_chunk(args):
    store_path, N, C, row_start, col_start = args
    z = zarr.open(store_path, mode='r+')
    x_values = np.linspace(-2, 2, N)
    y_values = np.linspace(-2, 2, N)
    row_end = min(row_start + C, N)
    col_end = min(col_start + C, N)
    block = np.empty((row_end - row_start, col_end - col_start), dtype='int32')
    for i, ri in enumerate(range(row_start, row_end)):
        for j, ci in enumerate(range(col_start, col_end)):
            block[i, j] = mandelbrot_escape_time(complex(x_values[ci], y_values[ri]))
    z[row_start:row_end, col_start:col_end] = block


if __name__ == '__main__':
    N = int(sys.argv[1])
    C = int(sys.argv[2])
    num_proc = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    store_path = sys.argv[4] if len(sys.argv) > 4 else 'mandelbrot.zarr'

    z = zarr.open(store_path, mode='w', shape=(N, N), chunks=(C, C), dtype='int32')

    chunk_args = [
        (store_path, N, C, r, c)
        for r in range(0, N, C)
        for c in range(0, N, C)
    ]

    with multiprocessing.Pool(num_proc) as pool:
        pool.map(compute_chunk, chunk_args)
