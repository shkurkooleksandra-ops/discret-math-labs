import sys

X = 0
Y = 1


def input_point():
    user_input = input("Введіть координати x,y через кому: ")

    point = [int(n) for n in user_input.split(",")]
    if 1 <= point[X] <= 8 and 1 <= point[Y] <= 8:
        return point
    else:
        sys.exit("Введені координати (" + str(point[X]) + "," + str(point[Y]) + "), допустимі значення (1,1)-(8,8)")


p1 = input_point()
p2 = input_point()

queenAbleToMove = p1[X] == p2[X] or p1[Y] == p2[Y] or abs(p1[X] - p2[X]) == abs(p1[Y] - p2[Y])
print(queenAbleToMove)
