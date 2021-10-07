def solution(s):
    text=""
    low=[]
    up=[]
    for i in range(len(s)):
        if 96< ord(s[i])<123:
            low.append(s[i])
        else:
            up.append(s[i])
    low.sort(reverse=True)
    up.sort(reverse=True)
    for j in up:
        low.append(j)
    for h in low:
        text += h
    return text