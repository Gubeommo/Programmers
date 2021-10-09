def solution(n, m):
    # 유클리드 호제법 적용 (최대공약수, 최소공배수)
    for i in range(max(n,m),n*m+1):
        if i % n == 0 and i % m ==0:
            res = i
            break
    if(n>m) : n,m = m,n

    while(m!=0):
        n=n%m
        n,m=m,n
    
    return n,res