import math


def square(side):
    square_area = side * side
    return math.ceil(square_area) if not isinstance(side, int) else square_area


side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")
