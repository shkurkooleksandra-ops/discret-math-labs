N = int(input("Введіть число N:"))
isPrime = True
for divisor in range(2,N):
    if N % divisor == 0:
        isPrime = False
        break
print(isPrime)