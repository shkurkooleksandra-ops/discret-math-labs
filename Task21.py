import random


def RandomArray(n):
    if n <= 0:
        return []

    array = []

    while len(array) < n:
        number = random.randint(1, n)
        # додаємо якщо число ще не траплялось
        if array.count(number) == 0:
            array.append(number)

    return array


N = int(input("Введіть N: "))

result = RandomArray(N)

print("Випадковий масив:", result)
