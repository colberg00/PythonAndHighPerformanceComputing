import ctypes
import math
import multiprocessing as mp
import sys
from time import perf_counter as time

import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')


def reduce_step(args):
    b, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b] += arr[b + s]


if __name__ == '__main__':
    n_processes = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    chunk = 64

    data = np.load(sys.argv[1])
    n = len(data)
    elemshape = data.shape[1:]

    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    n_steps = math.ceil(math.log2(n))
    s = 1
    for _ in range(n_steps):
        tasks = [(i, s, elemshape)
                 for i in range(0, n, 2 * s)
                 if i + s < n]
        pool.map(reduce_step, tasks, chunksize=chunk)
        s *= 2

    pool.close()
    pool.join()

    arr[0] /= n
    print(time() - t)

    Image.fromarray(
        (255 * arr[0].astype(float)).astype('uint8')
    ).save('mean_face.png')
