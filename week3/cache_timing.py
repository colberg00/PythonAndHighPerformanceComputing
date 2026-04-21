import numpy as np
import timeit

SIZE = 100

mat = np.random.rand(SIZE, SIZE)

# Measure column access
column_time = timeit.timeit(
    lambda: 2 * mat[:, 0],
    number=1000
)

# Measure row access
row_time = timeit.timeit(
    lambda: 2 * mat[0, :],
    number=1000
)

print(f"Column access time (1000 reps): {column_time:.6f} seconds")
print(f"Row access time (1000 reps): {row_time:.6f} seconds")
print(f"Ratio (column/row): {column_time/row_time:.2f}x")
