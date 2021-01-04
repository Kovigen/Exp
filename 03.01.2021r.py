""""a = int(input())
for i in range(a):
    print("*" * (a - i))"""
a = int(input())
for i in range(a//2):
    print(" " * (a // 2 - i ) + "*" * (i * 2 + 1))
print("*" * a)
# todo по анологии нарисовать ёлочку
# TODO Дорисовать ромбик
