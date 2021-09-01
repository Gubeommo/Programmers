def solution(new_id):
    ch = "{}'!@#$%^&*[]()+=~`><:;/?," # 2간계 준비 작업
    p=".."
    b= True
    new_id.lower()
    result = new_id.lower()  # 1단계 단계임
    result = ''.join( x for x in  result if x not in ch) # 2단계 작업
    #문자열을 배제 하기 위해  ch에 나머지 문자 삽입
    while(b):
        if p in result:
            result = result.replace("..",".") # 3단계
        else:
            b= False
            
    if ( result !="" and result != "."):   #4단계            
        while( result[0] =="." or result[-1] =="."):
            if (result[0] =="."):
                result = result[1:]
            elif (result[-1] == "."):
                result = result[:-1] 
    else:
        result=""     
            
    if (result == ""): # 5단계
        result = "a"       
    if (len(result) >15):   # 6단계
        result = result[:15]
        if (result[-1] == "."):
            result = result[:-1]
    elif (len(result)< 3):  # 7단계
        while(len(result) <3):
            result = result + result[-1]
                  
    return result