def solution(record):
    answer = []
    user={}
    count=[]
    e=0
    l=0
    
    for i in range(len(record)):
        cmd = record[i].split()
        if cmd[0] == 'Enter':
            user[cmd[1]] = cmd[2]
            count.append(cmd[0])
            count.append(cmd[1])
        elif cmd[0] == 'Leave':        
            count.append(cmd[0])
            count.append(cmd[1])
        elif cmd[0] == 'Change':
            user[cmd[1]] = cmd[2]
    for j in count:
        if e == 1:
            answer.append("{}님이 들어왔습니다.".format(user[j]))
            e -=1
        elif l == 1:
            answer.append("{}님이 나갔습니다.".format(user[j]))
            l -=1
        if j == 'Enter':
            e +=1
        elif j == 'Leave':
            l +=1       
    return answer