a = int(input())
digit3 = a%10
digit2 = (a//10)%10
digit1 = a//100
x = digit3 + digit2 + digit1
y = digit3 * digit2 * digit1
print("Сумма цифр=", x)
print("Произведение цифр=", y)