def solution(price, money, count):
    answer = 0
    standard = price
    for i in range(count):
        answer += price
        price += standard
    
    if(money < answer):
        return answer-money
    else:
        return 0