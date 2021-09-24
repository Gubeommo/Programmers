def solution(s):
    answer = ''
    count=0
    for i in s:
        if i != " ":
            if (count == 0 or count % 2 ==0):
                answer += i.upper()
                count +=1
            else:
                answer += i.lower()
                count +=1
        else:
            answer += i
            count =0   
    return answer