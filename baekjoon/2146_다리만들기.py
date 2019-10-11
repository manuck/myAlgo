import sys
sys.stdin = open('2146_input.txt')

import collections

def bfs(y, x):
    q = collections.deque([])
    q.append((x, y))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visit[y][x] = 1
    g[y][x] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if g[ny][nx] != 0 and visit[ny][nx] == 0:
                q.append((nx, ny))
                visit[ny][nx] = 1
                g[ny][nx] = cnt


def bfs2(y, x, r, cnt):
    global ans
    q = collections.deque([])
    q.append((x, y, cnt))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visit[y][x] = 1
    while q:
        x, y, cnt = q.popleft()
        if cnt >= ans:
            return 9999
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if g[ny][nx] != r and g[ny][nx] != 0:
                return cnt
            if visit[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                visit[ny][nx] = 1



n = int(input())
g = []
visit = [[0 for _ in range(n)]for _ in range(n)]

for _ in range(n):
    g.append(list(map(int, input().split())))

cnt = 1
for i in range(n):
    for j in range(n):
        if g[i][j] != 0 and visit[i][j] == 0:
            bfs(i, j)
            cnt += 1

# for i in range(n):
#     print(g[i])
visit = [[0 for _ in range(n)]for _ in range(n)]
cnt = 0
ans = 9999
for i in range(n):
    for j in range(n):
        if g[i][j] != 0 and visit[i][j] == 0:
            res = bfs2(i, j, g[i][j], cnt)
            if ans > res:
                ans = res
print(ans)