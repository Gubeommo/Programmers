def solution(board, moves):
    n = len(board[0])
    m=0
    c=0

    stack = []

    result = 0
    # 이중 배열을 사용하여 NxN 정사각형 구현 및 접근 
    for i in range(len(moves)):
        for j in range(n):
            if (board[j][moves[i]-1] != 0) :
                if ( m == 0 ):
                    stack.append(board[j][moves[i]-1])
                    m = board[j][moves[i]-1]
                    board[j][moves[i]-1] = 0
                    break
                elif (m ==board[j][moves[i]-1] ):
                    if len(stack) == 1:
                        result += 2
                        stack.clear()
                        board[j][moves[i]-1] = 0
                        m=0
                        break
                    else:
                        del stack[-1:]
                        m = stack[-1]
                        board[j][moves[i]-1] = 0
                        result += 2
                        break      
                else:
                    stack.append(board[j][moves[i]-1])
                    m = board[j][moves[i]-1]
                    board[j][moves[i]-1] = 0
                    break
            else:
                continue
                    
                
            
               
    return result