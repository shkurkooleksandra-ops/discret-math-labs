import random


def RandomArray(array):
    if N <= 0:
        return []

    array = []

    while len(array) < N:
        number = random.randint(1, N)

        if array.count(number) == 0:
            array.append(number)

    return array


N = int(input("Введіть N: "))

result = RandomArray(N)

print("Випадковий масив:", result)
