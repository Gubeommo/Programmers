def solution(s):
    result = s.lower()
    a=0
    b=0
    for i in result:
        if i == "p":
            a += 1
        elif i == "y":
            b += 1
    if a != b:
        return False

    return True