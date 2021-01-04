a = input()
b = input()
c = input()
n = min(len(a), len(b), len(c))
x = max(len(a), len(b), len(c))
if len(a) == n:
    print(a)
elif len(b) == n:
    print(b)
else:
    print(c)
if len(a) == x:
    print(a)
elif len(b) == x:
    print(b)
else:
    print(c)