def solution(n, arr1, arr2):
    answer = []
    result = []
    text=""
    for i in range(n):   
        arr2[i] = int(bin(arr2[i])[2:])
        arr1[i] = int(bin(arr1[i])[2:])
        
        answer.append(str(arr1[i] + arr2[i]))
        if len(answer[i]) != n:
            for w in range(n - len(answer[i])):
                text += " "
        for z in answer[i]:
            print(text)
            if z == '1' or z == '2' :
                text +="#"
            else:
                text +=" "
        result.append(text)
        text=""
              
    return result