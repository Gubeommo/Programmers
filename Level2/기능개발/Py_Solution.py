def solution(progresses, speeds):
    answer = []
    suma =[]
    count=0
    
    n=1
    for i in range(len(progresses)):
        while (progresses[i] < 100):
            progresses[i] += speeds[i]
            count += 1
        suma.append(count)
        count =0 
        
    for j in range(len(suma)):
        if count == 0:
            count += suma[0]            
        elif count < suma[j]:
            answer.append(n)
            n =1
            count = suma[j]
        else:
            n +=1
        if j == len(suma)-1:
            answer.append(n)

    return answer