def solution(x, n):
    answer = []
    ch = x
    for i in range(n):
        answer.append(x)
        x += ch
    return answer