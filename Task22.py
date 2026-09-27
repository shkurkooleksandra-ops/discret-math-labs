import numpy as np

a = np.array([float(i) for i in range(1, 101)])

b = np.reshape(a, (10, 10))

print("Одномірний масив a:")
print(a)

print("\nМатриця b:")
print(b)