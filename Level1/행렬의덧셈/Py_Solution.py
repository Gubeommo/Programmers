def solution(arr1, arr2):
    answer = []
    temp=[]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
            if len(temp) == len(arr1[i]):
                answer.append(temp)
                temp=[]
    return answer