A = int(input("Введіть число A:"))
B = int(input("Введіть число B:"))
if B<A:
    print("B повинна бути більше A")
    A = int(input("Введіть число A:"))
    B = int(input("Введіть число B:"))
for i in range(A,B+1):
    print(i)
    N = B - A + 1
print("Кількість цілих чисел:",N)
