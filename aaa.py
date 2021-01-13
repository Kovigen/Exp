n = int(input())
if n < 2:
    print(n)
else:
    l = n + 1
    for i in range(2, n):
        if n%i == 0:
            l += i
    print(l)