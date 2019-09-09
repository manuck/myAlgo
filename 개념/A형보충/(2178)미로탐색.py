from collections import deque

N, M = map(int, input().split())

maze = [input() for _ in range(N)]
D = [[0] * M for _ in range(N)]

D[0][0] = 1
Q = deque()
Q.append((0, 0))


while Q:
    x, y = Q.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tx, ty = x + dx, y + dy

        if tx < 0 or tx == N or ty < 0 or ty == M: continue
        if maze[tx][ty] == '0' or D[tx][ty]: continue
        D[tx][ty] = D[x][y] + 1
        Q.append((tx, ty))

print(D[N - 1][M - 1])