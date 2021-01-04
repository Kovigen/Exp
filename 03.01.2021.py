import math
a = float(input())
b = float(input())
c = float(input())
#0 = a * x**2 + c
d = b**2 - 4 * a * c
if d < 0:
    print('Нет корней')
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 == x2:
        print(x1)
    else:
        print(min(x1, x2))
        print(max(x1, x2))
