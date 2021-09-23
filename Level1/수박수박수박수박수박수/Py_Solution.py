def solution(n):
    result=""
    for i in range(n):
        if i == 0 :
            result +="수"
        elif (i+1)% 2 == 0:
            result +="박"
        else:
            result +="수"
    return result