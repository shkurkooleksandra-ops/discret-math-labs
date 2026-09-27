import numpy as np

matrix = np.array([
    [3, 8, 0],
    [7, 1, 5],
    [3, 6, 4]
])

# Найбільші елементи кожного стовпця
max_columns = np.max(matrix, axis=0)

# Найменші елементи кожного стовпця
min_columns = np.min(matrix, axis=0)

# Найбільші елементи кожного рядка
max_rows = np.max(matrix, axis=1)

# Найменші елементи кожного рядка
min_rows = np.min(matrix, axis=1)

print("Найбільші елементи стовпців:", max_columns)
print("Найменші елементи стовпців:", min_columns)
print("Найбільші елементи рядків:", max_rows)
print("Найменші елементи рядків:", min_rows)