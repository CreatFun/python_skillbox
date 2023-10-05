side = float(input())

perimeter = side * 4
square = side ** 2
diagonal = (side ** 2 + side ** 2) ** (1/2)

print(round(perimeter, 2), round(square, 2), round(diagonal,2))