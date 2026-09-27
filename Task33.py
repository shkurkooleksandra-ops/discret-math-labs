class Student:
    """Зберігає особисті дані студента."""

    def __init__(
        self,
        name="John Doe",
        courses=None,
        phone="",
        email="",
        degree=""
    ):
        self.name = name
        self.courses = courses if courses is not None else []
        self.phone = phone
        self.email = email
        self.degree = degree

        print("Створено об’єкт для " + self.name)

    def print_details(self):
        """Виводить інформацію про студента."""

        print("\nІнформація про студента:")
        print("Ім’я:", self.name)
        print("Телефон:", self.phone)
        print("Email:", self.email)
        print("Освітній ступінь:", self.degree)
        print("Курси:", self.courses)

    def enroll(self, course):
        """Додає навчальний курс."""

        if course not in self.courses:
            self.courses.append(course)
            print("Курс додано:", course)
        else:
            print("Цей курс уже додано.")


student1 = Student(
    name="Mary",
    courses=["L548"],
    phone="+380671234567",
    email="mary@example.com",
    degree="Бакалавр"
)

print("Курси, які вивчає", student1.name)

new_course = input("Уведіть номер курсу або 'stop': ")

while new_course != "stop":
    student1.enroll(new_course)
    new_course = input("Уведіть номер курсу або 'stop': ")

student1.print_details()