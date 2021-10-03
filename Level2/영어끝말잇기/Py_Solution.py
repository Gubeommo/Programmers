def solution(n, words):
    answer = []
    a=0
    p=0
    w=1
    for i in range(len(words)):
        p +=1
        if p > n:
            w +=1
            p =1
        if i ==0:
            answer.append(words[i])
            continue
        if words[i] in answer or words[i-1][-1] != words[i][0] :
            a+=1
            break
        else:
            answer.append(words[i])            
    if p * w == len(words) and a == 0:
        p=0
        w=0
            
    return [p,w]