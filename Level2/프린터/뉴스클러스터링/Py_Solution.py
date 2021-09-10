import math

def solution(str1, str2):
    text1 = []
    text2 = []
    
    ins=0
    union=0
    result =0
    str1 = str1.upper()
    str2 = str2.upper()
    
    ## ord를 통해 소문자와 대문자의 범위를 알아낸다
    for i in range(len(str1)-1):
        if ( (65> ord(str1[i]) or 91 < ord(str1[i])) or ( 65 > ord(str1[i+1]) or 91 < ord(str1[i+1])) ):
            continue
        else:
            text1.append(str1[i]+str1[i+1])
            
        
    text1.sort()
    
    for j in range(len(str2)-1):
        if ( (65> ord(str2[j]) or 91 < ord(str2[j])) or ( 65 > ord(str2[j+1]) or 91 < ord(str2[j+1])) ):
            continue         
        else:
            text2.append(str2[j]+str2[j+1])
        
    text2.sort()
    print(text1)
    print(text2)  
    
    for z in text1:    
        for h in text2:
            if z == h:
                ins +=1
                text2.remove(h)         
                break
            
            
    union = len(text2) + (len(text1)-ins)+ins
    ## try except 문을 사용해서 예외처리를한다
    try:
        result = (ins / union) * 65536
    except:
        result = 65536
    
    result = math.trunc(result)
    answer = 0
    return result