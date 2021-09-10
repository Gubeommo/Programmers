def solution(priorities, location):
    if len(priorities) ==1:
            return 1
    vs=0
    pr= []
    count=[]
    a=0
    b=0
    for i in range(len(priorities)):
        count.append(i)
    while ( len(count)  > len(pr)):        
        vs = priorities.pop(0)        
        if len(priorities) == 1:
            if vs < priorities[0]:
                b=count.pop(a)
                count.append(b)
                priorities.append(vs)             
            else:   
                pr.append(vs)
                pr.append(priorities[0])
                print(pr)
                break
        if vs < max(priorities):
            b=count.pop(a)
            count.append(b)
            priorities.append(vs) 
        else:
            a +=1
            pr.append(vs)                 
    return count.index(location)+1