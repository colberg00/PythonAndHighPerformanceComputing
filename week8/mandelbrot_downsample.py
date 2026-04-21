import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = sys.argv[1]
    N = int(sys.argv[2])
    step = int(sys.argv[3])

    arr = np.memmap(filename, dtype='int32', mode='r', shape=(N, N))
    downsampled = arr[::step, ::step]

    plt.imshow(downsampled, cmap='hot')
    plt.axis('off')
    plt.imsave('mandelbrot_downsampled.png', bbox_inches='tight', pad_inches=0)
