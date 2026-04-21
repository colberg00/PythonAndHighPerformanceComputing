import sys
import numpy as np
import multiprocessing


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 100


def compute_rows(args):
    filename, N, row_start, row_end = args
    x_values = np.linspace(-2, 2, N)
    y_values = np.linspace(-2, 2, N)
    arr = np.memmap(filename, dtype='int32', mode='r+', shape=(N, N))
    for i in range(row_start, row_end):
        for j in range(N):
            arr[i, j] = mandelbrot_escape_time(complex(x_values[j], y_values[i]))


if __name__ == '__main__':
    N = int(sys.argv[1])
    num_proc = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    outfile = 'mandelbrot.raw'

    # Create the file
    arr = np.memmap(outfile, dtype='int32', mode='w+', shape=(N, N))
    del arr

    chunk = N // num_proc
    args = [(outfile, N, i * chunk, min((i + 1) * chunk, N))
            for i in range(num_proc)]

    with multiprocessing.Pool(num_proc) as pool:
        pool.map(compute_rows, args)
