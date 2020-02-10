import sys
sys.stdin = open('가장 큰 정사각형 찾기_input.txt')

t = int(input())
for case in range(t):
    n = int(input())
    board = []
    answer = 0
    for i in range(n):
        board.append((list(map(int, input().split()))))

    print(board)
    