def solution(d, budget):
    d.sort()
    c=0
    for i in d:
        if budget-i < 0:
            break
        budget -=  i
        c +=1   
    return c