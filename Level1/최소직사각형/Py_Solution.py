def solution(sizes):
    result=[0,0]
    
    for i in sizes:
        i.sort()
        if (i[0] > result[0]):
            result[0] = i[0]
        if(i[1] > result[1]):
            result[1] = i[1]

    return result[0] * result[1]