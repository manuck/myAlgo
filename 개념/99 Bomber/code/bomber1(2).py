
import sys
sys.stdin = open('bomber1_input.txt', 'r')
#sys.stdout = open('bomber1_output.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row, col = [0] * N, [0] * N

    for i in range(N):
        for j in range(N):
            row[i] += arr[i][j]
            col[i] += arr[j][i]

    Max = x = y = 0
    for i in range(N):
        for j in range(N):
            S = row[i] + col[j] - arr[i][j]
            if S >= Max:
                Max, x, y = S, i, j

    print('#{} {} {} {}'.format(tc, x, y, Max))
