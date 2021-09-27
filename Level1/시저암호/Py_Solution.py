def solution(s, n):
    answer = ''
    c=0
    for i in s:
        if i != " " and  i.isupper() == True:
            if int(ord(i))+n <91:
                answer += chr(int(ord(i))+n)
            else:
                answer += chr(64+(int(ord(i))+n-90))
        elif i != " " and i.isupper() == False:
            if int(ord(i))+n <123:
                answer += chr(int(ord(i))+n)
            else:
                answer += chr(96+(int(ord(i))+n-122))
        else:
            answer += " "
            
            
    return answer