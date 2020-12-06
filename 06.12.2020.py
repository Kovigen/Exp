"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
 number of characters then it should replace the missing second character of the final pair with an underscore ('_').
 Завершите решение так, чтобы оно разбило строку на пары из двух символов. Если строка содержит нечетное количество
  символов, она должна заменить отсутствующий второй символ последней пары символом подчеркивания ('_').
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']"""
def solution(s):
    if len(s)%2 == 1:
        s+= "_"
    a = []
    for x in range(0,len(s),2):
        a.append(s[x:(x+2)])
    return a

print(solution("1231ыафыпфп"))
"""def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]"""
"""import re

def solution(s):
    return re.findall(".{2}", s + "_")"""