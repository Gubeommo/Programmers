def solution(n):
    #에라토스네스의 채
    # 2를 포함한 n까지 배열을 만든후 2를제외하고 2의배수 만든 배열삭제 1씩 커지면서 삭제
    cmd = set(range(2, n+1))
    for i in range(2, n+1):
        if i in cmd: 
            cmd -= set(range(i*2, n+1, i))
    answer = len(cmd)
    return answer