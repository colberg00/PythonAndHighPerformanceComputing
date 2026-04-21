import multiprocessing
import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100


def _compute_chunk(chunk):
    return [mandelbrot_escape_time(c) for c in chunk]


def generate_mandelbrot_set(points, num_processes):
    chunk_size = len(points) // num_processes
    chunks = [points[i:i + chunk_size] for i in range(0, len(points), chunk_size)]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(_compute_chunk, chunks)

    escape_times = np.array([t for chunk in results for t in chunk])
    return escape_times


def generate_mandelbrot_set_chunks(points, num_processes):
    chunk_size = 100  # small fixed size so there are many more chunks than workers
    chunks = [points[i:i + chunk_size] for i in range(0, len(points), chunk_size)]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(_compute_chunk, chunks)

    escape_times = np.array([t for chunk in results for t in chunk])
    return escape_times


def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
    import sys

    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = int(sys.argv[1]) if len(sys.argv) > 1 else 4

    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    mandelbrot_set = generate_mandelbrot_set_chunks(points, num_proc)
    mandelbrot_set = mandelbrot_set.reshape((height, width))
    plot_mandelbrot(mandelbrot_set)
    print('Done')
