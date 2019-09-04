import sys
sys.stdin = open('14503_input.txt')


def dfs(x, y, d):
    for i in range(4):
        d = turn(d)
        nx = x + d[1]
        ny = y + d[0]
        if g[ny][nx] == 0:
            g[ny][nx] = 2
            dfs(nx, ny, d)
            return
    bx = x - d[1]
    by = y - d[0]
    if g[by][bx] != 1:
        g[by][bx] = 2
        dfs(bx, by, d)


def turn(a):
    if a == [-1, 0]:        # 북 -> 서
        return [0, -1]
    elif a == [0, 1]:       # 동 -> 북
        return [-1, 0]
    elif a == [1, 0]:       # 남 -> 동
        return [0, 1]
    elif a == [0, -1]:      # 서 -> 남
        return [1, 0]

n, m = map(int, input().split())        # n x m 지도
y, x, d = map(int, input().split())     # 로봇 현재위치 (x, y) , 방향 d ( 0 = 북, 1 = 동, 2 = 남, 3 = 서)
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

d2 = [[-1, 0], [0, 1], [1, 0], [0, -1]]     # 북, 동, 남, 서

d = d2[d]
g[y][x] = 2

dfs(x, y, d)
res = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            res += 1

print(res)
