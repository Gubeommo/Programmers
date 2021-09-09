def solution(absolutes, signs):
    result=0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result += -1 * absolutes[i]       
    return result