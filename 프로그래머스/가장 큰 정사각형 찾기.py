import sys
sys.stdin = open('가장 큰 정사각형 찾기_input.txt')

t = int(input())
for case in range(t):
    print()
    K = int(input())
    board = []
    answer = 0
    for i in range(K):
        board.append((list(map(int, input().split()))))

    y = len(board)
    x = len(board[0])
    for i in range(y):
        for j in range(x):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], min(board[i - 1][j], board[i][j - 1])) + 1
            if answer < board[i][j]:
                answer = board[i][j]
    for i in range(y):
        print(board[i])

    print(answer ** 2)
