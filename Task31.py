from datetime import datetime


def sort_by_birth_date(students):
    return tuple(
        sorted(
            students,
            key=lambda student: datetime.strptime(
                student[1], "%d.%m.%y"
            )
        )
    )


students = (
    ["Шевченко Тарас Григорович", "15.03.04"],
    ["Франко Олена Іванівна", "02.11.03"],
    ["Українець Андрій Петрович", "28.07.05"]
)

result = sort_by_birth_date(students)

print(result)