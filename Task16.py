text = "Python"

print("Почаковий рядок:", text)

print("Перший символ:", text[0])
print("Третій символ:", text[2])

try:
    text[0] = "J"
except TypeError:
    print("Помилка: символи рялка не можна змінювати окремо.")

second_text = " programming"

combined_text = text + second_text
print("Об'єднаий рядок:", combined_text)

repeated_text = text * 10
print("Рядок, повторений 10 разів:", repeated_text)

symbol = "!"
position = 3

inserted_text = text[:position] + symbol + text[position:]
print("Рядок після вставки символу:", inserted_text)

position = 0
new_symbol = "J"

changed_text = text[:position] + new_symbol + text[position + 1:]
print("Новій рядок із заміненим символом:", changed_text)