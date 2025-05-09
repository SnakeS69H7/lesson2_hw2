import math 

def square(side):
    Square_area = side * side
    return math.ceil(Square_area) if not isinstance(side, int) else Square_area

side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")