import sys
sys.stdin = open('bomber4_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    S = 0
    for _ in range(M):
        x, y, r = map(int, input().split())
        xend = min(x + r, N)
        yend = min(y + r, N)
        for i in range(x, xend):
            for j in range(y, yend):
                S += arr[i][j]
                arr[i][j] = 0
    print('#{} {}'.format(tc, S))