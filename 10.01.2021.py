m = int(input())
n = int(input())
if m < n:
    for i in range(m, n, +1):
        print(i)
    print(n)
elif m > n:
    for i in range(m, n, -1):
        print(i)
    print(n)
else:
    print(m)