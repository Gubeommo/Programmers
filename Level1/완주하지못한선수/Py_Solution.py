def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for a,b in zip(participant, completion):
        if a != b:
            return a
        
    return participant[-1]
"""
왜 sort와 zip를 썼는지
기본에 기본 코드 작성시 코드는 통과가 되지만 효율성에서 광탈...
그 이후 원인을 찾고자 알게된 시간복잡도
정렬을 하면 보다 시간복잡도가 빨라지게되고 zip이라는 함수는  내장함수로써 여러개의 순회가능한
객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플형태로 접근할수 있는 반복자를 반환함.. 무슨말이냐면
 participant 그리고 completion 는 리스트가 각 각 존재한다 zip()으로 인해 예제 1로 들어보면
 for a in zip(participant, completion):
        print(a) 
를 한다면 결과는  // ('eden','eden') ('kiki','kiki') 즉 정렬을 하고 zip을 통해 for문을 돌린다면 각자 맞는 문장에 일치
될것이고 알맞게 비교가  될것이다 즉 적은 코드로 많은 효율을 볼수 있다는의미이다.

"""