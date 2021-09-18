def solution(a, b):
    n=0
    if a ==b:
        return a
    else:
        for i in range(min(a,b),max(a,b)+1):
            n += i
    return n