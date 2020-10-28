import sys
sys.stdin = open('크레인 인형뽑기 게임_input.txt')

board = []
for i in range(5):
    board.append(list(map(int, input().split())))
moves = list(map(int, input().split()))

for i in range(5):
    print(board[i])

print(moves)

answer = 0
n = len(board)
A = []
for i in moves:
    print(A)
    for j in range(n):
        if board[j][i-1] != 0:
            A.append(board[j][i-1])
            board[j][i - 1] = 0
            break
    if len(A) >= 2:
        if A[-1] == A[-2]:
            answer += 2
            A.pop()
            A.pop()

print(answer)