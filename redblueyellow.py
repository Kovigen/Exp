a = int(input())
if a == 0:
    print('зеленый')
if 1 <= a <= 10:
    if a%2 == 1:
        print('красный')
    if a%2 == 0:
        print('черный')
elif 10 < a <= 18:
    if a%2 == 1:
        print('черный')
    if a%2 == 0:
        print('красный')
elif 18 < a <= 28:
    if a%2 == 1:
        print('красный')
    if a%2 == 0:
        print('черный')
elif 28 < a <= 36:
    if a%2 == 1:
        print('черный')
    if a%2 == 1:
        print('красный')
if (a < 0) or (a > 36):
    print('ошибка ввода')