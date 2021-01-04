a = input()
b = input()
c = input()
la = len(a)
lb = len(b)
lc = len(c)

print(la, lb, lc)
d = min(la, lb, lc)
x = max(la, lb, lc)

if la != d and la != x:
    o = lc
elif lb != d and lb != x:
    o = lb
elif lc != d and lc != x:
    o = lc

print("d = ", d)
print("o = ", o)
print("x = ", x)
if (x - o) == (o - d):
    print('YES')
else:
    print('NO')