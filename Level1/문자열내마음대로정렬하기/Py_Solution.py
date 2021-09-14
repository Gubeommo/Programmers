def solution(strings, n):
    ##람다 사용하기
    strings.sort()
    return sorted(strings, key = lambda x:x[n])