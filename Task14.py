number_five_found = False

for attempt in range(1, 6):
    number = int(input(f"Спроба {attempt}/5. Введіть число: "))

    if number == 5:
        print("Вітаю! Ви правильно вибрали число 5.")
        number_five_found = True
        break
    else:
        print("Неправильне число.")

if not number_five_found:
    print("Ви не ввели число 5 за п’ять спроб.")