import numpy as np

b = np.arange(1.0, 101.0).reshape(10, 10)
one_line_string = np.array2string(
    b.reshape(-1),
    separator=" ",
    max_line_width=10000
)

print(one_line_string)
