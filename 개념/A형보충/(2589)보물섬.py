from collections import deque

L, W = map(int, input().split())
MAP = []
for _ in range(L):
    MAP.append(input())

diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0
for i in range(L):
    for j in range(W):
        if MAP[i][j] == 'W': continue
        visit = [[False] * W for _ in range(L)]
        D = [[0] * W for _ in range(L)]
        visit[i][j] = True
        Q = deque()
        Q.append((i, j))
        while len(Q):
            x, y = Q.popleft()
            for dx, dy in diff:
                tx, ty = x + dx, y + dy

                if tx < 0 or tx == L or ty < 0 or ty == W: continue
                if MAP[tx][ty] == 'W' or visit[tx][ty]: continue
                visit[tx][ty] = True
                D[tx][ty] = D[x][y] + 1
                Q.append((tx, ty))
            ans = max(ans, D[x][y])

print(ans)