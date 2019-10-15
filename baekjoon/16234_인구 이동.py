import sys
sys.stdin = open('16234_input.txt')

import collections
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    global N, R, L
    q = collections.deque()
    point = [[y, x]]
    level = 0
    f = [y, x]
    visited[y][x] = 1
    q.append([y, x])

    while q:
        level += 1
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            if not visited[ny][nx]:
                if L <= abs(g[y][x]-g[ny][nx]) <= R:
                    point.append([ny, nx])
                    q.append([ny, nx])
                    visited[ny][nx] = 1
    if level == 1:
        visited[f[0]][f[1]] = 0
    else:
        pointAll.append(point)




N, L, R = map(int, input().split())

g = []
for i in range(N):
    g.append(list(map(int, input().split())))

# for i in range(N):
#     print(g[i])

ans = 0

while True:
    pointAll = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
    if not pointAll:
        break
    else:
        for points in pointAll:
            print(points)
            res = sum(map(lambda x: g[x[0]][x[1]], points)) // len(points)
            for q in points:
                g[q[0]][q[1]] = res
        ans += 1

print(ans)
