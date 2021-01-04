import math
x = float(input())
a = math.radians(x)
c = math.sin(a) + math.cos(a) + math.tan(a) * math.tan(a)
print(c)