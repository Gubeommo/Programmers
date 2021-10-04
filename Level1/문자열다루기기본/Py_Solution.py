def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6):
        if (s.isdigit() == True):
            print()
        else:
            answer = False
    else:
        answer = False
    return answer