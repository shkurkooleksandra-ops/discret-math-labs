def sort_ascending(array):
    return sorted(array)


def sort_descending(array):
    return sorted(array, reverse=True)


numbers = [71, 32, 93, 81, 15]

ascending = sort_ascending(numbers)
descending = sort_descending(numbers)

print("Початковий масив:", numbers)
print("За зростанням:", ascending)
print("За спаданням:", descending)