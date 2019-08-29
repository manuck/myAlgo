import sys
sys.stdin = open('2589_input.txt')


def bfs(x, y, cnt):
    global n, m, sol
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [[x, y, cnt]]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        x, y, ncnt = q.pop(0)
        # print(x, y ,ncnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m: continue
            if ny < 0 or ny >= n: continue

            if g[ny][nx] == 'L' and visited[ny][nx] == 0:
                visited[ny][nx] = 1 + ncnt
                q.append([nx, ny, ncnt+1])

    for i in range(n):
        for j in range(m):
            if visited[i][j] > sol:
                sol = visited[i][j]

    return sol


n, m = map(int, input().split())

g = []
# visited = [[0 for _ in range(m)]for _ in range(n)]
sol = 0
for i in range(n):
    g.append(list(input()))

# for i in range(n):
#     print(g[i])

for i in range(n):
    for j in range(m):
        if g[i][j] == 'L':
            bfs(j, i, 0)

print(sol)
# print(visited)
