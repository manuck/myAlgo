import sys
sys.stdin = open('2667_input.txt')


def dfs(x, y, cnt):
    global N
    g[y][x] = 0
    # for i in range(N):
    #     print(g[i])
    # print()
    # print(cnt)
    # print('__________________________')
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if g[ny][nx] == 1:
                cnt = dfs(nx, ny, cnt+1)
    # print(cnt)
    return cnt


N = int(input())
g = []
visited = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    a = list(map(int, input()))
    g.append(a)

# for i in range(N):
#     print(g[i])

res = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            res.append(dfs(j, i, 1))

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])