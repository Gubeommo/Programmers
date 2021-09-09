def solution(s):
    dic={} 
    ch=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dic[ch[i]]= i
    print(dic)
    result=''
    chn=''
    for i in s:
        if i.isdigit():
             result = result + i
        elif i.isalpha():
                chn = chn+i
                if chn in dic.keys():
                    result = result+str(dic[chn])
                    chn = ''
    return int(result)