def solution(nums):
    abc = nums
    
    cm = int(len(abc)/2)
    cba = list(set(abc))
    bcm = int(len(cba))

    result =0
    if (cm >bcm or cm == bcm):
        result  = bcm
    else:
        result = cm

    
    return result