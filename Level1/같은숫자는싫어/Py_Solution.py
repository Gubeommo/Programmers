def solution(arr):
    number= -1
    answer=[]   
    for i in arr:
        if number == -1:
            answer.append(i)
            number = i
        elif number != i :
            answer.append(i)
            number = i
        else:
            continue
    return answer