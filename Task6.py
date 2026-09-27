x = int(input("Введіть координату x:"))
y = int(input("Введіть координату y:"))
if 1 <= x <= 8 and 1 <= y <= 8:
    is_white = (x + y) % 2 == 1
    print(is_white)
    print("біла" if is_white else "чорна")
else:
    print("Введені координати (" + str(x) + "," + str(y)+"), допустимі значення (1,1)-(8,8)")
