a = int(input())
b = a//100
c = (a//10)%10
d = a%10
k = min(b, c, d)
l = max(b, c, d)
n = b + c + d - (k + l)
if n == l - k:
    print('Число интересное')
else:
    print('Число неинтересное')
