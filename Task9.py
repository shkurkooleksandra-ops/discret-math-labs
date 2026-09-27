N = int(input("Введіть число N:"))
if N < 0:
    print("N повинна бути більше 0")
    N = int(input("Введіть число N:"))
reversed_number = 0
while N > 0:
    digit = N % 10
    reversed_number = reversed_number * 10 + digit
    N = N // 10
print("Число у зворотньому порядку:", reversed_number)