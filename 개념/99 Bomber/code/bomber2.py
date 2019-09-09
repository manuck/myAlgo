import sys
sys.stdin = open('bomber_input.txt', 'r')

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = a = b = 0

    for x in range(N):
        for y in range(N):
            S = arr[x][y]
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]

                while tx >= 0 and tx != N and ty >= 0 and ty != N:
                    S += arr[tx][ty]
                    tx, ty = tx + dx[i], ty + dy[i]

            if S >= Max:
                Max, a, b = S, x, y

    print('#{} {} {} {}'.format(tc, a, b, Max))
