import math
n = int(input())
x = -math.log(n)
for i in range(n):
    x += 1 / (i + 1)
print(x)