N = int(input("Введіть число N:"))
isPrime = True
N>1
for divisor in range(2,N):
    if N % divisor == 0:
        isPrime = False
        break
print(isPrime)