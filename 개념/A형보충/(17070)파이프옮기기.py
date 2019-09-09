def DFS(x, y, dir):
    if x == N - 1 and y == N - 1:
        global ans
        ans += 1
        return

    if dir == 1:
        if y + 1 < N and wall[x][y + 1] == 0:
            DFS(x, y + 1, 1)
        if x + 1 < N and y + 1 < N and wall[x][y + 1] == 0 and wall[x + 1][y] == 0 and wall[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 3)
    elif dir == 2:
        if x + 1 < N and wall[x + 1][y] == 0:
            DFS(x + 1, y, 2)
        if x + 1 < N and y + 1 < N and wall[x][y + 1] == 0 and wall[x + 1][y] == 0 and wall[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 3)
    else:
        if y + 1 < N and wall[x][y + 1] == 0:
            DFS(x, y + 1, 1)
        if x + 1 < N and wall[x + 1][y] == 0:
            DFS(x + 1, y, 2)
        if x + 1 < N and y + 1 < N and wall[x][y + 1] == 0 and wall[x + 1][y] == 0 and wall[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 3)


N = int(input())
wall = [list(map(int, input().split())) for _ in range(N)]

ans = 0
DFS(0, 1, 1)
print(ans)