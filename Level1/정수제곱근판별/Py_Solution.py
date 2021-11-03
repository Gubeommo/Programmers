import math
## sqrt는 math에 제곱근을 구할때 쓰는 함수이고 math.sqrt(x) 는 x의 제곱근을 반환합니다.
def solution(n):
    if n % ((round(math.sqrt(n)))) !=0:
        return -1                
    else:
        return (round(math.sqrt(n))+1) *(round(math.sqrt(n))+1)