
import sys; sys.stdin = open('bomber1_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = x = y = 0
    for r in range(N):
        for c in range(N):
            S = 0
            for i in range(N):
                S += arr[r][i] + arr[i][c]
            S -= arr[r][c]
            if ans <= S:
                ans, x, y = S, r, c

    print('#{} {} {} {}'.format(tc, x, y, ans))
