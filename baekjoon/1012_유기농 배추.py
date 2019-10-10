import sys
sys.stdin = open('1012_input.txt')


def bfs(y, x):
    global m, n
    q = [(y, x)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visit = [[0 for _ in range(m)]for _ in range(n)]
    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m: continue
            if ny < 0 or ny >= n: continue
            if visit[ny][nx] == 0 and g[ny][nx] == 1:
                q.append([ny, nx])
                visit[ny][nx] = 1
                g[ny][nx] = 0


t = int(input())

for case in range(t):
    m, n, k = map(int, input().split())
    g = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        g[y][x] = 1

    # for i in range(n):
    #     print(g[i])
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)