def solution(dartResult):
    answer = 0
    result = []
    c=0
    
    for i in range(len(dartResult)):
        if c == 1:
            c=0
            continue
        if 47 < ord(dartResult[i]) < 58 and  dartResult[i+1] != '0':
            if dartResult[i+1] == 'S':
                result.append(int(dartResult[i]) **1)
            elif dartResult[i+1] == 'D':
                result.append(int(dartResult[i]) **2)
            elif dartResult[i+1] == 'T':
                result.append(int(dartResult[i]) **3)
        elif dartResult[i] == '1' and  dartResult[i+1] =='0':
            if dartResult[i+2] == 'S':
                result.append(10 **1)
            elif dartResult[i+2] == 'D':
                result.append(10 **2)
            elif dartResult[i+2] == 'T':
                result.append(10 **3)
            c +=1
            
        
        if (i ==2 and (dartResult[i] =='*' or dartResult[i]=='#')):
            if dartResult[i] =='*':
                result[0] = result[0] *2
            else:
                result[0] = result[0] * -1
        elif ( 2<i<6 and (dartResult[i] =='*' or dartResult[i]=='#')):
            if dartResult[i] =='*':
                result[0] = result[0] *2
                result[1] = result[1] *2
            else:
                result[1] = result[1] * -1
        elif ( i+1 == len(dartResult) and (dartResult[i] =='*' or dartResult[i]=='#')):
            if dartResult[i] =='*':
                result[1] = result[1] *2
                result[2] = result[2] *2
            else:
                result[2] = result[2] * -1
                
    for i in range(len(result)):
        answer += result[i]       
    return answer