n = int(input("Введіть кількість елементів: "))

array = []

for i in range(n):
    value = float(input(f"Введіть елемент {i + 1}: "))
    array.append(value)

average = sum(array) / n

for i in range(n):
    if array[i] > average:
        array[i] -= 18

print("Середнє значення:", average)
print("Змінений масив:", array)