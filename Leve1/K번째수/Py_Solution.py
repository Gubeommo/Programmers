def solution(array, commands):
    result =[]
    for i in range(len(commands)):
        a = array[commands[i][0]-1:commands[i][1]]
        a.sort()
        result.append(a[commands[i][2]-1])
    return result