a, b, c, = int(input()), int(input()), int(input())
if a == b and a == c:
    print('Равносторонний')
elif (a == b and a != c) or (a != b and a == c):
    print('Равнобедренный')
else:
    print('Разносторонний')

