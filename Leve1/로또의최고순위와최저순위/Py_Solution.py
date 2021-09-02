def solution(lottos, win_nums):   # 먼가 마음에 안들어 다음에 수정 예정(코드가 간결하지 못하다)
    answer = []
    n=0
    m=0
    for i in range(6):
        for j in range(6):
            if (lottos[i] == 0):
                m += 1
                break
            elif (lottos[i] == win_nums[j]):
                n +=1
                break
    while (len(answer) <2):
        if answer ==[]:
            if n+m > 0:
                if n+m ==6:
                    answer.append(1)
                elif n+m ==5:
                    answer.append(2)
                elif n+m ==4:
                    answer.append(3)
                elif n+m ==3:
                    answer.append(4)
                elif n+m ==2:
                    answer.append(5)
                elif n+m <2:
                    answer.append(6)
            else:
                answer.append(6)
        else:
            if (m != 6):    
                if n ==6:
                    answer.append(1)
                elif n ==5:
                    answer.append(2)
                elif n ==4:
                    answer.append(3)
                elif n ==3:
                    answer.append(4)
                elif n ==2:
                    answer.append(5)
                elif n <2:
                    answer.append(6)
            else:
                answer.append(6)
    return answer