def input_phone():
    while True:
        p = input("Введіть номер телефона: ").strip()
        if not p.isdigit():
            print("Номер телефона має містити лише цифри. Спробуйте ще раз.\n")
            continue
        break
    return p



s = input("Введіть прізвище: ").strip()
n = input("Введіть ім'я: ").strip()
p = input_phone()
if not s or not n or not p:
    print("Не залишайте жодні поля порожніми. Спробуйте ще раз.\n")

if not p.isdigit():
    print("Номер телефона має містити лише цифри. Спробуйте ще раз.\n")

print("Спасибі")


s = input("Введіть прізвище: ").strip()
n = input("Введіть ім'я: ").strip()
p = input("Введіть номер телефона: ").strip()
if n or s or p:
    print("Спасибі")
else:
    print("Не залишайте жодні поля порожніми")

s = input("Введіть прізвище: ").strip()
n = input("Введіть ім'я: ").strip()
p = input("Введіть номер телефона(необов'язково): ").strip()
if not n or not s:
    print("Не залишайте ім'я та прізвище порожніми")
else:
    print("Спасибі")
