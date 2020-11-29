from datetime import datetime

def timer(funk):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = funk(*args, **kwargs)
        print(datetime.now() - start)
        return res
    return wrapper

@timer
def solution(number):
    x = 0
    for i in range(number):
       if i %3 ==0 or  i% 5==0:
           x += i
    return(x)

@timer
def solution1(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
print(solution1(10**7))
print(solution(10**7))
