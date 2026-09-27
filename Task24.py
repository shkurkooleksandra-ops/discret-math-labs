import numpy as np

a = np.arange(1.0, 101.0).reshape(1, 100)

print("Початковий розмір:", a.shape)
print(a)

a = a.reshape(100, 1)

print("Новий розмір:", a.shape)
print(a)