# Week 9 - Exercise 2.1 (CUDA Vector Addition): add_kernel
# Week 9 - Exercise 2.2 (CUDA Vector Addition job): run via vector_add_job.sh

from time import perf_counter as time
import numpy as np
from numba import cuda


@cuda.jit
def add_kernel(x, y, out):
    i = cuda.grid(1)
    if i < out.shape[0]:
        out[i] = x[i] + y[i]


if __name__ == '__main__':
    n = 1_000_000
    x = np.random.rand(n).astype(np.float32)
    y = np.random.rand(n).astype(np.float32)
    out = np.empty_like(x)

    threadsperblock = 256
    blockspergrid = (n + threadsperblock - 1) // threadsperblock

    # Warm-up run so the kernel is compiled before timing
    add_kernel[blockspergrid, threadsperblock](x, y, out)
    cuda.synchronize()

    rep = 200
    t = time()
    for _ in range(rep):
        add_kernel[blockspergrid, threadsperblock](x, y, out)
    cuda.synchronize()
    print((time() - t) / rep * 1000, 'ms')
