n = int(input())
flag = True
counte = 0
for i in range(1, n + 1):
    if flag:
        counte += i
    else:
        counte -= i
    flag = not(flag)
print(counte)