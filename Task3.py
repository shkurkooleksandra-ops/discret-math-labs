# Task 3
import numpy as np

x1 = 13
x2 = 42
y1 = 31
y2 = 75

def abs(x1, x2):
    return np.abs(x1 - x2)


def P(a, b):
    return 2 * (a + b)

def S(a, b):
    return a * b

a = abs(x1, x2)
b = abs(y1, y2)

print("S=" + str(S(a, b)))
print("P=" + str(P(a, b)))
