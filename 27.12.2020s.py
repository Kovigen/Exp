x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
k = (abs(x2-x1)%2 + abs(y2-y1)%2 )%2
if k == 0:
    print('YES')
else:
    print('NO')