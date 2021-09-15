def solution(s):
    result =''
    mid = len(s)/2
    if mid % 1 == 0 :
        result = s[int(mid -1):int(mid+1)]
    else:
        result = s[int(mid)]
    return result