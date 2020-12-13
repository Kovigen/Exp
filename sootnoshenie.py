a = int(input())
b = a%10
c = (a//10)%10
d = (a//100)%10
e = a//1000
if b + e == d -c:
    print('ДА')
else:
    print('НЕТ')