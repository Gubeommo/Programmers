def solution(n):
    number = 1
    isTrue = True
    
    while(isTrue):
        if ( n % number == 1 ):
            isTrue = False
        else:
            number +=1
    
    return number