class Employee:
    def __init__(self, name, age, position, pay):
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay

    def print_info(self):
        """Виводить інформацію про працівника."""
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Посада: {self.position}")
        print(f"Заробітна плата: {self.pay} грн")

    def give_raise(self, amount):
        """Збільшує заробітну плату на вказану суму."""
        self.pay += amount

    def change_position(self, new_position):
        """Змінює посаду працівника."""
        self.position = new_position

    def annual_pay(self):
        """Повертає річну заробітну плату."""
        return self.pay * 12

    def is_adult(self):
        """Перевіряє, чи працівнику є 18 років."""
        return self.age >= 18


employee = Employee(
    name="Олександра",
    age=17,
    position="Програміст",
    pay=30000
)

print("Початкова інформація:")
employee.print_info()

print("\nЧи повнолітній працівник?")
print(employee.is_adult())

employee.give_raise(5000)
employee.change_position("Старший програміст")

print("\nІнформація після змін:")
employee.print_info()

print("\nРічна заробітна плата:", employee.annual_pay(), "грн")