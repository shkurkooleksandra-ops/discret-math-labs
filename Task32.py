def normalize_name(name):
    return " ".join(name.split()).casefold()


def order_cost(price_list, order):
    products = {}

    for product in price_list:
        name, price, quantity = product
        products[normalize_name(name)] = product

    requested = {}

    for name, quantity in order:
        key = normalize_name(name)
        requested[key] = requested.get(key, 0) + quantity

    for name, quantity in requested.items():
        if name not in products:
            return -2

        if quantity > products[name][2]:
            return -1

    total = 0

    for name, quantity in requested.items():
        product = products[name]

        total += product[1] * quantity
        product[2] -= quantity

    return total


price_list = (
    ["Хліб", 34.9, 23],
    ["Молоко", 56.9, 5],
    ["Яблука", 21.5, 48]
)

order = (
    (" хліб ", 2),
    ("МОЛОКО", 1)
)

result = order_cost(price_list, order)

if result == -1:
    print("Недостатня кількість товару")
elif result == -2:
    print("Товар відсутній у прейскуранті")
else:
    print("Вартість замовлення:", result)
    print("Оновлений прейскурант:")

    for product in price_list:
        print(product)
